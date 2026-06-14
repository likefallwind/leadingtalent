#!/usr/bin/env python3
"""Red-team round 2: do the headline conclusions survive scoring NOISE?

Attacks the logged soft-spot "±1 切分误差未做敏感性传播" — the 0-3 cutpoints are
analyst conventions with admitted ±1 error. If a conclusion flips under ±1 jitter,
it is an artifact of the cutpoints, not a real signal.

Two tests (pure computation, unaffected by analyst confirmation bias):
  A. ±1 per-cell perturbation Monte Carlo (clamped 0..3) at several noise rates p.
  B. Bootstrap / subsample stability (drop 20% of people, recompute).

Tracks the conclusions that matter:
  - PC1 variance share  (must stay <<70% => no single 'leadership' axis)
  - archetype within/overall distance ratio (<1 => archetypes are real clusters)
  - D1==3 fraction (must stay ~half => no universal flagship strength)
  - D3>=1 fraction (the only near-universal floor)
  - # exact duplicate shape pairs (the 'zero overlap' claim)

Run: python3 redteam_sensitivity.py   (reads ../scores.md, pure stdlib)
"""
import re, itertools, statistics, random, math, os
from collections import defaultdict

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

def pca_pc1_share(vecs):
    N, D = len(vecs), 9
    cols = [[v[d] for v in vecs] for d in range(D)]
    mean = [statistics.mean(c) for c in cols]
    M = [[vecs[i][d] - mean[d] for d in range(D)] for i in range(N)]
    cov = [[sum(M[i][a] * M[i][b] for i in range(N)) / (N - 1) for b in range(D)] for a in range(D)]
    def mv(A, x): return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]
    def nrm(x): return math.sqrt(sum(v * v for v in x))
    x = [random.random() for _ in range(D)]
    for _ in range(300):
        y = mv(cov, x); n = nrm(y); x = [v / n for v in y]
    lam = sum(x[i] * mv(cov, x)[i] for i in range(D))
    tot = sum(cov[i][i] for i in range(D))
    return lam / tot if tot else 0.0

def arch_ratio(vecs, arch):
    N = len(vecs)
    pairs = list(itertools.combinations(range(N), 2))
    overall = statistics.mean(man(vecs[i], vecs[j]) for i, j in pairs)
    g = defaultdict(list)
    for i, a in enumerate(arch): g[a].append(i)
    wsum = wn = 0
    for a, idx in g.items():
        if len(idx) < 2: continue
        wd = statistics.mean(man(vecs[i], vecs[j]) for i, j in itertools.combinations(idx, 2))
        wsum += wd * len(idx); wn += len(idx)
    return (wsum / wn / overall) if (wn and overall) else float('nan')

def metrics(vecs, arch):
    N = len(vecs)
    d1 = sum(1 for v in vecs if v[0] == 3) / N
    d3 = sum(1 for v in vecs if v[2] >= 1) / N
    dup = sum(1 for i, j in itertools.combinations(range(N), 2) if vecs[i] == vecs[j])
    return pca_pc1_share(vecs), arch_ratio(vecs, arch), d1, d3, dup

def perturb(v, p):
    out = []
    for x in v:
        if random.random() < p:
            x = max(0, min(3, x + random.choice((-1, 1))))
        out.append(x)
    return out

def main():
    names, arch, vecs = load()
    N = len(vecs)
    random.seed(1)
    base = metrics(vecs, arch)
    print(f"N={N}")
    print(f"BASELINE: PC1={base[0]*100:.1f}% | arch-ratio={base[1]:.2f} | D1=3 {base[2]*100:.0f}% | D3>=1 {base[3]*100:.0f}% | dup-pairs={base[4]}")

    print("\n=== TEST A: ±1 per-cell perturbation (does each conclusion survive scoring noise?) ===")
    print(f"{'noise p':>8} | {'PC1% (mean[min..max])':>26} | {'arch-ratio':>18} | {'D1=3%':>14} | {'D3>=1%':>14} | dup-pairs")
    for p in (0.10, 0.20, 0.33):
        TR = 400
        pc1, ar, d1, d3, dup = [], [], [], [], []
        for _ in range(TR):
            pv = [perturb(v, p) for v in vecs]
            m = metrics(pv, arch)
            pc1.append(m[0]); ar.append(m[1]); d1.append(m[2]); d3.append(m[3]); dup.append(m[4])
        f = lambda L: f"{statistics.mean(L)*100:.1f} [{min(L)*100:.0f}..{max(L)*100:.0f}]"
        print(f"{p:>8.2f} | {f(pc1):>26} | {statistics.mean(ar):.2f} [{min(ar):.2f}..{max(ar):.2f}] | {f(d1):>14} | {f(d3):>14} | {statistics.mean(dup):.1f} (max {max(dup)})")

    print("\n=== TEST B: bootstrap stability (drop random 20% of people, recompute) ===")
    TR = 500; k = int(N * 0.8)
    pc1, ar, d1, d3 = [], [], [], []
    for _ in range(TR):
        idx = random.sample(range(N), k)
        sv = [vecs[i] for i in idx]; sa = [arch[i] for i in idx]
        m = metrics(sv, sa)
        pc1.append(m[0]); ar.append(m[1]); d1.append(m[2]); d3.append(m[3])
    print(f"over {TR} subsamples of {k}/{N}:")
    print(f"  PC1 share:   mean {statistics.mean(pc1)*100:.1f}%  range [{min(pc1)*100:.0f}..{max(pc1)*100:.0f}]%")
    print(f"  arch-ratio:  mean {statistics.mean(ar):.2f}   range [{min(ar):.2f}..{max(ar):.2f}]")
    print(f"  D1=3 frac:   mean {statistics.mean(d1)*100:.0f}%  range [{min(d1)*100:.0f}..{max(d1)*100:.0f}]%")
    print(f"  D3>=1 frac:  mean {statistics.mean(d3)*100:.0f}%  range [{min(d3)*100:.0f}..{max(d3)*100:.0f}]%")

if __name__ == "__main__":
    main()
