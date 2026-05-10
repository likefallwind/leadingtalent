"""Wikipedia 传记抓取。

策略：
  1. 若 CSV 提供了 wikipedia_title，直接取
  2. 否则按英文名搜索
  3. 取 extract（plain text 摘要，约前几段）
"""
from __future__ import annotations

import logging
from typing import Optional

from .base import HttpClient, truncate

log = logging.getLogger(__name__)


def fetch_wikipedia(
    client: HttpClient,
    title_or_name: str,
    rate: float,
    extract_chars: int = 4000,
    lang: str = "en",
) -> dict:
    if not title_or_name:
        return {"status": "skipped"}

    base = f"https://{lang}.wikipedia.org/w/api.php"
    # 用 query API 一次拿到 extract
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts|info",
        "inprop": "url",
        "explaintext": 1,
        "titles": title_or_name,
        "redirects": 1,
    }
    data = client.get(base, source="wikipedia", rate_limit_seconds=rate, params=params)
    if not data:
        return {"status": "fetch_failed"}

    pages = (data.get("query") or {}).get("pages") or {}
    for _, page in pages.items():
        if "missing" in page:
            # 尝试搜索
            return _search_then_fetch(client, title_or_name, rate, extract_chars, lang)
        return {
            "status": "ok",
            "title": page.get("title"),
            "url": page.get("fullurl"),
            "extract": truncate(page.get("extract"), extract_chars),
            "lang": lang,
        }
    return {"status": "no_page"}


def _search_then_fetch(client: HttpClient, q: str, rate: float, chars: int, lang: str) -> dict:
    base = f"https://{lang}.wikipedia.org/w/api.php"
    data = client.get(
        base,
        source="wikipedia",
        rate_limit_seconds=rate,
        params={"action": "opensearch", "search": q, "limit": 1, "format": "json"},
    )
    if not data or len(data) < 2 or not data[1]:
        return {"status": "not_found", "query": q}
    title = data[1][0]
    log.info(f"  [WIKI] '{q}' resolved → '{title}'")
    return fetch_wikipedia(client, title, rate, chars, lang)
