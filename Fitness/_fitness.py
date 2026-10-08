# -*- coding: utf-8 -*-
"""生成【健身理论手册 · 中英对照】单文件 HTML：index.html
- 8 大主题知识卡(英文术语+中文讲解) + 🧠SRS间隔复习+错题本 + 测试题自动判分 + 看板
- 实用计算器：1RM 估算 / TDEE+蛋白质 / 磅⇄公斤；术语表可搜索
- 纯前端自包含，进度存 localStorage(命名空间 FIT::)；适配 iPad 大字
运行： python Fitness/_fitness.py
"""
import os
import json
import html as _html

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "index.html")


def esc(s):
    return _html.escape(s, quote=True)


# 每个主题：icon, 英文名, 中文名, cards[(英文术语, 中文术语, 中文讲解)], quiz[(题干,[选项],正确项,解析)]
TOPICS = [
    {"icon": "🏋️", "en": "Training Principles", "cn": "训练原理",
     "cards": [
         ("Progressive Overload", "渐进超负荷", "想持续进步，必须逐步增加训练压力（加重量 / 加次数 / 加组数 / 缩短间歇）。是增肌增力的第一原则。"),
         ("Training Volume", "训练容量", "通常指『组数 × 次数 × 重量』，或每个肌群每周的有效组数。容量是肌肥大的主要驱动，常见建议每肌群每周 10–20 组。"),
         ("Intensity", "训练强度", "多指相对强度，即占 1RM 的百分比。大重量低次数偏力量，中等重量中次数偏增肌。"),
         ("Frequency", "训练频率", "每个肌群每周训练的次数。把同样容量分到每周练 2 次，通常优于只练 1 次。"),
         ("One-Rep Max (1RM)", "单次最大重量", "某动作只能标准完成 1 次的最大重量，用于衡量力量、安排强度百分比。"),
         ("RIR / RPE", "储备次数 / 自觉用力度", "RIR = 还能再做几次（留几次余量）；RPE = 10 分制主观强度。用来控制接近力竭的程度。"),
         ("Supercompensation", "超量恢复", "训练后机体先下降、恢复后超过原水平；在超量窗口再训练才持续进步。练太频或太稀都不理想。"),
         ("SAID Principle", "特异性原则", "Specific Adaptation to Imposed Demands：身体只对你施加的具体刺激产生适应，想练什么就得专项练什么。"),
         ("Periodization", "周期化", "有计划地变化容量与强度（线性：逐步加重；波动 DUP：每次训练变量）。用来突破平台、管理疲劳。"),
         ("Compound vs Isolation", "复合 vs 孤立动作", "复合（深蹲/硬拉/卧推）多关节多肌群、效率高；孤立（弯举/飞鸟）针对单一肌群补强。"),
         ("Deload", "减载周", "每隔几周主动降低容量/强度一周，让身体恢复、消除累积疲劳，预防过度训练与受伤。"),
         ("Movement Patterns", "基本动作模式", "推 push、拉 pull、下蹲 squat、髋铰链 hinge、提携 carry 等；均衡覆盖训练才全面。"),
     ],
     "quiz": [
         ("增肌最主要的驱动因素是？", ["大量做有氧", "训练容量与渐进超负荷", "多喝水", "多做拉伸"], 1, "容量 + 渐进超负荷是肌肥大的核心。"),
         ("RIR 2 表示？", ["做 2 组", "已经力竭", "还能再做 2 次", "休息 2 分钟"], 2, "RIR = 储备次数，2 表示还能再做 2 次。"),
         ("关于周期化，正确的是？", ["一直用同一重量", "有计划地变化容量和强度", "只练一个动作", "从不休息"], 1, "周期化就是有计划地变化训练变量。"),
     ]},
    {"icon": "💪", "en": "Muscles & Anatomy", "cn": "肌肉与解剖",
     "cards": [
         ("Hypertrophy", "肌肥大", "肌肉横截面积增大，也就是俗称的『长肌肉』。"),
         ("Muscle Fiber Types", "肌纤维类型", "I 型（慢肌，耐力、抗疲劳）与 II 型（快肌，爆发、力量、更易增粗）。"),
         ("Concentric", "向心收缩", "肌肉缩短发力的阶段（卧推把杠铃推起来）。"),
         ("Eccentric", "离心收缩", "肌肉拉长、控制负荷的阶段（卧推把杠铃放下来）。离心对肌肥大和酸痛贡献很大。"),
         ("Isometric", "等长收缩", "肌肉长度不变但发力（平板支撑）。"),
         ("Agonist / Antagonist", "主动肌 / 拮抗肌", "完成动作的主动肌，与相反方向的拮抗肌（肱二头肌 vs 肱三头肌）。"),
         ("Chest (Pectorals)", "胸大肌", "主导『推』类水平动作：卧推、俯卧撑、飞鸟。"),
         ("Back (Lats / Traps)", "背阔肌 / 斜方肌", "主导『拉』：引体向上、划船、硬拉。"),
         ("Quads / Hamstrings / Glutes", "股四头 / 腘绳 / 臀", "下肢三大群：深蹲重股四与臀，硬拉和臀桥重腘绳与臀。"),
         ("Core", "核心", "腹直肌、腹横肌、竖脊肌等，负责稳定脊柱、传导力量。"),
         ("Range of Motion (ROM)", "动作幅度", "关节活动范围。充分幅度通常比半程更利于增肌。"),
         ("Mind-Muscle Connection", "念动一致", "主动去感受目标肌肉发力，孤立动作中尤其有用。"),
     ],
     "quiz": [
         ("离心收缩指的是？", ["肌肉缩短发力", "肌肉拉长、控制负荷", "长度不变", "完全不发力"], 1, "离心 = 肌肉在拉长中控制重量。"),
         ("深蹲主要锻炼哪些肌群？", ["胸大肌", "背阔肌", "股四头与臀", "肱二头肌"], 2, "深蹲主练下肢股四头与臀。"),
         ("充分的动作幅度(ROM)对增肌通常？", ["更不利", "没影响", "通常更有利", "会受伤"], 2, "全幅度通常优于半程。"),
     ]},
    {"icon": "🔥", "en": "Muscle Gain & Fat Loss", "cn": "增肌与减脂",
     "cards": [
         ("Caloric Surplus", "热量盈余", "吃进 > 消耗，是增肌（增重）的前提；建议小幅盈余以减少多余增脂。"),
         ("Caloric Deficit", "热量赤字", "消耗 > 吃进，是减脂的根本；约每天 300–500 kcal 赤字较为稳健。"),
         ("Energy Balance (CICO)", "能量平衡", "体重变化本质由『摄入 vs 消耗』决定。"),
         ("Mechanisms of Hypertrophy", "肌肥大三机制", "机械张力（最关键）、代谢压力（泵感）、肌肉损伤。"),
         ("Mechanical Tension", "机械张力", "肌肉在负荷下产生的张力，是肌肥大的主要驱动，靠大重量 / 接近力竭来实现。"),
         ("Body Recomposition", "身体重组", "新手或复练者可同时增肌减脂；进阶者较难，通常分阶段（增肌期 / 减脂期）。"),
         ("Spot Reduction (myth)", "局部减脂（误区）", "不能靠练某个部位只减该处脂肪；脂肪是全身性消耗的。"),
         ("Lean Bulk", "精益增肌", "小幅热量盈余 + 足量蛋白 + 力量训练，增肌同时控制脂肪增长。"),
         ("Cutting", "减脂期", "制造热量赤字 + 保持高蛋白 + 继续力量训练，以尽量保住肌肉。"),
         ("Metabolic Adaptation", "代谢适应", "长期节食后消耗下降、饥饿感增强；可用 diet break / refeed 缓解。"),
         ("Role of Protein", "蛋白质的作用", "提供肌肉合成原料，且高饱腹、高食物热效应，增肌减脂都关键。"),
     ],
     "quiz": [
         ("减脂的根本是？", ["局部运动", "热量赤字", "只做有氧", "完全不吃碳水"], 1, "热量赤字是减脂的根本。"),
         ("肌肥大最关键的机制是？", ["机械张力", "出汗", "肌肉酸痛", "拉伸"], 0, "机械张力是肌肥大的主要驱动。"),
         ("能不能只减肚子的脂肪？", ["能，多做卷腹", "不能，脂肪全身性减少", "能，靠束腰", "能，靠空腹"], 1, "不存在局部减脂。"),
     ]},
    {"icon": "🥗", "en": "Nutrition", "cn": "营养",
     "cards": [
         ("Macronutrients", "三大宏量营养素", "蛋白质(4 kcal/g)、碳水(4 kcal/g)、脂肪(9 kcal/g)。"),
         ("Protein Intake", "蛋白质摄入", "增肌 / 减脂期约 1.6–2.2 g/kg 体重，分散到每餐效果更好。"),
         ("Carbohydrates", "碳水化合物", "主要供能，支撑高强度训练与恢复。并非增脂元凶，关键看总热量。"),
         ("Dietary Fat", "膳食脂肪", "维持激素与整体健康，别低于约 0.5–0.8 g/kg；含必需脂肪酸。"),
         ("TDEE", "每日总能量消耗", "Total Daily Energy Expenditure = 基础代谢 BMR × 活动系数。据此设定增 / 减热量。"),
         ("BMR", "基础代谢率", "静息状态维持生命所需的热量；可用 Mifflin-St Jeor 公式估算。"),
         ("Nutrient Timing", "营养时机", "训练前后摄入蛋白 + 碳水有益，但『全天总量』远比『精确时机』重要。"),
         ("Hydration", "水分", "脱水会显著降低力量与耐力表现；训练中注意补水。"),
         ("Creatine", "肌酸", "证据最充分的补剂：提升力量与肌肉表现，每天 3–5 g，安全有效。"),
         ("Whey Protein", "乳清蛋白", "方便补足蛋白缺口的食品，并非必需，但很实用。"),
         ("Caffeine", "咖啡因", "有效的训练前增强剂，提升专注与表现，约 3–6 mg/kg。"),
         ("BCAA", "支链氨基酸", "若每日蛋白摄入已达标，额外补 BCAA 基本没有额外收益。"),
         ("Fiber & Micronutrients", "纤维与微量营养", "蔬果、全谷提供纤维、维生素与矿物质，利于饱腹与健康。"),
     ],
     "quiz": [
         ("增肌 / 减脂期蛋白质推荐约？", ["0.2 g/kg", "1.6–2.2 g/kg", "5 g/kg", "完全不需要"], 1, "通常建议 1.6–2.2 g/kg 体重。"),
         ("证据最充分、最推荐的补剂是？", ["BCAA", "肌酸", "燃脂丸", "谷氨酰胺"], 1, "肌酸是循证支持最强的补剂。"),
         ("关于营养时机，正确的是？", ["必须练后 30 分钟内吃", "全天总量比精确时机更重要", "只能早上吃蛋白", "碳水完全不能碰"], 1, "全天总量 > 精确时机。"),
     ]},
    {"icon": "😴", "en": "Recovery", "cn": "恢复",
     "cards": [
         ("Sleep", "睡眠", "恢复与肌肉生长的头号因素，建议 7–9 小时。缺觉会损害力量、增肌与减脂。"),
         ("Rest Days", "休息日", "肌肉是在休息时生长的；合理安排休息，防止过度训练。"),
         ("DOMS", "延迟性肌肉酸痛", "训练后 24–72 小时的酸痛，主要由离心引起。酸痛 ≠ 训练有效，也不是必须酸才有效。"),
         ("Overtraining", "过度训练", "长期容量过大 + 恢复不足，表现为成绩下降、持续疲劳、睡眠情绪变差、受伤增多。"),
         ("Warm-up", "热身", "升温 + 动态拉伸 + 递增热身组，降低受伤风险、提升表现。"),
         ("Static vs Dynamic Stretching", "静态 vs 动态拉伸", "训练前宜做动态拉伸；长时间静态拉伸放到训练后或单独进行。"),
         ("Active Recovery", "主动恢复", "低强度活动（散步、轻骑行）促进血液循环、帮助恢复。"),
         ("Injury Prevention", "预防受伤", "规范动作、循序渐进、别盲目冲重量、重视热身与恢复。"),
         ("Fatigue Management", "疲劳管理", "用 RIR、deload、睡眠与营养共同管理累积疲劳。"),
         ("Muscle Protein Synthesis (MPS)", "肌肉蛋白合成", "训练与进食后升高的合成反应，可持续约 24–48 小时，是增肌的生理基础。"),
     ],
     "quiz": [
         ("对恢复最重要的单一因素是？", ["泡澡", "睡眠", "拉伸", "补剂"], 1, "睡眠是恢复第一要素。"),
         ("DOMS（延迟酸痛）说明？", ["一定练到位了", "只是新异/离心刺激，不等于有效", "肌肉必然在增长", "必须每次都酸"], 1, "酸痛不是训练有效的指标。"),
         ("过度训练的典型表现不包括？", ["成绩下降", "持续疲劳", "睡眠变差", "力量稳步提升"], 3, "力量稳步提升是恢复良好的表现。"),
     ]},
    {"icon": "🎯", "en": "Technique", "cn": "动作技术",
     "cards": [
         ("Squat", "深蹲", "下肢之王。要点：核心收紧、膝盖与脚尖同向、至少蹲到大腿平行、背部中立。"),
         ("Deadlift", "硬拉", "髋铰链动作。杠铃贴腿、背部中立不弓、用腿和臀发力起身，别用腰硬拽。"),
         ("Bench Press", "卧推", "肩胛后收下沉、小幅拱腰、杠铃落到中下胸、双脚踩实。"),
         ("Overhead Press", "站姿推举", "核心收紧、别过度后仰、推起时头稍前送、杠铃走直线。"),
         ("Valsalva Maneuver", "瓦式呼吸", "大重量前吸气憋住、绷紧核心以稳定脊柱。高血压人群慎用。"),
         ("Full ROM", "充分幅度", "完整幅度通常优于半程，除非为特定训练目的。"),
         ("Tempo", "节奏/控速", "控制离心（如 2–3 秒下放）能增加张力与刺激。"),
         ("Common Mistakes", "常见错误", "弓背硬拉、膝盖内扣、借力甩动、幅度不够、只加重量不顾动作质量。"),
         ("Grip Types", "握法", "正握 / 反握 / 对握；硬拉可用正反握或助力带防止脱手。"),
         ("Bracing", "核心支撑", "像『要被打一拳』那样绷紧腹部，保护腰椎。"),
     ],
     "quiz": [
         ("瓦式呼吸(Valsalva)的主要作用是？", ["减肥", "大重量时稳定脊柱", "放松身体", "增加柔韧性"], 1, "憋气绷紧核心以稳定脊柱。"),
         ("硬拉的正确做法是？", ["弓着背硬拽", "背部中立、用腿臀发力", "只用腰发力", "耸着肩拉"], 1, "保持中立脊柱、腿臀发力。"),
         ("关于动作与重量，正确的是？", ["只追求加重量", "动作质量优先，再逐步加重", "幅度越小越好", "越快越好"], 1, "先把动作做对再加重量。"),
     ]},
    {"icon": "📋", "en": "Programming", "cn": "计划制定",
     "cards": [
         ("Full-body", "全身训练", "每次练全身，适合新手或训练频率低者，每周 2–3 次。"),
         ("Upper / Lower", "上下肢分化", "上肢日 + 下肢日，常每周 4 次，容量与频率平衡较好。"),
         ("Push / Pull / Legs (PPL)", "推拉腿分化", "按动作模式分化，适合进阶、训练频率较高者。"),
         ("Beginner Programs", "新手计划", "以复合动作为主、线性渐进加重（如全身训练每周 3 练），进步最快。"),
         ("Sets & Reps", "组数与次数", "力量：1–5 次大重量；增肌：以 6–12 次为主；耐力：15 次以上。增肌多落在 6–15 区间。"),
         ("Warm-up Sets", "热身组", "正式组前用递增的轻重量热身、试重，不计入有效容量。"),
         ("Rest Intervals", "组间休息", "大复合动作 2–5 分钟，孤立动作 1–2 分钟；休息够长才能保证下一组表现。"),
         ("Exercise Order", "动作顺序", "先大后小、先复合后孤立、先练弱项；精力充沛时练最重要的。"),
         ("Weekly Volume per Muscle", "每肌群周容量", "常见 10–20 个有效组 / 周，按个人恢复能力调整。"),
         ("Autoregulation", "自我调节", "根据当天状态（RPE / RIR）灵活调整当天的重量与次数。"),
         ("Double Progression", "双重渐进", "进阶者常用：先把次数加到区间上限，再加重量、次数回到下限。"),
     ],
     "quiz": [
         ("推拉腿(PPL)是按什么来分化的？", ["肌肉大小", "动作模式(推/拉/腿)", "星期几", "器械种类"], 1, "按推、拉、腿三类动作模式。"),
         ("增肌最常用的次数区间大致是？", ["1–2 次", "6–15 次", "30 次以上", "100 次"], 1, "增肌多在 6–15 次区间。"),
         ("大复合动作的组间休息通常为？", ["10 秒", "2–5 分钟", "完全不休息", "1 小时"], 1, "大动作需 2–5 分钟恢复。"),
     ]},
    {"icon": "🚫", "en": "Myth Busting", "cn": "破除误区",
     "cards": [
         ("Soreness = good workout?", "酸痛=有效？", "否。酸痛主要反映新异刺激或离心成分，不是进步的必要或充分指标。"),
         ("Lifting makes women bulky?", "女生练铁会变壮？", "否。女性睾酮水平低，很难自然练出『大块头』，力量训练多是紧致塑形。"),
         ("Fasted cardio burns more fat?", "空腹有氧更燃脂？", "差别很小。总的热量赤字才是减脂关键。"),
         ("Spot reduction?", "局部减脂？", "不存在。脂肪是全身性减少的。"),
         ("Carbs make you fat?", "碳水使人发胖？", "否。热量过剩才会；碳水还支撑训练表现。"),
         ("No pain, no gain?", "没有痛苦就没收获？", "疼痛（尤其关节痛）常是受伤信号，别硬扛。"),
         ("More is always better?", "练得越多越好？", "否。超过恢复能力会适得其反，恢复与质量同样重要。"),
         ("Anabolic window?", "必须练后立刻进食？", "所谓窗口比过去认为的宽得多，全天蛋白总量更重要。"),
         ("Machines are useless?", "器械没用，只能自由重量？", "否。器械安全、易孤立、也能有效增肌，与自由重量各有优势。"),
         ("Supplements are necessary?", "补剂是必需的？", "否。补剂只是补充，真正的基础是训练、饮食和睡眠。"),
     ],
     "quiz": [
         ("女生做力量训练会变成『金刚芭比』吗？", ["很容易", "很难，主要是塑形紧致", "一定会", "一周就会"], 1, "女性很难自然练出大块头。"),
         ("『没有酸痛就没效果』对吗？", ["对", "不对，酸痛不是必要指标", "必须天天酸", "越酸越好"], 1, "酸痛与进步不划等号。"),
         ("空腹有氧是否显著更燃脂？", ["是", "差别很小，总赤字才关键", "燃脂翻倍", "是唯一方法"], 1, "减脂看总热量赤字。"),
     ]},
]

