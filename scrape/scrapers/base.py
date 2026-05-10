"""通用工具：HTTP、缓存、限速、重试。

设计要点：
- 所有 HTTP 响应按 URL 缓存到磁盘（hash 命名），下次运行直接命中
- 限速器按 source 分别计数，避免触发 API 速率限制
- 失败自动指数退避重试
"""
from __future__ import annotations

import hashlib
import json
import logging
import os
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import requests

log = logging.getLogger(__name__)


@dataclass
class HttpClient:
    """带缓存与限速的 HTTP 客户端。"""

    cache_dir: Path
    user_agent: str
    timeout: int = 30
    retry_max: int = 3
    retry_backoff: int = 5

    def __post_init__(self):
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._last_call: dict[str, float] = {}

    def _cache_key(self, url: str, params: Optional[dict]) -> str:
        h = hashlib.sha256()
        h.update(url.encode())
        if params:
            h.update(json.dumps(params, sort_keys=True).encode())
        return h.hexdigest()[:16]

    def _wait(self, source: str, min_interval: float):
        last = self._last_call.get(source, 0.0)
        delta = time.time() - last
        if delta < min_interval:
            time.sleep(min_interval - delta)
        self._last_call[source] = time.time()

    def get(
        self,
        url: str,
        source: str,
        rate_limit_seconds: float,
        params: Optional[dict] = None,
        headers: Optional[dict] = None,
        accept_json: bool = True,
        force_refresh: bool = False,
    ) -> Optional[dict | str]:
        """GET 请求。命中缓存直接返回；否则限速、重试、写缓存。"""
        key = self._cache_key(url, params)
        cache_file = self.cache_dir / f"{source}_{key}.json"
        if cache_file.exists() and not force_refresh:
            try:
                return json.loads(cache_file.read_text(encoding="utf-8"))
            except Exception:
                pass  # 缓存损坏则重抓

        h = {"User-Agent": self.user_agent, "Accept": "application/json" if accept_json else "*/*"}
        if headers:
            h.update(headers)

        last_err: Optional[Exception] = None
        for attempt in range(self.retry_max):
            try:
                self._wait(source, rate_limit_seconds)
                r = requests.get(url, params=params, headers=h, timeout=self.timeout)
                if r.status_code == 429:
                    backoff = self.retry_backoff * (2**attempt)
                    log.warning(f"[{source}] 429 rate-limited, sleeping {backoff}s")
                    time.sleep(backoff)
                    continue
                if r.status_code >= 500:
                    backoff = self.retry_backoff * (2**attempt)
                    log.warning(f"[{source}] {r.status_code}, sleeping {backoff}s")
                    time.sleep(backoff)
                    continue
                if r.status_code == 404:
                    return None
                r.raise_for_status()
                data = r.json() if accept_json else r.text
                cache_file.write_text(
                    json.dumps(data, ensure_ascii=False) if accept_json else json.dumps({"_text": data}),
                    encoding="utf-8",
                )
                return data
            except requests.RequestException as e:
                last_err = e
                backoff = self.retry_backoff * (2**attempt)
                log.warning(f"[{source}] {url} attempt {attempt+1} failed: {e}; sleep {backoff}s")
                time.sleep(backoff)
        log.error(f"[{source}] {url} all retries failed: {last_err}")
        return None

    def get_text(self, url: str, source: str, rate_limit_seconds: float, **kw) -> Optional[str]:
        result = self.get(url, source, rate_limit_seconds, accept_json=False, **kw)
        if isinstance(result, dict) and "_text" in result:
            return result["_text"]
        return result if isinstance(result, str) else None


def truncate(s: Optional[str], n: int) -> str:
    if not s:
        return ""
    return s if len(s) <= n else s[:n].rstrip() + "…"


def write_json(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def read_json(path: Path) -> Optional[dict]:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None
