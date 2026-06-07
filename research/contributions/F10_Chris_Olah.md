# F10 Chris Olah 完整主要贡献清单
> 原型：学术研究者（非传统路径）+ 创始人/高管（interpretability 负责人）。
> 审计轮次：v1（2026-06-07）。本轮已查来源：
> - colah.github.io/about.html（个人官方页）
> - distill.pub（Distill 期刊官方）
> - openai.com/index/microscope/（OpenAI Microscope）
> - distill.pub/2020/circuits/zoom-in/（Circuits 研究）
> - anthropic.com（Towards Monosemanticity/Scaling Monosemanticity）
> - Transformer Circuits Thread: transformer-circuits.pub

## 教育与履历（非贡献，用于深度可比）
无传统 PhD（通过自学/写作/研究进入 ML 核心圈）；Google Brain research scientist；OpenAI interpretability team lead ~2018-2021；Anthropic 联合创始人/interpretability research lead 2021-。

## 1. 学术（论文/里程碑/高被引/开创概念）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Feature Visualization（神经网络特征可视化体系）| 2017 | distill.pub/2017/feature-visualization/ 【论文/报告】 | 把特征可视化从结果展示变为研究工具；奠定 circuits 可视化方法论 | 主要作者 | 已覆盖 F2（笼统）|
| The Building Blocks of Interpretability | 2018 | distill.pub/2018/building-blocks/ 【论文/报告】 | 系统化神经网络内部特征到输出的解释方法；Distill 高引文章之一 | 主要作者 | **缺口待补**：未进入 facts |
| Zoom In: An Introduction to Circuits | 2020 | distill.pub/2020/circuits/zoom-in/ 【论文/报告】 | 正式提出 circuits 框架（神经元→特征→子电路）；OpenAI 可解释性核心论文 | 主要作者（Olah, Cammarata, Schubert, Goh, Petrov, Carter） | 已覆盖 F4（笼统），**待补论文名** |
| A Mathematical Framework for Transformer Circuits | 2021 | transformer-circuits.pub 【论文/报告】 | 将 circuits 框架系统化延展至 Transformer/注意力头；影响大量后续 mechanistic interp 研究 | 共同作者（Elhage, Nanda, Olah 等） | **缺口待补**：未进入 facts |
| Toy Models of Superposition | 2022 | transformer-circuits.pub 【论文/报告】 | 系统化提出 superposition 问题（神经元同时编码多个概念）；奠定 monosemanticity 研究方向 | 共同作者（Elhage, Hume, … Olah） | **缺口待补**：未进入 facts |
| Towards Monosemanticity: Decomposing Language Models With Dictionary Learning | 2023 | anthropic.com/research 【机构官方页】 | 用 sparse autoencoders 从 MLP 中提取单义可解释特征；mechanistic interp 关键论文 | 通讯/主导（Anthropic interpretability team） | 已覆盖 F5（笼统），**待补论文名** |
| Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet | 2024 | anthropic.com/research 【机构官方页】 | 将 sparse autoencoder 扩展到 Claude 3 Sonnet；在前沿大模型中找到可解释特征 | 通讯/主导（Anthropic interpretability team） | **缺口待补**：未进入 facts |

## 2. 系统与框架（框架/工具链/平台/基准·数据集）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| OpenAI Microscope | 2020 | openai.com/index/microscope/ 【机构官方页】 | 对若干视觉"model organisms"关键层和神经元系统化可视化的开放工具集；研究社区广泛使用 | 贡献者/负责人（Olah, Carter, Schubert, Goh, Cammarata, Petrov） | 已覆盖 F4（笼统），**待补正式名称** |

## 3. 产品与工程（产品/产品线/技术系统）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| （本类贡献有限；Olah 主要贡献在研究/期刊/概念/机构层）| — | — | — | — | — |

## 4. 公司与组织（公司/实验室/研究院）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Anthropic 联合创始人/interpretability 负责人 | 2021- | anthropic.com 【机构官方页】 | Anthropic 是全球最重要的 AI 安全公司之一；Olah 领导基础安全研究方向 | 联合创始人/Interpretability Research Lead | 已覆盖 F5 |

## 5. 标准与基础设施（标准/芯片/算力平台）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| （本类贡献有限）| — | — | — | — | — |

## 6. 学术服务与荣誉（Fellow/院士/大奖/委员会角色）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Distill 联合创始人兼主编 | 2017- | distill.pub 【机构官方页】 | 把"解释清楚"确立为学术贡献；2021 起停刊（on hiatus）后影响仍延续 | 联合创始人/主编 | 已覆盖 F3 |

## 7. 人才与生态（师承/培养学生/社区·教育影响）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| colah.github.io 博客（神经网络可视化/LSTM/自然语言处理理解系列）| 2014- | colah.github.io 【个人官方页】 | 影响极大的 ML 讲解博客；"Understanding LSTM Networks" 是最广泛引用的 LSTM 入门文章之一 | 独立作者 | **缺口待补**：未进入 facts；F3 只提 Distill |
| mechanistic interpretability 研究社区的组织者和定义者 | 2018- | transformer-circuits.pub；distill.pub 【机构官方页+论文】 | 定义并推动 mechanistic interp 成为 AI safety 核心研究子领域；吸引大量年轻研究者 | 领域定义者/社区领袖 | 已覆盖 F7 |

## 8. 思想与公共影响（著作/观点报告/政策治理）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| "Growing Neural Networks"/"Neural networks are grown, not built"核心比喻 | 持续 | colah.github.io；TIME 引用 【个人官方页+权威媒体】 | 定义理解神经网络的研究哲学；影响领域共同语言 | 独立倡导者 | 已覆盖 F6 |

---

## 对账小结

### 缺口待补（现有 facts 未覆盖、来源够硬）
1. **colah.github.io 博客**（包括"Understanding LSTM Networks"等高引文章）— F3 只提 Distill，个人博客影响巨大未进入 facts
2. **Zoom In: An Introduction to Circuits 论文名（2020）** — F4 笼统
3. **A Mathematical Framework for Transformer Circuits（2021）** — 未进入 facts
4. **Toy Models of Superposition（2022）** — 未进入 facts，superposition 概念奠基论文
5. **Towards Monosemanticity 论文名（2023）** — F5 笼统
6. **Scaling Monosemanticity（2024）** — 未进入 facts
7. **The Building Blocks of Interpretability（2018，Distill）** — 未进入 facts
8. **Distill on hiatus since 2021** — 上下文信息，期刊已停刊但影响持续

### 已建议回填到
- `research/facts/F10_Chris_Olah.md`：更新 F4/F5，新增 F8-F11（各关键论文名）
- `profiles/Chris Olah.md`：补充具体论文名和"LSTM Understanding"博文
- `research/coverage_audit.md`：升级为 `updated`

### coverage_audit 状态拟升为：`updated`
