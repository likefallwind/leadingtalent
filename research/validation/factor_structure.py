import numpy as np
from numpy.linalg import eigh

# D1 D2 D3 D4 D5 D6 D7 D8(信念) D9(拐点) — from scores.md v3
names = ["Hinton","LeCun","Bengio","Dean","Sutskever","Hassabis","Altman","Amodei","Karpathy","Olah","Ng","FeiFei","黄学东","沈向洋","周志华","朱军","汤晓鸥","张钹","高文","梁文锋","杨植麟","王慧文","王小川","李开复","Russell","Bostrom","Christiano","Sutton","Goodfellow","Gomez","刘铁岩","张林峰","鄂维南","唐杰","雷军","张鹏","闫俊杰","姜大昕","印奇","余凯","朱珑","陈天石","王兴兴","张一鸣","周靖人","王海峰","田奇","张正友","何恺明","谢赛宁","张祥雨","朱松纯","张亚勤","黄铁军","林达华","贾佳亚","颜水成","刘知远","孙茂松","李航"]
M = np.array([
[3,1,2,1,0,2,2,3,0],[3,2,3,2,1,1,3,3,1],[3,2,3,1,0,3,3,2,0],[3,3,2,2,1,0,2,1,0],
[3,2,2,2,0,3,0,3,0],[3,2,3,2,2,1,1,3,0],[0,3,3,3,0,1,0,0,3],[2,2,3,2,0,3,1,2,1],
[2,2,1,1,1,1,3,1,0],[2,0,2,0,0,3,3,1,0],[1,2,2,2,0,0,3,0,2],[3,1,3,1,1,2,2,2,0],
[2,3,2,1,0,0,1,0,1],[1,3,3,2,0,1,1,0,1],[3,0,3,0,0,1,3,2,0],[3,2,2,1,0,2,2,1,0],
[3,2,3,2,0,0,3,0,0],[3,0,3,0,1,2,2,2,0],[3,2,3,1,2,0,1,1,0],[3,2,2,2,0,0,3,3,2],
[3,2,2,2,0,0,2,0,2],[0,2,2,3,0,0,0,0,2],[2,3,2,2,0,0,2,0,2],[1,2,3,3,0,1,2,0,2],
[2,0,2,0,0,3,3,2,0],[1,0,2,0,0,3,2,2,0],[3,1,2,0,0,3,1,1,0],[3,0,2,0,1,1,3,3,0],
[3,1,1,1,1,2,3,1,0],[3,2,2,2,0,0,2,2,0],[3,2,2,1,1,0,3,1,0],[3,2,2,1,2,0,2,2,0],
[3,1,3,1,2,2,2,3,0],[3,2,3,2,0,0,2,0,2],[0,3,3,3,3,0,1,0,2],[1,2,2,2,0,0,2,0,1],
[2,3,2,2,0,0,0,0,2],[2,2,2,2,0,0,0,0,1],[2,2,3,2,2,1,1,0,0],[2,3,2,2,3,0,0,3,0],
[3,2,2,1,2,0,0,1,0],[3,2,2,2,3,0,0,2,0],[2,3,2,2,3,0,1,2,0],[1,3,3,3,0,1,0,0,3],
[2,3,2,2,0,0,3,0,1],[2,3,2,2,1,0,2,0,1],[2,2,2,1,2,0,0,1,0],[3,2,2,1,3,0,1,2,0],
[3,0,0,1,1,0,3,2,0],[3,0,2,2,2,0,3,1,0],[3,2,2,1,2,0,1,1,0],[3,0,3,1,1,2,1,3,0],
[1,2,3,2,1,0,1,0,2],[2,1,3,1,2,1,3,2,0],[2,1,2,1,0,0,3,1,0],[3,2,2,2,2,0,2,0,2],
[3,2,2,2,2,0,1,2,0],[2,2,2,1,0,1,3,2,0],[3,1,2,0,0,1,3,2,0],[2,2,2,1,0,0,3,1,0],
])
dims = ["D1原创","D2工程","D3机构","D4资本","D5物理","D6安全","D7教育","D8信念","D9拐点"]
assert M.shape == (60,9), M.shape

# ---- correlation matrix ----
C = np.corrcoef(M.T)
np.set_printoptions(precision=2, suppress=True, linewidth=160)
print("=== Pearson correlation (9x9) ===")
print("       " + " ".join(f"{d[:3]:>5}" for d in dims))
for i,d in enumerate(dims):
    print(f"{d:>6} " + " ".join(f"{C[i,j]:5.2f}" for j in range(9)))

# strongest off-diagonal pairs
print("\n=== |r| ranked pairs ===")
pairs=[]
for i in range(9):
    for j in range(i+1,9):
        pairs.append((abs(C[i,j]),C[i,j],dims[i],dims[j]))
for a,r,di,dj in sorted(pairs,reverse=True):
    tag = "***" if a>=0.5 else ("**" if a>=0.3 else "")
    print(f"  {di:>6} ~ {dj:>6}  r={r:+.2f} {tag}")

# ---- PCA on correlation (standardized) ----
Z = (M - M.mean(0)) / M.std(0)
Cz = np.corrcoef(Z.T)
vals, vecs = eigh(Cz)
order = np.argsort(vals)[::-1]
vals = vals[order]; vecs = vecs[:,order]
ev = vals / vals.sum()
print("\n=== PCA (corr matrix) — variance explained ===")
cum=0
for k in range(9):
    cum+=ev[k]
    kaiser = "  <- eigenvalue<1 (Kaiser: drop)" if vals[k]<1 else ""
    print(f"  PC{k+1}: eig={vals[k]:.2f}  var={ev[k]*100:4.1f}%  cum={cum*100:5.1f}%{kaiser}")

n_kaiser = int((vals>=1).sum())
print(f"\nKaiser criterion (eig>=1): keep {n_kaiser} components")
for thr in (0.7,0.8,0.9):
    k = int(np.searchsorted(np.cumsum(ev), thr)+1)
    print(f"  components for >= {int(thr*100)}% variance: {k}")

# loadings of the retained components
print(f"\n=== Loadings of first {max(n_kaiser,5)} PCs (rows=dims) ===")
K=max(n_kaiser,5)
print("        " + " ".join(f"PC{k+1:>2}" for k in range(K)))
for i,d in enumerate(dims):
    print(f"{d:>6}  " + " ".join(f"{vecs[i,k]:+5.2f}" for k in range(K)))
