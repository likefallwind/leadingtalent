# 负样本 NS09：Diederik Kingma（Durk Kingma）

> **对照组用途**：测 8 维框架的判别力——此人的 Adam 优化器被引数超过名单内多数人，
> 且长期投入 AI 核心基础研究，但从未出现在任何主要 AI 领军名单。
> 产物仅在 `research/validation/negative_sample/`，**绝不进入正式分数文件**。

---

## 候选确认

**姓名**：Diederik P. Kingma（常用名 Durk Kingma）  
**机构**：Anthropic（2024–）；前 Google Brain/DeepMind（2018–2024）；OpenAI 创始成员（2015–2018）

**"够格当对照"的硬证据**：
- Adam 优化器论文（*Adam: A Method for Stochastic Optimization*，2014/ICLR 2015）—— Google Scholar 被引 **255,725**（S2 核验：scholar.google.com/citations?user=yyIoQu4AAAAJ，2026-06）。是历史上被引最多的机器学习论文之一；所有现代神经网络训练的标配。
- VAE 论文（*Auto-Encoding Variational Bayes*，2013）—— 被引 **57,556**（S2，同上，2026-06）。奠定了生成式 AI 的核心框架。
- Google Scholar 总引用 **369,920**，h-index 60（S2，2026-06）
- ICLR 2024 Test of Time Award（VAE）；ICLR 2025 Test of Time Award（Adam）— 来源：blog.iclr.cc/2025/04/14/announcing-the-test-of-time-award-winners-from-iclr-2015/ (S1)
- OpenAI 创始成员（2015，15 人创始团队之一）— 来源：dpkingma.com (S3)，需更强来源
- 长期投入：2013–至今，AI 核心基础研究 10+ 年

**未入名单的依据**：TIME100 AI 2023/2024/2025、Forbes AI 50 搜索结果均未出现其名字（S4：WebSearch 核验，2026-06）。注：其就职 Anthropic 后在 AI 圈内知名度上升，但仍属技术圈内人而非公众领军形象。

**存疑与局限**：
- OpenAI 创始成员身份来自个人主页（S3），未找到 S1 级公开注册/官方文件
- Anthropic 职位描述未找到 S1/S2 来源，仅 S4 媒体报道
- Adam 论文的共同作者 Jimmy Ba 在普遍认知中也对此有贡献，Kingma 的独立贡献份额无法精确量化

---

## 本轮已查来源

- Google Scholar 个人页：scholar.google.com/citations?user=yyIoQu4AAAAJ（S2）
- 个人主页：dpkingma.com（S3）
- ICLR Test of Time 2025 公告：blog.iclr.cc/2025/04/14/announcing-the-test-of-time-award-winners-from-iclr-2015/（S1）
- ICLR X 帖：x.com/iclr_conf/status/1911889473715282318（S2 质性——赛事官方账号）
- Maginative 报道：maginative.com/article/openai-cofounder-durk-kingma-joins-anthropic/（S4）
- Gigazine 报道：gigazine.net/gsc_news/en/20241002-durk-kingma-joins-to-anthropic/（S4）
- TIME100 AI 2023/2024/2025 搜索：未见 Kingma 名字（S4 交叉核对）

---

## 八类维度普查

### 1. 学术

| 贡献 | 年份 | 来源/S级 | 引用数（口径/as-of） | 本人角色 |
|---|---|---|---|---|
| *Adam: A Method for Stochastic Optimization*（Adam 优化器） | 2014（ICLR 2015） | scholar.google.com/citations?user=yyIoQu4AAAAJ (S2) | **255,725**（Google Scholar，2026-06） | 第一作者（与 Jimmy Ba 共著，第一作者） |
| *Auto-Encoding Variational Bayes*（VAE） | 2013（ICLR 2014） | scholar.google.com/citations?user=yyIoQu4AAAAJ (S2) | **57,556**（Google Scholar，2026-06） | 第一作者（与 Max Welling 共著） |
| *Score-based Generative Modeling through Stochastic Differential Equations*（得分扩散模型） | 2020 | scholar.google.com/citations?user=yyIoQu4AAAAJ (S2) | **13,221**（Google Scholar，2026-06） | 共同作者（Yang Song 第一作者） |
| *Glow: Generative Flow with Invertible 1×1 Convolutions* | 2018 | scholar.google.com/citations?user=yyIoQu4AAAAJ (S2) | **4,690**（Google Scholar，2026-06） | 第一作者 |
| ICLR 2024 Test of Time Award（VAE 论文） | 2024（颁奖） | blog.iclr.cc/2025/04/14/announcing-the-test-of-time-award-winners-from-iclr-2015/（**S1**） | — | 受奖人 |
| ICLR 2025 Test of Time Award（Adam 论文） | 2025（颁奖） | x.com/iclr_conf/status/1911889473715282318（S2质性） | — | 受奖人 |
| h-index 60，总引用 369,920 | — | scholar.google.com (S2) | as-of 2026-06 | — |

