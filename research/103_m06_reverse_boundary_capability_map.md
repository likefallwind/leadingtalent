# 原始能力映射：m06 反向边界审计批次

本文件从 `m06rev_f001-m06rev_f019` 中抽取原始能力。这里的能力用于反向审计，不等同于把所有相邻路径并入 m06。

## 原始能力

| raw_capability_id | 人物 | 原始能力 | 关联事实 | 初始证据等级 | 机制线索 |
|---|---|---|---|---|---|
| cap234 | Jeff Dean | 能把大规模分布式系统、训练系统、框架、芯片和模型组织成公司内部 AI 研究与产品基础设施。 | m06rev_f001, m06rev_f002, m06rev_f003 | A | m05 |
| cap235 | Jeff Dean | 能把内部机器学习基础设施的一部分开放成全球开发者可复用框架和云 TPU 资源。 | m06rev_f004, m06rev_f005 | A | m05 / m03 / m06 |
| cap236 | Jeff Dean | 能让 AI 系统基础设施在搜索、广告、YouTube、Gmail、Workspace、Cloud、Pixel、Waymo 等多产品中持续复用。 | m06rev_f002, m06rev_f003, m06rev_f005 | A | m05 |
| cap237 | 陈天石 | 能把 AI 芯片定位为人工智能计算平台的核心承载者，围绕计算力释放组织技术路线。 | m06rev_f006, m06rev_f007 | A | watch-ai-chip-substrate / m21 |
| cap238 | 陈天石 | 能把云端 AI 芯片、板卡、基础软件平台和主流框架支持组织成客户可部署的算力硬件产品。 | m06rev_f008, m06rev_f009 | A | watch-ai-chip-substrate |
| cap239 | 陈天石 | 能把云边端车协同的全算力产品布局用于智能汽车和行业智能化升级。 | m06rev_f007, m06rev_f010 | A | watch-ai-chip-substrate / m28 |
| cap240 | Zhang Yiming | 能把移动互联网机会转化为 Toutiao、Douyin、TikTok 等内容产品组合，并形成全球扩张路径。 | m06rev_f011, m06rev_f012 | A | m11 |
| cap241 | Zhang Yiming | 能把个性化内容发现和短视频产品组织成多产品内容平台，而不是单一媒体产品。 | m06rev_f012, m06rev_f013 | A | m11 / watch-application-translation |
| cap242 | Zhang Yiming | 能把 ByteDance 的技术能力延伸为 BytePlus 等智能平台服务，但其核心仍来自内容产品和应用平台。 | m06rev_f014 | B | m11 / m06 边界 |
| cap243 | 高文 | 能把视频编码标准、人工智能应用、多媒体技术和国家实验室领导角色连接成国家级技术基础设施。 | m06rev_f015, m06rev_f016 | A | m19 / m21 |
| cap244 | 高文 | 能组织鹏城云脑、云态智能计算软件体系和开源软件栈，形成公共智能算力基础设施。 | m06rev_f017, m06rev_f018 | A | m19 |
| cap245 | 高文 | 能把智能算力互联体系和中国算力网研究计划组织成面向国家战略的公共基础设施。 | m06rev_f018, m06rev_f019 | A | m19 / m21 |

## 初步边界观察

| 反向样本 | 边界判断 |
|---|---|
| Jeff Dean | 主要是 m05 企业内部基础设施；TensorFlow/Cloud TPU 触及 m06，但不应把整个 Jeff Dean 路径都归入 m06。 |
| 陈天石 | 核心是 AI 芯片和算力硬件底座，不是模型家族、API 或云服务平台。可作为 m06 的硬件前置条件，但不是 m06 本身。 |
| Zhang Yiming | 核心是推荐算法驱动的内容产品和全球应用平台，不是云 AI 与模型家族平台。BytePlus 是边界项，但不足以改写主归属。 |
| 高文 | 核心是国家/公共智能算力基础设施、标准和国家实验室，不是企业云模型平台。 |

