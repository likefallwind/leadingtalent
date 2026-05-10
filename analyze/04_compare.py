"""V0 ↔ 涌现集 三方对照（核心步骤，产出主要研究价值）。

输入：
  - data/outputs/v0_matrix.json  （V0 矩阵，含每原子的总体可观测度）
  - data/outputs/emergent_atoms.json （涌现簇）

处理：
  1. V0 12 个原子 + 每个涌现簇都做 embedding
  2. 计算 V0 × 涌现 相似度矩阵
  3. 对每个 V0 原子：
     - 找最相似涌现簇 E*；记录 sim 值
     - 结合 V0 矩阵里的 level_mean
     - 决定状态：确证 / 证伪 / 细化
  4. 对每个涌现簇：
     - 若没 V0 原子 sim 超阈值 → 发现（potential new atom）
     - 若有 → 已被覆盖

输出：data/outputs/comparison_matrix.json
  分四张表：confirmed / discovered / refuted / refined / unclear
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

import numpy as np
import yaml

from lib.io import load_json, write_json, EmbeddingClient, cosine_sim
from lib.v0 import V0_ATOMS, atom_text_for_embedding

log = logging.getLogger("04_compare")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", stream=sys.stdout)


def cluster_text(c: dict) -> str:
    """涌现簇的代表文本。"""
    names = c.get("representative_names", [])
    centroid = c.get("centroid_text", "")
    return f"{' / '.join(names[:3])}：{centroid}" if names else centroid


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    args = ap.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))

    out_dir = Path(cfg["paths"]["outputs_dir"])
    v0_data = load_json(out_dir / "v0_matrix.json")
    em_data = load_json(out_dir / "emergent_atoms.json")
    if not v0_data or not em_data:
        log.error("缺前置产物，先跑 02 和 03")
        return

    cmp_cfg = cfg["compare"]

    # 1) embedding
    emb_client = EmbeddingClient(cfg)
    v0_texts = [atom_text_for_embedding(a) for a in V0_ATOMS]
    em_clusters = em_data["clusters"]
    em_texts = [cluster_text(c) for c in em_clusters]
    v0_vec = emb_client.embed(v0_texts)
    em_vec = emb_client.embed(em_texts)

    # 2) 相似度矩阵
    sim = cosine_sim(v0_vec, em_vec)  # (12, K)

    # V0 原子总体可观测度（从 02 step）
    atom_score: dict[int, float] = {}
    for s in v0_data["atom_stats"]:
        atom_score[s["atom_id"]] = s["level_mean"] if s["level_mean"] is not None else 0.0

    # 3) 每个 V0 原子的状态
    v0_findings = []
    matched_clusters: set[int] = set()  # 被某 V0 sim 命中的簇
    for i, a in enumerate(V0_ATOMS):
        sims = sim[i]  # (K,)
        order = np.argsort(-sims)
        best_j = int(order[0])
        best_sim = float(sims[best_j])
        score = atom_score.get(a["id"], 0.0)

        # 决策
        if best_sim >= cmp_cfg["similarity_high"]:
            matched_clusters.add(best_j)
            if score >= cmp_cfg["v0_strength_threshold"]:
                status = "确证"
            else:
                # 涌现里有，但 V0 评分中位偏低 → 可能定义未对齐
                status = "细化"
        elif best_sim < cmp_cfg["similarity_low"]:
            if score < cmp_cfg["v0_strength_threshold"]:
                status = "证伪"
            else:
                # V0 评分高但涌现里找不到 → 概念可能与 emergent 表达不同（少见但可能）
                status = "细化"
        else:
            status = "待审"  # 中间区

        # top-3 涌现簇
        top3 = []
        for j in order[:3]:
            j = int(j)
            top3.append({
                "cluster_id": em_clusters[j]["cluster_id"],
                "similarity": float(sims[j]),
                "size": em_clusters[j]["size"],
                "representative_names": em_clusters[j]["representative_names"][:3],
            })

        v0_findings.append({
            "atom_id": a["id"],
            "atom_name": a["name"],
            "cluster": a["cluster"],
            "v0_level_mean": score,
            "best_match_cluster_id": em_clusters[best_j]["cluster_id"] if em_clusters else None,
            "best_match_similarity": best_sim,
            "top3_emergent": top3,
            "status": status,
        })

    # 4) 涌现簇里没被任何 V0 高度匹配的 → 发现
    discovered = []
    for j, c in enumerate(em_clusters):
        # 与所有 V0 的最大相似度
        max_sim = float(sim[:, j].max())
        if max_sim < cmp_cfg["similarity_high"]:
            best_v0_idx = int(np.argmax(sim[:, j]))
            discovered.append({
                "cluster_id": c["cluster_id"],
                "size": c["size"],
                "unique_persons": c["unique_persons"],
                "model_diversity": c["model_diversity"],
                "representative_names": c["representative_names"][:5],
                "centroid_text": c["centroid_text"],
                "max_sim_to_v0": max_sim,
                "closest_v0": V0_ATOMS[best_v0_idx]["name"],
            })

    # 按状态归类
    by_status = {"确证": [], "细化": [], "证伪": [], "待审": []}
    for f in v0_findings:
        by_status[f["status"]].append(f)

    # 排序：discovered 按 size 降序
    discovered.sort(key=lambda x: (x["size"], x["unique_persons"]), reverse=True)

    log.info("=== V0 原子状态 ===")
    for s in ["确证", "细化", "证伪", "待审"]:
        log.info(f"  {s}: {len(by_status[s])} 个")
        for f in by_status[s]:
            log.info(
                f"    [{f['atom_id']:2d}] {f['atom_name']:<14} "
                f"v0_level={f['v0_level_mean']:.2f} sim={f['best_match_similarity']:.2f}"
            )

    log.info(f"\n=== 发现的潜在新原子（{len(discovered)} 个）===")
    for d in discovered[:15]:
        log.info(
            f"  size={d['size']:>3} persons={d['unique_persons']:>3} "
            f"models={d['model_diversity']} max_sim_v0={d['max_sim_to_v0']:.2f} | "
            f"{d['representative_names'][:3]}"
        )

    write_json(out_dir / "comparison_matrix.json", {
        "config_used": cmp_cfg,
        "v0_findings": v0_findings,
        "discovered": discovered,
        "by_status": {k: [f["atom_id"] for f in v] for k, v in by_status.items()},
        "summary": {
            "total_v0_atoms": len(V0_ATOMS),
            "确证": len(by_status["确证"]),
            "细化": len(by_status["细化"]),
            "证伪": len(by_status["证伪"]),
            "待审": len(by_status["待审"]),
            "discovered": len(discovered),
        },
    })


if __name__ == "__main__":
    main()
