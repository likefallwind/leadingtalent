# Soumith Chintala（苏米特·钦塔拉）

## 基本定位

Soumith Chintala 是 **PyTorch 的共同创建者与长期负责人**，深度学习框架生态的代表性人物 [A]。他在 60 人名单里与陈天奇（F66）一同补"工具·框架·平台型"原型，但形状不同：陈天奇是**学术 + 开源**路径（XGBoost 单篇 8 万引、CMU 教授），Chintala 是**工业工程领袖 → 创业高管**路径——在 Facebook AI Research（FAIR）做了约 11 年、官至 AI 基础设施副总裁，2025 年底转任 Mira Murati 创办的 Thinking Machines Lab 首席技术官 [A]。两人同属"框架建设者"却长出不同雷达形状，正是名单"即便同型也无两人相同"的有力佐证。

## 系统与框架：一个框架定义了一个时代的研究工具

Chintala 2014 年加入 FAIR，2016 年与 Adam Paszke、Sam Gross 等人共同创建 PyTorch，并长期担任团队负责人与社区公开代表 [A]。PyTorch 以"命令式、动态图、优雅 API"的设计哲学迅速成为研究界默认框架：github.com/pytorch/pytorch 约 **101k stars**；到 2023 年，**NeurIPS 等顶会论文中超过 80% 使用 PyTorch**，被估计有 90% 以上的 AI 从业者与企业采用 [A]。它本身已成为深度学习的"软基础设施"。2022 年 PyTorch 移交 Linux Foundation 成立 PyTorch Foundation，确立开放中立治理 [A]。

他的设计理念是"让 AI 研究变得愉悦、让工具变得优雅"，刻意降低研究者的进入门槛——这一开发者文化本身是其影响力的一部分 [A]。他还著有广为流传的《How to Train a GAN?》（ganhacks，约 11.6k stars）与早期的 convnet-benchmarks [A]。

## 学术：GAN 早期的两块奠基石

在 PyTorch 之前，Chintala 已是生成对抗网络（GAN）早期的关键研究者。2015 年他与 Alec Radford、Luke Metz 合作的 **DCGAN**（《Unsupervised Representation Learning with Deep Convolutional GANs》）把 GAN 与卷积网络结合，是生成模型的奠基性架构，Semantic Scholar 约 **14,776 次引用** [A]。2017 年他与 Martin Arjovsky、Léon Bottou 合作的 **Wasserstein GAN（WGAN）** 改善了 GAN 训练稳定性，两个版本合计被引超过 1.3 万次 [A]。这些使他的 D1（原创奠基）并不为零——区别于纯工程型框架作者。

## 公司与组织

在 FAIR/Meta 的 11 年里，他从早期工程（首个 FAIR 计算集群、目标检测、StarCraft AI bot）一路做到 **AI 基础设施副总裁** [A]。2025 年 11 月离开 Meta，加入前 OpenAI CTO Mira Murati 创办的 **Thinking Machines Lab**，2026 年起出任 **CTO**，负责技术战略、研究方向与基础设施扩张 [A]。这让他的 D3（机构/组织）从"大厂技术领袖"延伸到"明星创业公司技术一把手"。

## 在画像中的位置（建议，待 v4 重评）

按 9 维框架，Chintala 的形状预计是：**D2 工程产品化与 D7 教育开源标志级**（PyTorch 事实标准 + 全球最大深度学习开源社区之一），**D1 原创奠基中等偏强**（DCGAN/WGAN 两块奠基石），**D3 机构中等**（Meta VP → Thinking Machines CTO），而 D4 资本（无亲自主导的融资/创办）、D5 硬件、D6 安全、D8 信念逆向、D9 拐点偏低。与陈天奇（F66）对照：同为框架建设者，Chintala 的 D3 更高、D1 略低、D4 同样低——**两个"框架人"形状不重合**。正式分数等下一个统一重评批次（v4）。

## 边界

需诚实区分角色：PyTorch 是 **21 人团队作品**（Paszke/Gross/Lerer 等），Chintala 是共同创建者、长期 lead 与公开代表，不可写成单人发明；DCGAN、WGAN 均为共同作者。他走工业工程路径，**无院士/Fellow 等学术头衔**——与陈天奇一样，其"领军"由 star 数、框架采用率等行为性指标确立。Google Scholar 总引用因 PyTorch 论文而显著高于 scispace 的保守口径（22,681），精确值待核。

## 资料来源

- soumith.ch（S3，个人页）；github.com/soumith 及 pytorch/pytorch（S2，star 数 as-of 2026-06）。
- PyTorch：papers.nips.cc（S1，NeurIPS 2019）；en.wikipedia.org/wiki/PyTorch（S4，采用率/治理）；infoq.com（S4，PyTorch Foundation）。
- DCGAN：arXiv 1511.06434（S2）；scispace（S2，14,776 引/作者总引 22,681/h-29）。WGAN：arXiv 1701.07875（S2，Semantic Scholar 引用）。
- Thinking Machines CTO：startuptalky.com / americanbazaaronline.com（S4，2025-11 加入、2026 任 CTO）。
- 完整逐条与硬度分级见 `research/contributions/F67_Soumith_Chintala.md`。
