# F71 Noam Shazeer（诺姆·沙泽尔）完整主要贡献清单
> 原型：奠基科学家×科学家–创业者（深度学习架构发明者 + 框架/系统工程师 + AI 创业者/巨头技术领袖）。
> 相似性诱导对抗采样：与 **F30 Aidan Gomez** 同为《Attention Is All You Need》八位共同作者，专测"近克隆人是否坍缩到同一形状"。
> 红队记录：`validation/negative_sample/README.md` 曾把他列为 NS07 候选，因 **TIME100 AI 2023** 入选不满足负样本条件而剔除，并注明其缺席是"名单媒体可见度偏差"——本次入库正是补此系统性缺口。
> 审计轮次：v1（2026-06-14，新人入库）。本轮已查来源：en.wikipedia.org/wiki/Noam_Shazeer（S4）、
> scholar.google.com（user=wsGvgA8AAAAJ，总引/h-index S2）、arXiv（Transformer/MoE/Mesh-TF/AdaFactor 原文 S2）、
> research.com & scispace 作者页（h-index 交叉 S2）、CNBC/TechCrunch/WSJ 报道（$2.7B 交易、Gemini 任命 S4）。

## 教育与履历（非贡献，用于深度可比）
- 1975/1976 年生；**杜克大学数学与计算机科学学士（1994–1998）**；UC Berkeley 研究生项目**入读未完成——无博士学位**（与 F30 Gomez 同为"无 PhD 的奠基架构作者"）。
- 1994 年国际数学奥林匹克（IMO）**满分金牌**——早慧硬底子标志。
- **2000 年加入 Google**，长期任高级研究员/Distinguished Engineer；改进 Google 搜索拼写纠错；与 Daniel de Freitas 构建对话模型 Meena。
- **2021 年离开 Google**，与 de Freitas 共同创办 Character.AI 任 CEO。
- **2024-08 经 $2.7B"反向收购式"协议重返 Google**，任工程副总裁、与 Jeff Dean(F04)、Oriol Vinyals 共同领衔 Gemini。

## 1. 学术（论文/里程碑/高被引/开创概念）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| 《Attention Is All You Need》(Transformer) | 2017 | arXiv 1706.03762（S2）；scholar（S2） | **约 261,099 引**（Google Scholar，as-of 2026-06），21 世纪被引最多论文之一；几乎所有现代大模型架构基础 | **八位"贡献均等"共同作者之一**（与 Vaswani/Gomez/Uszkoreit/Kaiser 等），自述贡献多头自注意力 | **与 F30 Gomez 同篇共同作者** |
| 《Outrageously Large Neural Networks: 稀疏门控 MoE 层》 | 2017 | arXiv 1701.06538（S2） | 引入稀疏门控 **Mixture-of-Experts**，>1000× 模型容量提升而算力仅微增；今为 GPT-4/Mixtral/DeepSeek-V3 等稀疏大模型基石 | 第一作者 | 新增（独有，Gomez 无此线） |
| 《Exploring the Limits of Transfer Learning…》(T5) | 2020 | arXiv 1910.10683（S2） | **约 32,926 引**（Scholar，as-of 2026-06）；text-to-text 统一范式 | 共同作者（Raffel 等） | 新增 |
| 《PaLM: Scaling Language Modeling with Pathways》 | 2022 | arXiv 2204.02311（S2） | **约 9,511 引**（Scholar，as-of 2026-06）；540B 参数里程碑 | 共同作者 | 新增 |
| Google Scholar 总计量 | as-of 2026-06 | scholar（user=wsGvgA8AAAAJ，S2） | **总引 356,331、h-index 74、i10-index 135**（research.com 计 h=41 系子集，严重低估，不采用） | 本人 | 新增；以 Scholar 为准口径 |

## 2. 系统与框架（框架/工具链/平台/基准·数据集）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| **Mesh-TensorFlow**《Deep Learning for Supercomputers》 | 2018 | arXiv 1811.02084（S2） | 面向超算的大模型分布式训练框架，模型并行基础设施，被后续 GShard/大模型训练沿用 | 主导作者 | 新增；硬系统/基础设施贡献 |
| **AdaFactor** 优化器《Adaptive Learning Rates with Sublinear Memory Cost》 | 2018 | arXiv 1804.04235（S2） | 亚线性内存自适应优化器，大模型训练常用，节省优化器状态显存 | 共同第一作者（与 Mitchell Stern） | 新增 |
| Meena 对话模型（后演化为 LaMDA 路线） | 2020 | arXiv 2001.09977（S2） | 端到端开放域对话模型，谷歌内部对话 AI 前身；因谷歌拒绝公开发布而促成其离职创业 | 共同作者/主导 | 新增 |

## 3. 产品与工程（产品/产品线/技术系统）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| **Character.AI** 消费级对话产品 | 2021–2024 | TechCrunch（S4）；wikipedia（S4） | 上线首年达独角兽；以高黏性角色扮演对话著称，月活/访问量达数千万级（口径媒体估计，S4） | 联合创始人兼 CEO（产品总负责） | 新增 |
| Google **Gemini** 旗舰大模型（工程联席领衔） | 2024–至今 | CNBC（S4）；TechCrunch（S4） | 谷歌前沿大模型，与 Jeff Dean/Oriol Vinyals 共同领衔；全球前三梯队前沿模型 | 工程副总裁 / Gemini co-lead | **与 F04 Jeff Dean 共同领衔** |
| Google 搜索拼写纠错改进 | 2000s | wikipedia（S4） | 早期改进 Google 搜索拼写纠错系统（十亿级用户产品） | 工程师 | 新增 |

