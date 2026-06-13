# F68 François Chollet（弗朗索瓦·肖莱）完整主要贡献清单
> 原型：工具·框架·平台型（深度学习框架）+ 思想/逆共识型（智能度量与 AGI 路线）。
> 审计轮次：v1（2026-06-14，新人入库）。本轮已查来源：en.wikipedia.org/wiki/François_Chollet（S4）、
> github.com/fchollet（pinned repos star 数 S2）、keras-team/keras（star S2）、
> scispace/Semantic Scholar（Xception 引用 S2）、Google Scholar 总引（S2）、
> arXiv 1911.01547《On the Measure of Intelligence》（S2）、arcprize.org（ARC Prize/funders S1/S3）、
> 6sense（Keras 采用统计 S4）、YC/媒体（Ndea S4）。

## 教育与履历（非贡献，用于深度可比）
- 生于 1989-10-20（法国）；ENSTA Paris 工程硕士（M.Eng）。
- Google 2015 至 2024-11（9+ 年），升至 AI 团队 Senior Staff Engineer；其间创建 Keras、发布 ARC-AGI。
- 2024-11 离开 Google，与 Zapier 联合创始人 Mike Knoop 共同创办 Ndea（程序合成路线的 AGI 研究公司）；并主导 ARC Prize Foundation。

## 1. 学术（论文/里程碑/高被引/开创概念）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Xception: Deep Learning with Depthwise Separable Convolutions（CVPR 2017） | 2017 | arXiv 1610.02357（S2）；Semantic Scholar（S2） | 约 **16,506 引**（Semantic Scholar，as-of 2026-06）；CVPR 被引前十之列；深度可分离卷积奠基性架构 | 独立作者 | 新增 |
| On the Measure of Intelligence（智能度量论文） | 2019 | arXiv 1911.01547（S2） | 提出"智能=技能获取效率"而非"任务表现"，定义 ARC 数据集；AI 哲学/AGI 路线讨论中被广泛引用（精确被引待核，SS 解析异常） | 独立作者 | 新增；思想性奠基 |
| Google Scholar 总引用 | as-of 2026-06 | scholar.google（S2，VfYhf2wAAAAJ） | 总引约 **74,543**（主要由 Xception + Keras 论文拉动） | 本人 | 新增 |

## 2. 系统与框架（框架/工具链/平台/基准·数据集）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| **Keras** 深度学习高层 API | 2015 起 | github.com/keras-team/keras（S2）；keras.io（S3） | **约 64.1k stars**（as-of 2026-06）；TensorFlow 2.x 官方高层 API；据 6sense 全球 1.1 万+ 公司采用，用户含 CERN/NASA/Google/YouTube/Amazon/Hugging Face | 创建者（最初独立创建） | 新增 |
| **ARC-AGI** 抽象与推理基准 | 2019 起 | github.com/fchollet/ARC-AGI（S2）；arcprize.org（S3） | 约 **4.8k stars**；衡量 AI 解决新颖推理问题能力的标杆基准，被视为 LLM 时代"AGI 试金石"；后续 ARC-AGI-2（2025）/ARC-AGI-3（2026） | 创建者 | 新增 |
| deep-learning-with-python-notebooks | 2017 起 | github.com/fchollet/deep-learning-with-python-notebooks（S2） | 约 **20.1k stars**；配套畅销教材的开放笔记本 | 作者 | 新增 |

## 3. 产品与工程（产品/产品线/技术系统）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Keras 作为 Google AI 团队工程产品 | 2015–2024 | wikipedia（S4） | 在 Google 内长期维护并集成进 TensorFlow，成为全球默认易用深度学习栈 | Senior Staff Engineer/维护者 | 新增 |
| Ndea 程序合成 AGI 研究系统（在研） | 2024–至今 | YC/媒体（S4） | 尚处早期研究阶段，无成熟量产产品 | 联合创始人 | 新增；早期，标 S4 |

