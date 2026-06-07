# F03 Yoshua Bengio 完整主要贡献清单
> 原型：学术/工业研究科学家 + AI安全·治理·学者。
> 审计轮次：v1（2026-06-06）。本轮已查来源：
> - 个人官方页 https://yoshuabengio.org/
> - Google Scholar（research.com、citationmap.com、UdeM nouvelles 2025-10）
> - Wikipedia Yoshua Bengio 词条
> - Element AI 维基百科词条；Globe and Mail 收购报道（2021）
> - International AI Safety Report 官方页 https://internationalaisafetyreport.org/
> - Mila 官方页 https://mila.quebec/
> - ACM Turing Award 官方页
> - Deep Learning 教材 MIT Press / deeplearningbook.org
> - WebSearch: GAN citations / attention paper / Neural Probabilistic LM / LawZero

## 教育与履历（非贡献，用于深度可比）
McGill 计算机工程学士 1986、硕士 1988、博士 1991；MIT 博后 1991-92（Michael Jordan）；AT&T Bell Labs 博后 1992-93（与 LeCun）；蒙特利尔大学教授 1993-；Mila 创始人兼科学总监 1993-2025，现为创始人兼科学顾问；Element AI 联合创始人 2016-2020；LawZero 联合总裁兼科学总监 2025-。

## 1. 学术（论文/里程碑/高被引/开创概念）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| A Neural Probabilistic Language Model（神经语言模型/词向量基础） | 2003 | JMLR 2003；https://jmlr.org/papers/v3/bengio03a.html 【论文/报告】 | 7,600+ 被引（Semantic Scholar）；首次把词映射到连续空间，为 word2vec、预训练 LM 铺路 | 第一/通讯作者（Bengio, Ducharme, Vincent, Janvin） | 已覆盖 F6（笼统），**待补充论文名和被引量** |
| Learning Long-Term Dependencies with Gradient Descent is Difficult | 1994 | IEEE Transactions on Neural Networks 1994 【论文/报告】 | 揭示梯度消失/爆炸问题；为 LSTM、残差网络的理论基础 | 第一作者（Bengio, Simard, Frasconi） | **缺口待补**：梯度消失研究未进入 F03 facts |
| Neural Machine Translation by Jointly Learning to Align and Translate（注意力机制） | 2015 | ICLR 2015；arXiv 1409.0473 【论文/报告】 | 被引极高（>25,000）；引入 soft attention，成为 Transformer 注意力的直接前驱 | 共同通讯/指导者（Bahdanau, Cho, Bengio） | 已覆盖 F7（笼统），**待补充论文名和被引量** |
| Learning Phrase Representations using RNN Encoder-Decoder（seq2seq/编码器-解码器架构） | 2014 | EMNLP 2014；arXiv 1406.1078 【论文/报告】 | 奠定 seq2seq 框架，被引 20,000+；为机器翻译、摘要生成等序列任务奠基 | 共同通讯/指导者（Cho, van Merriënboer, …, Bengio） | 已覆盖 F7（笼统），**待补充** |
| Generative Adversarial Nets（GAN，Goodfellow et al.） | 2014 | NeurIPS 2014；arXiv 1406.2661 【论文/报告】 | 105,000+ 被引；Goodfellow 是 Bengio 博士生，GAN 在其研究组涌现 | 研究土壤/共同作者（Bengio 是 Goodfellow 导师，排名第六位共同作者） | 已覆盖 F8（笼统），**待补充被引量和角色说明** |
| Curriculum Learning | 2009 | ICML 2009 【论文/报告】 | 引入课程学习训练策略，被引 5,000+，广泛影响训练方法设计 | 第一/通讯作者 | **缺口待补**：未进入 F03 facts |
| Greedy Layer-Wise Training of Deep Networks | 2007 | NeurIPS 2007 【论文/报告】 | 逐层预训练使深度网络可训练；为 2006-2012 深度学习复兴核心方法之一 | 共同作者 | **缺口待补**：未进入 F03 facts |
| Deep Learning（教材，Goodfellow、Bengio、Courville） | 2016 | MIT Press；deeplearningbook.org 【论文/报告】 | 第一本全面深度学习教科书；被引数万次；成为全球高校标准教材 | 共同作者（Bengio 为第二作者） | **缺口待补**：未进入 F03 facts |
| 总被引量 / h-index | 2026 | research.com / citationmap.com；UdeM nouvelles 2025-10-24 【学术索引+大学官方页】 | h-index 254；1,091,407+ 总引用（2025-10 首破 100 万，全球在世科学家总被引第一） | — | **缺口待补**：量级数字未进入 facts |

