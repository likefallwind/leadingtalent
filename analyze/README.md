# Round 2 聚合分析模块

研究方案 V0.1 的 **Round 2** 实现：把 `extract/` 抽取出的原始 LLM 输出，聚合为 **V0 → V1 对照矩阵**——本项目的核心交付物。

---

## 流水线（编号即依赖顺序）

```
01_load_normalize.py    抽取 JSON → 三张扁平表
        ↓
02_v0_matrix.py         构建 V0 评分矩阵（人 × 12 原子）
        ↓
03_emergent_cluster.py  涌现 traits 语义聚类
        ↓
04_compare.py           V0 ↔ 涌现 三方对照（确证/细化/证伪/待审/发现）
        ↓
05_orthogonality.py     V0 原子相关矩阵 + heatmap
        ↓
06_archetype.py         人 × 原子 → archetype 聚类
        ↓
07_report.py            生成 V0 → V1 认知更新报告
```

每步独立可重跑。修改后续步骤的参数无需重跑前面（关键产物都是文件落盘）。

---

## 目录

```
analyze/
├── README.md
├── requirements.txt
├── config.yaml                  ← 各步阈值统一在这
├── lib/
│   ├── v0.py                    ← V0 12 原子定义（修改这里 = 修改假设）
│   └── io.py                    ← 共享 I/O + Embedding 客户端
├── 01_load_normalize.py
├── 02_v0_matrix.py
├── 03_emergent_cluster.py
├── 04_compare.py
├── 05_orthogonality.py
├── 06_archetype.py
├── 07_report.py
└── data/outputs/
    ├── normalized.json          ← 01 输出
    ├── v0_matrix.json/csv       ← 02
    ├── v0_per_call.csv          ← 02 细粒度
    ├── emergent_atoms.json      ← 03
    ├── comparison_matrix.json   ← 04 ⭐
    ├── orthogonality.json       ← 05
    ├── orthogonality_heatmap.png← 05
    ├── archetypes.json          ← 06
    └── V0_to_V1_report.md       ← 07 ⭐⭐ 核心交付物
```

---

## 准备

### 1. 前置依赖：先跑 extract

```bash
cd ../scrape && python scrape.py && python aggregate.py
cd ../extract && python extract.py
cd ../analyze
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 设置 embedding API key

```bash
export OPENAI_API_KEY=sk-...   # 用于 03 / 04 的 embedding
```

如果用 OpenAI 兼容的 embedding 服务（如 SiliconFlow、本地部署），改 `config.yaml` 的 `embedding.base_url` 即可。

---

## 一键跑全流程

```bash
python 01_load_normalize.py && \
python 02_v0_matrix.py && \
python 03_emergent_cluster.py && \
python 04_compare.py && \
python 05_orthogonality.py && \
python 06_archetype.py && \
python 07_report.py
```

报告在 `data/outputs/V0_to_V1_report.md`。

---

## 关键决策（在 config.yaml 调整）

| 参数 | 默认 | 含义 |
|---|---|---|
| `emergent_clustering.distance_threshold` | 0.35 | 越小簇越多越细 |
| `emergent_clustering.min_cluster_size` | 3 | 单点/双点不算簇 |
| `compare.similarity_high` | 0.65 | 视作"V0 与涌现匹配"的阈值 |
| `compare.similarity_low` | 0.40 | 视作"V0 与涌现无关"的阈值 |
| `compare.v0_strength_threshold` | 1.5 | V0 评分均值 ≥ 此值算"V0 强" |
| `orthogonality.high_corr_threshold` | 0.7 | V0 原子高相关警示阈值 |
| `archetype.k_range` | [3, 8] | archetype 数量搜索范围 |

---

## 状态判定逻辑（V0 原子 → 状态）

```
sim = V0 原子定义 与 最相似涌现簇 的余弦相似度
score = V0 原子在所有人 × 模型 × run 上的 level 平均值

if sim >= similarity_high:
    if score >= v0_strength_threshold:
        → 确证   (V0 假设 + 数据支持都强)
    else:
        → 细化   (涌现里有概念，但 V0 评分弱：可能定义未对齐)
elif sim < similarity_low:
    if score < v0_strength_threshold:
        → 证伪   (V0 评分也弱，且涌现里找不到 → 这个维度可能不存在)
    else:
        → 细化   (V0 评分高但涌现里找不到：少见但存在)
else:
    → 待审   (中间区，需人工判断)
```

涌现簇里没被任何 V0 原子高相似命中（max sim < similarity_high）→ **发现**（可能的新原子）。

---

## 已知限制

| 问题 | 当前处置 | 后续 |
|---|---|---|
| 缺失值（某 LLM 调用失败） | 列均值填充 | 样本足够时可改为 EM 填充 |
| 中间相似度区（待审）需人工 | 报告中列出 | 后续可加 LLM 调用做 pair-wise 判定 |
| 阈值参数敏感 | 默认值可能不适合每个数据集 | 跑出后看分布，必要时调 |
| archetype 命名 | 输出"高权重原子+代表名人"，不自动起名 | 命名属于人类工作 |
| 小样本（60 人） | 聚类会偏不稳定 | 报告里给 silhouette；如果 <0.2 应当心 |

---

## 流程跑通后的人类工作

报告生成只是开始。Round 2 真正完成需要：

1. **审视"待审"原子**——在 `04_compare.py` 输出里逐条人工判断
2. **审视"发现"簇**——决定哪些真的是新维度，哪些是 V0 已有的换皮
3. **修订 V0**：合并高相关原子、调整定义、补入新原子 → 这就是 **V1**
4. **回测 V1**：把修订后的 V0_ATOMS 写入 `lib/v0.py`，重跑 02-06，看稳定性是否改善

第 4 步是 **Round 3** 的工作。
