# 资料收集与原子能力抽取模板

## 人物资料登记

| 字段 | 说明 |
|---|---|
| canonical_name | 后续模型最容易识别的姓名，外籍人物优先英文原名 |
| aliases | 中文名、英文名、常见拼写、机构内称呼 |
| country_or_region | 只用于资料检索，不作为能力标签 |
| current_anchor | 当前最重要的机构或角色，需注明是否已核验 |
| historical_anchors | 曾经显著影响其路径的机构或角色 |
| representative_outputs | 论文、产品、公司、数据集、系统、教材、开源项目等 |
| source_urls | 资料入口，按 A/B/C/D 等级标注 |
| notes | 不确定点、争议信息、需要继续核验的地方 |

## 原子事实格式

| 字段 | 说明 |
|---|---|
| person | 人物 |
| fact_id | 唯一编号 |
| fact | 单一、可核验事实 |
| source_url | 来源 |
| source_level | A/B/C/D |
| date_or_period | 时间点或时间段 |
| confidence | high / medium / low |

示例：

| person | fact_id | fact | source_level | confidence |
|---|---|---|---|---|
| Geoffrey Hinton | hinton_f001 | 2013-2023 年在 Google 兼职工作，并成为 VP and Engineering Fellow | A | high |

## 原子能力格式

| 字段 | 说明 |
|---|---|
| capability_id | 唯一编号 |
| capability | 细粒度能力描述 |
| evidence_facts | 支撑事实编号 |
| observed_in | 出现该能力的人物 |
| counter_evidence | 反证或限制 |
| confidence | high / medium / low |
| provisional_cluster | 临时聚类名，可以为空 |

示例：

| capability_id | capability | evidence_facts | observed_in | confidence |
|---|---|---|---|---|
| cap_001 | 能在主流低估阶段长期推进一个技术路线，并等待算力/数据条件成熟 | hinton_f001, hinton_f002 | Geoffrey Hinton | medium |

## 能力命名约束

能力项尽量采用动词结构：

| 不推荐 | 推荐 |
|---|---|
| 创新能力 | 能提出并坚持非主流技术范式直到外部条件成熟 |
| 领导力 | 能把研究议题组织成跨机构团队和可持续实验室 |
| 商业能力 | 能把模型能力映射成可规模化产品入口和付费场景 |
| 学术影响力 | 能通过论文、教材、开源或课程建立后续研究者的共同语言 |

## 置信度规则

| 置信度 | 标准 |
|---|---|
| high | 至少 2 个 A/B 来源支持，且事实链清楚 |
| medium | 有 A/B 来源支持，但能力解释仍需更多人物对照 |
| low | 只有二级来源或资料不足，只能作为待验证假设 |

## 聚类规则

聚类只能在原子能力达到一定数量后进行。聚类时不直接问“这些人属于哪类”，而是问：

1. 哪些原子能力经常共同出现？
2. 哪些能力虽然少见，但对成为领军人才有明显杠杆？
3. 哪些能力只在某个时代、机构或产业阶段出现？
4. 哪些能力之间存在张力，比如开放传播和闭源商业化、学术深耕和产品速度？