## 2. 系统与框架（框架/工具链/平台/基准·数据集）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Theano（深度学习框架，蒙特利尔团队主导） | 2010-2017 | github.com/Theano/Theano；JMLR 2016 论文 【项目仓库+论文】 | 首批深度学习主流框架之一，TensorFlow/PyTorch 之前的事实标准；GitHub 9k+ Stars | 机构主导者/PI（学生团队开发） | **缺口待补**：未进入 F03 facts |

## 3. 产品与工程（产品/产品线/技术系统）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| （本类无个人主导工程产品；产业化通过 Element AI 进行）| — | — | — | — | — |

## 4. 公司与组织（公司/实验室/研究院）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Mila（魁北克 AI 研究院）创立 | 1993 | mila.quebec 官方；Wikipedia 【机构官方页】 | 全球最大深度学习学术研究中心之一（1,500+ 研究人员）；蒙特利尔成为全球 AI 中心的核心机构 | 创始人兼科学总监（1993-2025）→科学顾问 | 已覆盖 F9 |
| Element AI 联合创始人 | 2016 | Wikipedia Element AI条目；Globe and Mail 报道 【权威媒体】 | 募资 $102M（Series A）；2020 被 ServiceNow 以 $230M 收购；展示学术→产业转化 | 联合创始人（与 Gagné, Martel, Chapados, Beaudoin） | **缺口待补**：F03 facts 未提 Element AI |
| LawZero 联合创始 | 2025 | yoshuabengio.org；WebSearch 【本人官方页+权威媒体】 | ~$30M 启动资金；聚焦"低代理性/不以自我目标行动"AI 安全研究 | 联合总裁兼科学总监 | 已覆盖 F11（笼统） |

## 5. 标准与基础设施（标准/芯片/算力平台）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| （本类无；Theano 列于第 2 类）| — | — | — | — | — |

## 6. 学术服务与荣誉（Fellow/院士/大奖/委员会角色）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| 2018 ACM 图灵奖（与 Hinton, LeCun） | 2018 | ACM 官方 【官方页】 | CS 最高奖项 | 共同获奖者 | 已覆盖 F13 |
| 皇家学会 Fellow（伦敦+加拿大） | — | Royal Society 官方 | 英国 + 加拿大双重科学最高荣誉 | Fellow | 已覆盖 F13（笼统） |
| Officer of the Order of Canada | — | 加拿大总督官方 | 加拿大国家荣誉 | 获得者 | **缺口待补**：F13 未明确 |
| Knight of the Légion d'Honneur（法国荣誉军团骑士） | — | 法国政府官方 | 法国最高国家荣誉 | 获得者 | **缺口待补**：F13 未明确 |
| CIFAR Canada AI Chair（主持 Learning in Machines & Brains 项目） | 2004- | CIFAR 官方 | 长期与 Hinton 并行主持加拿大神经网络共同体 | 项目主持人 | 已覆盖 F9（笼统） |

