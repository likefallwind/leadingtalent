# F27 Paul Christiano 完整主要贡献清单
> 原型：AI安全·对齐研究科学家 + 机构创始人。
> 审计轮次：v1（2026-06-07）。本轮已查来源：paulfchristiano.com（个人主页）、NIST/CAISI官方页、www.alignment.org（ARC官网）、metr.org/about/（METR官网）、arXiv（1706.03741 RLHF、1810.08575 迭代放大、1606.06565 Concrete Problems）、Semantic Scholar（P. Christiano authorId 145791315）、WebSearch×多轮（ARC Evals→METR历史、ELK报告、NIST CAISI角色）。

## 教育与履历（非贡献，用于深度可比）
- UC Berkeley 博士（统计学习理论方向）；博士后/研究时期活跃于有效利他主义和 AI alignment 社区；
- ~2016–2021 OpenAI：早期研究员 → 语言模型对齐团队负责人；
- 2021 创办 Alignment Research Center（ARC）；
- 2022–2023 ARC Evals 分拆为 METR（Model Evaluation & Threat Research）；
- 2023 至今：NIST 下属 Center for AI Standards and Innovation（CAISI）技术顾问；同时继续领导 ARC 对齐理论研究。

## 1. 学术（论文/里程碑/高被引/开创概念）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Deep RL from Human Preferences（RLHF，arXiv 1706.03741，NeurIPS 2017） | 2017 | arxiv.org/abs/1706.03741（论文仓库）；semanticscholar.org（authorId 145791315） | 5,324 引用（Semantic Scholar，2026-06）；成为 ChatGPT/InstructGPT 训练关键技术 | 第一作者（Paul Christiano, Jan Leike, Tom B. Brown, Miljan Martic, Shane Legg, Dario Amodei） | 已覆盖(F2)，补引用数量+作者列表 |
| Concrete Problems in AI Safety（arXiv 1606.06565，ICML 2016） | 2016 | arxiv.org/abs/1606.06565 | 框架化AI安全5大实践研究方向（副作用/奖励劫持/可扩展监督等）；高被引安全论文 | 共同作者（Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, Dan Mané） | 缺口待补（现有facts未提） |
| Supervising strong learners by amplifying weak experts（迭代放大，arXiv 1810.08575） | 2018 | arxiv.org/abs/1810.08575 | 提出 Iterated Amplification 方法，解决超人任务的可扩展监督 | 第一作者（Paul Christiano, Buck Shlegeris, Dario Amodei） | 缺口待补（现有facts未提具体论文） |
| AI Safety via Debate（OpenAI blog + arXiv） | 2018 | openai.com/research/debate | 提出 Debate 方法：两个 AI 系统辩论+人类裁判，用于可扩展监督 | 主要作者 | 已覆盖(F4，概念层面) |
| Eliciting Latent Knowledge（ELK，ARC报告） | 2021–2022 | www.alignment.org（ARC官网，2021发布的报告） | 定义"如何知道AI说的话是否反映其真实信念"的核心对齐问题；引发社区广泛讨论 | 主要作者/研究负责人 | 缺口待补（现有facts未提） |

## 2. 系统与框架（框架/工具链/平台/基准·数据集）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| ARC Evals 评测框架（危险能力评估流程与工具） | 2022–2023 | metr.org/about/（METR官网） | 首批将"前沿模型危险能力"系统化评测落地；被 OpenAI、Anthropic 等采用为部署前评测 | 创始人/主要推动者 | 已覆盖(F5，隐含)，补评测框架维度 |

## 3. 产品与工程（产品/产品线/技术系统）

（本类无：Christiano 研究以安全方法论为主，无独立发布的商业产品或工程平台。ARC 为非营利研究组织。）

## 4. 公司与组织（公司/实验室/研究院）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Alignment Research Center（ARC） | 2021 | www.alignment.org（官网）；www.alignment.org/team/ | 独立对齐研究非营利机构；当前聚焦神经网络行为的机理解释理论 | 创始人（2021）；现仍关联 | 已覆盖(F5) |
| ARC Evals → METR（Model Evaluation & Threat Research） | 2023 | metr.org/about/（官网）；metr.org发布公告 | ARC 的评测部门独立为 METR；与 OpenAI、Anthropic、NIST AI Safety Institute Consortium、欧盟 AI Office 合作 | 主要推动者/联合创始人背景 | 缺口待补（facts未提 METR 分拆） |

