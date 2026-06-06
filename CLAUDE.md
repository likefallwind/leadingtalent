# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **Markdown-first research archive** (no package manifest, no build system, no tests in the software sense). The research question: *"What does an AI leadership talent actually look like?"* — answered **bottom-up** from the real biographical data of 60 recognized AI leaders, deliberately **without presupposing** any trait dimensions. Output is `research/report.html` + Markdown analysis layers.

Core finding (see `research/FINDINGS.md`): there is **no single template** — 60 people show 59 distinct 8-dimension radar shapes; the data is multi-peak. Only two "floor" requirements approach universality, and even those are likely artifacts of list-selection bias.

`AGENTS.md` holds the contributor-facing conventions (style, commits, PRs); read it too. This file focuses on the pipeline architecture and the discipline rules that make the evidence chain trustworthy.

## The evidence chain (the central architecture)

Everything is one **downward-drillable chain**. A score must always trace back to raw source text:

```
profiles/*.md                  60 people, one file per person, rich source data (7–16KB each)
   ↓  (contributions/ census is an upstream pre-step that feeds profiles & facts)
research/facts/F##.md          per-person hard FACTs (## FACTS) + atomic CAPs (## CAPS)
   ↓
research/capability_pool.md    ~430 raw CAPs hand-coded into normalized capabilities
   ↓
research/capability_matrix.md  person × capability ledger, each cell carries `from F#`
   ↓
research/scores.md             8-dimension 0–3 scores, folded from the matrix
   ↓
research/profile/portrait.md   8 dims = radar axes; ~7 archetypes by co-occurrence
   ↓
research/validation/validation.md   falsification test against people inside & outside the list
```

Reverse drill (always preserve this): a number in `scores.md` → which normalized capabilities it hit in `capability_matrix.md` → the `from F#` links → `facts/F##.md` → original text in `profiles/`.

### Two reinforcement layers (do NOT let them touch the official scores)
- `research/contributions/F##_<name>.md` — **completeness layer**, upstream of facts. Exhaustively enumerates one person's major contributions across **8 fixed categories** using one uniform source checklist, so every person is mined to comparable depth. Produced by the `contribution-census` skill (`.claude/skills/contribution-census/`). **Collects/backfills facts only.**
- `research/evidence/F##_<name>.md` — **experimental audit** of step 4. Scans normalized-capability IDs per person and labels each `confirmed/partial/insufficient/not_found/contested` with citations. **Exposes boundary problems; does not change scores.**

## Notation & naming conventions (must stay consistent)

- **FACT tags:** `[A]` = hard fact explicitly stated in source; `[B]` = stated but vague/needs caution. Never write inferences beyond the source.
- **CAP evidence links:** every capability line ends with `— from F#,F#` pointing at the facts that support it. This link is mandatory and is what makes claims re-checkable.
- **Person IDs:** `F01`–`F60`. Facts/contributions/evidence files are named `F##_<name>.md`; profile files use the visible display name (`profiles/Andrew Ng.md`, `profiles/张钹.md`). Preserve the existing mixed Chinese/English naming.
- **Counts must agree across files.** Summary numbers in `research/README.md`, `FINDINGS.md`, `capability_pool.md`, `scores.md` should reconcile. (Known open discrepancy: docs say "42" normalized capabilities but visible IDs count 41 — see `research/README.md` notes; don't silently "fix" one side.)

## Discipline rules (the reason this study claims fairness)

1. **Census/evidence layers backfill facts only.** Never rewrite numbers in `research/scores.md` or `research/capability_matrix.md` from these layers.
2. **Re-score in a single pass only after all 60 people reach `audited-v1`/`updated`** in `research/coverage_audit.md`. Auditing people one at a time and re-scoring as you go gives whoever was audited first an unfair edge — this is the exact bias the pipeline exists to remove.
3. **One person per census run; aim for completeness, not patching a diff.**
4. **Bias disclaimers travel with every conclusion** (survivorship / selection / source bias — see end of `research/README.md`). Completeness only narrows the information-gap bias.
5. Step 3 (normalizing capabilities) is **manual thematic coding, not algorithmic clustering** — numbers are analyst judgment with ±2–3 person error.

## Working commands (shell checks, not a build)

```bash
git status --short
rg "from F#" research/facts        # verify CAP evidence links are present
rg "TODO|TBD|待补" profiles research # find unfinished spots
python3 -m http.server 8000 -d research   # then open http://localhost:8000/report.html
```

"Testing" here = content validation: after edits, confirm referenced files exist, `from F#` links still point at real facts, cross-file summary numbers still agree, and `report.html` renders charts/tables/links without broken content.

## Agent etiquette for this repo

Prefer minimal, traceable edits. Do not rewrite profiles, scores, or conclusions wholesale unless asked. When you change an analysis layer, update its downstream summary files **in the same commit** so the evidence chain stays reviewable. Keep claims grounded in `profiles/` and `research/facts/` — no conclusions that aren't in the source data.
