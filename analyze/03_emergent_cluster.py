"""涌现 traits 聚类。

输入：normalized.json 里的 open_traits + supplementary
处理：
  1. 每条 trait 拼成 "name + description" 文本
  2. embedding（OpenAI text-embedding-3-small）
  3. 用 cosine 距离聚类（agglomerative，distance_threshold 切割）
  4. 每个簇：取最具代表性（最近质心）的若干 trait 作为代表名

输出：data/outputs/emergent_atoms.json
  [
    {
      "cluster_id": 0,
      "size": 17,                   # 包含 trait 数
      "unique_persons": 12,         # 涉及多少不同人物
      "open_count": 14,             # 来自开放抽取
      "supp_count": 3,              # 来自半结构补充
      "model_diversity": 3,         # 几个不同模型贡献
      "representative_names": [...], # 代表性 trait 名（前 5 条）
      "centroid_text": "...",       # 最接近质心的一条
      "members": [{trait_name, description, pid, model, run, source}]
    }
  ]
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

import numpy as np
import yaml
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.metrics import silhouette_score

from lib.io import load_json, write_json, EmbeddingClient

log = logging.getLogger("03_emergent")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", stream=sys.stdout)


def trait_text(t: dict) -> str:
    name = (t.get("trait_name") or "").strip()
    desc = (t.get("description") or "").strip()
    return f"{name}：{desc}" if desc else name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    args = ap.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))

    out_dir = Path(cfg["paths"]["outputs_dir"])
    norm = load_json(out_dir / "normalized.json")
    if not norm:
        log.error("normalized.json 不存在，先跑 01")
        return

    # 合并 open + supplementary，标注来源
    items = []
    for t in norm["open_traits"]:
        items.append({**t, "source": "open"})
    for t in norm["supplementary"]:
        items.append({**t, "source": "supp"})

    if not items:
        log.error("没有任何 trait")
        return

    # 过滤掉空名/空描述
    items = [t for t in items if (t.get("trait_name") or "").strip()]
    log.info(f"待聚类 trait 数：{len(items)}")

    # Embedding
    emb_client = EmbeddingClient(cfg)
    texts = [trait_text(t) for t in items]
    vecs = emb_client.embed(texts)
    log.info(f"embedding 完成: shape={vecs.shape}")

    # 聚类
    ec = cfg["emergent_clustering"]
    algo = ec.get("algorithm", "agglomerative")
    if algo == "agglomerative":
        # cosine + average linkage + distance_threshold
        # AgglomerativeClustering 需要 metric='cosine' 与 linkage='average'
        clustering = AgglomerativeClustering(
            n_clusters=None,
            metric="cosine",
            linkage="average",
            distance_threshold=ec["distance_threshold"],
        )
        labels = clustering.fit_predict(vecs)
    else:
        # k-means：在 k_range 内挑 silhouette 最高
        best = None
        for k in range(ec["k_range"][0], ec["k_range"][1] + 1):
            km = KMeans(n_clusters=k, n_init=10, random_state=42)
            lb = km.fit_predict(vecs)
            sc = silhouette_score(vecs, lb, metric="cosine") if len(set(lb)) > 1 else -1
            log.info(f"  k={k} silhouette={sc:.3f}")
            if best is None or sc > best[1]:
                best = (lb, sc, k)
        labels = best[0]
        log.info(f"选定 k={best[2]} silhouette={best[1]:.3f}")

    log.info(f"得到 {len(set(labels))} 个簇，最大簇大小 {max(np.bincount(labels))}")

    # 组织簇
    clusters: dict[int, list[int]] = {}
    for idx, lb in enumerate(labels):
        clusters.setdefault(int(lb), []).append(idx)

    min_size = ec["min_cluster_size"]
    out_clusters = []
    for cid, idxs in sorted(clusters.items(), key=lambda kv: -len(kv[1])):
        if len(idxs) < min_size:
            continue
        members = [items[i] for i in idxs]
        # 质心
        sub_vecs = vecs[idxs]
        centroid = sub_vecs.mean(axis=0)
        # 距离质心最近的几条
        dists = np.linalg.norm(sub_vecs - centroid, axis=1)
        order = np.argsort(dists)
        rep_indices = [idxs[i] for i in order[:5]]
        rep_names = [items[i]["trait_name"] for i in rep_indices]
        centroid_text = texts[rep_indices[0]]

        out_clusters.append({
            "cluster_id": cid,
            "size": len(members),
            "unique_persons": len({m["pid"] for m in members}),
            "open_count": sum(1 for m in members if m["source"] == "open"),
            "supp_count": sum(1 for m in members if m["source"] == "supp"),
            "model_diversity": len({m["model"] for m in members}),
            "representative_names": rep_names,
            "centroid_text": centroid_text,
            "members": [
                {
                    "pid": m["pid"], "name": m["name"],
                    "model": m["model"], "run": m["run"], "source": m["source"],
                    "trait_name": m["trait_name"], "description": m["description"],
                    "evidence": m.get("evidence", []),
                }
                for m in members
            ],
        })

    log.info(f"保留 size >= {min_size} 的簇：{len(out_clusters)}")
    log.info("Top 10 簇（按规模）：")
    for c in out_clusters[:10]:
        log.info(
            f"  #{c['cluster_id']:>3} size={c['size']:>3} persons={c['unique_persons']:>3} "
            f"models={c['model_diversity']} | {c['representative_names'][:3]}"
        )

    write_json(out_dir / "emergent_atoms.json", {
        "config_used": ec,
        "total_traits_input": len(items),
        "total_clusters": len(set(labels)),
        "kept_clusters": len(out_clusters),
        "clusters": out_clusters,
    })


if __name__ == "__main__":
    main()