## 4. 公司与组织（公司/实验室/研究院）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Ndea（AGI 研究公司，程序合成路线） | 2024 | wikipedia/YC（S4） | 与 Mike Knoop 共同创办；明确押注"程序合成"而非纯规模化通往 AGI | 联合创始人 | 新增；融资额待核 |
| ARC Prize Foundation | 2024 | arcprize.org（S1/S3） | 非营利组织，运营 ARC Prize 竞赛（2024 \$1M、2025 总奖池约 \$2M）；funders 含 Knoop+Chollet \$1.1M、Ndea \$1M、xAI \$1M | 联合发起人 | 新增 |

## 5. 标准与基础设施（标准/芯片/算力平台）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| ARC-AGI 作为 AGI 评测"事实基准" | 2019–至今 | arcprize.org（S3） | 成为业界讨论 AGI 进展的公共评测基础设施之一 | 缔造者 | 新增；评测基准，非芯片/正式标准机构 |
| （芯片/正式技术标准本类无） | — | — | 查个人页/媒体无芯片/标准机构记录 | — | — |

## 6. 学术服务与荣誉（Fellow/院士/大奖/委员会角色）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| （院士/Turing/Fellow 本类暂无：工程/思想路径，无 ACM/IEEE Fellow 记录） | — | — | 影响以 Keras 行业地位 + 高被引论文 + 公共思想为主 | — | 新增；如实记"无重型头衔" |

## 7. 人才与生态（师承/培养学生/社区·教育影响）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| 著《Deep Learning with Python》（畅销逾 10 万册）+《Deep Learning with R》 | 2017/2018 | wikipedia（S4） | 销量逾 10 万册，全球深度学习入门标准教材之一 | 作者/共著 | 新增 |
| Keras 全球开发者社区 + "deep learning for humans"普及文化 | 2015–至今 | github.com/keras-team（S2） | 让深度学习从专业实验室走向大众开发者，降低门槛 | 社区缔造者 | 新增 |
| ARC Prize 全球竞赛社区 | 2024–至今 | arcprize.org（S1/S3） | 围绕 ARC-AGI 形成的开放研究竞赛生态 | 组织者 | 新增 |

## 8. 思想与公共影响（著作/观点报告/政策治理）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| **逆共识 AGI 路线主张**：智能=技能获取效率、纯规模化不通往 AGI、程序合成/抽象推理才是关键 | 2019–至今 | arXiv 1911.01547（S2）；公开演讲/X（S4） | 在"scaling is all you need"主流共识下持续逆向，以 ARC-AGI 把主张做成可证伪的公共基准；AI 公共话语中最知名的"规模派批评者"之一 | 提出者/旗手 | 新增；**D8 信念逆向核心证据** |

## 对账小结

- **缺口待补（库中本无此人，全部新增）**：八类中标准/芯片(5)、院士级荣誉(6) 基本为空（已注明查过、工程+思想路径无头衔），其余六类命中。
  最硬锚点：keras-team/keras 64.1k stars + 1.1 万+ 公司采用(S2/S4)、Xception 16,506 引(S2)、Scholar 总引 74,543(S2)、ARC Prize \$1M–\$2M(S1/S3)。
- **待更正**：无（新人）。
- **需更强来源**：《On the Measure of Intelligence》精确被引（SS 解析异常，标待核）；Ndea 融资额（未查到，标待核）；Keras 单篇论文被引细分。
- **角色边界**：Keras **最初为他个人创建**（后成团队/Google 项目），Xception、ARC-AGI、智能度量论文均为**独立作者**——D1/D8 的个人归属比 F66/F67 更清晰；ARC Prize 与 Mike Knoop 共同发起。
- 已建议回填到：`profiles/François Chollet.md`（新建）/ `research/facts/F68_François_Chollet.md`（新建）。
- coverage_audit 状态拟升为：`audited-v1`。
- **打分等 v4 统一重评**，不写入 scores.md。建议 9 维向量见 facts 末。
