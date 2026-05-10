"""共享 I/O 与 embedding 工具。"""
from __future__ import annotations

import hashlib
import json
import logging
import os
import time
from pathlib import Path
from typing import Iterable, Optional

import numpy as np

log = logging.getLogger(__name__)


def load_json(path: Path) -> Optional[dict]:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        log.warning(f"读取 JSON 失败 {path}: {e}")
        return None


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


# --- Embedding 客户端（带缓存）-----------------------------------

class EmbeddingClient:
    """OpenAI 兼容 embedding API + 磁盘缓存。

    缓存 key = hash(model + text)；不同模型互相独立。
    """

    def __init__(self, cfg: dict):
        from openai import OpenAI
        emb_cfg = cfg["embedding"]
        api_key = os.environ.get(emb_cfg["api_key_env"])
        if not api_key:
            raise RuntimeError(f"环境变量未设置: {emb_cfg['api_key_env']}")
        self.client = OpenAI(api_key=api_key, base_url=emb_cfg.get("base_url") or None)
        self.model = emb_cfg["model"]
        self.batch_size = emb_cfg.get("batch_size", 100)
        self.cache_path = Path(emb_cfg["cache_file"])
        self._cache: dict[str, list[float]] = {}
        if self.cache_path.exists():
            try:
                self._cache = json.loads(self.cache_path.read_text(encoding="utf-8"))
            except Exception:
                self._cache = {}

    def _key(self, text: str) -> str:
        h = hashlib.sha256()
        h.update(self.model.encode())
        h.update(b"||")
        h.update(text.encode("utf-8"))
        return h.hexdigest()[:24]

    def _flush_cache(self):
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        self.cache_path.write_text(json.dumps(self._cache, ensure_ascii=False), encoding="utf-8")

    def embed(self, texts: list[str]) -> np.ndarray:
        """返回 (len(texts), dim) numpy array，命中缓存的不重算。"""
        results: list[Optional[list[float]]] = [None] * len(texts)
        to_query: list[tuple[int, str]] = []
        for i, t in enumerate(texts):
            k = self._key(t)
            cached = self._cache.get(k)
            if cached:
                results[i] = cached
            else:
                to_query.append((i, t))

        if to_query:
            log.info(f"  embedding {len(to_query)} 条（已缓存 {len(texts) - len(to_query)} 条）")
            for batch_start in range(0, len(to_query), self.batch_size):
                batch = to_query[batch_start : batch_start + self.batch_size]
                batch_texts = [t for _, t in batch]
                # 简单重试
                for attempt in range(3):
                    try:
                        resp = self.client.embeddings.create(model=self.model, input=batch_texts)
                        break
                    except Exception as e:
                        if attempt == 2:
                            raise
                        log.warning(f"  embed batch failed, retry: {e}")
                        time.sleep(2 ** attempt * 5)
                for (idx, text), item in zip(batch, resp.data):
                    vec = item.embedding
                    self._cache[self._key(text)] = vec
                    results[idx] = vec
            self._flush_cache()

        return np.array(results, dtype=np.float32)


def cosine_sim(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """a: (n,d) b: (m,d) → (n,m) 余弦相似度。"""
    an = a / (np.linalg.norm(a, axis=1, keepdims=True) + 1e-12)
    bn = b / (np.linalg.norm(b, axis=1, keepdims=True) + 1e-12)
    return an @ bn.T
