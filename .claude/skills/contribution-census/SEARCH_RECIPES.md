# 逐维度检索词配方（Search Recipes）

> 给 `contribution-census` skill 的 Step 2 用。照配方对每个人发**同一组**查询，深度才可比。
> `<name>` 用中文名，`<en>` 用英文名（中文人物务必两种都发）。先发"打底"组拿生平长文，再逐维度补。

## 打底（最高优先，先做）
- `<name> 简介 经历 主要成就`
- `<en> biography research contributions`
- `<name> OR <en> ACM Fellow OR IEEE Fellow OR 院士 公告`  ← 获奖/Fellow 公告最系统枚举贡献
- `<en> Google Scholar`（拿总被引、h-index、代表作列表——逐条过，别只看前几条）
- `<en> homepage` / `<name> 个人主页`

## 1 学术
- `<en> most cited papers` / `<en> representative papers`
- `<en> arXiv` / `<en> DBLP` / `<en> Semantic Scholar`
- `<name> 代表论文 被引 OR 引用量 OR h-index`
- `<en> best paper award OR test of time award`
- 开创概念：`<en> proposed OR introduced OR pioneered <已知方向>`

## 2 系统与框架
- `<en> github` / `<name> 开源 框架 OR 工具`
- 直接抓仓库：`WebFetch https://github.com/<org-or-user>` 看 pinned/全家桶，逐个读 star/fork
- `<框架名> stars` / `<框架名> downloads PyPI`
- `<en> benchmark OR dataset OR toolkit released`

## 3 产品与工程
- `<name> 产品 OR 上线 OR 落地 用户 OR 营收 OR 规模`
- `<en> product OR deployed OR shipped users OR revenue`
- 比赛/系统里程碑：`<en> won KDD Cup OR WMT OR competition`（"研究→冠军→落地"强信号）

## 4 公司与组织
- `<name> 创立 OR 联合创始人 OR 任职 公司 OR 实验室 OR 研究院`
- `<en> founder OR co-founder OR CEO OR director`
- `<公司名> 融资 轮次 估值` / `<company> funding round valuation IPO`
- `<公司名> 员工 OR 团队 规模`

## 5 标准与基础设施
- `<name> 标准 OR 芯片 OR 算力平台`
- `<en> standard OR chip OR accelerator OR infrastructure`
- 确实无 → 在清单里写"（本类无）"并注明查过哪些来源

## 6 学术服务与荣誉
- `<name> Fellow OR 院士 OR 杰出 OR 奖`
- `<en> IEEE Fellow OR ACM Fellow OR AAAI Fellow OR national academy`
- `<en> general chair OR program chair OR area chair`（顶会角色）
- `<en> associate editor OR editorial board`（期刊角色）
- `<name> 著作 OR 专著 OR 教材 销量`

## 7 人才与生态
- `<name> 学生 OR 弟子 OR 培养 谱系`
- `<en> students OR advisees OR lab alumni`
- `<name> 课程 OR 科普 OR 社区 影响`
- 无具体学生名单时标"需更强来源"，别拍脑袋写谱系

## 8 思想与公共影响
- `<name> 著作 OR 观点 OR 演讲 OR 报告`
- `<en> book OR essay OR testimony OR policy OR governance`
- `<name> 接受采访 谈 AI`（交叉，单独不作硬来源）

## 教育与履历（顺手抓，用于深度可比）
- `<name> 本科 OR 硕士 OR 博士 院校 年份`
- `<en> PhD OR education <university>`

## 实测注意
- `WebFetch` 抓不动 JS 渲染官页（`microsoft.com/.../research/people/*` 等）→ 当指针，改抓机构文章/镜像/大学新闻/仓库/arXiv。
- 百度百科常 403 → 用 WebSearch 摘要交叉，别直接抓。
- 影响/规模一律落到**数字**；本人角色一律区分 独立/共同/团队/组织者。
