# 全员覆盖缺口审计（Coverage Gap Audit）

> 目的：防止 `profiles/` 与 `facts/` 漏掉关键硬成果，导致后续规范能力编码和 8 维评分在错误事实集上显得“客观”。
> 这是进入 `research/evidence/` 前的基础步骤。

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
| F16 | 朱军 | queued |  | 需复核 DPM-Solver、U-ViT、ZhuSuan、概率机器学习、鲁棒/安全贡献 |
| F17 | 汤晓鸥 | queued |  | 需复核 MMLab、DeepID、商汤、暗原色先验、人才谱系与产业化事实 |
| F18 | 张钹 | queued |  | 需复核商空间、第三代 AI、清华智能实验室、中国 AI 学科建设 |
| F19 | 高文 | queued |  | 需复核 AVS/AVS3、鹏城实验室、鹏城云脑、OpenI、视频编码标准 |
| F20 | 梁文锋 | queued |  | 需复核 DeepSeek V2/V3/R1、开源、技术报告、幻方算力、全球影响范围 |
| F21 | 杨植麟 | queued |  | 需复核 Transformer-XL、XLNet、Moonshot/Kimi、Mooncake、长上下文与产品化 |
| F22 | 王慧文 | queued |  | 需复核美团、光年之外、资本/组织与大模型创业事实边界 |
| F23 | 王小川 | queued |  | 需复核搜狗输入法/搜索、百川智能、大模型产品、清华/IOI 背景 |
| F24 | 李开复 | queued |  | 需复核微软/Google China/创新工场/零一万物/AI 投资生态 |
| F25 | Stuart Russell | queued |  | 需复核 AIMA、CHAI、Human Compatible、国会证词、AI safety 报告 |
| F26 | Nick Bostrom | queued |  | 需复核 Superintelligence、FHI、existential risk、哲学/治理影响 |
| F27 | Paul Christiano | queued |  | 需复核 RLHF、iterated amplification、ARC、OpenAI alignment 贡献 |
| F28 | Richard Sutton | queued |  | 需复核 TD learning、policy gradient、RL textbook、Bitter Lesson、DeepMind/Alberta |
| F29 | Ian Goodfellow | queued |  | 需复核 GAN、deep learning textbook、adversarial examples、Google/OpenAI/Apple |
| F30 | Aidan Gomez | queued |  | 需复核 Transformer、Cohere、企业级 LLM、开源/社区边界 |
| F31 | 刘铁岩 | updated | MSRA「2021 ACM Fellow」官方文章、github.com/microsoft/LightGBM、LightGBM 作者页、Alan Turing Institute 人物页、清华电子系/校友总会页、MS Research 本人页 | 贡献清单 v1 已穷举八类维度并回填 F8–F14：对偶学习/listwise/Graphormer/LightLDA/FastSpeech/Suphx/新冠预测/T-DETECT/被引3.5万·h68/ACM Fellow2021/顶会主席·期刊副主编/专著近10万册/三清学历。清单见 `research/contributions/F31_刘铁岩.md`；对分数的建议见 evidence，待 60 人齐后统一重评。唯「具体学生谱系」仍 needs-source |
| F32 | 张林峰 | updated | DeePMD-kit GitHub、深势科技/Bohrium/Hermite 官网、arXiv(1707.09571/1712.03641/2004.11658/2008.00167)、北大讲座预告、36氪/投中网/财联社融资报道、新华网/人民网专访、百度百科/LinkedIn | 贡献清单 v1 已穷举八类并回填 F8–F12、更正 F1（博导 Roberto Car，非鄂维南）：新增 AISI 院长、完整融资链(累计十几亿/估值数十倍)、DeePMD-kit 框架规模、Bohrium/Hermite/RiDYMO/Piloteye 产品矩阵、Uni 系列、DeepModeling 开源社区、福布斯/胡润 U30、Gordon Bell 亚洲首位。清单见 `research/contributions/F32_张林峰.md`；建议 D4.1/D7.3/D2 上调，待 60 人齐后统一重评。Scholar 精确被引与学生谱系仍 needs-source |
| F33 | 鄂维南 | needs-followup | DeePMD-kit GitHub/arXiv、Deep Ritz/PNAS 论文线索、DeepModeling 文档 | 现有 facts 覆盖 AI4S 和数学基础，但需补 Deep Ritz/high-dimensional PDE、DeePMD-kit/DeepModeling 谱系、DeepPKS 等候选，判断是否强化 `D1.1/D1.3/D5.5/D8.3` |
| F34 | 唐杰 | needs-followup | 唐杰清华个人主页、ChatGLM/GLM arXiv、CogDL PyPI、Zhipu/Z.ai 资料 | 现有 facts 已覆盖 AMiner/GLM/ChatGLM/智谱主线；还需补充 GLM-130B、ChatGLM 下载/使用规模、CogView/CogVideo、CodeGeeX、CogDL 与 AMiner 用户规模，判断是否强化 `D1.1/D2.2/D7.3` |
| F35 | 雷军 | queued |  | 需复核金山、小米、MIUI、IoT/汽车/机器人、AIoT 与资本生态 |
| F36 | 张鹏 | queued |  | 需复核 GLM/ChatGLM、智谱商业化、开源/企业平台、清华 KEG 背景 |
| F37 | 闫俊杰 | queued |  | 需复核 MiniMax、Talkie、abab 模型、海螺 AI、多模态/语音产品 |
| F38 | 姜大昕 | queued |  | 需复核 Bing/Cortana/STCA、Step 系列、StepFun-Prover、融资与治理升级 |
| F39 | 印奇 | queued |  | 需复核 Face++、Brain++、MegEngine、旷视城市/IoT、AI 基础设施转型 |
| F40 | 余凯 | queued |  | 需复核百度 IDL、地平线征程芯片、车规量产数据、SuperDrive、Wintel 愿景 |
| F41 | 朱珑 | queued |  | 需复核依图、医疗 AI、求索芯片、计算机视觉与监管/商业化边界 |
| F42 | 陈天石 | queued |  | 需复核寒武纪、DianNao 系列、MLU、上市、国产算力生态 |
| F43 | 王兴兴 | queued |  | 需复核 Unitree 四足/人形机器人、产品销量、开源/低成本工程路线 |
| F44 | 张一鸣 | queued |  | 需复核推荐系统、今日头条/抖音/TikTok、组织算法文化、AI/大模型布局 |
| F45 | 周靖人 | queued |  | 需复核 Qwen/通义千问、阿里云 CTO、开源模型、云上 AI 平台 |
| F46 | 王海峰 | queued |  | 需复核飞桨、文心、百度搜索/NLP/知识图谱、昆仑芯/全栈 AI |
| F47 | 田奇 | queued |  | 需复核华为诺亚、盘古大模型、盘古天气、视觉研究、工业/云平台落地 |
| F48 | 张正友 | queued |  | 需复核 Zhang calibration、微软/腾讯、Robotics X、机器人/三维视觉 |
| F49 | 何恺明 | needs-followup | MIT 个人主页、Mask R-CNN arXiv/OpenAccess、MAE arXiv、MoCo GitHub/论文线索 | 现有 facts 覆盖 ResNet/研究品味，但需补 Mask R-CNN、MoCo、MAE、Faster R-CNN 相关视觉基础件，判断 `D1.1/D7.3` 是否低估 |
| F50 | 谢赛宁 | needs-followup | 个人主页、GitHub、ResNeXt/ConvNeXt/MAE/DiT 论文线索 | 现有 facts 需复核是否漏掉 ConvNeXt、DiT、MAE 共同贡献、AMI Labs CSO 等近期角色，判断是否影响 `D1.1/D8.4` |
| F51 | 张祥雨 | needs-followup | ShuffleNet OpenAccess、RepLKNet 论文线索、ResNet 论文/作者信息、旷视相关资料 | 现有 facts 覆盖 ResNet/ShuffleNet/RepLKNet 主线；需补具体论文证据与 MegEngine/Brain++ 角色边界，判断是否强化 `D2.2/D5.3` |
| F52 | 朱松纯 | queued |  | 需复核 stochastic grammar、Raven、BIGAI、通用智能、认知/具身路线 |
| F53 | 张亚勤 | queued |  | 需复核微软/百度/清华 AIR、自动驾驶/产业研究、AI 治理/教育 |
| F54 | 黄铁军 | queued |  | 需复核智源、悟道、FlagOpen/FlagEval、类脑计算、开源生态 |
| F55 | 林达华 | audited-v1 | OpenMMLab 官网、MMDetection GitHub/arXiv、OpenMMLab ReadTheDocs | 现有 facts 已覆盖 OpenMMLab 作为视觉开源基础设施、复现标准与从视觉到大模型开源的主线；后续可补具体项目名 MMDetection/MMCV/MMEngine/MMDeploy 作为证据颗粒度增强，但暂未发现会改变能力归属的大缺口 |
| F56 | 贾佳亚 | queued |  | 需复核图像去模糊/修复、CUHK、SmartMore、工业视觉平台 |
| F57 | 颜水成 | queued |  | 需复核 SAIL/Sea AI Lab、压缩/AutoML/视觉、360/商汤经历 |
| F58 | 刘知远 | needs-followup | OpenNRE GitHub/arXiv、OpenKE GitHub、OpenBMB/MiniCPM GitHub、清华新闻、MiniCPM arXiv | 现有 facts 覆盖 OpenBMB/密度法则/面壁智能主线，但缺少 OpenNRE、OpenKE、MiniCPM/MiniCPM-V 等具体工具与模型证据；需判断是否强化 `D2.2/D7.3/D7.5/D8.1` |
| F59 | 孙茂松 | queued |  | 需复核自然标注语料、九歌、学堂在线、OpenBMB/密度法则、中文 NLP 谱系 |
| F60 | 李航 | queued |  | 需复核统计学习方法、Learning to Rank、华为诺亚、字节 AI Lab、工业 NLP/搜索 |

## 下一批优先级

第一优先级是工具/框架/平台型人物，因为这类成果最容易被人物叙事漏掉：

1. F31 刘铁岩：继续审计 Graphormer、LightLDA、FastSpeech、dual learning。
2. F55 林达华：审计 OpenMMLab 全家桶是否足够进入 D2.2/D7.5。
3. F58 刘知远、F34 唐杰：审计 OpenKE/OpenNRE/CogDL/AMiner/GLM 归属边界。
4. F49 何恺明、F50 谢赛宁、F51 张祥雨：审计 ResNet/ResNeXt/ConvNeXt/ShuffleNet/RepLKNet 的共同贡献边界。
5. F32 张林峰、F33 鄂维南：审计 DeePMD/DP-GEN/AI4S 工具链与平台化证据。
