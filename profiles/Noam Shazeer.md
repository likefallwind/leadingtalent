# Noam Shazeer（诺姆·沙泽尔）

> F71 · 深度学习架构发明者 → AI 创业者 → 巨头技术领袖。
> 一句话：他既是 Transformer 八位"贡献均等"作者之一、又是稀疏 MoE 的第一作者，
> 还把这套信念做成了 Character.AI，最终被 Google 以 27 亿美元"反向收购"请回去共同领衔 Gemini。
> 入库定位：与 F30 Aidan Gomez 同篇 Transformer 作者，作为"相似性诱导对抗采样"检验"近克隆人是否同形"。

## 时间线与履历
- **1975/1976 生**。1994 年国际数学奥林匹克（IMO）**满分金牌**——早慧硬底子。
- **杜克大学数学与计算机科学学士（1994–1998）**；UC Berkeley 研究生项目入读但未完成，**无博士学位**。
- **2000 年加入 Google**，长期高级研究员/Distinguished Engineer。早期改进 Google 搜索的拼写纠错系统（服务十亿级用户）。
- 2010s 后期与 **Daniel de Freitas** 构建开放域对话模型 **Meena**（后演化为 LaMDA 路线）。
- **2021 年离开 Google**——因谷歌拒绝公开发布 Meena，他坚信对话 AI 的价值，遂与 de Freitas 共同创办 **Character.AI**，任 CEO。
- **2024-08**：Google 以 **$27 亿**非独占技术授权协议，把他与约 30 名核心成员"反向收购"式请回，他出任**工程副总裁**、与 **Jeff Dean（F04）、Oriol Vinyals 共同领衔 Gemini**。
- **2026 年当选美国国家工程院（NAE）院士**。

## 关键贡献
### 原创架构（标志级，D1）
- **Transformer**（《Attention Is All You Need》, 2017）：八位贡献均等的共同作者之一，自述贡献多头自注意力机制。该文约 **261,099 次引用**（Google Scholar, 2026-06），是 21 世纪被引最多的论文之一，几乎所有现代大模型（GPT/Claude/Gemini/DeepSeek/Kimi）的架构基础。**与 F30 Gomez 同列作者。**
- **稀疏门控 Mixture-of-Experts**（《Outrageously Large Neural Networks》, 2017，**第一作者**）：用可训练门控在上千个子网络里稀疏激活，>1000× 扩张模型容量而算力仅微增。多年后成为 GPT-4、Mixtral、DeepSeek-V3 等稀疏大模型的范式基石——这是他**早于主流的逆向押注**。

### 训练系统与优化（D2 的一半）
- **Mesh-TensorFlow**（2018）：面向超级计算机的大模型分布式/模型并行训练框架，被后续 GShard 等沿用。
- **AdaFactor**（2018，共同第一作者）：亚线性内存的自适应优化器，大模型训练常用以节省优化器状态显存。
- 共同作者 **T5**（约 32,926 引）与 **PaLM**（约 9,511 引）等里程碑大模型工作。
- 总计量：Google Scholar **总引 356,331、h-index 74、i10-index 135**（2026-06）。

### 产品与公司（D2 另一半 + D3/D4）
- **Character.AI**（2021–2024）：消费级角色扮演对话产品，上线首年即估值破 $10 亿（独角兽），以极高用户黏性著称，月活/访问量达数千万级（媒体口径）。本人持股 **30–40%**，2023 年 a16z 领投约 $1.5 亿 Series A。
- **$27 亿反向收购**（2024）：Google 非独占授权 Character.AI 技术并回聘其团队，本人个人套现估 **$7.5 亿–$10 亿**（媒体口径）。
- **Gemini 共同领衔**（2024–）：与 Jeff Dean、Oriol Vinyals 同领谷歌前沿大模型。

### 荣誉（D 声誉性背书）
- **美国国家工程院院士（2026）**、**TIME100 AI（2023）**、IMO 1994 满分金牌。

## 思想与逆向
他的"逆向"主要体现在两次行动而非檄文：一是 2017 年在稠密模型主导期押注稀疏 MoE 可把容量扩三个数量级；
二是 2021 年因谷歌不肯公开对话模型而离职、亲手把"消费级对话 AI"做出来。两者都被后来的浪潮证明方向正确，
但他没有 Sutton《Bitter Lesson》、Chollet ARC-AGI 那样的公开思想宣言——信念藏在代码与创业选择里。

## 边界与存疑
- 工业研究/创业路径：**无博导谱系**（影响经由论文与产品而非带学生）、无物理硬件、无安全治理工作。
- Character.AI 的月活/估值、$27 亿交易的个人套现均为**媒体估计（S4）**，非事务性披露。
- NAE 2026 待补官网一手来源（S1）。
- Transformer 是 **8 人贡献均等**之作，不可写成个人发明；Gemini 为"共同领衔"非独掌。

## 资料来源
- Google Scholar（user=wsGvgA8AAAAJ，总引/h-index，S2，2026-06）
- arXiv 原文：Transformer 1706.03762 / MoE 1701.06538 / Mesh-TF 1811.02084 / AdaFactor 1804.04235 / T5 1910.10683 / PaLM 2204.02311（S2）
- en.wikipedia.org/wiki/Noam_Shazeer（S4，生平/教育/IMO/NAE）
- CNBC 2024-08 / TechCrunch 2024-08 / WSJ 转述（S4，$2.7B 交易与 Gemini 任命）
- TIME100 AI 2023（S1）
