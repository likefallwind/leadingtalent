# F07 Sam Altman Evidence Ledger

> 状态：experimental。编码单位为 `capability_pool.md` 的规范能力 ID；`D1-D8` 仅作后续汇总。

## Status Map

- confirmed: T1, T2, B2, D2.3, D3.2, D4.1, D4.3, D8.2
- partial: D2.2, D4.4, D6.1, D8.3
- insufficient: D3.5
- contested:
- not_found: B1, D1.1, D1.2, D1.3, D1.4, D1.5, D1.6, D2.1, D2.4, D3.1, D3.3, D3.4, D4.2, D5.1, D5.2, D5.3, D5.4, D5.5, D6.2, D6.3, D6.4, D7.1, D7.2, D7.3, D7.4, D7.5, D8.1, D8.4

## Evidence Rows

| 能力ID | 判定 | 支持事实 | 角色强度 | 影响范围 | 限制/反证 | 置信度 |
|---|---|---|---|---|---|---|
| T1 | confirmed | F5,F6,F7 / C1 | 创始 CEO/整合者 | 全球产品/产业级 | 非核心模型算法设计者 | high |
| T2 | confirmed | F3,F4,F5,F8 / C2,C4 | 连续创业与组织者 | 创业生态/公司级 | 技术研究长期投入不是其主线 | medium |
| B2 | confirmed | F8 / C6 | 危机中重建权力者 | 组织治理级 | 该事实也可能反映治理结构问题，应避免单向美化 | high |
| D2.2 | partial | F6,F7 / C1 | 平台整合者 | 开发者/企业平台级 | facts 没有展开 API、企业版的规模指标 | medium |
| D2.3 | confirmed | F6,F7 / C1,C8 | 产品化主导者 | 全球大众产品级 | ChatGPT 是团队成果，需表述为组织与产品整合 | high |
| D3.2 | confirmed | F5,F8 / C1,C6 | 公司创建/领导者 | 公司级 | OpenAI 最初为多人共同创办 | high |
| D3.5 | insufficient | F4,F5 / C2 | 多组织经历者 | 创业生态到公司级 | YC 到 OpenAI 不能直接等同“跨国公司-大厂-高校系统搭建者” | low |
| D4.1 | confirmed | F5 / C3 | 资本与算力动员者 | 产业资源级 | 当前 facts 未列具体金额，但 Microsoft/Azure 绑定足够明确 | high |
| D4.3 | confirmed | F5 / C3 | 资本结构设计者 | 公司治理/资本结构级 | capped-profit 是多人治理设计，不能归为单人发明 | high |
| D4.4 | partial | F4 / C2 | 创业生态配置者 | 创业生态级 | YC 总裁影响生态，但事实卡未证明其个人投资配置路径 | medium |
| D6.1 | partial | F7 / C5 | 公共议程参与者 | 政策/社会叙事级 | facts 只写“多次谈风险与治理”，未展开具体治理贡献 | medium |
| D8.2 | confirmed | F6 / C8 | 产品化窗口捕捉者 | 全球产业拐点级 | ChatGPT 触发拐点是组织成果，不是单人预判 | high |
| D8.3 | partial | F7 / C5 | 叙事组织者 | 公共议程级 | “AGI/生产力/UBI”叙事不等同长期科研攻坚问题 | low |

## 对现有明账的校正提示

- Altman 可能应在 `D2.2` 有 `partial` 命中，因为 API/企业版/开发者平台是其产品化影响的一部分；但当前 facts 需要补规模与平台使用证据。
- `D4.4` 可作为候选补充项，但需要区分 YC 总裁的创业生态组织与“用投资配置影响生态”。
