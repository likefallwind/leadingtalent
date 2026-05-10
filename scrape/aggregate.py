"""把每人的多源 JSON 聚合成一份 Markdown，作为 LLM 抽取的输入。

输出位于 traces/{id}/profile.md，与多个 JSON 并存。
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def render_person(person_dir: Path) -> str:
    meta = load_json(person_dir / "meta.json")
    ss = load_json(person_dir / "semantic_scholar.json")
    ax = load_json(person_dir / "arxiv.json")
    gh = load_json(person_dir / "github.json")
    wk = load_json(person_dir / "wikipedia.json")
    ps = load_json(person_dir / "personal_site.json")

    lines: list[str] = []
    name_zh = meta.get("chinese_name") or ""
    name_en = meta.get("english_name") or ""
    lines.append(f"# {name_zh} / {name_en}")
    lines.append("")
    lines.append(f"- **ID**: {meta.get('id')}")
    lines.append(f"- **类别**: {meta.get('category')}")
    lines.append(f"- **任职**: {meta.get('affiliation')}")
    if meta.get("notes"):
        lines.append(f"- **备注**: {meta['notes']}")
    lines.append("")

    # Wikipedia
    if wk and wk.get("status") == "ok":
        lines.append("## Wikipedia 摘要")
        lines.append(f"*Source: {wk.get('url','')}*")
        lines.append("")
        lines.append(wk.get("extract", ""))
        lines.append("")

    # Semantic Scholar
    if ss and ss.get("status") == "ok":
        lines.append("## 学术产出 (Semantic Scholar)")
        lines.append(f"- h-index: **{ss.get('h_index')}**")
        lines.append(f"- 总引用: **{ss.get('total_citations')}**")
        lines.append(f"- 论文总数: {ss.get('paper_count')}")
        if ss.get("affiliations"):
            lines.append(f"- 机构: {', '.join(a.get('name','') for a in ss['affiliations'] if isinstance(a, dict))}")
        lines.append("")
        lines.append("### 代表论文 (按引用排序)")
        for p in ss.get("top_papers", [])[:20]:
            line = f"- **{p.get('title')}** ({p.get('year')}, {p.get('citations')} cites"
            if p.get("venue"):
                line += f", {p['venue']}"
            line += ")"
            lines.append(line)
            if p.get("abstract"):
                lines.append(f"  > {p['abstract']}")
        lines.append("")

    # arXiv
    if ax and ax.get("status") == "ok" and ax.get("papers"):
        lines.append(f"## 近期 arXiv 预印本 ({ax.get('count')} 篇)")
        for p in ax["papers"][:15]:
            cat = p.get("primary_category") or ""
            lines.append(f"- *{p.get('published','')[:10]}* [{cat}] **{p.get('title')}**")
            if p.get("summary"):
                lines.append(f"  > {p['summary']}")
        lines.append("")

    # GitHub
    if gh and gh.get("status") == "ok":
        lines.append("## GitHub 公开活动")
        lines.append(f"- 用户名: `{gh.get('username')}`")
        lines.append(f"- Followers: {gh.get('followers')}")
        lines.append(f"- 公开仓库: {gh.get('public_repos')}")
        if gh.get("bio"):
            lines.append(f"- Bio: {gh['bio']}")
        if gh.get("blog"):
            lines.append(f"- Blog: {gh['blog']}")
        lines.append("")
        lines.append("### 主要项目 (按 star 排序)")
        for r in gh.get("top_repos", [])[:15]:
            lines.append(
                f"- **[{r.get('name')}]({r.get('url')})** ★{r.get('stars')} "
                f"({r.get('language') or 'n/a'}) — {r.get('description') or ''}"
            )
            if r.get("readme_excerpt"):
                excerpt = r["readme_excerpt"][:600].replace("\n", " ")
                lines.append(f"  > {excerpt}…")
        lines.append("")

    # Personal site
    if ps and ps.get("status") == "ok":
        lines.append("## 个人主页摘要")
        lines.append(f"*Source: {ps.get('url')}*")
        lines.append("")
        lines.append(ps.get("content", "")[:4000])
        lines.append("")

    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="config.yaml")
    args = ap.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    out_dir = Path(cfg["paths"]["output_dir"])

    count = 0
    for person_dir in sorted(out_dir.iterdir()):
        if not person_dir.is_dir():
            continue
        md = render_person(person_dir)
        (person_dir / "profile.md").write_text(md, encoding="utf-8")
        count += 1
        print(f"  ✓ {person_dir.name}")

    print(f"\n生成 {count} 份 profile.md")


if __name__ == "__main__":
    main()
