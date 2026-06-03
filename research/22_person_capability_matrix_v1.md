# 人物-能力矩阵 v1

本文件将 `20_normalized_capabilities_v1.md` 中的 84 条归并能力映射回 32 个已进入事实抽取的唯一人物。它用于观察每个人的能力组合，而不是给人物贴类型标签。

## 计数说明

| 项目 | 数量 |
|---|---:|
| 已抽取唯一人物 | 32 |
| v1 归并能力 | 84 |
| v1 候选簇 | 13 |

## 人物-能力矩阵

| person | nc_count | cluster_coverage | normalized_capabilities | 当前主要杠杆 |
|---|---:|---|---|---|
| Geoffrey Hinton | 4 | c01, c13 | nc001, nc002, nc006, nc082 | 长期神经网络路线、方法积累和公共影响 |
| Jeff Dean | 3 | c05, c13 | nc023, nc024, nc078 | 大规模工程平台和组织内技术权威 |
| Fei-Fei Li | 2 | c03, c13 | nc012, nc081 | ImageNet/基准塑造和以人为本 AI 公共议题 |
| Sam Altman | 4 | c09 | nc050, nc051, nc052, nc053 | 公司治理、监管接口和部署型组织 |
| Demis Hassabis | 4 | c11, c12 | nc061, nc062, nc063, nc071 | AI for Science、里程碑系统和统一实验室 |
| Liang Wenfeng | 3 | c07 | nc039, nc040, nc041 | 量化资源迁移、效率路线和开放验证 |
| Tang Jie | 4 | c06, c13 | nc030, nc031, nc032, nc080 | 清华知识系统到智谱技术底座的转译 |
| Liu Tieyan | 3 | c11, c12 | nc064, nc065, nc072 | AI for Science 组织议程和跨机构研究管理 |
| Yang Zhilin | 2 | c08 | nc046, nc047 | 关键技术团队组装和产品窗口选择 |
| Zhang Peng | 4 | c06, c08 | nc030, nc035, nc036, nc049 | GLM 产品线、国产生态适配和模型能力叙事 |
| Lin Dahua | 3 | c03, c12, c13 | nc013, nc077, nc084 | OpenMMLab 工具链、视觉研究组织和应用推进 |
| Wang Haifeng | 4 | c05, c13 | nc025, nc026, nc079, nc083 | 百度平台连续演进、飞桨/文心和国家工程接口 |
| Stuart Russell | 2 | c10 | nc054, nc055 | AI 安全教材化和 human-compatible AI 研究议程 |
| Nick Bostrom | 3 | c10, c13 | nc056, nc057, nc082 | 超级智能风险框架和公共风险叙事 |
| Paul Christiano | 3 | c10 | nc058, nc059, nc060 | 对齐问题拆解、ARC 和安全评估议程 |
| Richard Sutton | 3 | c01, c03 | nc003, nc014, nc015 | 强化学习教材、理论共同体和路线原则化 |
| Yann LeCun | 2 | c01 | nc004, nc005 | 卷积网络、自监督路线和工业基础研究 |
| Chris Olah | 3 | c04 | nc016, nc017, nc018 | 机械可解释性和解释型传播 |
| Andrew Ng | 3 | c04, c06 | nc019, nc022, nc034 | 在线教育、人才训练入口和应用 AI 工具化 |
| Andrej Karpathy | 2 | c04 | nc020, nc021 | 工程教学转译和非正式学习者网络 |
| Ian Goodfellow | 2 | c01, c02 | nc006, nc007 | GAN 训练范式和方法共同语言 |
| Aidan Gomez | 2 | c02, c06 | nc008, nc033 | Transformer 架构到 Cohere 企业模型服务 |
| Kaiming He | 2 | c02 | nc009, nc011 | ResNet 瓶颈突破和视觉路线扩展 |
| Saining Xie | 2 | c02 | nc010, nc011 | ResNeXt 架构空间扩展和视觉表示研究 |
| Wang Xiaochuan | 3 | c07, c08 | nc037, nc040, nc042 | 搜索产品经验、资源约束产品化和创业叙事 |
| Jiang Daxin | 2 | c07, c08 | nc038, nc048 | 微软研究组织迁移和多模态/终端入口 |
| Yan Junjie | 4 | c08, c09 | nc043, nc044, nc045, nc053 | 创始人集中控制、多模态产品组合和资本市场接口 |
| Zhou Jingren | 3 | c05 | nc027, nc028, nc029 | 阿里云/Qwen 企业级模型平台和开源商业张力 |
| Huang Tiejun | 3 | c12, c13 | nc073, nc074, nc080 | 智源/北大非营利研究平台和区域 AI 生态 |
| Zhang Yaqin | 3 | c12, c13 | nc075, nc076, nc080 | 清华 AIR、微软经验和大学产业桥接 |
| Zhang Linfeng | 3 | c11 | nc066, nc067, nc068 | Deep Potential、科学工具体系和工业 R&D 基础设施 |
| Weinan E | 2 | c11 | nc069, nc070 | 数学/计算科学到 AI for Science 研究议程 |

## 高覆盖人物

当前 `nc_count` 不能简单理解为“更强”，因为每个人资料厚度不同。但高覆盖人物通常表现为跨多个机制形成杠杆。

| person | nc_count | 解释 |
|---|---:|---|
| Geoffrey Hinton | 4 | 同时有长期技术路线、方法体系和公共影响。 |
| Sam Altman | 4 | 集中在组织控制和公共接口，不是技术结构发明。 |
| Demis Hassabis | 4 | 同时覆盖 AI for Science 和研究组织平台。 |
| Tang Jie | 4 | 同时覆盖学术到产业转译和多重技术权威。 |
| Zhang Peng | 4 | 同时覆盖清华孵化产品线和技术创业组织。 |
| Wang Haifeng | 4 | 同时覆盖企业平台和国家工程接口。 |
| Yan Junjie | 4 | 同时覆盖创始人控制、产品组合和资本接口。 |

## 低覆盖但高杠杆人物

低覆盖不代表不重要，可能说明其影响集中在单一高杠杆点。

| person | nc_count | 高杠杆点 |
|---|---:|---|
| Fei-Fei Li | 2 | ImageNet 改变了视觉研究的任务和评测方式。 |
| Aidan Gomez | 2 | Transformer 结构贡献转化为企业模型平台。 |
| Kaiming He | 2 | ResNet 解决深层网络训练瓶颈。 |
| Saining Xie | 2 | ResNeXt 扩展视觉网络架构设计空间。 |
| Weinan E | 2 | 把数学和计算科学组织进 AI for Science 议程。 |

## 矩阵使用方式

| 用途 | 做法 |
|---|---|
| 看人物画像 | 读该人物覆盖的 `nc` 和 `cluster_coverage`，不要用单一标签概括。 |
| 看能力高频 | 转到 `23_cluster_frequency_v1.md` 查看簇覆盖。 |
| 看证据链 | 回到 `20_normalized_capabilities_v1.md` 的 `source_caps`，再追溯到事实表。 |
| 看缺口 | 对 `nc_count` 低但名单中重要的人物，优先补事实而不是直接下结论。 |
