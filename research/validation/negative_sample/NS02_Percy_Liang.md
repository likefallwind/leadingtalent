# 负样本 NS02：Percy Liang

> **对照组用途**：测 8 维框架的判别力——此人**同时具备** D3（创建斯坦福 CRFM 中心）+ D4（Together AI 联创，$3.3B）+ 评测治理（HELM），即"初步诊断怀疑的真正筛子"两维他都有，却仍未进任何主要 AI 领军名单。
> 产物仅在 `research/validation/negative_sample/`，**绝不进入正式分数文件**。

---

## 候选确认

**姓名**：Percy Liang
**机构**：斯坦福大学计算机系副教授；基础模型研究中心（CRFM, Center for Research on Foundation Models）主任；Together AI 联合创始人兼首席科学家

**"够格当对照"的硬证据**：
- Semantic Scholar 报告 h-index ~100，总引用 ~74,671（来源：semanticscholar.org/author/Percy-Liang S2；研究.com 另报 D-index 99 / 引用 ~54,667，口径差异已并列）
- SQuAD（100,000+ Questions for Machine Comprehension of Text，2016）共同作者——机器阅读理解标准基准（来源：Wikipedia / Stanford S3）
- HELM（Holistic Evaluation of Language Models）主导者——首个把 30+ 主流大模型放在同一标准下横向对照的评测框架（来源：venturebeat / snorkel S3）
- 提出并推广 "foundation models" 术语（2021，CRFM 创立）（来源：S3/S4）
- Together AI 联合创始人（开放基础模型平台；2025-02 完成 $305M B 轮，估值 $3.3B，累计融资 $534M）（来源：together.ai / Sacra / Crunchbase S3）
- Semantic Machines 首席科学家（核心对话理解技术，2018 被微软收购，技术进入 Google Assistant）（来源：Microsoft 官方博客 / PRNewswire S2/S3）
- MIT 学士（2004）+ UC Berkeley 博士（2011）

**未入名单的依据**：TIME100 AI 2023/2024/2025 三届均未检索到其名字（S4：WebSearch 核验 2026-06）。Forbes AI 50 未单独核验（待查）。

**存疑与局限**：
- 引用/h-index 跨源口径差异大（Semantic Scholar h-100/74k vs research.com 99/54k），并列保守取用
- SQuAD 本人为资深/指导作者（Rajpurkar 为第一作者），贡献分量归属待细化
- Together AI 为 5 位联创之一（Chris Ré/Ce Zhang/Vipul Ved Prakash/Tri Dao/Percy Liang），CEO 为 Vipul，本人任首席科学家——资本动员中本人非主导

---

## 本轮已查来源

- semanticscholar.org/author/Percy-Liang/145419642（S2，引用/h-index）
- en.wikipedia.org/wiki/Percy_Liang（S4）
- engineering.stanford.edu/people/percy-liang（S3，斯坦福官方）
- together.ai/about-us（S3，Together AI 官方）
- sacra.com/c/together-ai/ + crunchbase（S3，融资/估值）
- blogs.microsoft.com 2018-05-20 收购 Semantic Machines（S2，微软官方）
- venturebeat.com / snorkel.ai（S3，HELM）
- TIME100 AI 2023/2024/2025 榜单页（S2，核"未入名单"）

---

## 八类维度普查

### 1. 学术

| 贡献 | 年份 | 来源/S级 | 影响/规模 | 本人角色 |
|---|---|---|---|---|
| SQuAD 阅读理解基准 | 2016 | Stanford (S3) | 机器阅读理解事实标准基准，催生大量 QA 研究 | 共同/资深作者 |
| HELM 整体评测框架 | 2022 | venturebeat (S3) | 首个 30+ 大模型同标准横评，成大模型评测范式 | 主导 |
| 语义解析（semantic parsing）系列 | 2011+ | Scholar (S2) | NLP 语义解析长期奠基贡献 | 第一/通讯作者 |
| "Foundation Models" 术语与 CRFM 报告 | 2021 | S3/S4 | 重新定义大模型话语框架，被广泛采用 | 主导（CRFM 创立） |

