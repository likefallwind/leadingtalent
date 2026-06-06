# F01 Geoffrey Hinton 完整主要贡献清单
> 原型：学术/工业研究科学家。
> 审计轮次：v1（2026-06-06）。本轮已查来源：
> - University of Toronto 个人主页 https://www.cs.toronto.edu/~hinton/
> - Former PhD students page http://www.cs.toronto.edu/~hinton/gradstuphd.html
> - Wikipedia Geoffrey Hinton 词条
> - NobelPrize.org 2024 Physics facts
> - ACM Turing Award page
> - Vector Institute 官方公告（vectorinstitute.ai）及维基百科词条
> - CIFAR 官方新闻稿
> - Citationmap.com / research.com（Scholar h-index、总被引）
> - arxiv.org 论文页（2212.13345 Forward-Forward; 2212.10560 Mortal Computation）
> - WebSearch: Dropout 2014 / t-SNE 2008 / Knowledge Distillation 2015 / Capsule Networks 2017 被引量

## 教育与履历（非贡献，用于深度可比）
剑桥大学实验心理学学士 1970；爱丁堡大学 AI 博士 1978；CMU 助/副教授 1982-87；多伦多大学教授 1987-2014（荣休）；UCL Gatsby Unit 创始主任 1998-2001；CIFAR 项目主任 2004-2013；Google VP & Engineering Fellow 2013-2023；Vector Institute 联合创始人兼首席科学顾问 2017-。

## 1. 学术（论文/里程碑/高被引/开创概念）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| AlexNet — ImageNet Classification with Deep CNNs | 2012 | NeurIPS 2012；https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html 【论文/报告】 | 126,795+ 被引（Semantic Scholar）；ImageNet Top-5 error 降至 15.3%，突破传统方法 | 共同作者（与 Krizhevsky、Sutskever） | 已覆盖 F8 |
| Dropout: A Simple Way to Prevent Neural Networks from Overfitting | 2014 | JMLR 2014；https://jmlr.org/papers/v15/srivastava14a.html 【论文/报告】 | 40,815+ 被引；成为深度学习标准正则化技术 | 共同作者（Srivastava, Hinton, Krizhevsky, Sutskever, Salakhutdinov） | **缺口待补**：未进入 F01 facts |
| Learning representations by back-propagating errors | 1986 | Nature 1986；https://www.nature.com/articles/323533a0 【论文/报告】 | 20,000+ 被引；使反向传播成为标准训练方法 | 共同作者（Rumelhart, Hinton, Williams） | 已覆盖 F5（笼统） |
| A Fast Learning Algorithm for Deep Belief Nets | 2006 | Neural Computation 2006；https://doi.org/10.1162/neco.2006.18.7.1527 【论文/报告】 | 引发 2006 年深度学习复兴；被引 10,000+ | 共同作者（Hinton, Osindero, Teh） | 已覆盖 F6（笼统） |
| Visualizing Data using t-SNE | 2008 | JMLR 2008；https://www.jmlr.org/papers/v9/vandermaaten08a.html 【论文/报告】 | 被引 30,000+ ；成为高维数据可视化主流工具 | 共同作者（van der Maaten, Hinton） | **缺口待补**：未进入 F01 facts |
| Distilling the Knowledge in a Neural Network | 2015 | NeurIPS Workshop 2015；arXiv 1503.02531 【论文/报告】 | 奠定知识蒸馏领域基础，被引 15,000+ | 共同作者（Hinton, Vinyals, Dean） | **缺口待补**：未进入 F01 facts |
| Dynamic Routing Between Capsules | 2017 | NeurIPS 2017；arXiv 1710.09829 【论文/报告】 | 胶囊网络新方向，被引 5,000+ | 共同作者（Sabour, Frosst, Hinton） | **缺口待补**：未进入 F01 facts |
| The Forward-Forward Algorithm: Some Preliminary Investigations | 2022 | arXiv 2212.13345 【论文/报告】 | 提出反向传播替代方案（局部目标函数），启发生物合理学习研究 | 独立作者（Hinton） | **缺口待补**：未进入 F01 facts |
| Learning Distributed Representations of Words | 1986 | AAAI 1986 workshop；Hinton 1986 【论文/报告】 | 早期词向量/词嵌入思想来源，与后续 word2vec/嵌入空间有谱系关联 | 独立/共同作者 | 间接覆盖于 F4（分布式表征） |
| Boltzmann Machine / RBM | 1983-85 | Science 1983 等；NobelPrize.org 2024 确认 【官方页/论文】 | 2024 诺贝尔物理学奖核心；RBM 成为深度信念网络基础件 | 共同作者/主要推动者（Sejnowski, Hinton） | 已覆盖 F6 |
| Mixture of Experts (早期架构) | 1991 | Neural Computation 1991；Jacobs, Jordan, Nowlan, Hinton 【论文/报告】 | 为现代 MoE 模型（如 GPT-4, Mixtral）奠定架构概念 | 共同作者 | **缺口待补**：未进入 F01 facts |
| 总被引量 / h-index | 2026 | research.com / citationmap.com 【学术索引】 | 1,035,072 总引用；h-index = 190；776+ 出版物（截至 2026 年 6 月） | — | **缺口待补**：量级数字未进入 facts |

