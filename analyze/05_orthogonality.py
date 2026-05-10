"""V0 原子正交性检验。

对人 × 原子矩阵（来自 02）做 Pearson 相关；
高相关原子对意味着"在样本上几乎共变" → 该考虑合并。

输出：
  - data/outputs/orthogonality.json
  - data/outputs/orthogonality_heatmap.png （如果 matplotlib 可用）
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

import numpy as np
import yaml

from lib.io import load_json, write_json
from lib.v0 import V0_ATOMS

log = logging.getLogger("05_orth")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", stream=sys.stdout)


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

    matrix_rows = v0_data["matrix"]
    atom_ids = [a["id"] for a in V0_ATOMS]

    # 构造人 × 原子矩阵（缺失值用 nan）
    M = np.full((len(matrix_rows), len(atom_ids)), np.nan, dtype=np.float32)
    for i, r in enumerate(matrix_rows):
        for j, aid in enumerate(atom_ids):
            v = r.get(f"a{aid}_mean")
            if v is not None:
                M[i, j] = v

    # Pearson correlation, pairwise complete
    K = len(atom_ids)
    corr = np.full((K, K), np.nan, dtype=np.float32)
    for i in range(K):
        for j in range(K):
            xi, xj = M[:, i], M[:, j]
            mask = ~np.isnan(xi) & ~np.isnan(xj)
            if mask.sum() < 5:
                continue
            xi_, xj_ = xi[mask], xj[mask]
            if np.std(xi_) < 1e-9 or np.std(xj_) < 1e-9:
                continue
            corr[i, j] = float(np.corrcoef(xi_, xj_)[0, 1])

    # 找高相关对
    thresh = cfg["orthogonality"]["high_corr_threshold"]
    pairs = []
    for i in range(K):
        for j in range(i + 1, K):
            c = corr[i, j]
            if not np.isnan(c) and abs(c) >= thresh:
                pairs.append({
                    "atom_a_id": atom_ids[i], "atom_a_name": V0_ATOMS[i]["name"],
                    "atom_b_id": atom_ids[j], "atom_b_name": V0_ATOMS[j]["name"],
                    "correlation": float(c),
                })
    pairs.sort(key=lambda x: -abs(x["correlation"]))

    # 输出
    write_json(out_dir / "orthogonality.json", {
        "atoms": [{"id": a["id"], "name": a["name"]} for a in V0_ATOMS],
        "correlation_matrix": [[None if np.isnan(corr[i, j]) else float(corr[i, j]) for j in range(K)] for i in range(K)],
        "high_corr_pairs": pairs,
        "high_corr_threshold": thresh,
    })

    log.info(f"原子相关矩阵 {K}×{K} 已计算")
    if pairs:
        log.info(f"高相关原子对（|r| >= {thresh}）：{len(pairs)}")
        for p in pairs[:10]:
            log.info(f"  r={p['correlation']:+.2f}  [{p['atom_a_id']}] {p['atom_a_name']}  ↔  [{p['atom_b_id']}] {p['atom_b_name']}")
    else:
        log.info(f"没有相关 |r| >= {thresh} 的原子对（V0 正交性良好）")

    # 简单 heatmap
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(9, 8))
        im = ax.imshow(np.where(np.isnan(corr), 0, corr), cmap="RdBu_r", vmin=-1, vmax=1)
        ax.set_xticks(range(K))
        ax.set_yticks(range(K))
        labels = [f"{a['id']}.{a['name']}" for a in V0_ATOMS]
        ax.set_xticklabels(labels, rotation=45, ha="right")
        ax.set_yticklabels(labels)
        for i in range(K):
            for j in range(K):
                if not np.isnan(corr[i, j]):
                    ax.text(j, i, f"{corr[i,j]:.2f}", ha="center", va="center",
                            color="white" if abs(corr[i, j]) > 0.5 else "black", fontsize=7)
        plt.colorbar(im, ax=ax, label="Pearson r")
        plt.title("V0 原子相关矩阵")
        plt.tight_layout()
        plt.savefig(out_dir / "orthogonality_heatmap.png", dpi=150)
        log.info("已生成 orthogonality_heatmap.png")
    except Exception as e:
        log.warning(f"绘图失败（可忽略）: {e}")


if __name__ == "__main__":
    main()