# 构建 SRS 卡片数据（供 JS）与术语表
CARDS = []
for ti, t in enumerate(TOPICS):
    for ci, (ten, tcn, exp) in enumerate(t["cards"]):
        CARDS.append({"id": f"c{ti}_{ci}", "topic": ti, "ten": ten, "tcn": tcn, "exp": exp})

CSS = """
<style>
*{box-sizing:border-box;}
body{font-family:-apple-system,"Segoe UI","Microsoft YaHei",sans-serif;margin:0;background:#f5f3f0;color:#231f1c;line-height:1.75;}
header{position:sticky;top:0;z-index:10;background:#e8590c;color:#fff;padding:14px 20px;box-shadow:0 2px 6px rgba(0,0,0,.15);}
header h1{margin:0 0 4px;font-size:18px;}
header .sub{font-size:12.5px;opacity:.92;}
.tabs{display:flex;gap:6px;margin-top:10px;flex-wrap:wrap;}
.tabs button{border:none;background:rgba(255,255,255,.16);color:#fff;padding:8px 16px;border-radius:8px 8px 0 0;cursor:pointer;font-size:14px;}
.tabs button.active{background:#f5f3f0;color:#e8590c;font-weight:600;}
main{max-width:880px;margin:0 auto;padding:20px 16px 80px;}
.panel{display:none;} .panel.show{display:block;}
.util{background:#d9480f;color:#fff;border:none;border-radius:8px;padding:6px 12px;cursor:pointer;font-size:13px;margin-right:6px;}
.hint{color:#6a635d;font-size:13px;}
.disclaimer{background:#fff8e6;border:1px solid #f0d98a;border-radius:8px;padding:9px 13px;margin:10px 0;font-size:13px;color:#8a6d00;}
.topicnav{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0;}
.topicnav a{background:#fff;border:1px solid #f0c9a8;color:#d9480f;border-radius:16px;padding:5px 12px;cursor:pointer;font-size:13px;text-decoration:none;}
.topicnav a:hover{background:#ffe8d6;}
.topic{background:#fff;border-radius:10px;padding:16px 18px;margin:16px 0;box-shadow:0 1px 4px rgba(0,0,0,.06);border-left:5px solid #f0a870;}
.topic h2{margin:0 0 4px;font-size:19px;color:#d9480f;}
.topic .en-name{color:#9a8f86;font-size:14px;font-weight:400;}
.lesson{background:#fbf7f3;border:1px solid #f0e2d4;border-radius:8px;padding:4px 16px 12px;margin:10px 0 4px;line-height:1.9;}
.lesson h4{margin:14px 0 4px;color:#d9480f;font-size:15.5px;}
.lesson p{margin:6px 0;color:#2c2622;}
.lesson ul{margin:6px 0;padding-left:22px;} .lesson li{margin:4px 0;}
.lesson b{color:#b03a00;}
.cards-h{font-size:15px;color:#9a6b4a;margin:16px 0 4px;border-top:1px dashed #f0d9c8;padding-top:10px;}
.ftab{width:100%;border-collapse:collapse;margin:8px 0;font-size:14px;}
.ftab th,.ftab td{border:1px solid #f0e2d4;padding:6px 8px;text-align:left;}
.ftab th{background:#fbeee3;color:#b03a00;}
.ftab tr:nth-child(even){background:#fbf7f3;}
.tnote{color:#6a635d;font-size:13px;margin-top:4px;}
.subtabs{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0 14px;}
.subtab{border:1px solid #f0c9a8;background:#fff;color:#d9480f;border-radius:16px;padding:6px 14px;cursor:pointer;font-size:14px;}
.subtab.active{background:#e8590c;color:#fff;border-color:#e8590c;font-weight:600;}
.topicsub{display:none;}
.card{padding:10px 0;border-bottom:1px solid #f1ece7;}
.card:last-of-type{border-bottom:none;}
.card .ten{font-weight:700;font-size:16px;color:#231f1c;}
.card .spk{border:1px solid #f0c0a0;background:#fff6f0;color:#d9480f;border-radius:13px;padding:2px 9px;cursor:pointer;font-size:12.5px;margin:0 6px;}
.card .tcn{color:#d9480f;font-weight:600;}
.card .exp{display:block;color:#444;margin-top:3px;}
.seedbtn{margin:12px 0 4px;}
.quizwrap{margin-top:14px;padding-top:10px;border-top:1px dashed #f0d9c8;}
.quizwrap h3{font-size:15px;color:#d9480f;margin:0 0 8px;}
.quiz{background:#fff;border:1px solid #f1ece7;border-radius:8px;padding:10px 14px;margin:8px 0;}
.quiz .qq{font-weight:600;margin-bottom:6px;}
.qopt{display:block;padding:4px 8px;border-radius:6px;cursor:pointer;margin:2px 0;}
.qopt:hover{background:#fdf3ec;}
.qopt input{margin-right:8px;}
.qopt.correct{background:#e6f4ea;border-left:3px solid #1a7f37;}
.qopt.wrong{background:#fde8e8;border-left:3px solid #d1242f;}
.qbtn{border:none;background:#e8590c;color:#fff;border-radius:6px;padding:5px 14px;cursor:pointer;font-size:13px;margin-top:6px;}
.qexp{margin-top:8px;padding:8px 10px;background:#fff8e6;border:1px solid #f0d98a;border-radius:6px;font-size:14px;display:none;}
.qexp.show{display:block;}
/* 看板 + SRS */
.dash{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0;}
.dcell{flex:1;min-width:92px;background:#fff;border:1px solid #f1ece7;border-radius:10px;padding:10px 8px;text-align:center;}
.dcell .dnum{font-size:22px;font-weight:800;color:#e8590c;}
.dcell .dlab{font-size:12px;color:#666;margin-top:2px;}
.srsctl{display:flex;gap:8px;flex-wrap:wrap;margin:10px 0;}
.srsflash{background:#fff;border:2px solid #f0c9a8;border-radius:14px;padding:28px 20px;margin:8px 0;min-height:160px;text-align:center;box-shadow:0 2px 8px rgba(0,0,0,.08);}
.srsflash .big{font-size:22px;font-weight:800;color:#d9480f;}
.srs-tag{color:#b06a3a;font-size:13px;}
.srs-prompt{font-size:24px;font-weight:800;margin:8px 0;}
.srs-ans{margin-top:10px;padding:12px;background:#fff6f0;border:1px solid #f0c9a8;border-radius:8px;text-align:left;}
.srs-ans .ten{font-size:20px;font-weight:800;color:#d9480f;}
.srs-ans .exp{margin-top:6px;color:#333;}
.srsbtns{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-bottom:8px;}
.srsbtns button,.qbtn.big{border:none;border-radius:10px;padding:10px 20px;cursor:pointer;font-size:15px;color:#fff;}
.qbtn.big{background:#e8590c;}
.btn-dunno{background:#d1242f;} .btn-fuzzy{background:#d98a00;} .btn-know{background:#1a7f37;}
.weakwrap summary{cursor:pointer;color:#d1242f;font-weight:600;margin-top:10px;}
.weakrow{padding:5px 0;border-bottom:1px solid #f1ece7;font-size:14px;}
/* 计算器 */
.calc{background:#fff;border:1px solid #f1ece7;border-radius:10px;padding:14px 16px;margin:12px 0;}
.calc h3{margin:0 0 8px;color:#d9480f;}
.calc label{display:inline-block;min-width:92px;color:#555;font-size:14px;}
.calc input,.calc select{padding:6px 9px;border:1px solid #f0c9a8;border-radius:6px;font-size:15px;margin:4px 0;}
.calc .res{margin-top:10px;padding:10px 12px;background:#fff6f0;border:1px solid #f0c9a8;border-radius:8px;font-size:15px;}
/* 术语表 */
.gsearch{width:100%;padding:9px 12px;border:1px solid #f0c9a8;border-radius:8px;font-size:15px;margin-bottom:10px;}
.gloss-row{display:flex;gap:8px;align-items:flex-start;padding:8px 0;border-bottom:1px solid #f1ece7;}
.gloss-row .ten{font-weight:700;min-width:40%;}
.gloss-row .tcn{color:#d9480f;}
@media (pointer:coarse) and (min-width:768px){
  html{-webkit-text-size-adjust:100%;text-size-adjust:100%;}
  body{font-size:32px;line-height:1.9;}
  main{width:90%;max-width:none;margin:0 auto;padding:16px 0 72px;}
  header h1{font-size:30px;} header .sub{font-size:24px;}
  .tabs button{font-size:30px;padding:14px 24px;}
  .util{font-size:24px;padding:12px 20px;}
  .hint,.disclaimer{font-size:24px;}
  .topicnav a{font-size:24px;padding:8px 16px;}
  .topic h2{font-size:34px;} .topic .en-name{font-size:24px;}
  .lesson{line-height:2;} .lesson h4{font-size:29px;} .lesson p,.lesson li{font-size:28px;}
  .cards-h{font-size:26px;}
  .ftab{font-size:26px;} .tnote{font-size:24px;}
  .subtab{font-size:26px;padding:10px 22px;}
  .card .ten{font-size:30px;} .card .tcn{font-size:29px;} .card .exp{font-size:28px;}
  .card .spk{font-size:22px;padding:6px 14px;}
  .quizwrap h3{font-size:29px;} .quiz{font-size:29px;}
  .dcell .dnum{font-size:34px;} .dcell .dlab{font-size:20px;}
  .srsflash .big,.srs-prompt{font-size:36px;} .srs-ans .ten{font-size:32px;} .srs-ans .exp{font-size:28px;}
  .srsbtns button,.qbtn.big{font-size:28px;padding:14px 28px;}
  .calc label{font-size:26px;min-width:150px;} .calc input,.calc select{font-size:27px;} .calc .res{font-size:28px;}
  .gsearch{font-size:28px;} .gloss-row{font-size:28px;}
}
@media(max-width:640px){main{padding:16px 8px 60px;}}
</style>
"""

