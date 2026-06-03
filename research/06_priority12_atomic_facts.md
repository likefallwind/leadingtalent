# 优先 12 人原子事实草稿

本文件从 `05_source_seeds_priority12.md` 的来源入口中拆出原子事实。事实只服务于后续能力抽取，不直接等同于结论。

| fact_id | person | 原子事实 | source_level | confidence |
|---|---|---|---|---|
| hinton_f001 | Geoffrey Hinton | Hinton 的个人主页列出其研究贡献包括反向传播、Boltzmann machines、distributed representations、mixtures of experts、deep belief nets 等。 | A | high |
| hinton_f002 | Geoffrey Hinton | Hinton 2013-2023 年间在 Google 兼职工作，并成为 Vice President and Engineering Fellow。 | A | high |
| hinton_f003 | Geoffrey Hinton | Nobel Prize 官方页面显示 Hinton 因 2024 年诺贝尔物理学奖获奖，获奖时机构为 University of Toronto。 | A | high |
| dean_f001 | Jeff Dean | Google 官方博客在 2023 年 Google Brain 与 DeepMind 合并时称 Jeff Dean 将担任 Google Chief Scientist，并服务 Google Research 与 Google DeepMind。 | A | high |
| dean_f002 | Jeff Dean | Google Research 个人页面列出 Jeff Dean 参与或推动的系统与模型包括 DistBelief、TensorFlow、Pathways、TPUs、BERT、PaLM 等。 | A | high |
| feifei_f001 | Fei-Fei Li | Stanford HAI 介绍称 Fei-Fei Li 是 ImageNet 和 ImageNet Challenge 的发明者。 | A | high |
| feifei_f002 | Fei-Fei Li | Stanford 官方页面将 Fei-Fei Li 与 Stanford HAI、Stanford Vision and Learning Lab 等机构关联。 | A | high |
| altman_f001 | Sam Altman | OpenAI 官方参议院证词页面将 Sam Altman 表述为 OpenAI Chief Executive Officer。 | A | high |
| altman_f002 | Sam Altman | OpenAI 官方博客记录 Sam Altman 在 2023 年治理危机后回归 CEO，并形成新的初始董事会。 | A | high |
| altman_f003 | Sam Altman | OpenAI 2024 年官方审查结果称 Altman 将作为 CEO 重新加入 OpenAI 董事会。 | A | high |
| hassabis_f001 | Demis Hassabis | Google DeepMind 官方介绍称 Google DeepMind 由 CEO Demis Hassabis 领导。 | A | high |
| hassabis_f002 | Demis Hassabis | Google DeepMind 官方介绍将 Google Brain 与 DeepMind 描述为合并后的单一 AI 团队。 | A | high |
| liang_f001 | Liang Wenfeng | TechCrunch 资料将 Liang Wenfeng 识别为 DeepSeek 创始人，并强调其量化投资背景。 | B | medium |
| liang_f002 | Liang Wenfeng | AP 报道称 Liang Wenfeng 先建立量化基金 High-Flyer，再将机器学习能力延伸到 DeepSeek。 | B | medium |
| tang_f001 | Tang Jie | 清华相关公开材料将 Tang Jie 表述为清华大学教授和 Zhipu AI 首席科学家。 | A/B | high |
| tang_f002 | Tang Jie | Tang Jie 个人主页和公开履历显示其长期研究 social networks、data mining、machine learning、knowledge graphs 等方向。 | A | high |
| liu_f001 | Liu Tieyan | 北京中关村学院官方介绍称 Liu Tieyan 为 Zhongguancun Academy 院长。 | A | high |
| liu_f002 | Liu Tieyan | 北京中关村学院官方介绍列出其曾任 Microsoft Research Asia 相关管理职位和 Microsoft Research AI for Science 科学家经历。 | A | high |
| yang_f001 | Yang Zhilin | Moonshot AI 官方页面称公司由早期核心技术团队建立，团队包含 Transformer-XL、RoPE、Group Normalization、ShuffleNet 等关键技术发明者。 | A | medium |
| yang_f002 | Yang Zhilin | 高可信媒体资料将 Yang Zhilin 识别为 Moonshot AI 创始人兼 CEO。 | B | medium |
| zhangpeng_f001 | Zhang Peng | Zhipu/Z.ai 相关资料将 Zhang Peng 识别为 Zhipu/Z.ai CEO。 | C | medium |
| zhangpeng_f002 | Zhang Peng | Zhipu/Z.ai 官方产品入口显示公司以 GLM 系列和大模型产品为核心路线。 | A | medium |
| lindahua_f001 | Lin Dahua | OpenMMLab GitHub 组织是可追踪其开源视觉生态影响的重要入口。 | A | medium |
| lindahua_f002 | Lin Dahua | 上海 AI Lab 相关团队页面显示 Dahua Lin 与中心级研究组织和开源系统生态有关联。 | A/B | medium |
| wanghaifeng_f001 | Wang Haifeng | Baidu IR 官方管理层页面称 Wang Haifeng 自 2019 年 5 月起担任 Baidu CTO。 | A | high |
| wanghaifeng_f002 | Wang Haifeng | Baidu IR 官方管理层页面称 Wang Haifeng 是 National Engineering Research Center of Deep Learning Technology and Application 主任。 | A | high |
| wanghaifeng_f003 | Wang Haifeng | Baidu Research 文章将 ERNIE Bot 与 PaddlePaddle、ERNIE 大模型技术体系的联合优化相关联，并引用 Baidu CTO Wang Haifeng 的说明。 | A | high |

## 事实抽取注意事项

| 注意事项 | 处理方式 |
|---|---|
| Zhang Peng 的 CEO 信息当前仍需官方强来源 | 暂时用 C 级资料标记，不把其作为强结论 |
| Liang Wenfeng 的官方履历资料较少 | 用 B 级报道做线索，后续优先补 DeepSeek/High-Flyer 一手材料 |
| Lin Dahua 的个人角色需要补强 | 先记录 OpenMMLab 和上海 AI Lab 入口，不急于抽强能力 |
| Yang Zhilin 的个人官方资料入口不足 | 先用 Moonshot 团队技术线索和媒体创始人信息组合，后续补论文与采访 |
