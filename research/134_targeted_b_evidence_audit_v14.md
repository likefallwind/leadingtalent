# 定向 B 级补证审计 v14：m06 / m29 / m30

## 审计目的

v13 后还有 72 条 B 级能力。直接平均补全部 B 级能力会浪费精力，也会把研究重新带回“资料越多越重要”的误区。

本轮只审计会影响机制升降级的 B 级能力：

- `m06 云 AI 与模型家族平台`
- `m29 企业侧视觉 AI 基础设施`
- `m30 AI 芯片与算力硬件底座`

## 审计结论摘要

| 机制 | 本轮结论 |
|---|---|
| m06 | 平台证据增强，但人物-平台组织链仍不够直接；继续保持 core-candidate，不升 core。 |
| m29 | 贾佳亚 / SmartMore 工业视觉链路可以补强，相关 B 级能力可升 A。 |
| m30 | AMD、Cerebras、Tenstorrent 的部分硬件底座能力可以升 A；但 m30 仍保持 core-candidate。 |

## 能力证据等级调整

| normalized_id | 人物 | 原等级 | 新等级 | 调整理由 |
|---|---|---|---|---|
| nc189 | 贾佳亚 | B | A | SmartMore 官方资料支撑 industrial vision platform、quality control、traceability、MOA；CUHK Innovation 资料支撑 Jia Jiaya 创办 SmartMore 并聚焦 industrial optimization and automation / vision AI。 |
| nc200 | Lisa Su | B | A | AMD 官方 leadership、ROCm for AI、Instinct accelerators、Developer Cloud 资料共同支撑 CPU/GPU/软件/开放生态组成 AI/HPC 基础设施路径。 |
| nc203 | Andrew Feldman | B | A | Cerebras 官方资料支撑 Andrew Feldman 等创办 Cerebras，并将 wafer-scale computing 推向市场；Cerebras/WEF/TIME 资料支撑 AI training/inference hardware platform。 |
| nc207 | Jim Keller | B | A | Tenstorrent 官方 vision 页面明确 AI Graph Processors、RISC-V CPUs、configurable chiplets、software stack，并关联 Jim Keller 对 AI models as graphs 的公开说明。 |

## 明确不调整的能力

| normalized_id | 人物 | 保持等级 | 原因 |
|---|---|---|---|
| nc187 | 雷军 | B | 它是 m06 反向边界能力：小米 AIoT/EV/智能硬件产品生态不等同于云模型平台。产品生态证据强，但“AI 影响范围”仍需更细产品级材料。 |
| nc191 | 颜水成 | B | 企业 AI Lab 组织路径明确，但具体组织产出和平台影响需要更多一手材料。 |
| nc193 | 张祥雨 | B | 论文部分强，但“工业视觉组织中的基础模型落地”仍主要来自人物资料和公开报道。 |
| nc201 | Lisa Su | B | “替代性 AI 算力供给和开放生态路线”是合理机制判断，但竞争效果和采用规模还需要更多外部采用链路。 |

## m06 审计结果

Alibaba Cloud Model Studio、Qwen API 和 Qwen 技术报告能增强 `m06 云 AI 与模型家族平台` 的机制证据：

- Model Studio 官方文档证明平台集成 Qwen 系列、官方 Qwen API 和 OpenAI-compatible API。
- Model list 和 service page 证明 Qwen models、AI-native apps、AI solutions、Model Studio 是 Alibaba Cloud 企业/开发者服务的一部分。
- Qwen 系列技术报告中可见 Jingren Zhou 的技术贡献链。

但 m06 仍不升 core：

| 原因 | 说明 |
|---|---|
| 人物组织链不够直接 | 公开技术报告能证明技术贡献，但不能完整证明个人对云平台、模型家族和商业化组织链的主导。 |
| 与 m05 重叠 | 企业内部 AI 基础设施和云上模型平台仍需区分。 |
| 与 m30 重叠 | 云平台可能使用 AI 芯片和算力硬件，但两者外部行为不同。 |
| 与 m11 重叠 | AI 应用入口和云模型平台不能混写。 |