## 2. 系统与框架（框架/工具链/平台/基准·数据集）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| （本类无独立主导的开源框架/数据集；学术软件如 t-SNE 实现、RBM 代码均以论文为主要载体）| — | — | — | — | — |

## 3. 产品与工程（产品/产品线/技术系统）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Google 深度学习产品应用（语音识别、翻译、搜索、图像） | 2013-2023 | Google Blog 等 【权威媒体，交叉核对】 | Google 旗下多条产品线深度学习化；但 Hinton 以研究顾问角色为主，非直接产品 PM | 顾问/研究参与者 | 已覆盖 F9（笼统） |

## 4. 公司与组织（公司/实验室/研究院）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| DNNresearch Inc. | 2012 | U of T News 2013 【大学官方页】 | 被 Google 收购，触发深度学习产业化拐点 | 联合创始人（与 Krizhevsky, Sutskever） | 已覆盖 F9 |
| Vector Institute | 2017 | vectorinstitute.ai；维基百科；Newswire 2017 【机构官方页 + 权威媒体】 | 加拿大最重要 AI 研究机构之一；提升多伦多 AI 生态吸引力 | **联合创始人**（与 Brendan Frey, Raquel Urtasun）+ 首席科学顾问 | F10 只写顾问，未写联合创始人；**待更正** |
| UCL Gatsby Computational Neuroscience Unit | 1998-2001 | UCL 页面（需核查具体 URL） 【大学官方页】 | 英国顶级计算神经科学中心之一，培育后来计算神经科学人才 | 创始主任 | **缺口待补**：未进入 F01 facts |
| CIFAR "Neural Computation and Adaptive Perception" 项目 | 2004-2013 | CIFAR 官方 2024 新闻 https://cifar.ca/cifarnews/2024/10/08/long-time-cifar-fellow-geoffrey-hinton-awarded-2024-nobel-prize-in-physics/ 【机构官方页】 | 深度学习低潮期提供长周期共同体支持，为 2010s 复兴奠基 | 项目主任 | 已覆盖 F7 |

## 5. 标准与基础设施（标准/芯片/算力平台）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| （本类无：Hinton 非芯片/硬件/标准主导型人物） | — | — | — | — | — |

## 6. 学术服务与荣誉（Fellow/院士/大奖/委员会角色）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| 2024 诺贝尔物理学奖（与 Hopfield） | 2024 | NobelPrize.org 【官方页】 | 最高科学荣誉 | 共同获奖者 | 已覆盖 F12 |
| 2018 ACM 图灵奖（与 Bengio, LeCun） | 2018 | ACM 官方 【官方页】 | CS 最高奖项 | 共同获奖者 | 已覆盖 F12 |
| 2022 Princess of Asturias Award | 2022 | Princess of Asturias Foundation 【奖项官方页】 | 西班牙顶级国际奖项 | 获奖者 | **缺口待补**：未进入 F01 facts（已在 profile 中提到） |
| 2021 Dickson Prize in Science | 2021 | Carnegie Mellon University 【大学官方页】 | 美国重要科学奖项 | 获奖者 | **缺口待补**：未进入 F01 facts |
| 皇家学会 Fellow (FRS) | 1998 | 皇家学会官方名录 | 英国科学最高荣誉之一 | 会员 | 已覆盖 F12 |
| 加拿大 Order of Canada（Companion 级） | 2018 | Governor General of Canada 官方 | 加拿大最高荣誉 | 获得者 | **缺口待补**：未进入 F01 facts |
| AAAI Fellow; IEEE Fellow; 美国国家工程院/科学院外籍 Honorary Member | 多年 | AAAI/IEEE/美国科学院官方 | 跨学会高等级 Fellow | 会员 | 已覆盖 F12（笼统） |
| Queen Elizabeth Prize for Engineering | 2013 | QEPrize.org 【奖项官方页】 | 工程领域顶级奖项 | 共同获奖者（与 LeCun, Bengio, Jordan） | **缺口待补**：未进入 F01 facts |

