#!/usr/bin/env bash
# 证据链自检（T1④，见 research/METHOD_IMPROVEMENTS.md）
# 内容校验，非软件测试：核对计数自洽 + from F# 链不断裂。
# 用法：bash research/check_chain.sh   （从仓库根目录运行）
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
R="$ROOT/research"
fail=0
note() { printf '%-44s %s\n' "$1" "$2"; }

# 1) 人数自洽：profiles = facts 文件 = scores 评分行 = 60
p=$(ls "$ROOT"/profiles/*.md 2>/dev/null | wc -l | tr -d ' ')
f=$(ls "$R"/facts/F*.md 2>/dev/null | wc -l | tr -d ' ')
s=$(grep -cE '^\| [0-9]{2} \|' "$R/scores.md")
note "profiles 数" "$p";  note "facts F## 文件数" "$f";  note "scores 评分行数" "$s"
if [ "$p" = 60 ] && [ "$f" = 60 ] && [ "$s" = 60 ]; then
  note "→ 人数自洽 (期望 60/60/60)" "OK"
else
  note "→ 人数自洽 (期望 60/60/60)" "FAIL"; fail=1
fi

# 2) from F# 链：每个 facts 文件都应含至少一条 from F 证据链
miss=0
for x in "$R"/facts/F*.md; do grep -q "from F" "$x" || { echo "  MISS from-F: ${x##*/}"; miss=1; }; done
[ "$miss" = 0 ] && note "→ facts 全部含 from F# 链" "OK" || { note "→ facts 全部含 from F# 链" "FAIL"; fail=1; }

# 3) 计数提示（不强校验，仅回显，便于跨文件对账：README/FINDINGS 写 569 facts / 498 CAP / 41 规范能力）
caps=$(grep -rhoE '— from F' "$R"/facts | wc -l | tr -d ' ')
note "facts 中 CAP(— from F) 行数" "$caps  (供与 498 对账，人工核)"

echo "----"
[ "$fail" = 0 ] && echo "RESULT: PASS（结构自检通过；语义/分数对账仍需人工）" || echo "RESULT: FAIL（见上）"
exit $fail