因此，m06 继续保持 core-candidate。

## m29 审计结果

贾佳亚 / SmartMore 链条已经足以补强工业视觉路径：

| 证据链 | 说明 |
|---|---|
| Jiaya Jia -> SmartMore | CUHK Innovation 资料支撑 SmartMore 由 Jia Jiaya 创办。 |
| SmartMore -> industrial vision | SmartMore 官方资料支撑 smart industrial vision platform、quality control、traceability。 |
| SmartMore -> MOA | SmartMore 官方资料支撑 Manufacturing Optimization and Automation。 |

因此，`nc189` 从 B 升 A。

但 m29 仍不升 core：

| 原因 | 说明 |
|---|---|
| 视觉产业路径内部差异大 | 安防视觉、城市视觉、工业视觉、制造优化不是同一条窄机制。 |
| 与 m07 重叠 | 研究资产到公司技术底座和企业视觉基础设施有交叉。 |
| 与 m17 重叠 | 视觉模型效率、工具链和工业部署约束不能全部归入 m29。 |
| 与 m28 重叠 | 机器人/车载/具身视觉接口不能简单归入企业视觉基础设施。 |

因此，m29 继续保持 core-candidate。

## m30 审计结果

m30 的证据增强最明显。本轮可把 `nc200/nc203/nc207` 从 B 升 A。

| 子路径 | 代表 | 证据状态 |
|---|---|---|
| GPU / CUDA / AI accelerated computing | Jensen Huang | 已是 A |
| AMD heterogeneous AI/HPC infrastructure | Lisa Su | 升 A |
| Wafer-scale training/inference platform | Andrew Feldman | 升 A |
| LPU / inference compute | Jonathan Ross | 已是 A |
| 中国 AI processor / 端云协同 | 陈天石 | 已是 A |
| AI Graph Processors / RISC-V AI platform | Jim Keller | 升 A |

m30 仍不升 core：

| 原因 | 说明 |
|---|---|
| 与 m05 相邻 | NVIDIA/AMD 同时也是企业 AI 基础设施供应商。 |
| 与 m06 相邻 | 云模型平台和底层 AI 加速器高度耦合。 |
| 与 m19 相邻 | 国产 AI 芯片和国家级基础设施语境容易重叠。 |
| 与 m28 相邻 | 端侧/机器人/车载芯片可能支撑物理世界智能，但不等同于具身平台。 |
| 仍需采用链路 | AMD/Cerebras/Tenstorrent 的生态和客户采用链路仍不如 NVIDIA/Groq/寒武纪清楚。 |

因此，m30 保持 core-candidate。

## 证据强度变化

| 等级 | v13 | 本轮调整 | 调整后 |
|---|---:|---:|---:|
| A | 135 | +4 | 139 |
| B | 72 | -4 | 68 |
| C | 0 | 0 | 0 |

## 对最终封版的影响

本轮补证后，三个边界敏感机制都可以进入最终报告，但都必须带边界条件：

| 机制 | 最终报告写法 |
|---|---|
| m06 | core-candidate：云 AI、模型家族、开发者平台；不等同于企业内部平台、硬件底座或应用入口。 |
| m29 | core-candidate：企业侧视觉 AI 基础设施；不等同于所有视觉研究、视觉工具链或机器人视觉接口。 |
| m30 | core-candidate：AI 芯片与算力硬件底座；不等同于云平台、国家平台、企业平台或具身智能平台。 |

当前已经具备生成最终版画像报告的条件。最终报告不应再继续扩大样本，而应整合：

- 第一批 60 人完整覆盖。
- 470 条原子事实。
- 299 条原始能力。
- 207 条归并能力。
- A 139 / B 68 / C 0。
- 19 core / 3 core-candidate / 9 important / 3 watch。
- v13 权重模型和本轮 B 级补证审计。

