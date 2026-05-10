# AI 名人公开痕迹抓取脚本

研究方案 V0.1 中 **轨 B（名人反推轨）** 的数据采集模块。  
目标：对 100-200 位 AI 领军人物，从公开渠道抓取学术、代码、传记、个人主页等痕迹，输出为统一格式的 Markdown，作为 LLM 双抽取（Round 1）的输入。

---

## 目录结构

```
scrape/
├── README.md                  ← 本文件
├── requirements.txt           ← Python 依赖
├── config.yaml                ← 配置（API key、限速、抓取上限）
├── scrape.py                  ← 主入口（抓取）
├── aggregate.py               ← 聚合脚本（多源 JSON → 单份 profile.md）
├── scrapers/
│   ├── base.py                ← HTTP 客户端、缓存、限速、重试
│   ├── semantic_scholar.py    ← 学术论文（h-index、引用、abstract）
│   ├── arxiv.py               ← arXiv 预印本
│   ├── github.py              ← GitHub 用户、仓库、README
│   ├── wikipedia.py           ← 维基百科传记
│   └── personal_site.py       ← 个人主页（HTML → 纯文本）
└── data/
    ├── names_seed.csv         ← 种子名单（30 人 starter，扩展到 100-200）
    ├── traces/                ← 输出目录（抓取后自动生成）
    │   └── P001/
    │       ├── meta.json
    │       ├── semantic_scholar.json
    │       ├── arxiv.json
    │       ├── github.json
    │       ├── wikipedia.json
    │       ├── personal_site.json
    │       └── profile.md     ← 聚合后的 LLM 输入
    ├── cache/                 ← HTTP 响应缓存（按 URL hash）
    └── logs/                  ← 运行日志
```

---

## 快速开始

### 1. 安装依赖

```bash
cd scrape
pip install -r requirements.txt
```

### 2. 申请 API key（强烈推荐）

不申请也能跑，但速率会极慢：

| 服务 | 申请地址 | 用途 |
|---|---|---|
| Semantic Scholar | https://www.semanticscholar.org/product/api | 学术论文（无 key 限速 100req/5min） |
| GitHub | https://github.com/settings/tokens | 代码仓库（无 token 限速 60req/h） |

**两种方式提供 key**：
- 改 `config.yaml` 里的 `api_keys` 字段
- 或设环境变量：`export SS_API_KEY=...` / `export GITHUB_TOKEN=...`（会覆盖配置文件）

### 3. 测试跑通（先抓 3 个人）

```bash
python scrape.py --limit 3
```

观察 `data/traces/P001/`、`P002/`、`P003/` 目录下生成的 JSON。如果都 `"status": "ok"`，表示流程正常。

### 4. 全量抓取

```bash
python scrape.py
```

预估耗时（30 人）：~10-20 分钟（受 arXiv 3 秒/请求限制）。  
扩展到 100-200 人后约 30-60 分钟。

### 5. 聚合为 Markdown

```bash
python aggregate.py
```

每人生成一份 `profile.md`，作为 Round 1 LLM 抽取的输入。

---

## 名单扩展（核心工作）

`data/names_seed.csv` 当前只有 30 人 starter，按方案设计需扩到 100-200 人。  
**这一步是人工工作**，自动化做不了——需要研究方各位老师按覆盖原则提名。

### CSV 字段说明

| 字段 | 必填 | 说明 |
|---|---|---|
| `id` | ✓ | 唯一编号 P001-P999 |
| `chinese_name` | | 中文名（中文展示用） |
| `english_name` | ✓ | 英文名（搜索 Semantic Scholar / Wikipedia 必需） |
| `category` | ✓ | 覆盖类别（学术认证/工业领军/创业领军/中国本土/AI安全治理/跨界教育/失败对照） |
| `affiliation` | | 主要任职 |
| `wikipedia_title` | | Wiki 页面标题（不填则用 english_name 搜索） |
| `semantic_scholar_id` | | SS 作者 ID（不填则按名搜索，可能 disambiguation 不准） |
| `arxiv_query` | | arXiv 作者查询字符串（不填则用英文名） |
| `github_username` | | GitHub 用户名（不填则跳过 GitHub） |
| `personal_url` | | 个人主页 URL（不填则跳过个人主页） |
| `notes` | | 备注 |

### 怎么找 ID（提高准确率）

- **Semantic Scholar ID**：搜索 https://www.semanticscholar.org，进作者页，URL 末段就是 ID
- **GitHub username**：直接看 URL `github.com/{username}`
- **Wikipedia title**：浏览器地址栏 `wikipedia.org/wiki/{title}`，下划线连接

不填这些 ID 也能跑（脚本会自动按名搜索），但对**重名严重的中国人名**强烈建议手填，避免抓错人。

### 覆盖原则提醒

按方案要求：
- 学术认证 20-30
- 工业领军 15-25
- 创业领军 20-30（中美）
- 中国本土 25-35
- AI 安全/治理 10-15
- 跨界/教育 10-15
- **失败/平庸对照 15-25**（关键，不能省）
- 强制性别/地域比例底线

---

## 命令参考

```bash
# 全量抓取
python scrape.py

# 只抓指定 ID
python scrape.py --only P001,P020,P021

# 只抓前 5 个（调试用）
python scrape.py --limit 5

# 强制重抓（忽略缓存与已存在文件）
python scrape.py --force

# 聚合所有人为 markdown
python aggregate.py
```

---

## 已知限制

| 问题 | 现状 | 说明 |
|---|---|---|
| 重名 disambiguation | 启发式（取 paper count 最高） | 中国人名重名严重时建议手填 SS ID |
| Twitter / X | 不支持 | API 收费 + 反爬严，规模化不可行；如需后续用 Nitter / 手工搜集 |
| YouTube talks | 不支持 | 后续可加，需用 yt-dlp + whisper 转写 |
| 知乎 / 微博 | 不支持 | 反爬严，建议手工补充关键访谈到个人主页字段 |
| 百度百科 | 不支持 | 中文人物建议优先用中文 Wikipedia（`lang="zh"` 改 `wikipedia.py`） |
| 个人主页深度 | 只抓单页 | 不递归追链接，避免无界爬取 |

---

## 法律与伦理

- 仅抓取**公开**数据，遵守各源 robots.txt 与速率限制
- 仅用于学院内部研究目的
- 抓取结果不对外二次发布
- 如某人物明确表示反对被纳入研究，应从 CSV 移除

---

## 与下一阶段的衔接

聚合后的 `profile.md` 是 **Round 1 双抽取** 的输入：

```
profile.md → LLM (开放式 prompt) → E_open
profile.md → LLM (V0 结构化 prompt) → E_seeded
```

抽取模块见 [`../extract/`](../extract/README.md)。
