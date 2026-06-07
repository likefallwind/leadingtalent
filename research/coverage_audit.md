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
| F05 | Ilya Sutskever | queued |  | 需复核 seq2seq、AlexNet、GPT/Scaling、Superalignment、SSI 的来源与下游编码 |
| F06 | Demis Hassabis | queued |  | 需复核 DeepMind、AlphaFold/AlphaGo/Isomorphic、2024 Nobel 官方来源 |
| F07 | Sam Altman | queued |  | 需复核 YC、OpenAI capped-profit、Microsoft/Azure、ChatGPT/API、治理危机与公共治理 |
| F08 | Dario Amodei | queued |  | 需复核 GPT-2/GPT-3、Anthropic、Constitutional AI、RSP、国会证词 |
| F09 | Andrej Karpathy | queued |  | 需复核 CS231n、Tesla Autopilot、nanoGPT、OpenAI、Eureka Labs |
| F10 | Chris Olah | queued |  | 需复核 Distill、mechanistic interpretability、Anthropic transformer circuits |
| F11 | Andrew Ng | queued |  | 需复核 Google Brain、Coursera、DeepLearning.AI、Landing AI、AI Fund、data-centric AI |
| F12 | Fei-Fei Li | queued |  | 需复核 ImageNet、Stanford HAI、AI4ALL、World Labs、空间智能 |
| F13 | 黄学东 | queued |  | 需复核微软语音组、Switchboard 人类水平、Azure AI、Zoom CTO、专利/院士 |
| F14 | 沈向洋 | queued |  | 需复核 MSRA、Bing、微软全球 AI、AIR、IDEA/小冰相关边界 |
| F15 | 周志华 | queued |  | 需复核 LAMDA、集成学习/弱监督/开放环境机器学习、西瓜书、CCF/IEEE/AAAI 角色 |
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
