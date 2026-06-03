# 第三轮研究进展报告

## 本轮新增

本轮新增下一批 12 人，重点补强前两轮不足的四类路径：

| 路径 | 人物 |
|---|---|
| 安全/治理/风险问题设定 | Stuart Russell、Nick Bostrom、Paul Christiano |
| 理论路线长期坚持 | Richard Sutton、Yann LeCun |
| 教育传播和解释型研究 | Chris Olah、Andrew Ng、Andrej Karpathy |
| 模型结构和视觉架构发明 | Ian Goodfellow、Aidan Gomez、Kaiming He、Saining Xie |

新增文件：

| 文件 | 内容 |
|---|---|
| `11_source_seeds_next12.md` | 下一批 12 人来源入口 |
| `12_next12_atomic_facts.md` | 72 条新原子事实 |
| `13_next12_capability_map.md` | 36 条新原子能力 |

## 当前数据规模

| 数据层 | 当前规模 |
|---|---:|
| 人物登记 | 61 人 |
| 已进入事实抽取的人物 | 24 人 |
| 优先 12 人扩展事实 | 72 条 |
| 下一批 12 人事实 | 72 条 |
| 第一批/扩展/下一批能力合计 | 94 条 |

能力总数计算口径：`02_pilot` 8 条、`07_priority12` 24 条、`09_priority12_expanded` 34 条、`13_next12` 36 条。注意其中存在重复和同义项，后续需要去重合并。

## 第三轮后更清晰的发现

### 1. “传播”不是外围能力，而是人才放大器

Andrew Ng、Andrej Karpathy、Chris Olah、Richard Sutton 显示，教材、课程、博客、可视化文章和开源教学代码可以改变人才进入领域的路径。它们不是简单“科普”，而是把复杂方法转化为共同语言和训练入口。

### 2. “安全治理”至少有两条不同路径

Sam Altman 代表公司治理、监管接口和组织危机整合；Stuart Russell、Nick Bostrom、Paul Christiano 代表教材化、概念框架化、研究议程化的安全/对齐路径。这两类不能混成一个维度。

### 3. “结构发明”是一类独立高杠杆能力

GAN、Transformer、ResNet、ResNeXt 这类贡献的共同点不是某个应用结果，而是提出可被后续大量研究复用的训练范式或架构设计空间。它们会改变领域后续几年甚至十几年的默认方法。

### 4. “长期路线判断”与“长期问题意识”不同

Hinton 体现长期围绕神经网络路线积累方法和人才；Sutton 的 The Bitter Lesson 更像长期历史规律判断；LeCun 则体现工业基础研究中的未来路线主张。这些都属于长期性，但机制不同。

### 5. “学术到产业转译”需要拆得更细

Tang Jie/Zhipu 是高校知识系统到大模型公司的转译；Aidan Gomez/Cohere 是基础模型结构到企业平台公司的转译；Andrew Ng/Landing AI 是教育和应用 AI 方法到企业工具流程的转译。这三种路径不应合并为同一个粗标签。

## 当前能力簇候选

以下簇仍是候选，不是最终画像：

| 候选簇 | 代表能力 | 代表人物 |
|---|---|---|
| 长期技术路线 | 非共识阶段坚持、路线原则化、未来路线主张 | Geoffrey Hinton、Richard Sutton、Yann LeCun |
| 结构/范式发明 | GAN、Transformer、ResNet、ResNeXt 等可复用结构 | Ian Goodfellow、Aidan Gomez、Kaiming He、Saining Xie |
| 任务/基准/工具塑造 | ImageNet、OpenMMLab、教材、benchmark | Fei-Fei Li、Lin Dahua、Richard Sutton |
| 教育与解释放大 | 在线课程、CS231n、可视化解释、开发者教学 | Andrew Ng、Andrej Karpathy、Chris Olah |
| 大规模工程和平台 | TensorFlow/TPU/Pathways、PaddlePaddle/ERNIE | Jeff Dean、Wang Haifeng |
| 学术到产业转译 | 清华/智谱、Transformer/Cohere、DeepLearning.AI/Landing AI | Tang Jie、Aidan Gomez、Andrew Ng |
| AI for Science | AlphaFold、科学智能组织、科学基座模型 | Demis Hassabis、Liu Tieyan |
| 资源迁移与效率突破 | 量化投资资源到 DeepSeek、开放模型验证 | Liang Wenfeng |
| 安全/治理共同语言 | AIMA、Superintelligence、ARC、CHAI | Stuart Russell、Nick Bostrom、Paul Christiano |
| 组织控制与公共接口 | OpenAI 治理危机、监管表达、公司部署 | Sam Altman |

## 当前更稳的中间画像

AI 领军人才不是“会研究、会管理、会创业”的泛化集合，而是能把某种技术、问题、组织或传播形式变成领域级杠杆的人。

这种杠杆目前至少有十种形态：

| 杠杆形态 | 作用 |
|---|---|
| 技术路线杠杆 | 让领域在长期方向上重新下注 |
| 结构范式杠杆 | 让后续研究复用新的训练范式或模型结构 |
| 任务基准杠杆 | 改变领域如何训练、评测和比较 |
| 教育传播杠杆 | 改变人才进入领域的速度和方式 |
| 工程平台杠杆 | 把研究能力变成组织级基础设施 |
| 产业转译杠杆 | 把学术成果转为公司、产品和市场入口 |
| 科学问题杠杆 | 用 AI 改写高价值科学问题的求解方式 |
| 资源效率杠杆 | 通过算力、资金、效率路线改变竞争边界 |
| 安全治理杠杆 | 让风险、对齐和人类兼容成为研究与政策议题 |
| 组织公共接口杠杆 | 代表 AI 组织处理监管、治理、员工和公众信任 |

## 下一步

下一轮应优先补中国大模型创业横向批和平台生态批：

| 批次 | 人物 | 目的 |
|---|---|---|
| 中国大模型创业横向批 | 王小川、姜大昕、闫俊杰、张鹏、杨植麟、梁文锋 | 比较技术团队、产品窗口、资本组织和路线选择 |
| 平台生态批 | 周靖人、王海峰、黄铁军、林达华、张亚勤 | 比较企业平台、国家级研究平台、开源平台和产业生态 |
| 视觉/感知产业批 | 张正友、何恺明、谢赛宁、张祥雨、印奇、汤晓鸥 | 比较论文范式、工程视觉系统和产业应用路径 |

## 结论边界

当前能力数量已经接近第一次聚类所需规模，但仍不能给最终画像。原因是：

1. 能力项还没有去重，同一机制可能被不同文字重复描述。
2. 中国创业者和平台型人物的横向事实仍不足。
3. “成就事实”和“促成成功的能力”之间仍需更严格区分。
4. 需要把能力项按证据强度分层，避免媒体叙事过度影响结论。
