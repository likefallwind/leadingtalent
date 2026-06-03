# 能力簇覆盖与频率 v1

本文件基于 `20_normalized_capabilities_v1.md` 和 `22_person_capability_matrix_v1.md`，统计 13 个候选簇的能力数量和人物覆盖。

## 簇频率表

| cluster_id | 簇名 | nc_count | person_count | observed_persons | 当前判断 |
|---|---|---:|---:|---|---|
| c01 | 长期技术路线 | 6 | 4 | Geoffrey Hinton, Richard Sutton, Yann LeCun, Ian Goodfellow | 中等证据，偏理论/学术路线 |
| c02 | 结构与范式发明 | 5 | 4 | Ian Goodfellow, Aidan Gomez, Kaiming He, Saining Xie | 强证据，论文和后续复用清晰 |
| c03 | 任务基准与工具 | 4 | 3 | Fei-Fei Li, Lin Dahua, Richard Sutton | 强证据，公共产物改变共同体行为 |
| c04 | 教育与解释放大 | 7 | 3 | Chris Olah, Andrew Ng, Andrej Karpathy | 强证据，改变人才进入路径 |
| c05 | 大规模工程平台 | 7 | 3 | Jeff Dean, Wang Haifeng, Zhou Jingren | 强证据，企业级平台样本清晰 |
| c06 | 学术到产业转译 | 7 | 4 | Tang Jie, Zhang Peng, Aidan Gomez, Andrew Ng | 强证据，但内部机制需细分 |
| c07 | 前史资源迁移 | 5 | 3 | Wang Xiaochuan, Jiang Daxin, Liang Wenfeng | 中等证据，中国大模型创业批支撑 |
| c08 | 技术创业组织 | 8 | 5 | Wang Xiaochuan, Yan Junjie, Yang Zhilin, Jiang Daxin, Zhang Peng | 中等证据，个人官方资料强度不均 |
| c09 | 组织控制与公共接口 | 4 | 2 | Sam Altman, Yan Junjie | 中等证据，样本少但机制清楚 |
| c10 | 安全治理共同语言 | 7 | 3 | Stuart Russell, Nick Bostrom, Paul Christiano | 强证据，非工程型领军路径清晰 |
| c11 | AI for Science | 10 | 4 | Demis Hassabis, Liu Tieyan, Zhang Linfeng, Weinan E | 强证据，科学问题组织路径清晰 |
| c12 | 研究组织与平台 | 7 | 5 | Demis Hassabis, Liu Tieyan, Huang Tiejun, Zhang Yaqin, Lin Dahua | 强证据，研究院/实验室/区域平台样本清晰 |
| c13 | 多重技术权威与公共影响 | 7 | 9 | Jeff Dean, Wang Haifeng, Tang Jie, Huang Tiejun, Zhang Yaqin, Fei-Fei Li, Geoffrey Hinton, Nick Bostrom, Lin Dahua | 中等证据，覆盖广但边界较松 |

## 高频簇

按人物覆盖数看，最广的簇是：

| 排名 | 簇 | person_count | 解释 |
|---|---|---:|---|
| 1 | c13 多重技术权威与公共影响 | 9 | 很多领军者会跨越组织边界，但该簇边界仍需拆。 |
| 2 | c08 技术创业组织 | 5 | 中国大模型创业样本强化了产品窗口、创始人控制和团队组装。 |
| 3 | c12 研究组织与平台 | 5 | 实验室、研究院和区域平台是领域级影响的重要载体。 |
| 4 | c01 长期技术路线 | 4 | 主要来自理论/基础研究人物。 |
| 5 | c02 结构与范式发明 | 4 | 来自模型结构和训练范式发明者。 |
| 6 | c06 学术到产业转译 | 4 | 横跨高校、企业模型服务和应用 AI 工具。 |
| 7 | c11 AI for Science | 4 | 由科学问题、模型方法和科学工具共同支撑。 |

## 稀有但高杠杆簇

| 簇 | person_count | 为什么高杠杆 |
|---|---:|---|
| c02 结构与范式发明 | 4 | 单个结构或训练范式能改变大量后续研究。 |
| c03 任务基准与工具 | 3 | 数据集、工具箱、教材能改变整个共同体工作流。 |
| c10 安全治理共同语言 | 3 | 不是工程产物，但改变风险、对齐和政策讨论的语言。 |
| c09 组织控制与公共接口 | 2 | 样本少，但前沿 AI 公司治理和监管接口影响极大。 |

## 当前最需要拆分的簇

| 簇 | 为什么需要拆 | 可能拆法 |
|---|---|---|
| c13 多重技术权威与公共影响 | 覆盖 9 人，边界最松 | 拆成组织内技术权威、公共议题影响、国家工程接口 |
| c06 学术到产业转译 | Tang Jie、Aidan Gomez、Andrew Ng、Zhang Peng 的机制不同 | 拆成高校孵化、结构到公司、教育到产业、国产生态适配 |
| c08 技术创业组织 | 创始人控制、技术团队、产品窗口和资本接口混在一起 | 拆成团队组装、产品窗口、资本治理、创始人集中控制 |
| c05 大规模工程平台 | Google、百度、阿里平台机制不同 | 拆成基础设施平台、云/模型平台、开发者生态 |

## 对最终画像的含义

当前频率表说明，AI 领军人才画像不应只看能力出现次数。更关键的是能力是否能改变共同体行为。

| 类型 | 例子 | 画像含义 |
|---|---|---|
| 高频机制 | 多重技术权威、技术创业组织、研究组织平台 | 说明很多领军者需要跨组织形成影响。 |
| 低频高杠杆机制 | 结构发明、任务基准、安全共同语言 | 说明少数能力一旦成立，会强烈改变领域方向。 |
| 待拆机制 | 学术到产业转译、技术创业组织、大规模工程平台 | 说明画像正在变细，不能回退到粗标签。 |