**注**：h-index ~100、引用 ~74k（S2），属名单内 3 档学者量级。

### 2. 系统与框架

| 贡献 | 年份 | 来源/S级 | 影响/规模 | 本人角色 |
|---|---|---|---|---|
| HELM 开源评测框架 | 2022+ | venturebeat (S3) | 大模型评测基础设施，多机构采用 | 主导 |
| Semantic Machines 对话理解技术 | –2018 | Microsoft blog (S2) | 技术进入 Google Assistant；微软收购 | 首席科学家 |

### 3. 产品与工程

| 贡献 | 年份 | 来源/S级 | 影响/规模 | 本人角色 |
|---|---|---|---|---|
| Together AI 开放模型推理/训练平台 | 2022–至今 | together.ai (S3) | 年化营收近 $1B（传闻 S4）；开放模型云平台 | 联创+首席科学家（**非产品/CEO 主导**） |
| Semantic Machines → Google Assistant 核心技术 | –2018 | Microsoft (S2) | 进入消费级语音助手 | 首席科学家 |

### 4. 公司与组织

| 贡献 | 年份 | 来源/S级 | 影响/规模 | 本人角色 |
|---|---|---|---|---|
| **CRFM（斯坦福基础模型研究中心）主任** | 2021–至今 | Stanford (S3) | 创建并领导定义"foundation models"领域的研究中心 | 创始主任 |
| **Together AI 联合创始人** | 2022 | together.ai/Sacra (S3) | $305M B 轮 / 估值 $3.3B / 累计 $534M | 5 位联创之一，首席科学家 |
| Semantic Machines 联合领导/首席科学家 | –2018 | Microsoft (S2) | 被微软收购 | 首席科学家 |

### 5. 标准与基础设施

| 贡献 | 年份 | 来源/S级 |
|---|---|---|
| HELM 成为大模型评测事实标准 | 2022+ | venturebeat (S3) |
| CRFM 基础模型透明度指数（Foundation Model Transparency Index） | 2023+ | S3/S4 |

（无芯片/物理硬件标准记录。）

### 6. 学术服务与荣誉

| 贡献 | 年份 | 来源/S级 |
|---|---|---|
| Schmidt Sciences AI2050 Fellow | — | ai2050.schmidtsciences.org (S3) |
| 大模型透明度/开放性政策倡导（评测即治理） | 2022+ | S3/S4 |
| 斯坦福 CS 副教授，多届顶会 PC/领域主席 | 持续 | Stanford (S3) |

### 7. 人才与生态

| 贡献 | 年份 | 来源/S级 |
|---|---|---|
| HELM/CRFM 开源释放，推动开放基础模型生态 | 2022+ | venturebeat (S3) |
| 斯坦福 CS224 等课程教学，培养 NLP 博士群 | 持续 | Stanford (S3) |
| 公开使命"通过开源让基础模型更可及" | 持续 | Stanford (S3) |

### 8. 思想与公共影响

| 贡献 | 年份 | 来源/S级 |
|---|---|---|
| "Foundation Models" 术语奠定行业话语 | 2021 | S3/S4 |
| HELM 把"评测/透明度"提为治理议题 | 2022+ | venturebeat (S3) |
| TEDAI 等公开演讲 | 持续 | S4 |

---

## 8 维打分（用同一 rubric）

