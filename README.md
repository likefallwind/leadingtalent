# AI 领军人才画像建设研究

学院 AI 博士生培养——即 AI 领军人才培养——画像方法论与执行管线。

详见研究方案：[`AI领军人才画像研究方案_V0.1.md`](./AI领军人才画像研究方案_V0.1.md)

---

## 方法论一句话

不靠人定维度，也不让数据空降；**先种 V0 假设，让大批名人公开痕迹来涌现挑战，三轨握手得到 V1**。核心交付物不是 V1 框架本身，而是 **V0 → V1 的认知更新报告**。

---

## 三个执行模块

```
scrape/    抓取 100-200 位 AI 名人公开痕迹（学术 / 代码 / 传记 / 主页）
   ↓
extract/   Round 1 双抽取：开放式 + 半结构式（多模型 × 多次采样）
   ↓
analyze/   Round 2 聚合：V0 评分 / 涌现聚类 / 三方对照 / archetype / 报告
```

每个模块独立 README，独立可跑。

---

## 端到端跑全流程

```bash
# 1. 装依赖（每个模块各一次）
cd scrape   && pip install -r requirements.txt
cd ../extract && pip install -r requirements.txt
cd ../analyze && pip install -r requirements.txt

# 2. 设 API key（环境变量）
export ANTHROPIC_API_KEY=sk-ant-...
export OPENAI_API_KEY=sk-...
export DEEPSEEK_API_KEY=sk-...     # 可选
export GITHUB_TOKEN=ghp_...        # 可选，提速 GitHub 抓取
export SS_API_KEY=...              # 可选，提速 Semantic Scholar

# 3. 抓数据
cd ../scrape
python scrape.py
python aggregate.py

# 4. 双抽取
cd ../extract
python extract.py

# 5. 聚合分析
cd ../analyze
python 01_load_normalize.py && \
python 02_v0_matrix.py && \
python 03_emergent_cluster.py && \
python 04_compare.py && \
python 05_orthogonality.py && \
python 06_archetype.py && \
python 07_report.py

# 报告：analyze/data/outputs/V0_to_V1_report.md
```

---

## 当前状态

- ✅ V0.1 方案文档
- ✅ scrape / extract / analyze 三模块代码
- ✅ 60 人名人池种子（待扩到 100-200）
- ⏳ 实跑数据待启动
- ⏳ Round 3 回测待 Round 2 结束后

---

## 仓库结构

```
.
├── README.md                                此文件
├── AI领军人才画像研究方案_V0.1.md           方法论与计划
├── scrape/                                  公开痕迹抓取
│   ├── README.md
│   ├── scrape.py
│   ├── aggregate.py
│   ├── scrapers/                            分源 scraper
│   └── data/names_seed.csv                  60 人名单
├── extract/                                 LLM 双抽取
│   ├── README.md
│   ├── extract.py
│   ├── llm.py
│   └── prompts/
│       ├── open.md
│       └── seeded.md
└── analyze/                                 聚合分析
    ├── README.md
    ├── 01_load_normalize.py
    ├── 02_v0_matrix.py
    ├── 03_emergent_cluster.py
    ├── 04_compare.py
    ├── 05_orthogonality.py
    ├── 06_archetype.py
    ├── 07_report.py
    └── lib/
        ├── v0.py                            V0 12 原子定义
        └── io.py
```
