"""Semantic Scholar 学术发表抓取。

文档：https://api.semanticscholar.org/api-docs/graph
关键端点：
  - 搜索作者：GET /graph/v1/author/search?query=
  - 作者详情：GET /graph/v1/author/{id}
  - 作者论文：GET /graph/v1/author/{id}/papers

抓取策略：
  1. 若 CSV 已提供 semantic_scholar_id，直接用
  2. 否则按英文名搜索，取最高 paper count 的候选（disambiguation 简化处理）
  3. 拉作者详情（h-index, 总引用）
  4. 拉论文列表，按 citationCount 降序，取 top N
"""
from __future__ import annotations

import logging
from typing import Optional

from .base import HttpClient, truncate

log = logging.getLogger(__name__)

API = "https://api.semanticscholar.org/graph/v1"


def search_author(client: HttpClient, name: str, rate: float, api_key: str) -> Optional[str]:
    headers = {"x-api-key": api_key} if api_key else {}
    data = client.get(
        f"{API}/author/search",
        source="semantic_scholar",
        rate_limit_seconds=rate,
        params={"query": name, "limit": 5, "fields": "name,paperCount,hIndex,affiliations"},
        headers=headers,
    )
    if not data or not data.get("data"):
        return None
    # 启发式 disambiguation: 取 paperCount 最高的
    candidates = data["data"]
    best = max(candidates, key=lambda c: c.get("paperCount", 0) or 0)
    log.info(f"  [SS] '{name}' → {best.get('name')} (id={best['authorId']}, papers={best.get('paperCount')})")
    return best.get("authorId")


def fetch_author(
    client: HttpClient,
    name: str,
    seed_id: Optional[str],
    rate: float,
    api_key: str,
    max_papers: int,
    abstract_chars: int,
) -> dict:
    """抓取作者基础信息 + top-N 论文。返回结构化 dict。"""
    headers = {"x-api-key": api_key} if api_key else {}
    author_id = seed_id if seed_id else search_author(client, name, rate, api_key)
    if not author_id:
        return {"status": "not_found", "name": name}

    # 作者详情
    detail = client.get(
        f"{API}/author/{author_id}",
        source="semantic_scholar",
        rate_limit_seconds=rate,
        params={"fields": "name,affiliations,homepage,hIndex,citationCount,paperCount"},
        headers=headers,
    )
    if not detail:
        return {"status": "detail_failed", "author_id": author_id}

    # 论文列表（按引用数降序，需要分页或一次拉）
    papers_raw = client.get(
        f"{API}/author/{author_id}/papers",
        source="semantic_scholar",
        rate_limit_seconds=rate,
        params={
            "fields": "title,year,citationCount,abstract,venue,externalIds",
            "limit": max_papers,
        },
        headers=headers,
    )
    papers = []
    if papers_raw and papers_raw.get("data"):
        sorted_papers = sorted(
            papers_raw["data"],
            key=lambda p: p.get("citationCount", 0) or 0,
            reverse=True,
        )
        for p in sorted_papers[:max_papers]:
            papers.append(
                {
                    "title": p.get("title"),
                    "year": p.get("year"),
                    "citations": p.get("citationCount"),
                    "venue": p.get("venue"),
                    "abstract": truncate(p.get("abstract"), abstract_chars),
                    "arxiv_id": (p.get("externalIds") or {}).get("ArXiv"),
                }
            )

    return {
        "status": "ok",
        "author_id": author_id,
        "name": detail.get("name"),
        "affiliations": detail.get("affiliations"),
        "homepage": detail.get("homepage"),
        "h_index": detail.get("hIndex"),
        "total_citations": detail.get("citationCount"),
        "paper_count": detail.get("paperCount"),
        "top_papers": papers,
    }
