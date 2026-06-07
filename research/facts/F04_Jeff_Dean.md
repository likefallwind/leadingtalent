# F04 Jeff Dean
> Google Chief Scientist；大规模系统/AI 基础设施奠基者。活跃窗口 1996–至今。证据深度：RICH

## FACTS
### 出身与早年
- F1 [A] 1968 生于夏威夷。父亲做热带疾病研究、母亲是医学人类学者（通多语）；童年随父母多次搬家，早接触跨国/现实问题。
- F2 [A] 少年与父亲焊接组装 IMSAI 8080 套件，形成对硬件/性能/并发/故障的强直觉；13 岁曾跳课去索马里难民营帮父母。
- F3 [A] 高中编写流行病学数据软件 Epi Info，后成为公共卫生现场标准工具，广泛分发。
- F4 [A] 1990 明尼苏达大学计算机+经济学（summa cum laude）；1990–91 为 WHO 全球艾滋病规划开发 HIV 流行病建模软件。
- F5 [A] 1996 华盛顿大学计算机博士，研究编译器与面向对象语言全程序优化；后在 DEC Western Research Lab 做系统研究，结识 Sanjay Ghemawat。
### 关键贡献
- F6 [A] 1999 中加入 Google；2000s 与 Ghemawat 主导 MapReduce（OSDI 2004，被引 30,000+）、Bigtable（OSDI 2006，被引 10,000+）；2012 年与 Corbett 等共同发表 Spanner（OSDI 2012，全球分布式数据库，被引 9,000+）——把数万台机器变成可编程容错平台，重塑互联网规模计算。（来源：OSDI 论文页）
- F7 [A] 与 Ghemawat 长期结对编程的互补型合作（Dean 把握整体方向、Ghemawat 重结构可靠性），罕见的长期高产组合。
- F8 [A] 2011 共同创建 Google Brain，把神经网络扩到 Google 数据/算力规模，落地语音/图像/翻译/排序。
- F9 [A] 主导/参与的关键技术贡献：DistBelief（NeurIPS 2012，首批分布式深度网络系统，被引 5,000+）；TensorFlow（OSDI 2016，被引 50,000+，GitHub 180k+ Stars，最广泛使用的 ML 框架之一）；word2vec（与 Mikolov、Chen、Corrado 共同发表，arXiv 1301.3781，被引 40,000+，NLP 词嵌入事实标准）；BERT（Google Brain 机构主导，NeurIPS/NAACL 2019，Devlin et al.，被引 100,000+，预训练 LM 行业标准）；JAX（Google Brain 开源数值计算框架，研究社区高采用率）；Pathways（MLSys 2022，新一代异步分布式 ML 数据流平台）；PaLM、Gemini（多模态大模型，Gemini 联合负责人）；ML for chip design/洪水预测/医疗诊断等科学应用。（来源：arXiv 1301.3781；OSDI 2016 TensorFlow；research.google）
- F10 [A] 2023 Google Brain 与 DeepMind 合并后任 Google Chief Scientist，与 Hassabis 共定 AI 研究方向与多模态模型战略。
### 荣誉
- F11 [A] Google Senior Fellow（公司最高工程技术级别）；ACM Fellow；美国国家工程院院士；2012 与 Ghemawat 共获 ACM Prize in Computing（互联网规模分布式系统）；2021 IEEE John von Neumann Medal（"大规模分布式计算机系统和 AI 系统的科学与工程贡献"，IEEE 最高荣誉之一）；TIME 100 Most Influential People in AI 2025；总被引 376,000–416,000+。（来源：IEEE 官方；TIME 2025；research.google）

## CAPS
- C1 识别关键抽象、把复杂分布式难题封装成普通工程师可用的平台（MapReduce/Bigtable）— from F6
- C2 把机器学习与超大规模基础设施连接、推动深度学习工业化 — from F8,F9
- C3 造出被全行业沿用的基础件（MapReduce/Bigtable/TensorFlow/TPU）— from F6,F9
- C4 极宽的技术跨度：从底层系统到基础模型到科学应用 — from F9
- C5 罕见的长期互补型合作关系驱动工程突破，非孤胆英雄 — from F7
- C6 从顶级工程师成长为整个 Google AI 路线的科学领导者 — from F10
- C7 把硬件/性能/故障的底层直觉贯穿到大系统设计 — from F2,F5,F6
- C8 长期把计算用于大规模现实问题（公共卫生→搜索→医疗/气候）— from F1,F3,F4,F9
- C9 编译器/系统训练转化为大规模 AI 效率优势 — from F5,F6
- C10 连续 20 年在同一组织内不断升级贡献层级：系统→ML 基础件→大模型→Chief Scientist — from F6,F8,F9,F10