## 4. 公司与组织（公司/实验室/研究院）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Character.AI 创办与执掌 | 2021–2024 | wikipedia（S4）；TechCrunch（S4） | 创办即年内估值破 $10 亿；本人持股 **30–40%**；2023 a16z 领投 Series A 约 $1.5 亿/$10 亿估值 | 联合创始人兼 CEO | 新增 |
| $2.7B 反向收购式交易回归 Google | 2024-08 | CNBC（S4）；WSJ 转述（S4） | 谷歌以 **$27 亿**非独占授权 Character.AI 技术并回聘其与约 30 名核心成员；本人个人套现估 **$7.5 亿–$10 亿** | 交易核心人物 | 新增 |

## 5. 标准与基础设施（标准/芯片/算力平台）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Transformer/MoE 作为现代大模型"软基础设施" | 2017–至今 | arXiv（S2） | 其架构是当下几乎所有大模型的底层范式（软基础设施层） | 共同缔造者 | 新增；属软基础设施，非芯片/正式标准 |
| （芯片/正式技术标准本类无） | — | — | 查 wikipedia/媒体无亲自主导芯片或标准机构记录 | — | — |

## 6. 学术服务与荣誉（Fellow/院士/大奖/委员会角色）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| **美国国家工程院（NAE）院士** | 2026 | wikipedia（S4，待补 NAE 官网 S1） | 工程界最高荣誉之一，表彰深度学习架构贡献 | 本人 | 新增；硬荣誉（拟升 S1） |
| **TIME100 AI** | 2023 | TIME（S1） | 全球 AI 最具影响力 100 人 | 本人 | 新增；与 NS07 剔除依据同源 |
| IMO 1994 满分金牌 | 1994 | wikipedia（S4） | 国际数学奥赛满分，早慧标志 | 本人 | 新增 |

## 7. 人才与生态（师承/培养学生/社区·教育影响）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| 通过开放研究塑造整代大模型工程 | 2017–至今 | arXiv（S2） | Transformer/MoE/T5/Mesh-TF/AdaFactor 均为公开论文+多数开源代码，被全行业沿用 | 作者/开放者 | 新增；研究开放性强，但非框架托管/教育者 |
| （正式师承/培养知名学生本类弱）| — | wikipedia（S4） | 工业研究路径，无博导谱系；影响经由论文与产品而非带学生 | — | 新增；如实记"无博导谱系" |

## 8. 思想与公共影响（著作/观点报告/政策治理）

| 贡献 | 年份 | 来源URL + S级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| "稀疏/超大模型"早期逆向押注 | 2017 | arXiv 1701.06538（S2） | 在稠密模型主导期押注稀疏 MoE 可把容量扩 1000×，多年后成主流——信念逆向的硬证据 | 第一作者 | 新增 |
| 为"消费级对话 AI"离开谷歌创业 | 2021 | wikipedia（S4）；TechCrunch（S4） | 因谷歌拒绝公开 Meena，坚信对话 AI 价值而离职自办 Character.AI——以行动押注逆向判断 | 本人 | 新增；无公开宣言式檄文 |

## 对账小结

- **缺口待补（库中本无此人，全部新增）**：八类中标准/芯片(5)、正式师承(7) 弱（已注明查过、工业路径无谱系），其余六类命中。
  最硬锚点：Scholar 总引 **356,331 / h-index 74**(S2)、Transformer 261k 引(S2)、MoE/Mesh-TF/AdaFactor 原文(S2)、NAE 2026(待升 S1)、TIME100 AI 2023(S1)。
- **待更正**：无（新人）。
- **需更强来源**：NAE 2026 待补官网 S1；Character.AI 月活/估值与 $2.7B 个人套现均为媒体口径(S4)，标"媒体估计"；research.com 的 h=41 系子集低估，已弃用、采 Scholar h=74。
- **角色边界**：Transformer 是 **8 人贡献均等**之作（与 Gomez 同列），不可写成单人发明；MoE/Mesh-TF/AdaFactor 他为第一/共同第一作者，归属更强；Gemini 为"共同领衔"非独掌。
- 已建议回填到：`profiles/Noam Shazeer.md`（新建）/ `research/facts/F71_Noam_Shazeer.md`（新建）。
- coverage_audit 状态拟升为：`audited-v1`。
- **打分等 v5 统一重评**，不写入 scores.md。建议 9 维向量见 facts 末。

### 相似性诱导对抗采样：与 F30 Gomez 的形状对照（核心目的）
- F30 Aidan Gomez（已入表）= **[3,2,2,2,0,0,2,2,0]**（科学家-创业，Transformer 作者→Cohere CEO）。
- F71 Shazeer 建议 = **[3,3,2,2,0,0,2,2,1]**（见 facts 末理由）。
- **曼哈顿距离 = 2**，仅在 **D2(3 vs 2，Shazeer 多 Mesh-TF 系统+Gemini 领衔+消费产品)** 与 **D9(1 vs 0，Shazeer 抢在 ChatGPT 前做消费对话且年内独角兽)** 分叉。
- **诚实读法**：两位 Transformer 共同作者**没有坍缩成同一形状**，但距离仅 2、且差异落在 ±1 打分误差量级附近——
  这正印证红队结论：在**不刻意制造差异**的相似性诱导采样下，"零重合"虽未被推翻，却比对抗样本脆弱得多（多数对子距离 9）。
  待 v5 入表后由 `redteam_robustness.py` 复算最小距离分布，验证"相似性采样把点云局部压紧"的预期。