JS = r"""
<script>
function speak(t){try{window.speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(t);u.lang='en-US';u.rate=0.9;window.speechSynthesis.speak(u);}catch(e){}}
function esc2(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
document.addEventListener('click',function(e){var el=e.target;if(el.classList&&el.classList.contains('spk'))speak(el.dataset.t);});
function showTab(i){
  document.querySelectorAll('.panel').forEach(function(p,x){p.classList.toggle('show',x===i);});
  document.querySelectorAll('.tabs button').forEach(function(b,x){b.classList.toggle('active',x===i);});
  localStorage.setItem('FIT::tab',i);window.scrollTo(0,0);
}
function showTopic(i){
  document.querySelectorAll('.topicsub').forEach(function(p,x){p.style.display=(x===i)?'block':'none';});
  document.querySelectorAll('.subtab').forEach(function(b,x){b.classList.toggle('active',x===i);});
  localStorage.setItem('FIT::topic',i);window.scrollTo(0,0);
}
// ---- 测验判分 ----
function gradeQuiz(btn){var box=btn.closest('.quiz');var cor=parseInt(box.dataset.correct);var opts=box.querySelectorAll('.qopt');var picked=-1;
  opts.forEach(function(o,i){var r=o.querySelector('input');o.classList.remove('correct','wrong');if(r.checked)picked=i;});
  if(picked<0){alert('先选一个答案');return;}
  opts[cor].classList.add('correct');if(picked!==cor)opts[picked].classList.add('wrong');
  box.querySelector('.qexp').classList.add('show');localStorage.setItem(box.dataset.k+'::done','1');
  if(picked!==cor){seedCard(box.dataset.card);} }
// ---- SRS ----
var FIT_INT=[1,2,4,7,15,30,60];
function srsGet(){try{return JSON.parse(localStorage.getItem('FIT::srs')||'{}')}catch(e){return{}}}
function srsSet(o){localStorage.setItem('FIT::srs',JSON.stringify(o))}
function statGet(){try{return JSON.parse(localStorage.getItem('FIT::stat')||'{"c":0,"t":0}')}catch(e){return{c:0,t:0}}}
function statSet(o){localStorage.setItem('FIT::stat',JSON.stringify(o))}
function iso(n){var d=new Date();d.setHours(0,0,0,0);d.setDate(d.getDate()+n);return d.toISOString().slice(0,10)}
function cardById(id){for(var i=0;i<CARDS.length;i++)if(CARDS[i].id===id)return CARDS[i];return null;}
function seedCard(id){if(!id)return;var s=srsGet();if(!s[id]){s[id]={box:0,due:iso(0),seen:0,wrong:0};srsSet(s);renderDash();}}
function seedTopic(ti){var s=srsGet(),n=0;CARDS.forEach(function(c){if(c.topic===ti&&!s[c.id]){s[c.id]={box:0,due:iso(0),seen:0,wrong:0};n++;}});srsSet(s);renderDash();alert('已把本主题的 '+n+' 张卡加入复习池。到「🧠 复习」点「今日到期」开始。');}
function seedAll(){var s=srsGet(),n=0;CARDS.forEach(function(c){if(!s[c.id]){s[c.id]={box:0,due:iso(0),seen:0,wrong:0};n++;}});srsSet(s);renderDash();alert('已把全部 '+n+' 张卡加入复习池。');}
function shuffle(a){for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t;}return a;}
function due(){var s=srsGet(),t=iso(0),o=[];CARDS.forEach(function(c){var r=s[c.id];if(r&&r.due<=t)o.push(c);});return o;}
function weak(){var s=srsGet(),o=[];CARDS.forEach(function(c){var r=s[c.id];if(r&&r.seen>0&&r.box<=1)o.push(c);});return o;}
function seeded(){var s=srsGet(),o=[];CARDS.forEach(function(c){if(s[c.id])o.push(c);});return o;}
var RS={list:[],idx:0,shown:false};
function startSrs(mode){var list=mode==='weak'?weak():(mode==='all'?seeded():due());
  var a=document.getElementById('srsarea'),b=document.getElementById('srsbtns');
  if(!list.length){a.innerHTML='<div class="big">🎉 '+(mode==='weak'?'错题本是空的':'没有到期要复习的了')+'</div><div class="hint">先在「📚 知识手册」里学完某主题，点该主题下的「加入复习池」。</div>';b.innerHTML='';return;}
  shuffle(list);RS={list:list,idx:0,shown:false};renderSrs();}
function renderSrs(){var a=document.getElementById('srsarea'),b=document.getElementById('srsbtns');
  if(RS.idx>=RS.list.length){a.innerHTML='<div class="big">🎉 复习完成！</div>';b.innerHTML='';renderDash();renderWeak();return;}
  var c=RS.list[RS.idx];
  a.innerHTML='<div class="srs-tag">'+esc2(TOPICS_CN[c.topic])+'　'+(RS.idx+1)+' / '+RS.list.length+'</div>'+
    '<div class="srs-prompt">'+esc2(c.tcn)+'</div><div class="hint">先想想它的英文术语和含义，再显示答案</div>'+
    '<div class="srs-ans" id="ans" style="display:none"><span class="ten">'+esc2(c.ten)+'</span> <button class="spk" data-t="'+esc2(c.ten).replace(/"/g,'&quot;')+'">🔊</button><div class="exp">'+esc2(c.exp)+'</div></div>';
  if(!RS.shown){b.innerHTML='<button class="qbtn big" onclick="srsShow()">显示答案</button>';}else{rateBtns(b);}}
function srsShow(){RS.shown=true;var el=document.getElementById('ans');if(el)el.style.display='block';rateBtns(document.getElementById('srsbtns'));}
function rateBtns(b){b.innerHTML='<button class="btn-dunno" onclick="rate(0)">✗ 不记得</button><button class="btn-fuzzy" onclick="rate(1)">🤔 模糊</button><button class="btn-know" onclick="rate(2)">✓ 记得</button>';}
function rate(g){var c=RS.list[RS.idx];var s=srsGet();var r=s[c.id]||{box:0,due:iso(0),seen:0,wrong:0};r.seen=(r.seen||0)+1;
  if(g===0){r.box=0;r.wrong=(r.wrong||0)+1;r.due=iso(1);}else if(g===1){r.due=iso(FIT_INT[Math.max(0,r.box||0)]||1);}else{r.box=Math.min(FIT_INT.length-1,(r.box||0)+1);r.due=iso(FIT_INT[r.box]);}
  s[c.id]=r;srsSet(s);var st=statGet();st.t++;if(g===2)st.c++;statSet(st);RS.idx++;RS.shown=false;renderSrs();renderDash();}
function renderDash(){var s=srsGet();var pool=0,mas=0,wk=0;Object.keys(s).forEach(function(id){pool++;if(s[id].box>=4)mas++;if(s[id].seen>0&&s[id].box<=1)wk++;});
  var d=due().length;var st=statGet();var acc=st.t?Math.round(st.c/st.t*100):0;
  var cells=[['复习池',pool],['今日到期',d],['已掌握',mas],['错题本',wk],['正确率',acc+'%']];
  var el=document.getElementById('dash');if(el)el.innerHTML=cells.map(function(c){return '<div class="dcell"><div class="dnum">'+c[1]+'</div><div class="dlab">'+c[0]+'</div></div>';}).join('');}
function renderWeak(){var box=document.getElementById('weaklist');if(!box)return;var w=weak();
  if(!w.length){box.innerHTML='<p class="hint">错题本为空。复习答错或点「不记得/模糊」的卡会进这里。</p>';return;}
  box.innerHTML=w.map(function(c){return '<div class="weakrow"><b>'+esc2(c.ten)+'</b> — '+esc2(c.tcn)+'　<span class="hint">'+esc2(TOPICS_CN[c.topic])+'</span></div>';}).join('');}
// ---- 计算器 ----
function calc1rm(){var w=parseFloat(document.getElementById('w1').value),r=parseInt(document.getElementById('r1').value);var o=document.getElementById('res1');
  if(!w||!r){o.textContent='请输入重量和次数';return;}var orm=w*(1+r/30);
  o.innerHTML='估算 1RM ≈ <b>'+orm.toFixed(1)+' kg</b>（Epley 公式）<br>'+
   '90%: '+(orm*0.9).toFixed(1)+' · 85%: '+(orm*0.85).toFixed(1)+' · 80%: '+(orm*0.8).toFixed(1)+' · 70%: '+(orm*0.7).toFixed(1)+' kg';}
function calcTdee(){var g=document.getElementById('gender').value,a=parseInt(document.getElementById('age').value),h=parseFloat(document.getElementById('ht').value),w=parseFloat(document.getElementById('wt').value),act=parseFloat(document.getElementById('act').value),goal=document.getElementById('goal').value;var o=document.getElementById('res2');
  if(!a||!h||!w){o.textContent='请填写年龄、身高、体重';return;}
  var bmr=10*w+6.25*h-5*a+(g==='m'?5:-161);var tdee=bmr*act;var target=tdee+(goal==='bulk'?300:(goal==='cut'?-400:0));
  var pMin=(w*1.6).toFixed(0),pMax=(w*2.2).toFixed(0);
  o.innerHTML='基础代谢 BMR ≈ <b>'+bmr.toFixed(0)+'</b> kcal<br>每日总消耗 TDEE ≈ <b>'+tdee.toFixed(0)+'</b> kcal<br>目标摄入 ≈ <b>'+target.toFixed(0)+'</b> kcal（'+(goal==='bulk'?'增肌 +300':(goal==='cut'?'减脂 -400':'维持'))+'）<br>蛋白质建议 ≈ <b>'+pMin+'–'+pMax+' g/天</b>';}
function convW(){var lb=document.getElementById('lb').value,kg=document.getElementById('kg').value;var o=document.getElementById('res3');
  if(document.activeElement&&document.activeElement.id==='lb'&&lb){o.innerHTML=lb+' lb ≈ <b>'+(lb*0.453592).toFixed(1)+' kg</b>';}
  else if(kg){o.innerHTML=kg+' kg ≈ <b>'+(kg/0.453592).toFixed(1)+' lb</b>';}else{o.textContent='';}}
// ---- 术语表搜索 ----
function filterGloss(){var q=document.getElementById('gsearch').value.toLowerCase();
  document.querySelectorAll('#glosslist .gloss-row').forEach(function(r){r.style.display=r.textContent.toLowerCase().indexOf(q)>=0?'':'none';});}
// ---- 导出/导入 ----
function expData(){var o={};for(var i=0;i<localStorage.length;i++){var k=localStorage.key(i);if(k.indexOf('FIT::')===0)o[k]=localStorage.getItem(k);}var b=new Blob([JSON.stringify(o,null,2)],{type:'application/json'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='健身理论进度备份.json';a.click();}
function impData(inp){var f=inp.files[0];if(!f)return;var r=new FileReader();r.onload=function(){try{var o=JSON.parse(r.result);Object.keys(o).forEach(function(k){localStorage.setItem(k,o[k]);});location.reload();}catch(e){alert('文件有误');}};r.readAsText(f);}
window.addEventListener('DOMContentLoaded',function(){
  document.querySelectorAll('.quiz').forEach(function(box){if(localStorage.getItem(box.dataset.k+'::done')==='1'){var cor=parseInt(box.dataset.correct);box.querySelectorAll('.qopt')[cor].classList.add('correct');box.querySelector('.qexp').classList.add('show');}});
  renderDash();renderWeak();
  showTopic(parseInt(localStorage.getItem('FIT::topic')||'0'));
  showTab(parseInt(localStorage.getItem('FIT::tab')||'0'));
});
</script>
"""


