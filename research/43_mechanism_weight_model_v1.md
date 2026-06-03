# 28 个主机制初步权重模型 v1

## 目的

本文件基于 `42_mechanism_cluster_dedup_audit_v1.md` 中建议保留的 28 个主机制，建立第一版权重模型。

这个模型不是给人物排名，也不是判断某个机制“高级”或“低级”。它的用途是：

1. 区分高频机制和低频高杠杆机制。
2. 区分证据强、证据中等和仍需补样的机制。
3. 避免最终画像把所有机制等权处理。
4. 为后续补样和最终报告提供优先级。

## 权重维度

| 维度 | 取值 | 说明 |
|---|---|---|
| observed_persons | 数量 | 当前矩阵中直接代表该机制的人物数。 |
| evidence_grade | A / B / mixed | 该机制对应能力的总体证据强度。 |
| leverage_type | 技术 / 共同体 / 平台 / 组织 / 产业 / 治理 / 科学 | 机制主要改变的外部行为。 |
| frequency_class | high / medium / low | 当前样本中出现频率，不等于重要性。 |
| leverage_class | foundational / amplifying / organizational / translational / governance | 该机制产生杠杆的方式。 |
| priority | core / important / watch | 当前画像使用优先级。 |

## 权重模型表

| mechanism_id | 主机制 | observed_persons | evidence_grade | leverage_type | frequency_class | leverage_class | priority | 解释 |
|---|---|---:|---|---|---|---|---|---|
| m01 | 长期路线与范式判断 | 3 | mixed | 技术 | medium | foundational | core | Hinton/Sutton/LeCun 支撑多年尺度路线判断，是基础画像机制。 |
| m02 | 结构与训练范式发明 | 4 | A | 技术 | medium | foundational | core | GAN、Transformer、ResNet、ResNeXt 等证据强，低频但改变模型构建方式。 |
| m03 | 共同体工作流标准化 | 3 | A | 共同体 | medium | amplifying | core | ImageNet、OpenMMLab、教材等改变训练、评测、复用和比较。 |
| m04 | 教育解释与人才入口 | 3 | A/mixed | 共同体 | medium | amplifying | core | Andrew Ng、Karpathy、Olah 显示教学/解释能改变人才进入路径。 |
| m05 | 企业基础设施平台 | 2 | A | 平台 | medium | organizational | core | Jeff Dean、Wang Haifeng 支撑企业级 AI 生产能力。 |
| m06 | 云与模型家族平台 | 1 | B | 平台 | low | organizational | important | Zhou Jingren/Qwen 机制重要，但样本和人物一手材料仍需补。 |
| m07 | 研究资产到公司技术底座 | 2 | A/mixed | 产业 | medium | translational | core | Tang Jie、Zhang Peng 体现高校知识资产进入公司技术栈。 |
| m08 | 前史资源迁移到模型竞争 | 3 | B | 产业 | medium | translational | important | 搜索、微软研究、量化资源进入大模型窗口，解释力强但需更多一手材料。 |
| m09 | 创业叙事与资本接口 | 2 | B | 产业 | medium | translational | important | 资本聚合和叙事影响创业资源配置，但媒体材料仍占比高。 |
| m10 | 技术团队组装 | 1 | A | 组织 | low | organizational | important | Yang Zhilin 样本强，但目前样本少。 |
| m11 | 产品窗口与落地入口 | 4 | B | 产业 | high | translational | core | 多个中国大模型创业样本共同支撑，是产品化路径核心机制。 |
| m12 | 公司公共政策接口 | 1 | A | 治理 | low | governance | important | Sam Altman 样本强，但同类样本少。 |
| m13 | 前沿公司治理韧性 | 2 | mixed | 组织 | medium | governance | important | Sam Altman/Yan Junjie 支撑公司治理和资本韧性，但需更多同类样本。 |
| m14 | 安全治理共同语言 | 3 | A/mixed | 治理 | medium | governance | core | Russell/Bostrom/Christiano 支撑概念、教材、研究议程路径。 |
| m15 | 科学问题与 AI 系统验证 | 1 | A | 科学 | low | foundational | core | Demis Hassabis/DeepMind 低频但杠杆极高，不能因频率低而降权。 |
| m16 | 科学智能组织议程 | 2 | A/mixed | 科学 | medium | organizational | core | Liu Tieyan、Weinan E 支撑 AI for Science 跨学科组织议程。 |
| m17 | 科学模型与工具基础设施 | 1 | A/mixed | 科学 | low | translational | important | Zhang Linfeng 路径证据强，但当前样本集中。 |
| m18 | 顶级实验室整合 | 1 | A | 组织 | low | organizational | core | Demis Hassabis 的 DeepMind 路径低频但对前沿研究组织极关键。 |
| m19 | 国家级/区域研究平台 | 2 | A/mixed | 组织 | medium | organizational | important | Liu Tieyan/Huang Tiejun 支撑国家级或区域研究平台机制。 |
| m20 | 大学-产业研究院桥接 | 2 | A/mixed | 组织 | medium | translational | important | Zhang Yaqin、Lin Dahua 支撑大学与产业间长期转化承接。 |
| m21 | 国家工程与工业技术权威 | 1 | A | 平台 | low | organizational | important | Wang Haifeng 样本强，但目前人物集中。 |
| m22 | 公共议题与研究叙事影响 | 3 | B | 治理 | medium | governance | important | Fei-Fei Li、Hinton、Bostrom 支撑公共叙事，但影响量化不足。 |
| m23 | 前沿模型 scaling 与路线判断 | 2 | A | 技术 | medium | foundational | core | Dario/Ilya 补强大模型 scaling 和跨阶段前沿路线判断。 |
| m24 | 安全导向前沿公司 | 1 | A | 组织/治理 | low | governance | core | Anthropic 路径显示安全可以成为公司组织原则，低频但高杠杆。 |
| m25 | 单目标安全实验室 | 1 | B | 组织/治理 | low | governance | important | SSI 组织目标清楚，但公开产出少，暂不列为最高确定性。 |
| m26 | 长期机器学习共同体 | 1 | A/mixed | 共同体 | low | amplifying | core | 周志华路径说明教材、研究组和方法路线能形成长期共同体。 |
| m27 | 跨学科 AGI 研究院 | 1 | A/mixed | 组织 | low | organizational | core | 朱松纯/BIGAI 路径显示 AGI 研究院和人才组织是独立机制。 |
| m28 | 经典视觉方法到机器人平台 | 1 | A/mixed | 技术/平台 | low | translational | important | 张正友路径显示标准视觉方法能进入机器人和具身智能平台。 |

