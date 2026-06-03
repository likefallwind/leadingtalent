# AI 芯片与算力硬件底座边界审计 v1

## 审计问题

此前 `watch-ai-chip-substrate` 主要由陈天石样本支撑，因此只能作为观察项。本轮加入 Jensen Huang、Lisa Su、Andrew Feldman、Jonathan Ross、Jim Keller 等对照样本后，需要重新判断：

`AI 芯片与算力硬件底座` 是否应从 watch 升为主机制候选？

## 结论

建议将 `watch-ai-chip-substrate` 升为 `m30 AI 芯片与算力硬件底座` core-candidate。

不建议直接升为 core。原因是该机制虽然已不再是单样本，但仍与 m05、m06、m19、m28 有强边界重叠，需要在最终报告中带边界使用。

## 为什么可以升为 core-candidate

| 判断 | 证据 |
|---|---|
| 不再是单一样本 | Jensen Huang、Lisa Su、Andrew Feldman、Jonathan Ross、陈天石、Jim Keller 覆盖 GPU、异构计算、wafer-scale、inference LPU、端云 AI 芯片、RISC-V AI processor。 |
| 跨训练和推理 | Cerebras 更偏训练算力，Groq 更偏推理算力，NVIDIA/AMD 覆盖数据中心平台。 |
| 跨端云和数据中心 | 陈天石样本覆盖云端、终端、机器人等芯片路线，NVIDIA/AMD/Cerebras/Groq 更偏数据中心和服务化算力。 |
| 改变外部行为 | 这些机制改变研究者、模型公司、云服务商和开发者获得 AI 算力的方式。 |
| 不能被 m05/m06/m19/m28 完全吸收 | 它们相邻但外部行为不同：这里的核心是处理器架构和算力供给。 |

## 为什么暂不升 core

| 风险 | 说明 |
|---|---|
| 与 m05 重叠 | NVIDIA 和 AMD 同时也是企业基础设施平台，不能把所有企业 AI 基础设施都算成芯片机制。 |
| 与 m06 重叠 | AI 芯片常被云模型平台使用，但芯片机制不是云服务和模型家族本身。 |
| 与 m19 重叠 | 陈天石样本涉及中国科学院和国产替代语境，但 m30 不是国家平台机制。 |
| 与 m28 重叠 | 端侧、机器人和车载芯片可以支撑物理世界智能，但 m30 不等同于机器人平台。 |
| 证据不均衡 | NVIDIA/Groq/寒武纪证据较强，AMD/Cerebras/Tenstorrent 仍需要更多产品采用和生态影响链路补强。 |

## m30 边界定义

`m30 AI 芯片与算力硬件底座` 指：

通过处理器架构、加速器、数据中心硬件系统、推理硬件、端云 AI 芯片或硬件-软件协同生态，改变 AI 模型训练、推理、部署和使用成本的人才机制。

不包括：

| 不包括 | 应归入 |
|---|---|
| 只是使用 GPU 或云算力训练模型 | m06 或对应模型/平台机制 |
| 企业内部 AI 工程平台 | m05 |
| 国家级开放算力平台、标准和公共基础设施 | m19 |
| 车载/机器人/具身智能产品平台 | m28 |
| AI 应用产品入口 | m11 |

## m30 代表人物

| 人物 | 机制贡献 |
|---|---|
| Jensen Huang | GPU、CUDA、networking、系统和软件生态组成 AI 加速计算底座。 |
| Lisa Su | CPU/GPU/软件/开放生态组成异构 AI/HPC 基础设施竞争路径。 |
| Andrew Feldman | wafer-scale chip/system 路线改变大模型训练算力供给。 |
| Jonathan Ross | LPU / inference compute 路线强化大模型推理算力瓶颈。 |
| 陈天石 | 中国 AI 处理器、端云协同和商业深度学习芯片路径。 |
| Jim Keller | 高性能 CPU/SoC 架构经验向 AI processor 和 RISC-V 平台迁移。 |

## 对正式权重模型的影响

建议在下一版正式权重模型中加入：

| mechanism_id | 机制 | 层级 | report_weight | 使用规则 |
|---|---|---|---:|---|
| m30 | AI 芯片与算力硬件底座 | core-candidate | 0.75 | 带边界保留，不与 m05/m06/m19/m28 混同。 |

同时将 watch 机制从 4 个降为 3 个：

| watch_id | 状态 |
|---|---|
| watch-local-deploy | 保持 watch |
| watch-cross-interface | 保持 watch |
| watch-application-translation | 保持 watch |
| watch-ai-chip-substrate | 升为 m30 core-candidate |

## 对总画像的影响

m30 的加入说明 AI 领军人才画像中必须保留“算力物理底座”路径。这个路径不是传统意义上的半导体人物标签，而是：

让 AI 模型能以新的成本、延迟、规模或能耗结构被训练、部署和使用的人。

这条路径应与技术路线、模型平台、应用入口、国家基础设施和具身智能平台并列作为边界敏感候选机制。

