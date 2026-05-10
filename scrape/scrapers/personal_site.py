"""个人主页抓取（仅当 CSV 提供 URL 时启用）。

策略简单粗暴：拉 HTML，去标签，截断。不追链接（避免无界爬取）。
适合主页是简洁文本风格的研究者（多数符合）。
"""
from __future__ import annotations

import logging
import re
from typing import Optional

from bs4 import BeautifulSoup

from .base import HttpClient, truncate

log = logging.getLogger(__name__)


def fetch_personal(
    client: HttpClient,
    url: Optional[str],
    rate: float,
    max_chars: int = 8000,
) -> dict:
    if not url:
        return {"status": "skipped"}

    text = client.get_text(url, source="personal", rate_limit_seconds=rate)
    if not text:
        return {"status": "fetch_failed", "url": url}

    try:
        soup = BeautifulSoup(text, "html.parser")
        # 去掉脚本/样式
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        plain = soup.get_text(separator="\n")
        plain = re.sub(r"\n\s*\n+", "\n\n", plain).strip()
        return {
            "status": "ok",
            "url": url,
            "title": soup.title.string.strip() if soup.title and soup.title.string else None,
            "content": truncate(plain, max_chars),
        }
    except Exception as e:
        log.warning(f"  [PSITE] parse failed {url}: {e}")
        return {"status": "parse_failed", "url": url}
