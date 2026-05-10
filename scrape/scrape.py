"""主入口：读取 names_seed.csv → 对每人调用各 scraper → 写入 traces/{id}/。

支持断点续跑：每人每源生成单独 JSON，已有则跳过（除非 --force）。
"""
from __future__ import annotations

import argparse
import csv
import logging
import os
import sys
from pathlib import Path

import yaml
from tqdm import tqdm

from scrapers.base import HttpClient, write_json, read_json
from scrapers import semantic_scholar, arxiv, github, wikipedia, personal_site


def load_config(path: Path) -> dict:
    cfg = yaml.safe_load(path.read_text(encoding="utf-8"))
    # 环境变量覆盖
    if os.environ.get("SS_API_KEY"):
        cfg["api_keys"]["semantic_scholar"] = os.environ["SS_API_KEY"]
    if os.environ.get("GITHUB_TOKEN"):
        cfg["api_keys"]["github"] = os.environ["GITHUB_TOKEN"]
    return cfg


def setup_logging(log_dir: Path):
    log_dir.mkdir(parents=True, exist_ok=True)
    fmt = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=fmt,
        handlers=[
            logging.FileHandler(log_dir / "scrape.log", encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def load_names(csv_path: Path) -> list[dict]:
    rows = []
    with csv_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append({k: (v.strip() if isinstance(v, str) else v) for k, v in row.items()})
    return rows


def scrape_one(person: dict, cfg: dict, client: HttpClient, force: bool):
    pid = person["id"]
    out_dir = Path(cfg["paths"]["output_dir"]) / pid
    out_dir.mkdir(parents=True, exist_ok=True)

    sources = cfg["sources"]
    keys = cfg["api_keys"]
    rate = cfg["rate_limit"]
    sc = cfg["scraping"]

    log = logging.getLogger("scrape")
    log.info(f"=== {pid} {person.get('chinese_name')} / {person.get('english_name')} ===")

    # 1. Semantic Scholar
    if sources.get("semantic_scholar"):
        out = out_dir / "semantic_scholar.json"
        if force or not out.exists():
            data = semantic_scholar.fetch_author(
                client,
                name=person.get("english_name") or person.get("chinese_name"),
                seed_id=person.get("semantic_scholar_id") or None,
                rate=rate["semantic_scholar_seconds"],
                api_key=keys.get("semantic_scholar", ""),
                max_papers=sc["max_papers_per_author"],
                abstract_chars=sc["abstract_chars"],
            )
            write_json(out, data)

    # 2. arXiv
    if sources.get("arxiv"):
        out = out_dir / "arxiv.json"
        if force or not out.exists():
            q = person.get("arxiv_query") or person.get("english_name", "").replace(" ", "+")
            data = arxiv.fetch_arxiv(
                client,
                query=q,
                rate=rate["arxiv_seconds"],
                max_results=sc["max_arxiv_per_author"],
                abstract_chars=sc["abstract_chars"],
            )
            write_json(out, data)

    # 3. GitHub
    if sources.get("github"):
        out = out_dir / "github.json"
        if force or not out.exists():
            data = github.fetch_github(
                client,
                username=person.get("github_username") or None,
                rate=rate["github_seconds"],
                token=keys.get("github", ""),
                max_repos=sc["max_repos_per_user"],
                readme_chars=sc["github_readme_chars"],
            )
            write_json(out, data)

    # 4. Wikipedia
    if sources.get("wikipedia"):
        out = out_dir / "wikipedia.json"
        if force or not out.exists():
            title = person.get("wikipedia_title") or person.get("english_name")
            data = wikipedia.fetch_wikipedia(
                client,
                title_or_name=title,
                rate=rate["wikipedia_seconds"],
            )
            write_json(out, data)

    # 5. 个人主页
    if sources.get("personal_site") and person.get("personal_url"):
        out = out_dir / "personal_site.json"
        if force or not out.exists():
            data = personal_site.fetch_personal(
                client,
                url=person["personal_url"],
                rate=1.0,
            )
            write_json(out, data)

    # 元信息（CSV 原始字段）
    write_json(out_dir / "meta.json", person)


def main():
    ap = argparse.ArgumentParser(description="抓取 AI 名人公开痕迹")
    ap.add_argument("--config", default="config.yaml")
    ap.add_argument("--force", action="store_true", help="忽略已存在文件，强制重抓")
    ap.add_argument("--only", help="只抓某 id（逗号分隔，如 P001,P020）")
    ap.add_argument("--limit", type=int, help="只跑前 N 个，用于测试")
    args = ap.parse_args()

    cfg = load_config(Path(args.config))
    setup_logging(Path(cfg["paths"]["log_dir"]))

    client = HttpClient(
        cache_dir=Path(cfg["paths"]["cache_dir"]),
        user_agent=cfg["http"]["user_agent"],
        timeout=cfg["http"]["timeout_seconds"],
        retry_max=cfg["http"]["retry_max"],
        retry_backoff=cfg["http"]["retry_backoff_seconds"],
    )

    names = load_names(Path(cfg["paths"]["names_csv"]))
    if args.only:
        wanted = set(args.only.split(","))
        names = [n for n in names if n["id"] in wanted]
    if args.limit:
        names = names[: args.limit]

    log = logging.getLogger("scrape")
    log.info(f"将抓取 {len(names)} 人")

    for person in tqdm(names, desc="人物"):
        try:
            scrape_one(person, cfg, client, force=args.force)
        except Exception as e:
            log.exception(f"{person.get('id')} 失败: {e}")

    log.info("全部完成")


if __name__ == "__main__":
    main()
