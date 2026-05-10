"""把 extract/ 输出的 720+ 份 JSON 标准化为三张扁平表。

输入：../extract/data/extractions/{pid}/{cond}__{model}__run{N}.json
输出：data/outputs/normalized.json，结构：

{
  "open_traits":     [{pid, name, model, run, trait_name, description, evidence, confidence}, ...],
  "seeded_v0":       [{pid, name, model, run, atom_id, atom_name, evidence_strength, level, evidence, reasoning}, ...],
  "supplementary":   [{pid, name, model, run, name, description, why_not_covered, evidence, confidence}, ...],
  "summary":         {...}
}
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

import yaml

from lib.io import load_json, write_json

log = logging.getLogger("01_load")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", stream=sys.stdout)


def parse_filename(name: str) -> tuple[str, str, int] | None:
    """文件名形如 'open__claude-sonnet__run2.json'。"""
    if not name.endswith(".json"):
        return None
    stem = name[:-5]
    parts = stem.split("__")
    if len(parts) != 3 or not parts[2].startswith("run"):
        return None
    cond = parts[0]
    model = parts[1]
    try:
        run = int(parts[2][3:])
    except ValueError:
        return None
    return cond, model, run


def safe_get(d, key, default=None):
    if not isinstance(d, dict):
        return default
    return d.get(key, default)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    args = ap.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))

    in_dir = Path(cfg["paths"]["extractions_dir"])
    out_path = Path(cfg["paths"]["outputs_dir"]) / "normalized.json"

    open_traits = []
    seeded_v0 = []
    supplementary = []
    parse_failures = 0
    files_seen = 0

    for person_dir in sorted(in_dir.iterdir()):
        if not person_dir.is_dir():
            continue
        pid = person_dir.name
        # 试着从某个文件里找 person_name
        pname = pid
        for f in person_dir.iterdir():
            d = load_json(f)
            if d and isinstance(d.get("data"), dict):
                pname = d["data"].get("person_name") or pname
                break

        for f in sorted(person_dir.iterdir()):
            parsed = parse_filename(f.name)
            if not parsed:
                continue
            cond, model, run = parsed
            files_seen += 1
            d = load_json(f)
            if d is None:
                parse_failures += 1
                continue
            meta = d.get("_meta", {})
            if meta.get("status") != "ok":
                parse_failures += 1
                continue
            data = d.get("data") or {}

            if cond == "open":
                for t in data.get("traits", []) or []:
                    if not isinstance(t, dict) or not t.get("name"):
                        continue
                    open_traits.append({
                        "pid": pid,
                        "name": pname,
                        "model": model,
                        "run": run,
                        "trait_name": t.get("name", "").strip(),
                        "description": t.get("description", "").strip(),
                        "evidence": t.get("evidence") or [],
                        "confidence": t.get("confidence", ""),
                    })
            elif cond == "seeded":
                for a in data.get("v0_assessment", []) or []:
                    if not isinstance(a, dict):
                        continue
                    seeded_v0.append({
                        "pid": pid,
                        "name": pname,
                        "model": model,
                        "run": run,
                        "atom_id": a.get("atom_id"),
                        "atom_name": (a.get("atom_name") or "").strip(),
                        "evidence_strength": (a.get("evidence_strength") or "").strip(),
                        "level": (a.get("level") or "").strip(),
                        "evidence": a.get("evidence") or [],
                        "reasoning": (a.get("reasoning") or "").strip(),
                    })
                for s in data.get("supplementary_traits", []) or []:
                    if not isinstance(s, dict) or not s.get("name"):
                        continue
                    supplementary.append({
                        "pid": pid,
                        "name": pname,
                        "model": model,
                        "run": run,
                        "trait_name": s.get("name", "").strip(),
                        "description": s.get("description", "").strip(),
                        "why_not_covered": s.get("why_not_covered", "").strip(),
                        "evidence": s.get("evidence") or [],
                        "confidence": s.get("confidence", ""),
                    })

    summary = {
        "files_seen": files_seen,
        "parse_failures": parse_failures,
        "open_traits_count": len(open_traits),
        "seeded_v0_rows": len(seeded_v0),
        "supplementary_count": len(supplementary),
        "unique_persons": len({r["pid"] for r in seeded_v0} | {r["pid"] for r in open_traits}),
    }
    log.info(f"标准化完成：{summary}")

    write_json(out_path, {
        "open_traits": open_traits,
        "seeded_v0": seeded_v0,
        "supplementary": supplementary,
        "summary": summary,
    })
    log.info(f"写入 {out_path}")


if __name__ == "__main__":
    main()
