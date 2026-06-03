#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate an interactive HTML report from the 60 dossier files.
Pulls FACT/CAP text straight from research/facts/*.md (authoritative),
applies the per-capability -> cluster mapping below, and emits report.html.
"""
import os, re, json, glob

HERE = os.path.dirname(os.path.abspath(__file__))
FACTS = os.path.join(HERE, "facts")

# ---- cluster definitions ----
CLUSTERS = {
 "CL1":"长期专注·数十年持续产出","CL2":"按长期信念逆向押注",
 "CL3":'造"基础件"（方法/架构/系统/标准/数据集）',"CL4":"跨学科·跨界迁移",
 "CL5":"工程贯通到量产/产品/平台","CL6":"从零创建并长期领导机构",
 "CL7":"师父·批量育人成谱系","CL8":"早慧硬底子+顶级师承",
 "CL9":"多角色转场·被持续争抢","CL10":"撬动巨额资本与组织动员",
 "CL11":"选大问题·愿景组织攻坚","CL12":"教育/科普/把复杂讲清楚",
 "CL13":"开源·开放作为路线","CL14":"安全/风险/治理/伦理担当",
 "CL15":"命名/造词/框架化·元认知自省","CL16":"韧性·挫折·诚实面对边界",
 "CL17":"捕捉拐点/窗口·趋势预判","CL0":"其他/未归簇",
}
COLORS = {
 "CL1":"#7c83ff","CL2":"#ff6b6b","CL3":"#ffb020","CL4":"#36c5f0",
 "CL5":"#2ec27e","CL6":"#a06cd5","CL7":"#f78fb3","CL8":"#f9a826",
 "CL9":"#4dd0e1","CL10":"#e15554","CL11":"#9b5de5","CL12":"#43aa8b",
 "CL13":"#577590","CL14":"#d62246","CL15":"#b5179e","CL16":"#8d6e63",
 "CL17":"#1982c4","CL0":"#9aa0a6",
}
# ---- per-person cluster tags, in C1..Cn order (must match cap count per file) ----
MAP = {
"F01":["CL2","CL4","CL3","CL17","CL1","CL7","CL5","CL14","CL14","CL15","CL16"],
"F02":["CL5","CL6","CL13","CL2","CL9","CL2","CL2","CL3"],
"F03":["CL2","CL3","CL3","CL14","CL10","CL2","CL6","CL14"],
"F04":["CL3","CL5","CL9","CL0","CL6","CL5","CL14","CL16"],
"F05":["CL17","CL2","CL3","CL14","CL10","CL6","CL15","CL8"],
"F06":["CL4","CL4","CL11","CL3","CL6","CL9","CL11","CL14"],
"F07":["CL10","CL10","CL5","CL10","CL11","CL10","CL14","CL16","CL16"],
"F08":["CL3","CL4","CL6","CL14","CL14","CL10","CL14","CL2"],
"F09":["CL12","CL12","CL9","CL5","CL12","CL9","CL15"],
"F10":["CL8","CL3","CL12","CL3","CL1","CL14"],
"F11":["CL12","CL9","CL6","CL17","CL15","CL10","CL12"],
"F12":["CL2","CL11","CL11","CL14","CL14","CL9","CL16","CL4"],
"F13":["CL3","CL5","CL1","CL3","CL8","CL9","CL5"],
"F14":["CL7","CL9","CL6","CL6","CL6","CL7","CL11"],
"F15":["CL8","CL2","CL3","CL3","CL12","CL6","CL3"],
"F16":["CL2","CL13","CL5","CL14","CL6","CL3"],
"F17":["CL6","CL3","CL5","CL7","CL6","CL10","CL16"],
"F18":["CL6","CL16","CL7","CL1","CL2","CL6"],
"F19":["CL9","CL3","CL6","CL11","CL3","CL6"],
"F20":["CL4","CL17","CL5","CL13","CL2","CL2","CL8"],
"F21":["CL3","CL8","CL9","CL2","CL15","CL16","CL15"],
"F22":["CL9","CL10","CL10","CL17","CL16","CL16"],
"F23":["CL8","CL5","CL5","CL10","CL17","CL11","CL16"],
"F24":["CL9","CL9","CL6","CL10","CL16","CL5","CL12","CL16"],
"F25":["CL12","CL4","CL3","CL14","CL14","CL7","CL15"],
"F26":["CL4","CL15","CL15","CL6","CL15","CL16","CL15"],
"F27":["CL8","CL3","CL6","CL14","CL14","CL14","CL16"],
"F28":["CL4","CL1","CL12","CL15","CL2","CL9","CL16"],
"F29":["CL3","CL8","CL12","CL14","CL5","CL16","CL9"],
"F30":["CL3","CL9","CL11","CL13","CL14","CL10"],
"F31":["CL3","CL13","CL3","CL5","CL6","CL3"],
"F32":["CL4","CL8","CL13","CL6","CL6","CL4"],
"F33":["CL15","CL3","CL4","CL3","CL9","CL7","CL3"],
"F34":["CL5","CL3","CL17","CL13","CL5","CL3","CL13"],
"F35":["CL1","CL9","CL5","CL11","CL2","CL15","CL8"],
"F36":["CL1","CL2","CL2","CL13","CL1","CL5"],
"F37":["CL9","CL2","CL3","CL10","CL15","CL9"],
"F38":["CL9","CL9","CL2","CL13","CL17","CL9"],
"F39":["CL8","CL3","CL5","CL10","CL9","CL14"],
"F40":["CL9","CL6","CL5","CL11","CL5","CL9"],
"F41":["CL8","CL3","CL5","CL5","CL5","CL16"],
"F42":["CL8","CL3","CL5","CL3","CL10","CL9"],
"F43":["CL16","CL5","CL17","CL5","CL15","CL10"],
"F44":["CL2","CL17","CL16","CL5","CL16","CL10"],
"F45":["CL5","CL9","CL13","CL7","CL3","CL9"],
"F46":["CL3","CL5","CL13","CL8","CL9","CL15"],
"F47":["CL8","CL9","CL5","CL3","CL9","CL3"],
"F48":["CL3","CL3","CL9","CL1","CL6","CL6"],
"F49":["CL8","CL3","CL3","CL17","CL9","CL8"],
"F50":["CL3","CL3","CL2","CL9","CL16","CL8"],
"F51":["CL8","CL3","CL3","CL8","CL2","CL15"],
"F52":["CL11","CL3","CL6","CL7","CL2","CL2","CL4"],
"F53":["CL8","CL9","CL3","CL6","CL11","CL9","CL11"],
"F54":["CL16","CL2","CL3","CL6","CL2","CL3"],
"F55":["CL13","CL13","CL8","CL11","CL6","CL13"],
"F56":["CL3","CL3","CL9","CL5","CL10","CL7","CL9"],
"F57":["CL8","CL6","CL3","CL9","CL9","CL2"],
"F58":["CL2","CL7","CL17","CL13","CL5","CL15","CL13"],
"F59":["CL3","CL3","CL12","CL5","CL6","CL4","CL7"],
"F60":["CL12","CL9","CL9","CL3","CL1","CL9"],
}
ARCHETYPES = [
 ["奠基型科学家","CL3·CL1·CL2·CL7","以原创理论/方法奠基，长期专注、形成学派",
  ["F01","F02","F03","F28","F25","F18","F33","F52","F15","F19","F49","F50","F51","F54","F55","F31"]],
 ["科学家–创业者","CL3·CL5·CL6·CL10","把自己的研究直接裂变成公司",
  ["F06","F17","F32","F39","F40","F42","F34","F56","F41","F29","F05","F16","F30","F57"]],
 ["产品/组织型领袖","CL5·CL10·CL11·CL17","以产品与组织动员定义市场",
  ["F07","F35","F44","F22","F23","F20","F43","F37","F21","F36","F38"]],
 ["巨头技术统帅","CL3·CL6·CL9","在大厂长期统领最广技术与平台",
  ["F04","F14","F46","F45","F47","F48","F53","F13","F60"]],
 ["安全/思想型","CL14·CL15·CL12","以风险/治理/思想框架影响行业",
  ["F25","F26","F27","F10","F08","F12"]],
 ["传播/教育型","CL12·CL13","把前沿翻译成大众可学、降低门槛",
  ["F11","F09","F59","F60","F58","F24"]],
]
WALK = {
 "F01":"Hinton = 典型『奠基型科学家→安全/思想型』迁移：寒冬坚持(CL2)、造标准件(CL3)、师父谱系(CL7)，功成后转向风险担当(CL14)，并诚实承认他人优先权、与逆境共存(CL15/CL16)。他几乎不沾资本/产品类簇——印证『领军≠全能模板』。",
 "F31":"刘铁岩 = 干净的『奠基型科学家』：开创排序学习子领域并写定义性专著(CL3)、把研究沉淀成全行业默认工具 LightGBM(CL13)、用竞赛硬指标自证(CL3)、理论+系统+工程兼顾(CL5)，最后从研究院领导转去掌舵新教育机构(CL6)。无资本/逆向/安全类簇——是『纯硬通货』路径的代表。",
 "F32":"张林峰 = 『科学家–创业者』的年轻样本：数学/物理交叉训练(CL4)把深度学习引入分子模拟、开辟 AI for Science；极年轻拿戈登贝尔奖(CL8 底子)；做成系列开源软件生态(CL13)；在导师背书下把科研转化为公司+研究院(CL6)。展示了『跨学科迁移→开源生态→建机构』的链路。",
}

def parse(fp):
    txt = open(fp, encoding="utf-8").read().splitlines()
    title = txt[0].lstrip("# ").strip()
    intro = ""
    for l in txt[1:6]:
        if l.startswith("> ") and "证据深度" not in l:
            intro = l[2:].strip(); break
    facts, caps = [], []
    for l in txt:
        m = re.match(r'^- (F\d+)\s+\[([ABC])\]\s+(.*)$', l)
        if m:
            facts.append({"id":m.group(1),"conf":m.group(2),"t":m.group(3)})
            continue
        m = re.match(r'^- (C\d+)\s+(.*)$', l)
        if m:
            body = m.group(2)
            parts = re.split(r'\s*[—\-]\s*from\s*', body)
            t = parts[0].strip()
            frm = parts[1].strip() if len(parts) > 1 else ""
            caps.append({"id":m.group(1),"t":t,"from":frm})
    return title, intro, facts, caps

people = []
for fp in sorted(glob.glob(os.path.join(FACTS, "F*.md"))):
    base = os.path.basename(fp)
    pid = base.split("_")[0]            # F01
    title, intro, facts, caps = parse(fp)
    clusters = MAP.get(pid, [])
    for i, c in enumerate(caps):
        c["cl"] = clusters[i] if i < len(clusters) else "CL0"
    people.append({"id":pid,"name":title,"intro":intro,"facts":facts,"caps":caps})

# cluster -> distinct people, total caps
clu_people, clu_caps = {k:set() for k in CLUSTERS}, {k:0 for k in CLUSTERS}
for p in people:
    for c in p["caps"]:
        clu_people[c["cl"]].add(p["id"]); clu_caps[c["cl"]] += 1
clu_stats = {k:{"people":sorted(clu_people[k]),"n":len(clu_people[k]),"caps":clu_caps[k]} for k in CLUSTERS}

total_caps = sum(len(p["caps"]) for p in people)
total_facts = sum(len(p["facts"]) for p in people)

DATA = {"clusters":CLUSTERS,"colors":COLORS,"people":people,"cluStats":clu_stats,
        "archetypes":ARCHETYPES,"walk":WALK,
        "totals":{"people":len(people),"caps":total_caps,"facts":total_facts}}

html = open(os.path.join(HERE,"_template.html"), encoding="utf-8").read()
html = html.replace("/*__DATA__*/","const DATA = "+json.dumps(DATA,ensure_ascii=False)+";")
open(os.path.join(HERE,"report.html"),"w",encoding="utf-8").write(html)
print("people=%d facts=%d caps=%d -> report.html"%(len(people),total_facts,total_caps))
for k in CLUSTERS:
    if k!="CL0": print("  %s %-22s 人=%2d 能力=%2d"%(k,CLUSTERS[k][:18],clu_stats[k]["n"],clu_stats[k]["caps"]))