def card_html(c):
    return (f'<div class="card"><span class="ten">{esc(c[0])}</span>'
            f'<button class="spk" data-t="{esc(c[0])}">🔊</button>'
            f'<span class="tcn">{esc(c[1])}</span>'
            f'<span class="exp">{esc(c[2])}</span></div>')


def quiz_html(ti, q):
    out = []
    for qi, (qq, opts, cor, exp) in enumerate(q, 1):
        name = f"FIT::quiz::t{ti}::q{qi}"
        letters = "ABCD"
        ol = "".join(
            f'<label class="qopt"><input type="radio" name="{name}" value="{oi}"> {letters[oi]}. {esc(o)}</label>'
            for oi, o in enumerate(opts)
        )
        out.append(
            f'<div class="quiz" data-correct="{cor}" data-k="{name}" data-card="c{ti}_0">'
            f'<div class="qq">{qi}. {esc(qq)}</div>{ol}'
            f'<button class="qbtn" onclick="gradeQuiz(this)">对答案</button>'
            f'<div class="qexp">✅ 正确答案：{letters[cor]}。{esc(exp)}</div></div>'
        )
    return "".join(out)


# 每个主题的「系统讲解」文章（把概念串成逻辑，放在术语卡之上）
LESSONS = [
    # 0 训练原理
    """<h4>一、肌肉为什么会变强、变大</h4>
<p>训练的本质是“<b>刺激 → 恢复 → 适应</b>”。你给肌肉一个<b>超过它当前习惯</b>的压力（刺激），训练后在吃和睡中修复，并<b>反弹到比原来更高</b>的水平——这叫<b>超量恢复 (Supercompensation)</b>。关键在于：身体一旦适应，<b>同样的重量就不再是刺激</b>。所以要持续进步，就得不断给出“略高于现状”的负荷，这就是健身第一原则——<b>渐进超负荷 (Progressive Overload)</b>。</p>
<p>超负荷不只“加重量”，手段还有：每组多做 1–2 次、多做 1 组、提高每周频率、缩短组间休息、放慢并控制<b>离心</b>、增大幅度。对<b>减脂塑形</b>的你尤其重要：减脂期要<b>尽力维持这些训练压力</b>，才能把肌肉留住、线条练出来。</p>
<h4>二、三个核心变量：容量 / 强度 / 频率</h4>
<ul>
<li><b>容量 (Volume)</b>：≈ 组数 × 次数 × 重量，常用“每肌群每周有效组数”衡量。它是<b>增肌/保肌的主要驱动</b>，一般每肌群<b>每周 10–20 组</b>，新手偏低端、进阶偏高端。</li>
<li><b>强度 (Intensity)</b>：相对强度（占 <b>1RM</b> 的百分比）。大重量低次数偏<b>力量</b>，中等重量中次数偏<b>增肌</b>。</li>
<li><b>频率 (Frequency)</b>：把每周容量分几次练完。同样 12 组，分 2 天（每次 6 组）通常优于 1 天堆完——质量更高、恢复更好。</li>
</ul>
<p>三者在你的<b>恢复能力</b>之内此消彼长：强度高了单次容量要降，频率高了单次量要分散。</p>
<h4>三、练到多累：RIR / RPE 与“有效次数”</h4>
<p>用 <b>RIR</b>（还能再做几次）或 <b>RPE</b>（10 分制主观强度）衡量努力。真正刺激肌肉的是接近力竭的那几次（“<b>有效次数</b>”）。增肌/保肌通常练到<b>留 1–3 次余量 (RIR 1–3)</b> 即可，不必每组力竭——力竭会大幅拉高疲劳、拖慢恢复，性价比低；大重量复合动作更要留足余量以保证安全。</p>
<h4>四、动作选择：复合优先</h4>
<p><b>复合动作</b>（多关节多肌群：深蹲、硬拉、卧推、划船、推举）效率最高、能举更大重量、保肌最好，应作训练主体；<b>孤立动作</b>（弯举、飞鸟、侧平举）用来补强弱项。减脂期时间精力有限，更要“<b>抓大放小</b>”，先保住大复合动作。</p>
<h4>五、周期化与减载：管理疲劳、避免平台</h4>
<p>长期一成不变会撞<b>平台</b>，疲劳也会累积。<b>周期化 (Periodization)</b> 指有计划地变化容量与强度（线性：逐步加重；波动 DUP：每次变量不同）。每训练 <b>4–8 周</b>安排一次<b>减载 (Deload)</b>（重量或组数降到约一半，练一周），让身体彻底恢复，回来往往更强。</p>
<h4>六、怎么判断“我在进步”</h4>
<p>一定要<b>记录训练</b>（重量×次数×组数）。进步不只是加重量：同样重量多做几次、动作更稳、组间恢复更快、估算 <b>1RM</b> 上升，都算。减脂期如果力量能<b>基本维持</b>，就说明肌肉保住了——这正是塑形成功的信号。</p>
<h4>七、落地清单</h4>
<ul><li>复合动作为主，坚持记录，让表现缓慢但持续上升。</li><li>每肌群每周 10–20 组，分 2 次练。</li><li>多数组留 1–3 次余量。</li><li>每 4–8 周减载一周。</li><li><b>SAID 特异性</b>：目标是什么就专项练什么。</li></ul>""",
    # 1 肌肉与解剖
    """<h4>一、肌肉如何发力：三种收缩</h4>
<p><b>向心 (Concentric)</b>——缩短发力（卧推推起）；<b>离心 (Eccentric)</b>——拉长控制（卧推下放）；<b>等长 (Isometric)</b>——长度不变地绷住（平板支撑）。<b>离心对增肌和酸痛贡献很大</b>，所以“怎么放下来”和“怎么举起来”一样重要——别让重量自由落体，用 2–3 秒控制下放能明显增加刺激。</p>
<h4>二、主动肌与拮抗肌：为什么要均衡</h4>
<p>动作由<b>主动肌</b>完成，反方向的<b>拮抗肌</b>协同稳定（屈肘靠肱二头、伸肘靠肱三头）。一对对肌群容量要大致平衡（比如<b>推与拉</b>别失衡），关节才稳、体态才正，否则容易圆肩等问题。</p>
<h4>三、增肌＝肌肥大，与纤维类型</h4>
<p>训练让现有肌纤维变粗、肌肉横截面积增大，即<b>肌肥大 (Hypertrophy)</b>（增肌不是长出新纤维）。纤维分 <b>I 型</b>（慢肌，耐力、抗疲劳）与 <b>II 型</b>（快肌，爆发、力量，更易增粗）；各次数区间都能练到，不必纠结。</p>
<h4>四、用“动作模式”理解肌群（比背肌肉名实用）</h4>
<ul><li><b>水平推</b>（卧推、俯卧撑）→ 胸、三头、三角肌前束</li><li><b>水平拉</b>（划船）→ 背阔、斜方、二头</li><li><b>垂直推</b>（站姿推举）→ 肩、三头</li><li><b>垂直拉</b>（引体、高位下拉）→ 背阔、二头</li><li><b>下蹲 Squat</b> → 股四头、臀</li><li><b>髋铰链 Hinge</b>（硬拉、臀桥、罗马尼亚硬拉）→ 腘绳、臀、下背</li></ul>
<p>好计划会覆盖这几种模式，身材才均衡；只练“镜子肌”（胸、二头）易体态失衡。<b>核心 (Core)</b> 在几乎所有动作里稳定脊柱，不必天天单独狂练腹。</p>
<h4>五、让每一组更有效</h4>
<ul><li><b>充分幅度 (Full ROM)</b>：完整幅度（尤其拉长位）通常比半程更利于增肌。</li><li><b>念动一致</b>：孤立动作主动“找”目标肌发力、减少借力。</li><li>控制<b>离心</b>、在拉长位稍停，比盲目加重更能刺激肌肉。</li></ul>
<p>对塑形：线条 = 肌肉有一定量 + 体脂够低。所以“塑形”既要练出/保住肌肉（本篇），也要减脂（见「增肌与减脂」）。</p>""",
    # 2 增肌与减脂（当前重点：减脂塑形）
    """<h4>👉 先说清楚：减脂塑形到底怎么回事</h4>
<p>破一个最大的误解：<b>“塑形 / toning”不是一种特殊训练方式</b>，没有“只紧致、不增肌也不减脂”的魔法动作，也不是“小重量高次数”。练出线条本质是两件事叠加：<b>① 降低体脂</b>（让肌肉显出来）＋ <b>② 保住/练出肌肉</b>（让身材有形紧致）。所以 <b>减脂塑形 = 热量赤字减脂 ＋ 力量训练保肌 ＋ 高蛋白</b>，就这三根支柱。</p>
<h4>一、总开关：能量平衡</h4>
<p>体重增减由<b>能量平衡 (Energy Balance / CICO)</b> 决定：<b>赤字 (Deficit)</b> 才减脂、<b>盈余 (Surplus)</b> 才增重。减脂塑形期你要制造一个<b>温和赤字</b>，同时把训练与蛋白维持在“增肌标准”，这样掉的尽量是脂肪、肌肉被保住——体重降得慢些，但<b>围度和线条明显变化</b>。</p>
<h4>二、第一步：设定赤字</h4>
<ul><li>用「🧮 工具」tab 算 <b>TDEE</b>，减脂目标摄入 ≈ <b>TDEE − 20%</b>（约每天 −300~−500 kcal）。</li><li>合理速度：<b>每周减体重的 0.5%~1%</b>（约 0.25~0.5 kg）。太猛会掉肌肉、加剧饥饿与<b>代谢适应</b>、更易反弹。</li><li>减脂是“<b>耐心游戏</b>”：健康速度每月掉 1~2 kg 很正常，急不得。</li></ul>
<h4>三、第二步：蛋白质拉满（减脂期头号营养）</h4>
<p>赤字下身体更想分解肌肉供能，<b>高蛋白是保肌关键</b>。减脂期建议 <b>1.8~2.2 g/kg 体重</b>（甚至偏 2.0~2.4），分到每餐（每餐 25~40 g）。蛋白还<b>最抗饿</b>、食物热效应最高，吃够蛋白减脂会轻松很多。碳水别砍太狠（保训练表现与情绪），脂肪别低于约 0.5 g/kg。</p>
<h4>四、第三步：继续举铁，别改“小重量高次数”</h4>
<p>这是减脂期<b>最重要、也最多人做错</b>的一点：<b>要继续力量训练，而且重量别明显下降</b>。身体靠“你还在举重”这个信号来<b>决定留住肌肉</b>。一减脂就换小哑铃、轻飘飘“塑形操”，反而掉肌肉、越减越松。正确做法：</p>
<ul><li>维持<b>中大重量</b>、<b>6~15 次</b>区间、复合为主（和增肌期几乎一样）。</li><li>训练<b>容量可略降</b>（赤字下恢复变差），但<b>强度（重量）尽量保持</b>。</li><li>目标：“<b>力量基本不掉</b>”——做到了就说明肌肉保住了。</li></ul>
<h4>五、有氧与 NEAT：制造赤字的工具，而非必需</h4>
<ul><li>减脂<b>不一定要做有氧</b>：靠“饮食赤字 + 力量训练”就能减；有氧只是<b>额外增加消耗</b>的手段。</li><li><b>NEAT</b>（走路、家务等非运动消耗）常被低估——<b>每天 8k~10k 步</b>性价比极高，还不占训练恢复。</li><li>要加有氧：<b>LISS</b>（低强度长时间，如快走/慢骑，省恢复）或少量 <b>HIIT</b> 都行；别过量，否则挤占力量训练恢复、还更饿。</li></ul>
<h4>六、平台、refeed 与代谢适应</h4>
<ul><li>体重<b>连续 2~3 周</b>不动才算真平台（短期波动多是水分/排便）。先确认吃动有没有执行到位，再<b>小幅</b>降热量或加步数，别一次砍太多。</li><li>长期赤字会<b>代谢适应</b>（消耗下降、更饿、乏力）。可每隔几周安排 1~2 天<b>回到维持热量（diet break / refeed，多补碳水）</b>，缓解生理与心理疲劳。</li></ul>
<h4>七、怎么看进步（别只盯体重秤）</h4>
<p>体重每天因水分、盐、碳水、经期大幅波动，要看<b>趋势</b>而非单日：</p>
<ul><li>每天固定条件称重，比<b>一周平均值</b>。</li><li><b>腰围</b>是减脂最准的尺子，每 1~2 周量一次。</li><li>同角度<b>照片</b>、衣服松紧、<b>力量表现</b>（没掉就说明肌肉还在）。</li></ul>
<h4>八、关于“塑形”的真相与常见坑</h4>
<ul><li><b>局部减脂不存在</b>：狂练腹不会只掉肚子脂肪；腹肌是“<b>吃出来的</b>”，体脂够低自然显现。</li><li><b>女生举铁不会变“金刚芭比”</b>：睾酮低很难长大块头，力量训练恰是紧致塑形的关键。</li><li>别“<b>极低热量 + 疯狂有氧</b>”：掉肌肉、代谢崩、极易暴食反弹。</li><li>没有“<b>燃脂动作</b>”或“排毒茶/暴汗服”，只有总赤字管用。</li></ul>
<h4>九、给你的一周落地模板（减脂塑形）</h4>
<ul><li><b>力量训练 3~4 次/周</b>（上/下肢 或 推/拉/腿），复合为主、留 1~2 次余量、重量尽量维持。</li><li><b>每天 8k~10k 步</b>（NEAT）；可选 2 次 20~30 min LISS 有氧。</li><li>热量 ≈ <b>TDEE − 20%</b>；蛋白 ≈ <b>2.0 g/kg</b>；多蔬菜、喝够水、<b>睡 7~9 小时</b>（缺觉会增饿、掉肌肉）。</li><li>每周称重取平均 + 每两周量腰围/拍照；平台两三周才微调。</li></ul>
<p>把这套坚持 <b>8~12 周</b>，比任何“速成法”都靠谱。</p>""",
    # 3 营养
    """<h4>一、三步定饮食</h4>
<p><b>① 定总热量</b>：算 <b>TDEE</b>（＝ 基础代谢 <b>BMR</b> × 活动系数），减脂 −20%、增肌 +10~15%、维持不变。<b>② 定蛋白</b>：按体重先把蛋白定下来。<b>③ 分配碳水与脂肪</b>：用剩余热量按喜好和训练需求分。</p>
<h4>二、三大宏量逐个讲透</h4>
<ul>
<li><b>蛋白质 (Protein, 4 kcal/g)</b>：最重要，<b>1.6~2.2 g/kg</b>（减脂取高端）。来源：鸡胸、鱼虾、瘦牛、蛋、低脂奶/希腊酸奶、豆制品、乳清。每餐 25~40 g、全天分散最好。</li>
<li><b>碳水 (Carbs, 4 kcal/g)</b>：主要供能，支撑训练强度与恢复，也影响状态心情。<b>碳水不等于长胖</b>，热量过剩才会。优选：米饭、燕麦、土豆/红薯、全谷、水果。</li>
<li><b>脂肪 (Fat, 9 kcal/g)</b>：维持激素与健康，<b>别低于约 0.5 g/kg</b>。优选：坚果、橄榄油、鱼油、蛋黄、牛油果；热量密度高，减脂期别过量。</li>
</ul>
<h4>三、举个例子（60 kg，减脂）</h4>
<p>设 TDEE ≈ 2000 kcal → 减脂目标约 <b>1600 kcal</b>。蛋白 2.0 g/kg = 120 g（480 kcal）；脂肪 0.8 g/kg ≈ 48 g（430 kcal）；剩约 690 kcal 给碳水 ≈ 170 g。这只是起点，按体重趋势微调。</p>
<h4>四、饱腹感：减脂期的隐形关键</h4>
<p>同样热量，<b>高蛋白 + 高纤维（蔬菜、全谷、豆类）+ 足量水分</b>最抗饿；高度加工的高糖高脂食物热量高又不顶饱。减脂期多选<b>体积大、热量低、蛋白高</b>的食物，饿感会小很多。</p>
<h4>五、时机 vs 总量</h4>
<p>训练前后吃点蛋白＋碳水有益，但<b>全天总量远比精确时机重要</b>，不必迷信“练后 30 分钟窗口”。一天几餐看习惯——<b>能长期坚持的方案才是好方案</b>。</p>
<h4>六、补剂金字塔（按性价比）</h4>
<ul><li>地基：<b>训练 ＋ 饮食 ＋ 睡眠</b>（真正决定结果）。</li><li>证据扎实：<b>肌酸</b> 3~5 g/天（增力保肌，减脂期也可继续）、<b>咖啡因</b> 练前。</li><li>图方便：<b>乳清蛋白</b>（补蛋白缺口的食品，非必需）。</li><li>多数可省：BCAA、各种“燃脂丸”，蛋白达标时几乎无额外收益。</li></ul>
<h4>七、关于酒精</h4>
<p>酒精 7 kcal/g 且几乎“空热量”，还抑制脂肪氧化、影响睡眠与恢复。减脂期尽量少喝；要喝就选低糖、并算进当天热量。</p>
<h4>八、常见高蛋白食物速查（每 100 g，约数）</h4>
<table class="ftab"><thead><tr><th>食物</th><th>蛋白 (g)</th><th>热量 (kcal)</th></tr></thead><tbody>
<tr><td>鸡胸肉（熟）</td><td>31</td><td>165</td></tr>
<tr><td>虾（熟）</td><td>24</td><td>99</td></tr>
<tr><td>金枪鱼（水浸罐头）</td><td>24</td><td>110</td></tr>
<tr><td>瘦牛肉（熟）</td><td>26</td><td>180</td></tr>
<tr><td>三文鱼（熟）</td><td>22</td><td>200</td></tr>
<tr><td>鸡腿（去皮，熟）</td><td>24</td><td>170</td></tr>
<tr><td>鸡蛋（1 个 ≈ 6 g 蛋白）</td><td>13</td><td>155</td></tr>
<tr><td>希腊酸奶（无糖）</td><td>10</td><td>60</td></tr>
<tr><td>脱脂牛奶（每 100 ml）</td><td>3.5</td><td>35</td></tr>
<tr><td>老豆腐</td><td>12</td><td>120</td></tr>
<tr><td>毛豆（熟）</td><td>11</td><td>120</td></tr>
<tr><td>乳清蛋白粉（1 勺约 30 g）</td><td>80</td><td>380</td></tr>
</tbody></table>
<p class="tnote">数值为常见约数，烹饪与品牌会有差异。减脂优先选“<b>高蛋白、低热量、顶饱</b>”的：鸡胸、虾、金枪鱼、希腊酸奶、豆腐、瘦牛。</p>""",
    # 4 恢复
    """<h4>一、训练是“破坏”，恢复才“生长”</h4>
<p>训练只是给出刺激，肌肉在<b>休息和进食时</b>修复长大（<b>肌肉蛋白合成 MPS</b> 训练后持续约 24~48 小时）。恢复不是偷懒，而是训练不可分割的另一半——练了不恢复，等于白练甚至倒退。</p>
<h4>二、睡眠：被低估的头号因素（减脂期尤甚）</h4>
<p><b>睡眠 7~9 小时</b>。缺觉对减脂塑形特别糟：皮质醇升高、饥饿激素 <b>ghrelin↑ / 瘦素 leptin↓</b>——结果就是<b>更饿、更馋高糖高脂、更难控制热量</b>，同时损害力量与肌肉保留。可以说<b>没睡好，减脂先输一半</b>。</p>
<h4>三、休息日与训练频率</h4>
<p>肌肉在休息时生长。因 MPS 约 48 小时，<b>每个肌群每周练 2 次</b>通常优于 1 次。别天天把同一部位练到力竭；每周留 1~2 个完全休息或主动恢复日。</p>
<h4>四、压力也占“恢复预算”</h4>
<p>工作/生活压力同样消耗恢复能力，高压期可适当降量。<b>主动恢复</b>（散步、轻骑、拉伸）促进循环、帮助恢复，还顺带增加 NEAT 消耗，对减脂一举两得。</p>
<h4>五、酸痛与过度训练</h4>
<p><b>DOMS（延迟性酸痛）≠ 训练有效</b>，不酸也能很有效；长期酸到影响训练反而说明没恢复好。<b>过度训练 (Overtraining)</b> 信号：成绩持续下降、总是疲惫、睡眠情绪变差、食欲紊乱、易受伤——出现就减量或减载。</p>
<h4>六、热身与疲劳管理</h4>
<p>训练前 <b>5~10 分钟升温 + 动态拉伸 + 递增热身组</b>（长时间静态拉伸放训练后或单独做）。用 <b>RIR（别总力竭）＋ 定期减载 ＋ 睡眠营养</b> 共同管理累积疲劳。</p>""",
    # 5 动作技术
    """<h4>一、原则：动作质量 &gt; 重量</h4>
<p>先把动作模式做标准，再谈加重。盲目冲重量、动作走形是受伤和进步慢的头号原因。减脂期更要稳——别为了“燃脂”把动作做得又快又乱。</p>
<h4>二、通用要点（所有大动作适用）</h4>
<ul><li><b>中立脊柱</b>：全程别弓腰塌背、别过度后仰。</li><li><b>核心支撑 (Bracing)</b>：像“要挨一拳”那样 360° 绷紧腹部；大重量配合<b>瓦式呼吸 (Valsalva)</b>（起始前吸气憋住稳住躯干，完成后呼气；高血压/心血管问题者改用正常呼吸）。</li><li><b>充分幅度 + 控制离心</b>：慢放 2~3 秒、不借惯性。</li><li><b>关节走正轨</b>：膝随脚尖、肩别耸、手腕中立。</li></ul>
<h4>三、四大动作要点</h4>
<ul><li><b>深蹲 Squat</b>：脚约与肩同宽、脚尖略外展；吸气绷核心，髋膝同时下沉，膝与脚尖同向，至少蹲到大腿平行；脚跟踩实、背部中立。</li><li><b>硬拉 Deadlift</b>：杠铃贴小腿、肩略在杠前、背部中立；用<b>腿蹬地 + 臀发力</b>把杠“推”起来，杠贴腿上行，<b>别弓腰硬拽</b>。</li><li><b>卧推 Bench</b>：肩胛<b>后收下沉</b>、小幅挺胸、双脚踩实；杠落到<b>中下胸</b>、前臂垂直，推起走微弧线。</li><li><b>推举 OHP</b>：核心收紧、夹臀防过度后仰；杠过脸后头略前送，锁定在头顶正上方。</li></ul>
<h4>四、热身流程（每次训练前）</h4>
<p>5 分钟升温（快走/划船机）→ 目标肌群动态活动 → 该动作用<b>空杆/轻重量做 2~3 组递增热身组</b>，逐步加到工作重量。既防伤又能“试重”。</p>
<h4>五、落地</h4>
<p>新动作先用<b>空杆或轻重量练模式</b>，<b>录视频自查</b>或请教练看一眼，标准后再按渐进超负荷慢慢加。<b>关节刺痛/锐痛是停止信号，别硬扛</b>；肌肉的“酸胀累”则正常。</p>""",
    # 6 计划制定
    """<h4>一、先按“每周能练几天”选分化</h4>
<ul><li><b>全身 Full-body（每周 3 练）</b>：每次练到全身主要肌群，频率高、适合新手或时间少的人，也很适合<b>减脂期</b>（效率高、保肌好）。</li><li><b>上/下肢 Upper/Lower（每周 4 练）</b>：上肢日＋下肢日各 2 次，容量与频率平衡好，适合中级。</li><li><b>推/拉/腿 PPL（每周 5~6 练）</b>：按动作模式分化，容量大，适合进阶、时间充裕者。</li></ul>
<h4>二、组数 / 次数 / 休息</h4>
<ul><li>次数：力量 1~5；增肌/保肌 6~12（整体 6~15 都有效）；耐力 15+。减脂塑形用 <b>6~15</b> 即可，别一味高次数轻重量。</li><li>每肌群<b>每周 10~20 个有效组</b>；减脂期可取<b>偏低~中</b>（约 10~14）以匹配下降的恢复。</li><li>组间休息：大复合 <b>2~3 分钟</b>，孤立 <b>1~2 分钟</b>——休息够才能保证下一组重量。</li></ul>
<h4>三、动作顺序与进阶</h4>
<p>顺序：<b>先大后小、先复合后孤立、先练弱项</b>；正式组前做热身组。进阶：新手<b>线性加重</b>；之后用<b>双重渐进</b>——先把次数加到区间上限（如 12），再加重量、次数回到下限（如 8），循环往上。每 4~8 周<b>减载</b>一周。</p>
<h4>四、给你的减脂塑形模板（上/下肢 ×4）</h4>
<ul>
<li><b>下肢 A</b>：深蹲 3×6-10、罗马尼亚硬拉 3×8-12、腿举 3×10-15、提踵 3×12-20、卷腹/平板支撑。</li>
<li><b>上肢 A</b>：卧推 3×6-10、划船 3×8-12、肩推 3×8-12、高位下拉 3×10-12、二头/三头各 2×10-15。</li>
<li><b>下肢 B</b>：硬拉或臀桥 3×6-10、箭步蹲 3×10/腿、腿弯举 3×12-15、臀外展 3×15。</li>
<li><b>上肢 B</b>：引体/下拉 3×6-10、上斜卧推 3×8-12、坐姿划船 3×10-12、侧平举 3×12-20、面拉 3×15。</li></ul>
<p>每组留 1~2 次余量，重量能维持就说明肌肉保住了；配合每天 8k~10k 步。</p>
<h4>五、纯新手：全身 ×3/周 模板</h4>
<p>刚开始的 2~3 个月，用<b>全身训练 + 线性加重</b>进步最快，也最适合减脂期（高效、保肌好）。每周三练（如一/三/五，中间隔一天），每次按顺序做下面几个动作：</p>
<ul>
<li><b>深蹲 Squat</b> 3×8–10</li>
<li><b>卧推 或 俯卧撑</b> 3×8–10</li>
<li><b>罗马尼亚硬拉 或 硬拉</b> 2×8–10</li>
<li><b>划船 或 高位下拉</b> 3×8–12</li>
<li><b>肩推 Overhead Press</b> 2×8–12</li>
<li>（可选）<b>平板支撑</b> 3×30–45 秒</li>
</ul>
<p>每个大动作先做 1–2 组轻重量<b>热身组</b>。<b>进阶方式</b>：某动作三组都做到了次数上限，下次就加一点重量（上肢约 +1–2.5 kg，下肢约 +2.5–5 kg），次数回到下限再往上爬。全程<b>动作标准优先</b>、留 1–3 次余量。坚持 8–12 周，你会明显感到力量和线条的变化。</p>
<h4>六、坚持比完美更重要</h4>
<p><b>选一个计划坚持 8~12 周</b>再评估，别频繁换；记录训练、按双重渐进慢慢加。<b>能长期执行的计划才是最好的计划</b>。</p>""",
    # 7 破除误区
    """<h4>判断任何健身说法，先问三件事</h4>
<p><b>有没有证据？符不符合能量平衡？符不符合渐进超负荷与恢复？</b> 用这三把尺子，大多数流行说法一测便知。</p>
<h4>训练类</h4>
<ul>
<li><b>“酸痛才有效”</b> —— 否。<b>DOMS</b> 只反映新异/离心刺激，不酸也能长肌肉；长期剧痛反而是没恢复好。</li>
<li><b>“女生练铁会变壮”</b> —— 否。女性睾酮低，很难自然长大块头，力量训练正是<b>紧致塑形</b>的关键。</li>
<li><b>“小重量高次数才塑形、大重量只长块”</b> —— 误区。线条＝减脂＋保肌，保肌靠中大重量；轻飘飘高次数既不保肌也不高效。</li>
<li><b>“练得越多越好”</b> —— 否，超过恢复能力会适得其反。</li>
<li><b>“器械没用、只能自由重量”</b> —— 否，器械安全易孤立，也能有效增肌，各有优势。</li>
</ul>
<h4>减脂 / 饮食类（你当前最该分清的）</h4>
<ul>
<li><b>“局部减脂”“狂练腹出马甲线”</b> —— 不存在。脂肪全身性减少，腹肌靠<b>低体脂</b>才显现。</li>
<li><b>“空腹有氧更燃脂”</b> —— 差别很小，减脂看<b>总热量赤字</b>。</li>
<li><b>“碳水/主食使人胖”“晚上吃碳水长肉”</b> —— 否，<b>热量过剩</b>才会；时间点不改变总账。</li>
<li><b>“出汗多＝燃脂多”“裹保鲜膜/暴汗服减脂”</b> —— 否，出汗只是失水，补水就回来。</li>
<li><b>“排毒茶/代餐/燃脂丸能瘦”</b> —— 基本是智商税；真正起效的只有赤字＋训练＋睡眠。</li>
<li><b>“必须练后马上进食”</b> —— 窗口很宽，全天蛋白总量更重要。</li>
<li><b>“极低热量速瘦”</b> —— 掉肌肉、代谢适应、几乎必反弹；温和赤字才可持续。</li>
</ul>""",
]