## 7. 人才与生态（师承/培养学生/社区·教育影响）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| 38 位 PhD 学生（1987-2016，完整名单） | 1987-2016 | http://www.cs.toronto.edu/~hinton/gradstuphd.html 【本人官方页】 | 包含 Ilya Sutskever、Ruslan Salakhutdinov、Radford Neal、Yee Whye Teh、Alex Graves、Nitish Srivastava、Navdeep Jaitly 等行业/学界核心人物 | 主导导师 | F11 只写"Sutskever, Krizhevsky"；**缺口待补**：谱系宽度严重低估 |
| 知名博后：Yann LeCun、Peter Dayan、Max Welling | 1987-2000s | Wikipedia 词条（交叉核对） 【百科，交叉核对】 | LeCun 后成深度学习三巨头之一；Dayan 计算神经科学奠基人 | 博后导师/合作者 | F11 提到与 LeCun 并称但未写导师关系；**需更强来源**确认是否正式博后 |
| CIFAR 项目支撑连接主义共同体（2004-2013） | 2004-2013 | CIFAR 官方 【机构官方页】 | 低潮期维系全球神经网络研究网络 | 项目主任 | 已覆盖 F7 |

## 8. 思想与公共影响（著作/观点报告/政策治理）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| AI 风险公开发声（离 Google 后） | 2023- | 多家权威媒体 （NYT, BBC 等） 【权威媒体，交叉核对】 | 以深度学习奠基人身份警告失控/虚假信息/劳动冲击风险，公共讨论权重特殊 | 独立发声者 | 已覆盖 F13 |
| Mortal Computation 概念 | 2022 | arXiv 2212.13345（兼论 forward-forward） 【论文/报告】 | 提出以硬件特性承载学习计算的新范式，为生物合理 AI 提供理论框架 | 独立作者 | **缺口待补**：未进入 F01 facts |
| 200+ 同行评审出版物 | 1972-2026 | Google Scholar（research.com/citationmap） 【学术索引】 | 1,035,072 总引用；h-index 190 | 主要作者 | **缺口待补**：量级数字未进入 facts |

---

## 对账小结

### 缺口待补（现有 facts 未覆盖、来源够硬）
1. **Dropout (2014)** — JMLR，40,815+ 被引，Hinton 共同作者，应进入 facts F14 + D1.1 强化
2. **t-SNE (2008)** — JMLR，30,000+ 被引，Hinton 共同作者，应进入 facts F15
3. **Knowledge Distillation (2015)** — arXiv 1503.02531，15,000+ 被引，应进入 facts F16
4. **Capsule Networks (2017)** — NeurIPS 2017，5,000+ 被引，应进入 facts F17
5. **Forward-Forward Algorithm (2022)** — arXiv 2212.13345，Hinton 独著，应进入 facts F18
6. **UCL Gatsby Unit 创始主任 (1998-2001)** — 已在 profile 中提到，应进入 facts F19
7. **Vector Institute 联合创始人**（非仅"首席顾问"）— 需更正 F10 表述
8. **总被引 >100 万、h-index 190** — 量级数字应进入 facts
9. **完整 PhD 学生谱系（38 人）** — F11 严重低估；应扩写至至少列 8-10 位知名学生
10. **Queen Elizabeth Prize for Engineering (2013)** — 应进入 F12 补充
11. **Order of Canada Companion (2018)** — 应进入 F12 补充
12. **Mixture of Experts (1991)** — 为现代 MoE 架构概念来源，应补入 facts
13. **Mortal Computation 概念 (2022)** — 应进入 facts F18（与 forward-forward 合并）

### 待更正
- F10 "首席科学顾问" → 应补为 "联合创始人（与 Brendan Frey, Raquel Urtasun）兼首席科学顾问"

### 需更强来源
- Yann LeCun、Peter Dayan 是否正式以博后身份在 Hinton 实验室工作（Wikipedia 交叉提及，需官方页确认）

### 已建议回填到
- `profiles/Geoffrey Hinton.md`：补充 Dropout、t-SNE、知识蒸馏、胶囊网络、Forward-Forward 段落；更正 Vector Institute 联合创始人表述
- `research/facts/F01_Geoffrey_Hinton.md`：新增 F14-F21（Dropout/t-SNE/知识蒸馏/胶囊/Forward-Forward/Gatsby/完整学生谱系/量级数字）；更正 F10、F12
- `research/evidence/F01_Geoffrey_Hinton.md`：D1.1 标为 confirmed (stronger)，D7.3/D7.5 标为 partial/confirmed
- `research/coverage_audit.md`：升级为 `updated`

### coverage_audit 状态拟升为：`updated`
