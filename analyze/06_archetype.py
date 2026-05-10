"""archetype 聚类：人 × V0 原子 矩阵 → 几个 archetype。

每个 archetype 由：
  - 高权重原子（聚类中心向量上分量大的）
  - 邻近名人（距离质心最近的）
来定义。

输出：data/outputs/archetypes.json
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

import numpy as np
import yaml
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score

from lib.io import load_json, write_json
from lib.v0 import V0_ATOMS

log = logging.getLogger("06_arch")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", stream=sys.stdout)


def impute_with_atom_mean(M: np.ndarray) -> np.ndarray:
    """缺失值用列均值填充（粗粒度，但小样本下够用）。"""
    out = M.copy()
    for j in range(out.shape[1]):
        col = out[:, j]
        if np.isnan(col).all():
            out[:, j] = 0.0
        else:
            mean = np.nanmean(col)
            col[np.isnan(col)] = mean
            out[:, j] = col
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    args = ap.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))

    out_dir = Path(cfg["paths"]["outputs_dir"])
    v0_data = load_json(out_dir / "v0_matrix.json")
    if not v0_data:
        log.error("v0_matrix.json 不存在，先跑 02")
        return

    rows = v0_data["matrix"]
    atom_ids = [a["id"] for a in V0_ATOMS]
    pids = [r["pid"] for r in rows]
    names = [r["name"] for r in rows]

    M = np.full((len(rows), len(atom_ids)), np.nan, dtype=np.float32)
    for i, r in enumerate(rows):
        for j, aid in enumerate(atom_ids):
            v = r.get(f"a{aid}_mean")
            if v is not None:
                M[i, j] = v

    M_imp = impute_with_atom_mean(M)
    # 标准化（按原子做 z-score，让不同原子尺度可比）
    mu = M_imp.mean(axis=0, keepdims=True)
    sd = M_imp.std(axis=0, keepdims=True) + 1e-9
    Z = (M_imp - mu) / sd

    arch_cfg = cfg["archetype"]
    algo = arch_cfg.get("algorithm", "kmeans")
    k_range = arch_cfg["k_range"]

    # 选 k：silhouette
    best_k = None
    best_labels = None
    best_score = -1.0
    scores = []
    for k in range(k_range[0], k_range[1] + 1):
        if k >= len(rows):
            break
        if algo == "agglomerative":
            cl = AgglomerativeClustering(n_clusters=k, linkage="ward")
        else:
            cl = KMeans(n_clusters=k, n_init=10, random_state=42)
        labels = cl.fit_predict(Z)
        if len(set(labels)) < 2:
            continue
        sc = silhouette_score(Z, labels)
        scores.append({"k": k, "silhouette": float(sc)})
        log.info(f"  k={k} silhouette={sc:.3f}")
        if sc > best_score:
            best_score = sc
            best_k = k
            best_labels = labels

    log.info(f"选定 k={best_k}, silhouette={best_score:.3f}")

    # 每簇分析
    archetypes = []
    for cid in sorted(set(best_labels)):
        idxs = [i for i, lb in enumerate(best_labels) if lb == cid]
        sub_z = Z[idxs]  # 标准化空间
        sub_raw = M_imp[idxs]
        centroid_raw = sub_raw.mean(axis=0)
        centroid_z = sub_z.mean(axis=0)

        # 高权重原子：z 分量最大的 top 5
        top_atom_idx = np.argsort(-centroid_z)[:5]
        top_atoms = [
            {
                "atom_id": atom_ids[j],
                "atom_name": V0_ATOMS[j]["name"],
                "z_score": float(centroid_z[j]),
                "raw_level": float(centroid_raw[j]),
            }
            for j in top_atom_idx
        ]

        # 邻近名人：距离质心最近的 top 5
        dists = np.linalg.norm(sub_z - centroid_z, axis=1)
        order = np.argsort(dists)
        repr_persons = [
            {"pid": pids[idxs[k]], "name": names[idxs[k]], "distance": float(dists[k])}
            for k in order[:5]
        ]

        archetypes.append({
            "archetype_id": int(cid),
            "size": len(idxs),
            "top_atoms": top_atoms,
            "representative_persons": repr_persons,
            "all_member_pids": [pids[i] for i in idxs],
        })

        log.info(f"=== Archetype {cid} (n={len(idxs)}) ===")
        log.info(f"  代表: {[p['name'] for p in repr_persons]}")
        log.info(f"  高权重原子: {[(a['atom_name'], round(a['z_score'], 2)) for a in top_atoms[:5]]}")

    write_json(out_dir / "archetypes.json", {
        "k_selected": int(best_k),
        "silhouette_selected": float(best_score),
        "k_scan": scores,
        "algorithm": algo,
        "n_persons": len(rows),
        "archetypes": archetypes,
    })


if __name__ == "__main__":
    main()
