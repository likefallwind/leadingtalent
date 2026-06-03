# v1 能力证据强度审计

本文件对 `20_normalized_capabilities_v1.md` 的 84 条能力做证据强度审计。这里的等级不是判断能力重要性，而是判断当前证据是否足够支撑该能力。

## 等级定义

| evidence_grade | 定义 |
|---|---|
| A | 有强一手来源或论文/官方资料，且能力表述与事实链距离较近。 |
| B | 有一手来源或多来源支撑，但能力解释需要更多对照样本。 |
| C | 主要依赖媒体/二级资料，或能力解释离事实较远，需要补证。 |

## 审计表

| normalized_id | evidence_grade | source_type | audit_note |
|---|---|---|---|
| nc001 | B | 官方主页 | 长期坚持技术路线合理，但需要更多反事实和时间线材料。 |
| nc002 | B | 官方主页 | 学生/合作网络事实清楚，能力解释仍需更多人物对照。 |
| nc003 | A | 个人主页/文章 | The Bitter Lesson 是强一手文本，能力与证据距离近。 |
| nc004 | B | 官方/公开材料 | LeCun 长期主张清楚，但具体“维持基础研究方向”需补机构材料。 |
| nc005 | A | 论文/个人主页 | LeNet/卷积路线事实清楚。 |
| nc006 | B | 官方/教材 | 跨 Hinton/Goodfellow，合理但较概括。 |
| nc007 | A | 论文 | GAN 训练范式证据强。 |
| nc008 | A | 论文/官方公司资料 | Transformer 作者和 Cohere 角色清楚。 |
| nc009 | A | 论文 | ResNet 训练瓶颈证据强。 |
| nc010 | A | 论文 | ResNeXt/cardinality 证据强。 |
| nc011 | B | 个人主页/论文 | 路线扩展清楚，但需要进一步拆分 Kaiming He 与 Saining Xie 的不同机制。 |
| nc012 | A | Stanford/论文 | ImageNet/ILSVRC 改变任务定义证据强。 |
| nc013 | A | 开源/论文 | OpenMMLab/MMDetection 工具链证据强。 |
| nc014 | A | 教材/官方 | RL 教材事实强。 |
| nc015 | A | 个人主页/教材 | 长期维护共同体入口证据强。 |
| nc016 | A | 个人博客/研究发布 | 可视化解释材料证据强。 |
| nc017 | A | Transformer Circuits | 机械可解释性研究对象证据强。 |
| nc018 | B | 博客/研究发布 | “传播即工具”解释合理但需更多影响证据。 |
| nc019 | A | 官方课程/个人主页 | DeepLearning.AI/Coursera 证据强。 |
| nc020 | A | 课程/个人主页 | CS231n 和公开教学材料证据强。 |
| nc021 | B | 公开课程/代码 | 非正式学习者网络影响需更多量化证据。 |
| nc022 | A | 官方组织资料 | Andrew Ng 多组织角色证据强。 |
| nc023 | A | Google 官方 | Google 系统和基础设施证据强。 |
| nc024 | A | Google 官方 | 跨系统/芯片/模型证据强。 |
| nc025 | A | Baidu 官方 | 搜索、飞桨、文心路径证据强。 |
| nc026 | B | Baidu 官方/报道 | 开发生态影响合理，但需要开发者规模或采用证据。 |
| nc027 | B | 媒体/技术报告 | Zhou Jingren 组织角色多依赖媒体，需官方补强。 |
| nc028 | B | 技术报告/媒体 | Qwen 模型家族事实强，个人能力链需补强。 |
| nc029 | B | 官方文档/开源仓库 | Alibaba Cloud Model Studio 与 QwenLM 官方仓库可支撑开源模型家族和云上商业服务并存；“战略张力”仍是研究解释。 |
| nc030 | A | 官方/清华/Z.ai | 清华/智谱/Z.ai 技术底座证据较强。 |
| nc031 | A | 官方/清华 | Tang Jie 双重技术路线连续性证据强。 |
| nc032 | B | 官方/系统材料 | AMiner 到产业资产解释合理，需更直接证据。 |
| nc033 | A | 论文/官方公司资料 | Transformer 到 Cohere 路径证据强。 |
| nc034 | B | Andrew Ng 官方资料 | 应用方法工具化合理，需更多企业采用证据。 |
| nc035 | A | Z.ai 官方 | GLM 产品线和清华孵化证据强。 |
| nc036 | A | Z.ai 官方 | 国产芯片适配证据强。 |
| nc037 | B | 媒体 | 搜索到助手迁移合理但需王小川一手访谈补强。 |
| nc038 | B | 公开会议/官方与行业资料 | StepFun 创始人 CEO 角色和微软前史已有多来源支撑，但仍需人物一手材料。 |
| nc039 | B | AP/DeepSeek 技术材料 | High-Flyer 资源和 DeepSeek 技术路线组合支撑。 |
| nc040 | B | 媒体/技术发布 | 效率路线有技术发布支撑，但“限制压力”解释需补强。 |
| nc041 | A | DeepSeek 官方/GitHub | 开放技术报告和模型入口证据强。 |
| nc042 | B | 一手公开表述/媒体 | “中国需要自己的 OpenAI”叙事和融资事实有多来源支撑，但仍主要依赖公开报道。 |
| nc043 | A | MiniMax 官方/招股书 | 创始人多重控制角色证据强。 |
| nc044 | B | MiniMax 官方/产品资料 | 产品组合证据较强，但需更完整产品线材料。 |
| nc045 | B | 上市文件/媒体 | 资本市场接口事实清楚，能力解释仍需补治理材料。 |
| nc046 | A | Moonshot 官方 | 技术团队组装证据强。 |
| nc047 | B | Moonshot 官方/媒体 | 产品窗口判断合理，但需更多产品和用户证据。 |
| nc048 | B | 合作发布/产品资料 | Geely、Qianli Technology 与 StepFun 的 Agent OS/AI+车资料补强了终端和汽车入口事实链。 |
| nc049 | B | Z.ai 官方/二级资料 | 模型能力叙事有官方材料，个人角色需补证。 |
| nc050 | A | OpenAI 官方证词 | 政策监管接口证据强。 |
| nc051 | A | OpenAI 官方公告 | 治理危机整合证据强。 |
| nc052 | A | OpenAI 官方证词 | 研究/构建/部署目标证据强。 |
| nc053 | B | OpenAI/MiniMax | 跨公司治理能力合理，但 MiniMax 部分仍需补组织材料。 |
| nc054 | A | 官方/教材 | AIMA 与 Russell 安全路线证据强。 |
| nc055 | A | CHAI 官方 | Human-compatible AI 研究议程证据强。 |
| nc056 | A | 个人主页/著作 | Superintelligence 概念框架证据强。 |
| nc057 | B | 个人主页/机构/著作资料 | Bostrom 个人主页、FHI 和 Superintelligence 资料可把能力限定在超级智能、存在风险和长期未来框架中。 |
| nc058 | A | ARC/公开文章 | 对齐问题拆解证据强。 |
| nc059 | A | ARC 官方 | 独立安全评估组织证据强。 |
| nc060 | B | 博客/组织资料 | 社区议程影响需更多引用/社区证据。 |
| nc061 | A | DeepMind 官方 | AlphaFold/AlphaGo 科学问题证据强。 |
| nc062 | A | DeepMind 官方 | 开放方法和科学社区参与证据强。 |
| nc063 | B | DeepMind 官方 | 游戏到生命科学迁移合理，但需补 Hassabis 路径材料。 |
| nc064 | A | Microsoft/BZA 官方 | Liu Tieyan AI for Science 组织议题证据强。 |
| nc065 | B | Microsoft 文章 | 科学基座模型构想需更多项目持续证据。 |
| nc066 | A | 论文/官方材料 | DeePMD 科学计算方法证据强。 |
| nc067 | A | DP Technology 官方 | 科学工具体系证据强。 |
| nc068 | B | DP 官方/报道 | 工业 R&D 基础设施需更多客户/应用证据。 |
| nc069 | A | Princeton/北大/论文 | 数学、计算科学和 AI for Science 证据强。 |
| nc070 | A | Princeton/北大 | 跨机构科学智能组织证据强。 |
| nc071 | A | DeepMind 官方 | 统一实验室和长期目标证据强。 |
| nc072 | A | BZA/Microsoft 官方 | 跨国研究机构到国家级学院证据强。 |
| nc073 | A | 北大/北京官方 | 非营利 AI 基础研究平台证据强。 |
| nc074 | B | 官方/地方资料 | 区域创新中心角色需更多组织成果证据。 |
| nc075 | A | 清华 AIR 官方 | 微软经验到清华 AIR 证据强。 |
| nc076 | B | 清华 AIR 官方 | 大学产业桥接机制合理，需更多项目成果证据。 |
| nc077 | A | CUHK/实验室资料 | 视觉实验室和跨学科组织证据强。 |
| nc078 | A | Google 官方 | 组织内技术权威证据强。 |
| nc079 | A | Baidu 官方 | 国家工程中心/CTO/学术共同体证据强。 |
| nc080 | B | 官方材料 | 跨机构技术接口合理，但人物机制不同。 |
| nc081 | B | Stanford/HAI | 公共议题和治理叙事证据较强，但应与教学传播区分。 |
| nc082 | B | 主页/著作/媒体 | 公共传播影响合理但需要更系统引用证据。 |
| nc083 | B | Baidu/PRNewswire | AI native applications 方向需更多落地案例。 |
| nc084 | B | CUHK/OpenMMLab | 视觉研究到商业化应用需更多产业证据。 |

## 审计汇总

| evidence_grade | 数量 |
|---|---:|
| A | 48 |
| B | 36 |
| C | 0 |

## 已补强的原 C 级能力

| normalized_id | 补强后状态 |
|---|---|
| nc029 | 已补 Alibaba Cloud Model Studio 与 QwenLM 官方仓库，升为 B；仍需周靖人一手材料。 |
| nc038 | 已补 StepFun/Jiang Daxin 公开资料，升为 B；仍需官方人物页或一手访谈。 |
| nc042 | 已补 Wang Xiaochuan 公开表述和融资资料，升为 B；仍不作为 A 级强结论。 |
| nc048 | 已补 Geely/StepFun Agent OS 与 AI+车合作资料，升为 B；仍需个人能力链补证。 |
| nc057 | 已补 Bostrom 个人主页、FHI 和 Superintelligence 资料，升为 B；仍需影响网络材料。 |

详见 `30_c_grade_evidence_supplement.md`。
