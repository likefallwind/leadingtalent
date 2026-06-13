# 全员覆盖缺口审计（Coverage Gap Audit）

> 目的：防止 `profiles/` 与 `facts/` 漏掉关键硬成果，导致后续规范能力编码和 8 维评分在错误事实集上显得“客观”。
> 这是进入 `research/evidence/` 前的基础步骤。

> ✅ **统一重评已执行（v2，2026-06-10）**：60 人全部达 `audited-v1`/`updated` 后，按"满 60 人单次重评"规则
> 完成一轮统一重评——29 人 39 处分数上调（全部为补全证据后的上调，无下调），明细见 `research/scores.md` 末
> 的 v2 变更记录，每处依据在 `research/capability_matrix.md` 以 `▲v2` 标注。下游 `capability_pool.md` 频率、
> `profile/portrait.md` 分布、`FINDINGS.md`、`report.html` 已同步重算。核心结论（多峰、60 种形状、无单一模板）不变。
> 各行"对分数潜在影响：…待 60 人齐后统一重评"的提示至此已兑现，留作历史记录。

## 审计原则

1. 每个人都必须先过“覆盖缺口审计”，再进入规范能力证据账本。
2. 审计对象不是 D1-D8 分数，而是候选硬成果：论文/架构/系统/开源框架/产品/公司/标准/奖项/机构角色/公共报告。
3. 候选硬成果必须有外部权威来源支撑，优先级为：本人/机构官方页面、项目仓库、论文/报告、奖项官方页、大学/公司页面、权威媒体。
4. 未在当前 facts 中出现的候选成果，不得直接写成能力分；先进入本表，再决定是否补入 `profiles/`、`facts/`、`evidence/`、`capability_matrix.md`。
5. `queued` 不等于无遗漏；只有状态为 `audited-v1` 或 `updated` 的人，才表示完成了一轮外部来源对照。

## 状态说明

| 状态 | 含义 |
|---|---|
| `queued` | 已列入全员审计队列，尚未完成外部来源对照 |
| `audited-v1` | 完成一轮外部来源对照，未发现必须立即回填的硬缺口 |
| `updated` | 审计发现硬缺口，且已回填到相关文件 |
| `needs-source` | 发现候选缺口，但来源强度不足，不能直接回填 |
| `needs-followup` | 已发现可能影响评分的缺口，需要继续深挖或批量更新下游文件 |

## 已处理的硬缺口

| 人物 | 缺口 | 处理 |
|---|---|---|
| F31 刘铁岩 | LightGBM 未进入 profile/facts/evidence，导致 `D1.1`、`D2.2` 被低估 | 已补入 `profiles/刘铁岩.md`、`research/facts/F31_刘铁岩.md`、`research/evidence/F31_刘铁岩.md`、`research/capability_matrix.md` |

## 全员审计台账

