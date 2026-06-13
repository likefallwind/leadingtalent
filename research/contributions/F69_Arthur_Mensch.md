# F69 Arthur Mensch（阿尔蒂尔·孟什）完整主要贡献清单
> 原型：创始人/高管（开源权重大模型）+ 前工业研究科学家；欧洲 AI 主权叙事代表。
> 审计轮次：v1（2026-06-14，新人入库）。本轮已查来源：en.wikipedia.org/wiki/Arthur_Mensch（S4）、
> Chinchilla 维基/arXiv（S2/S4，DeepMind 共同作者）、huggingface.co/mistralai（开源模型/许可 S2）、
> TechCrunch/Bloomberg/CNBC 报道（融资/估值 S4）、TIME 100 2024（S1/S4）、londontechweek 演讲者页（S3）。

## 教育与履历（非贡献，用于深度可比）
- 生于 1992-07-17（法国 Sèvres）；父数学家、母计算机科学家。École Polytechnique（2011–2015）；ENS Paris-Saclay MVA 硕士；Télécom Paris；后在 INRIA 方向机器学习（脑成像/优化）读博。
- DeepMind（巴黎）研究员 2020–2023（约 3 年），参与 Flamingo、Chinchilla（计算最优缩放）、RAG、Gemini 相关工作。
- 2023 年与 Guillaume Lample、Timothée Lacroix（均前 Meta/LLaMA 团队）共同创办 Mistral AI，任 CEO 至今。

## 1. 学术（论文/里程碑/高被引/开创概念）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Chinchilla《Training Compute-Optimal Large Language Models》 | 2022 | arXiv 2203.15556（S2）；en.wikipedia.org/wiki/Chinchilla_(language_model)（S4） | 计算最优缩放定律奠基论文（训练 400+ 模型 70M–16B），重塑大模型训练范式，极高被引 | 共同作者（Hoffmann/Borgeaud/Mensch 等，DeepMind 团队） | 新增 |
| Flamingo 多模态模型 | 2022 | DeepMind/维基（S4） | 视觉语言模型里程碑，少样本多模态 | 共同贡献者（团队） | 新增 |
| 早期学术（脑成像 ML/优化，含 scikit-learn 相关贡献） | 2015–2019 | 个人学术页/维基（S4） | 博士期间 ML 优化与神经成像研究 | 作者 | 新增；待补精确被引 |

## 2. 系统与框架（框架/工具链/平台/基准·数据集）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| **Mistral 7B / Mixtral 8x7B 开源权重模型** | 2023 起 | huggingface.co/mistralai/Mistral-7B-v0.1、Mixtral-8x7B-v0.1（S2） | **Apache 2.0 开源权重**；Mixtral 为稀疏 MoE（8 专家/总参 ~45B，前向计算约等于 14B）；HuggingFace 上被海量下载与衍生（TheBloke 等量化版广传） | 创始 CEO/团队 | 新增；开源生态贡献 |
| Mistral 后续模型矩阵（Mistral Large / Small / Codestral / Pixtral 等） | 2024–2025 | mistral.ai/huggingface（S2/S3） | 覆盖通用/代码/多模态的模型线，部分开源部分商用 | 创始 CEO | 新增 |

## 3. 产品与工程（产品/产品线/技术系统）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Le Chat（面向欧洲的 AI 助手产品） | 2024 起 | TechCrunch/媒体（S4） | Mistral 旗舰对话产品，金融/电信等行业采用增长 | 创始 CEO | 新增 |
| Mistral 营收增长 | 2023–2025 | FinTech Weekly/媒体（S4） | 营收预计从 2023 年 €1000 万增至 2025 年约 €6000 万（约 5 倍） | 创始 CEO | 新增；媒体口径 |

## 4. 公司与组织（公司/实验室/研究院）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| **Mistral AI 创办与执掌** | 2023 | en.wikipedia.org/wiki/Arthur_Mensch（S4） | 欧洲最具价值 AI 初创之一；与 Lample、Lacroix 共同创办 | 联合创始人兼 CEO | 新增 |
| 融资与估值里程碑 | 2023–2025 | techcrunch.com/Bloomberg/CNBC（S4） | 2023 种子轮 €1.05 亿；2024-06 Series B 估值 €5.8B；**2025-09 Series C €1.7B 由 ASML 领投（取 ~11% 股权），post-money 估值 \$14B（€12B）** | 创始 CEO | 新增 |

## 5. 标准与基础设施（标准/芯片/算力平台）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| 微软 Azure / 战略合作分发 | 2024 | 媒体（S4） | 微软投资并在 Azure 分发 Mistral 模型 | 合作签署方 | 新增 |
| （芯片/正式技术标准本类无） | — | — | 查媒体无亲自主导芯片/标准记录（ASML 为投资方非其业务） | — | — |

## 6. 学术服务与荣誉（Fellow/院士/大奖/委员会角色）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| TIME 100（2024，最具前景全球创新者，唯一法国人入选该类） | 2024 | TIME（S1/S4） | 国际权威榜单认可 | 本人 | 新增 |
| （院士/Fellow 本类暂无：年轻创始人，无院士级头衔） | — | — | 荣誉以榜单 + 公司影响为主 | — | 新增 |

## 7. 人才与生态（师承/培养学生/社区·教育影响）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| 开源权重模型对全球开发者生态的贡献 | 2023–至今 | huggingface.co/mistralai（S2） | Apache 2.0 开源权重显著推动欧洲及全球开源大模型生态、衍生模型与微调繁荣 | 推动者 | 新增 |
| 欧洲 AI 人才聚集 | 2023–至今 | 媒体（S4） | 汇聚前 DeepMind/Meta 欧洲研究者，成欧洲 AI 人才枢纽 | 创始 CEO | 新增 |

## 8. 思想与公共影响（著作/观点报告/政策治理）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| **"欧洲 AI 主权 + 开源权重"路线主张** | 2023–至今 | Bloomberg/媒体/演讲（S4） | 在美国闭源大厂主导格局下，旗帜性主张欧洲技术独立 + 开源权重路线，被视为欧洲 AI 的代表声音；参与欧盟 AI 监管讨论 | 旗手/倡导者 | 新增；D8 信念逆向证据（地缘+开源） |

## 对账小结

- **缺口待补（库中本无此人，全部新增）**：八类中标准/芯片(5)、院士级荣誉(6) 基本为空（已注明），其余六类命中。
  最硬锚点：Mistral \$14B 估值 + ASML €1.7B 领投(S4)、Mistral 7B/Mixtral Apache 2.0 开源权重(S2)、Chinchilla 共同作者(S2)、TIME 100 2024(S1)。
- **待更正**：无（新人）。
- **需更强来源**：个人 Google Scholar 精确总引（未单独核）；Mistral 营收/Le Chat 用户量（媒体口径，标 S4）；HuggingFace 精确下载数（标"海量/待核"）。
- **角色边界**：Chinchilla/Flamingo 是 **DeepMind 团队作品**，他是共同作者非单一发明；Mistral 由**三人共同创办**，他任 CEO；ASML 是投资方，芯片非其业务。
- 已建议回填到：`profiles/Arthur Mensch.md`（新建）/ `research/facts/F69_Arthur_Mensch.md`（新建）。
- coverage_audit 状态拟升为：`audited-v1`。
- **打分等 v4 统一重评**，不写入 scores.md。建议 9 维向量见 facts 末。
