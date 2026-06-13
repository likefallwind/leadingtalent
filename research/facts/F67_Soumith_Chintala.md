# F67 Soumith Chintala（苏米特·钦塔拉）
> PyTorch 共同创建者与长期负责人；前 Meta/FAIR AI 基础设施副总裁（约 11 年）；2025 起 Thinking Machines Lab CTO；DCGAN/WGAN 共同作者。活跃窗口 2014–至今。证据深度：RICH（新人入库 v1）
> 贡献清单（v1 2026-06-14）见 research/contributions/F67_Soumith_Chintala.md

## FACTS
### 系统与框架（核心标志）
- F1 [A] 2016 年与 Adam Paszke、Sam Gross 等共同创建 PyTorch 并长期担任负责人/社区公开代表（github.com/pytorch/pytorch 约 101k stars，as-of 2026-06）。（S2 GitHub + S4 维基）
- F2 [A] PyTorch 成为研究界事实标准：到 2023 年 NeurIPS 等顶会论文 >80% 使用、被估计 >90% AI 从业者/企业采用。（S4 维基/媒体）
- F3 [A] 2022 年 PyTorch 移交 Linux Foundation 成立 PyTorch Foundation，确立开放中立治理。（S4 InfoQ/维基）
- F4 [A] 著《How to Train a GAN?》(ganhacks，约 11.6k stars)、convnet-benchmarks（约 2.7k stars）等开源资料。（S2 GitHub）
### 学术与原创
- F5 [A] 共同作者 DCGAN《Unsupervised Representation Learning with Deep Convolutional GANs》(2015，与 Alec Radford/Luke Metz)——GAN+CNN 奠基架构，约 14,776 引（Semantic Scholar，as-of 2026-06）。（S2）
- F6 [A] 共同作者 Wasserstein GAN（2017，与 Martin Arjovsky/Léon Bottou），两版本合计 >1.3 万引——改善 GAN 训练稳定性的里程碑。（S2 arXiv/Semantic Scholar）
- F7 [A] PyTorch 论文（NeurIPS 2019，21 位作者，资深作者）极高被引；scispace 计个人总引 22,681、h-index 29（保守口径，Google Scholar 含 PyTorch 论文后更高，待核）。（S1 NeurIPS + S2 scispace）
### 公司与组织
- F8 [A] Facebook AI Research（FAIR/Meta AI）2014–2025 约 11 年，历任至 AI 基础设施副总裁（VP of AI Infrastructure）；早期构建首个 FAIR 计算集群等。（S4 媒体 + S3 个人页）
- F9 [A] 2025-11 加入 Thinking Machines Lab（前 OpenAI CTO Mira Murati 创办），2026 起任首席技术官（CTO），负责技术战略/研究方向/基础设施。（S4 StartupTalky/AmericanBazaar）
### 人才与生态
- F10 [A] PyTorch 全球最大深度学习开源社区之一的长期领袖；以"让 AI 研究愉悦、工具优雅"的设计哲学降低研究门槛，影响一代研究者工具习惯。（S2 GitHub + S4 访谈）
- F11 [A] 师承：VIT 学士（2005–2009）、NYU 硕士（AI/机器人/CV，在 Yann LeCun 实验室环境内，与本名单 F02 交叉）。（S3 个人页 + S4 维基）
### 边界
- F12 [B] 工业工程路径，无院士/ACM·IEEE Fellow 等头衔；其"领军"由 PyTorch 采用率/star 等行为性指标确立——D4 资本（无自办融资）、D5 硬件、D6 安全、D8 信念逆向、D9 拐点偏低。（分析性，标 [B]）

## CAPS
- C1 共同创建并长期主导 PyTorch（研究界事实标准框架，101k stars/>80% 顶会采用）— from F1,F2
- C2 推动 PyTorch 开放中立治理（PyTorch Foundation）— from F3
- C3 GAN 早期两块奠基石（DCGAN/WGAN，合计近 3 万引）— from F5,F6
- C4 大厂 AI 基础设施技术领袖（Meta VP）→ 明星创业公司技术一把手（Thinking Machines CTO）— from F8,F9
- C5 全球最大深度学习开源社区之一的领袖 + "优雅工具/愉悦研究"开发者文化 — from F10
- C6 高被引研究者（PyTorch 论文/GAN 系列）— from F7

## 打分准备（建议向量，仅供下一个重评批次 v4 参考，未写入 scores.md）
> 按 9 维 rubric（v3）：
> **建议 [D1=2, D2=3, D3=2, D4=0, D5=0, D6=0, D7=3, D8=1, D9=1]，原型迁移=–**
> - D1=2：DCGAN+WGAN 两块 GAN 奠基石（共同作者，近 3 万引），强但非范式独创级（S2 支撑）。
> - D2=3：PyTorch 事实标准框架，标志级工程产品化（S2+S4 硬支撑）。
> - D3=2：Meta AI 基础设施副总裁 → Thinking Machines CTO，机构技术领导（非创始/院长）。
> - D4=0：无亲自主导的创办/融资/资本动员（PyTorch 是公司内部项目；TMLab 非其创办）。
> - D5=0 / D6=0：无物理硬件、无安全治理框架。
> - D7=3：全球最大深度学习开源社区之一的长期领袖 + 开发者文化影响，标志级开源（S2 硬支撑）。
> - D8=1：有"开放/优雅工具"价值观，但非逆共识范式级信念逆向。
> - D9=1：PyTorch 早期押注动态图踩中研究界需求拐点，但属团队产品判断，非个人市场嗅觉标志。
> - 迁移=–：始终在"深度学习系统/框架"主线内（GAN 研究→框架→AI 基础设施→创业 CTO 是同一工程领袖路径深化）。
> - 主原型：工具·框架·平台型（D2+D7 双标志）——与 F66 陈天奇同型但 D3 更高、D1 略低、D4 同低，**形状不重合**。
> 建议硬度：D2/D7 的 ≥2 有 S2(GitHub)+S4(采用率) 支撑稳；D1 的 2 有 S2(被引) 支撑；D3 的 2 仅 S4(媒体)，但属可核实任职，保留。