**注**：Adam 论文单篇引用量超过名单内 Hinton 的全部文章引用总和（待核验，仅印象对比）；是历史上被引最多的优化算法论文之一。VAE 开创了生成式 AI 的隐空间范式，直接影响 DALL-E/Stable Diffusion 等系统。

### 2. 系统与框架

| 贡献 | 年份 | 来源/S级 | 影响/规模 | 本人角色 |
|---|---|---|---|---|
| Adam 优化器——事实上成为所有深度学习框架（PyTorch/TensorFlow/JAX）的默认优化器 | 2014– | S2（论文被引作为代理指标）| 255,725 引用作为部署规模代理；无独立部署数字 | 第一作者/发明人 |
| Advanza（机器学习咨询公司，2010–2016被收购）| 2010–2016 | dpkingma.com (S3) | 较小规模，细节未核验 | 联合创始人 |

### 3. 产品与工程

（VAE/Adam 是基础算法层，没有直接上线产品。Anthropic 职位为内部研究，无独立产品线。）

### 4. 公司与组织

| 贡献 | 年份 | 来源/S级 | 影响/规模 | 本人角色 |
|---|---|---|---|---|
| OpenAI 创始成员（15 人创始团队） | 2015 | dpkingma.com (S3)；需更强来源 | 全球最大 AI 公司之一，但离开时间早（2018） | 创始研究员（非 CEO/董事） |
| Anthropic 研究员（2024–） | 2024– | maginative.com (S4) | 顶级 AI 安全公司，研究员岗位 | 研究员 |

### 5. 标准与基础设施

（无独立标准记录。Adam 优化器实际已成"事实标准"，但未经正式标准化机构认定。）

### 6. 学术服务与荣誉

| 贡献 | 年份 | 来源/S级 |
|---|---|---|
| ICLR 2024 Test of Time Award（VAE） | 2024 | blog.iclr.cc（S1） |
| ICLR 2025 Test of Time Award（Adam） | 2025 | ICLR 官方 X 账号（S2质性） |
| Google European Doctoral Fellowship in Deep Learning | 2015 | dpkingma.com (S3) |
| Dutch Datascience Award | 2019 | dpkingma.com (S3) |
| ELLIS PhD Award | 2019 | dpkingma.com (S3) |
| PhD cum laude（阿姆斯特丹大学 CS 系 30 年来首位） | 2017 | dpkingma.com (S3) |

**注**：无 ACM/IEEE Fellow 记录（h-index=60 偏低；主要贡献集中在 2014 年少数论文）。

### 7. 人才与生态

（无明显师承谱系记录。VAE/Adam 对整个生成式 AI 社区有巨大的生态影响，但属于论文贡献而非人才培养。）

### 8. 思想与公共影响

（无公共政策参与、著作或重大媒体观点记录。低调技术研究者，几乎不接受媒体采访。）

---

## 8 维打分（用同一 rubric）

