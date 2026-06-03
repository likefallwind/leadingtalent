# 正式机制权重模型 v13 增量

## 更新目的

`125_formal_mechanism_weight_model_v12.md` 在 v12 口径下建立了正式机制权重模型。当时 `watch-ai-chip-substrate` 仍是观察项。

`130_ai_chip_substrate_boundary_audit_v1.md` 完成后，`watch-ai-chip-substrate` 已有足够跨样本证据，应升级为 `m30 AI 芯片与算力硬件底座` core-candidate。

本文件只记录 v13 权重增量，不重写整个权重模型。

## v13 权重变更

| 项目 | v12 | v13 |
|---|---|---|
| core 机制 | 19 | 19 |
| core-candidate 机制 | 2 | 3 |
| important 机制 | 9 | 9 |
| watch 机制 | 4 | 3 |
| 新增 core-candidate | - | m30 AI 芯片与算力硬件底座 |
| 移出 watch | watch-ai-chip-substrate | 已升为 m30 |

## 新增机制权重

| mechanism_id | 机制 | 当前层级 | report_weight | confidence | 使用规则 | 权重理由 |
|---|---|---|---:|---|---|---|
| m30 | AI 芯片与算力硬件底座 | core-candidate | 0.75 | A/B mixed | 带边界保留 | 跨 Jensen Huang、Lisa Su、Andrew Feldman、Jonathan Ross、陈天石、Jim Keller 等样本，已不再是单点观察；但与 m05/m06/m19/m28 边界重叠，暂不升 core。 |

## watch 机制更新

| watch_id | v13 状态 |
|---|---|
| watch-local-deploy | 保持 watch |
| watch-cross-interface | 保持 watch |
| watch-application-translation | 保持 watch |
| watch-ai-chip-substrate | 移出 watch，升级为 m30 core-candidate |

## m30 使用边界

`m30 AI 芯片与算力硬件底座` 只用于解释：

- 处理器架构、GPU、LPU、wafer-scale chip、RISC-V AI processor 等底层算力供给。
- 硬件-软件协同、数据中心系统、训练/推理加速和端云 AI 芯片。
- 改变模型训练、推理、部署成本、延迟、能耗或规模结构的机制。

不用于解释：

| 不应归入 m30 | 更合适机制 |
|---|---|
| 只是使用云算力训练模型 | m06 或对应模型平台机制 |
| 企业内部 AI 工程生产平台 | m05 |
| 国家级开放平台、标准和公共基础设施 | m19 |
| 车载、机器人、具身智能产品平台 | m28 |
| AI 应用入口和用户场景 | m11 |

## v13 后的正式权重使用规则

| 层级 | report_weight | 使用规则 |
|---|---:|---|
| core-high | 1.00 | 最终画像必须保留，是解释 AI 领军人才的主骨架。 |
| core | 0.90 | 正式画像应保留，但表达时可根据路径合并呈现。 |
| core-lowfreq | 0.85 | 低频但高杠杆，不能因样本少而删除。 |
| core-candidate | 0.75 | 进入画像，但必须带边界条件，暂不作为无条件主轴。 |
| important-high | 0.65 | 作为重要补充，能解释部分人物和路径。 |
| important | 0.55 | 有明确价值，但样本、证据或边界仍需补强。 |
| watch | 0.30 | 只作为观察项，不进入正式主画像。 |

## 当前结论

v13 后，正式画像报告应把 `m30 AI 芯片与算力硬件底座` 放入“算力物理底座和硬件-软件协同”路径。

但在最终封版前，m30 仍必须写成 core-candidate，而不是 core。

