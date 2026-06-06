# F01 Geoffrey Hinton Evidence Ledger

> 状态：experimental。编码单位为 `capability_pool.md` 的规范能力 ID；`D1-D8` 仅作后续汇总。

## Status Map

- confirmed: T1, T2, D1.1, D1.4, D1.5, D6.1, D7.4, D8.1, D8.4
- partial: D2.1, D3.1
- insufficient: D6.4
- contested:
- not_found: B1, B2, D1.2, D1.3, D1.6, D2.2, D2.3, D2.4, D3.2, D3.3, D3.4, D3.5, D4.1, D4.2, D4.3, D4.4, D5.1, D5.2, D5.3, D5.4, D5.5, D6.2, D6.3, D7.1, D7.2, D7.3, D7.5, D8.2, D8.3

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

## 对现有明账的校正提示

- `capability_matrix.md` 将 D3.1 作为 Hinton D3 得分依据；证据账本建议标为 `partial`，因为当前 facts 支持其机构影响，但不足以证明“从零创建并长期领导”。
- D6.4 不宜仅因 2023 后安全发声而自动命中，需要补充其是否公开反思自身路线或承认边界的证据。
