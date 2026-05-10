"""Round 1 双抽取主入口。

对每位名人：
  for condition in (open, seeded):
      for model in enabled_models:
          for run_idx in 1..runs_per_combo:
              如果输出已存在 → 跳过（断点续跑）
              否则：组装 prompt → 调 LLM → 解析 JSON → 写盘

输出结构：
  data/extractions/
    └── P001/
        ├── open__claude-sonnet__run1.json
        ├── open__claude-sonnet__run2.json
        ├── open__gpt-4o__run1.json
        ├── seeded__claude-sonnet__run1.json
        └── ...

每份 JSON 是 LLM 的原始结构化输出（已尝试 JSON 解析；解析失败保留原文 + 错误标注）。
"""
from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from dataclasses import asdict
from pathlib import Path
from typing import Optional

import yaml
from tqdm import tqdm

from llm import ModelConfig, build_client, call_with_retry, LLMError

log = logging.getLogger("extract")


def setup_logging(log_dir: Path):
    log_dir.mkdir(parents=True, exist_ok=True)
    fmt = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=fmt,
        handlers=[
            logging.FileHandler(log_dir / "extract.log", encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def load_config(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_prompt(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def truncate_middle(s: str, max_chars: int) -> str:
    """profile.md 太长时截掉中间，保头保尾。"""
    if len(s) <= max_chars:
        return s
    half = max_chars // 2
    return s[:half] + f"\n\n…[中段省略 {len(s)-max_chars} 字]…\n\n" + s[-half:]


def extract_json(text: str) -> tuple[Optional[dict], Optional[str]]:
    """尝试从 LLM 输出里解析 JSON，返回 (parsed, error_message)。

    宽容处理：
      - 直接 json.loads
      - 失败则尝试剥离 ```json``` 包裹
      - 再失败则返回原文 + error
    """
    text = text.strip()
    # 直接尝试
    try:
        return json.loads(text), None
    except json.JSONDecodeError:
        pass
    # 剥 ```json ... ```
    m = re.search(r"```(?:json)?\s*(.+?)\s*```", text, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(1)), None
        except json.JSONDecodeError as e:
            return None, f"json fenced parse failed: {e}"
    # 取第一个 { 到最后一个 } 之间
    s, e = text.find("{"), text.rfind("}")
    if s != -1 and e != -1 and e > s:
        try:
            return json.loads(text[s : e + 1]), None
        except json.JSONDecodeError as e2:
            return None, f"brace-extract failed: {e2}"
    return None, "no json structure found"


def render_prompt(template: str, profile_md: str, person_id: str, person_name: str) -> tuple[str, str]:
    """填充模板。返回 (system_prompt, user_prompt)。

    设计：system 留空（或固定一句），所有任务说明放 user，便于跨 provider 一致。
    """
    user = (
        template.replace("{person_id}", person_id)
        .replace("{person_name}", person_name)
        .replace("{profile_md}", profile_md)
    )
    system = "你是一位严谨的研究助手，输出严格遵守要求的 JSON。"
    return system, user


def process_one(
    person_dir: Path,
    out_dir: Path,
    cfg: dict,
    prompts: dict,
    clients: dict,
    force: bool,
):
    pid = person_dir.name
    profile_path = person_dir / "profile.md"
    meta_path = person_dir / "meta.json"
    if not profile_path.exists():
        log.warning(f"{pid}: 无 profile.md，跳过（先跑 scrape/aggregate.py）")
        return
    profile = profile_path.read_text(encoding="utf-8")
    profile = truncate_middle(profile, cfg["profile"]["max_chars"])
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}
    name = meta.get("chinese_name") or meta.get("english_name") or pid

    person_out = out_dir / pid
    person_out.mkdir(parents=True, exist_ok=True)

    runs = cfg["runs_per_combo"]
    llm_cfg = cfg["llm"]

    for cond_name, cond in cfg["conditions"].items():
        if not cond.get("enabled", True):
            continue
        prompt_tpl = prompts[cond_name]
        system_prompt, user_prompt = render_prompt(prompt_tpl, profile, pid, name)

        for client_id, client in clients.items():
            for run_idx in range(1, runs + 1):
                fname = f"{cond_name}__{client_id}__run{run_idx}.json"
                fpath = person_out / fname
                if fpath.exists() and not force:
                    continue

                log.info(f"  {pid} | {cond_name} | {client_id} | run {run_idx}")
                raw = call_with_retry(
                    client,
                    system_prompt=system_prompt,
                    user_prompt=user_prompt,
                    temperature=llm_cfg["temperature"],
                    max_tokens=llm_cfg["max_tokens"],
                    timeout=llm_cfg["timeout_seconds"],
                    retry_max=llm_cfg["retry_max"],
                    retry_backoff=llm_cfg["retry_backoff_seconds"],
                )
                if raw is None:
                    fpath.write_text(
                        json.dumps(
                            {
                                "_meta": {
                                    "person_id": pid,
                                    "condition": cond_name,
                                    "model": client_id,
                                    "run": run_idx,
                                    "status": "llm_failed",
                                }
                            },
                            ensure_ascii=False,
                            indent=2,
                        ),
                        encoding="utf-8",
                    )
                    continue

                parsed, err = extract_json(raw)
                output = {
                    "_meta": {
                        "person_id": pid,
                        "condition": cond_name,
                        "model": client_id,
                        "run": run_idx,
                        "status": "ok" if parsed else "json_parse_failed",
                        "json_error": err,
                    },
                    "raw": raw if not parsed else None,
                    "data": parsed,
                }
                fpath.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")


def build_clients(cfg: dict) -> dict:
    out = {}
    for m in cfg["models"]:
        if not m.get("enabled", True):
            continue
        mc = ModelConfig(**{k: m.get(k, "") for k in ("id", "provider", "model", "api_key_env", "base_url", "enabled")})
        try:
            out[mc.id] = build_client(mc)
            log.info(f"已启用模型: {mc.id} ({mc.provider} / {mc.model})")
        except LLMError as e:
            log.warning(f"跳过模型 {mc.id}: {e}")
    if not out:
        raise LLMError("无可用模型；检查 config.yaml 与 API key 环境变量")
    return out


def main():
    ap = argparse.ArgumentParser(description="Round 1 双抽取（开放式 + 半结构式）")
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--force", action="store_true", help="忽略已存在文件，强制重跑")
    ap.add_argument("--only", help="只处理指定 ID，逗号分隔（如 P001,P020）")
    ap.add_argument("--limit", type=int, help="只跑前 N 个，调试用")
    args = ap.parse_args()

    cfg = load_config(Path(args.config))
    setup_logging(Path(cfg["paths"]["log_dir"]))

    profiles_dir = Path(cfg["paths"]["profiles_dir"])
    out_dir = Path(cfg["paths"]["output_dir"])
    prompts_dir = Path(cfg["paths"]["prompts_dir"])

    prompts = {
        cond_name: load_prompt(prompts_dir / cond["prompt_file"])
        for cond_name, cond in cfg["conditions"].items()
        if cond.get("enabled", True)
    }

    clients = build_clients(cfg)

    persons = sorted([p for p in profiles_dir.iterdir() if p.is_dir()])
    if args.only:
        wanted = set(args.only.split(","))
        persons = [p for p in persons if p.name in wanted]
    if args.limit:
        persons = persons[: args.limit]

    log.info(f"将处理 {len(persons)} 人 × {len(prompts)} 条件 × {len(clients)} 模型 × {cfg['runs_per_combo']} runs")
    log.info(f"= {len(persons) * len(prompts) * len(clients) * cfg['runs_per_combo']} 次 LLM 调用")

    for person_dir in tqdm(persons, desc="人物"):
        try:
            process_one(person_dir, out_dir, cfg, prompts, clients, force=args.force)
        except Exception as e:
            log.exception(f"{person_dir.name} 失败: {e}")

    log.info("Round 1 抽取完成")


if __name__ == "__main__":
    main()