# 每个主题 = 一个独立面板（点对应 tab 只看该主题）
_disc = ("<div class='disclaimer'>⚠️ 以下为通用的循证科普知识，<b>不构成针对个人的医疗或营养处方</b>。"
         "有伤病、慢性病或特殊情况请咨询医生或专业教练。</div>")
topic_subtabs = []     # 知识手册里的 8 个主题子标签
topic_subpanels = []   # 对应的 8 个子面板（一次只显示一个）
for ti, t in enumerate(TOPICS):
    cards = "".join(card_html(c) for c in t["cards"])
    quiz = quiz_html(ti, t["quiz"])
    topic_subtabs.append(
        f"<button class='subtab' onclick='showTopic({ti})'>{esc(t['icon'])} {esc(t['cn'])}</button>"
    )
    topic_subpanels.append(
        f'<div class="topicsub" id="ts{ti}">'
        f'<section class="topic" id="t{ti}"><h2>{esc(t["icon"])} {esc(t["cn"])} '
        f'<span class="en-name">{esc(t["en"])}</span></h2>'
        f'<div class="lesson">{LESSONS[ti]}</div>'
        f'<h3 class="cards-h">📇 术语速查卡（配合上面的讲解，用来记忆与复习）</h3>'
        f'{cards}'
        f'<div class="seedbtn"><button class="util" onclick="seedTopic({ti})">➕ 学完了？把本主题加入复习池</button></div>'
        f'<div class="quizwrap"><h3>✅ 小测验</h3>{quiz}</div>'
        f'</section></div>'
    )

