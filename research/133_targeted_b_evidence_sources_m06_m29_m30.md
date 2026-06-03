# m06 / m29 / m30 定向 B 级补证资料

本文件只收集影响 `m06 云 AI 与模型家族平台`、`m29 企业侧视觉 AI 基础设施`、`m30 AI 芯片与算力硬件底座` 三个边界敏感机制的补证材料。

目标不是平均补全部 B 级能力，而是判断哪些 B 级能力可以升 A，哪些仍应保留 B。

## m06 云 AI 与模型家族平台

| source_id | 来源 | 用途 | 证据判断 |
|---|---|---|---|
| target_s01 | Alibaba Cloud Model Studio 文档：`https://www.alibabacloud.com/help/doc-detail/2579562.html` | 证明 Model Studio 集成 Qwen 系列、官方 Qwen API 和 OpenAI-compatible API。 | A for platform |
| target_s02 | Alibaba Cloud Model Studio model list：`https://www.alibabacloud.com/help/en/model-studio/user-guide/model/` | 证明 Qwen 系列作为模型服务和 API 平台的一部分。 | A for platform |
| target_s03 | Alibaba Cloud services page：`https://www.alibabacloud.com/en/services` | 证明 Alibaba Cloud 将 Qwen models、AI-native apps、AI solutions 和 Model Studio 放在企业/开发者 AI 服务中。 | A for platform |
| target_s04 | Qwen / Qwen2 / Qwen-VL / Qwen-Image 技术报告 | 证明 Jingren Zhou 出现在 Qwen 系列技术报告作者链中。 | A for technical contribution, B for platform leadership chain |

结论：m06 的平台证据更强，但 `Zhou Jingren -> Qwen 技术链 -> Alibaba Cloud Model Studio 平台链` 仍不是完全一手人物组织材料。因此不把 m06 直接升 core，也不把相关人物能力强行全升 A。

## m29 企业侧视觉 AI 基础设施

| source_id | 来源 | 用途 | 证据判断 |
|---|---|---|---|
| target_s05 | SmartMore global：`https://global.smartmore.com/` | 证明 SmartMore 提供 smart industrial vision platform、quality control、traceability 和 Manufacturing Optimization and Automation。 | A |
| target_s06 | CUHK Innovation SmartMore article：`https://www.innovation.cuhk.edu.hk/articles/81?cid=2` | 证明 SmartMore 由 Professor JIA Jiaya 创办，并聚焦 industrial optimization and automation / vision AI。 | A |
| target_s07 | CUHK / SmartMore 相关人物资料 | 辅助证明 Jiaya Jia 的计算机视觉研究和 SmartMore 创办链路。 | A/B |

结论：`贾佳亚 -> SmartMore -> 工业视觉 / 智能制造优化` 链条可以从 B 升 A，因为人物、公司、技术方向和工业场景都有官方或机构资料支撑。

## m30 AI 芯片与算力硬件底座

| source_id | 来源 | 用途 | 证据判断 |
|---|---|---|---|
| target_s08 | AMD Lisa Su leadership：`https://www.amd.com/en/corporate/leadership-lisa-su` | 证明 Lisa Su 是 AMD chair and CEO，并具备半导体研发和业务领导背景。 | A |
| target_s09 | AMD ROCm for AI：`https://www.amd.com/en/products/software/rocm/ai.html` | 证明 ROCm 面向 LLM training、AMD Instinct accelerators、Developer Cloud 和 AI development。 | A |
| target_s10 | AMD Instinct accelerators：`https://www.amd.com/en/products/accelerators/instinct.html` | 证明 AMD Instinct + ROCm 面向 AI models、HPC workloads、data center AI accelerators。 | A |
| target_s11 | AMD Developer Cloud：`https://www.amd.com/en/developer/resources/cloud-access/amd-developer-cloud.html` | 证明 AMD Developer Cloud 提供 Instinct GPUs 访问，用于 AI、ML、HPC workloads。 | A |
| target_s12 | Cerebras company page：`https://www.cerebras.ai/company/` | 证明 Andrew Feldman 等创办 Cerebras，并将 wafer-scale computing 推向市场。 | A |
| target_s13 | Cerebras / WEF / TIME 资料 | 证明 Wafer-Scale Engine、AI training/inference platform 和大模型训练算力系统。 | A/B |
| target_s14 | Groq about / product：`https://groq.com/about-us`、`https://groq.com/` | 证明 Jonathan Ross、Groq LPU、inference compute 路线。 | A |
| target_s15 | Tenstorrent vision：`https://tenstorrent.com/vision` | 证明 Tenstorrent 设计 AI Graph Processors、high-performance RISC-V CPUs、configurable chiplets 和 software stack，并由 Jim Keller 公开讲解。 | A |

结论：m30 的证据强度进一步增强，但仍不直接升 core。原因不是证据少，而是边界复杂：它必须和 m05、m06、m19、m28 区分。

