# 原子能力第一次粗聚类 v0

本文件基于当前 102 条能力项做第一次粗聚类。它不是最终画像，而是为了把分散的原子能力组织成可检验的候选结构。

## 聚类方法

本轮聚类只使用前面已经抽取的事实和能力，不引入新的先验维度。

聚类依据：

1. 能力项描述中反复出现的动作机制。
2. 支撑事实中反复出现的成果类型。
3. 人物路径中的可放大杠杆点。
4. 能力之间是否共同出现或相互支撑。

不按以下方式聚类：

| 不采用 | 原因 |
|---|---|
| 学术/产业/中国/美国 | 过粗，会遮蔽真实机制 |
| 研究型/创业型/管理型 | 容易把职位当能力 |
| 创新力/领导力/影响力 | 语义太泛，无法指导后续资料抽取 |

## v0 候选能力簇

| cluster_id | 候选能力簇 | 核心机制 | 代表能力 | 代表人物 | 置信度 |
|---|---|---|---|---|---|
| cl01 | 长期技术路线判断 | 在主流变化前后长期坚持、修正或公开主张一条技术路线 | 非共识坚持、路线原则化、未来路线主张 | Geoffrey Hinton、Richard Sutton、Yann LeCun | medium |
| cl02 | 结构/范式发明 | 提出可被后续研究大量复用的训练方式、模型结构或设计维度 | GAN、Transformer、ResNet、ResNeXt | Ian Goodfellow、Aidan Gomez、Kaiming He、Saining Xie | high |
| cl03 | 任务/基准/工具塑造 | 改变领域如何训练、评测、复用和比较系统 | ImageNet、OpenMMLab、MMDetection、教材 | Fei-Fei Li、Lin Dahua、Richard Sutton | high |
| cl04 | 教育与解释放大 | 把复杂技术转化为课程、博客、可视化、代码和开发者入口 | 在线课程、CS231n、Distill/Transformer Circuits | Andrew Ng、Andrej Karpathy、Chris Olah | high |
| cl05 | 大规模工程系统 | 把模型、框架、硬件、训练系统和部署工具连成组织级基础设施 | TensorFlow、TPU、Pathways、PaddlePaddle、ERNIE | Jeff Dean、Wang Haifeng | high |
| cl06 | 学术到产业转译 | 把高校或研究机构中的知识系统、模型结构或人才网络转化为公司和产品路线 | 清华到智谱、Transformer 到 Cohere、课程到 Landing AI | Tang Jie、Zhang Peng、Aidan Gomez、Andrew Ng | medium |
| cl07 | AI for Science 问题组织 | 选择高价值科学问题，并组织模型、数据、科学家和工程团队求解 | AlphaFold、AI for Science、科学基座模型 | Demis Hassabis、Liu Tieyan | medium |
| cl08 | 资源迁移与效率突破 | 从非传统领域积累资源，再用效率路线或开放验证改变竞争边界 | High-Flyer 到 DeepSeek、开放 R1、低成本模型路线 | Liang Wenfeng | low |
| cl09 | 安全/治理共同语言 | 把风险、对齐、人类兼容等问题转化为教材、概念框架、研究组织和评估议程 | AIMA、Superintelligence、ARC、CHAI | Stuart Russell、Nick Bostrom、Paul Christiano | high |
| cl10 | 组织控制与公共接口 | 处理治理危机、监管、董事会、员工、合作伙伴和公众信任 | OpenAI 治理危机、参议院证词、部署组织 | Sam Altman | medium |
| cl11 | 技术团队组装与产品窗口 | 围绕关键技术发明者、明确能力窗口和产品入口建立创业组织 | Moonshot 技术团队、长上下文/Kimi、GLM 产品线 | Yang Zhilin、Zhang Peng | low |
| cl12 | 多重技术权威 | 同时在高校、公司、国家级平台或大型组织中保持技术话语权 | 教授兼首席科学家、研究院负责人、公司 CTO | Tang Jie、Liu Tieyan、Wang Haifeng、Jeff Dean | medium |

## 簇间关系

这些簇不是平行独立维度，它们经常形成链条：

