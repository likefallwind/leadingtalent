"""聚合所有产物为 V0 → V1 认知更新报告（核心交付物）。

整合：
  - 02 V0 矩阵（每原子可观测度）
  - 03 涌现簇
  - 04 对照矩阵（确证/细化/证伪/待审 + 发现）
  - 05 正交性
  - 06 archetype 聚类

输出：data/outputs/V0_to_V1_report.md
"""
from __future__ import annotations

import argparse
import logging
import sys
from datetime import date
from pathlib import Path

import yaml

from lib.io import load_json
from lib.v0 import V0_ATOMS, ATOM_BY_ID

log = logging.getLogger("07_report")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", stream=sys.stdout)


def fmt_pct(x: float) -> str:
    return f"{x*100:.0f}%" if x is not None else "-"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    args = ap.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))

    out_dir = Path(cfg["paths"]["outputs_dir"])
    norm = load_json(out_dir / "normalized.json")
    v0 = load_json(out_dir / "v0_matrix.json")
    em = load_json(out_dir / "emergent_atoms.json")
    cmp_ = load_json(out_dir / "comparison_matrix.json")
    orth = load_json(out_dir / "orthogonality.json")
    arch = load_json(out_dir / "archetypes.json")

    if not all([norm, v0, em, cmp_, orth, arch]):
        log.error("缺产物，先按 01-06 顺序跑")
        return

    L: list[str] = []
    L.append(f"# V0 → V1 认知更新报告\n")
    L.append(f"*生成时间：{date.today().isoformat()}*\n")
    L.append("---\n")

    # ----- 0. 总览 -----
    summary = norm["summary"]
    L.append("## 总览\n")
    L.append(f"- 名人样本：{summary['unique_persons']} 人")
    L.append(f"- LLM 调用：{summary['files_seen']} 次（解析失败 {summary['parse_failures']}）")
    L.append(f"- 开放式抽取 trait 总数：{summary['open_traits_count']}")
    L.append(f"- 半结构补充 trait 总数：{summary['supplementary_count']}")
    L.append(f"- 涌现簇数：{em['kept_clusters']}（min_size={em['config_used']['min_cluster_size']}）")
    L.append(f"- archetype 数：{arch['k_selected']}（silhouette={arch['silhouette_selected']:.2f}）\n")

    # ----- 1. V0 状态总表 -----
    s = cmp_["summary"]
    L.append("## 1. V0 → V1 对照表（核心结论）\n")
    L.append(f"| 状态 | 数量 | V0 原子 ID |")
    L.append(f"|---|---|---|")
    for status in ["确证", "细化", "证伪", "待审"]:
        ids = cmp_["by_status"].get(status, [])
        names = [f"{i}.{ATOM_BY_ID[i]['name']}" for i in ids]
        L.append(f"| **{status}** | {len(ids)} | {', '.join(names) or '—'} |")
    L.append(f"| **发现（新涌现，未在 V0）** | {s['discovered']} | （见第 4 节） |")
    L.append("")

    # ----- 2. 详细：每个 V0 原子 -----
    L.append("## 2. V0 原子逐项判定\n")
    L.append("| ID | 原子 | 簇 | V0 平均 level | 最相似涌现簇 sim | 状态 |")
    L.append("|---|---|---|---|---|---|")
    for f in cmp_["v0_findings"]:
        L.append(
            f"| {f['atom_id']} | **{f['atom_name']}** | {f['cluster']} | "
            f"{f['v0_level_mean']:.2f} | {f['best_match_similarity']:.2f} | "
            f"**{f['status']}** |"
        )
    L.append("")

    L.append("### 每个原子的 top-3 最相似涌现簇\n")
    for f in cmp_["v0_findings"]:
        L.append(f"**{f['atom_id']}. {f['atom_name']}** （状态：{f['status']}，V0 level={f['v0_level_mean']:.2f}）")
        for t in f["top3_emergent"]:
            L.append(f"  - sim={t['similarity']:.2f}, size={t['size']}: {t['representative_names']}")
        L.append("")

    # ----- 3. 正交性 -----
    L.append("## 3. V0 原子正交性\n")
    pairs = orth.get("high_corr_pairs", [])
    if not pairs:
        L.append(f"未发现 |r| ≥ {orth['high_corr_threshold']} 的高相关原子对。**V0 整体正交性良好。**\n")
    else:
        L.append(f"高相关原子对（|r| ≥ {orth['high_corr_threshold']}），建议讨论是否合并：\n")
        L.append("| 原子 A | 原子 B | r |")
        L.append("|---|---|---|")
        for p in pairs:
            L.append(f"| {p['atom_a_name']} | {p['atom_b_name']} | {p['correlation']:+.2f} |")
        L.append("")
        L.append("> 见 `orthogonality_heatmap.png` 全矩阵\n")

    # ----- 4. 发现（涌现里的新原子候选） -----
    L.append("## 4. 涌现的新原子候选（未在 V0 中）\n")
    discovered = cmp_.get("discovered", [])
    if not discovered:
        L.append("无显著新原子涌现——V0 维度集已基本覆盖样本中的特质表达。\n")
    else:
        L.append("按规模降序，**这是项目最有研究价值的产出**：\n")
        L.append("| 簇 | trait 数 | 涉及人数 | 跨模型 | 与 V0 最相似 | 代表名称 |")
        L.append("|---|---|---|---|---|---|")
        for d in discovered[:20]:
            names = " / ".join(d["representative_names"][:3])
            L.append(
                f"| #{d['cluster_id']} | {d['size']} | {d['unique_persons']} | "
                f"{d['model_diversity']} | {d['closest_v0']} ({d['max_sim_to_v0']:.2f}) | {names} |"
            )
        L.append("")
        L.append("### 详细：每个候选的代表证据\n")
        for d in discovered[:10]:
            L.append(f"#### #{d['cluster_id']}　{' / '.join(d['representative_names'][:3])}")
            L.append(f"- 规模：{d['size']} 条 trait，{d['unique_persons']} 个不同人物，{d['model_diversity']} 个模型")
            L.append(f"- 与 V0 最相似：**{d['closest_v0']}** (sim={d['max_sim_to_v0']:.2f})")
            L.append(f"- 中心描述：{d['centroid_text']}\n")

    # ----- 5. archetype 聚类 -----
    L.append("## 5. Archetype 聚类（人 × V0 原子）\n")
    L.append(
        f"k={arch['k_selected']}（在 {arch['archetypes'][0].get('archetype_id') if arch['archetypes'] else '?'}-? 之间用 silhouette 选）, "
        f"silhouette={arch['silhouette_selected']:.2f}\n"
    )
    L.append("| Archetype | 规模 | 高权重原子（top 3，z 分） | 代表名人（前 3） |")
    L.append("|---|---|---|---|")
    for a in arch["archetypes"]:
        atoms = " / ".join(f"{at['atom_name']}({at['z_score']:+.1f})" for at in a["top_atoms"][:3])
        persons = " / ".join(p["name"] for p in a["representative_persons"][:3])
        L.append(f"| {a['archetype_id']} | {a['size']} | {atoms} | {persons} |")
    L.append("")

    # ----- 6. V1 草案建议 -----
    L.append("## 6. V1 框架草案（由本报告反推）\n")
    L.append("基于第 1-5 节结果，建议 V1 维度集如下（**仍需专家 review**）：\n")
    confirmed = [f for f in cmp_["v0_findings"] if f["status"] == "确证"]
    refined = [f for f in cmp_["v0_findings"] if f["status"] == "细化"]
    refuted = [f for f in cmp_["v0_findings"] if f["status"] == "证伪"]
    pending = [f for f in cmp_["v0_findings"] if f["status"] == "待审"]
    L.append(f"### 6.1 直接保留（{len(confirmed)} 个确证原子）")
    for f in confirmed:
        L.append(f"- **{f['atom_id']}. {f['atom_name']}** — V0 定义有效")
    L.append("")
    L.append(f"### 6.2 需修订定义（{len(refined)} 个细化原子）")
    for f in refined:
        L.append(f"- **{f['atom_id']}. {f['atom_name']}** — sim={f['best_match_similarity']:.2f}，对应涌现簇与 V0 描述不完全一致")
    L.append("")
    L.append(f"### 6.3 候选删除（{len(refuted)} 个证伪原子）")
    for f in refuted:
        L.append(f"- **{f['atom_id']}. {f['atom_name']}** — V0 评分低（{f['v0_level_mean']:.2f}）且涌现集中无对应（最大 sim={f['best_match_similarity']:.2f}）")
    L.append("")
    L.append(f"### 6.4 待人工审议（{len(pending)} 个）")
    for f in pending:
        L.append(f"- {f['atom_id']}. {f['atom_name']} — sim={f['best_match_similarity']:.2f} 处于中间区")
    L.append("")
    L.append(f"### 6.5 候选新增（来自第 4 节）")
    L.append(f"前 {min(5, len(discovered))} 个高规模涌现簇值得讨论是否补入 V1：")
    for d in discovered[:5]:
        L.append(f"- {' / '.join(d['representative_names'][:3])} — {d['size']} 条 / {d['unique_persons']} 人")
    L.append("")

    # ----- 7. 方法学说明 -----
    L.append("## 7. 方法学说明\n")
    L.append(f"- 数据：每位名人由 LLM 在 2 种条件 × N 模型 × 2 次采样下抽取（详见 extract/）")
    L.append(f"- 涌现聚类：{em['config_used']['algorithm']}, distance_threshold={em['config_used'].get('distance_threshold')}")
    L.append(f"- V0 ↔ 涌现 匹配：embedding 余弦相似度，high={cmp_['config_used']['similarity_high']}, low={cmp_['config_used']['similarity_low']}")
    L.append(f"- 状态判定阈值：V0 level mean ≥ {cmp_['config_used']['v0_strength_threshold']} 视为'V0 强'")
    L.append("- 所有阈值在 config.yaml 可调；该报告参数敏感性需要专班审议")
    L.append("")
    L.append("> **重要**：本报告是 R2 自动产出。Round 3 需要：(1) 人工审议待审原子；(2) 修订 V1 定义；(3) 用 V1 重新跑 02-06 验证稳定性。")

    out_path = out_dir / "V0_to_V1_report.md"
    out_path.write_text("\n".join(L), encoding="utf-8")
    log.info(f"报告已写入 {out_path}")
    log.info(f"  确证: {len(confirmed)} | 细化: {len(refined)} | 证伪: {len(refuted)} | 待审: {len(pending)} | 发现: {len(discovered)}")


if __name__ == "__main__":
    main()
