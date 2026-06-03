# 能力聚类 v2：细分边界松的候选簇

本文件不重写 84 条 `nc` 原子能力，而是在 `v1` 基础上拆分边界较松的簇。重点拆分 `c05`, `c06`, `c08`, `c13`。

## 拆分原则

| 原则 | 说明 |
|---|---|
| 只拆机制，不拆身份 | 不按“学术/产业/中国/美国”拆。 |
| 保持证据链 | 每个子簇仍然回到 `nc` 编号。 |
| 允许一个人物跨多个子簇 | 领军人才画像本来就是组合型。 |
| 先形成可检验结构 | 后续可用新人物事实继续推翻或合并。 |

## v2 聚类表

| v2_cluster_id | v2 簇名 | 来源 v1 簇 | 归并能力 | 代表人物 | 证据强度 | 说明 |
|---|---|---|---|---|---|---|
| vc01 | 长期技术路线判断 | c01 | nc001, nc002, nc003, nc004, nc005, nc006 | Geoffrey Hinton, Richard Sutton, Yann LeCun | medium | 多年尺度上的路线坚持、路线原则和基础研究主张。 |
| vc02 | 结构与训练范式发明 | c02 | nc007, nc008, nc009, nc010, nc011 | Ian Goodfellow, Aidan Gomez, Kaiming He, Saining Xie | high | 提出可复用的模型结构、训练范式或架构设计空间。 |
| vc03 | 任务、基准与工具标准化 | c03 | nc012, nc013, nc014, nc015 | Fei-Fei Li, Lin Dahua, Richard Sutton | high | 改变研究共同体如何训练、评测、复用和比较。 |
| vc04 | 教育、解释与人才放大 | c04 | nc016, nc017, nc018, nc019, nc020, nc021, nc022 | Chris Olah, Andrew Ng, Andrej Karpathy | high | 把复杂技术转化为课程、解释材料、代码和学习入口。 |
| vc05 | 企业基础设施平台 | c05 | nc023, nc024, nc025 | Jeff Dean, Wang Haifeng | high | 模型、框架、硬件、搜索/NLP 和大模型形成企业级基础设施。 |
| vc06 | 开发者与企业生态平台 | c05 | nc026, nc083 | Wang Haifeng | medium | 通过框架、开发者生态和 AI native applications 扩大产业使用。 |
| vc07 | 云与模型家族平台 | c05 | nc027, nc028, nc029 | Zhou Jingren | medium | 云基础设施、Qwen 模型家族和开源/商业张力。 |
| vc08 | 高校知识资产到公司技术底座 | c06 | nc030, nc031, nc032, nc035 | Tang Jie, Zhang Peng | high | 清华/高校知识系统、模型架构和研究平台转为公司技术底座。 |
| vc09 | 结构发明到企业模型服务 | c06 | nc033 | Aidan Gomez | high | Transformer 贡献延伸到 Cohere 企业模型平台。 |
| vc10 | 教育与应用方法到产业工具 | c06 | nc034 | Andrew Ng | medium | 应用 AI 方法、课程和工具流程进入企业落地。 |
| vc11 | 本土部署生态适配 | c06 | nc036 | Zhang Peng | high | 国产芯片和本土产业部署能力。 |
| vc12 | 前史资源迁移到大模型竞争 | c07 | nc037, nc038, nc039, nc040, nc041 | Wang Xiaochuan, Jiang Daxin, Liang Wenfeng | medium | 搜索、微软研究、量化、算力和开放验证进入大模型。 |
| vc13 | 创业叙事与资本聚合 | c08 | nc042, nc045 | Wang Xiaochuan, Yan Junjie | medium | 用叙事和资本市场接口聚合资源、治理和长期融资。 |
| vc14 | 创始人集中控制 | c08 | nc043 | Yan Junjie | high | 创始人同时掌握治理、经营和技术最高角色。 |
| vc15 | 技术团队组装 | c08 | nc046 | Yang Zhilin | high | 通过关键技术发明者团队建立模型公司可信度。 |
| vc16 | 产品窗口选择 | c08 | nc044, nc047, nc048, nc049 | Yan Junjie, Yang Zhilin, Jiang Daxin, Zhang Peng | medium | 角色、多模态、长上下文、Agent、汽车/终端等入口选择。 |
| vc17 | 公司公共政策与监管接口 | c09 | nc050, nc052 | Sam Altman | high | 代表 AI 公司进入政策、监管和部署讨论。 |
| vc18 | 前沿公司治理与组织韧性 | c09 | nc051, nc053 | Sam Altman, Yan Junjie | medium | 董事会、员工、合作伙伴、资本市场和公众信任。 |
| vc19 | 安全治理共同语言 | c10 | nc054, nc055, nc056, nc057, nc058, nc059, nc060 | Stuart Russell, Nick Bostrom, Paul Christiano | high | 风险、对齐、人类兼容转化为教材、框架、组织和议程。 |
| vc20 | 科学问题与 AI 系统验证 | c11 | nc061, nc062, nc063 | Demis Hassabis | high | 用高难科学问题检验和扩散 AI 系统能力。 |
| vc21 | 科学智能组织议程 | c11 | nc064, nc065, nc069, nc070 | Liu Tieyan, Weinan E | high | 把 AI for Science 建成跨学科、跨机构长期议程。 |
| vc22 | 科学模型与工具基础设施 | c11 | nc066, nc067, nc068 | Zhang Linfeng | high | 从 Deep Potential 到科学工具体系和工业 R&D 基础设施。 |
| vc23 | 顶级实验室整合 | c12 | nc071 | Demis Hassabis | high | 多个顶级研究团队整合为统一实验室并围绕长期目标组织资源。 |
| vc24 | 国家级/区域研究平台 | c12 | nc072, nc073, nc074 | Liu Tieyan, Huang Tiejun | high | 国家级学院、非营利研究院、区域 AI 创新中心。 |
| vc25 | 大学-产业研究院桥接 | c12 | nc075, nc076, nc077 | Zhang Yaqin, Lin Dahua | high | 用研究院或实验室形式承接大学与产业间的长期转化。 |
| vc26 | 组织内技术权威 | c13 | nc078 | Jeff Dean | high | 组织变化中保留技术权威并服务多个研究单元。 |
| vc27 | 国家工程与工业技术权威 | c13 | nc079 | Wang Haifeng | high | 在公司 CTO、国家工程中心和学术共同体之间形成技术权威。 |
| vc28 | 跨机构技术接口 | c13 | nc080 | Tang Jie, Huang Tiejun, Zhang Yaqin | medium | 高校、创业公司、研究院之间保持技术路线和组织接口。 |
| vc29 | 公共议题与研究叙事影响 | c13 | nc081, nc082 | Fei-Fei Li, Geoffrey Hinton, Nick Bostrom | medium | 技术贡献扩展为公共议题、治理叙事或风险讨论。 |
| vc30 | 应用范式转译 | c13 | nc083, nc084 | Wang Haifeng, Lin Dahua | medium | 将模型或视觉研究转译为产业应用范式和商业化路径。 |