| 维度 | 名称 | 命中规范能力 | 分数 | 依据 |
|---|---|---|---|---|
| D1 | 原创奠基 | D1.1（SQuAD 标准基准）；D1.1（HELM 评测范式）；D1.1（语义解析长期奠基）；D1.x（foundation models 话语） | **3** | h-100/74k 引用，SQuAD+HELM+语义解析多件被广泛使用的奠基/标准——清晰标志性原创（SQuAD 本人非第一作者，故标注归属待细化，但综合达 3 档） |
| D2 | 工程产品化 | D2.x（Together AI 平台，联创但非产品主导）；D2.x（Semantic Machines→Assistant） | **1** | 有产品落地路径，但本人是研究/科学侧而非产品化主导，且 Together 营收规模为传闻 S4——存在但次要 |
| D3 | 机构组织与领导 | D3.1（CRFM 创始主任，创建并定义领域的研究中心）；D3.3（斯坦福教席） | **2** | 创建并领导 CRFM（清晰强项）；但 CRFM 是研究中心非大型组织/公司，未达 DeepMind/OpenAI 量级的 D3=3 |
| D4 | 资本与生态动员 | D4.1（Together AI 联创，$3.3B/$534M）；D4.x（Semantic Machines 被微软收购） | **2** | 真实资本动员（Together $3.3B），清晰强项；但本人是 5 联创之一、任首席科学家而非 CEO——给 2 不给 3 |
| D5 | 物理世界/硬件/具身 | 无 | **0** | — |
| D6 | 安全·治理·思想框架 | D6.x（HELM/透明度指数把评测提为治理议题）；D6.x（开放性政策倡导） | **1** | 评测/透明度是治理相邻贡献（清晰但非顶格），非 alignment/安全框架级别（对照 Bostrom=3/Olah=3）——给 1 |
| D7 | 教育·开源·传播 | D7.1（HELM/CRFM 开源生态）；D7.4（斯坦福课程+博士培养）；D7.x（开放模型倡导） | **2** | 两条路径（开源基础设施+教育），达清晰强项；但无单一标志性 MOOC/教材 |
| D8 | 趋势预判与逆向押注 | D8.3（2021 早押"foundation models"框架与系统评测，先于主流）；D8.x（押注开放模型路线） | **2** | 早于行业把"基础模型+整体评测+开放"作为方向押注，达清晰强项 |

**8 维向量：[3, 1, 2, 2, 0, 1, 2, 2]**

---

## 与 60 人分布比较

60 人各维度均值：D1~2.5, D2~2.0, D3~2.3, D4~1.6, D5~1.0, D6~0.8, D7~1.8, D8~1.9。

Liang 向量 [3,1,2,2,0,1,2,2]：
- **几乎逐维持平或高于均值**：D1=3>均值、D3=2≈均值、D4=2>均值、D6=1>均值、D7=2>均值、D8=2>均值。只有 D2=1 与 D5=0 偏低。
- 与名单内"科学家-创业/治理"原型（如 Fei-Fei Li、Andrew Ng 一类学术+机构+创业复合体）**高度重叠**，且在 D4（资本动员）上他**并不弱**——这恰恰击中了 NS README 的初步猜想"D3/D4 才是真正筛子"。

**初步结论（对原猜想的反证）：Percy Liang 同时具备 D3（创建 CRFM）、D4（Together AI 联创 $3.3B）、D6（评测治理）——即"初步诊断怀疑的真正筛子"几维他都有，却仍未进任何主要名单。这说明 D3/D4 也不能干净地把名单内/外分开。结合 NS05 Vinyals（D1/D2/D3 达标、仅缺 D4 而落选）两个相反方向的反例，更可信的解读是：8 维中没有任何单一维度（含 D3/D4）构成纳入的充分判别，真正起作用的是维度之外的"公众可见度 / 单一标志性叙事 / 提名显著性"——即名单循环性本身。这与 `METHOD_IMPROVEMENTS.md` 共识 1 一致，且把"门槛特异度低"的结论从 D1 推进到了 D3/D4。**

---

## 事实存疑汇总

| 条目 | 当前依据 | 状态 |
|---|---|---|
| h-index / 引用（100/74k vs 99/54k） | Semantic Scholar S2 / research.com S4 | 跨源口径差异，并列保守取用 |
| SQuAD 贡献分量（非第一作者） | Stanford S3 | 归属分量待细化 |
| Together AI 年化营收近 $1B | 传闻 S4 | 待 S1/S2 核验 |
| Forbes AI 50 是否收录 | 未核 | 待查 |

---

*本文件创建：2026-06-13 | 仅用于对照诊断，不进入正式分数*
