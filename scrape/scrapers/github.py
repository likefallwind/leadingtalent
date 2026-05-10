"""GitHub 用户与代码仓库抓取。

API 文档：https://docs.github.com/en/rest
速率限制：未认证 60req/h；带 token 5000req/h。强烈建议提供 token。
仅取 public 数据。
"""
from __future__ import annotations

import base64
import logging
from typing import Optional

from .base import HttpClient, truncate

log = logging.getLogger(__name__)

API = "https://api.github.com"


def fetch_github(
    client: HttpClient,
    username: Optional[str],
    rate: float,
    token: str,
    max_repos: int,
    readme_chars: int,
) -> dict:
    if not username:
        return {"status": "skipped", "reason": "no_username"}

    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    user = client.get(
        f"{API}/users/{username}",
        source="github",
        rate_limit_seconds=rate,
        headers=headers,
    )
    if not user:
        return {"status": "user_not_found", "username": username}

    # repos：按 stars 降序需要拉全量后排序，简单起见拉前 100 按 updated
    repos_raw = client.get(
        f"{API}/users/{username}/repos",
        source="github",
        rate_limit_seconds=rate,
        params={"per_page": 100, "sort": "updated", "type": "owner"},
        headers=headers,
    )
    repos_list = []
    if isinstance(repos_raw, list):
        # 按 star 排序取 top
        sorted_repos = sorted(repos_raw, key=lambda r: r.get("stargazers_count", 0), reverse=True)
        for r in sorted_repos[:max_repos]:
            if r.get("fork"):
                continue
            repo_info = {
                "name": r.get("name"),
                "full_name": r.get("full_name"),
                "description": r.get("description"),
                "stars": r.get("stargazers_count"),
                "forks": r.get("forks_count"),
                "language": r.get("language"),
                "topics": r.get("topics"),
                "created_at": r.get("created_at"),
                "updated_at": r.get("updated_at"),
                "url": r.get("html_url"),
            }
            # README（只拉前 N 个高 star repo 的，避免过多请求）
            if len(repos_list) < 10:
                readme = _fetch_readme(client, r.get("full_name"), rate, headers, readme_chars)
                if readme:
                    repo_info["readme_excerpt"] = readme
            repos_list.append(repo_info)

    return {
        "status": "ok",
        "username": username,
        "name": user.get("name"),
        "bio": user.get("bio"),
        "company": user.get("company"),
        "location": user.get("location"),
        "blog": user.get("blog"),
        "followers": user.get("followers"),
        "public_repos": user.get("public_repos"),
        "created_at": user.get("created_at"),
        "top_repos": repos_list,
    }


def _fetch_readme(
    client: HttpClient,
    full_name: Optional[str],
    rate: float,
    headers: dict,
    chars: int,
) -> Optional[str]:
    if not full_name:
        return None
    data = client.get(
        f"{API}/repos/{full_name}/readme",
        source="github",
        rate_limit_seconds=rate,
        headers=headers,
    )
    if not data or "content" not in data:
        return None
    try:
        decoded = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
        return truncate(decoded, chars)
    except Exception as e:
        log.warning(f"  [GH] decode readme failed for {full_name}: {e}")
        return None
