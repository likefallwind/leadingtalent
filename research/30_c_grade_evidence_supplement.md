# C 级能力补证记录

## 目的

本文件补强 `26_evidence_strength_audit_v1.md` 中 5 条 C 级能力的证据链。

这里的目标不是把这些能力升级为强结论，而是降低“主要依赖媒体叙事”的风险：如果能找到官方资料、一手访谈、技术发布或机构材料支撑事实链，则先从 C 提升到 B；如果能力解释仍然需要推断，则不升到 A。

## 补证结果

| normalized_id | 原缺口 | 新增来源 | 补强后判断 | 新等级 |
|---|---|---|---|---|
| nc029 | Qwen 开源/商业张力主要依赖媒体解释。 | Alibaba Cloud Model Studio 文档说明 Model Studio 集成 Qwen 系列并提供官方 Qwen API 与 OpenAI-compatible API；QwenLM GitHub 官方仓库说明 Qwen 是 Alibaba Cloud 提出的模型并提供开源代码/部署材料。 | “开源模型家族 + 云上商业 API/Model Studio”同时存在，因此可以支撑“在开源与商业云服务之间管理平台张力”的机制判断；但“战略张力”仍是研究解释，不是周靖人一手表述。 | B |
| nc038 | Jiang Daxin 从微软到 StepFun 的迁移缺少官方简历支撑。 | 公开会议/行业资料和 StepFun 资料均显示 Jiang Daxin 为 StepFun 创始人兼 CEO；公开资料同时记录其 Microsoft Research Asia / Microsoft 全球合伙人等经历。 | 微软研究机构经验进入 StepFun 创业路径的事实链已比单一媒体更稳；但仍需要 StepFun 官方人物页或 Jiang Daxin 一手访谈才能升到 A。 | B |
| nc042 | Wang Xiaochuan “中国自己的 OpenAI”创业叙事和资本聚合主要依赖媒体。 | TechCrunch 记录其公开提出“中国需要自己的 OpenAI”的创业叙事；TIME、SCMP、Forbes 等资料记录 Baichuan 融资、估值和投资方。 | 叙事和资本聚合之间有多来源支撑，但仍主要是媒体和公开报道，不足以作为强一手结论。 | B |
| nc048 | StepFun 终端/汽车/Agent 入口缺少官方合作或产品资料。 | BusinessWire/Geely 相关资料记录 Geely Auto 与 StepFun 联合展示，并提到 Agent OS、智能座舱和 Step 3；行业资料记录 Geely、Qianli Technology 与 StepFun 推动“AI+车”合作。 | “基础模型路线连接到 Agent、汽车和智能终端入口”已有合作与产品材料支撑；但人物层面的 Jiang Daxin 个人能力链仍需一手访谈。 | B |
| nc057 | Nick Bostrom 长期未来/宏观战略与 AI 风险边界不够清晰。 | Nick Bostrom 个人主页列出 `Superintelligence: Paths, Dangers, Strategies` 并说明其引发 AI 未来讨论；FHI 资料说明该机构研究文明前景和存在风险；OUP/个人页面明确 Superintelligence 主题。 | 可以把能力限定为“把 AI 风险放入超级智能、存在风险和长期未来框架”，避免泛化成一般长期主义；但宏观战略影响范围仍需更多引用网络证据。 | B |

## 使用来源

| 能力 | 来源 |
|---|---|
| nc029 | https://www.alibabacloud.com/help/doc-detail/2579562.html |
| nc029 | https://github.com/QwenLM/Qwen |
| nc038 | https://www.stepfun.com/ |
| nc038 | https://cips-cl.org/static/CCIR2025_%E4%BC%9A%E8%AE%AE%E6%89%8B%E5%86%8C.pdf |
| nc042 | https://techcrunch.com/2023/07/11/chinas-search-engine-pioneer-unveils-open-source-large-language-model-to-rival-openai/ |
| nc042 | https://time.com/7012775/wang-xiaochuan/ |
| nc042 | https://www.scmp.com/tech/tech-trends/article/3271908/chinese-ai-start-baichuan-raises-us700-million-alibaba-tencent-xiaomi |
| nc048 | https://www.businesswire.com/news/home/20250731651940/fr |
| nc048 | https://stcn.com/article/detail/1539155.html |
| nc057 | https://nickbostrom.com/ |
| nc057 | https://nickbostrom.com/papers/existential-risks/ |
| nc057 | https://www.futureofhumanityinstitute.org/home |
| nc057 | https://www.oup.com.au/books/higher-education/art-and-technology/9780198739838-superintelligence |

## 结论边界

这 5 条能力可以从 C 提升到 B，但不应升到 A。

原因是：新增来源补强了事实链，却没有完全消除解释环节。尤其是 `nc029` 的“战略张力”、`nc042` 的“叙事聚合资本”、`nc048` 的“个人能力链”仍需要一手访谈、官方人物材料或更完整时间线。