## 权重解释

### core 机制

`core` 机制不是“出现最多”的机制，而是当前画像必须保留的主轴。

| core 类型 | 机制 |
|---|---|
| 技术基础型 | m01、m02、m15、m23 |
| 共同体放大型 | m03、m04、m26 |
| 平台组织型 | m05、m07、m11、m18、m27 |
| 科学与安全型 | m14、m16、m24 |

这些机制如果从画像中删除，会明显降低解释力。

### important 机制

`important` 机制有明确价值，但当前或样本少，或证据主要为 B，或边界还需要后续人物验证。

| important 类型 | 机制 |
|---|---|
| 平台和产业转译 | m06、m08、m09、m10、m17、m19、m20、m21、m28 |
| 治理和公共接口 | m12、m13、m22、m25 |

这些机制不能删除，但在最终报告里应标注为“重要但需继续补样”。

### watch 机制

第一次去重后，`vc11`、`vc28`、`vc30` 暂未进入 28 个主机制，因此不在本表中单独赋权。它们应在后续补样后决定是否升为主机制。

## 频率与重要性的关系

当前模型明确区分两类重要机制：

| 类型 | 例子 | 判断 |
|---|---|---|
| 高频/中频核心机制 | m02、m03、m04、m11、m14 | 多人物支撑，能作为画像稳定骨架。 |
| 低频高杠杆机制 | m15、m18、m24、m26、m27 | 样本少但外部行为改变极大，不能因低频降权。 |

这点非常关键：如果简单按频率排序，会低估 ImageNet、AlphaFold、Anthropic、SSI、BIGAI、张氏标定法这类低频但高杠杆路径。

## 当前最稳定的画像骨架

如果要用最少机制概括当前画像，建议使用以下 14 个 `core` 机制作为骨架：

| mechanism_id | 主机制 |
|---|---|
| m01 | 长期路线与范式判断 |
| m02 | 结构与训练范式发明 |
| m03 | 共同体工作流标准化 |
| m04 | 教育解释与人才入口 |
| m05 | 企业基础设施平台 |
| m07 | 研究资产到公司技术底座 |
| m11 | 产品窗口与落地入口 |
| m14 | 安全治理共同语言 |
| m15 | 科学问题与 AI 系统验证 |
| m16 | 科学智能组织议程 |
| m18 | 顶级实验室整合 |
| m23 | 前沿模型 scaling 与路线判断 |
| m24 | 安全导向前沿公司 |
| m26 | 长期机器学习共同体 |
| m27 | 跨学科 AGI 研究院 |

说明：这里实际是 15 个机制。保留 15 个比强行压成 14 个更诚实，因为 `m26` 和 `m27` 分别代表中国长期机器学习共同体和 AGI 研究院，不能合并。

## 后续补样优先级

| 需要补样的机制 | 优先人物 | 目的 |
|---|---|---|
| m06 云与模型家族平台 | Zhou Jingren、黄学东、沈向洋 | 验证云 AI 平台和模型家族组织机制。 |
| m08 前史资源迁移到模型竞争 | 李开复、沈向洋、黄学东 | 验证跨国研究、投资和产品前史资源迁移。 |
| m09 创业叙事与资本接口 | 李开复、Wang Xiaochuan | 验证资本、叙事和创业生态机制。 |
| m12 公司公共政策接口 | Dario Amodei、Sam Altman | 验证公司进入政策接口的不同方式。 |
| m19 国家级/区域研究平台 | 高文、黄铁军 | 验证鹏城实验室、智源等平台机制。 |
| m28 经典视觉方法到机器人平台 | 张正友、朱松纯、余凯 | 验证视觉/机器人/具身智能路线。 |

## 当前使用建议

在最终报告之前，建议这样使用权重模型：

| 场景 | 建议 |
|---|---|
| 写阶段性结论 | 用 15 个 core 机制作为主骨架，再列 important 机制作为补充。 |
| 做补样 | 优先补 important 中样本少但可能升 core 的机制。 |
| 做最终画像 | 不按频率排序，而按杠杆类型组织。 |
| 做人才评估框架 | 不要求每个人覆盖多个机制，允许低频单点高杠杆。 |