## v2 结构变化

| v1 簇 | v2 拆分 |
|---|---|
| c05 大规模工程平台 | vc05 企业基础设施平台；vc06 开发者与企业生态平台；vc07 云与模型家族平台 |
| c06 学术到产业转译 | vc08 高校知识资产到公司技术底座；vc09 结构发明到企业模型服务；vc10 教育与应用方法到产业工具；vc11 本土部署生态适配 |
| c08 技术创业组织 | vc13 创业叙事与资本聚合；vc14 创始人集中控制；vc15 技术团队组装；vc16 产品窗口选择 |
| c13 多重技术权威与公共影响 | vc26 组织内技术权威；vc27 国家工程与工业技术权威；vc28 跨机构技术接口；vc29 公共议题与研究叙事影响；vc30 应用范式转译 |

## v2 画像表达

AI 领军人才的画像在 `v2` 中不再是 13 个较粗簇，而是 30 个可组合机制。更准确的说法是：

AI 领军人才通常至少在一个高杠杆机制上形成强影响，并通过另一个机制扩散。例如结构发明者需要工具、课程或公司平台扩散；平台型人物需要工程系统和开发者生态；创业者需要前史资源、产品窗口和资本组织；安全治理型人物需要概念框架和研究组织。

## 当前最稳机制

| v2 簇 | 稳定原因 |
|---|---|
| vc02 结构与训练范式发明 | 论文证据和后续复用强。 |
| vc03 任务、基准与工具标准化 | 公共产物清晰，改变共同体工作流。 |
| vc04 教育、解释与人才放大 | 多人物、多材料支撑，能解释人才进入路径。 |
| vc05 企业基础设施平台 | Google/百度样本清晰。 |
| vc19 安全治理共同语言 | Russell/Bostrom/Christiano 的机制一致。 |
| vc20-vc22 AI for Science 子簇 | DeepMind、Liu Tieyan、Zhang Linfeng、Weinan E 共同支撑。 |

## 仍需验证机制

| v2 簇 | 缺口 |
|---|---|
| vc07 云与模型家族平台 | 目前主要依赖 Zhou Jingren/Qwen，需补更多阿里官方和周靖人材料。 |
| vc13 创业叙事与资本聚合 | 媒体资料占比较高，需要官方融资、招股书或访谈补强。 |
| vc16 产品窗口选择 | 很多是产品观察，需要更多用户/产品/技术报告证据。 |
| vc18 前沿公司治理与组织韧性 | Sam Altman 样本强，但同类样本少。 |
| vc28 跨机构技术接口 | 机制合理，但边界还需通过更多人物验证。 |
