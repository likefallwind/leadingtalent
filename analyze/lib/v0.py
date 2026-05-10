"""V0 种子原子集（与方案 V0.1 第 4.2 节一致）。

修改这里 = 修改 V0 假设。需要重跑 02 之后的所有步骤。
"""
from __future__ import annotations

V0_ATOMS = [
    {"id": 1, "cluster": "智识底盘", "name": "问题嗅觉",
     "definition": "识别真正重要问题的判断力（research taste）；选题、对他人工作的批评、提问深度"},
    {"id": 2, "cluster": "智识底盘", "name": "数学/理论深度",
     "definition": "真正理解底层机制（非调包）；推导、对方法的复述深度、理论功底"},
    {"id": 3, "cluster": "智识底盘", "name": "系统性思维",
     "definition": "复杂问题的拆解、组件化、统筹能力；架构设计、长任务规划"},
    {"id": 4, "cluster": "智识底盘", "name": "反共识勇气",
     "definition": "在主流方向之外下注；对热门方法的批评、独立判断、坚持冷门方向"},
    {"id": 5, "cluster": "工程能力", "name": "代码/系统实现力",
     "definition": "idea 到 working system 的能力；高质量代码产出、复杂系统交付"},
    {"id": 6, "cluster": "工程能力", "name": "复现与调试力",
     "definition": "把他人工作跑通并真懂；reproduction、bug 定位、issue 质量"},
    {"id": 7, "cluster": "工程能力", "name": "速度/迭代节奏",
     "definition": "快速试错并调整；prototype 速度、产出节奏、迭代频率"},
    {"id": 8, "cluster": "内驱成长", "name": "长期专注与韧性",
     "definition": "持续投入难题、抗挫折；长项目跟进、产出连续性、面对失败的恢复"},
    {"id": 9, "cluster": "内驱成长", "name": "自我更新速度",
     "definition": "跟上 AI 快速演化的能力；新技术上手时间、跨方向迁移、reading 时效"},
    {"id": 10, "cluster": "外向放大", "name": "表达与影响力",
     "definition": "写、讲、说服的能力；talk 质量、博客阅读量、论文写作、对外演示"},
    {"id": 11, "cluster": "外向放大", "name": "协作与组织力",
     "definition": "合作、带人、跨组；项目协作、带 junior、跨组合作、360 评价"},
    {"id": 12, "cluster": "外向放大", "name": "开源/社区参与",
     "definition": "进入 AI 全球社区；开源贡献、社区互动、外部 workshop、被采纳频次"},
]

ATOM_BY_ID = {a["id"]: a for a in V0_ATOMS}
ATOM_BY_NAME = {a["name"]: a for a in V0_ATOMS}


def atom_text_for_embedding(atom: dict) -> str:
    """生成用于 embedding 的文本，包含名字和定义。"""
    return f"{atom['name']}：{atom['definition']}"
