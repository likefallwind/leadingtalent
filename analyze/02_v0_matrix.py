"""构建 V0 评分矩阵：人 × 12 原子。

每格：跨模型 × 跨 run 的 level 平均值（带方差）。
方差大 = 模型们对这个人在这个原子上分歧大，要谨慎使用。

输出：
  - data/outputs/v0_matrix.json （结构化）
  - data/outputs/v0_matrix.csv  （人工查看）
  - data/outputs/v0_per_call.csv （细粒度，每条 LLM 调用一行）
"""
from __future__ import annotations

import argparse
import csv
import logging
import sys
from pathlib import Path

import numpy as np
import yaml

from lib.io import load_json, write_json
from lib.v0 import V0_ATOMS, ATOM_BY_ID

log = logging.getLogger("02_v0matrix")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", stream=sys.stdout)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    args = ap.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))

    out_dir = Path(cfg["paths"]["outputs_dir"])
    norm = load_json(out_dir / "normalized.json")
    if not norm:
        log.error("normalized.json 不存在，先跑 01_load_normalize.py")
        return

    level_map = cfg["level_map"]
    es_map = cfg["evidence_strength_map"]
    rows = norm["seeded_v0"]
    if not rows:
        log.error("seeded_v0 为空")
        return

    # 收集所有 (pid, atom_id) → list[(level, evidence_strength, model, run)]
    cells: dict[tuple[str, int], list[dict]] = {}
    persons: dict[str, str] = {}  # pid → name
    for r in rows:
        aid = r["atom_id"]
        if aid not in ATOM_BY_ID:
            continue
        pid = r["pid"]
        persons[pid] = r.get("name") or pid
        cells.setdefault((pid, aid), []).append({
            "level_num": level_map.get(r["level"], np.nan),
            "es_num": es_map.get(r["evidence_strength"], np.nan),
            "model": r["model"],
            "run": r["run"],
            "raw_level": r["level"],
            "raw_es": r["evidence_strength"],
        })

    pid_list = sorted(persons.keys())
    atom_ids = [a["id"] for a in V0_ATOMS]

    # 矩阵
    matrix_rows = []
    per_call_rows = []
    for pid in pid_list:
        row = {"pid": pid, "name": persons[pid]}
        for aid in atom_ids:
            calls = cells.get((pid, aid), [])
            for c in calls:
                per_call_rows.append({
                    "pid": pid, "name": persons[pid],
                    "atom_id": aid, "atom_name": ATOM_BY_ID[aid]["name"],
                    "model": c["model"], "run": c["run"],
                    "level": c["raw_level"], "level_num": c["level_num"],
                    "evidence_strength": c["raw_es"], "es_num": c["es_num"],
                })
            if not calls:
                row[f"a{aid}_mean"] = None
                row[f"a{aid}_std"] = None
                row[f"a{aid}_n"] = 0
                continue
            levels = np.array([c["level_num"] for c in calls if not np.isnan(c["level_num"])])
            if len(levels) == 0:
                row[f"a{aid}_mean"] = None
                row[f"a{aid}_std"] = None
            else:
                row[f"a{aid}_mean"] = float(np.mean(levels))
                row[f"a{aid}_std"] = float(np.std(levels)) if len(levels) > 1 else 0.0
            row[f"a{aid}_n"] = int(len(levels))
        matrix_rows.append(row)

    # 整体统计：每个 atom 的平均 level（跨所有人，反映"V0 此原子在样本中是否普遍可观测"）
    atom_stats = []
    for aid in atom_ids:
        all_levels = []
        all_es = []
        for pid in pid_list:
            for c in cells.get((pid, aid), []):
                if not np.isnan(c["level_num"]):
                    all_levels.append(c["level_num"])
                if not np.isnan(c["es_num"]):
                    all_es.append(c["es_num"])
        atom_stats.append({
            "atom_id": aid,
            "atom_name": ATOM_BY_ID[aid]["name"],
            "cluster": ATOM_BY_ID[aid]["cluster"],
            "level_mean": float(np.mean(all_levels)) if all_levels else None,
            "level_std": float(np.std(all_levels)) if all_levels else None,
            "evidence_strength_mean": float(np.mean(all_es)) if all_es else None,
            "n_calls": len(all_levels),
        })

    write_json(out_dir / "v0_matrix.json", {
        "atoms": V0_ATOMS,
        "atom_stats": atom_stats,
        "matrix": matrix_rows,
    })

    # CSV：行=人，列=12 原子的 mean
    with (out_dir / "v0_matrix.csv").open("w", encoding="utf-8-sig", newline="") as f:
        cols = ["pid", "name"] + [f"a{aid}_{ATOM_BY_ID[aid]['name']}" for aid in atom_ids]
        w = csv.writer(f)
        w.writerow(cols)
        for r in matrix_rows:
            w.writerow([r["pid"], r["name"]] + [r.get(f"a{aid}_mean") for aid in atom_ids])

    # CSV：每条 LLM 调用一行
    with (out_dir / "v0_per_call.csv").open("w", encoding="utf-8-sig", newline="") as f:
        if per_call_rows:
            w = csv.DictWriter(f, fieldnames=list(per_call_rows[0].keys()))
            w.writeheader()
            w.writerows(per_call_rows)

    log.info(f"V0 矩阵：{len(pid_list)} 人 × {len(atom_ids)} 原子")
    log.info("各原子总体可观测度（level mean，越高表示越普遍可见）：")
    for s in sorted(atom_stats, key=lambda x: x["level_mean"] or 0, reverse=True):
        log.info(f"  [{s['atom_id']:2d}] {s['atom_name']:<14} level_mean={s['level_mean']:.2f}  n={s['n_calls']}")


if __name__ == "__main__":
    main()
