# 第一轮小样本原子能力试抽取

本文件不是最终结论，而是验证研究路径：先从公开事实出发，拆出更细的能力，再等待样本扩大后聚类。

## 已用来源线索

| 人物 | 来源线索 |
|---|---|
| Geoffrey Hinton | 个人官网、University of Toronto、Nobel Prize |
| Yoshua Bengio | Mila 官方介绍 |
| Ilya Sutskever | SSI 官网、OpenAI Superalignment 旧文、公开新闻 |
| Demis Hassabis | Google DeepMind 官方介绍 |
| 唐杰 | 清华相关公开材料、智谱 AI 公开资料 |
| 刘铁岩 | 北京中关村学院官方介绍 |
| 梁文锋 | DeepSeek 公开报道、公司相关资料 |
| 闫俊杰 | MiniMax 官方管理层信息 |

## 试抽取：原子事实

| fact_id | person | 原子事实 | source_level | confidence |
|---|---|---|---|---|
| f001 | Geoffrey Hinton | 多伦多大学个人主页列出其长期研究包括反向传播、Boltzmann machines、distributed representations、deep belief nets 等。 | A | high |
| f002 | Geoffrey Hinton | 2013-2023 年间 Hinton 在 Google 兼职工作，并成为 VP and Engineering Fellow。 | A | high |
| f003 | Yoshua Bengio | Mila 官方介绍称 Bengio 是蒙特利尔大学教授，并是 Mila 创始人和科学顾问。 | A | high |
| f004 | Ilya Sutskever | SSI 官网将公司目标表述为“one goal and one product: a safe superintelligence”。 | A | high |
| f005 | Ilya Sutskever | OpenAI 曾公布 Superalignment 团队由 Ilya Sutskever 和 Jan Leike 共同领导。 | A | high |
| f006 | Demis Hassabis | Google DeepMind 官方介绍称 Google DeepMind 由 CEO Demis Hassabis 领导。 | A | high |
| f007 | 唐杰 | 清华公开材料将唐杰表述为清华大学教授、智谱 AI 首席科学家。 | A/B | high |
| f008 | 刘铁岩 | 北京中关村学院官方介绍称刘铁岩为中关村学院院长，并列出其微软亚洲研究院与 Microsoft Research AI for Science 经历。 | A | high |
| f009 | 闫俊杰 | MiniMax 官方管理层页面称 Yan Junjie 为 Founder、Chairman、CEO and CTO。 | A | high |
| f010 | 梁文锋 | 多家公开报道将梁文锋识别为 DeepSeek 创始人，并指出 DeepSeek 在 2025 年后进入全球 AI 讨论核心。 | B/C | medium |

## 试抽取：原子能力

| capability_id | 原子能力 | 证据事实 | observed_in | confidence | 临时聚类 |
|---|---|---|---|---|---|
| cap001 | 能在长期不被主流完全看好的技术路线中持续积累方法和学生网络 | f001, f002 | Geoffrey Hinton | medium | 长期技术信念 |
| cap002 | 能把个人研究议题扩展成研究机构、人才网络和地区 AI 生态 | f003 | Yoshua Bengio | medium | 机构化研究生态 |
| cap003 | 能把抽象安全目标转化为组织使命，并用单一目标约束公司方向 | f004, f005 | Ilya Sutskever | medium | 使命聚焦 |
| cap004 | 能将科学研究、工程系统和组织管理结合成持续产出的实验室 | f006 | Demis Hassabis | medium | 研究组织能力 |
| cap005 | 能把高校研究体系中的知识图谱/大模型研究连接到商业公司和产品体系 | f007 | 唐杰 | medium | 学术到产业转译 |
| cap006 | 能在跨国研究机构、国家级学院和 AI for Science 之间转移组织经验 | f008 | 刘铁岩 | medium | 跨组织迁移 |
| cap007 | 能同时承担创始人、董事长、CEO、CTO 等角色，将技术路线与公司控制权集中推进 | f009 | 闫俊杰 | medium | 技术型创业控制 |
| cap008 | 能以高效率模型和开放技术成果改变全球对中国大模型能力的判断 | f010 | 梁文锋 | low | 反向突破与效率路线 |

## 第一轮观察

当前只从 8 个样本抽取，不能得出完整画像，但已经能看到几个不应被预设维度覆盖掉的能力方向：

| 观察 | 说明 |
|---|---|
| 领军人才不只靠“研究能力” | Hinton/Bengio 是研究路线与人才网络，唐杰/刘铁岩是研究到组织和产业的连接，闫俊杰/梁文锋则体现公司控制和产品/模型路线。 |
| “组织化能力”可能是关键中间层 | 很多人的影响力不是单篇论文，而是把方法、团队、资源、平台和叙事组织起来。 |
| “技术路线选择”比泛泛的“创新”更可分析 | 例如长期坚持神经网络、选择安全超级智能、选择高效率开源大模型，都是具体路线选择。 |
| 需要记录时代窗口 | 同一能力在不同阶段价值不同，例如 ImageNet 时代的数据集能力、大模型时代的算力/推理效率能力、AI for Science 时代的跨学科建模能力。 |

## 下一步

1. 将 61 人全部建立 source register。
2. 每人先抽取 8-15 条原子事实。
3. 每 10 人合并一次原子能力同义项。
4. 达到约 100 条原子能力后再做第一轮聚类。
5. 对高频能力和稀有高杠杆能力分别写解释，避免只看频率。
