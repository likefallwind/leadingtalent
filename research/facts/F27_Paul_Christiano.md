# F27 Paul Christiano
> 贡献清单（v1 2026-06-07）见 research/contributions/F27_Paul_Christiano.md
> Alignment Research Center 创始人 / NIST CAISI 技术顾问。活跃窗口 ~2015–至今。证据深度：RICH（早年资料少）

## FACTS
### 训练与社区
- F1 [A] 数学/理论计算机科学/机器学习训练；活跃于有效利他主义与 AI alignment 社区，撰写大量迭代放大/可扩展监督/对齐理论文章（童年/家庭资料少，不延伸）。
### RLHF
- F2 [A] 2017 在 OpenAI 发表 RLHF 论文（"Deep Reinforcement Learning from Human Preferences"，NeurIPS 2017，arXiv 1706.03741，5,324 引用 Semantic Scholar 2026-06；作者：Paul Christiano, Jan Leike, Tom B. Brown, Miljan Martic, Shane Legg, Dario Amodei），后领导 OpenAI 语言模型对齐团队；RLHF 成为 ChatGPT 等对话模型关键训练环节。— from F2
- F3 [A] RLHF 把"人类想要什么"部分转化为可收集/可训练/可优化的数据问题；今几乎所有主流大模型都用某种人类反馈/偏好优化。— from F2
### 可扩展监督
- F4 [A] 长期研究 scalable oversight：迭代放大、debate、recursive reward modeling，解决"任务超出人类直接评估时如何监督"。
### 机构
- F5 [A] 2021 创办 Alignment Research Center（ARC，www.alignment.org），做模型评测、危险能力识别（自主复制/网络攻击/欺骗/长期规划）、对齐理论——前沿模型部署前识别风险。
- F6 [A] 任 NIST 下属 Center for AI Standards and Innovation（CAISI）技术顾问（paulfchristiano.com 自述），把技术对齐与标准/评测/政府能力建设结合——少数同时被前沿实验室+独立组织+政府认可者。— from F5,F6
### 新增贡献
- F8 [A] 2016 年共同发表"Concrete Problems in AI Safety"（arXiv 1606.06565，ICML 2016；作者：Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, Dan Mané）；框架化 AI 安全5大实践研究方向（副作用/奖励劫持/可扩展监督/安全探索/分布偏移），高被引基础论文。— from F1,F4
- F9 [A] 2018 年发表"Supervising strong learners by amplifying weak experts"（Iterated Amplification，arXiv 1810.08575；作者：Paul Christiano, Buck Shlegeris, Dario Amodei）；提出 Iterated Amplification 方法，解决超人任务的可扩展监督问题。— from F4
- F10 [A] 2021–2022 年 ARC 发布 Eliciting Latent Knowledge（ELK）报告，定义"如何知道 AI 说的话是否反映其真实信念"的核心对齐问题；引发社区广泛讨论和后续研究方向。— from F5
- F11 [A] ARC Evals 部门（危险能力评测）于 2023 年分拆独立为 METR（Model Evaluation & Threat Research，metr.org）；METR 原型化 Responsible Scaling Policies（RSP）方法，已被 9 家头部 AI 开发商采用；与 OpenAI、Anthropic、NIST AI Safety Institute Consortium、欧盟 AI Office 合作。— from F5,F6
### 局限
- F7 [A] 务实技术化风格（追问用什么训练信号/评测/监督降低风险），但 RLHF 不保证深层对齐、可扩展监督未在超人任务证明——是提供路线而非已解决。

## CAPS
- C1 造出被全行业沿用的基础件（RLHF，5,324 引用）— from F2,F3
- C2 把抽象安全担忧转化为具体可研究的技术问题 — from F1,F4,F8
- C3 从零创办独立安全研究组织（ARC）— from F5
- C4 把研究/评测连接到政府标准与公共能力建设 — from F6,F11
- C5 按长期信念专注一个方向（对齐）跨实验室/独立/政府 — from F2,F5,F6
- C6 危险能力评测的范式开创（ARC Evals→METR，RSP方法） — from F5,F11
- C7 诚实面对方法局限（不宣称已解决对齐）— from F7
- C8 从可扩展监督到 ELK 的递进技术路线（Debate→Amplification→ELK）— from F4,F9,F10
