# F04 Jeff Dean 完整主要贡献清单
> 原型：工具·框架·平台型 + 学术/工业研究科学家。
> 审计轮次：v1（2026-06-06）。本轮已查来源：
> - Google Research 个人页 https://research.google/people/jeff/
> - Wikipedia Jeff Dean 词条
> - WebSearch: MapReduce/BigTable/TensorFlow/word2vec/Gemini 论文+引用量
> - IEEE John von Neumann Medal 2021 页面（UMN CSE 新闻）
> - TIME 100 Most Influential People in AI 2025
> - research.google / ResearchGate 引用数据

## 教育与履历（非贡献，用于深度可比）
明尼苏达大学计算机+经济学 1990；华盛顿大学计算机博士 1996（编译器/全程序优化）；DEC Western Research Lab 1996-99；Google Senior Fellow 1999-；Google Brain 创始领导者（2011-2023）；Google Chief Scientist 2023-（与 Hassabis 共定 AI 研究方向）。

## 1. 学术（论文/里程碑/高被引/开创概念）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| MapReduce: Simplified Data Processing on Large Clusters | 2004 | OSDI 2004；dl.acm.org 【论文/报告】 | 30,000+ 被引；重塑互联网规模分布式计算 | 共同第一作者（Dean, Ghemawat） | 已覆盖 F6（笼统），**待补被引量** |
| Bigtable: A Distributed Storage System for Structured Data | 2006 | OSDI 2006；dl.acm.org 【论文/报告】 | 10,000+ 被引；仍为 Google Search/Gmail/YouTube 底层 | 共同第一作者（Chang, Dean, Ghemawat et al.） | 已覆盖 F6（笼统） |
| Spanner: Google's Globally Distributed Database | 2012 | OSDI 2012 【论文/报告】 | 全球分布式数据库；9,000+ 被引 | 共同作者（Corbett, Dean et al.） | **缺口待补**：F6 笼统未明确 Spanner |
| Efficient Estimation of Word Representations in Vector Space（word2vec） | 2013 | arXiv 1301.3781；ICLR 2013 workshop 【论文/报告】 | 被引 40,000+（Semantic Scholar）；word2vec 成为 NLP 词嵌入事实标准 | 共同作者（Mikolov, Chen, Corrado, Dean） | 已覆盖 F9（笼统），**待补具体论文名和被引量** |
| Large Scale Distributed Deep Networks（DistBelief） | 2012 | NeurIPS 2012 【论文/报告】 | 首批大规模分布式深度网络训练系统论文；5,000+ 被引 | 共同作者（Dean, Corrado, Ghemawat et al.） | **缺口待补**：未进入 facts |
| BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding | 2018 | NAACL 2019；arXiv 1810.04805 【论文/报告】 | 被引 100,000+；Google Brain 主导，奠定预训练语言模型标准 | Google Brain 负责人（非直接第一作者，但机构主导）；Devlin 等实际作者 | **缺口待补**：F9 提到 BERT 但未明确规模 |
| TensorFlow: A System for Large-Scale Machine Learning | 2016 | OSDI 2016；arXiv 1605.08695 【论文/报告】 | 被引 50,000+；研究+生产双用开源 ML 框架 | 核心设计者/共同作者（Abadi, Dean et al.） | 已覆盖 F9（笼统），**待补具体被引量** |
| 总被引量 | 2025 | research.google；ResearchGate；clickrank.ai 【学术索引+机构官方页】 | 376,000–416,000+ 总引用（跨分布式系统/AI/ML/编译器）| — | **缺口待补**：量级数字未进入 facts |

## 2. 系统与框架（框架/工具链/平台/基准·数据集）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| TensorFlow（开源 ML 框架） | 2015 | github.com/tensorflow/tensorflow；tensorflow.org 【项目仓库+机构官方页】 | 180,000+ GitHub Stars；Google 生产与研究主力框架；行业广泛部署 | 核心设计者/共同创建者 | 已覆盖 F9（笼统），**待补 GitHub Stars 规模** |
| MapReduce 编程模型（内部 + 论文） | 2004 | Google 内部 + OSDI 2004 论文 【论文/报告】 | 触发 Hadoop 等开源生态；启发 Spark；改变大数据行业 | 共同发明者（Dean, Ghemawat） | 已覆盖 F6 |
| Pathways（异步分布式 ML 数据流平台） | 2022 | MLSys 2022 论文；ai.googleblog.com 【论文/报告+机构官方页】 | Google 新一代 AI 训练基础设施；支持 PaLM/Gemini 等超大模型 | 原始设计者/共同作者 | 已覆盖 F9（笼统） |
| JAX（数值计算框架，Google Brain） | 2018- | github.com/google/jax 【项目仓库】 | 研究社区高采用率；NumPy API + 自动微分 + GPU/TPU 加速 | Google Brain 机构主导（非单一作者） | **缺口待补**：F9 未单独列出 JAX |

## 3. 产品与工程（产品/产品线/技术系统）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Google 搜索索引基础设施（Bigtable/Spanner 驱动） | 2005- | Google 官方 Blog 【机构官方页】 | 支撑全球最大搜索引擎后端 | 核心系统架构师 | 已覆盖 F6（笼统） |
| Google 语音识别、机器翻译、图像识别（Brain 落地） | 2012- | Google Blog 等 【机构官方页交叉核对】 | 直接改善 Google 多个产品线用户体验 | Google Brain 领导者 | 已覆盖 F8,F9（笼统） |
| Gemini 多模态模型系列 | 2023- | deepmind.google；Google Blog 【机构官方页】 | Google 旗舰多模态大模型；co-lead | 联合负责人（co-lead with Hassabis） | 已覆盖 F9,F10（笼统） |
| Epi Info（WHO 合作公共卫生数据软件） | 1990-1991 | WHO 相关记录；Wikipedia 【权威媒体交叉核对】 | 成为公共卫生现场标准工具，WHO 全球分发 | 主要开发者（高中阶段 + 大学后） | 已覆盖 F3 |

