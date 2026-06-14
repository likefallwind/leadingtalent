# F71 Noam Shazeer（诺姆·沙泽尔）
> 深度学习架构发明者（Transformer 八作者之一、稀疏 MoE 第一作者）+ 系统工程师（Mesh-TensorFlow/AdaFactor）+ AI 创业者（Character.AI 创始 CEO）→ 巨头技术领袖（Google Gemini 共同领衔）。活跃窗口 2000–至今。证据深度：RICH（新人入库 v1）。
> 相似性诱导对抗采样：与 F30 Aidan Gomez 同为《Attention Is All You Need》共同作者，测"近克隆人是否坍缩同形"。
> 贡献清单（v1 2026-06-14）见 research/contributions/F71_Noam_Shazeer.md

## FACTS
### 出身与早慧
- F1 [A] 杜克大学数学与 CS 学士（1994–1998）；UC Berkeley 研究生入读未完成，**无博士学位**；**1994 年 IMO 满分金牌**。（S4 维基；早慧硬底子）
- F2 [A] 2000 年加入 Google，长期任高级研究员/Distinguished Engineer；早期改进 Google 搜索拼写纠错（十亿级用户产品）。（S4 维基）
### 学术与原创（标志）
- F3 [A] 《Attention Is All You Need》(2017) **八位"贡献均等"共同作者之一**，多头自注意力贡献者；该文约 **261,099 引**（Google Scholar，as-of 2026-06），现代大模型架构基石。（S2 arXiv 1706.03762 + S2 Scholar）（**与 F30 Gomez 同篇**）
- F4 [A] **稀疏门控 Mixture-of-Experts** 第一作者（《Outrageously Large Neural Networks》2017），>1000× 模型容量提升而算力微增；今为 GPT-4/Mixtral/DeepSeek-V3 等稀疏大模型基石。（S2 arXiv 1701.06538）
- F5 [A] 共同作者 T5（约 32,926 引）与 PaLM（约 9,511 引）；主导 **Mesh-TensorFlow**（超算分布式训练框架，2018）与 **AdaFactor**（亚线性内存优化器，2018）。（S2 arXiv 各篇）
- F6 [A] Google Scholar **总引 356,331、h-index 74、i10-index 135**（as-of 2026-06）；research.com 计 h=41 系子集低估，不采用。（S2 Scholar user=wsGvgA8AAAAJ）
### 产品与公司
- F7 [A] 与 Daniel de Freitas 共同创办 **Character.AI**（2021）任 CEO；上线首年估值破 $10 亿，本人持股 30–40%；2023 a16z 领投约 $1.5 亿/$10 亿估值。（S4 维基/TechCrunch）
- F8 [A] **2024-08 经 $27 亿非独占技术授权"反向收购"协议重返 Google**，回聘其与约 30 名核心成员；个人套现估 $7.5 亿–$10 亿（媒体口径）。（S4 CNBC/WSJ 转述）
- F9 [A] 现任 Google 工程副总裁，与 Jeff Dean(F04)、Oriol Vinyals **共同领衔 Gemini** 旗舰大模型。（S4 CNBC/TechCrunch）（**与 F04 交叉**）
### 荣誉
- F10 [A] 美国**国家工程院（NAE）院士（2026）**；**TIME100 AI（2023）**。（S4 维基/S1 TIME；NAE 待补官网 S1）
### 思想/逆向
- F11 [A] 早于主流押注稀疏超大模型（MoE，2017）；因谷歌拒绝公开对话模型 Meena 而离职创业，以行动押注"消费级对话 AI"——信念逆向，但无公开宣言式檄文。（S2 arXiv + S4 维基）
### 边界
- F12 [B] 工业研究/创业路径：无博导谱系(D7 偏弱)、无物理硬件(D5=0)、无安全治理工作(D6=0)。标志在 D1 原创(Transformer+MoE)与 D2 工程(Mesh-TF+Character.AI+Gemini)。与 F30 Gomez 的差异：Shazeer 多 Mesh-TF 系统级基础设施 + Gemini 领衔 + 抢在 ChatGPT 前做消费对话。（分析性，标 [B]）

## CAPS
- C1 极早慧（IMO 满分金牌）+ 无 PhD 仍达架构奠基级 — from F1
- C2 共同发明 Transformer（261k 引，全行业架构基础）— from F3
- C3 独立开创稀疏 MoE 范式（大模型稀疏化基石）— from F4
- C4 多项大模型训练系统/优化器（Mesh-TF/AdaFactor/T5/PaLM）— from F5
- C5 从奠基研究直接创办消费 AI 公司并任 CEO（Character.AI 独角兽）— from F7
- C6 $27 亿反向收购式回归 + 巨头前沿模型共同领衔（Gemini）— from F8,F9
- C7 NAE 院士 + TIME100 AI（声誉性硬背书）— from F10
- C8 早期逆向押注稀疏超大模型 + 为信念离职创业 — from F11

## 打分准备（建议向量，仅供下一个重评批次 v5 参考，未写入 scores.md）
> 按 9 维 rubric（v3）：
> **建议 [D1=3, D2=3, D3=2, D4=2, D5=0, D6=0, D7=2, D8=2, D9=1]，原型迁移=✓（奠基科学家→创业 CEO→巨头统帅）**
> - D1=3：Transformer 共同作者 + MoE 第一作者（双标志级原创，h74/356k 引 S2 极硬）。
> - D2=3：Mesh-TensorFlow 训练基础设施 + AdaFactor + Character.AI 消费产品 + Gemini 工程联席领衔——系统+产品双线，比 Gomez(D2=2) 多基础设施与前沿模型领衔。
> - D3=2：Character.AI 创始 CEO（独角兽）+ Google 工程 VP/Gemini co-lead；机构领导显著但非自建大型新机构，与 Gomez 同档。
> - D4=2：Character.AI a16z 领投 + $27 亿交易；规模可观但低于 Cohere 累计 $1.6B 的持续融资强度，与 Gomez 同档。
> - D5=0 / D6=0：无硬件、无安全治理工作。
> - D7=2：Transformer/MoE/T5/Mesh-TF 公开论文+多数开源代码、被全行业沿用（研究开放性强）；但无博导谱系/框架托管/教育者角色，故非 3，与 Gomez 同档。
> - D8=2：早期逆向押注稀疏 MoE + 为信念离职创业；无公开宣言式檄文，故 2 非 3。
> - D9=1：抢在 ChatGPT 前(2021)做消费对话、年内独角兽，有拐点嗅觉；但 Character.AI 商业化吃力、最终以人才交易退出，故 1 非 2（Gomez D9=0）。
> - 迁移=✓：奠基研究者→创业 CEO→巨头前沿模型统帅，一生多次原型迁移。
> - 主原型：奠基科学家 × 科学家–创业者。
> **与 F30 Gomez [3,2,2,2,0,0,2,2,0] 对照（相似性诱导采样的核心结果）**：
> 共享 **D1=3/D3=2/D4=2/D5=0/D6=0/D7=2/D8=2** 七维骨架，仅在 **D2(3 vs 2)、D9(1 vs 0)** 分叉，**曼哈顿距离=2**。
> 两位 Transformer 共同作者**未坍缩同形，但距离远小于全样本中位数 9**，且差异落在 ±1 打分误差量级——
> 这是对"零重合"最诚实的一击：相似性采样下点云被局部压紧，"无两人相同"虽未被推翻却显脆弱。
> 建议硬度：D1/D2 的 3 有 S2(Scholar 356k/h74、arXiv 原文)支撑，极稳；D9 的 1 仅 S4 媒体口径，偏软。