## 7. 人才与生态（师承/培养学生/社区·教育影响）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| Ian Goodfellow（GAN 发明者，后任 Apple, Alphabet, DeepMind 研究负责人） | — | Wikipedia；Mila 校友名单 【百科+机构官方页】 | GAN 领域奠基人；苹果/DeepMind 顶级负责人 | 博士导师 | 已覆盖 F10（笼统） |
| Aaron Courville（Deep Learning 教材共同作者，Mila 教授） | — | Mila 官方 https://mila.quebec/en/directory/aaron-courville 【机构官方页】 | 教材共同作者；Mila 核心教授 | 博士/长期合作者 | **缺口待补**：F10 未列名 |
| Hugo Larochelle（Google Brain 加拿大负责人） | — | Google Brain 官方/权威媒体交叉核对 | 后成 Google Brain Canada 负责人 | 博士导师 | 已覆盖 F10（F10 有列名） |
| Kyunghyun Cho（NYU 教授，seq2seq 关键作者） | — | NYU 官方页/权威媒体 | seq2seq/GRU 联合发明者，NLP 核心研究者 | 指导/合作者（博后/合作） | **缺口待补**：F10 未列名 |
| Mila 1,500+ 研究人员生态 | 1993- | mila.quebec 官方 【机构官方页】 | 将蒙特利尔打造为全球 AI 人才高地；多个 AI 明星公司孵化于 Mila 圈 | 生态主导者 | 已覆盖 F9（笼统） |

## 8. 思想与公共影响（著作/观点报告/政策治理）

| 贡献 | 年份 | 来源URL + 层级 | 影响/规模 | 本人角色 | 与现有facts关系 |
|---|---|---|---|---|---|
| International AI Safety Report（主席，2025/2026版） | 2025-2026 | internationalaisafetyreport.org 【机构官方页】 | 100+ AI 专家共同执笔，30+ 国家和国际组织支持；权威政策参考文件 | 主席（Chair） | 已覆盖 F12（笼统），**待补充版本/规模** |
| 美国参议院 AI 听证证词 | 多次 | 美国参议院记录【官方页】 | 用科学共识支持 AI 监管 | 证人 | 已覆盖 F12（笼统） |
| AI 安全/存在风险公开发声（"生存威胁"论） | 2023- | yoshuabengio.org / 权威媒体 | 与 Hinton 并立，作为深度学习奠基者主张 AI 存在风险，影响政策讨论 | 独立发声者 | 已覆盖 F11,F12（笼统） |
| AI 安全相关博客文章与技术政策写作 | 2023- | yoshuabengio.org/category/ai-safety/ 【本人官方页】 | 持续技术政策写作，影响监管议程 | 独立写作者 | **缺口待补**：未进入 F03 facts |

---

## 对账小结

### 缺口待补（现有 facts 未覆盖、来源够硬）
1. **梯度消失/爆炸研究（1994）** — IEEE TNN，LSTM/ResNet 的理论前驱，应进入 facts
2. **Curriculum Learning（2009）** — ICML，5,000+ 被引，训练方法重要贡献
3. **Greedy Layer-Wise Training（2007）** — NeurIPS，深度学习复兴核心方法
4. **Deep Learning 教材（2016）** — MIT Press，全球标准教材，未进入 facts
5. **Theano 框架** — TF/PyTorch 之前主流框架，蒙特利尔团队主导
6. **Element AI 联合创始（2016）** — $102M 融资，$230M 退出，未进入 facts
7. **h-index 254，总被引 >109 万** — 全球在世科学家总被引第一（2025-10 突破）
8. **神经语言模型（2003）论文名和被引量** — F6 笼统，待补具体信息
9. **注意力机制论文名（arXiv 1409.0473）和被引量** — F7 笼统，待补
10. **seq2seq/编码器解码器架构（2014）** — EMNLP 2014，F7 笼统，待补
11. **GAN 被引量（105,000+）** — F8 笼统，待补
12. **Officer of the Order of Canada / Knight of Légion d'Honneur** — F13 未明确
13. **Aaron Courville、Kyunghyun Cho 学生/合作者关系** — F10 未列全

### 已建议回填到
- `profiles/Yoshua Bengio.md`：补充 Element AI/Theano/教材/梯度消失/Curriculum Learning/总被引突破
- `research/facts/F03_Yoshua_Bengio.md`：新增 F14-F21
- `research/coverage_audit.md`：升级为 `updated`

### coverage_audit 状态拟升为：`updated`