## 4. 公司与组织（公司/实验室/研究院）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Google Brain 联合创建并长期领导 | 2011-2023 | Wikipedia；Google Research 页 【机构官方页+百科】 | 深度学习工业化最重要实验室之一；孵化 TensorFlow/word2vec/BERT/Gemini | 联合创始人（与 Andrew Ng, Greg Corrado）；2012 起领导者 | 已覆盖 F8（笼统） |

## 5. 标准与基础设施（标准/芯片/算力平台）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| TPU（Tensor Processing Unit）推动与系统设计 | 2016- | Google Blog；ISCA 2017 论文 【机构官方页+论文】 | 定义 AI 专用加速器行业方向；TPU v1-v5 驱动 Google 全部大模型训练 | 核心推动者/Google Brain 负责人（硬件决策者） | 已覆盖 F9（笼统） |

## 6. 学术服务与荣誉（Fellow/院士/大奖/委员会角色）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| 2021 IEEE John von Neumann Medal | 2021 | IEEE 官方；UMN CSE 新闻 https://cse.umn.edu/cs/news/jeffrey-dean-awarded-prestigious-ieee-john-von-neumann-medal 【奖项官方页+大学官方页】 | IEEE 最高荣誉之一，表彰大规模分布式系统和 AI 系统贡献 | 获奖者 | **缺口待补**：未进入 F11 |
| 2012 ACM Prize in Computing（与 Ghemawat） | 2012 | ACM 官方 【奖项官方页】 | 表彰互联网规模分布式系统（MapReduce/Bigtable） | 共同获奖者 | 已覆盖 F11 |
| ACM Fellow；美国国家工程院院士 | — | ACM/NAE 官方 | 顶级学会荣誉 | Fellow/院士 | 已覆盖 F11 |
| TIME 100 Most Influential People in AI 2025 | 2025 | TIME 官方 https://time.com/collections/time100-ai-2025/7305831/jeffrey-dean/ 【权威媒体】 | 全球 AI 最具影响力 100 人 | 入选者 | **缺口待补**：未进入 facts |
| Google Senior Fellow（公司最高工程级别） | — | Google 官方 | Google 工程师体系最高荣誉级别 | 获得者 | **缺口待补**：仅 F10 提及职级，未单独突出 |

## 7. 人才与生态（师承/培养学生/社区·教育影响）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Google Brain 培养 AI 人才生态 | 2011-2023 | Google Research；权威媒体 | BERT/word2vec/Gemini 等核心工程师和研究人员从 Brain 走出 | 机构领导者 | 已覆盖 F8（笼统） |
| TensorFlow 开源社区（PyPI 下载量极高） | 2015- | tensorflow.org；PyPI 统计 【项目官方页】 | 推动全球工程师可用深度学习；生态极大 | 框架共同创建者 | 已覆盖 F9（笼统） |

## 8. 思想与公共影响（著作/观点报告/政策治理）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| AI for Science 公开倡导（洪水预测/医疗诊断/气候）| 2018- | Google Blog；权威媒体 【机构官方页+权威媒体】 | 推动 AI 用于大规模现实问题议题进入公众视野 | 倡导者 | 已覆盖 F9（笼统） |

---

## 对账小结

### 缺口待补（现有 facts 未覆盖、来源够硬）
1. **Spanner（2012）**— OSDI 2012，Google 全球分布式数据库，9,000+ 被引，应进入 facts
2. **word2vec 论文名和被引量**（arXiv 1301.3781，40,000+ 被引）— F9 笼统，应补具体信息
3. **DistBelief（2012）**— NeurIPS，首批分布式深度网络系统论文，5,000+ 被引
4. **MapReduce 被引量（30,000+）** — F6 笼统，应补具体数字
5. **TensorFlow 被引量（50,000+）和 GitHub Stars（180k+）** — F9 笼统
6. **BERT 被引量（100,000+）** — F9 提到但未明确规模
7. **IEEE John von Neumann Medal（2021）** — 未进入 F11
8. **总被引量（376k–416k）** — 未进入 facts
9. **Google Senior Fellow 身份** — 应在 F11 突出（公司最高工程级别）
10. **JAX 框架** — F9 未单独列出
11. **TIME 100 Most Influential People in AI 2025** — 未进入 facts

### 待更正
- F8 说 Google Brain 2011 "共同创建"：维基百科显示 Dean 于 2012 年正式担任 Brain 领导者；联合创建者还包括 Andrew Ng、Greg Corrado — 应补全

### 需更强来源
- Dean 是否直接参与 BERT 论文写作（vs 机构负责人角色）需查 BERT 论文作者列表确认

### 已建议回填到
- `profiles/Jeff Dean.md`：补充 Spanner/word2vec/DistBelief/BERT 规模/JAX/von Neumann Medal
- `research/facts/F04_Jeff_Dean.md`：更新 F6/F9/F11，新增 F12-F15
- `research/coverage_audit.md`：升级为 `updated`

### coverage_audit 状态拟升为：`updated`