| 链条 | 示例 | 解释 |
|---|---|---|
| 结构发明 -> 工具/基准 -> 教育传播 | ResNet、OpenMMLab、CS231n | 新结构需要工具和课程扩散，才会成为共同语言。 |
| 长期路线 -> 工程系统 -> 平台生态 | Hinton/LeCun 路线、Google/Baidu 平台 | 长期方向只有进入基础设施，才会形成组织级能力。 |
| 学术系统 -> 创业公司 -> 产品窗口 | Tang Jie/Zhipu、Aidan Gomez/Cohere | 高校或论文中的能力需要转译为公司和产品入口。 |
| 安全问题设定 -> 研究组织 -> 政策接口 | Russell/Bostrom/Christiano、Altman | 一部分安全路线是研究议程，一部分是公司部署和监管接口。 |
| 资源迁移 -> 效率突破 -> 开放验证 | Liang Wenfeng/DeepSeek | 非传统资源进入模型研发后，通过开放模型和技术报告被外部验证。 |

## v0 画像表达

基于当前 24 个已抽取人物和 102 条原子能力，AI 领军人才的 `v0` 画像可以这样表述：

人工智能领军人才不是由固定身份定义的，而是由其是否能在某个关键机制上形成“领域级杠杆”定义的。这个杠杆可能来自技术路线判断、模型结构发明、任务与工具标准化、教育传播、大规模工程系统、学术到产业转译、科学问题组织、安全治理语言、组织公共接口、资源效率突破或多重技术权威。

换句话说，领军人才的关键不只是“做出了成果”，而是他们的成果改变了其他人做研究、训练模型、组织团队、使用工具、判断风险、进入行业或配置资源的方式。

## 最可能保留为最终画像骨架的簇

当前证据较强、跨人物出现明显的簇：

| 簇 | 保留理由 |
|---|---|
| 结构/范式发明 | 多个代表人物有明确论文和后续复用证据 |
| 任务/基准/工具塑造 | ImageNet、OpenMMLab、教材等都改变了共同体行为 |
| 教育与解释放大 | Andrew Ng、Karpathy、Olah、Sutton 显示传播能塑造人才池 |
| 大规模工程系统 | Jeff Dean、Wang Haifeng 的能力链高度清楚 |
| 安全/治理共同语言 | Russell、Bostrom、Christiano 形成清晰的非工程领军路径 |

当前证据仍弱、需要继续验证的簇：

| 簇 | 当前弱点 | 下一步 |
|---|---|---|
| 资源迁移与效率突破 | 主要依赖 Liang Wenfeng 单一强样本 | 补 DeepSeek、High-Flyer、其他低成本模型路线 |
| 技术团队组装与产品窗口 | Yang Zhilin/Zhang Peng 个人事实仍不足 | 补王小川、姜大昕、闫俊杰、张鹏、杨植麟横向材料 |
| AI for Science 问题组织 | 当前只有 Demis Hassabis、Liu Tieyan 较厚 | 补张林峰、鄂维南、相关科学模型资料 |
| 组织控制与公共接口 | Sam Altman 特征强但样本少 | 补 Dario Amodei、李开复、王小川等组织型人物 |

## 下一步去重计划

当前 102 条能力项中存在同义和近义，需要在下一轮做三件事：

1. 合并近义项，例如“教育规模化”“工程教学转译”“传播即工具”可能属于同一大簇下的不同子能力。
2. 标记强证据能力和弱证据能力，防止媒体叙事类能力过度影响聚类。
3. 为每个簇保留反例和边界，例如结构发明者不一定擅长组织，创业者不一定贡献底层模型结构。

## 下一轮抽取优先级

| 优先级 | 人物 | 目标 |
|---|---|---|
| 1 | 王小川、姜大昕、闫俊杰、张鹏、杨植麟、梁文锋 | 验证中国大模型创业机制 |
| 2 | Dario Amodei、Ilya Sutskever、Sam Altman | 验证安全、组织控制和前沿实验室路线 |
| 3 | 张林峰、鄂维南、刘铁岩、Demis Hassabis | 验证 AI for Science 能力簇 |
| 4 | 周靖人、王海峰、黄铁军、张亚勤 | 验证平台生态和国家级研究平台路径 |
