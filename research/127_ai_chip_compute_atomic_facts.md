# AI 芯片 / 算力硬件底座原子事实

本文件记录 AI 芯片和算力硬件对照样本的原子事实。目标是判断 `watch-ai-chip-substrate` 是否只是陈天石个例。

## Jensen Huang

| fact_id | 原子事实 | 来源 | 备注 |
|---|---|---|---|
| chip_f001 | NVIDIA 官方董事会资料称 Jensen Huang 于 1993 年创办 NVIDIA，并自公司成立起担任 president、CEO 和董事会成员。 | chip_s01 | A |
| chip_f002 | NVIDIA 官方资料将公司定位为 accelerated computing 的开创者，并将 AI 与高性能计算作为核心应用场景。 | chip_s02 | A |
| chip_f003 | NVIDIA 的 AI 影响不是单个芯片，而是 GPU、CUDA、networking、系统和软件生态组成的加速计算平台。 | chip_s01/chip_s02 | A，机制判断 |
| chip_f004 | Jensen Huang 样本说明 AI 算力底座可以通过硬件、软件、开发者生态和数据中心系统共同形成。 | chip_s01/chip_s02 | A，机制判断 |

## Lisa Su

| fact_id | 原子事实 | 来源 | 备注 |
|---|---|---|---|
| chip_f005 | AMD 官方资料称 Lisa Su 是 AMD chair and CEO，并具备长期半导体研发和业务领导背景。 | chip_s03 | A |
| chip_f006 | AMD AI infrastructure 资料把 CPU、GPU、软件、developer cloud 和开放生态放入 AI-ready data center 叙事。 | chip_s04 | B |
| chip_f007 | Lisa Su 样本说明 AI 算力底座不仅是单一 GPU，也包括异构计算、数据中心平台和开放软件生态。 | chip_s03/chip_s04 | B，机制判断 |
| chip_f008 | AMD 路径更接近“AI/HPC 算力基础设施竞争者”，不等同于云模型平台或应用产品入口。 | chip_s03/chip_s04 | B，边界判断 |

## Andrew Feldman

| fact_id | 原子事实 | 来源 | 备注 |
|---|---|---|---|
| chip_f009 | Cerebras 公司资料显示 Andrew Feldman 是 Cerebras 领导团队成员，并与公司创业团队相关。 | chip_s05 | A |
| chip_f010 | Cerebras 路线聚焦 wafer-scale AI compute，用大芯片和系统设计缓解大模型训练中的数据移动和并行计算瓶颈。 | chip_s05/chip_s06 | B |
| chip_f011 | Cerebras 样本说明 AI 算力底座可以通过“改变芯片尺度和系统形态”形成，而不是只通过通用 GPU 扩展。 | chip_s05/chip_s06 | B，机制判断 |
| chip_f012 | Andrew Feldman 样本强化了“训练算力系统”作为独立硬件创业路径的存在。 | chip_s05/chip_s06 | B，机制判断 |

## Jonathan Ross

| fact_id | 原子事实 | 来源 | 备注 |
|---|---|---|---|
| chip_f013 | Groq 官方资料称 Jonathan Ross 是 Groq CEO and founder。 | chip_s07 | A |
| chip_f014 | Groq 官方资料将 LPU 描述为面向 inference / language 的专用处理器路径。 | chip_s07/chip_s08 | A |
| chip_f015 | Groq 样本说明 AI 算力底座可以围绕推理延迟、吞吐、开发者使用成本和服务化入口重构。 | chip_s07/chip_s08 | A，机制判断 |
| chip_f016 | Jonathan Ross 路径与训练 GPU 或 wafer-scale training chip 不同，主要强化 inference compute 作为独立瓶颈。 | chip_s07/chip_s08 | A，边界判断 |

## 陈天石

| fact_id | 原子事实 | 来源 | 备注 |
|---|---|---|---|
| chip_f017 | 寒武纪官方资料将陈天石与寒武纪创始人及 CEO 角色联系在一起。 | chip_s09 | A |
| chip_f018 | 中国科学院英文资料称寒武纪开发了面向深度学习应用的商业处理器，并把目标放在 AI 芯片市场。 | chip_s10 | A |
| chip_f019 | 寒武纪资料显示其关注云端、终端、机器人等智能芯片和端云协同路径。 | chip_s09/chip_s10 | A |
| chip_f020 | 陈天石样本说明中国 AI 芯片路径可以从研究所技术积累转为商业 AI 加速器和端云硬件底座。 | chip_s09/chip_s10 | A，机制判断 |

## Jim Keller

| fact_id | 原子事实 | 来源 | 备注 |
|---|---|---|---|
| chip_f021 | Tenstorrent 公开资料将公司定位于 AI processor、RISC-V 和相关计算架构路线。 | chip_s11 | B |
| chip_f022 | 公开资料显示 Jim Keller 与 Tenstorrent 的技术和组织角色相关。 | chip_s11/chip_s12 | B |
| chip_f023 | Jim Keller 样本体现通用 CPU/SoC 架构经验向 AI processor 和 graph compute 平台迁移。 | chip_s11/chip_s12 | B，机制判断 |
| chip_f024 | Tenstorrent 路径与 NVIDIA/AMD 的规模化 GPU 平台不同，更强调架构替代、开放 ISA 和 AI 处理器设计。 | chip_s11/chip_s12 | B，边界判断 |

## 跨样本原子判断

| fact_id | 原子事实 | 来源 | 备注 |
|---|---|---|---|
| chip_f025 | AI 芯片 / 算力硬件路径至少包含 GPU 加速计算、异构 CPU/GPU 数据中心、wafer-scale training、inference LPU、端云 AI 芯片、RISC-V AI processor 六种形态。 | chip_s01-chip_s12 | A/B，归纳判断 |
| chip_f026 | 这些样本共同说明 AI 算力硬件不是单个国家或单个公司的个例，而是跨公司、跨训练/推理、跨端云场景的基础设施路径。 | chip_s01-chip_s12 | A/B，机制判断 |
| chip_f027 | 该机制与 m05 企业基础设施平台相邻，但 m05 更强调企业内部生产能力，AI 芯片机制更强调算力物理底座和处理器架构。 | chip_s01-chip_s12 | 边界判断 |
| chip_f028 | 该机制与 m06 云 AI 与模型家族平台相邻，但 m06 更强调云服务、模型家族和开发者平台，AI 芯片机制更强调底层加速器供给。 | chip_s01-chip_s12 | 边界判断 |
| chip_f029 | 该机制与 m19 国家级技术标准与 AI 基础设施相邻，但 m19 更强调标准、公共平台和国家级组织，AI 芯片机制更强调硬件商业和架构路线。 | chip_s09/chip_s10 | 边界判断 |
| chip_f030 | 该机制与 m28 具身/车载/机器人智能平台相邻，但 m28 更强调物理世界智能系统，AI 芯片机制更强调底层计算供给。 | chip_s01-chip_s12 | 边界判断 |