## 5. 标准与基础设施（标准/芯片/算力平台）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Responsible Scaling Policies（RSP）方法原型 | 2022–2023 | metr.org/about/（官网提及 METR 原型化 RSP 方法） | 已被9家头部 AI 开发商采用；将危险能力评测阈值与部署决策绑定 | 主要推动方（METR/ARC Evals背景） | 缺口待补（现有facts未提） |
| NIST CAISI 技术顾问 | 2023–至今 | paulfchristiano.com（个人主页）；NIST官方 | 将技术对齐方法纳入美国国家标准与技术体系 | 技术顾问（Technical Advisor） | 已覆盖(F6)，补 CAISI 全称 |

## 6. 学术服务与荣誉（Fellow/院士/大奖/委员会角色）

（本类无公开记录的 Fellow 称号或主要学术大奖。Christiano 的影响更多体现在研究方向开创与政策渗透而非传统荣誉。已查 paulfchristiano.com / NIST 页面。）

## 7. 人才与生态（师承/培养学生/社区·教育影响）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| 有效利他主义与 AI alignment 社区的核心博主/思想输出者 | 2010s–至今 | paulfchristiano.com（博客）；alignment论坛 | 多篇被广泛引用的对齐思想文章（迭代放大/可扩展监督概念先于论文流通） | 撰写者/社区思想领袖 | 已覆盖(F1)，补具体渠道 |
| 培养/带动 ARC 研究员生态 | 2021–至今 | www.alignment.org（ARC博客） | ARC 有 Jacob Hilton 等长期对齐研究员；ARC 研究方向影响多家实验室安全团队 | ARC 创始人/研究负责人 | 需更强来源（学生/成员谱系） |

## 8. 思想与公共影响（著作/观点报告/政策治理）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| RLHF 技术路线的先发推广（从论文到 ChatGPT 工业落地） | 2017–2022 | arxiv.org/abs/1706.03741；openai.com/research/learning-from-human-preferences | 几乎所有主流大模型(ChatGPT/Claude/Gemini)的训练中枢 | 创始研究者 | 已覆盖(F2,F3) |
| 可扩展监督概念体系（ELK/Debate/Iterated Amplification）公开推广 | 2018–2022 | paulfchristiano.com（博客）；AI alignment论坛 | 定义"超级对齐"技术路线；Anthropic/OpenAI 等超级对齐/scalable oversight团队均引用 | 主要概念提出者 | 已覆盖(F4)，补具体文档 |
| NIST AI Safety Institute 参与 + RSP 方法向政策转化 | 2023–至今 | metr.org/about/（METR官网）；paulfchristiano.com | 影响美国联邦 AI 风险评估标准；RSP 被 9 家 AI 开发商采用 | 技术顾问/主要推动方 | 已覆盖(F6)，补 RSP 维度 |

## 对账小结

### 缺口待补（现有 facts 未覆盖、来源够硬）
1. **Concrete Problems in AI Safety（2016）**——arXiv 1606.06565，高被引对齐论文，共同作者之一，facts 未提
2. **迭代放大论文（2018）Supervising strong learners**——arXiv 1810.08575，迭代放大的正式论文，facts 未提具体论文
3. **Eliciting Latent Knowledge（ELK）报告（2021–22）**——ARC 官网发布，对齐社区里程碑文档，facts 未提
4. **ARC Evals 分拆为 METR（2023）**——metr.org 官网确认，facts 只提"ARC 做危险能力评测"
5. **Responsible Scaling Policies（RSP）原型化**——METR 官网明确提到，被 9 家 AI 开发商采用
6. **NIST CAISI 全称**（Center for AI Standards and Innovation）——paulfchristiano.com 确认，facts 只写"NIST head of AI safety"需更新为"CAISI 技术顾问"
7. **RLHF 论文引用数（5,324，Semantic Scholar 2026-06）+ 作者完整列表**

### 待更正（现有 facts/profile 错记的头衔/年份/归属/量级）
- F6 描述 "head of AI safety" 可补充更精确头衔：Technical Advisor at CAISI（paulfchristiano.com 自述）
- Profile 未提及 UC Berkeley 博士背景（统计学习理论）

### 需更强来源（候选但来源不足，先不回填）
- Paul Christiano UC Berkeley 博士导师姓名（未找到权威来源）
- ARC 具体成员/被培养研究员谱系
- RLHF 论文的 Google Scholar 全量引用数（Semantic Scholar 5,324 已够硬）

### 已建议回填到
- `profiles/Paul Christiano.md`：补 UC Berkeley 博士学历、CAISI 全称、METR 分拆、RLHF 引用量、Concrete Problems 论文、ELK 报告、RSP 方法
- `research/facts/F27_Paul_Christiano.md`：新增 F8（Concrete Problems in AI Safety）、F9（迭代放大论文）、F10（ELK 报告）、F11（METR 分拆）；扩写 F2（补 RLHF 引用 5,324）、F6（补 CAISI 全称）

### coverage_audit 状态拟升为：`updated`
