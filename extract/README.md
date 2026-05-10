# Round 1 双抽取模块

研究方案 V0.1 中 **Round 1（名人涌现）** 的执行模块。
对每位名人的公开痕迹（来自 `scrape/` 模块），用多个 LLM 跑两种条件：

- **开放式**（不给 V0 维度）→ E_open
- **半结构式**（给 V0 12 个原子，允许补充）→ E_seeded

每条件下用 N 个模型 × M 次采样，跨条件交集即"稳定信号"，差集即"先验代价"或"V0 漏掉的"。

---

## 目录

```
extract/
├── README.md
├── requirements.txt
├── config.yaml             ← 模型组合、采样次数、prompt 路径
├── llm.py                  ← Anthropic / OpenAI 兼容统一封装
├── extract.py              ← 主入口
├── prompts/
│   ├── open.md             ← 开放式 prompt（不暴露 V0）
│   └── seeded.md           ← 半结构式 prompt（含 V0 12 原子定义）
└── data/
    ├── extractions/        ← 输出
    │   └── P001/
    │       ├── open__claude-sonnet__run1.json
    │       ├── open__claude-sonnet__run2.json
    │       ├── open__gpt-4o__run1.json
    │       ├── seeded__claude-sonnet__run1.json
    │       └── ...
    └── logs/
```

---

## 准备工作

### 1. 先跑 scrape 模块

`extract/` 读取 `scrape/data/traces/{id}/profile.md`。如果还没跑：

```bash
cd ../scrape
pip install -r requirements.txt
python scrape.py
python aggregate.py
cd ../extract
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置 API key（环境变量）

```bash
# 必填至少一个；config.yaml 默认启用三个，未设 key 的会自动跳过
export ANTHROPIC_API_KEY=sk-ant-...
export OPENAI_API_KEY=sk-...
export DEEPSEEK_API_KEY=sk-...
```

如要加 Qwen / SiliconFlow / Moonshot 等其它 OpenAI 兼容 API，在 `config.yaml` 的 `models:` 里复制一条 `openai_compat` 项，改 `base_url` 即可。

---

## 运行

```bash
# 测试 3 人跑通流程
python extract.py --limit 3

# 全量
python extract.py

# 只重跑某人
python extract.py --only P020

# 强制重跑（忽略已存在文件）
python extract.py --force
```

**计算量估算**（默认配置：60 人 × 2 条件 × 3 模型 × 2 runs）：
- = 720 次 LLM 调用
- Claude/GPT 各约 240 次，DeepSeek 240 次
- 单次约 3000 token 输入 + 1500 token 输出
- 估算成本：Claude $30 + GPT-4o $20 + DeepSeek $2 ≈ **$50**
- 估算时间：串行约 1-2 小时

---

## 输出格式

### 开放式（open）

```json
{
  "_meta": { "person_id": "P001", "condition": "open", "model": "claude-sonnet", "run": 1, "status": "ok" },
  "data": {
    "person_id": "P001",
    "person_name": "Geoffrey Hinton",
    "traits": [
      {
        "name": "对反主流的长期下注",
        "description": "在神经网络被边缘化的几十年间持续投入，形成对'当前共识'的免疫力",
        "evidence": ["80-90 年代神经网络冷遇期持续在 Toronto 做反向传播变体研究", "..."],
        "confidence": "高"
      }
    ]
  }
}
```

### 半结构式（seeded）

```json
{
  "_meta": { "..." },
  "data": {
    "v0_assessment": [
      { "atom_id": 1, "atom_name": "问题嗅觉", "evidence_strength": "强", "level": "高", "evidence": ["..."], "reasoning": "..." }
      // ... 共 12 项
    ],
    "supplementary_traits": [
      { "name": "学术家族建设力", "description": "...", "why_not_covered": "...", "evidence": ["..."] }
    ],
    "notes": "..."
  }
}
```

---

## 设计要点

| 决策 | 为什么 |
|---|---|
| 每人 × 条件 × 模型 × run 单独存盘 | 任一格失败不影响其他；下游聚合可灵活按维度切片 |
| 每条产出原子 JSON（不汇总） | 后续做正交性、聚类时需要原始多样性，不要过早汇总 |
| 高 temperature (0.7) | 多 run 有意义；低 t 等于多花钱拿同一个答案 |
| 开放式与半结构式都跑 | 二者差集是核心研究产出（先验代价 + 漏掉的强信号） |
| JSON 解析容错（剥 fence、抓 brace） | LLM 时不时出 markdown 包裹，硬失败浪费一次调用 |
| 失败也写盘（带状态标记） | 下游聚合脚本不会因为找不到文件而错乱 |

---

## 已知问题

| 问题 | 当前处置 | 后续 |
|---|---|---|
| profile.md 太长超 context | 中段截断（保头保尾） | 后续可加分段抽取再 merge |
| LLM 输出非 JSON | 多重容错解析；最终失败保留 raw | 可再加一轮"只返回 JSON"的修复调用 |
| 不同模型 token 成本差异大 | 在 config 里禁用某模型即可 | — |
| 中文名公开痕迹不足 | profile.md 内容稀薄→抽取退化为大模型先验 | 见 scrape/README，需补中文源 |

---

## 下一步：Round 2（聚合 + 对照）

抽取完成后进入 Round 2：
1. 把所有 JSON 聚合为 `名人 × 原子 × 模型` 矩阵
2. 对 `traits` 做语义聚类（embedding + clustering）
3. 与 V0 做三方对照（确证 / 发现 / 证伪 / 细化）
4. 在 `名人 × 原子` 矩阵上做 archetype 聚类

将作为下一个独立模块 `analyze/` 开发。