# 术语表
gloss_rows = "".join(
    f'<div class="gloss-row"><span class="ten">{esc(c["ten"])} <button class="spk" data-t="{esc(c["ten"])}">🔊</button></span>'
    f'<span class="tcn">{esc(c["tcn"])}</span></div>'
    for c in sorted(CARDS, key=lambda x: x["ten"].lower())
)

# 数据脚本
data_js = ("<script>var CARDS=" + json.dumps(CARDS, ensure_ascii=False)
           + ";var TOPICS_CN=" + json.dumps([t["cn"] for t in TOPICS], ensure_ascii=False) + ";</script>")

calc_html = (
    "<div class='calc'><h3>🧮 1RM 估算（Epley）</h3>"
    "<div><label>重量 (kg)</label><input id='w1' type='number' inputmode='decimal'></div>"
    "<div><label>完成次数</label><input id='r1' type='number' inputmode='numeric'></div>"
    "<button class='util' onclick='calc1rm()'>计算</button><div class='res' id='res1'></div></div>"
    "<div class='calc'><h3>🍚 TDEE + 蛋白质</h3>"
    "<div><label>性别</label><select id='gender'><option value='m'>男</option><option value='f'>女</option></select></div>"
    "<div><label>年龄</label><input id='age' type='number'></div>"
    "<div><label>身高 (cm)</label><input id='ht' type='number'></div>"
    "<div><label>体重 (kg)</label><input id='wt' type='number'></div>"
    "<div><label>活动量</label><select id='act'>"
    "<option value='1.2'>久坐</option><option value='1.375'>轻度(每周1-3练)</option>"
    "<option value='1.55' selected>中度(每周3-5练)</option><option value='1.725'>高度(每周6-7练)</option></select></div>"
    "<div><label>目标</label><select id='goal'><option value='maintain'>维持</option><option value='bulk'>增肌</option><option value='cut'>减脂</option></select></div>"
    "<button class='util' onclick='calcTdee()'>计算</button><div class='res' id='res2'></div></div>"
    "<div class='calc'><h3>⚖️ 磅 ⇄ 公斤</h3>"
    "<div><label>磅 (lb)</label><input id='lb' type='number' oninput='convW()'></div>"
    "<div><label>公斤 (kg)</label><input id='kg' type='number' oninput='convW()'></div>"
    "<div class='res' id='res3'></div></div>"
)

