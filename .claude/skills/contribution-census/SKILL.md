---
name: contribution-census
description: >
  Build a COMPLETE inventory of an AI leader's major contributions for the
  leadpeopleprofile research project, then backfill it into the pipeline.
  Goal is completeness — enumerate ALL major contributions across eight
  dimensions using one uniform source checklist for every person, so the
  later 8-dimension scoring sits on a full, comparable fact set instead of
  uneven, incomplete profiles. Use when the user wants to collect / complete
  / audit one person's contributions or asks whether a profile is missing work.
  Triggers: "补全X的资料", "把X的贡献加全", "给X建贡献清单", "X还漏了什么",
  "审计X", "X的主要贡献", "coverage audit", "contribution census",
  "complete X's contributions", "what is X missing".
---

# Contribution Census（完整主要贡献清单）

为 `leadpeopleprofile` 项目里的**一位** AI 领军人物建立**完整**的主要贡献清单，再回填到流水线。

**第一目标是"全"，不是"补差"。** 评分不公的根源是每个人被挖掘的广度/深度不一致——
谁先被零散补全谁就暂时显得更强。本 skill 用**同一套来源清单**把每个人的主要贡献**穷举**收全，
让深度可比；对账找缺口只是其中一个子步骤。

## 硬纪律（务必遵守）

1. **单次只做一个人**。用户给名字（或 `F##`）就做谁。
2. **不动正式分**：绝不修改 `research/scores.md` 与 `research/capability_matrix.md` 的分数数字。
   分数统一重评要等 60 人全部 `audited-v1`/`updated` 后另行进行。
3. **每条贡献至少 1 个官方/索引级来源**（层级见下）。无硬来源的候选进"需更强来源"，不写成事实。
4. **八类维度逐类都要扫**，某类确实为空写"（本类无）"并说明查过哪些来源——让"没有"是被记录的结论。
5. 保留现有标注约定：FACT 用 `[A]`（明确硬事实）/`[B]`（概括需谨慎）；CAP 与 FACT 之间保 `from F#` 链。

## 来源层级（优先级，沿用 coverage_audit.md §3）

本人/机构官方页 > 项目仓库 / 学术索引(Google Scholar / DBLP / Semantic Scholar) > 论文·报告 >
奖项官方页 > 大学·公司页 > 权威媒体 > 百科。
权威媒体与百科只用于**交叉核对**，单独不作硬来源。

## 八类覆盖维度（强制穷举）

1. **学术**：代表论文 / 里程碑 / 高被引 / 开创概念（引用量、会议·期刊、年份）
2. **系统与框架**：开源框架、工具链、平台、基准/数据集（GitHub/PyPI、星标/下载/采用规模）
3. **产品与工程**：上线产品、产品线、技术系统（用户/营收/规模）
4. **公司与组织**：创立/执掌的公司、实验室、研究院（融资、上市、团队规模）
5. **标准与基础设施**：技术标准、芯片、算力平台
6. **学术服务与荣誉**：Fellow/院士/Turing/Nobel、最佳论文/Test-of-Time、重要委员会角色
7. **人才与生态**：师承谱系、培养的知名学生、社区/教育影响
8. **思想与公共影响**：著作、有影响力的观点/报告、政策与治理参与

## 检索引擎

- **首选 `agent-reach`**：覆盖中英文 + GitHub / Google Scholar / LinkedIn / Exa web search +
  微博/微信公众号/B站等中文源。逐维度发关键词检索。
- **`WebFetch`**：打开官方人物页、项目仓库、论文页、奖项页核对**原文**，确认来源层级。
- **`WebSearch`**：兜底补充。

## 分步流程（按顺序执行，可低温度复现）

### Step 0 — 锁定目标与基线
- 由名字解析出 `F##` 与文件名。读已有：`profiles/<name>.md`、`research/facts/F##_<name>.md`、
  `research/evidence/F##_<name>.md`（若有）、`research/coverage_audit.md` 中该人的行。
- 列出"现有已知主要贡献"作为基线。

### Step 1 — 判定原型，组装检索清单
按 `第一批60人名单.md` / 现有 profile 判定原型，决定加挂层（**加深，不替代**核心层）：
- **全员核心层（必查）**：官方人物页；Google Scholar / DBLP / Semantic Scholar（**逐条过代表作列表**，
  不止看前几条）；GitHub 个人与所属 org 全家桶；荣誉权威页；权威媒体/百科交叉核对。
- 学术/工业研究科学家 → 代表论文 arXiv/会议页、实验室页、被引里程碑、标准/基准。
- 创始人/高管 → 融资轮次、产品线与用户/营收规模、上市/招股书、组织规模。
- 工具/框架/平台型 → GitHub org 全家桶、PyPI/下载量、生态采用（**最易被人物叙事漏掉，最高优先**）。
- AI 安全/治理/学者 → 政策报告、国会证词、著作、机构（FHI/CHAI/Anthropic 等）。

### Step 2 — 逐维度穷举检索，写贡献清单
- 复制 `research/contributions/TEMPLATE.md` 到 `research/contributions/F##_<name>.md`。
- 对**八类维度逐类**用 agent-reach 检索，每条命中用 WebFetch 核对官方原文，按 schema 填一行：
  `贡献名 | 类别 | 年份 | 来源URL+层级 | 影响/规模 | 本人角色(独立/共同/团队/组织者) | 与现有facts关系`。
- **目标是收全**：把基线之外新发现的主要贡献都加进来，不要只盯着"和现有 facts 的差"。
- 在文件头"本轮已查来源"逐项记下实际打开过的来源，便于复核与保证深度可比。

### Step 3 — 对账
- 贡献清单 × 现有 facts，给每条标 `已覆盖 / 缺口待补 / 需更强来源`，汇总到清单末"对账小结"。

### Step 4 — 回填（不动分数）
- **profiles**：让 `profiles/<name>.md` 反映清单里的**全部主要贡献**（叙述化，标 `[A]/[B]` 口径）。
- **facts**：在 `research/facts/F##_<name>.md` 把新增主要贡献写成 `F#` 事实并按需补 `C#` 能力，保 `from F#` 链。
- **evidence**：更新 `research/evidence/F##_<name>.md`——填 TEMPLATE 的 "Coverage Gap Audit" 段与 Evidence Rows；
  对分数的影响**只写在"对现有明账的校正提示"里作建议**，不改分数文件。
- **coverage_audit**：在 `research/coverage_audit.md` 该人行填"本轮权威来源对照"列，状态升级：
  - `audited-v1`：穷举完成、无须立即回填的硬缺口；
  - `updated`：发现硬缺口并已回填；
  - `needs-source`：发现候选但来源强度不足；
  - `needs-followup`：发现会影响评分、需批量统一处理的缺口。
  必要时把硬缺口登记到"已处理的硬缺口"表。

### Step 5 — 自检
- `rg "from F#" research/facts/F##_<name>.md` 确认证据链未断。
- 引用的来源 URL 可达；每条贡献至少 1 个官方/索引级来源。
- 确认**未修改** `research/scores.md` 与 `research/capability_matrix.md` 的分数。
- `rg "TODO|TBD|待补" profiles/<name>.md research/facts/F##_<name>.md` 无遗留占位。

## 完成汇报
向用户报告：新发现的主要贡献条数、八类维度命中情况、对账三态计数、coverage_audit 新状态，
以及"对分数的潜在影响"（仅建议，待 60 人齐后统一重评）。
