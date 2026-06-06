# F01 Geoffrey Hinton Evidence Ledger

> 状态：experimental。编码单位为 `capability_pool.md` 的规范能力 ID；`D1-D8` 仅作后续汇总。

## Status Map（更新于 2026-06-06，贡献清单 v1 回填后）

- confirmed: T1, T2, D1.1, D1.4, D1.5, D6.1, D6.2, D7.3, D7.4, D8.1, D8.4
- partial: D2.1, D3.1, D7.5
- insufficient: D6.4
- contested:
- not_found: B1, B2, D1.2, D1.3, D1.6, D2.2, D2.3, D2.4, D3.2, D3.3, D3.4, D3.5, D4.1, D4.2, D4.3, D4.4, D5.1, D5.2, D5.3, D5.4, D5.5, D6.3, D7.1, D7.2, D8.2, D8.3

## Evidence Rows

| 能力ID | 判定 | 支持事实 | 角色强度 | 影响范围 | 限制/反证 | 置信度 |
|---|---|---|---|---|---|---|
| T1 | confirmed | F5,F6,F8,F12 / C4 | 共同主导/奠基者 | 行业级 | 反传、Boltzmann machine、AlexNet 路线分别涉及多位合作者，应保留共同贡献表述 | high |
| T2 | confirmed | F3,F7 / C1 | 长期路线坚持者 | 学术共同体级 | 无 | high |
| D1.1 | confirmed | F5,F6,F8 / C4 | 共同主导 | 行业级 | AlexNet 是学生与其共同完成，反传也非单人发明 | high |
| D1.4 | confirmed | F2,F6 / C2,C10 | 跨学科引入者 | 方法级 | 统计物理工具的直接行业转化需通过后续模型链条理解 | high |
| D1.5 | confirmed | F7,F10,F11 / C6,C7 | 生态与人才土壤建设者 | 区域生态/人才谱系级 | CIFAR/Vector 并非都由其从零创建 | medium |
| D2.1 | partial | F8,F9 / C5 | 转化参与者 | 产业研究级 | 当前 facts 只说明 DNNresearch 被 Google 收购，未证明其主导量产系统 | medium |
| D3.1 | partial | F7,F10 / C6 | 机构关键人物 | 机构/区域生态级 | 能证明参与和影响 CIFAR/Vector，不能严格证明“从零创建并长期领导世界级研究机构” | medium |
| D6.1 | confirmed | F13 / C9 | 公共发声者 | 公共议程级 | facts 未展开具体政策参与或技术治理方案 | medium |
| D6.4 | insufficient | F13 / C9 | 角色转变者 | 思想层 | 公开谈风险不等于“反身性自省”，需补充原话或行动证据 | low |
| D7.4 | confirmed | F11 / C7 | 师父/导师 | 人才谱系级 | 当前 facts 只列代表学生，完整谱系可继续补充 | high |
| D8.1 | confirmed | F3,F4,F7 / C1 | 长期逆向押注者 | 范式级 | 无 | high |
| D8.4 | confirmed | F2,F4,F6,F8,F13 / C10,C9 | 原型迁移者 | 学术到公共议程级 | “迁移”强，但每一阶段的边界可再细化 | high |

## 新增 Evidence Rows（贡献清单 v1 回填）

| 能力ID | 判定 | 支持事实 | 角色强度 | 影响范围 | 限制/反证 | 置信度 |
|---|---|---|---|---|---|---|
| D1.1（补强） | confirmed | F14(Dropout),F15(t-SNE),F16(知识蒸馏),F17(胶囊),F18(FF算法) / C11 | 连续多代贡献，每项被引均在 5,000+ | 行业级 | 各项均为共同作者，非独立完成；胶囊网络尚未成主流 | high |
| D6.2 | confirmed | F12 / Queen Elizabeth Prize, Order of Canada, Princess of Asturias, Dickson Prize | 多个顶级荣誉，跨工程/科学/国家类别 | 国际级 | — | high |
| D7.3 | confirmed | F11(38博士生+知名博后) / C12 | 师承网络宽度极大，直接产出 OpenAI/DeepMind 等核心创始人 | 全球人才链级 | 部分博后关系（LeCun等）需更强来源确认 | high |
| D7.5 | partial | F7,F10,F11 / C6 | 通过 CIFAR/Vector/学生网络建生态，而非直接创建社区平台 | 区域生态级 | 非社区平台/课程运营型 | medium |

## 对现有明账的校正提示

- `capability_matrix.md` 将 D3.1 作为 Hinton D3 得分依据；证据账本建议标为 `partial`，因为当前 facts 支持其机构影响，但不足以证明”从零创建并长期领导”。
- D6.4 不宜仅因 2023 后安全发声而自动命中，需要补充其是否公开反思自身路线或承认边界的证据。
- D1.1 在补充 F14-F17 后可从 confirmed 升至 confirmed（更强）；C11 所指”连续基础件”是 Hinton 有别于其他深度学习三巨头的重要特征，待 60 人齐后重评时可参考。
- D7.3/D7.4 区分：D7.4（直接学生）已 confirmed；D7.3（更广学术影响/社区建设）现升为 confirmed，因 38 PhD 谱系 + 知名博后链条已够硬。
