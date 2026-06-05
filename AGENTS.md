# Repository Guidelines

## Project Structure & Module Organization

This repository is a Markdown-first research archive for AI leadership talent profiles. Source profiles live in `profiles/*.md`; keep one person per file and preserve the existing mixed Chinese/English naming pattern. The research pipeline lives under `research/`: `facts/F01-F60.md` contains per-person facts and derived capabilities, `capability_pool.md` and `capability_matrix.md` hold normalized capability analysis, `scores.md` stores 8-dimension scoring, and `profile/portrait.md` plus `validation/validation.md` contain synthesis and validation. `research/FINDINGS.md` is the short entry point, while `research/report.html` is the static interactive report.

## Build, Test, and Development Commands

There is no package manifest or build system. Use shell checks before committing:

```bash
git status --short
rg "from F#" research/facts
rg "TODO|TBD|待补" profiles research
python3 -m http.server 8000 -d research
```

Use the local HTTP server to inspect `research/report.html` at `http://localhost:8000/report.html`. Keep generated or manually edited report content consistent with the Markdown sources.

## Coding Style & Naming Conventions

Write research documents in concise Markdown with stable headings and evidence-first claims. Keep FACT/CAP notation consistent: facts use numbered `F#` references and capability lines should retain `from F#` evidence links. For new person files, use the visible display name as the filename, for example `profiles/Andrew Ng.md` or `profiles/张钹.md`. Avoid introducing conclusions that are not grounded in `profiles/` or `research/facts/`.

## Testing Guidelines

Testing is content validation. After edits, verify referenced files exist, capability references still point to facts, and summary numbers in `research/README.md`, `FINDINGS.md`, `capability_pool.md`, and `scores.md` agree. For HTML changes, open the report locally and check that charts, tables, and links render without console-visible broken content.

## Commit & Pull Request Guidelines

Recent commits use short subject lines in Chinese or English, for example `一阶段结论` and `Refine scoring criteria and validation framework in research documentation`. Keep commits focused on one research step or report update. Pull requests should describe the changed research layer, list affected files, explain any scoring or capability-count changes, and include screenshots when `research/report.html` changes.

## Agent-Specific Instructions

Prefer minimal, traceable edits. Do not rewrite profiles, scores, or conclusions wholesale unless requested. When changing analysis, update the downstream summary files in the same commit so the evidence chain remains reviewable.