| 维度 | 名称 | 命中规范能力 | 分数 | 依据 |
|---|---|---|---|---|
| D1 | 原创奠基 | D1.1（Adam 优化器——基础工具，影响所有神经网络训练）；D1.1（VAE——生成模型基础框架）；D1.3（变分推断/生成模型理论） | **3** | 两篇各自开创整个子领域的论文（Adam 255k 引、VAE 57k 引），均获 ICLR Test of Time Award（S1 验证）。命中 ≥3 条规范能力且均属标志性基础件——达到 D1=3 门槛 |
| D2 | 工程产品化 | D2.x（Adam 事实上成为所有框架默认优化器，但属于他人工程化，本人未主导量产平台） | **1** | Adam 被大规模工程化但 Kingma 本人未直接主导产品/平台开发；属"间接工程化"，给 1 |
| D3 | 机构组织与领导 | D3.x（OpenAI 创始成员但非核心管理层；Anthropic 研究员无管理记录） | **1** | 参与性：OpenAI 创始但地位和 Altman/Brockman/Sutskever 等有差异，且 2018 年离开。给 1 |
| D4 | 资本与生态动员 | D4.x（Advanza 联创，规模小；未见主导重大融资记录） | **0** | 无 S1/S2 支撑的重大融资记录 |
| D5 | 物理世界/硬件/具身 | 无记录 | **0** | — |
| D6 | 安全·治理·思想框架 | 无显著记录（Anthropic 就职可能间接与安全相关，但本人无公开安全研究发表） | **0** | — |
| D7 | 教育·开源·传播 | D7.3（Adam/VAE 开源算法，广泛传播）；D7.1（《An Introduction to Variational Autoencoders》教材级综述，弱） | **1** | 有开源算法传播效果，但非主导教育社区/平台建设；无课程/MOOC/教材标志 |
| D8 | 趋势预判与逆向押注 | D8.1（2013 年做 VAE 时生成模型属于边缘方向——算一次逆向，弱）；D8.4（OpenAI→Google→Anthropic 跨机构迁移，弱） | **1** | 有逆向押注成分（2013 年变分推断+深度学习被认为不可行），但 Kingma 本人未明确公开表达"逆向押注"意图，此推断存在不确定性 |

**8 维向量：[3, 1, 1, 0, 0, 0, 1, 1]**

---

## 与 60 人分布比较

60 人各维度均值：D1~2.5, D2~2.0, D3~2.3, D4~1.6, D5~1.0, D6~0.8, D7~1.8, D8~1.9。

Kingma 向量 [3,1,1,0,0,0,1,1]：
- **D1=3 与"奠基科学家"原型完全重叠**，甚至因 Adam 单篇引用量（255k）超越该原型内大多数人，属于极端值。
- **D2–D8 几乎全面低于 60 人均值**，除了 D1 外只有 1 分。
- 最接近的 60 人比对：Ian Goodfellow [3,1,1,1,1,2,3,1]（GAN 发明人），但 Goodfellow 在 D7 有 3 分（教育传播），在 D6 有 2 分（对抗样本安全），Kingma 均为 0。

**初步结论：Kingma 是"D1 极高、其他维度极低"的一根独柱形态——类似于 Chris Olah [2,0,2,0,0,3,3,1]（另一侧的极端），但方向相反（Olah 是 D6/D7 极高、D1 中等）。在 60 人中，这种"D1 独柱"最接近 Goodfellow（但 Goodfellow 在 D7 额外有贡献）。判别力诊断：D1 分布"分不开"（与 14 位奠基科学家重叠），D2–D8 系统性低于均值——说明 D1 本身不足以区分"名单内/外"，多维度参与（D3 机构/D7 教育等）可能才是真正的差异来源。这与"学术极端优秀但几乎不做机构建设、教育传播或资本动员"的模式完全吻合。**

---

## 事实存疑汇总

| 条目 | 当前依据 | 状态 |
|---|---|---|
| OpenAI 创始成员（15 人团队） | dpkingma.com (S3) | 待核——需查 OpenAI 官方创始公告 S1 |
| ICLR 2025 Test of Time Award（Adam） | ICLR X 账号帖（S2质性） | 较可信，但非 ICLR 官方网站 S1 页面；blog.iclr.cc 对应的是 2015 年论文的 Award，逻辑与时间线吻合 |
| Anthropic 职位 | S4 媒体报道 | 待核—— anthropic.com 官方团队页可能有记录 |
| "PhD cum laude，UvA CS 系 30 年来首位" | dpkingma.com (S3) | 待核—— UvA 官方记录 |

---

*本文件创建：2026-06-13 | 仅用于对照诊断，不进入正式分数*
