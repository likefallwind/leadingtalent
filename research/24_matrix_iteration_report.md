# 矩阵化阶段报告

## 本轮新增

本轮将 `v1` 能力库从文字归并推进到可分析矩阵。

| 文件 | 内容 |
|---|---|
| `22_person_capability_matrix_v1.md` | 32 个已抽取唯一人物到 84 条归并能力的映射 |
| `23_cluster_frequency_v1.md` | 13 个候选簇的能力数量和人物覆盖 |

## 统计修正

之前第四轮报告和 `v1` 聚类报告把“已进入事实抽取的人物”写成 36 人，这是按批次相加导致的重复计数。因为 Liang Wenfeng、Yang Zhilin、Zhang Peng、Wang Haifeng 在不同批次重复出现，当前唯一人物数应为 32。

| 项目 | 数量 |
|---|---:|
| 批次计数 | 36 |
| 唯一人物计数 | 32 |
| 重复人物 | Liang Wenfeng, Yang Zhilin, Zhang Peng, Wang Haifeng |

## 矩阵后的发现

### 1. 高频不等于重要

`c13 多重技术权威与公共影响` 覆盖 9 人，是当前覆盖最广的簇，但它边界较松，未来应拆分。相反，`c02 结构与范式发明` 只覆盖 4 人，但 GAN、Transformer、ResNet、ResNeXt 都是强杠杆贡献。

### 2. 稀有能力可能更决定领域方向

以下能力不一定高频，但对领域走向影响极大：

| 能力 | 代表 |
|---|---|
| 提出可复用训练范式 | Ian Goodfellow / GAN |
| 提出通用模型架构 | Aidan Gomez / Transformer |
| 改变评测和任务定义 | Fei-Fei Li / ImageNet |
| 建立安全治理共同语言 | Stuart Russell / Nick Bostrom / Paul Christiano |

### 3. 中国大模型创业路径被拆细

矩阵显示，中国大模型创业不是一个统一画像，而是由多种前史资源进入大模型窗口：

| 机制 | 代表 |
|---|---|
| 搜索产品和用户理解 | Wang Xiaochuan |
| 微软研究组织迁移 | Jiang Daxin |
| 创始人集中控制 | Yan Junjie |
| 技术团队组装 | Yang Zhilin |
| 清华孵化和国产生态适配 | Zhang Peng |
| 量化算力和效率路线 | Liang Wenfeng |

### 4. 平台类能力至少分三层

| 层级 | 代表 |
|---|---|
| 企业基础设施平台 | Jeff Dean、Wang Haifeng、Zhou Jingren |
| 研究组织平台 | Demis Hassabis、Liu Tieyan、Huang Tiejun、Zhang Yaqin |
| 工具/开源平台 | Lin Dahua、Andrew Ng、Andrej Karpathy、Chris Olah |

## 当前画像的矩阵化表达

AI 领军人才画像可以初步写成：

一个人成为 AI 领军人才，并不要求同时覆盖所有能力簇。更常见的是，他在一个或两个高杠杆机制上形成压倒性影响，再通过组织、传播、平台或产业转译把这个影响扩散出去。

有些人是“结构发明杠杆”，例如 Goodfellow、Aidan Gomez、Kaiming He；有些人是“平台组织杠杆”，例如 Jeff Dean、Wang Haifeng；有些人是“教育传播杠杆”，例如 Andrew Ng、Karpathy、Olah；有些人是“安全问题设定杠杆”，例如 Russell、Bostrom、Christiano；有些人是“创业窗口和资源迁移杠杆”，例如 Liang Wenfeng、Yang Zhilin、Yan Junjie、Wang Xiaochuan。

## 下一步

下一步应做两件事：

| 任务 | 目的 |
|---|---|
| 拆分 `c13`, `c06`, `c08`, `c05` 四个边界较松的簇 | 得到更干净的最终画像结构 |
| 为每个 `nc` 能力补证据强度细分 | 区分官方/论文强证据和媒体叙事弱证据 |
