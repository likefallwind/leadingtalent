# 归并能力 v13 增量：AI 芯片 / 算力硬件底座

本批次新增 10 条归并能力，编号 `nc198-nc207`。

## v13 normalized capabilities

| normalized_id | 人物 | 归并能力 | 来源能力 | 证据强度 | 机制指向 | 备注 |
|---|---|---|---|---|---|---|
| nc198 | Jensen Huang | 把 GPU、CUDA、networking、系统和软件生态组织成 AI 加速计算底座。 | cap282/cap283 | A | chip-substrate / m05 | 强化 AI 算力硬件不是单颗芯片，而是硬件-软件-生态系统。 |
| nc199 | Jensen Huang | 把数据中心计算资源重构为面向 AI 工作负载的加速计算平台。 | cap284 | A | chip-substrate / m06-boundary | 与云模型平台相邻，但底层杠杆不同。 |
| nc200 | Lisa Su | 把 CPU、GPU、软件和开放生态组织成异构 AI/HPC 基础设施竞争路径。 | cap285/cap286 | B | chip-substrate | 证据足以支撑机制判断，但需更多 AMD AI 采用链路补强。 |
| nc201 | Lisa Su | 在主导性 GPU 平台之外形成替代性的 AI 算力供给和开放生态路线。 | cap287 | B | chip-substrate | 边界为“算力供给竞争”，不是模型平台。 |
| nc202 | Andrew Feldman | 把大模型训练瓶颈转化为 wafer-scale chip 和专用系统设计。 | cap288/cap289 | A | chip-substrate | 强化训练算力系统作为独立路径。 |
| nc203 | Andrew Feldman | 将 AI training compute 做成专用硬件系统创业路径。 | cap290 | B | chip-substrate / m09b-boundary | 与创业生态相邻，但核心杠杆是训练硬件。 |
| nc204 | Jonathan Ross | 把大模型推理延迟、吞吐和成本瓶颈转化为 LPU / inference compute 架构。 | cap291/cap292 | A | chip-substrate | 强化推理算力不同于训练算力。 |
| nc205 | Jonathan Ross | 将 inference compute 从通用 GPU 训练逻辑中拆出为独立硬件和服务化入口。 | cap293 | A | chip-substrate / m11-boundary | 与产品入口相邻，但核心是推理硬件供给。 |
| nc206 | 陈天石 | 把深度学习算法效率问题转化为商业 AI 处理器、端云协同和中国 AI 芯片供给路线。 | cap294/cap295/cap296 | A | chip-substrate / m08-boundary | 强化中国 AI 芯片路径不是个例。 |
| nc207 | Jim Keller | 把高性能 CPU/SoC 架构经验迁移到 AI processor、RISC-V 和 graph compute 平台。 | cap297/cap298 | B | chip-substrate | 证据为 B，机制用于边界补充。 |

## 证据强度增量

| 等级 | 新增数量 | normalized_id |
|---|---:|---|
| A | 6 | nc198, nc199, nc202, nc204, nc205, nc206 |
| B | 4 | nc200, nc201, nc203, nc207 |
| C | 0 | - |

