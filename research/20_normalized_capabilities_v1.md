# 归并后的原子能力库 v1

本文件将前四轮 137 条能力项合并为 84 条较少重复的原子能力。`source_caps` 指向前序能力表中的能力编号，用于保留证据链。

## 归并规则

| 规则 | 说明 |
|---|---|
| 合并同义项 | 例如“教育规模化”“工程教学转译”“非正式人才网络”保留为不同子能力，但归入同一传播簇。 |
| 保留机制差异 | “公司治理危机整合”和“安全共同语言”都与治理有关，但机制不同，不合并。 |
| 降低身份标签 | 不用“学术型/产业型/中国型”命名能力，只写可迁移机制。 |
| 标记证据强度 | high 表示多位人物或强一手证据支撑；medium 表示证据够用但仍需扩样本；low 表示目前主要依赖少数样本或二级资料。 |

## v1 原子能力表

| normalized_id | 原子能力 | source_caps | observed_in | evidence_strength | candidate_cluster |
|---|---|---|---|---|---|
| nc001 | 在非共识或低热度阶段长期推进技术路线，等待外部条件成熟 | cap001, cap025 | Geoffrey Hinton | medium | 长期技术路线 |
| nc002 | 将长期研究目标表达成稳定问题意识，并围绕它选择方法、学生和合作网络 | cap025, cap027 | Geoffrey Hinton | medium | 长期技术路线 |
| nc003 | 用简洁原则总结技术历史规律，并影响后续路线选择 | cap069 | Richard Sutton | high | 长期技术路线 |
| nc004 | 在工业研究实验室中维持基础研究方向并参与路线辩论 | cap072, cap073 | Yann LeCun | medium | 长期技术路线 |
| nc005 | 从早期应用系统中抽象出可扩展的模型结构路线 | cap071 | Yann LeCun | high | 长期技术路线 |
| nc006 | 将多个基础方法积累成后续研究可复用的工具箱 | cap002, cap084 | Geoffrey Hinton, Ian Goodfellow | medium | 方法体系积累 |
| nc007 | 提出可复用训练范式，使大量后续研究沿该范式展开 | cap083, cap085 | Ian Goodfellow | high | 结构与范式发明 |
| nc008 | 提出通用模型架构并在产业化阶段延续其应用价值 | cap087 | Aidan Gomez | high | 结构与范式发明 |
| nc009 | 通过关键架构技巧解决深层模型训练瓶颈 | cap089 | Kaiming He | high | 结构与范式发明 |
| nc010 | 在既有网络范式上提出新的结构维度，扩大架构设计空间 | cap092, cap094 | Saining Xie | high | 结构与范式发明 |
| nc011 | 从单一架构突破扩展到多条后续视觉表示路线 | cap090, cap091, cap093 | Kaiming He, Saining Xie | medium | 结构与范式发明 |
| nc012 | 通过数据集或挑战赛改变领域默认任务定义和评测标准 | cap005, cap030 | Fei-Fei Li | high | 任务基准与工具 |
| nc013 | 通过开源工具箱、benchmark 和工程框架降低领域实践门槛 | cap021, cap022, cap054 | Lin Dahua | high | 任务基准与工具 |
| nc014 | 用教材把复杂技术分支标准化为后续研究者训练入口 | cap068 | Richard Sutton | high | 任务基准与工具 |
| nc015 | 长期维护理论方向的论文、教材和研究材料，形成稳定共同体 | cap070 | Richard Sutton | high | 任务基准与工具 |
| nc016 | 把复杂神经网络机制转化为可视化、可读、可讨论的解释材料 | cap074 | Chris Olah | high | 教育与解释放大 |
| nc017 | 围绕模型内部机制建立新的研究对象和研究语言 | cap075 | Chris Olah | high | 教育与解释放大 |
| nc018 | 让传播材料本身成为研究共同体的共享工具 | cap076 | Chris Olah | medium | 教育与解释放大 |
| nc019 | 通过大规模在线课程把前沿 AI 知识转化为全球人才训练入口 | cap077 | Andrew Ng | high | 教育与解释放大 |
| nc020 | 将研究论文和工程实践翻译为开发者可执行的教学材料 | cap080 | Andrej Karpathy | high | 教育与解释放大 |
| nc021 | 通过开源代码、视频和课程影响非正式学习者网络 | cap082 | Andrej Karpathy | medium | 教育与解释放大 |
| nc022 | 把大学研究、在线教育、创业投资和产业工具连接成连续影响链 | cap078 | Andrew Ng | high | 教育与解释放大 |
| nc023 | 在公司内部推动底层机器学习基础设施，使研究能力成为组织级生产力 | cap003, cap028 | Jeff Dean | high | 大规模工程平台 |
| nc024 | 围绕系统、框架、芯片、模型和应用形成跨层协同 | cap004, cap028 | Jeff Dean | high | 大规模工程平台 |
| nc025 | 在大型互联网公司内长期连接搜索、NLP、大模型和深度学习平台 | cap023, cap056, cap115 | Wang Haifeng | high | 大规模工程平台 |
| nc026 | 通过开发者生态和企业生态扩大框架与大模型的产业影响 | cap024, cap057 | Wang Haifeng | medium | 大规模工程平台 |
| nc027 | 将云基础设施、模型实验室和集团技术委员会连接成企业级 AI 组织架构 | cap112 | Zhou Jingren | medium | 大规模工程平台 |
| nc028 | 通过模型家族把语言、多模态和图像基础模型纳入同一平台 | cap113 | Zhou Jingren | medium | 大规模工程平台 |
| nc029 | 在开源模型和商业云服务之间管理平台战略张力 | cap114 | Zhou Jingren | low | 大规模工程平台 |
| nc030 | 把高校知识系统或模型架构转化为创业公司的技术底座 | cap013, cap041, cap106 | Tang Jie, Zhang Peng | high | 学术到产业转译 |
| nc031 | 在高校教授和公司首席科学家等身份之间保持技术路线连续性 | cap042 | Tang Jie | high | 学术到产业转译 |
| nc032 | 把研究组长期积累的平台系统变成产业组织可复用资产 | cap043 | Tang Jie | medium | 学术到产业转译 |
| nc033 | 把基础模型结构发明转化为企业级模型服务公司 | cap086, cap088 | Aidan Gomez | high | 学术到产业转译 |
| nc034 | 把应用 AI 方法打包成企业可采用的工具和流程 | cap079 | Andrew Ng | medium | 学术到产业转译 |
| nc035 | 把清华孵化的大模型技术组织成公司级多代产品线 | cap050, cap106 | Zhang Peng | high | 学术到产业转译 |
| nc036 | 围绕国产芯片适配构建面向本土产业的模型部署能力 | cap051, cap107 | Zhang Peng | high | 学术到产业转译 |
| nc037 | 将搜索引擎时代的用户理解和产品经验迁移到大模型助手 | cap095 | Wang Xiaochuan | medium | 前史资源迁移 |
| nc038 | 把跨国研究机构经验迁移到中国多模态大模型创业公司 | cap098 | Jiang Daxin | medium | 前史资源迁移 |
| nc039 | 从量化投资场景积累机器学习、资金和算力资源，再迁移到基础模型 | cap011, cap038, cap109 | Liang Wenfeng | medium | 前史资源迁移 |
| nc040 | 在算力和芯片限制压力下选择效率优先模型路线 | cap040, cap097, cap111 | Liang Wenfeng, Wang Xiaochuan | medium | 前史资源迁移 |
| nc041 | 通过开放技术报告和模型入口接受全球研究社区验证 | cap039, cap110 | Liang Wenfeng | high | 前史资源迁移 |
| nc042 | 围绕“中国自己的 OpenAI”等叙事快速聚合资本和人才 | cap096 | Wang Xiaochuan | medium | 技术创业组织 |
| nc043 | 在创业公司中集中承担创始人、董事长、CEO、CTO 等控制角色 | cap100 | Yan Junjie | high | 技术创业组织 |
| nc044 | 把通用大模型能力包装成角色、多模态和生成内容产品组合 | cap101 | Yan Junjie | medium | 技术创业组织 |
| nc045 | 借助资本市场上市结果将模型公司纳入长期融资和治理体系 | cap102 | Yan Junjie | medium | 技术创业组织 |
| nc046 | 把关键技术发明者组装成核心团队，并用团队技术背景支撑公司可信度 | cap047, cap103 | Yang Zhilin | high | 技术创业组织 |
| nc047 | 围绕长上下文、智能体、coding 等能力窗口形成差异化产品定位 | cap048, cap104, cap105 | Yang Zhilin | medium | 技术创业组织 |
| nc048 | 把基础模型路线连接到 Agent、汽车和智能终端等落地入口 | cap099 | Jiang Daxin | medium | 技术创业组织 |
| nc049 | 将 reasoning、coding、agent 能力整合进对外模型能力叙事 | cap052, cap108 | Zhang Peng | medium | 技术创业组织 |
| nc050 | 把 AI 公司放到公共政策和监管场景中直接表达立场 | cap032 | Sam Altman | high | 组织控制与公共接口 |
| nc051 | 在治理冲突后重新整合董事会、员工、合作伙伴和公众信任 | cap008, cap033 | Sam Altman | medium | 组织控制与公共接口 |
| nc052 | 同时管理研究、构建、部署三个组织目标 | cap034 | Sam Altman | medium | 组织控制与公共接口 |
| nc053 | 用组织危机和资本治理能力维持前沿 AI 公司运转 | cap007, cap008, cap102 | Sam Altman, Yan Junjie | medium | 组织控制与公共接口 |
| nc054 | 把 AI 安全问题写入标准教材和学术共同语言 | cap059 | Stuart Russell | high | 安全治理共同语言 |
| nc055 | 将“AI 是否符合人类目标”转化为长期研究中心和研究议程 | cap060 | Stuart Russell | high | 安全治理共同语言 |
| nc056 | 提出足够有穿透力的概念框架，使技术风险进入跨学科公共讨论 | cap062, cap064 | Nick Bostrom | high | 安全治理共同语言 |
| nc057 | 将 AI 风险放入长期未来、存在风险和宏观战略框架中讨论 | cap063 | Nick Bostrom | medium | 安全治理共同语言 |
| nc058 | 把抽象对齐问题拆成可操作研究子问题和评估议程 | cap065 | Paul Christiano | high | 安全治理共同语言 |
| nc059 | 在前沿实验室外部建立独立安全评估和研究组织 | cap067 | Paul Christiano | medium | 安全治理共同语言 |
| nc060 | 通过博客、研究组织和社区讨论塑造新兴安全方向的研究议程 | cap066 | Paul Christiano | medium | 安全治理共同语言 |
| nc061 | 选择高难科学问题作为 AI 系统能力验证场景 | cap010, cap036 | Demis Hassabis | high | AI for Science |
| nc062 | 将 AI 系统应用于科学难题，并通过开放方法推动外部研究社区参与 | cap036 | Demis Hassabis | high | AI for Science |
| nc063 | 把游戏/强化学习等系统经验迁移到生命科学问题 | cap037 | Demis Hassabis | medium | AI for Science |
| nc064 | 将 AI for Science 抽象为跨学科组织议题，连接项目、人才和科学问题 | cap045 | Liu Tieyan | high | AI for Science |
| nc065 | 围绕科学基座模型构想设计长期研究议程 | cap046 | Liu Tieyan | medium | AI for Science |
| nc066 | 把深度学习势能模型转化为科学计算基础方法 | cap124 | Zhang Linfeng | high | AI for Science |
| nc067 | 将 AI for Science 方法组织成覆盖蛋白、RNA、原子、分子和科学文献的工具体系 | cap125 | Zhang Linfeng | high | AI for Science |
| nc068 | 把科学模型从论文方法推进为工业 R&D 可用基础设施 | cap126 | Zhang Linfeng | medium | AI for Science |
| nc069 | 把数学、计算科学和机器学习统一到 AI for Science 长期研究议程 | cap127 | Weinan E | high | AI for Science |
| nc070 | 在多机构之间组织跨学科科学智能研究 | cap128, cap129 | Weinan E | high | AI for Science |
| nc071 | 把多个顶级研究团队整合为统一实验室并围绕长期目标组织资源 | cap009, cap035 | Demis Hassabis | high | 研究组织与平台 |
| nc072 | 把跨国研究机构中的研究管理经验迁移到国家级学院和研究院 | cap015, cap044 | Liu Tieyan | high | 研究组织与平台 |
| nc073 | 把高校、地方政府和研究院资源组织成非营利 AI 基础研究平台 | cap118, cap120 | Huang Tiejun | high | 研究组织与平台 |
| nc074 | 让研究机构同时承担基础模型、前沿问题和区域 AI 创新中心角色 | cap119 | Huang Tiejun | medium | 研究组织与平台 |
| nc075 | 把微软全球研究和管理经验转化为清华产业 AI 研究院组织能力 | cap121 | Zhang Yaqin | high | 研究组织与平台 |
| nc076 | 用研究院形式承接大学和产业之间的长期技术转化 | cap122, cap123 | Zhang Yaqin | medium | 研究组织与平台 |
| nc077 | 把高校视觉研究实验室建设成跨学科 AI 研究机构 | cap053 | Lin Dahua | high | 研究组织与平台 |
| nc078 | 在组织结构变化中保留技术权威位置并服务多个研究单元 | cap029 | Jeff Dean | high | 多重技术权威 |
| nc079 | 在学术、工业组织和国家工程中心之间同时保持技术权威 | cap058, cap116 | Wang Haifeng | high | 多重技术权威 |
| nc080 | 在高校、创业公司、研究院之间维持技术路线和组织接口 | cap042, cap120, cap123 | Tang Jie, Huang Tiejun, Zhang Yaqin | medium | 多重技术权威 |
| nc081 | 把单一技术贡献扩展为研究机构、公共议题和治理叙事 | cap006, cap031 | Fei-Fei Li | medium | 公共研究影响 |
| nc082 | 通过公众传播、媒体和书籍扩大技术路线或风险议题影响力 | cap026, cap064 | Geoffrey Hinton, Nick Bostrom | medium | 公共研究影响 |
| nc083 | 将大模型能力转译为 AI native applications 等产业应用方向 | cap117 | Wang Haifeng | medium | 应用范式转译 |
| nc084 | 把计算机视觉研究、工程工具和商业化应用放在同一组织路径中推进 | cap055 | Lin Dahua | medium | 应用范式转译 |

## 初步去重结果

| 项目 | 数量 |
|---|---:|
| 原始能力项 | 137 |
| v1 归并后能力项 | 84 |
| 候选簇 | 13 |

## 仍需注意的重复风险

| 风险 | 说明 |
|---|---|
| “平台生态”和“研究组织”边界仍有重叠 | Wang Haifeng、Huang Tiejun、Zhang Yaqin 同时有平台和组织属性。 |
| “教育传播”和“公共研究影响”边界仍需清理 | Andrew Ng/Karpathy/Olah 是教学工具化，Bostrom/Hinton/Fei-Fei Li 更偏公共叙事和议题影响。 |
| “学术到产业转译”和“技术创业组织”边界仍需保留两层 | 前者是技术资产转译，后者是公司组织和产品窗口。 |
