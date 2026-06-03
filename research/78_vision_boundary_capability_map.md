# m29 与工具链/机器人路径边界对照能力映射

本文件基于 `77_vision_boundary_atomic_facts.md` 抽取对照能力。能力编号从 `cap207` 开始，接续当前 206 条原始能力。

| capability_id | 原子能力 | evidence_facts | observed_in | confidence | provisional_cluster |
|---|---|---|---|---|---|
| cap207 | 能把计算机视觉算法组织成开源工具链、benchmark 和工程框架，改变研究共同体的复用方式 | lindh_boundary_f001, lindh_boundary_f002 | Lin Dahua | high | 视觉开源工具链 |
| cap208 | 能把开源平台从视觉算法扩展到更广泛 AI 研发和大模型落地工具体系 | lindh_boundary_f002, lindh_boundary_f003 | Lin Dahua | medium | 开源工具到大模型落地 |
| cap209 | 能在高校实验室和上海 AI 实验室之间组织视觉研究、开源平台和商业化接口 | lindh_boundary_f003, lindh_boundary_f004 | Lin Dahua | medium | 研究工具链与产业接口 |
| cap210 | 能提出足够简单可复用的相机标定方法，使 3D 视觉成为机器人和视觉系统的底层工具 | zhangzy_boundary_f001, zhangzy_boundary_f002, zhangzy_boundary_f003 | 张正友 | high | 底层视觉方法标准化 |
| cap211 | 能把经典视觉方法和长期工业研究经验迁移到 AI Lab 与 Robotics X 机器人组织 | zhangzy_boundary_f001, zhangzy_boundary_f004 | 张正友 | medium | 视觉方法到机器人组织 |
| cap212 | 能把视觉、AI Lab 和 Robotics X 组织成面向具身智能的软硬件研究接口 | zhangzy_boundary_f004 | 张正友 | medium | 机器人研究接口 |

## 对 m29 的边界提示

| 对照机制 | 代表能力 | 与 m29 的关系 |
|---|---|---|
| m03 共同体工作流标准化 | cap207, cap208 | Lin Dahua/OpenMMLab 改变研究者如何复用视觉算法，核心是开源工具链，不是企业行业基础设施。 |
| m28 具身/车载/机器人智能平台 | cap210, cap211, cap212 | 张正友路径进入机器人和具身智能，核心是底层视觉方法到机器人组织，不是视觉 AI 行业解决方案。 |
| m29 企业侧视觉 AI 基础设施 | nc133-nc144 | 朱珑/汤晓鸥/印奇路径偏视觉 AI 公司、城市/医疗/IoT/供应链和行业系统。 |