html = (
    "<!DOCTYPE html><html lang='zh'><head><meta charset='utf-8'>"
    "<meta name='viewport' content='width=device-width,initial-scale=1'>"
    "<title>健身理论手册</title>" + CSS + "</head><body>"
    "<header><h1>🏋️ 健身理论手册 · 中英对照</h1>"
    "<div class='sub'>循证健身知识 · 术语中英对照 · 🧠 间隔复习 · 🧮 实用计算器</div>"
    "<div style='margin-top:8px'><button class='util' onclick='expData()'>💾 导出</button>"
    "<button class='util' onclick=\"document.getElementById('impf').click()\">📂 导入</button>"
    "<input type='file' id='impf' accept='.json' style='display:none' onchange='impData(this)'></div>"
    "<div class='tabs'>"
    "<button onclick='showTab(0)'>📚 知识手册</button>"
    "<button onclick='showTab(1)'>🧠 复习</button>"
    "<button onclick='showTab(2)'>🧮 工具</button>"
    "<button onclick='showTab(3)'>📖 术语表</button>"
    "</div></header><main>"
    # 面板 0：知识手册（顶部 4 主 tab 之一；内部用子标签切换 8 个主题）
    + "<section class='panel'>" + _disc
    + "<p class='hint'>点下面的主题切换，每个主题包含：系统讲解 → 术语速查卡 → 小测验 → 加入复习池。</p>"
    + "<div class='subtabs'>" + "".join(topic_subtabs) + "</div>"
    + "".join(topic_subpanels) + "</section>"
    # 面板 1：复习
    + "<section class='panel'>"
    "<div class='dash' id='dash'></div>"
    "<div class='srsctl'><button class='util' onclick=\"startSrs('due')\">🔁 今日到期</button>"
    "<button class='util' onclick=\"startSrs('weak')\">❗ 只练错题本</button>"
    "<button class='util' onclick=\"startSrs('all')\">📚 全部过一遍</button>"
    "<button class='util' onclick='seedAll()'>➕ 全部加入复习池</button></div>"
    "<p class='hint'>看中文概念 → 回想它的英文术语和含义 → 显示答案核对 → 如实评价。记得牢的间隔拉长，记不住的进错题本。</p>"
    "<div class='srsflash' id='srsarea'><div class='big'>先在各主题 tab 里点「加入复习池」，再点「今日到期」</div></div>"
    "<div class='srsbtns' id='srsbtns'></div>"
    "<details class='weakwrap'><summary>❗ 错题本</summary><div id='weaklist'></div></details>"
    "</section>"
    # 面板 _nt+1：工具
    "<section class='panel'><p class='hint'>常用小工具。1RM 为估算值，接近力竭时越准；TDEE 为估算，按实际体重变化微调。</p>"
    + calc_html + "</section>"
    # 面板 _nt+2：术语表
    + "<section class='panel'><p class='hint'>所有英文术语与中文对照，可搜索（中英均可）。</p>"
    "<input class='gsearch' id='gsearch' placeholder='🔍 搜索术语…' oninput='filterGloss()'>"
    "<div id='glosslist'>" + gloss_rows + "</div></section>"
    + "</main>" + data_js + JS + "</body></html>"
)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print(f"done -> {OUT} ; 主题={len(TOPICS)} 知识卡={len(CARDS)}")
