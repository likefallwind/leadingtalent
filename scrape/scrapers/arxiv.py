"""arXiv 预印本抓取。

API 文档：https://info.arxiv.org/help/api/user-manual.html
说明：返回 Atom feed，用 feedparser 解析。
arXiv 要求请求间隔 ≥ 3 秒。
"""
from __future__ import annotations

import logging
from typing import Optional
from urllib.parse import quote_plus

import feedparser

from .base import HttpClient, truncate

log = logging.getLogger(__name__)

API = "http://export.arxiv.org/api/query"


def fetch_arxiv(
    client: HttpClient,
    query: str,
    rate: float,
    max_results: int,
    abstract_chars: int,
) -> dict:
    """按作者名查询 arXiv，返回最近的 max_results 篇预印本。

    query 形如 'Geoffrey+Hinton'，对应 arXiv 字段 au:。
    """
    if not query:
        return {"status": "skipped", "reason": "no_query"}

    url = f"{API}?search_query=au:{quote_plus(query)}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    text = client.get_text(url, source="arxiv", rate_limit_seconds=rate)
    if not text:
        return {"status": "fetch_failed"}

    feed = feedparser.parse(text)
    papers = []
    for e in feed.entries:
        papers.append(
            {
                "arxiv_id": e.get("id", "").rsplit("/", 1)[-1],
                "title": (e.get("title") or "").strip().replace("\n", " "),
                "published": e.get("published"),
                "updated": e.get("updated"),
                "authors": [a.get("name") for a in (e.get("authors") or [])],
                "summary": truncate((e.get("summary") or "").strip().replace("\n", " "), abstract_chars),
                "primary_category": (e.get("arxiv_primary_category") or {}).get("term"),
                "link": e.get("link"),
            }
        )

    return {"status": "ok", "query": query, "count": len(papers), "papers": papers}
