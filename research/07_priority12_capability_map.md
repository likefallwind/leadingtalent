# 优先样本原子能力映射

本文件把 `06_priority12_atomic_facts.md` 中的原子事实映射为原子能力。能力命名仍是临时的，后续应随着更多人物加入而合并、拆分或改名。

| capability_id | 原子能力 | evidence_facts | observed_in | confidence | provisional_cluster |
|---|---|---|---|---|---|
| cap001 | 能在长期非共识或低热度阶段持续推进一个技术路线，直到算力、数据和工程条件成熟 | hinton_f001, hinton_f002 | Geoffrey Hinton | medium | 长期技术信念 |
| cap002 | 能把多个基础方法积累成后续技术范式的工具箱，而不是只依赖单一论文 | hinton_f001 | Geoffrey Hinton | medium | 方法体系积累 |
| cap003 | 能在公司内部推动底层机器学习基础设施，使研究能力变成组织级生产力 | dean_f001, dean_f002 | Jeff Dean | high | 大规模工程系统 |
| cap004 | 能围绕系统、框架、芯片和模型形成跨层协同，而不是只优化单点算法 | dean_f002 | Jeff Dean | medium | 系统级协同 |
| cap005 | 能通过数据集或评测基准改变整个领域的训练目标和竞争标准 | feifei_f001 | Fei-Fei Li | high | 基准塑造 |
| cap006 | 能把学术研究、公共议题和机构建设结合，扩大技术路线的社会影响范围 | feifei_f002 | Fei-Fei Li | medium | 研究公共化 |
| cap007 | 能把前沿技术组织成面向公众和企业的产品入口，并持续管理组织扩张 | altman_f001, altman_f002, altman_f003 | Sam Altman | medium | 产品化与组织扩张 |
| cap008 | 能在高压治理危机后重建组织控制和外部信任关系 | altman_f002, altman_f003 | Sam Altman | medium | 组织韧性 |
| cap009 | 能把多个顶级研究团队整合为统一实验室，并围绕长期目标组织资源 | hassabis_f001, hassabis_f002 | Demis Hassabis | high | 实验室组织 |
| cap010 | 能选择高难科学问题作为 AI 系统能力验证场景 | hassabis_f001 | Demis Hassabis | medium | 科学问题选择 |
| cap011 | 能将量化交易中的算法、数据和算力经验迁移到大模型研发 | liang_f001, liang_f002 | Liang Wenfeng | low | 跨领域迁移 |
| cap012 | 能通过效率路线和模型开放性改变外部对本土大模型能力的判断 | liang_f001, liang_f002 | Liang Wenfeng | low | 效率突破 |
| cap013 | 能把高校知识图谱和大模型研究连接到创业公司与产品体系 | tang_f001, tang_f002 | Tang Jie | medium | 学术到产业转译 |
| cap014 | 能长期维护一个研究方向的工具、数据和学术共同体，使其成为后续创业/产品的知识底座 | tang_f002 | Tang Jie | medium | 研究共同体 |
| cap015 | 能将跨国研究机构经验迁移到国家级学院和 AI for Science 组织体系 | liu_f001, liu_f002 | Liu Tieyan | medium | 跨组织迁移 |
| cap016 | 能在研究管理、人才培养和科学智能之间建立组织接口 | liu_f001, liu_f002 | Liu Tieyan | medium | 研究组织治理 |
| cap017 | 能把早期大模型关键技术积累转化为创业公司的产品路线 | yang_f001, yang_f002 | Yang Zhilin | low | 技术创业转化 |
| cap018 | 能围绕长上下文和高交互产品形成差异化模型应用入口 | yang_f001, yang_f002 | Yang Zhilin | low | 产品路线选择 |
| cap019 | 能把 GLM 系列模型组织成企业级产品和服务体系 | zhangpeng_f001, zhangpeng_f002 | Zhang Peng | low | 大模型商业化 |
| cap020 | 能在强学术背景团队中承担商业化和组织运营角色 | zhangpeng_f001, zhangpeng_f002 | Zhang Peng | low | 组织运营 |
| cap021 | 能通过开源框架和工具链扩大领域实践者网络 | lindahua_f001, lindahua_f002 | Lin Dahua | medium | 开源生态 |
| cap022 | 能把高校/实验室视觉研究转化为可复用的工程框架和社区标准 | lindahua_f001, lindahua_f002 | Lin Dahua | medium | 工具链标准化 |
| cap023 | 能在大型互联网公司内持续推动模型、平台和产业应用的一体化演进 | wanghaifeng_f001, wanghaifeng_f003 | Wang Haifeng | high | 产业平台化 |
| cap024 | 能把深度学习框架、大模型和行业应用组织成开发者/企业生态 | wanghaifeng_f002, wanghaifeng_f003 | Wang Haifeng | high | 平台生态 |

## 当前临时能力簇

以下只是从 24 条能力中临时浮现出来的簇，不是最终维度：

| provisional_cluster | 关联能力 |
|---|---|
| 长期技术信念 | cap001, cap002 |
| 大规模工程系统 | cap003, cap004 |
| 基准塑造 | cap005 |
| 产品化与组织扩张 | cap007, cap008, cap019, cap020 |
| 实验室组织 | cap009, cap010, cap015, cap016 |
| 学术到产业转译 | cap013, cap014, cap017, cap018 |
| 开源/平台生态 | cap021, cap022, cap023, cap024 |
| 效率突破与跨领域迁移 | cap011, cap012 |

## 当前最值得继续验证的假设

| hypothesis_id | 假设 | 当前证据强度 | 下一步验证 |
|---|---|---|---|
| h001 | AI 领军人才通常不是只在“算法创新”上领先，而是在方法、组织、资源和传播中至少掌握一个可放大杠杆 | medium | 扩展到 61 人，看是否仍成立 |
| h002 | 数据集、框架、开源工具和平台生态可能与论文同等重要，甚至在某些路径上更关键 | medium | 加入 Andrew Ng、Karpathy、OpenMMLab、PaddlePaddle、TensorFlow 样本 |
| h003 | 中国大模型创业者的共同点可能不是“本土身份”，而是强技术团队、清华/微软/互联网大厂网络、产品窗口和资源组织 | low | 对杨植麟、张鹏、梁文锋、闫俊杰、姜大昕、王小川做横向比较 |
| h004 | AI for Science 可能是一条独立路径，需要同时具备科学问题选择、模型工程和跨学科组织能力 | low | 加入 Demis Hassabis、张林峰、鄂维南、刘铁岩的详细事实链 |
