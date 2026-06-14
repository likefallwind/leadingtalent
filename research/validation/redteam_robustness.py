#!/usr/bin/env python3
"""Red-team robustness check of the v4 (n=70) core conclusion.

Source of truth: ../scores.md scoring table (rows `| # | name | arch | d1..d9 | mig |`).
Run: python3 redteam_robustness.py   (no deps; pure stdlib)

Purpose: attack the headline "70 人 70 种形状零重合" and see what survives.
Findings are written up in redteam_robustness.md (keep numbers in sync).
"""
import re, itertools, statistics, random, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
SCORES = os.path.join(HERE, "..", "scores.md")

def load():
    names, arch, vecs = [], [], []
    row = re.compile(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|" + r"\s*([0-3])\s*\|" * 9)
    for line in open(SCORES, encoding="utf-8"):
        m = row.match(line.strip())
        if not m:
            continue
        names.append(m.group(2)); arch.append(m.group(3))
        vecs.append([int(m.group(4 + d)) for d in range(9)])
    return names, arch, vecs

def man(a, b): return sum(abs(x - y) for x, y in zip(a, b))

def main():
    names, arch, vecs = load()
    N = len(vecs)
    assert N >= 1, "no rows parsed"
    print(f"parsed {N} people from scores.md")
    pairs = list(itertools.combinations(range(N), 2))
    dists = [man(vecs[i], vecs[j]) for i, j in pairs]

    print("\n=== ATTACK 1: is 'all distinct' a strong claim, or knife-edge fragile? ===")
    dup = sum(1 for i, j in pairs if vecs[i] == vecs[j])
    print(f"exact duplicate pairs: {dup}")
    print(f"min Manhattan dist {min(dists)} | median {statistics.median(dists)} | mean {statistics.mean(dists):.2f} | max {max(dists)}")
    for t in (1, 2, 3):
        c = sum(1 for d in dists if d <= t)
        print(f"pairs within Manhattan<= {t}: {c} ({100*c/len(pairs):.1f}%)")

    print("\n=== ATTACK 2 (KILLER): is distinctness just inevitable from 4^9 granularity? ===")
    cols = [[v[d] for v in vecs] for d in range(9)]
    random.seed(0); TR = 20000; alld = 0; mins = []
    for _ in range(TR):
        samp = [tuple(random.choice(cols[d]) for d in range(9)) for _ in range(N)]
        if len(set(samp)) == N: alld += 1
        mins.append(min(man(samp[i], samp[j]) for i, j in pairs))
    print(f"draw {N} vectors from the SAME per-dim marginals: P(all distinct) = {alld/TR:.3f}")
    print(f"=> 'zero repeats' occurs by chance ~{100*alld/TR:.0f}% of the time. The metric is near-vacuous.")
    print(f"random mean min-dist {statistics.mean(mins):.2f} vs observed {min(dists)}")

    print("\n=== ATTACK 3 (what actually survives): one template axis, or many? ===")
    mean = [statistics.mean(c) for c in cols]
    M = [[vecs[i][d]-mean[d] for d in range(9)] for i in range(N)]
    cov = [[sum(M[i][a]*M[i][b] for i in range(N))/(N-1) for b in range(9)] for a in range(9)]
    def mv(A, x): return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]
    def nrm(x): return math.sqrt(sum(v*v for v in x))
    A = [r[:] for r in cov]; ev = []
    for _ in range(5):
        x = [random.random() for _ in range(9)]
        for _ in range(500):
            y = mv(A, x); n = nrm(y); x = [v/n for v in y]
        lam = sum(x[i]*mv(A, x)[i] for i in range(9)); ev.append(lam)
        A = [[A[i][j]-lam*x[i]*x[j] for j in range(9)] for i in range(9)]
    tot = sum(cov[i][i] for i in range(9)); cum = 0
    for i, l in enumerate(ev):
        cum += l; print(f"  PC{i+1}: {100*l/tot:5.1f}% var (cum {100*cum/tot:4.1f}%)")
    avg = statistics.mean(dists)
    print(f"mean pairwise dist {avg:.2f} = {100*avg/27:.0f}% of theoretical max (27). Wide cloud, not a blob.")

    print("\n=== ATTACK 4: are archetypes real sub-clusters or decorative labels? ===")
    from collections import defaultdict
    g = defaultdict(list)
    for i, a in enumerate(arch): g[a].append(i)
    wsum = wn = 0
    for a, idx in sorted(g.items(), key=lambda x: -len(x[1])):
        if len(idx) < 2: continue
        wd = statistics.mean(man(vecs[i], vecs[j]) for i, j in itertools.combinations(idx, 2))
        wsum += wd*len(idx); wn += len(idx)
        print(f"  {a:14s} n={len(idx):2d} within={wd:4.2f} ({wd/avg:.2f}x overall)")
    print(f"weighted within-archetype {wsum/wn:.2f} vs overall {avg:.2f} => {wsum/wn/avg:.2f}x")
    better = 0
    for i in range(N):
        same = [man(vecs[i], vecs[j]) for j in g[arch[i]] if j != i]
        diff = [man(vecs[i], vecs[j]) for j in range(N) if arch[j] != arch[i]]
        if same and diff and min(same) <= min(diff): better += 1
    print(f"nearest-neighbor-or-tie within own archetype: {better}/{N} ({100*better/N:.0f}%)")

if __name__ == "__main__":
    main()