| # | 人物 | 状态 | 本轮权威来源对照 | 候选缺口 / 处理提示 |
|---|---|---|---|---|
| F01 | Geoffrey Hinton | updated | U of T个人页/前博士生名单、NobelPrize.org、ACM Turing页、vectorinstitute.ai/Newswire 2017、CIFAR官方2024、JMLR(Dropout/t-SNE)、arXiv 2212.13345(Forward-Forward)、research.com/citationmap(Scholar) | 贡献清单v1已穷举八类；新增F14-F20：Dropout/t-SNE/知识蒸馏/胶囊网络/Forward-Forward/Gatsby Unit/MoE；更正F10（联合创始人）；扩写F11（38博士生谱系）；扩充F12（QE Prize/Order of Canada）；总被引103万+/h190补入。清单见contributions/F01_Geoffrey_Hinton.md。对分数潜在影响：D1.1(更强confirmed)、D7.3(confirmed)、D6.2(confirmed)，待60人齐后统一重评。 |
| F02 | Yann LeCun | updated | 个人官方页/publications列表、ACM Turing页、Meta AI官方博客、Semantic Scholar(LeNet 1998)、TechCrunch/SiliconANGLE(AMI Labs 2026)、research.com/citationmap(Scholar)、Wikipedia、OpenReview(JEPA 2022) | 贡献清单v1已穷举八类；新增F14-F17：SVM奠基(1992)、DjVu压缩格式、MNIST数据集、I/V-JEPA具体模型、LLaMA开源系列；补充AMI Labs融资$1.03B；更正F7(补JEPA论文名年份)、F9(明确PyTorch/LLaMA)、F12(补融资数字)、F13(补QE Prize)；扩写F17(Kavukcuoglu博士生谱系)；h-index171/总引47万补入。清单见contributions/F02_Yann_LeCun.md。对分数潜在影响：D2.2(PyTorch/LLaMA→更强)、D7.3(Kavukcuoglu→confirmed)，待60人齐后统一重评。 |
| F03 | Yoshua Bengio | updated | 个人官方页/yoshuabengio.org、ACM Turing页、Mila官方、Wikipedia(Element AI)、internationalaisafetyreport.org、UdeM nouvelles 2025-10(总被引突破)、research.com/citationmap、deeplearningbook.org、arXiv 1409.0473+1406.1078(attention/seq2seq) | 贡献清单v1已穷举八类；新增F14-F18：梯度消失研究(1994)/Curriculum Learning/Greedy Layer-Wise/Deep Learning教材/Theano框架/Element AI($$102M→$230M)；补充论文名+被引量(神经LM/attention/seq2seq/GAN)；更新F13(Order of Canada/Légion d'Honneur/总被引109万/h254)；扩写F10(Courville/Larochelle/Cho学生谱系)；C11-C13新增。清单见contributions/F03_Yoshua_Bengio.md。对分数潜在影响：D2.2(Theano)、D4.1(Element AI)、D7.3/D7.5(学生谱系)，待60人齐后统一重评。 |
| F04 | Jeff Dean | updated | research.google个人页、Wikipedia、OSDI论文(MapReduce/Bigtable/Spanner/TensorFlow)、arXiv 1301.3781(word2vec)、MLSys 2022(Pathways)、IEEE官方(von Neumann Medal)、TIME 100 AI 2025、research.google/ResearchGate(总引) | 贡献清单v1已穷举八类；丰富F6被引量(MapReduce 3万/Bigtable 1万)、补Spanner(OSDI 2012)；丰富F9(DistBelief/TF被引5万/word2vec具体论文名+4万引/BERT10万引/JAX)；更新F11(IEEE John von Neumann Medal 2021/TIME 100/总引376-416k/Google Senior Fellow)；新增C10。清单见contributions/F04_Jeff_Dean.md。对分数潜在影响：D2.2/D5(TF/TPU规模强化)，待60人齐后统一重评。 |
| F05 | Ilya Sutskever | updated | Wikipedia、research.com/scispace(总引/h-index)、arXiv 1409.3215(seq2seq)、openai.com(GPT-1/2/CLIP/InstructGPT)、TechCrunch 2025-04(SSI $32B)、NeurIPS官方(Test of Time)、NAS官方(2026奖) | 贡献清单v1已穷举八类；丰富F5(seq2seq论文名/2万被引)；大幅扩写F6(GPT-1/GPT-2/CLIP 3万被引/DALL-E/Scaling Laws/InstructGPT 1万被引)；补F9 SSI融资数字(2024$5B估值→2025$32B)；新增F10-F12(Test of Time 3届/NAS奖2026/总引81万)；C8-C9扩写。清单见contributions/F05_Ilya_Sutskever.md。对分数潜在影响：D1.1(CLIP/InstructGPT强化)，待60人齐后统一重评。 |
| F06 | Demis Hassabis | updated | NobelPrize.org(2024 Chemistry)、deepmind.google/blog、Wikipedia(AlphaFold/AlphaGo/DQN)、alphafold.ebi.ac.uk(数据库规模)、Semantic Scholar(DQN 3万/AlphaGo 1.8万被引)、Nature 2021 AlphaFold2(4.3万被引)、英国政府官方(CBE/Knight Bachelor) | 贡献清单v1已穷举八类；丰富F6(DQN论文名Nature 2015/3万被引)；丰富F7(AlphaGo论文名Nature 2016/1.8万被引；AlphaGo Zero论文名/1万被引)；大幅扩写F8(AlphaFold2论文名/4.3万被引；数据库500M+结构/2M+用户/190国；AlphaFold3 Nature 2024)；补F9(Isomorphic Labs合作Eli Lilly/Novartis)；补F10(CBE先于爵士)；新增F11(Gemini联合负责人)、F12(WaveNet 2016)；新增C10-C12。清单见contributions/F06_Demis_Hassabis.md。对分数潜在影响：D1.1/D2.2(DQN/AlphaGo/AlphaFold引用量强化)、D6.2(数据库规模confirmed)，待60人齐后统一重评。 |
| F07 | Sam Altman | updated | Britannica Money、openai.com(官方公告)、Fortune 2024-10($157B融资)、CNBC 2025-03($300B/$40B融资)、TechCrunch 2024-10(Worldcoin→World)、Wikipedia World(blockchain)、openai.com/index/sora-is-here/ | 贡献清单v1已穷举八类；新增F9(Tools for Humanity/World联合创始人/25M用户/Orb)、F10(for-profit结构转型2024-25)、F11(TIME 100 AI)；扩写F5(Microsoft $10B+；融资里程碑$157B/$300B)；扩写F6-F7(GPT-4o/o1/Sora具体产品里程碑)；新增C9-C10。清单见contributions/F07_Sam_Altman.md。对分数潜在影响：D4.1(World另立生态)、D8(公众叙事/治理博弈深化)，待60人齐后统一重评。 |
| F08 | Dario Amodei | updated | darioamodei.com、hertzfoundation.org、anthropic.com、TechCrunch 2021-05、Senate Judiciary 2023-07、DataCenter Dynamics(Amazon $4B)、Fortune(Google/估值)、arXiv 2212.15006(Constitutional AI) | 贡献清单v1已穷举八类；更新F4(GPT-3论文名arXiv 2005.14165/6万被引)；大幅扩写F5(Amazon $4B/Google $2B+/$61.5B估值)；大幅扩写F6(Constitutional AI论文名/RSP v1名称/ASL框架/Claude 3/Claude 3.5)；新增F8(Machines of Loving Grace 2024-10)、F9(TIME 100)；新增C9-C10。清单见contributions/F08_Dario_Amodei.md。对分数潜在影响：D4.1(Amazon/Google投资规模→深化)、D6(RSP/ASL→强化)，待60人齐后统一重评。 |
| F09 | Andrej Karpathy | updated | cs.stanford.edu、TIME100 AI 2024、TechCrunch 2024-07(Eureka Labs)、Axios 2026-05(Anthropic)、github.com/karpathy/(nanoGPT/micrograd/makemore)、youtube.com/@AndrejKarpathy | 贡献清单v1已穷举八类；既有facts已较完整；扩写F4(nanoGPT 40k stars/micrograd/makemore/YouTube 70万订阅/Software 2.0博文具体内容)；新增F9(DenseCap CVPR 2016/TIME100 AI 2024)；新增C9。清单见contributions/F09_Andrej_Karpathy.md。对分数潜在影响：D5(教育影响量化强化)，待60人齐后统一重评。 |
| F10 | Chris Olah | updated | colah.github.io、distill.pub、openai.com/index/microscope/、transformer-circuits.pub、anthropic.com/research(Towards/Scaling Monosemanticity) | 贡献清单v1已穷举八类；大幅扩写F3(colah.github.io博客/"Understanding LSTM Networks"；Distill on hiatus说明)；大幅扩写F4(Circuits论文名"Zoom In"/Transformer Circuits Framework 2021)；大幅扩写F5(Toy Models of Superposition/Towards Monosemanticity/Scaling Monosemanticity具体论文名)；新增C8。清单见contributions/F10_Chris_Olah.md。对分数潜在影响：D1.1(论文名强化confirmed)，待60人齐后统一重评。 |
| F11 | Andrew Ng | updated | andrewng.org、hai.stanford.edu、deeplearning.ai、ir.baidu.com、ir.aboutamazon.com、coursera.org、arXiv 1112.6209(Google cat ICML 2012) | 贡献清单v1已穷举八类；更新F2(AI for Everyone 100万+学习者)；大幅扩写F3(Coursera 148M+注册/DeepLearning.AI 700万学习者/The Batch 25万订阅)；更新F4(Google cat论文名arXiv 1112.6209/被引3500+)。清单见contributions/F11_Andrew_Ng.md。对分数潜在影响：D5(教育规模强化)，待60人齐后统一重评。 |
| F12 | Fei-Fei Li | updated | hai.stanford.edu、profiles.stanford.edu、worldlabs.ai、CVPR 2009 ImageNet(55k被引)、IJCV 2015 ILSVRC(50k被引)、Princeton 2024-02(The Worlds I See)、qeprize.org/vinfutureprize.org(2023) | 贡献清单v1已穷举八类；大幅扩写F3(ImageNet论文名CVPR 2009/55k被引；ILSVRC IJCV 2015/50k被引)；更新F8(World Labs Series A $230M/2024)；扩写F9(QE Prize 2023年份+共同获奖者/VinFuture 2023)；新增F10(Karpathy/Justin Johnson学生谱系/The Worlds I See回忆录)；新增C10。清单见contributions/F12_Fei-Fei_Li.md。对分数潜在影响：D1.1(ImageNet引用量强化/ILSVRC系统化)、D7.3(学生谱系confirmed)，待60人齐后统一重评。 |
| F13 | 黄学东 | updated | zoom.com/en/about/team/、blogs.microsoft.com/ai/、microsoft.com/en-us/research/(human-parity)、arXiv 1610.05256、zoom.com/en/blog/ | 贡献清单v1已穷举八类；既有facts已较完整；更新F3(论文名arXiv 1610.05256/被引1000+)；更新F6(NAE/AAAS院士2023年份)。清单见contributions/F13_黄学东.md。对分数潜在影响：D1.1(论文名补入强化)，待60人齐后统一重评。 |
| F14 | 沈向洋 | updated | idea.edu.cn/teams/harry、microsoft.com/en-us/research/people/hshum/、hkbu.edu.hk(荣誉博士)、tsinghua.edu.cn(AIR记录) | 贡献清单v1已穷举八类；既有facts已较完整；更新F9(NAE外籍院士2017年份)；注：AIR院长已确认为张亚勤/刘洋，不属于沈向洋。清单见contributions/F14_沈向洋.md。对分数潜在影响：minimal，待60人齐后统一重评。 |
| F15 | 周志华 | updated | cs.nju.edu.cn、lamda.nju.edu.cn、computer.org/profiles/zhi-hua-zhou、清华大学出版社(西瓜书) | 贡献清单v1已穷举八类；既有facts已较完整；更新F8(各奖年份：IEEE McCluskey 2019/CCF-ACM 2020/中科院院士2021)。清单见contributions/F15_周志华.md。对分数潜在影响：minimal，待60人齐后统一重评。 |
| F16 | 朱军 | updated | 清华计算机系官方页、个人主页(ml.cs.tsinghua.edu.cn/~jun/)、arXiv(DPM-Solver 2206.00927/Analytic-DPM 2201.06503/DPM-Solver++ 2211.01095)、NeurIPS 2022官方、ICLR 2022 Outstanding Paper博客、Semantic Scholar(DPM-Solver 1007引/Analytic-DPM 385引)、陈嘉庚奖官网(tsaf.cas.cn)、清华计算机系IEEE/AAAI/ACM Fellow公告、智源(科学探索奖2020)、GitHub(tianshou/zhusuan)、36氪(RealAI/生数科技融资)、智源(Vidu用户规模) | 贡献清单v1已穷举八类；新增F7(ACM Fellow 2025)/F8(陈嘉庚奖2024/科学探索奖2020/CCF奖2017/MIT TR35 2017)；扩写F3(ZhuSuan ~2.2k stars/Tianshou ~8.8k stars+JMLR 2022)；大幅扩写F4(DPM-Solver NeurIPS 2022 1007引/Highly Influential/被Huawei-OpenAI-Apple采用+DPM-Solver+++U-ViT+UniDiffuser)；扩写F5(RealAI 2018创立/A轮超3亿+生数科技Shengsu 2023/Vidu 1000万用户/ARR $2000万/B轮近20亿)；补IEEE Fellow年份2023/AAAI Fellow年份2024。清单见contributions/F16_朱军.md。对分数潜在影响：D2.2(DPM-Solver工业采用强化)、D3/D4(生数科技/RealAI深化)、D6.2(三重Fellow confirmed)，待60人齐后统一重评。 |
| F17 | 汤晓鸥 | updated | 商汤官方追思/学术成就页(sensetime.com/xo)、MMLab官网(mmlab.ie.cuhk.edu.hk)、Semantic Scholar(暗原色先验~11k引)、GitHub(open-mmlab/InternLM)、上海AI实验室官网、极客公园(商汤IPO)、腾讯新闻/网易(MMLab 134名学生)、媒体报道(IEEE Fellow 2009/DeepID 98.52%) | 贡献清单v1已穷举八类；新增F4(DeepID系列98.52%/超DeepFace)+F5(2011-13 ICCV/CVPR 14篇占48%)+F8(IEEE Fellow 2009)；扩写F2(MMLab 134名/代表学生谱系:何恺明/林达华/颜水成/贾佳亚)+F3(暗原色先验~11k引/作者顺序)+F6(商汤$52亿融资/2021上市最高市值3200亿港元)+F7(OpenMMLab规模30+库/~90k stars/110国/InternLM书生)。清单见contributions/F17_汤晓鸥.md。对分数潜在影响：D1.1(暗原色引用量强化)、D3/D4(商汤上市规模confirmed)、D7.3(134名学生谱系强化)，待60人齐后统一重评。 |
| F18 | 张钹 | updated | 清华大学官方/AI研究院(tsinghua.edu.cn)、智源社区、CCF官网(ccf.org.cn/c/2015-02-04/647520)、维基百科、Amazon(英文专著)、媒体报道(人民日报/腾讯新闻/知乎) | 贡献清单v1已穷举八类；既有facts已较完整；新增F7(英文专著"Quotient Space…" Morgan Kaufmann 2014/200+论文)+F8(ICL欧洲AI奖1984/国家自然科学三等奖1995/CCF终身成就奖2014/吴文俊最高成就奖2019)；新增C8。清单见contributions/F18_张钹.md。对分数潜在影响：D6.2(多重奖项strong confirmed)，待60人齐后统一重评。 |
| F19 | 高文 | updated | 百度百科、北大校友网(pku.org.cn/info/1013/2163, ACM Fellow 2013)、AVS工作组官网(avs.org.cn, AVS3/DVB采纳)、鹏城实验室官网、USTC通知(IEEE Fellow 2009)、DVBCN | 贡献清单v1已穷举八类；既有facts已较完整；补IEEE Fellow年份2009/ACM Fellow年份2013；新增F7(AVS3 2021/DVB 2022采纳/8K标准效率提升30%/北大数字视频国家工程实验室主任)；新增C8。清单见contributions/F19_高文.md。对分数潜在影响：D5.1(AVS3 DVB国际标准confirmed)，待60人齐后统一重评。 |
| F20 | 梁文锋 | updated | GitHub(deepseek-ai/DeepSeek-R1 92k stars)、arXiv 2412.19437(V3 Tech Report)、arXiv 2501.12948(R1)、api-docs.deepseek.com(R1-0528/V3.2)、TechCrunch 2025-01-27、HuggingFace统计、marketingltb.com(DeepSeek统计) | 贡献清单v1已穷举八类；扩写F5(V2 236B+V3 671B/37B激活/$5.6M训练/2048 H800/arXiv号)；扩写F6(R1 671B MoE/超越o1 benchmarks/92k GitHub stars/500+衍生模型/2.5M下载/股市震荡)；新增F8(R1-0528 AIME 87.5%/V3.2 2025-12智能体)；清单见contributions/F20_梁文锋.md。对分数潜在影响：D1.1(R1 benchmark结果强化)、D2.2(开源生态规模confirmed)，待60人齐后统一重评。 |
| F21 | 杨植麟 | updated | 贡献清单v1 contributions/F21_杨植麟.md；TechCrunch/Moonshot官网/arXiv 2407.00079/GitHub | 补充融资链($60M→$2B@$20B)/Kimi MAU 3600万/K1.5(2025-01)/K2 MoE开源/Mooncake FAST'25 |
| F22 | 王慧文 | updated | 贡献清单v1 contributions/F22_王慧文.md；美团港交所公告/36氪/创业邦 | 补充美团港股(3690.HK)/光年之外个人投入$5000万/A轮$2.3亿/美团收购$2.34亿结构 |
| F23 | 王小川 | updated | 贡献清单v1 contributions/F23_王小川.md；百川智能官网/GitHub/TechCrunch/新浪财经 | 补充搜狗NYSE IPO/$21.3亿私有化/百川融资@$28亿/Baichuan-M3 HealthBench全球第一 |
| F24 | 李开复 | updated | 贡献清单v1 contributions/F24_李开复.md；创新工场官网/01.ai GitHub/NYT Books/媒体 | 补充创新工场AUM$3B/500+投组/零一万物Yi-34B 7800stars/癌症经历细节/双榜单畅销书 |
| F25 | Stuart Russell | updated | 贡献清单v1 contributions/F25_Stuart_Russell.md；CHAI官网/Semantic Scholar/Senate记录/BBC | 补充AIMA 59k引用/CHAI资助$12M+/OBE 2021/BBC Reith Lectures/h-index 106/155k引用 |
| F26 | Nick Bostrom | updated | 贡献清单v1 contributions/F26_Nick_Bostrom.md；FHI关闭公告/牛津调查/ICAI/Wikipedia | 补充FHI 2024关闭原因/著作28+语种/世界超人类主义协会创立/争议邮件调查结论/h-index 63 |
| F27 | Paul Christiano | updated | 贡献清单v1 contributions/F27_Paul_Christiano.md；arXiv/ARC Evals官网/METR公告 | 补充RLHF 5324引用/METR创立/RSP被9家AI采纳/ELK报告(2021-22)/iterated amplification |
| F28 | Richard Sutton | updated | 贡献清单v1 contributions/F28_Richard_Sutton.md；Semantic Scholar/Amii官网/Bitter Lesson原文 | 补充h-index 101/186k引用/RL教材96662/TD 9201/策略梯度11127/Bitter Lesson日期URL |
| F29 | Ian Goodfellow | updated | 贡献清单v1 contributions/F29_Ian_Goodfellow.md；Semantic Scholar/Inceptive官网/arXiv | 补充h-index 103/430k引用/GAN 117960/教材99251/FGSM 30602/Inceptive CTO 2023 |
| F30 | Aidan Gomez | updated | 贡献清单v1 contributions/F30_Aidan_Gomez.md；Semantic Scholar/Cohere官网/BetaKit | 补充Attention 173k+引用/Cohere融资$1.6B+@$7B/Command R+/UofT学士2018/Roger Grosse导师 |
| F31 | 刘铁岩 | updated | MSRA「2021 ACM Fellow」官方文章、github.com/microsoft/LightGBM、LightGBM 作者页、Alan Turing Institute 人物页、清华电子系/校友总会页、MS Research 本人页 | 贡献清单 v1 已穷举八类维度并回填 F8–F14：对偶学习/listwise/Graphormer/LightLDA/FastSpeech/Suphx/新冠预测/T-DETECT/被引3.5万·h68/ACM Fellow2021/顶会主席·期刊副主编/专著近10万册/三清学历。清单见 `research/contributions/F31_刘铁岩.md`；对分数的建议见 evidence，待 60 人齐后统一重评。唯「具体学生谱系」仍 needs-source |
| F32 | 张林峰 | updated | DeePMD-kit GitHub、深势科技/Bohrium/Hermite 官网、arXiv(1707.09571/1712.03641/2004.11658/2008.00167)、北大讲座预告、36氪/投中网/财联社融资报道、新华网/人民网专访、百度百科/LinkedIn | 贡献清单 v1 已穷举八类并回填 F8–F12、更正 F1（博导 Roberto Car，非鄂维南）：新增 AISI 院长、完整融资链(累计十几亿/估值数十倍)、DeePMD-kit 框架规模、Bohrium/Hermite/RiDYMO/Piloteye 产品矩阵、Uni 系列、DeepModeling 开源社区、福布斯/胡润 U30、Gordon Bell 亚洲首位。清单见 `research/contributions/F32_张林峰.md`；建议 D4.1/D7.3/D2 上调，待 60 人齐后统一重评。Scholar 精确被引与学生谱系仍 needs-source |
| F33 | 鄂维南 | updated | 贡献清单v1 contributions/F33_鄂维南.md；ICIAM官网/Princeton DOF/arXiv/GitHub | 补充ICIAM Collatz(2003)+Maxwell(2023)双奖全球首例/DeePMD-kit~2k stars/完整学术谱系 |
| F34 | 唐杰 | updated | 贡献清单v1 contributions/F34_唐杰.md；AMiner官网/雷峰网/GitHub THUDM/新浪财经 | 补充IEEE/ACM/AAAI Fellow年份/AMiner 3000万用户/ChatGLM 41100 stars/智谱港股IPO |
| F35 | 雷军 | updated | 贡献清单v1 contributions/F35_雷军.md；小米官网/HK交易所/小米汽车官网/研究报告 | 补充IPO 240亿HKD/SU7首年136,854辆/玄戒O1芯片(3nm)/MiMo-7B/总营收3659亿/AIoT 9亿设备 |
| F36 | 张鹏 | updated | 贡献清单v1 contributions/F36_张鹏.md；智谱官网/港交所/arXiv GLM/GitHub THUDM | 补充GLM IPO 02513.HK/578.9亿首日/"大模型第一股"/融资83亿/CogVideoX ICLR 2025 |
| F37 | 闫俊杰 | updated | 贡献清单v1 contributions/F37_闫俊杰.md；MiniMax官网/港交所/媒体报道 | 补充MiniMax融资$1.55B/IPO 830亿港元市值/abab6.5万亿参数/星野MAU 2760万/7轮融资详情 |
| F38 | 姜大昕 | updated | 贡献清单v1 contributions/F38_姜大昕.md；阶跃星辰官网/媒体报道 | 补充StepFun融资轮次/Step-1/Step-2模型/Step-Video/MSRA全球伙伴VP背景 |
| F39 | 印奇 | updated | 贡献清单v1 contributions/F39_印奇.md；旷视官网/GitHub MegEngine/港交所公告 | 补充MegEngine 4.8k stars/Brain++三层架构/旷视IPO撤回(2024.11)/D轮$40亿估值/力帆科技董事长 |
| F40 | 余凯 | updated | 贡献清单v1 contributions/F40_余凯.md；港交所公告/地平线官网/汽车行业报告 | 补充IPO HK$63.2B(09660.HK)/600万片芯片出货/Journey6/27 OEM合作/大众合资Carizon |
| F41 | 朱珑 | updated | 贡献清单v1 contributions/F41_朱珑.md；NIST FRVT/Nature Medicine/依图官网 | 补充NIST FRVT 2017-18双冠/Nature Medicine 136万就诊AI诊断/求索SoC/科创板CDR终止(非HK IPO) |
| F42 | 陈天石 | updated | 贡献清单v1 contributions/F42_陈天石.md；ASPLOS 2014/寒武纪上交所/官网 | 补充ASPLOS 2014 Best Paper(大陆首次)/华为麒麟采用/IPO首日千亿/2024营收11.74亿+65% |
| F43 | 王兴兴 | updated | 贡献清单v1 contributions/F43_王兴兴.md；Unitree官网/GitHub/媒体/TIME | 补充G1人形$16K全球最低/四足23700台全球70%份额/春晚16台H1/Series C 7亿@120亿/TIME 100 AI |
| F44 | 张一鸣 | updated | 贡献清单v1 contributions/F44_张一鸣.md；Bloomberg/Fortune/媒体报道 | 补充ByteDance$3000亿估值/2024营收$1550亿/豆包3.3亿用户/南开双专业(纠正)/净资产$928亿 |
| F45 | 周靖人 | updated | 贡献清单v1 contributions/F45_周靖人.md；Qwen官网/GitHub QwenLM/ModelScope | 补充Qwen3 27k stars/36T tokens/119语言/235B-A22B MoE; QwQ-32B超o1; 100+模型4000万下载 |
| F46 | 王海峰 | updated | 贡献清单v1 contributions/F46_王海峰.md；飞桨官网/GitHub/百度IR/媒体报道 | 补充PaddlePaddle 23937 stars/文心一言上线/昆仑芯片7nm量产/深度学习国家工程研究中心(中国首个) |
| F47 | 田奇 | updated | 贡献清单v1 contributions/F47_田奇.md；Nature官方/Science评选/华为诺亚/IEEE/ACM | 补充h-index 141/112k引用/IEEE Fellow 2016/ACM Fellow 2024/AAAI Fellow 2026/盘古气象Nature/Science十大突破#1 |
| F48 | 张正友 | updated | 贡献清单v1 contributions/F48_张正友.md；Semantic Scholar/ICCV 2013/IEEE/腾讯官网 | 补充标定法23325引用/ICCV Helmholtz 2013首届奖/IEEE Fellow 2004/ACM Fellow 2013/腾讯T17最高技术等级 |
| F49 | 何恺明 | updated | 贡献清单v1 contributions/F49_何恺明.md；Nature 2025/NeurIPS 2025/MIT官网/Google DeepMind | 补充ResNet 328513引用/"21世纪最高被引"(Nature 2025)/MIT副教授+终身教职2025/未来科学奖2023/Faster R-CNN NeurIPS ToT |
| F50 | 谢赛宁 | updated | 贡献清单v1 contributions/F50_谢赛宁.md；Semantic Scholar/AMI Labs官网/NYU | 补充AMI Labs co-founder种子轮$1.03B(欧洲最大)/DiT 7456引用(Sora基础)/ConvNeXt 13962/h-index 53 |
| F51 | 张祥雨 | updated | 贡献清单v1 contributions/F51_张祥雨.md；Semantic Scholar/GitHub MegEngine/StepFun官网 | 补充h-index 80/453k引用/ResNet单篇323978/StepFun联创Step-2国内首个万亿MoE/ShuffleNetV2 ECCV |
| F52 | 朱松纯 | updated | 贡献清单v1 contributions/F52_朱松纯.md；IEEE官网/Science/BIGAI官网/Google Scholar | 补充h-index 110/51k引用/IEEE Fellow 2011/通通AGI儿童2024/Tong Test/BIGAI创立/$30M DARPA经费 |
| F53 | 张亚勤 | updated | 贡献清单v1 contributions/F53_张亚勤.md；IEEE官网/清华AIR官网/百度IR | 补充IEEE Fellow 1997最年轻/CAE 2021/清华AIR 20+教师400+实习/Apollo平台/《智能涌现》2023 |
| F54 | 黄铁军 | updated | 贡献清单v1 contributions/F54_黄铁军.md；BAAI官网/国家科学技术奖/AVS官网/IEEE | 补充BAAI首任院长/AVS秘书长/国家技术发明奖2017/吴文俊奖2022/四会士/SpikeCV类脑框架 |
| F55 | 林达华 | audited-v1 | OpenMMLab 官网、MMDetection GitHub/arXiv、OpenMMLab ReadTheDocs | 现有 facts 已覆盖 OpenMMLab 作为视觉开源基础设施、复现标准与从视觉到大模型开源的主线；后续可补具体项目名 MMDetection/MMCV/MMEngine/MMDeploy 作为证据颗粒度增强，但暂未发现会改变能力归属的大缺口 |
| F56 | 贾佳亚 | updated | 贡献清单v1 contributions/F56_贾佳亚.md；IEEE官网/ACM官网/港交所/TPAMI | 补充IEEE Fellow 2018/ACM Fellow 2025/TPAMI副主编首位华人/思谋独角兽$12.3亿/港交所递表2026/h≥120 |
| F57 | 颜水成 | updated | 贡献清单v1 contributions/F57_颜水成.md；ACM/AAAI/IEEE官网/NUS官网 | 补充NIN论文1×1卷积(9900+引)/h≥125/110k引用/ACM Fellow 2020/AAAI Fellow 2022/Sea SAIL创立/NUS回归2025 |
| F58 | 刘知远 | updated | 贡献清单v1 contributions/F58_刘知远.md；GitHub thunlp/面壁智能官网/arXiv MiniCPM | 补充MiniCPM-V 25565 stars/面壁融资10亿+/WantWords 7108 stars/密度法则100天翻倍/OpenNRE+OpenKE |
| F59 | 孙茂松 | updated | 贡献清单v1 contributions/F59_孙茂松.md；ACL官网/欧洲院官网/清华新闻/Scholar | 补充ACL Fellow 2022(唯一华人)/欧洲人文院院士2020/九歌千万首/THULAC 2086 stars/Scholar 40k引用 |
| F60 | 李航 | updated | 贡献清单v1 contributions/F60_李航.md；ACL官网/IEEE/出版社/字节跳动研究 | 补充ACL Fellow 2019(第5位华人)/IEEE+ACM Fellow/统计学习方法4版全程/华为2012-17+字节2017-至今 |

### 增补（第二批，F61+）
| F61 | 李彦宏 | audited-v1 | 贡献清单v1 contributions/F61_李彦宏.md；US5920859专利(S1)/Nasdaq 8-K(S1)/TIME100 AI 2023(S1)/Baidu IR/Bloomberg | 新人入库：RankDex超链分析专利(早于PageRank)/百度2000创办+2005纳斯达克IPO/文心一言3亿用户/昆仑芯+Apollo/All in AI千亿研发/TIME100 AI唯一中国企业家。建议9维向量见 facts 末，待 v4 统一重评，未入 scores.md。 |
| F62 | 王坚 | audited-v1 | 贡献清单v1 contributions/F62_王坚.md；CAE院士增选2019(S1)/飞天电子学会特等奖2017(S1)/Alibaba Cloud Community/ITU | 新人入库：飞天中国唯一自研云OS提出者+总架构师/阿里云2009创办($135亿营收)/城市大脑首创/之江实验室主任/2019工程院院士(民营首位)。D8信念逆向极强。建议9维向量见 facts 末，待 v4 统一重评，未入 scores.md。 |

## 下一批优先级

第一优先级是工具/框架/平台型人物，因为这类成果最容易被人物叙事漏掉：

1. F31 刘铁岩：继续审计 Graphormer、LightLDA、FastSpeech、dual learning。
2. F55 林达华：审计 OpenMMLab 全家桶是否足够进入 D2.2/D7.5。
3. F58 刘知远、F34 唐杰：审计 OpenKE/OpenNRE/CogDL/AMiner/GLM 归属边界。
4. F49 何恺明、F50 谢赛宁、F51 张祥雨：审计 ResNet/ResNeXt/ConvNeXt/ShuffleNet/RepLKNet 的共同贡献边界。
5. F32 张林峰、F33 鄂维南：审计 DeePMD/DP-GEN/AI4S 工具链与平台化证据。
