# -*- coding: utf-8 -*-
"""生成【英语每日训练】单文件 HTML：英语学习-每日训练.html
- 30 天循环，每天约 30 分钟：今日歌曲跟唱 + 词汇短语(TTS发音) + 影子跟读 + 复习 + 打卡
- 浏览器自带朗读(TTS)，点 🔊 听发音；进度/打卡存 localStorage(命名空间 ENG::)
运行： python 英语学习/_english.py
"""
import os
import html as _html

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "index.html")


def esc(s):
    return _html.escape(s, quote=True)


# 每天：主题、词汇[(英, 中, 例句)]、跟读[(英, 中)]、歌曲(标题,歌手,难度,为什么/语言点,[(短语,中)])
DAYS = [
    {"theme": "自我介绍 Introducing yourself",
     "vocab": [("I'm a ... by profession", "我的职业是……", "I'm a software engineer by profession."),
                ("work for", "就职于", "I work for a foreign company."),
                ("be in charge of", "负责", "I'm in charge of the data team."),
                ("based in", "常驻/位于", "I'm based in Shanghai."),
                ("Nice to meet you", "很高兴认识你", "Nice to meet you. I've heard a lot about you.")],
     "shadow": [("Hi, I'm Yue. I work in the AI team.", "你好，我是 Yue，在 AI 团队工作。"),
                 ("Could you tell me a little about yourself?", "能介绍一下你自己吗？"),
                 ("I've been with the company for three years.", "我在这家公司工作三年了。")],
     "song": ("Count on Me", "Bruno Mars", "★☆☆ 易/慢", "吐字清晰、旋律简单，适合入门跟唱；学 count on 的用法。",
               [("count on", "依靠、指望"), ("there for you", "在你身边支持你")])},
    {"theme": "寒暄闲聊 Small talk",
     "vocab": [("How's it going?", "最近怎么样？", "Hey, how's it going?"),
                ("What have you been up to?", "最近在忙什么？", "What have you been up to lately?"),
                ("catch up", "叙旧/聊近况", "Let's catch up over coffee."),
                ("by the way", "顺便说一下", "By the way, did you see the news?"),
                ("I'd better get going", "我该走了", "I'd better get going. Talk soon!")],
     "shadow": [("How was your weekend?", "你周末过得怎么样？"),
                 ("Pretty good, thanks. How about you?", "挺好的，谢谢。你呢？"),
                 ("We should grab lunch sometime.", "我们改天一起吃个午饭吧。")],
     "song": ("Lemon Tree", "Fool's Garden", "★☆☆ 易/适中", "节奏稳、重复多，副歌好记；练习日常叙述。",
               [("I wonder", "我想知道/纳闷"), ("sitting here", "坐在这里")])},
    {"theme": "会议开场 Meetings – opening",
     "vocab": [("Let's get started", "我们开始吧", "Okay, let's get started."),
                ("on the agenda", "议程上", "First on the agenda is the budget."),
                ("go over", "过一遍/回顾", "Let's go over the main points."),
                ("make sure", "确保", "Let's make sure everyone is on the same page."),
                ("any questions", "有问题吗", "Any questions before we move on?")],
     "shadow": [("Thanks everyone for joining today.", "谢谢大家今天参加。"),
                 ("Let's keep this meeting short.", "我们把会议开短一点。"),
                 ("Can everyone hear me okay?", "大家能听清我说话吗？")],
     "song": ("You Are My Sunshine", "Classic", "★☆☆ 易/慢", "超经典、极慢极清晰，发音入门首选。",
               [("make me happy", "让我开心"), ("don't take ... away", "别把……带走")])},
    {"theme": "表达意见 Giving opinions",
     "vocab": [("In my opinion", "在我看来", "In my opinion, we should wait."),
                ("I think / I believe", "我认为", "I believe this is the best option."),
                ("from my point of view", "从我的角度看", "From my point of view, it's risky."),
                ("I'm not sure about", "我不太确定", "I'm not sure about the timeline."),
                ("That makes sense", "有道理", "That makes sense to me.")],
     "shadow": [("I see your point, but I disagree.", "我理解你的意思，但我不同意。"),
                 ("Could you explain that a bit more?", "你能再解释一下吗？"),
                 ("Let me think about it.", "让我想一想。")],
     "song": ("Take Me Home, Country Roads", "John Denver", "★★☆ 适中", "咬字清楚、画面感强，练连读和语调。",
               [("take me home", "带我回家"), ("belong", "属于")])},
    {"theme": "线上会议/电话 Calls",
     "vocab": [("You're on mute", "你静音了", "I think you're on mute."),
                ("break up", "信号断续", "Sorry, you're breaking up."),
                ("share my screen", "共享屏幕", "Let me share my screen."),
                ("drop off", "掉线", "I might drop off, bad connection."),
                ("talk you through", "带你过一遍", "I'll talk you through the slides.")],
     "shadow": [("Can you see my screen now?", "现在能看到我的屏幕吗？"),
                 ("Let's take this offline.", "这个我们会后再谈。"),
                 ("I'll follow up by email.", "我会邮件跟进。")],
     "song": ("Big Big World", "Emilia", "★☆☆ 易/慢", "慢速清晰、情感简单，副歌极好跟。",
               [("big big world", "大大的世界"), ("miss you", "想念你")])},
    {"theme": "邮件常用语 Email",
     "vocab": [("I hope this finds you well", "希望你一切都好(开头语)", "Hi John, I hope this email finds you well."),
                ("following up on", "跟进……", "I'm following up on my last email."),
                ("Please let me know", "请告知我", "Please let me know if you have questions."),
                ("attached", "附件", "Please see the attached file."),
                ("Looking forward to", "期待", "Looking forward to your reply.")],
     "shadow": [("Thanks for getting back to me.", "谢谢你回复我。"),
                 ("Just a quick reminder about tomorrow.", "简单提醒一下明天的事。"),
                 ("Let me know what works for you.", "你方便的话告诉我。")],
     "song": ("Yesterday Once More", "Carpenters", "★★☆ 适中", "经典老歌，发音标准，练优美语调。",
               [("those were ...", "那时候是……"), ("sing along", "一起唱")])},
    {"theme": "餐厅点餐 Restaurant",
     "vocab": [("a table for two", "两人桌", "Hi, a table for two, please."),
                ("What do you recommend?", "有什么推荐？", "What do you recommend here?"),
                ("I'll have ...", "我要……", "I'll have the chicken salad."),
                ("Could we get the bill?", "可以买单吗？", "Could we get the bill, please?"),
                ("to go / takeaway", "打包带走", "Can I get this to go?")],
     "shadow": [("Could I see the menu, please?", "可以看一下菜单吗？"),
                 ("Is this dish spicy?", "这道菜辣吗？"),
                 ("Everything was delicious, thank you.", "都很好吃，谢谢。")],
     "song": ("I'm Yours", "Jason Mraz", "★★☆ 适中", "轻松愉快、口语化，练自然连读。",
               [("I'm yours", "我是你的"), ("open up", "敞开心扉")])},
    {"theme": "购物 Shopping",
     "vocab": [("I'm just looking", "我随便看看", "Thanks, I'm just looking."),
                ("Do you have this in ...", "有……(颜色/尺码)的吗", "Do you have this in a medium?"),
                ("try it on", "试穿", "Can I try it on?"),
                ("on sale", "打折", "Is this on sale?"),
                ("refund / exchange", "退款/换货", "Can I get a refund?")],
     "shadow": [("How much is this?", "这个多少钱？"),
                 ("Do you take credit cards?", "可以刷信用卡吗？"),
                 ("It's a bit too expensive for me.", "对我来说有点贵。")],
     "song": ("Pretty Boy", "M2M", "★★☆ 适中", "女声清亮、慢速，适合练元音。",
               [("pretty boy", "帅气男孩"), ("in my mind", "在我脑海里")])},
    {"theme": "问路出行 Directions",
     "vocab": [("How do I get to ...", "怎么去……", "How do I get to the station?"),
                ("go straight", "直走", "Go straight for two blocks."),
                ("turn left / right", "左转/右转", "Turn left at the corner."),
                ("How far is it?", "有多远？", "How far is it from here?"),
                ("on foot", "步行", "Is it within walking distance?")],
     "shadow": [("Excuse me, is this the way to downtown?", "打扰一下，这是去市中心的路吗？"),
                 ("Could you show me on the map?", "能在地图上指给我看吗？"),
                 ("I think I'm lost.", "我好像迷路了。")],
     "song": ("Rhythm of the Rain", "The Cascades", "★★☆ 适中", "吐字清晰的经典，练句子节奏。",
               [("rhythm of the rain", "雨的节奏"), ("telling me", "告诉我")])},
    {"theme": "机场酒店 Airport & Hotel",
     "vocab": [("check in / check out", "登记入住/退房", "I'd like to check in, please."),
                ("boarding pass", "登机牌", "Here's my boarding pass."),
                ("Is breakfast included?", "含早餐吗", "Is breakfast included?"),
                ("a wake-up call", "叫醒服务", "Could I get a wake-up call at seven?"),
                ("delayed", "延误", "My flight is delayed.")],
     "shadow": [("I have a reservation under Yue.", "我用 Yue 这个名字订了房。"),
                 ("Where is the baggage claim?", "行李提取处在哪？"),
                 ("Could I have a late checkout?", "可以延迟退房吗？")],
     "song": ("Leaving on a Jet Plane", "John Denver", "★★☆ 适中", "慢而清晰，和出行主题呼应。",
               [("leaving", "离开"), ("don't know when", "不知道何时")])},
    {"theme": "项目进展 Project updates",
     "vocab": [("on track", "按计划进行", "The project is on track."),
                ("behind schedule", "落后于计划", "We're a bit behind schedule."),
                ("blocker", "阻碍/卡点", "We have one blocker to solve."),
                ("deadline", "截止期限", "The deadline is Friday."),
                ("wrap up", "收尾/完成", "We'll wrap it up this week.")],
     "shadow": [("Here's a quick update on the project.", "简单汇报一下项目进展。"),
                 ("We're making good progress.", "我们进展顺利。"),
                 ("We need another day or two.", "我们还需要一两天。")],
     "song": ("Right Here Waiting", "Richard Marx", "★★☆ 适中", "标准发音经典情歌，练长句语调。",
               [("right here waiting", "就在这里等你"), ("wherever you go", "无论你去哪")])},
    {"theme": "请求与帮助 Requests",
     "vocab": [("Could you ...?", "你能……吗(礼貌)", "Could you help me with this?"),
                ("Would you mind ...", "你介意……吗", "Would you mind closing the door?"),
                ("I was wondering if", "我想问一下是否", "I was wondering if you could help."),
                ("give me a hand", "帮我一把", "Can you give me a hand?"),
                ("no problem", "没问题", "Sure, no problem.")],
     "shadow": [("Could you do me a favor?", "能帮我个忙吗？"),
                 ("I'd really appreciate it.", "我会非常感激。"),
                 ("Let me know if you need anything.", "需要什么就告诉我。")],
     "song": ("Lean on Me", "Bill Withers", "★★☆ 适中", "主题就是互相帮助，副歌清晰好记。",
               [("lean on me", "依靠我"), ("carry on", "坚持下去")])},
    {"theme": "同意与反对 Agree / Disagree",
     "vocab": [("I totally agree", "我完全同意", "I totally agree with you."),
                ("I'm afraid I disagree", "恐怕我不同意", "I'm afraid I disagree."),
                ("good point", "说得好", "That's a good point."),
                ("on the other hand", "另一方面", "On the other hand, it costs more."),
                ("let's compromise", "我们折中一下", "Let's find a compromise.")],
     "shadow": [("I see what you mean.", "我明白你的意思。"),
                 ("I'm not so sure about that.", "这个我不太确定。"),
                 ("Let's agree to disagree.", "我们保留各自意见吧。")],
     "song": ("Hey Jude", "The Beatles", "★★☆ 适中", "国民级经典，副歌极易跟唱，练发声。",
               [("don't be afraid", "别害怕"), ("make it better", "让它变好")])},
    {"theme": "客服电话 Customer service",
     "vocab": [("I'd like to report ...", "我想反映……", "I'd like to report a problem."),
                ("It's not working", "用不了/坏了", "My account isn't working."),
                ("put you on hold", "让您稍等", "Let me put you on hold."),
                ("get back to you", "回复你", "I'll get back to you shortly."),
                ("sort it out", "解决它", "We'll sort it out for you.")],
     "shadow": [("I'm calling about my order.", "我打电话是关于我的订单。"),
                 ("Could you check that for me?", "能帮我查一下吗？"),
                 ("Thank you for your patience.", "谢谢你的耐心。")],
     "song": ("Perfect", "Ed Sheeran", "★★☆ 适中", "旋律优美、吐字清楚，练情感语调。",
               [("perfect", "完美的"), ("hold ... in my arms", "拥你入怀")])},
    {"theme": "描述工作 Your job",
     "vocab": [("My day-to-day", "我的日常工作", "My day-to-day is mostly coding."),
                ("deal with", "处理/应对", "I deal with client requests."),
                ("report to", "向……汇报", "I report to the team lead."),
                ("deadline-driven", "以截止期为导向", "It's a deadline-driven role."),
                ("work-life balance", "工作生活平衡", "I value work-life balance.")],
     "shadow": [("What does your job involve?", "你的工作主要做什么？"),
                 ("I handle the data pipeline.", "我负责数据管道。"),
                 ("It can get pretty busy.", "有时会挺忙的。")],
     "song": ("9 to 5", "Dolly Parton", "★★☆ 适中", "主题就是上班，欢快好记，练节奏。",
               [("9 to 5", "朝九晚五"), ("make a living", "谋生")])},
    {"theme": "时间日程 Scheduling",
     "vocab": [("Are you free ...?", "你……有空吗", "Are you free on Monday?"),
                ("set up a meeting", "安排会议", "Let's set up a meeting."),
                ("push back", "推迟", "Can we push it back an hour?"),
                ("reschedule", "改期", "I need to reschedule."),
                ("works for me", "我可以/合适", "Tuesday works for me.")],
     "shadow": [("Does ten o'clock work for you?", "十点你方便吗？"),
                 ("Let's move it to the afternoon.", "我们挪到下午吧。"),
                 ("I'm fully booked today.", "我今天排满了。")],
     "song": ("Time After Time", "Cyndi Lauper", "★★☆ 适中", "慢速清晰经典，练元音和连读。",
               [("time after time", "一次又一次"), ("I'll be waiting", "我会等着")])},
    {"theme": "天气与心情 Weather & feelings",
     "vocab": [("It's pouring", "下大雨", "It's pouring outside."),
                ("freezing / boiling", "极冷/极热", "It's freezing today."),
                ("I'm exhausted", "我累坏了", "I'm exhausted after work."),
                ("in a good mood", "心情好", "I'm in a good mood today."),
                ("cheer up", "振作/开心点", "Cheer up, it'll be fine.")],
     "shadow": [("What's the weather like today?", "今天天气怎么样？"),
                 ("I'm feeling a bit under the weather.", "我有点不舒服。"),
                 ("Have a great day!", "祝你今天愉快！")],
     "song": ("Here Comes the Sun", "The Beatles", "★★☆ 适中", "明亮温暖，吐字清晰，练轻快语调。",
               [("here comes the sun", "太阳出来了"), ("it's all right", "一切都好")])},
    {"theme": "兴趣爱好 Hobbies",
     "vocab": [("I'm into ...", "我喜欢/热衷于", "I'm into photography."),
                ("in my free time", "空闲时间", "In my free time I read."),
                ("get into", "开始喜欢上", "I got into running last year."),
                ("not really my thing", "不太合我胃口", "Golf is not really my thing."),
                ("give it a try", "试一试", "You should give it a try.")],
     "shadow": [("What do you like to do for fun?", "你平时喜欢做什么？"),
                 ("I usually work out on weekends.", "我周末通常健身。"),
                 ("That sounds like fun!", "听起来很有意思！")],
     "song": ("Lucky", "Jason Mraz & Colbie Caillat", "★★☆ 适中", "男女对唱、轻松清晰，适合跟读对话感。",
               [("lucky", "幸运的"), ("best friend", "最好的朋友")])},
    {"theme": "谈判与价格 Negotiation",
     "vocab": [("What's your budget?", "你的预算是多少", "What's your budget for this?"),
                ("meet halfway", "各让一步", "Let's meet halfway."),
                ("a better deal", "更优惠", "Can you give me a better deal?"),
                ("in that case", "那样的话", "In that case, we agree."),
                ("deal", "成交", "Okay, deal!")],
     "shadow": [("Is there any room for negotiation?", "价格还有商量余地吗？"),
                 ("That's a bit out of our range.", "这有点超出我们的范围。"),
                 ("Let's see what we can do.", "我们看看能怎么办。")],
     "song": ("Shallow", "Lady Gaga & Bradley Cooper", "★★★ 稍难", "情感强烈，练强弱和爆发音。",
               [("shallow", "肤浅的"), ("far from", "远离")])},
    {"theme": "汇报总结 Reporting",
     "vocab": [("To sum up", "总结一下", "To sum up, we're on track."),
                ("the key takeaway", "关键要点", "The key takeaway is simple."),
                ("in a nutshell", "简而言之", "In a nutshell, it works."),
                ("moving forward", "接下来", "Moving forward, we'll test it."),
                ("action items", "待办事项", "Here are the action items.")],
     "shadow": [("Let me summarize the main points.", "我来总结一下要点。"),
                 ("That's all from me.", "我这边就这些。"),
                 ("Does that cover everything?", "这样都讲到了吗？")],
     "song": ("Fix You", "Coldplay", "★★★ 稍难", "由慢到强，练气息和情感；副歌经典。",
               [("fix you", "治愈你"), ("lights will guide", "灯光会指引")])},
    {"theme": "科技与网络 Tech",
     "vocab": [("log in / sign up", "登录/注册", "You need to log in first."),
                ("the app crashed", "应用崩溃了", "The app just crashed."),
                ("back up", "备份", "Did you back up your files?"),
                ("update", "更新", "Please update the software."),
                ("user-friendly", "易用的", "The tool is very user-friendly.")],
     "shadow": [("My Wi-Fi keeps dropping.", "我的 Wi-Fi 老是断。"),
                 ("Have you tried restarting it?", "你试过重启吗？"),
                 ("It should work now.", "现在应该可以了。")],
     "song": ("Viva La Vida", "Coldplay", "★★★ 稍难", "节奏感强、句子长，练流利度(进阶)。",
               [("used to rule", "曾经统治"), ("I hear", "我听见")])},
    {"theme": "健康看病 Health",
     "vocab": [("I don't feel well", "我不舒服", "I don't feel well today."),
                ("have a headache", "头疼", "I have a bad headache."),
                ("see a doctor", "去看医生", "You should see a doctor."),
                ("take some rest", "休息一下", "Take some rest and drink water."),
                ("get well soon", "早日康复", "Get well soon!")],
     "shadow": [("I think I'm coming down with a cold.", "我好像要感冒了。"),
                 ("How long have you felt this way?", "你这样多久了？"),
                 ("Take care of yourself.", "照顾好自己。")],
     "song": ("Stand by Me", "Ben E. King", "★★☆ 适中", "经典、慢、重复多，强烈推荐跟唱。",
               [("stand by me", "支持我/陪着我"), ("won't be afraid", "不会害怕")])},
    {"theme": "鼓励与情绪 Encouragement",
     "vocab": [("You can do it", "你可以的", "Come on, you can do it!"),
                ("Don't give up", "别放弃", "Don't give up now."),
                ("Hang in there", "坚持住", "Hang in there, almost done."),
                ("I'm proud of you", "我为你骄傲", "I'm so proud of you."),
                ("It's gonna be okay", "会没事的", "Relax, it's gonna be okay.")],
     "shadow": [("Everything will work out.", "一切都会好起来的。"),
                 ("You did a great job.", "你做得很好。"),
                 ("Believe in yourself.", "相信你自己。")],
     "song": ("Hall of Fame", "The Script", "★★★ 稍难", "励志、节奏明快，练重音和气势。",
               [("hall of fame", "名人堂"), ("you can be", "你可以成为")])},
    {"theme": "道歉与感谢 Apology & Thanks",
     "vocab": [("I'm so sorry", "非常抱歉", "I'm so sorry about that."),
                ("My apologies", "我道歉(正式)", "My apologies for the delay."),
                ("It won't happen again", "不会再发生", "It won't happen again."),
                ("I really appreciate it", "我很感激", "I really appreciate your help."),
                ("You're welcome", "不客气", "You're welcome, anytime.")],
     "shadow": [("Sorry to keep you waiting.", "抱歉让你久等了。"),
                 ("Thanks a lot for your support.", "非常感谢你的支持。"),
                 ("I owe you one.", "我欠你一个人情。")],
     "song": ("Thank You", "Dido", "★★☆ 适中", "温柔清晰，主题感恩，练平稳语调。",
               [("thank you", "谢谢你"), ("the best day", "最好的一天")])},
    {"theme": "面试 Interview",
     "vocab": [("Tell me about yourself", "介绍一下你自己", "Tell me about yourself."),
                ("my strengths", "我的优势", "One of my strengths is teamwork."),
                ("deal with pressure", "应对压力", "I deal with pressure well."),
                ("looking for", "寻求", "I'm looking for new challenges."),
                ("Do you have any questions?", "你有问题吗", "Do you have any questions for us?")],
     "shadow": [("Why do you want this job?", "你为什么想要这份工作？"),
                 ("I'm a quick learner.", "我学东西很快。"),
                 ("Thank you for your time.", "谢谢你抽时间。")],
     "song": ("Firework", "Katy Perry", "★★★ 稍难", "励志、高潮强，练发声和自信语气。",
               [("firework", "烟花"), ("let it shine", "让它绽放")])},
    {"theme": "团队协作 Teamwork",
     "vocab": [("on the same page", "达成共识", "Let's get on the same page."),
                ("divide the work", "分工", "Let's divide the work."),
                ("count me in", "算我一个", "Count me in."),
                ("take the lead", "带头负责", "Can you take the lead on this?"),
                ("back each other up", "互相支持", "We back each other up.")],
     "shadow": [("Let's work on this together.", "我们一起来做这个。"),
                 ("Who wants to take this one?", "谁来负责这个？"),
                 ("Great teamwork, everyone!", "大家配合得真好！")],
     "song": ("We Are the Champions", "Queen", "★★★ 稍难", "气势磅礴，副歌经典，练长音和情感。",
               [("champions", "冠军"), ("keep on fighting", "继续奋斗")])},
    {"theme": "解决问题 Problem solving",
     "vocab": [("figure out", "弄清楚/想出", "Let's figure out the cause."),
                ("come up with", "想出(主意)", "Can you come up with a plan?"),
                ("the root cause", "根本原因", "What's the root cause?"),
                ("work around", "绕开/变通", "We found a work-around."),
                ("keep an eye on", "留意/盯着", "Let's keep an eye on it.")],
     "shadow": [("What's the best way to handle this?", "处理这个最好的办法是什么？"),
                 ("Let's break it down step by step.", "我们一步步拆解。"),
                 ("That should fix the issue.", "那应该能解决问题。")],
     "song": ("Don't Stop Me Now", "Queen", "★★★ 稍难", "欢快快节奏，练流利和连读(进阶)。",
               [("don't stop me", "别拦我"), ("having a good time", "玩得开心")])},
    {"theme": "计划与目标 Plans & goals",
     "vocab": [("set a goal", "设定目标", "I set a goal for this year."),
                ("stick to", "坚持", "I'll stick to my plan."),
                ("step by step", "一步步", "Let's do it step by step."),
                ("in the long run", "从长远看", "In the long run, it pays off."),
                ("make it a habit", "养成习惯", "Make it a daily habit.")],
     "shadow": [("What's your plan for this year?", "你今年有什么计划？"),
                 ("I want to improve my English.", "我想提升我的英语。"),
                 ("Little by little, it adds up.", "积少成多。")],
     "song": ("The Climb", "Miley Cyrus", "★★★ 稍难", "励志、主题就是坚持，练情感递进。",
               [("the climb", "攀登的过程"), ("keep moving", "继续前进")])},
    {"theme": "周末与文化 Weekend & culture",
     "vocab": [("hang out", "一起玩", "Let's hang out this weekend."),
                ("grab a drink", "喝一杯", "Want to grab a drink?"),
                ("chill / relax", "放松", "I just want to chill today."),
                ("What's it like ...", "……是什么样的", "What's it like living abroad?"),
                ("look forward to", "期待", "I look forward to the trip.")],
     "shadow": [("Any plans for the weekend?", "周末有什么安排吗？"),
                 ("We're thinking of going hiking.", "我们想去徒步。"),
                 ("Let's make it happen.", "那就定了/说干就干。")],
     "song": ("Riptide", "Vance Joy", "★★★ 稍难", "口语化、俚语多，练自然语流(进阶)。",
               [("riptide", "激流/离岸流"), ("take me", "带我走")])},
    {"theme": "复习与自由表达 Review & free talk",
     "vocab": [("in other words", "换句话说", "In other words, we agree."),
                ("to be honest", "老实说", "To be honest, I'm not sure."),
                ("the thing is", "问题是/其实", "The thing is, we're short on time."),
                ("as far as I know", "据我所知", "As far as I know, it's fine."),
                ("let's keep in touch", "保持联系", "Let's keep in touch!")],
     "shadow": [("Let me put it another way.", "我换个说法。"),
                 ("That's a good question.", "这是个好问题。"),
                 ("I'll talk to you soon.", "回头聊。")],
     "song": ("What a Wonderful World", "Louis Armstrong", "★★☆ 适中", "极慢极清晰的经典收官，练优美语调。",
               [("wonderful world", "美好的世界"), ("I see", "我看见")])},
]

# 进阶内容（与 DAYS 一一对应）：每天 短文(en,zh) + 重点表达 + 小测验 + 翻译练习
# quiz 结构: (题干, [选项A..D], 正确项下标(0起), 解析)
# translate 结构: (中文, 参考英文)
ENRICH = [
    {  # Day 1 自我介绍
     "passage": ("Whenever I meet new colleagues, I try to come across as approachable rather than formal. "
                 "I usually mention my role, what I'm currently working on, and one thing I genuinely enjoy outside of work. "
                 "Striking that balance helps people remember me without feeling like they've just read my resume. "
                 "Over the years, I've learned that a warm, concise introduction often opens more doors than a long, impressive one.",
                 "每次见到新同事，我都尽量让自己显得平易近人，而不是一本正经。我通常会说一下我的岗位、目前在做什么，"
                 "以及一件工作之外我真正喜欢的事。把握好这个分寸，能让别人记住我，又不会觉得像在听我念简历。"
                 "这些年我体会到，一个热情而简洁的自我介绍，往往比冗长而'高大上'的介绍更能打开局面。"),
     "pkey": [("come across as", "给人……的印象"), ("strike a balance", "把握分寸/取得平衡"), ("open doors", "带来机会")],
     "quiz": [("In the passage, 'come across as approachable' most nearly means ___.",
               ["to walk toward someone", "to give the impression of being easy to talk to", "to solve a hard problem", "to cross a road"],
               1, "come across as = 给人留下某种印象；approachable = 平易近人。"),
              ("The writer believes a good introduction is ___.",
               ["long and impressive", "warm and concise", "formal and detailed", "mostly about past jobs"],
               1, "文中说 warm, concise introduction 往往更能打开局面。")],
     "translate": [("第一次见客户时，我尽量显得专业又不失亲和。", "When I meet a client for the first time, I try to come across as professional yet approachable."),
                   ("简短的自我介绍往往比冗长的更有效。", "A short self-introduction is often more effective than a long one.")]},
    {  # Day 2 寒暄闲聊
     "passage": ("Small talk gets a bad reputation, but it's actually the glue that holds workplace relationships together. "
                 "A quick chat about the weekend or a shared frustration with traffic can break the ice before a tense meeting. "
                 "The trick is to keep it light, ask open-ended questions, and genuinely listen instead of waiting for your turn to speak. "
                 "Done well, small talk makes people feel seen, and that goodwill tends to pay off down the line.",
                 "闲聊常被人看不起，但它其实是维系职场关系的粘合剂。聊两句周末，或一起吐槽堵车，就能在紧张的会议前打破僵局。"
                 "诀窍是：保持轻松、多问开放式问题、真心去听，而不是等着轮到自己说。做得好的话，闲聊能让人感到被重视，"
                 "而这份善意往往会在日后得到回报。"),
     "pkey": [("break the ice", "打破僵局"), ("open-ended question", "开放式问题"), ("pay off", "有回报"), ("down the line", "日后/将来")],
     "quiz": [("'Break the ice' in the passage means ___.",
               ["to crush ice", "to ease the initial tension between people", "to start an argument", "to end a meeting"],
               1, "break the ice = 打破僵局、缓解尴尬。"),
              ("The writer suggests that during small talk you should ___.",
               ["talk as much as possible", "wait for your turn to speak", "genuinely listen", "avoid eye contact"],
               2, "文中强调 genuinely listen（真心倾听）。")],
     "translate": [("闲聊听起来没用，其实能拉近同事之间的距离。", "Small talk may sound useless, but it actually brings colleagues closer."),
                   ("开会前聊两句天气能缓解紧张气氛。", "A quick chat about the weather before a meeting can ease the tension.")]},
    {  # Day 3 会议开场
     "passage": ("A well-run meeting starts before anyone says a word. The organizer sets a clear agenda, shares it in advance, "
                 "and sticks to the allotted time. At the opening, it helps to remind everyone of the goal so the discussion doesn't drift. "
                 "Nothing kills momentum faster than a meeting that could have been an email, so if there's no real decision to make, "
                 "it's worth asking whether the meeting is needed at all.",
                 "一场高效的会议，在有人开口之前就已经开始了。组织者会定好清晰的议程、提前分享，并严格控制时间。"
                 "开场时，提醒大家本次目标很有帮助，这样讨论就不会跑偏。最打击效率的，莫过于一场本可以用邮件解决的会；"
                 "所以如果没有真正要拍板的事，不妨先问问这个会到底有没有必要开。"),
     "pkey": [("set an agenda", "制定议程"), ("stick to", "坚持/遵守"), ("drift", "跑偏/漫无目的"), ("kill momentum", "打击势头/效率")],
     "quiz": [("According to the passage, a meeting should be questioned when ___.",
               ["it has an agenda", "there is no real decision to make", "it starts on time", "the organizer is prepared"],
               1, "没有真正要决策的事，就该质疑这个会是否必要。"),
              ("'The discussion doesn't drift' means the discussion ___.",
               ["stays on topic", "becomes louder", "ends early", "moves online"],
               0, "drift = 跑题；doesn't drift = 不跑题。")],
     "translate": [("请提前把议程发给大家，这样会议才不会跑偏。", "Please share the agenda in advance so the meeting won't drift off topic."),
                   ("如果没有要决定的事，这个会其实可以用邮件代替。", "If there's nothing to decide, this meeting could actually have been an email.")]},
    {  # Day 4 表达意见
     "passage": ("Sharing an opinion at work is a bit of an art. You want to sound confident without coming off as arrogant, "
                 "and open-minded without seeming wishy-washy. A useful approach is to state your view, back it up with one concrete reason, "
                 "and then invite others to push back. That way you own your position but leave room for a better idea. "
                 "People respect those who can disagree without being disagreeable.",
                 "在职场里发表意见是门艺术。你希望显得自信，但又不至于傲慢；显得开放，但又不至于没主见。"
                 "一个好用的方法是：先亮明观点，用一个具体理由支撑，再邀请别人反驳。这样你既坚持了立场，又给更好的想法留了余地。"
                 "能做到'对事不对人地反对'的人，最受人尊重。"),
     "pkey": [("come off as", "显得/给人……印象"), ("back up", "支撑/佐证"), ("push back", "反驳/提出异议"), ("leave room for", "留余地")],
     "quiz": [("'Wishy-washy' in the passage describes someone who is ___.",
               ["too confident", "lacking a firm opinion", "very aggressive", "highly skilled"],
               1, "wishy-washy = 没主见、模棱两可。"),
              ("The recommended approach is to state your view and then ___.",
               ["refuse all criticism", "invite others to push back", "change the subject", "repeat it louder"],
               1, "文中建议邀请别人反驳（invite push back）。")],
     "translate": [("我想表达自己的看法，但不想显得咄咄逼人。", "I want to share my opinion without coming off as aggressive."),
                   ("请用一个具体的理由来支撑你的观点。", "Please back up your point with one concrete reason.")]},
    {  # Day 5 线上会议/电话
     "passage": ("Remote calls have their own set of unwritten rules. Mute yourself when you're not speaking, let people finish before jumping in, "
                 "and resist the urge to multitask -- everyone can tell when you've checked out. If the connection drops or people are talking over "
                 "each other, a quick 'go ahead' keeps things civil. And when the discussion gets complicated, it's often faster to take it offline "
                 "and sort out the details one-on-one.",
                 "远程通话有一套自己的潜规则。不说话时静音、等别人说完再插话、克制一心多用的冲动——你有没有走神，大家其实都看得出来。"
                 "如果信号断了，或者大家抢着说话，一句'你先说'就能维持礼貌。而当讨论变得复杂时，往往会后单独沟通、把细节捋清楚会更快。"),
     "pkey": [("jump in", "插话/加入"), ("check out", "(注意力)走神/神游"), ("talk over each other", "抢着说/互相打断"), ("take it offline", "会后(私下)再谈")],
     "quiz": [("'When you've checked out' here means you have ___.",
               ["left the building", "stopped paying attention", "paid a bill", "logged out"],
               1, "check out（口语）= 走神、不在状态。"),
              ("For complicated discussions, the passage suggests you ___.",
               ["talk over each other", "take it offline", "stay muted forever", "multitask"],
               1, "复杂讨论建议 take it offline（会后单独谈）。")],
     "translate": [("不说话的时候请把自己静音。", "Please mute yourself when you're not speaking."),
                   ("这个问题有点复杂，我们会后单独聊吧。", "This issue is a bit complicated; let's take it offline.")]},
    {  # Day 6 邮件
     "passage": ("A good work email respects the reader's time. Lead with the point instead of burying it in the third paragraph, "
                 "keep each message to a single topic, and make any request crystal clear -- what you need, and by when. "
                 "A polite tone costs nothing, but vague wording can trigger a long back-and-forth that a single clear sentence would have avoided. "
                 "Before hitting send, I skim it once as if I were the one receiving it.",
                 "一封好的工作邮件懂得尊重读者的时间。把重点放在开头，而不是埋在第三段；每封邮件只讲一件事；"
                 "任何请求都写得清清楚楚——你要什么、什么时候要。礼貌的语气不花一分钱，而含糊的措辞却可能引发一长串来回，"
                 "而这本可以用一句话说清楚就避免。点发送之前，我会站在收件人的角度再快速扫一遍。"),
     "pkey": [("lead with", "以……开头/先说"), ("bury", "埋没/藏起"), ("back-and-forth", "来回沟通/反复"), ("hit send", "点击发送")],
     "quiz": [("'Bury it in the third paragraph' means the point is ___.",
               ["emphasized", "hidden and hard to find", "deleted", "translated"],
               1, "bury = 埋没，使之不易被发现。"),
              ("The writer re-reads the email before sending to ___.",
               ["add more words", "check it from the reader's perspective", "make it longer", "delete the subject line"],
               1, "站在收件人角度再读一遍。")],
     "translate": [("请在邮件开头就说明你的请求。", "Please state your request at the very beginning of the email."),
                   ("含糊的措辞会导致很多来回沟通。", "Vague wording can lead to a lot of back-and-forth.")]},
    {  # Day 7 餐厅
     "passage": ("Eating out in an English-speaking country can be surprisingly stressful the first time. The waiter rattles off the specials, "
                 "asks how you'd like your steak cooked, and suddenly you're expected to decide on the spot. My advice is to slow things down: "
                 "it's perfectly fine to ask for a recommendation, to check whether a dish is spicy, or to request a minute to look over the menu. "
                 "Nobody minds, and a friendly 'What would you suggest?' usually gets you the best dish on the menu.",
                 "第一次在英语国家下馆子，可能会紧张得出乎意料。服务员飞快地报出今日特色、问你牛排要几分熟，突然就得当场拿主意。"
                 "我的建议是：把节奏放慢——完全可以请对方推荐、问问某道菜辣不辣，或者要求再看一会儿菜单。没人会介意，"
                 "而一句友好的'你有什么推荐？'通常能帮你点到菜单上最好吃的那道。"),
     "pkey": [("eat out", "下馆子/外出就餐"), ("rattle off", "飞快地一口气说出"), ("on the spot", "当场"), ("look over", "浏览/过目")],
     "quiz": [("'The waiter rattles off the specials' means the waiter ___.",
               ["forgets the specials", "lists them quickly", "writes them down", "cooks them"],
               1, "rattle off = 飞快地一口气说出。"),
              ("According to the passage, asking for a recommendation is ___.",
               ["rude", "perfectly acceptable", "expensive", "not allowed"],
               1, "文中说 perfectly fine，没人会介意。")],
     "translate": [("请给我一点时间看一下菜单。", "Could you give me a minute to look over the menu?"),
                   ("这道菜很受欢迎，我强烈推荐。", "This dish is very popular; I'd highly recommend it.")]},
    {  # Day 8 购物
     "passage": ("Shopping in person still has its charms, even in the age of one-click delivery. You can feel the fabric, try things on, "
                 "and walk out with exactly what you wanted. The downside is the sales pressure -- some assistants hover the moment you step in. "
                 "A simple 'I'm just browsing, thanks' sets a boundary without being rude. And if something doesn't fit once you get home, "
                 "most shops are happy to offer a refund or an exchange, as long as you keep the receipt.",
                 "即便在'一键下单'的时代，逛实体店依然有它的乐趣。你能摸到面料、试穿衣服，然后拿着正合心意的东西走出门。"
                 "缺点是销售压力——有些导购在你一进门就寸步不离。一句简单的'我随便看看，谢谢'就能划清界限，又不失礼貌。"
                 "而如果回家后发现不合身，只要留着小票，大多数店都乐意退货或换货。"),
     "pkey": [("try on", "试穿"), ("hover", "(在旁)盘旋/寸步不离"), ("set a boundary", "划清界限/立规矩"), ("keep the receipt", "保留小票")],
     "quiz": [("'Some assistants hover the moment you step in' suggests they ___.",
               ["ignore customers", "stay very close to customers", "offer big discounts", "close the shop"],
               1, "hover = 在旁边盘旋、紧跟不放。"),
              ("A refund or exchange is usually possible as long as you ___.",
               ["pay cash", "keep the receipt", "buy more", "complain loudly"],
               1, "文中条件是 keep the receipt（留好小票）。")],
     "translate": [("谢谢，我先随便看看。", "Thanks, I'm just browsing for now."),
                   ("只要你留着小票，就可以退货。", "You can return it as long as you keep the receipt.")]},
    {  # Day 9 问路出行
     "passage": ("Even with a phone in everyone's pocket, knowing how to ask for and give directions is a lifesaver when the battery dies. "
                 "The key is to keep it simple: landmarks work better than street names, and 'turn left at the bakery' sticks in the mind "
                 "far better than 'head north for 200 meters.' If you're the one lost, don't be shy -- most people are happy to point you the right way, "
                 "and a quick 'Am I going the right way?' can save you a long detour.",
                 "即便人人口袋里都有手机，会问路、会指路在没电时依然能救命。关键是化繁为简：地标比街名好使，"
                 "'在面包店左转'远比'向北走 200 米'更容易记住。如果迷路的是你，别不好意思——大多数人都乐意给你指路，"
                 "而一句'我走对方向了吗？'往往能帮你省下一段冤枉路。"),
     "pkey": [("a lifesaver", "救命稻草/帮大忙的东西"), ("landmark", "地标"), ("stick in the mind", "容易记住"), ("detour", "绕路/弯路")],
     "quiz": [("The passage says landmarks work better than ___.",
               ["phones", "street names", "maps", "bakeries"],
               1, "landmarks（地标）比 street names（街名）好记。"),
              ("'Save you a long detour' means save you from ___.",
               ["a long meeting", "going a long wrong way", "spending money", "a phone call"],
               1, "detour = 绕路/冤枉路。")],
     "translate": [("请问去地铁站怎么走？", "Excuse me, how do I get to the subway station?"),
                   ("在红绿灯那里左转，就能看到了。", "Turn left at the traffic lights and you'll see it.")]},
    {  # Day 10 机场酒店
     "passage": ("Travel runs smoothly right up until it doesn't. Flights get delayed, bags go missing, and the room you booked turns out "
                 "to be nothing like the photos. A calm, polite traveler usually gets further than an angry one: staff are far more willing "
                 "to bend the rules for someone who treats them like a human being. Keep your booking details handy, learn a few key phrases, "
                 "and remember that 'Is there anything you can do?' often works better than a complaint.",
                 "旅行一路顺畅，直到它不顺畅为止。航班会延误、行李会丢、你订的房间可能和照片完全不是一回事。"
                 "一个冷静、礼貌的旅客通常比发火的人更能把事办成：对于把自己当人看的客人，工作人员要灵活通融得多。"
                 "随身带好订单信息、学几句关键用语，并记住：一句'您看有没有什么办法？'往往比抱怨更管用。"),
     "pkey": [("run smoothly", "顺利进行"), ("go missing", "丢失/不见"), ("bend the rules", "灵活变通/通融"), ("keep ... handy", "随身备好/放在手边")],
     "quiz": [("Staff are more willing to bend the rules for travelers who are ___.",
               ["angry", "polite and calm", "in a hurry", "famous"],
               1, "对礼貌冷静的人更愿意通融。"),
              ("'My bag went missing' means the bag ___.",
               ["was found", "was lost", "was heavy", "was cheap"],
               1, "go missing = 丢失/不见。")],
     "translate": [("我的航班延误了，我能改签吗？", "My flight is delayed; can I change it to another one?"),
                   ("我用 Yue 这个名字订了一间房。", "I have a reservation under the name Yue.")]},
    {  # Day 11 项目进展
     "passage": ("Giving a project update is less about listing everything you did and more about telling people what they actually need to know. "
                 "Lead with the status -- on track, at risk, or blocked -- then explain why in a sentence or two. If something is slipping, say so early; "
                 "nobody likes a surprise at the deadline. Flagging a blocker isn't a sign of weakness, it's how you give the team a chance to help "
                 "before a small problem turns into a crisis.",
                 "汇报项目进展，重点不在于把你做过的事一一罗列，而在于告诉大家他们真正需要知道的。"
                 "先说状态——按计划、有风险、还是被卡住——再用一两句话说明原因。如果有延误迹象，就趁早说出来；没人喜欢在截止日那天收到'惊喜'。"
                 "抛出一个卡点并不是示弱，而是在小问题演变成危机之前，给团队一个帮忙的机会。"),
     "pkey": [("on track / at risk / blocked", "按计划/有风险/被卡住"), ("slip", "延误/滑坡"), ("flag a blocker", "指出/标记卡点"), ("turn into", "演变成")],
     "quiz": [("The passage says a project update should lead with ___.",
               ["everything you did", "the status", "your opinion", "the budget"],
               1, "先说 status（状态）。"),
              ("Flagging a blocker early is described as ___.",
               ["a sign of weakness", "a way to get help", "a waste of time", "a complaint"],
               1, "抛卡点是让团队有机会帮忙，而非示弱。")],
     "translate": [("项目目前进展顺利，预计周五完成。", "The project is on track and should be done by Friday."),
                   ("我们遇到了一个卡点，需要大家帮忙。", "We've hit a blocker and need some help from the team.")]},
    {  # Day 12 请求与帮助
     "passage": ("There's a real skill to asking for help without feeling like a burden. Be specific about what you need, acknowledge that the "
                 "other person is busy, and give them an easy way to say no. 'Would you mind taking a look when you get a chance?' lands much better "
                 "than a vague 'Can you help me?' And when someone does lend a hand, a genuine thank-you -- ideally mentioning exactly what they did -- "
                 "goes a long way toward making them happy to help again.",
                 "开口求助又不让人觉得是负担，是一项真功夫。把需求说具体、体谅对方很忙、并给对方一个方便拒绝的台阶。"
                 "'你方便的时候能帮我看一眼吗？'远比含糊的'你能帮我吗？'更得体。而当有人真的伸出援手时，一句真诚的感谢——"
                 "最好点明他具体帮了什么——会让他下次更乐意再帮你。"),
     "pkey": [("a burden", "负担"), ("lend a hand", "搭把手/帮忙"), ("land better", "(说出来)效果更好/更得体"), ("go a long way", "大有帮助/很管用")],
     "quiz": [("A good request should give the other person ___.",
               ["no choice", "an easy way to say no", "extra work", "a strict deadline"],
               1, "给对方一个方便拒绝的余地。"),
              ("'Lend a hand' means to ___.",
               ["borrow money", "offer help", "shake hands", "wave goodbye"],
               1, "lend a hand = 帮忙、搭把手。")],
     "translate": [("你方便的时候能帮我看一下这份报告吗？", "Would you mind taking a look at this report when you get a chance?"),
                   ("非常感谢你昨天帮我解决了那个问题。", "Thank you so much for helping me solve that problem yesterday.")]},
    {  # Day 13 同意与反对
     "passage": ("Disagreeing well is one of the most underrated workplace skills. The goal isn't to win but to get to the best answer together, "
                 "so attack the idea, never the person. Acknowledge what's valid in the other view first -- 'You make a fair point about the cost' -- "
                 "and then introduce your concern. Phrases like 'I see it a little differently' soften the blow without hiding where you stand. "
                 "Handled this way, disagreement sparks better decisions instead of bruised egos.",
                 "会'好好地反对'，是职场里最被低估的能力之一。目标不是争赢，而是一起找到最优解，所以要'对事不对人'。"
                 "先认可对方观点中合理的部分——'你关于成本的担心很有道理'——再提出你的顾虑。像'我的看法略有不同'这样的说法，"
                 "能既缓和语气又不掩饰你的立场。这样处理，分歧激发的是更好的决策，而不是受伤的自尊。"),
     "pkey": [("underrated", "被低估的"), ("make a fair point", "说得有道理"), ("soften the blow", "缓和/减轻冲击"), ("where you stand", "你的立场")],
     "quiz": [("The passage advises you to attack the ___, not the ___.",
               ["person; idea", "idea; person", "cost; benefit", "past; future"],
               1, "对事（idea）不对人（person）。"),
              ("'Soften the blow' means to ___.",
               ["hit harder", "make something less harsh", "agree completely", "end the talk"],
               1, "soften the blow = 缓和冲击、减轻打击。")],
     "translate": [("你说得有道理，不过我的看法略有不同。", "You make a fair point, but I see it a little differently."),
                   ("我们的目标是找到最好的方案，而不是争输赢。", "Our goal is to find the best solution, not to win the argument.")]},
    {  # Day 14 客服电话
     "passage": ("Dealing with customer service tests everyone's patience, on both sides of the line. As a customer, you'll get further by explaining "
                 "the problem clearly and calmly than by venting your frustration at whoever picks up. State what happened, what you've already tried, "
                 "and what outcome you're hoping for. The person on the other end usually has limited power but plenty of goodwill, so treating them "
                 "as an ally rather than an enemy is often the fastest route to getting things sorted out.",
                 "和客服打交道，考验的是电话两端所有人的耐心。作为顾客，把问题讲清楚、讲冷静，比对着接电话的人发泄情绪更能把事办成。"
                 "说清楚发生了什么、你已经试过什么、你希望得到什么结果。电话那头的人通常权限有限，但善意满满，"
                 "所以把对方当盟友而不是敌人，往往是把事情解决掉的最快路径。"),
     "pkey": [("vent (frustration)", "发泄(不满)"), ("pick up", "接(电话)"), ("an ally", "盟友"), ("sort out", "解决/处理好")],
     "quiz": [("The passage suggests customers should ___ rather than vent frustration.",
               ["hang up", "explain calmly", "write a review", "demand a refund"],
               1, "冷静、清楚地说明问题。"),
              ("Treating the agent as an ally is described as the fastest way to ___.",
               ["get a discount", "get things sorted out", "end the call", "file a complaint"],
               1, "把对方当盟友 = 最快解决问题的路径。")],
     "translate": [("我想反映一个关于我订单的问题。", "I'd like to report a problem with my order."),
                   ("我已经重启过设备了，但还是不行。", "I've already restarted the device, but it still doesn't work.")]},
    {  # Day 15 描述工作
     "passage": ("When people ask what I do, I've learned to skip the job title and describe the problem I solve instead. "
                 "'I help teams turn messy data into decisions' tells you far more than 'data engineer' ever could. Every role has its ups and downs -- "
                 "mine involves long stretches of focus broken up by firefighting when something breaks. What keeps me going is seeing something "
                 "I built actually get used. That, and a boss who respects the line between work and life.",
                 "当别人问我是做什么的，我学会了跳过职称，转而描述我解决的问题。'我帮团队把杂乱的数据变成决策'，远比'数据工程师'更能说明问题。"
                 "每份工作都有起伏——我的工作就是长时间的专注，中间夹杂着东西一出故障就得救火。支撑我坚持下去的，是看到自己做的东西真的被人用上。"
                 "还有，一个尊重工作与生活界限的老板。"),
     "pkey": [("skip", "跳过/略过"), ("ups and downs", "起起伏伏"), ("firefighting", "救火/应急处理"), ("keep (sb) going", "支撑/让人坚持")],
     "quiz": [("Instead of a job title, the writer prefers to describe ___.",
               ["their salary", "the problem they solve", "their boss", "their office"],
               1, "描述自己解决的问题。"),
              ("'Firefighting' here refers to ___.",
               ["putting out real fires", "handling urgent problems", "a hobby", "a vacation"],
               1, "firefighting（比喻）= 救火、应急处理。")],
     "translate": [("我的工作主要是把数据变成有用的决策。", "My job is mainly about turning data into useful decisions."),
                   ("每份工作都有起有伏。", "Every job has its ups and downs.")]},
    {  # Day 16 时间日程
     "passage": ("Scheduling across busy calendars is a quiet negotiation. Offer two or three concrete time slots rather than the open-ended "
                 "'When are you free?', which just pushes the work back onto the other person. If you have to move a meeting, give as much notice "
                 "as you can and apologize briefly -- people are usually flexible if you don't make a habit of it. And always confirm the time zone; "
                 "nothing is more awkward than showing up to a call a full hour early or late.",
                 "在排得满满的日程之间约时间，是一场无声的谈判。给出两三个具体的时间段，而不是开放式的'你什么时候有空'——那只是把活儿又推回给对方。"
                 "如果不得不改约，尽量提前通知、简短道歉——只要你别养成习惯，大家通常都挺灵活。还有，务必确认时区；"
                 "没有什么比电话会早到或迟到整整一个小时更尴尬了。"),
     "pkey": [("time slot", "时间段"), ("open-ended", "开放式的/无限定的"), ("give notice", "提前通知"), ("make a habit of", "养成……的习惯")],
     "quiz": [("The passage recommends offering ___ instead of asking 'When are you free?'",
               ["no times", "two or three concrete slots", "a whole week", "nothing"],
               1, "给出具体的时间段。"),
              ("You should always confirm the ___ to avoid being an hour off.",
               ["price", "time zone", "location", "agenda"],
               1, "务必确认时区（time zone）。")],
     "translate": [("我周二上午或周三下午都可以，你看哪个方便？", "I'm free Tuesday morning or Wednesday afternoon -- which works for you?"),
                   ("抱歉，我需要把会议改到明天。", "Sorry, I need to reschedule the meeting to tomorrow.")]},
    {  # Day 17 天气与心情
     "passage": ("The weather is the world's safest conversation starter, but it's also a surprisingly honest mirror of our moods. "
                 "A grey, drizzly Monday can make even a light workload feel heavy, while the first sunny morning of spring puts a spring in "
                 "everyone's step. I've started paying attention to how much the forecast affects my energy, and on the gloomy days I make a point "
                 "of getting outside anyway. A short walk, rain or shine, almost always lifts my mood.",
                 "天气是全世界最安全的开场白，但它也出奇诚实地映照着我们的心情。阴沉、细雨的周一，能让再轻的工作量都显得沉重；"
                 "而春天第一个晴朗的早晨，则让每个人脚步都轻快起来。我开始留意天气预报对我精力的影响有多大，在阴郁的日子里，我会特意还是出门走走。"
                 "一段短短的散步，不论晴雨，几乎总能让我的心情好起来。"),
     "pkey": [("conversation starter", "开场话题"), ("drizzly", "细雨蒙蒙的"), ("a spring in one's step", "脚步轻快/精神好"), ("rain or shine", "无论晴雨")],
     "quiz": [("'Puts a spring in everyone's step' means it makes people ___.",
               ["tired", "energetic and cheerful", "wet", "late"],
               1, "a spring in one's step = 精神焕发、脚步轻快。"),
              ("On gloomy days, the writer makes a point of ___.",
               ["staying in bed", "getting outside anyway", "skipping work", "checking the forecast only"],
               1, "阴天也特意出门走走。")],
     "translate": [("今天阴沉沉的，我感觉有点没精神。", "It's gloomy today, and I feel a bit low on energy."),
                   ("不管晴天还是下雨，散步总能让我心情变好。", "Rain or shine, a walk always lifts my mood.")]},
    {  # Day 18 兴趣爱好
     "passage": ("Hobbies are easy to drop when work gets busy, which is exactly when we need them most. Mine shift with the seasons -- "
                 "running in summer, reading through the winter -- but the point is always the same: a few hours doing something with no deadline attached. "
                 "I'm not particularly good at any of them, and that's rather the point. There's a quiet freedom in doing something purely because "
                 "you enjoy it, with nobody keeping score.",
                 "一忙起来，爱好最容易被丢到一边，而那恰恰是我们最需要它的时候。我的爱好随季节更替——夏天跑步、冬天读书——但核心始终如一："
                 "花几个小时做一件不带任何截止日期的事。这些我哪样都算不上擅长，而这正是重点。纯粹因为喜欢而去做一件事、没有人在旁边记分，"
                 "这里面有一种安静的自由。"),
     "pkey": [("drop", "放下/放弃"), ("shift with", "随……变化"), ("keep score", "记分/计较"), ("deadline attached", "带着截止期限")],
     "quiz": [("The writer says we need hobbies most when ___.",
               ["we are on holiday", "work gets busy", "we are good at them", "we have no money"],
               1, "越忙越需要爱好。"),
              ("'Nobody keeping score' suggests the activity is ___.",
               ["a competition", "done purely for enjoyment", "work-related", "very expensive"],
               1, "没人记分 = 纯粹为享受而做。")],
     "translate": [("我最近迷上了跑步。", "I've recently gotten into running."),
                   ("做自己喜欢的事，不必在乎做得好不好。", "When you do something you enjoy, it doesn't matter how good you are at it.")]},
    {  # Day 19 谈判与价格
     "passage": ("Good negotiation isn't about squeezing the other side until they break; it's about finding a deal both parties can live with. "
                 "Walk in knowing your budget and your walk-away point, but stay curious about what the other side actually values -- it isn't always price. "
                 "Sometimes a longer timeline or a bigger order matters more to them than a few percent. The best outcome is usually a compromise "
                 "where everyone feels they gave a little and gained a lot.",
                 "好的谈判不是把对方逼到崩溃，而是找到一个双方都能接受的方案。进场时要清楚自己的预算和底线，"
                 "但也要对对方真正看重的东西保持好奇——未必总是价格。有时候，更长的周期或更大的订单，对他们来说比那几个百分点更重要。"
                 "最好的结果，通常是一个各让一步、都觉得自己让了一点点却收获很多的折中方案。"),
     "pkey": [("squeeze", "压榨/逼迫"), ("walk-away point", "底线/走人的临界点"), ("live with", "接受/将就"), ("compromise", "折中/妥协")],
     "quiz": [("A 'walk-away point' is the point at which you ___.",
               ["sign the deal", "are no longer willing to continue", "raise your price", "call your boss"],
               1, "底线/愿意走人的临界点。"),
              ("The passage says what the other side values is ___.",
               ["always price", "not always price", "never important", "only the timeline"],
               1, "对方看重的未必总是价格。")],
     "translate": [("我们各让一步，你看怎么样？", "Let's meet halfway -- how does that sound?"),
                   ("价格还有商量的余地吗？", "Is there any room for negotiation on the price?")]},
    {  # Day 20 汇报总结
     "passage": ("A strong summary is harder to write than the long version. You have to decide what truly matters and have the courage to leave "
                 "the rest out. Start with the single most important takeaway, follow with the two or three points that support it, and end with "
                 "clear next steps -- who does what, by when. If your audience remembers only one sentence, make sure it's the right one. "
                 "Everything else is just supporting detail.",
                 "写好一段总结，比写长篇还要难。你必须判断什么才真正重要，并且有勇气把其余的舍掉。先说那条最重要的要点，"
                 "再跟上支撑它的两三条，最后给出清晰的下一步——谁、做什么、什么时候完成。如果听众只记得一句话，要确保那是对的那一句。"
                 "其余的，都只是辅助细节。"),
     "pkey": [("takeaway", "要点/收获"), ("leave out", "略去/舍掉"), ("next steps", "下一步/后续"), ("supporting detail", "辅助细节")],
     "quiz": [("The passage says a good summary should start with ___.",
               ["supporting details", "the most important takeaway", "next steps", "an apology"],
               1, "先说最重要的要点（takeaway）。"),
              ("'Leave the rest out' means to ___ the less important parts.",
               ["emphasize", "omit", "repeat", "translate"],
               1, "leave out = 略去、省略。")],
     "translate": [("简而言之，项目进展顺利。", "In a nutshell, the project is going well."),
                   ("最关键的一点是我们需要再招一个人。", "The key takeaway is that we need to hire one more person.")]},
    {  # Day 21 科技与网络
     "passage": ("Technology is wonderful right up until it isn't. The app crashes mid-task, the Wi-Fi drops during the one call that matters, "
                 "and an 'update' quietly changes the button you click a hundred times a day. Most problems, though, bow to the same humble fix: "
                 "turn it off and on again. Beyond that, backing up your work regularly is the cheapest insurance there is -- future you will be "
                 "grateful the day your laptop decides to die.",
                 "科技很美妙，直到它不美妙为止。应用在做到一半时崩溃、偏偏在那场最重要的通话里 Wi-Fi 断了、一次'更新'悄悄改动了你一天要点一百次的那个按钮。"
                 "不过，大多数问题都对同一个朴素的办法俯首称臣：关机再开。除此之外，定期备份你的工作，是世上最便宜的保险——"
                 "某天你的笔记本电脑决定罢工时，未来的你会感激今天的你。"),
     "pkey": [("crash", "崩溃/死机"), ("drop", "(信号)掉线"), ("bow to", "屈服于/听命于"), ("back up", "备份")],
     "quiz": [("The 'humble fix' mentioned in the passage is to ___.",
               ["buy a new laptop", "turn it off and on again", "call support", "update the app"],
               1, "最朴素的办法：关机再开。"),
              ("Backing up your work is called the cheapest ___.",
               ["app", "insurance", "update", "button"],
               1, "被称为最便宜的保险（insurance）。")],
     "translate": [("应用刚才崩溃了，我重启一下试试。", "The app just crashed; let me restart it and try again."),
                   ("记得定期备份你的文件。", "Remember to back up your files regularly.")]},
    {  # Day 22 健康看病
     "passage": ("We tend to treat our health as a problem to fix rather than something to maintain, and only notice it when something goes wrong. "
                 "A nagging headache, a night of bad sleep, that cold you can't quite shake -- small signals that it's time to slow down. "
                 "The hardest part is giving yourself permission to rest before you're forced to. Taking a sick day when you need one isn't slacking off; "
                 "it's how you avoid being out for a whole week instead.",
                 "我们往往把健康当成一个要'修好'的问题，而不是需要日常维护的东西，直到出了岔子才会注意到它。"
                 "挥之不去的头痛、一夜糟糕的睡眠、那场怎么也好不利索的感冒——都是在提醒你该慢下来了。最难的部分，是在被迫停下之前就允许自己休息。"
                 "在需要的时候请一天病假不是偷懒，而是你避免整整病倒一周的办法。"),
     "pkey": [("nagging", "(疼痛)缠人的/挥之不去的"), ("shake (a cold)", "摆脱(感冒)"), ("slow down", "放慢/歇一歇"), ("slack off", "偷懒/松懈")],
     "quiz": [("A cold you 'can't quite shake' is one you ___.",
               ["caught yesterday", "can't get rid of", "gave to others", "enjoy"],
               1, "shake = 摆脱；can't shake = 好不利索。"),
              ("The passage argues that taking a sick day is ___.",
               ["slacking off", "a smart way to avoid worse illness", "unprofessional", "never necessary"],
               1, "请病假是避免病更久，不是偷懒。")],
     "translate": [("我这几天有点不舒服，可能是感冒了。", "I haven't been feeling well these days; I think I'm catching a cold."),
                   ("你需要的时候就请一天假好好休息。", "Take a day off and rest well when you need to.")]},
    {  # Day 23 鼓励与情绪
     "passage": ("Encouragement works best when it's specific. 'Good job' is pleasant but forgettable; 'the way you handled that angry client "
                 "was really impressive' actually sticks. When someone is struggling, they rarely need you to fix their problem -- they need to hear "
                 "that the hard part is normal and that you believe they'll get through it. A few honest words at the right moment can carry a person "
                 "further than you'll ever know.",
                 "鼓励，越具体越有效。'干得好'让人舒服，却转眼就忘；'你处理那个发火客户的方式真让我佩服'才真正记得住。"
                 "当有人正身处困境，他们很少需要你替他们解决问题——他们需要听到：这段难熬是正常的，而且你相信他们能挺过去。"
                 "在对的时刻说几句真心话，能把一个人托举得比你想象的更远。"),
     "pkey": [("stick", "记得住/留下印象"), ("get through", "挺过/渡过"), ("carry (sb) further", "把人托举得更远"), ("at the right moment", "在对的时刻")],
     "quiz": [("According to the passage, encouragement works best when it is ___.",
               ["loud", "specific", "frequent", "public"],
               1, "越具体（specific）越有效。"),
              ("Someone who is struggling mainly needs to hear that ___.",
               ["they are wrong", "the hard part is normal", "they should quit", "you are busy"],
               1, "听到'难是正常的、你相信他们'。")],
     "translate": [("别放弃，你已经很接近成功了。", "Don't give up -- you're so close to making it."),
                   ("你今天的表现真的让我印象深刻。", "The way you performed today really impressed me.")]},
    {  # Day 24 道歉与感谢
     "passage": ("A real apology does three things: it names what went wrong, takes responsibility without excuses, and says what you'll do differently. "
                 "'I'm sorry you feel that way' isn't an apology -- it's a dodge. The same honesty applies to thanks: the more specific you are about "
                 "what someone did and how it helped, the more it means. Both apologies and thank-yous are small acts, but they're the quiet currency "
                 "that keeps relationships running smoothly.",
                 "一句真正的道歉要做到三件事：说清楚哪里错了、不找借口地承担责任、并说明下次你会怎么改。"
                 "'很抱歉你有这种感受'不是道歉——那是在躲闪。同样的真诚也适用于感谢：你越具体地说出对方做了什么、带来了什么帮助，这份感谢就越有分量。"
                 "道歉和感谢都是小小的举动，却是维系关系顺畅运转的、无声的通货。"),
     "pkey": [("take responsibility", "承担责任"), ("a dodge", "躲闪/托词"), ("mean (more)", "更有分量/更有意义"), ("run smoothly", "顺畅运转")],
     "quiz": [("The passage says 'I'm sorry you feel that way' is actually ___.",
               ["a real apology", "a dodge", "a thank-you", "a compliment"],
               1, "那是躲闪（a dodge），不是真道歉。"),
              ("A real apology should include what you'll ___.",
               ["blame", "do differently", "forget", "charge"],
               1, "说明下次你会怎么改（do differently）。")],
     "translate": [("给您带来不便，我深表歉意。", "I sincerely apologize for the inconvenience."),
                   ("非常感谢你一直以来的支持。", "Thank you so much for your continued support.")]},
    {  # Day 25 面试
     "passage": ("The best interview answers tell a short story rather than list adjectives. Instead of claiming you're 'a great problem solver,' "
                 "walk them through one problem you actually solved: the situation, what you did, and how it turned out. Interviewers can tell the "
                 "difference between a rehearsed line and a real experience. And remember, an interview runs both ways -- the questions you ask about "
                 "the role and the team often say as much about you as your answers do.",
                 "最好的面试回答是讲一个短小的故事，而不是罗列一堆形容词。与其声称自己是'出色的问题解决者'，不如带他们走一遍你真正解决过的一个问题："
                 "当时的情况、你做了什么、结果如何。面试官分得清一句背好的台词和一段真实的经历。还要记住，面试是双向的——"
                 "你就岗位和团队提出的问题，往往和你的回答一样，透露出你是什么样的人。"),
     "pkey": [("walk (sb) through", "带某人走一遍/详细讲解"), ("turn out", "结果是/最终"), ("rehearsed", "排练过的/背好的"), ("run both ways", "双向的")],
     "quiz": [("The passage recommends telling a short ___ instead of listing adjectives.",
               ["joke", "story", "list", "song"],
               1, "讲一个真实的小故事（story）。"),
              ("'An interview runs both ways' means ___.",
               ["it is recorded", "the candidate also evaluates the company", "it is very long", "only one side talks"],
               1, "面试是双向评估。")],
     "translate": [("我举个例子说明我是怎么解决这个问题的。", "Let me give you an example of how I solved that problem."),
                   ("我对这个岗位和团队也有几个问题想问。", "I also have a few questions about the role and the team.")]},
    {  # Day 26 团队协作
     "passage": ("The best teams aren't made up of the most talented individuals; they're the ones where people trust each other enough to be honest. "
                 "That means admitting when you're stuck, covering for a teammate without being asked, and sharing credit when things go well. "
                 "Friction is normal -- put smart people in a room and they'll disagree -- but healthy teams argue about ideas and then pull in the "
                 "same direction once a call is made. Trust is what turns a group of people into an actual team.",
                 "最好的团队，并非由最有才华的个人组成；而是那些成员之间彼此信任到敢说真话的团队。这意味着：卡住时肯承认、不等人开口就替队友补位、"
                 "事情顺利时也懂得分享功劳。摩擦是正常的——把一群聪明人放进一个房间，他们一定会有分歧——但健康的团队是'就观点争论、一旦拍板就朝同一个方向使劲'。"
                 "正是信任，把一群人变成了一支真正的团队。"),
     "pkey": [("made up of", "由……组成"), ("cover for", "替……补位/顶班"), ("share credit", "分享功劳"), ("pull in the same direction", "劲往一处使")],
     "quiz": [("According to the passage, the best teams are built on ___.",
               ["talent alone", "trust and honesty", "strict rules", "competition"],
               1, "核心是信任与坦诚。"),
              ("'Pull in the same direction' means team members ___.",
               ["argue forever", "work toward the same goal", "go home early", "compete with each other"],
               1, "朝同一个方向努力。")],
     "translate": [("卡住的时候就说出来，我们一起解决。", "When you're stuck, just say so and we'll solve it together."),
                   ("事情做成了，功劳是大家的。", "When it works out, the credit belongs to everyone.")]},
    {  # Day 27 解决问题
     "passage": ("When something breaks, the instinct is to jump straight to a fix -- but the fastest solvers slow down first. They define the problem "
                 "clearly, ask what changed recently, and resist blaming the most obvious suspect until the evidence points there. Breaking a big, scary "
                 "problem into small, testable pieces turns panic into a checklist. And once it's fixed, the real win is figuring out the root cause so "
                 "the same thing doesn't bite you again next month.",
                 "一出故障，人的本能就是直接扑上去修——但最快的解决者会先慢下来。他们先把问题定义清楚、问问最近有什么变动、"
                 "并在证据指向之前，忍住不去怪那个最明显的'嫌疑人'。把一个又大又吓人的问题拆成一个个可验证的小块，就能把慌乱变成一张清单。"
                 "而一旦修好，真正的收获是找出根本原因，这样同样的事下个月才不会再反咬你一口。"),
     "pkey": [("jump to", "直接跳到/贸然"), ("the obvious suspect", "最明显的嫌疑对象"), ("break into pieces", "拆分成小块"), ("root cause", "根本原因")],
     "quiz": [("The fastest problem solvers first ___.",
               ["blame someone", "define the problem clearly", "restart everything", "give up"],
               1, "先把问题定义清楚。"),
              ("The 'real win' after fixing something is to ___.",
               ["celebrate", "find the root cause", "forget it", "blame the suspect"],
               1, "找到根本原因（root cause）。")],
     "translate": [("我们先搞清楚根本原因，再动手修。", "Let's figure out the root cause before we start fixing it."),
                   ("把大问题拆成几个小步骤会容易很多。", "Breaking the big problem into small steps makes it much easier.")]},
    {  # Day 28 计划与目标
     "passage": ("Big goals are won or lost in the boring middle. The excitement of day one fades fast, and what carries you through is a system, "
                 "not willpower. Shrink the goal until the daily step is almost too small to skip -- ten minutes, one page, a single rep. Track it "
                 "somewhere you'll see, forgive the occasional miss, and never miss twice in a row. Progress rarely feels dramatic day to day, but look "
                 "back after a few months and the gap is startling.",
                 "大目标，是在枯燥的中段分出胜负的。第一天的兴奋消退得很快，真正带你走下去的是一套系统，而不是意志力。"
                 "把目标缩小，直到每天那一步小到几乎没理由跳过——十分钟、一页、一组动作。把它记录在你看得见的地方，原谅偶尔的中断，"
                 "但绝不连续中断两次。进步在日复一日里很少让人觉得惊天动地，但几个月后回头一看，差距会让你吓一跳。"),
     "pkey": [("fade", "消退/褪去"), ("carry (sb) through", "支撑某人走下去"), ("too small to skip", "小到无法跳过"), ("in a row", "连续地")],
     "quiz": [("The passage says what carries you through is ___, not willpower.",
               ["luck", "a system", "money", "excitement"],
               1, "靠一套系统（system）而非意志力。"),
              ("'Never miss twice in a row' means ___.",
               ["never start", "don't skip two days back-to-back", "always skip", "do it twice"],
               1, "别连续两次中断。")],
     "translate": [("把目标拆小，每天只做一点点，更容易坚持。", "Break the goal into small pieces and do a little each day -- it's easier to stick with."),
                   ("偶尔中断没关系，但别连续两天不做。", "Missing once is fine, but don't skip two days in a row.")]},
    {  # Day 29 周末与文化
     "passage": ("Weekends are easy to waste and surprisingly easy to overplan. Pack them too tight and Monday arrives before you've actually rested; "
                 "leave them totally empty and the hours dissolve into scrolling on the couch. I try to pencil in one thing worth looking forward to -- "
                 "a hike, a long lunch with friends, a new neighborhood to wander -- and leave the rest loose. Living abroad taught me that culture isn't "
                 "in the landmarks; it's in how people spend an ordinary Saturday.",
                 "周末既容易被浪费，又出奇地容易被安排得太满。排得太紧，还没真正休息，周一就到了；留得全空，时光又会化成瘫在沙发上刷手机的几个小时。"
                 "我会试着先轻轻定下一件值得期待的事——一次徒步、和朋友的一顿长午餐、一个可以闲逛的新街区——其余时间就留得松散些。"
                 "在国外生活让我明白：文化不在那些地标里，而在人们怎样度过一个平常的周六。"),
     "pkey": [("overplan", "安排得过满"), ("pencil in", "暂定/先记上"), ("dissolve into", "化为/消散成"), ("wander", "闲逛")],
     "quiz": [("The writer suggests you plan one thing and leave the rest ___.",
               ["empty", "loose", "cancelled", "at work"],
               1, "其余时间留松散（loose）。"),
              ("According to the writer, culture is found in ___.",
               ["famous landmarks", "how people spend an ordinary day", "expensive tours", "museums only"],
               1, "在人们普通的日常里。")],
     "translate": [("这个周末有什么安排吗？", "Do you have any plans for this weekend?"),
                   ("我想找个新地方随便逛逛。", "I'd like to find a new place to wander around.")]},
    {  # Day 30 复习与自由表达
     "passage": ("If there's one habit worth taking from these thirty days, it's talking to yourself in English without waiting to feel ready. "
                 "Describe your commute, narrate what you're cooking, argue both sides of a decision out loud. Fluency isn't a finish line you cross; "
                 "it's a muscle that only grows with use, and it fades the moment you stop. You already know far more than you can currently say -- "
                 "the gap now is confidence and reps, not vocabulary. So keep talking, keep listening, and keep going.",
                 "如果说这三十天里有一个值得带走的习惯，那就是：别等到'觉得准备好了'，直接用英语自言自语。描述你的通勤路、念叨你正在做的菜、"
                 "把一个决定的正反两面大声争一遍。流利不是一条你跨过去的终点线；它是一块只在使用中才会长大的肌肉，一旦停下就会萎缩。"
                 "你懂的，其实远比你此刻能说出来的多——如今的差距是信心和练习量，而不是词汇。所以，继续说、继续听、继续走下去。"),
     "pkey": [("narrate", "叙述/念出"), ("out loud", "大声地"), ("a finish line", "终点线"), ("reps (repetitions)", "练习次数/反复练习")],
     "quiz": [("The passage compares fluency to a ___ that grows with use.",
               ["finish line", "muscle", "vocabulary list", "song"],
               1, "把流利比作一块肌肉（muscle）。"),
              ("According to the writer, your current gap is ___.",
               ["vocabulary", "confidence and reps", "grammar rules", "money"],
               1, "差距在信心和练习量（reps）。")],
     "translate": [("别等准备好了，现在就开口说英语。", "Don't wait until you feel ready -- start speaking English now."),
                   ("流利靠的是不断练习，一停下来就会退步。", "Fluency comes from constant practice; it fades the moment you stop.")]},
]

# 每日核心词汇（12 词/天，CET-6→7000 高频进阶）：(单词, 词性, 中文, 例句)
VOCAB = [
    [("articulate", "adj.", "善于表达的", "She is articulate and persuasive."),
     ("approachable", "adj.", "平易近人的", "My boss is warm and approachable."),
     ("versatile", "adj.", "多才多艺的/通用的", "He's a versatile and adaptable worker."),
     ("credential", "n.", "资历/证书", "Her credentials are impressive."),
     ("demeanor", "n.", "举止/风度", "He has a calm, professional demeanor."),
     ("humble", "adj.", "谦逊的", "She stayed humble despite her success."),
     ("ambitious", "adj.", "有抱负的", "He's ambitious and driven."),
     ("competent", "adj.", "能胜任的", "She is a competent manager."),
     ("reserved", "adj.", "内敛的/矜持的", "He's reserved but friendly."),
     ("convey", "v.", "传达", "I want to convey confidence."),
     ("reputable", "adj.", "有声望的", "It's a reputable company."),
     ("outgoing", "adj.", "外向的", "She has an outgoing nature.")],
    [("rapport", "n.", "融洽关系", "She built rapport with clients fast."),
     ("mingle", "v.", "交际/寒暄", "Try to mingle at the event."),
     ("trivial", "adj.", "琐碎的", "We discussed trivial topics."),
     ("awkward", "adj.", "尴尬的", "There was an awkward pause."),
     ("witty", "adj.", "诙谐的", "He gave a witty reply."),
     ("spontaneous", "adj.", "随性的/自发的", "It was a spontaneous chat."),
     ("courteous", "adj.", "彬彬有礼的", "The staff were courteous."),
     ("engaging", "adj.", "吸引人的", "She's an engaging speaker."),
     ("relatable", "adj.", "引起共鸣的", "His story felt relatable."),
     ("banter", "n.", "玩笑/打趣", "Office banter keeps things light."),
     ("genuine", "adj.", "真诚的", "She showed genuine interest."),
     ("acquaintance", "n.", "熟人", "He's a mutual acquaintance.")],
    [("agenda", "n.", "议程", "Let's follow the agenda."),
     ("facilitate", "v.", "促进/主持", "She facilitated the session."),
     ("concise", "adj.", "简洁的", "Keep updates concise."),
     ("consensus", "n.", "共识", "We reached a consensus."),
     ("adjourn", "v.", "休会/延期", "The meeting was adjourned."),
     ("digress", "v.", "离题", "Sorry, I digress."),
     ("allocate", "v.", "分配", "Allocate time for Q&A."),
     ("streamline", "v.", "精简", "We streamlined the process."),
     ("pertinent", "adj.", "切题的/相关的", "Raise pertinent points."),
     ("productive", "adj.", "高效的", "A productive discussion."),
     ("recap", "v.", "回顾/总结", "Let me recap quickly."),
     ("moderate", "v.", "主持/缓和", "She moderated the debate.")],
    [("perspective", "n.", "视角", "From my perspective, it's risky."),
     ("justify", "v.", "证明...合理", "Can you justify the cost?"),
     ("advocate", "v.", "倡导", "I advocate caution."),
     ("subjective", "adj.", "主观的", "That's a subjective view."),
     ("objective", "adj.", "客观的", "Let's stay objective."),
     ("assert", "v.", "断言/坚称", "She asserted her view."),
     ("skeptical", "adj.", "怀疑的", "I'm skeptical about it."),
     ("nuance", "n.", "细微差别", "Note the nuance here."),
     ("compelling", "adj.", "有说服力的", "She made a compelling case."),
     ("valid", "adj.", "有根据的/有效的", "That's a valid point."),
     ("contend", "v.", "主张/争辩", "He contends it's risky."),
     ("reservation", "n.", "保留意见", "I have reservations about it.")],
    [("glitch", "n.", "小故障", "There was a technical glitch."),
     ("latency", "n.", "延迟", "High latency slows it down."),
     ("bandwidth", "n.", "带宽/精力", "We don't have the bandwidth for this."),
     ("disrupt", "v.", "打断/扰乱", "Noise disrupted the call."),
     ("inaudible", "adj.", "听不清的", "You were inaudible for a moment."),
     ("seamless", "adj.", "无缝的/流畅的", "A seamless transition."),
     ("asynchronous", "adj.", "异步的", "We use asynchronous communication."),
     ("overlap", "v.", "重叠", "Our working hours overlap."),
     ("reconnect", "v.", "重新连接", "Let me reconnect."),
     ("interrupt", "v.", "打断", "Sorry to interrupt."),
     ("freeze", "v.", "卡住/定格", "The screen froze."),
     ("notify", "v.", "通知", "I'll notify the team.")],
    [("recipient", "n.", "收件人", "Add me as a recipient."),
     ("draft", "v.", "起草", "I'll draft the email."),
     ("prompt", "adj.", "及时的", "Thanks for your prompt reply."),
     ("clarify", "v.", "澄清", "Let me clarify that point."),
     ("acknowledge", "v.", "确认收到/承认", "Please acknowledge receipt."),
     ("verbose", "adj.", "冗长的", "The email was too verbose."),
     ("courtesy", "n.", "礼貌", "As a courtesy, I let them know early."),
     ("attach", "v.", "附上", "I've attached the file."),
     ("forward", "v.", "转发", "I'll forward it to you."),
     ("concisely", "adv.", "简洁地", "Write concisely."),
     ("tone", "n.", "语气", "Mind the tone of the email."),
     ("reminder", "n.", "提醒", "Just a gentle reminder.")],
    [("cuisine", "n.", "菜系", "I love Thai cuisine."),
     ("appetizer", "n.", "开胃菜", "We ordered a few appetizers."),
     ("savory", "adj.", "咸鲜的", "It's a savory dish."),
     ("bland", "adj.", "清淡/没味道的", "The soup was a bit bland."),
     ("hearty", "adj.", "丰盛的", "A hearty meal."),
     ("beverage", "n.", "饮料", "Choose a beverage."),
     ("tip", "n.", "小费", "Leave a tip for good service."),
     ("spicy", "adj.", "辣的", "It's too spicy for me."),
     ("nutritious", "adj.", "有营养的", "A nutritious meal."),
     ("refill", "n./v.", "续杯/再加满", "Free refills on coffee."),
     ("leftover", "n.", "剩饭剩菜", "Let's take the leftovers home."),
     ("crave", "v.", "渴望(吃)", "I crave sushi tonight.")],
    [("bargain", "n.", "便宜货/划算的交易", "It's a real bargain."),
     ("refund", "n.", "退款", "I got a full refund."),
     ("receipt", "n.", "收据/小票", "Please keep the receipt."),
     ("discount", "n.", "折扣", "A 20% discount."),
     ("affordable", "adj.", "负担得起的", "It's quite affordable."),
     ("browse", "v.", "浏览/闲逛", "I'm just browsing."),
     ("merchandise", "n.", "商品", "High-quality merchandise."),
     ("warranty", "n.", "保修", "A two-year warranty."),
     ("checkout", "n.", "结账处", "A long checkout line."),
     ("splurge", "v.", "挥霍/大手笔买", "I splurged on new shoes."),
     ("flawed", "adj.", "有瑕疵的", "The item was slightly flawed."),
     ("pricey", "adj.", "昂贵的", "It's a bit pricey.")],
    [("intersection", "n.", "十字路口", "Turn at the intersection."),
     ("pedestrian", "n.", "行人", "Watch out for pedestrians."),
     ("detour", "n.", "绕行/弯路", "We had to take a detour."),
     ("commute", "n./v.", "通勤", "My commute is an hour long."),
     ("landmark", "n.", "地标", "Use a landmark to find it."),
     ("adjacent", "adj.", "相邻的", "The adjacent building."),
     ("vicinity", "n.", "附近", "Somewhere in the vicinity."),
     ("roundabout", "n.", "环岛", "Exit at the roundabout."),
     ("congestion", "n.", "拥堵", "Heavy traffic congestion."),
     ("navigate", "v.", "导航/找路", "I navigated the back streets."),
     ("en route", "phr.", "在途中", "I'm en route to the office."),
     ("shortcut", "n.", "捷径", "Let's take a shortcut.")],
    [("itinerary", "n.", "行程", "Check the itinerary."),
     ("accommodation", "n.", "住宿", "Book the accommodation early."),
     ("amenities", "n.", "便利设施", "The hotel amenities are great."),
     ("vacancy", "n.", "空房/空缺", "No vacancy tonight."),
     ("layover", "n.", "中转停留", "A three-hour layover."),
     ("luggage", "n.", "行李", "My luggage went missing."),
     ("boarding", "n.", "登机", "Boarding starts in ten minutes."),
     ("delay", "n.", "延误", "A long flight delay."),
     ("refundable", "adj.", "可退款的", "A refundable ticket."),
     ("customs", "n.", "海关", "We cleared customs quickly."),
     ("voucher", "n.", "代金券", "A hotel voucher."),
     ("spacious", "adj.", "宽敞的", "A spacious room.")],
    [("milestone", "n.", "里程碑", "We hit an important milestone."),
     ("deadline", "n.", "截止期限", "A tight deadline."),
     ("bottleneck", "n.", "瓶颈", "A bottleneck slowed us down."),
     ("deliverable", "n.", "交付物", "The final deliverable."),
     ("scope", "n.", "范围", "That's outside the project scope."),
     ("prioritize", "v.", "排优先级", "Let's prioritize the tasks."),
     ("setback", "n.", "挫折", "A minor setback."),
     ("feasible", "adj.", "可行的", "Is this feasible?"),
     ("estimate", "n./v.", "估计", "A rough estimate."),
     ("scalable", "adj.", "可扩展的", "A scalable solution."),
     ("ongoing", "adj.", "进行中的", "An ongoing task."),
     ("workflow", "n.", "工作流程", "Improve the workflow.")],
    [("favor", "n.", "帮忙/恩惠", "Can you do me a favor?"),
     ("assist", "v.", "协助", "I'm happy to assist."),
     ("accommodate", "v.", "迁就/满足", "We can accommodate that request."),
     ("delegate", "v.", "委派", "Delegate the task to someone."),
     ("reciprocate", "v.", "回报", "I'll reciprocate the favor."),
     ("hesitant", "adj.", "犹豫的", "I'm hesitant to ask."),
     ("oblige", "v.", "效劳/帮忙", "Happy to oblige."),
     ("willing", "adj.", "愿意的", "I'm willing to help out."),
     ("burden", "n.", "负担", "I don't want to be a burden."),
     ("grateful", "adj.", "感激的", "I'm really grateful."),
     ("spare", "v.", "抽出(时间)", "Can you spare a minute?"),
     ("rely on", "phr.", "依靠", "I rely on you for this.")],
    [("counter", "v.", "反驳", "She countered my point."),
     ("concede", "v.", "承认/让步", "I concede that you're right."),
     ("compromise", "n./v.", "妥协/折中", "Let's reach a compromise."),
     ("dispute", "n./v.", "争议/争论", "A minor dispute."),
     ("align", "v.", "一致/对齐", "We're fully aligned."),
     ("dissent", "n.", "异议", "She voiced her dissent."),
     ("reconcile", "v.", "调和/使和解", "Reconcile the two views."),
     ("mutual", "adj.", "相互的", "A mutual agreement."),
     ("contradict", "v.", "反驳/自相矛盾", "Don't contradict yourself."),
     ("endorse", "v.", "赞同/支持", "I endorse this plan."),
     ("objection", "n.", "反对", "Any objections?"),
     ("tentative", "adj.", "暂定的/试探性的", "A tentative agreement.")],
    [("complaint", "n.", "投诉", "File a complaint."),
     ("resolve", "v.", "解决", "We'll resolve the issue."),
     ("inquiry", "n.", "咨询/询问", "A customer inquiry."),
     ("compensation", "n.", "补偿", "We offered compensation."),
     ("escalate", "v.", "升级/上报", "Let me escalate the case."),
     ("patient", "adj.", "耐心的", "Please be patient."),
     ("dissatisfied", "adj.", "不满的", "A dissatisfied customer."),
     ("assure", "v.", "向...保证", "I assure you it's fine."),
     ("pending", "adj.", "待处理的", "The case is still pending."),
     ("representative", "n.", "客服代表", "A service representative."),
     ("prompt", "v.", "促使/提示", "This prompted a quick fix."),
     ("courteous", "adj.", "有礼貌的", "A courteous reply.")],
    [("responsibility", "n.", "职责", "My main responsibilities."),
     ("expertise", "n.", "专长/专业知识", "Her technical expertise."),
     ("proficient", "adj.", "熟练的", "I'm proficient in Python."),
     ("tedious", "adj.", "枯燥冗长的", "A tedious task."),
     ("hectic", "adj.", "忙乱的", "It's been a hectic week."),
     ("workload", "n.", "工作量", "A heavy workload."),
     ("colleague", "n.", "同事", "A supportive colleague."),
     ("supervise", "v.", "监管", "I supervise two interns."),
     ("multitask", "v.", "同时处理多任务", "I multitask all day."),
     ("rewarding", "adj.", "有成就感的", "A rewarding job."),
     ("mundane", "adj.", "平凡乏味的", "Mundane paperwork."),
     ("deadline-driven", "adj.", "以截止期为导向的", "A deadline-driven role.")],
    [("availability", "n.", "空闲/可用性", "Let me check my availability."),
     ("reschedule", "v.", "改期", "Can we reschedule?"),
     ("punctual", "adj.", "守时的", "Please be punctual."),
     ("slot", "n.", "时间段", "Is there a free slot?"),
     ("postpone", "v.", "推迟", "Let's postpone the meeting."),
     ("upcoming", "adj.", "即将到来的", "The upcoming event."),
     ("duration", "n.", "时长", "The duration is one hour."),
     ("simultaneously", "adv.", "同时地", "Both ran simultaneously."),
     ("beforehand", "adv.", "事先", "Confirm it beforehand."),
     ("flexible", "adj.", "灵活的", "My schedule is flexible."),
     ("overdue", "adj.", "逾期的", "The task is overdue."),
     ("interval", "n.", "间隔", "At regular intervals.")],
    [("gloomy", "adj.", "阴郁的", "A gloomy, grey day."),
     ("drizzle", "n./v.", "细雨/下毛毛雨", "A light drizzle."),
     ("humid", "adj.", "潮湿的", "It's hot and humid."),
     ("chilly", "adj.", "微冷的", "A chilly morning."),
     ("forecast", "n.", "预报", "The weather forecast."),
     ("cheerful", "adj.", "开朗愉快的", "She's in a cheerful mood."),
     ("irritable", "adj.", "易怒的", "I feel irritable today."),
     ("refreshed", "adj.", "焕然一新的", "I feel refreshed after a walk."),
     ("overcast", "adj.", "阴天的", "An overcast sky."),
     ("breeze", "n.", "微风", "A cool breeze."),
     ("moody", "adj.", "情绪化的", "He's a bit moody today."),
     ("soothing", "adj.", "抚慰的", "A soothing walk.")],
    [("leisure", "n.", "休闲", "In my leisure time."),
     ("enthusiast", "n.", "爱好者", "A fitness enthusiast."),
     ("pastime", "n.", "消遣", "Reading is my favorite pastime."),
     ("indulge", "v.", "沉迷/纵情于", "I indulge in good coffee."),
     ("recreational", "adj.", "娱乐的", "Recreational activities."),
     ("knack", "n.", "诀窍/天赋", "She has a knack for drawing."),
     ("dabble", "v.", "浅尝/涉猎", "I dabble in painting."),
     ("immerse", "v.", "使沉浸", "Immerse yourself in it."),
     ("rejuvenate", "v.", "使恢复活力", "Hobbies rejuvenate me."),
     ("avid", "adj.", "热衷的", "An avid reader."),
     ("unwind", "v.", "放松", "I unwind by cooking."),
     ("hands-on", "adj.", "动手的/亲历的", "A hands-on hobby.")],
    [("budget", "n.", "预算", "We're within budget."),
     ("negotiate", "v.", "谈判", "Let's negotiate the price."),
     ("leverage", "n.", "筹码/影响力", "We have some leverage here."),
     ("concession", "n.", "让步", "Make a small concession."),
     ("counteroffer", "n.", "还价", "They made a counteroffer."),
     ("mutually", "adv.", "互相地", "A mutually beneficial deal."),
     ("incentive", "n.", "激励/诱因", "A financial incentive."),
     ("viable", "adj.", "可行的", "A viable deal."),
     ("overpriced", "adj.", "定价过高的", "It's overpriced."),
     ("installment", "n.", "分期付款", "Pay in installments."),
     ("haggle", "v.", "讨价还价", "They haggled over the price."),
     ("lucrative", "adj.", "赚钱的/有利可图的", "A lucrative contract.")],
    [("summarize", "v.", "总结", "Let me summarize the report."),
     ("highlight", "v.", "强调/突出", "I'll highlight the key points."),
     ("outcome", "n.", "结果", "A positive outcome."),
     ("takeaway", "n.", "要点", "The key takeaway is simple."),
     ("overview", "n.", "概述", "A brief overview."),
     ("elaborate", "v.", "详述", "Could you elaborate?"),
     ("conclude", "v.", "得出结论", "We conclude that it works."),
     ("implication", "n.", "影响/含义", "The implications are serious."),
     ("underscore", "v.", "强调", "This underscores the risk."),
     ("findings", "n.", "发现/结果", "Share the findings."),
     ("succinct", "adj.", "简明的", "A succinct summary."),
     ("concise", "adj.", "简洁的", "Keep it concise.")],
    [("crash", "v.", "崩溃/死机", "The app crashed."),
     ("backup", "n.", "备份", "Make a backup first."),
     ("upgrade", "v.", "升级", "Upgrade the system."),
     ("bug", "n.", "程序漏洞", "Fix the bug."),
     ("compatible", "adj.", "兼容的", "It's compatible with my phone."),
     ("interface", "n.", "界面", "A clean user interface."),
     ("default", "n.", "默认(设置)", "Keep the default setting."),
     ("corrupt", "adj.", "损坏的", "A corrupt file."),
     ("sync", "v.", "同步", "Sync the data to the cloud."),
     ("troubleshoot", "v.", "排查故障", "Let's troubleshoot the error."),
     ("obsolete", "adj.", "过时的", "Obsolete hardware."),
     ("user-friendly", "adj.", "易用的", "A user-friendly tool.")],
    [("symptom", "n.", "症状", "Common flu symptoms."),
     ("diagnosis", "n.", "诊断", "An early diagnosis."),
     ("prescription", "n.", "处方", "Fill a prescription."),
     ("recover", "v.", "康复", "I hope you recover soon."),
     ("fatigue", "n.", "疲劳", "Constant fatigue."),
     ("nausea", "n.", "恶心", "A wave of nausea."),
     ("remedy", "n.", "疗法/补救", "A home remedy."),
     ("contagious", "adj.", "传染的", "A contagious cold."),
     ("immune", "adj.", "免疫的", "A strong immune system."),
     ("chronic", "adj.", "慢性的", "Chronic back pain."),
     ("dizzy", "adj.", "头晕的", "I feel a bit dizzy."),
     ("wellbeing", "n.", "健康/幸福", "Mental wellbeing matters.")],
    [("motivate", "v.", "激励", "A good leader motivates the team."),
     ("resilient", "adj.", "有韧性的", "Try to stay resilient."),
     ("persevere", "v.", "坚持不懈", "Persevere through hard times."),
     ("uplifting", "adj.", "鼓舞人心的", "An uplifting message."),
     ("reassure", "v.", "使安心", "Let me reassure you."),
     ("confidence", "n.", "自信", "Build your confidence."),
     ("overwhelmed", "adj.", "不知所措的", "I feel overwhelmed."),
     ("cope", "v.", "应对", "Cope with the stress."),
     ("optimistic", "adj.", "乐观的", "Stay optimistic."),
     ("determined", "adj.", "坚定的", "She's determined to win."),
     ("empower", "v.", "赋能/增强信心", "We empower each other."),
     ("encouragement", "n.", "鼓励", "A few words of encouragement.")],
    [("sincere", "adj.", "真诚的", "A sincere apology."),
     ("gratitude", "n.", "感激", "Express your gratitude."),
     ("inconvenience", "n.", "不便", "Sorry for the inconvenience."),
     ("appreciate", "v.", "感激/赏识", "I really appreciate it."),
     ("regret", "v.", "后悔/遗憾", "I regret the mistake."),
     ("amends", "n.", "补偿/弥补", "I want to make amends."),
     ("indebted", "adj.", "感激的/欠人情的", "I'm indebted to you."),
     ("heartfelt", "adj.", "衷心的", "Heartfelt thanks."),
     ("pardon", "v.", "原谅", "Pardon me for that."),
     ("owe", "v.", "欠", "I owe you one."),
     ("considerate", "adj.", "体贴的", "That's very considerate."),
     ("oversight", "n.", "疏忽", "It was a small oversight.")],
    [("candidate", "n.", "候选人", "A strong candidate."),
     ("qualification", "n.", "资格", "Relevant qualifications."),
     ("strength", "n.", "优势", "My key strength is teamwork."),
     ("weakness", "n.", "弱点", "A minor weakness."),
     ("achievement", "n.", "成就", "A proud achievement."),
     ("stand out", "phr.", "脱颖而出", "You need to stand out."),
     ("confident", "adj.", "自信的", "Be confident in the interview."),
     ("relevant", "adj.", "相关的", "Relevant experience."),
     ("accomplish", "v.", "完成/实现", "I accomplished my goals."),
     ("suitable", "adj.", "合适的", "A suitable role for me."),
     ("motivation", "n.", "动机", "What's your motivation?"),
     ("aspiration", "n.", "抱负", "My career aspirations.")],
    [("collaborate", "v.", "协作", "We collaborate closely."),
     ("cohesive", "adj.", "有凝聚力的", "A cohesive team."),
     ("contribute", "v.", "贡献", "Everyone contributes ideas."),
     ("synergy", "n.", "协同效应", "There's great synergy."),
     ("accountable", "adj.", "负责的", "We're all accountable."),
     ("morale", "n.", "士气", "Team morale is high."),
     ("dynamic", "n.", "动态/相互关系", "The team dynamic is good."),
     ("reliable", "adj.", "可靠的", "A reliable teammate."),
     ("coordinate", "v.", "协调", "Coordinate your efforts."),
     ("supportive", "adj.", "支持的", "A supportive environment."),
     ("camaraderie", "n.", "团队情谊", "There's strong camaraderie."),
     ("cooperative", "adj.", "合作的", "A cooperative attitude.")],
    [("diagnose", "v.", "诊断/判断", "Diagnose the real issue."),
     ("root cause", "n.", "根本原因", "Find the root cause."),
     ("workaround", "n.", "变通办法", "We found a workaround."),
     ("analyze", "v.", "分析", "Analyze the data first."),
     ("hypothesis", "n.", "假设", "Test the hypothesis."),
     ("isolate", "v.", "隔离/定位", "Isolate the problem."),
     ("mitigate", "v.", "缓解/减轻", "Mitigate the risk."),
     ("systematic", "adj.", "系统的", "A systematic approach."),
     ("pinpoint", "v.", "精确定位", "Pinpoint the error."),
     ("tackle", "v.", "解决/应对", "Let's tackle this issue."),
     ("recurring", "adj.", "反复出现的", "A recurring problem."),
     ("contingency", "n.", "应急/意外", "A contingency plan.")],
    [("aspire", "v.", "渴望/立志", "I aspire to grow."),
     ("willpower", "n.", "意志力", "It takes willpower."),
     ("consistent", "adj.", "一贯的/稳定的", "Be consistent every day."),
     ("discipline", "n.", "自律", "Self-discipline is key."),
     ("long-term", "adj.", "长期的", "A long-term goal."),
     ("attainable", "adj.", "可实现的", "Set attainable goals."),
     ("procrastinate", "v.", "拖延", "Don't procrastinate."),
     ("accountability", "n.", "问责/担责", "Build accountability."),
     ("momentum", "n.", "势头/动力", "Keep the momentum going."),
     ("incremental", "adj.", "渐进的", "Incremental progress."),
     ("habit", "n.", "习惯", "Make it a daily habit."),
     ("persist", "v.", "坚持", "Persist even when it's hard.")],
    [("leisurely", "adj.", "悠闲的", "A leisurely brunch."),
     ("wander", "v.", "闲逛/漫步", "We wandered the old streets."),
     ("getaway", "n.", "短途旅行", "A weekend getaway."),
     ("custom", "n.", "习俗", "A local custom."),
     ("scenic", "adj.", "风景优美的", "A scenic route."),
     ("recharge", "v.", "充电/恢复精力", "I recharge on weekends."),
     ("stroll", "n./v.", "散步", "Take a stroll in the park."),
     ("heritage", "n.", "遗产/传统", "Cultural heritage."),
     ("authentic", "adj.", "地道的/真实的", "Authentic local food."),
     ("explore", "v.", "探索", "Explore the city."),
     ("picturesque", "adj.", "如画的", "A picturesque town."),
     ("diverse", "adj.", "多元的", "A diverse culture.")],
    [("fluency", "n.", "流利", "Build your fluency."),
     ("vocabulary", "n.", "词汇量", "Expand your vocabulary."),
     ("pronunciation", "n.", "发音", "Clear pronunciation."),
     ("comprehension", "n.", "理解", "Listening comprehension."),
     ("paraphrase", "v.", "改述/换种说法", "Let me paraphrase that."),
     ("consolidate", "v.", "巩固", "Consolidate what you've learned."),
     ("retention", "n.", "记忆保持", "Improve word retention."),
     ("intonation", "n.", "语调", "Natural intonation."),
     ("proficiency", "n.", "熟练程度", "Language proficiency."),
     ("reinforce", "v.", "强化", "Reinforce the new words."),
     ("spontaneously", "adv.", "自然地/不假思索地", "Speak more spontaneously."),
     ("breakthrough", "n.", "突破", "A real breakthrough.")],
]

TOTAL = len(DAYS)

CSS = """
<style>
*{box-sizing:border-box;}
body{font-family:-apple-system,"Segoe UI","Microsoft YaHei",sans-serif;margin:0;background:#f4f6f8;color:#1f2328;line-height:1.75;}
header{position:sticky;top:0;z-index:10;background:#6b3fa0;color:#fff;padding:14px 20px;box-shadow:0 2px 6px rgba(0,0,0,.15);}
header h1{margin:0 0 8px;font-size:18px;}
.progwrap{background:rgba(255,255,255,.25);border-radius:20px;height:16px;overflow:hidden;}
.progbar{height:100%;background:#ffd94a;width:0;transition:width .3s;}
.progtext{font-size:13px;margin-top:6px;}
.tabs{display:flex;gap:6px;margin-top:10px;flex-wrap:wrap;}
.tabs button{border:none;background:rgba(255,255,255,.15);color:#fff;padding:8px 16px;border-radius:8px 8px 0 0;cursor:pointer;font-size:14px;}
.tabs button.active{background:#f4f6f8;color:#6b3fa0;font-weight:600;}
main{max-width:860px;margin:0 auto;padding:20px 16px 80px;}
.panel{display:none;} .panel.show{display:block;}
.day{background:#fff;border-radius:10px;padding:16px 18px;margin:14px 0;box-shadow:0 1px 4px rgba(0,0,0,.06);border-left:5px solid #d9c7ef;}
.day.done{border-left-color:#1a7f37;}
.day-h{display:flex;align-items:center;gap:10px;flex-wrap:wrap;}
.day-h h2{font-size:17px;margin:0;color:#6b3fa0;flex:1;}
.daynum{background:#6b3fa0;color:#fff;border-radius:8px;padding:2px 10px;font-size:13px;font-weight:600;}
.day.done .daynum{background:#1a7f37;}
.sec{margin-top:12px;padding-top:10px;border-top:1px dashed #e3dcef;}
.sec h3{margin:0 0 6px;font-size:15px;color:#8a2be2;}
.row{display:flex;align-items:flex-start;gap:8px;padding:5px 0;flex-wrap:wrap;}
.en{font-weight:600;}
.zh{color:#555;}
.ex{color:#777;font-size:14px;font-style:italic;}
.spk{border:1px solid #c9b3e8;background:#f6f0fd;color:#6b3fa0;border-radius:14px;padding:2px 10px;cursor:pointer;font-size:13px;flex:none;}
.spk:hover{background:#eadcfb;}
.song{background:#fff8e6;border:1px solid #f0d98a;border-radius:8px;padding:12px 14px;margin-top:12px;}
.song .t{font-size:16px;font-weight:700;color:#8a6d00;}
.song a{color:#0969da;}
.rev{background:#f3fbf5;border:1px solid #c9e9d2;border-radius:8px;padding:10px 14px;margin-top:12px;}
.chk{transform:scale(1.4);cursor:pointer;}
.hint{color:#6a737d;font-size:13px;}
.util{background:#8a5cc0;color:#fff;border:none;border-radius:8px;padding:6px 12px;cursor:pointer;font-size:13px;margin-right:6px;}
.mastered{text-decoration:line-through;opacity:.5;}
.theme-block{background:#fff;border-radius:10px;padding:14px 16px;margin:12px 0;box-shadow:0 1px 4px rgba(0,0,0,.06);}
.theme-block h3{margin:0 0 8px;color:#6b3fa0;}
/* 精读短文 */
.passage{background:#f7f4fc;border:1px solid #e3dcef;border-radius:8px;padding:12px 14px;margin-top:8px;}
.passage .en-p{font-size:15.5px;line-height:1.9;}
.passage .zh-p{color:#555;font-size:14px;margin-top:8px;padding-top:8px;border-top:1px dashed #e3dcef;}
.passage .zh-p.hide{display:none;}
.ptools{margin:8px 0;}
.ptools button{border:1px solid #c9b3e8;background:#fff;color:#6b3fa0;border-radius:14px;padding:3px 12px;cursor:pointer;font-size:13px;margin-right:6px;}
.ptools button:hover{background:#f0e8fb;}
/* 小测验 */
.quiz{background:#fff;border:1px solid #e3dcef;border-radius:8px;padding:10px 14px;margin:10px 0;}
.quiz .qq{font-weight:600;margin-bottom:6px;}
.qopt{display:block;padding:4px 8px;border-radius:6px;cursor:pointer;margin:2px 0;}
.qopt:hover{background:#f4f0fb;}
.qopt input{margin-right:8px;}
.qopt.correct{background:#e6f4ea;border-left:3px solid #1a7f37;}
.qopt.wrong{background:#fde8e8;border-left:3px solid #d1242f;}
.qbtn{border:none;background:#6b3fa0;color:#fff;border-radius:6px;padding:5px 14px;cursor:pointer;font-size:13px;margin-top:6px;}
.qexp{margin-top:8px;padding:8px 10px;background:#fff8e6;border:1px solid #f0d98a;border-radius:6px;font-size:14px;display:none;}
.qexp.show{display:block;}
/* 翻译练习 */
.trans{background:#fff;border:1px solid #e3dcef;border-radius:8px;padding:10px 14px;margin:10px 0;}
.trans .qq{font-weight:600;margin-bottom:6px;}
.tans{width:100%;min-height:52px;border:1px solid #c9b3e8;border-radius:6px;padding:8px;font-size:15px;font-family:inherit;resize:vertical;}
.tref{margin-top:8px;}
.tref summary{cursor:pointer;color:#6b3fa0;font-size:14px;font-weight:600;}
.tref .ref{margin-top:6px;padding:8px 10px;background:#f3fbf5;border:1px solid #c9e9d2;border-radius:6px;}
.tref .ref .en{color:#1a7f37;}
/* 核心词汇 */
.vcard{display:flex;align-items:flex-start;gap:8px;padding:7px 0;border-bottom:1px solid #f0ecf7;flex-wrap:wrap;}
.vcard:last-child{border-bottom:none;}
.vcard .w{font-weight:700;font-size:15.5px;color:#1f2328;}
.vcard .pos{color:#8a5cc0;font-size:12.5px;background:#f0e8fb;border-radius:4px;padding:0 5px;margin:0 4px;}
.vcard .vz{color:#444;}
.vcard .vex{display:block;color:#777;font-size:13.5px;font-style:italic;margin-top:2px;}
.vsearch{width:100%;padding:9px 12px;border:1px solid #c9b3e8;border-radius:8px;font-size:15px;margin-bottom:10px;}
/* 单词自测闪卡 */
.ftpanel{text-align:center;}
.ftbar{display:flex;gap:8px;justify-content:center;align-items:center;flex-wrap:wrap;margin-bottom:12px;}
.ftbar select{padding:6px 10px;border:1px solid #c9b3e8;border-radius:8px;font-size:14px;}
.flashcard{background:#fff;border:2px solid #d9c7ef;border-radius:14px;padding:36px 20px;margin:0 auto;max-width:520px;min-height:180px;display:flex;flex-direction:column;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,.08);}
.flashcard .fw{font-size:30px;font-weight:800;color:#6b3fa0;}
.flashcard .fpos{color:#8a5cc0;font-size:15px;margin-top:4px;}
.flashcard .fz{font-size:22px;color:#1a7f37;margin-top:14px;font-weight:700;}
.flashcard .fex{color:#666;font-style:italic;margin-top:10px;font-size:15px;}
.ftbtns{margin-top:16px;display:flex;gap:10px;justify-content:center;flex-wrap:wrap;}
.ftbtns button{border:none;border-radius:10px;padding:10px 20px;cursor:pointer;font-size:15px;}
.btn-show{background:#6b3fa0;color:#fff;}
.btn-know{background:#1a7f37;color:#fff;}
.btn-dunno{background:#d1242f;color:#fff;}
.btn-speak{background:#8a5cc0;color:#fff;}
.ftscore{margin-top:14px;color:#555;font-size:15px;}
/* 星标收藏按钮 */
.fav{border:none;background:none;cursor:pointer;font-size:18px;color:#ccc;flex:none;line-height:1;padding:0 2px;}
.fav.on{color:#f5a623;}
/* 收藏夹 */
.favadd{background:#fff8e6;border:1px solid #f0d98a;border-radius:8px;padding:12px 14px;margin-bottom:12px;}
.favadd input{width:100%;padding:8px 10px;border:1px solid #c9b3e8;border-radius:6px;font-size:15px;margin:4px 0;}
.favrow{display:flex;align-items:flex-start;gap:8px;background:#fff;border:1px solid #e3dcef;border-radius:8px;padding:10px 12px;margin:8px 0;}
.favrow .fcontent{flex:1;}
.favrow .fen{font-weight:700;}
.favrow .fzh{color:#555;}
.favrow .fex{display:block;color:#777;font-size:13.5px;font-style:italic;margin-top:2px;}
.favrow .ftag{font-size:12px;color:#8a5cc0;background:#f0e8fb;border-radius:4px;padding:0 6px;margin-right:6px;}
.favrow .fdel{border:none;background:#fde8e8;color:#d1242f;border-radius:6px;padding:3px 9px;cursor:pointer;font-size:13px;flex:none;}
/* 每日：日期选择条 + 学习记录 */
.daysel-bar{display:flex;align-items:center;gap:8px;flex-wrap:wrap;background:#fff;border:1px solid #e3dcef;border-radius:10px;padding:10px 12px;margin:10px 0;}
.daysel-bar select{flex:1;min-width:160px;padding:8px 10px;border:1px solid #c9b3e8;border-radius:8px;font-size:15px;}
.daysel-bar button{border:1px solid #c9b3e8;background:#f6f0fd;color:#6b3fa0;border-radius:8px;padding:8px 14px;cursor:pointer;font-size:15px;}
.daysel-bar button:hover{background:#eadcfb;}
.studylog{margin:8px 0;}
.studylog summary{cursor:pointer;color:#6b3fa0;font-weight:600;}
.logitem{padding:4px 0;border-bottom:1px solid #f0ecf7;font-size:14px;}
.logitem .ld{color:#1a7f37;font-weight:600;margin-right:8px;}
/* ===== iPad / 平板适配（10.9" 两种方向都舒适）===== */
@media (min-width:768px) and (max-width:1400px){
  body{font-size:18px;}
  main{max-width:92%;padding:22px 20px 90px;}
  header h1{font-size:22px;}
  .progtext{font-size:15px;}
  .tabs button{font-size:17px;padding:10px 20px;}
  .util{font-size:15px;padding:8px 15px;}
  .day{padding:20px 24px;}
  .day-h h2{font-size:20px;}
  .daynum{font-size:15px;padding:3px 12px;}
  .sec h3{font-size:17.5px;}
  .passage .en-p{font-size:18.5px;line-height:2;}
  .passage .zh-p{font-size:16px;}
  .vcard .w{font-size:18px;}
  .vcard .vz{font-size:16.5px;}
  .vcard .vex{font-size:15px;}
  .en,.zh{font-size:17px;}
  .ex{font-size:15.5px;}
  .quiz,.trans{font-size:17px;}
  .tans{font-size:17px;}
  .spk{font-size:15px;padding:4px 12px;}
  .fav{font-size:22px;}
  .chk{transform:scale(1.6);}
  .flashcard .fw{font-size:36px;}
  .flashcard .fz{font-size:26px;}
  .daysel-bar select,.daysel-bar button{font-size:17px;}
}
@media(max-width:640px){main{padding:16px 8px 60px;}}
</style>
"""

JS = """
<script>
function speak(t){try{window.speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(t);u.lang='en-US';u.rate=0.88;window.speechSynthesis.speak(u);}catch(e){}}
document.addEventListener('click',function(e){
  var el=e.target;
  if(el.classList&&el.classList.contains('spk')){speak(el.dataset.t);}
  if(el.classList&&el.classList.contains('fav')){toggleFav(el);}
});
// ===== 收藏夹 =====
function getFavs(){try{return JSON.parse(localStorage.getItem('ENG::favs')||'{}');}catch(e){return {};}}
function setFavs(o){localStorage.setItem('ENG::favs',JSON.stringify(o));}
function toggleFav(btn){
  var favs=getFavs();var id=btn.dataset.fid;
  if(favs[id]){delete favs[id];}
  else{favs[id]={t:btn.dataset.t,en:btn.dataset.en,zh:btn.dataset.zh||'',ex:btn.dataset.ex||''};}
  setFavs(favs);refreshStars();renderFavs();
}
function removeFav(id){var favs=getFavs();delete favs[id];setFavs(favs);refreshStars();renderFavs();}
function addCustomFav(){
  var en=document.getElementById('fav_en').value.trim();if(!en){alert('请填写英文内容');return;}
  var favs=getFavs();var id='c::'+Date.now();
  favs[id]={t:'custom',en:en,zh:document.getElementById('fav_zh').value.trim(),ex:document.getElementById('fav_ex').value.trim()};
  setFavs(favs);document.getElementById('fav_en').value='';document.getElementById('fav_zh').value='';document.getElementById('fav_ex').value='';
  renderFavs();refreshStars();alert('已添加到收藏夹 ⭐');
}
function refreshStars(){var favs=getFavs();
  document.querySelectorAll('.fav').forEach(function(b){var on=!!favs[b.dataset.fid];b.classList.toggle('on',on);b.textContent=on?'★':'☆';});
}
function renderFavs(){
  var favs=getFavs();var box=document.getElementById('favlist');if(!box)return;
  var ids=Object.keys(favs);
  var tagmap={word:'单词',phrase:'短语',custom:'自定义'};
  if(!ids.length){box.innerHTML='<p class="hint">还没有收藏。去「每日计划」或「词汇表」点 ☆ 收藏，或在上面自定义添加。</p>';return;}
  var order={word:0,phrase:1,custom:2};
  ids.sort(function(a,b){return (order[favs[a].t]-order[favs[b].t]);});
  box.innerHTML=ids.map(function(id){var f=favs[id];
    return '<div class="favrow"><button class="spk" data-t="'+(f.en||'').replace(/"/g,'&quot;')+'">🔊</button>'+
      '<div class="fcontent"><span class="ftag">'+(tagmap[f.t]||'')+'</span><span class="fen">'+esc2(f.en)+'</span>'+
      (f.zh?' — <span class="fzh">'+esc2(f.zh)+'</span>':'')+
      (f.ex?'<span class="fex">'+esc2(f.ex)+'</span>':'')+'</div>'+
      '<button class="fdel" onclick="removeFav(\\''+id.replace(/'/g,"\\\\'")+'\\')">✕ 移除</button></div>';
  }).join('');
}
function esc2(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
// ===== 每日：只看当天 + 筛选 =====
function firstIncompleteDay(){for(var i=1;i<=""" + str(TOTAL) + """;i++){if(localStorage.getItem('ENG::done::d'+i)!=='1')return i;}return """ + str(TOTAL) + """;}
function showDay(v){
  localStorage.setItem('ENG::viewday',v);
  document.getElementById('daysel').value=v;
  document.querySelectorAll('.day').forEach(function(d){
    d.style.display=(v==='all'||d.dataset.day===String(v))?'':'none';});
  window.scrollTo(0,0);
}
function prevDay(){var v=document.getElementById('daysel').value;if(v==='all')return;var n=Math.max(1,parseInt(v)-1);showDay(n);}
function nextDay(){var v=document.getElementById('daysel').value;if(v==='all')return;var n=Math.min(""" + str(TOTAL) + """,parseInt(v)+1);showDay(n);}
function updateDaySelOptions(){
  var sel=document.getElementById('daysel');if(!sel)return;
  for(var i=0;i<sel.options.length;i++){var o=sel.options[i];if(o.value==='all')continue;
    var done=localStorage.getItem('ENG::done::d'+o.value)==='1';
    var base=o.textContent.replace(/^✓ /,'');o.textContent=(done?'✓ ':'')+base;}
}
// ===== 学习记录（日期）=====
function todayStr(){var d=new Date();return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2);}
function renderStudyLog(){
  var box=document.getElementById('studylog');if(!box)return;var items=[];
  for(var i=1;i<=""" + str(TOTAL) + """;i++){var dt=localStorage.getItem('ENG::studied::d'+i);
    if(dt){var th=(document.querySelector('.day[data-day="'+i+'"] .day-h h2')||{}).textContent||'';items.push({d:i,dt:dt,th:th});}}
  if(!items.length){box.innerHTML='<p class="hint">还没有学习记录。完成任意一天的打卡后，这里会记下日期。</p>';return;}
  items.sort(function(a,b){return a.dt<b.dt?-1:(a.dt>b.dt?1:a.d-b.d);});
  box.innerHTML='<p class="hint">共 '+items.length+' 天有学习记录：</p>'+items.map(function(x){
    return '<div class="logitem"><span class="ld">'+x.dt+'</span>✓ Day '+x.d+' · '+esc2(x.th)+'</div>';}).join('');
}
function toggleZh(btn){var p=btn.closest('.passage');var z=p.querySelector('.zh-p');z.classList.toggle('hide');btn.textContent=z.classList.contains('hide')?'👁 显示中文':'🙈 隐藏中文';}
function gradeQuiz(btn){
  var box=btn.closest('.quiz');var correct=parseInt(box.dataset.correct);
  var opts=box.querySelectorAll('.qopt');var picked=-1;
  opts.forEach(function(o,i){var r=o.querySelector('input');o.classList.remove('correct','wrong');if(r.checked)picked=i;});
  if(picked<0){alert('先选一个答案哦');return;}
  opts[correct].classList.add('correct');
  if(picked!==correct)opts[picked].classList.add('wrong');
  var exp=box.querySelector('.qexp');exp.classList.add('show');
  localStorage.setItem(box.dataset.k+'::done','1');
}
function showTab(i){
  document.querySelectorAll('.panel').forEach(function(p,x){p.classList.toggle('show',x===i);});
  document.querySelectorAll('.tabs button').forEach(function(b,x){b.classList.toggle('active',x===i);});
  localStorage.setItem('ENG::tab',i); window.scrollTo(0,0);
}
function updateProgress(){
  var chks=document.querySelectorAll('.chk');var done=0;chks.forEach(function(c){if(c.checked)done++;});
  var pct=chks.length?Math.round(done/chks.length*100):0;
  document.getElementById('progbar').style.width=pct+'%';
  document.getElementById('progtext').innerHTML='已坚持打卡 <b>'+done+'</b> / '+chks.length+' 天（'+pct+'%）　每天约 30–40 分钟，轻松坚持 💪';
}
document.addEventListener('change',function(e){var el=e.target;
  if(el.classList&&el.classList.contains('chk')){
    var d=el.closest('.day');var dnum=d?d.dataset.day:null;
    if(el.checked){localStorage.setItem(el.dataset.k,'1');
      if(dnum&&!localStorage.getItem('ENG::studied::d'+dnum))localStorage.setItem('ENG::studied::d'+dnum,todayStr());}
    else{localStorage.removeItem(el.dataset.k);if(dnum)localStorage.removeItem('ENG::studied::d'+dnum);}
    if(d)d.classList.toggle('done',el.checked);
    updateProgress();updateDaySelOptions();renderStudyLog();
    // 打卡完成 → 自动跳到下一天
    var view=document.getElementById('daysel').value;
    if(el.checked&&dnum&&view!=='all'&&String(view)===String(dnum)){
      var nx=Math.min(""" + str(TOTAL) + """,parseInt(dnum)+1);showDay(nx);}
  }
  if(el.classList&&el.classList.contains('mchk')){var w=el.closest('.row');if(w)w.classList.toggle('mastered',el.checked);
    el.checked?localStorage.setItem(el.dataset.k,'1'):localStorage.removeItem(el.dataset.k);}
  if(el.type==='radio'&&el.name&&el.name.indexOf('ENG::quiz')===0){localStorage.setItem(el.name,el.value);}
});
document.addEventListener('input',function(e){var el=e.target;
  if(el.classList&&el.classList.contains('tans')){localStorage.setItem(el.dataset.k,el.value);}
});
function exportEng(){var o={};for(var i=0;i<localStorage.length;i++){var k=localStorage.key(i);if(k.indexOf('ENG::')===0)o[k]=localStorage.getItem(k);}
  var b=new Blob([JSON.stringify(o,null,2)],{type:'application/json'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='英语学习进度备份.json';a.click();}
function importEng(inp){var f=inp.files[0];if(!f)return;var r=new FileReader();r.onload=function(){try{var o=JSON.parse(r.result);Object.keys(o).forEach(function(k){localStorage.setItem(k,o[k]);});location.reload();}catch(e){alert('文件有误');}};r.readAsText(f);}
window.addEventListener('DOMContentLoaded',function(){
  document.querySelectorAll('.chk,.mchk').forEach(function(c){if(localStorage.getItem(c.dataset.k)==='1'){c.checked=true;var d=c.closest('.day');if(d&&c.classList.contains('chk'))d.classList.add('done');var w=c.closest('.row');if(w&&c.classList.contains('mchk'))w.classList.add('mastered');}});
  // 恢复翻译输入
  document.querySelectorAll('.tans').forEach(function(t){var v=localStorage.getItem(t.dataset.k);if(v!=null)t.value=v;});
  // 恢复测验选择 + 已答过的自动显示解析
  document.querySelectorAll('.quiz').forEach(function(box){
    var name=box.dataset.name;var saved=localStorage.getItem(name);
    if(saved!=null){var r=box.querySelector('input[value="'+saved+'"]');if(r)r.checked=true;}
    if(localStorage.getItem(box.dataset.k+'::done')==='1'){
      var correct=parseInt(box.dataset.correct);var opts=box.querySelectorAll('.qopt');var picked=parseInt(saved);
      opts[correct].classList.add('correct');
      if(!isNaN(picked)&&picked!==correct)opts[picked].classList.add('wrong');
      box.querySelector('.qexp').classList.add('show');
    }
  });
  updateProgress();
  // 收藏夹
  refreshStars();renderFavs();
  // 学习记录 + 日期选择
  updateDaySelOptions();renderStudyLog();
  // 每日只看当天：优先用上次选择，否则定位到第一个未完成的那天
  var vd=localStorage.getItem('ENG::viewday');
  if(vd===null||vd===undefined)vd=firstIncompleteDay();
  showDay(vd);
  showTab(parseInt(localStorage.getItem('ENG::tab')||'0'));
});
// ===== 词汇表搜索 =====
function filterVocab(){
  var q=document.getElementById('vsearch').value.toLowerCase();
  document.querySelectorAll('#vocablib .vcard').forEach(function(c){
    c.style.display=c.textContent.toLowerCase().indexOf(q)>=0?'':'none';});
  document.querySelectorAll('#vocablib .theme-block').forEach(function(b){
    var any=b.querySelectorAll('.vcard').length&&Array.prototype.some.call(b.querySelectorAll('.vcard'),function(c){return c.style.display!=='none';});
    b.style.display=any?'':'none';});
}
// ===== 单词自测闪卡 =====
var FT={list:[],idx:0,know:0,dunno:0};
function buildFT(){
  var day=document.getElementById('ftday').value;var arr=[];
  VOCAB_DATA.forEach(function(w){if(day==='all'||w.d==parseInt(day))arr.push(w);});
  for(var i=arr.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=arr[i];arr[i]=arr[j];arr[j]=t;}
  FT.list=arr;FT.idx=0;FT.know=0;FT.dunno=0;renderFT();
}
function renderFT(){
  var c=document.getElementById('flashcard');
  if(!FT.list.length){c.innerHTML='<div class="fw">点「开始」抽卡</div>';document.getElementById('ftscore').textContent='';return;}
  if(FT.idx>=FT.list.length){c.innerHTML='<div class="fw">🎉 完成！</div><div class="fz">✓认识 '+FT.know+'　✗没记住 '+FT.dunno+'</div>';document.getElementById('ftscore').textContent='再点「开始 / 重练」来一轮（会重新打乱顺序）';return;}
  var w=FT.list[FT.idx];
  c.innerHTML='<div class="fw">'+w.w+'</div><div class="fpos">'+w.p+'</div>'+
    '<div class="fz" id="fback" style="display:none">'+w.z+'<div class="fex">'+w.e+'</div></div>';
  document.getElementById('ftscore').textContent='第 '+(FT.idx+1)+' / '+FT.list.length+' 个　✓认识 '+FT.know+'　✗没记住 '+FT.dunno;
}
function ftSpeak(){if(FT.list[FT.idx])speak(FT.list[FT.idx].w);}
function ftShow(){var b=document.getElementById('fback');if(b)b.style.display='block';}
function ftNext(know){if(!FT.list.length||FT.idx>=FT.list.length)return;if(know)FT.know++;else FT.dunno++;FT.idx++;renderFT();}
</script>
"""


def vocab_rows(vocab, keyprefix):
    rows = []
    for vi, (en, zh, ex) in enumerate(vocab, 1):
        k = f"{keyprefix}::v{vi}"
        fid = f"p::{en}"
        rows.append(
            f'<div class="row"><input type="checkbox" class="mchk" data-k="{k}" title="已掌握">'
            f'<button class="fav" data-fid="{esc(fid)}" data-t="phrase" data-en="{esc(en)}" data-zh="{esc(zh)}" data-ex="{esc(ex)}" title="收藏">☆</button>'
            f'<button class="spk" data-t="{esc(en)}">🔊</button>'
            f'<div><span class="en">{esc(en)}</span> — <span class="zh">{esc(zh)}</span>'
            f'<br><span class="ex" >{esc(ex)}</span> '
            f'<button class="spk" data-t="{esc(ex)}">🔊 例句</button></div></div>'
        )
    return "".join(rows)


def shadow_rows(shadow):
    rows = []
    for en, zh in shadow:
        rows.append(
            f'<div class="row"><button class="spk" data-t="{esc(en)}">🔊</button>'
            f'<div><span class="en">{esc(en)}</span><br><span class="zh">{esc(zh)}</span></div></div>'
        )
    return "".join(rows)


def song_block(song):
    title, artist, level, why, phrases = song
    q = esc(f"{title} {artist} lyrics")
    ph = "".join(
        f'<div class="row"><button class="spk" data-t="{esc(p)}">🔊</button>'
        f'<div><span class="en">{esc(p)}</span> — <span class="zh">{esc(z)}</span></div></div>'
        for p, z in phrases
    )
    return (
        f'<div class="song"><div class="t">🎵 {esc(title)} — {esc(artist)}　<span class="hint">{esc(level)}</span></div>'
        f'<div class="hint">{esc(why)}</div>'
        f'<div style="margin:6px 0"><a href="https://www.youtube.com/results?search_query={q}" target="_blank">🔎 搜 MV/音频</a>　'
        f'<a href="https://www.google.com/search?q={q}" target="_blank">🔎 搜歌词</a></div>'
        f'<div class="hint">跟唱语言点：</div>{ph}</div>'
    )


def passage_block(e):
    en, zh = e["passage"]
    pk = "".join(
        f'<div class="row"><button class="spk" data-t="{esc(p)}">🔊</button>'
        f'<div><span class="en">{esc(p)}</span> — <span class="zh">{esc(z)}</span></div></div>'
        for p, z in e["pkey"]
    )
    return (
        f'<div class="passage"><div class="en-p">{esc(en)}</div>'
        f'<div class="ptools"><button class="spk" data-t="{esc(en)}">🔊 全文朗读</button>'
        f'<button onclick="toggleZh(this)">🙈 隐藏中文</button></div>'
        f'<div class="zh-p">{esc(zh)}</div>'
        f'<div class="hint" style="margin-top:8px">重点表达：</div>{pk}</div>'
    )


def quiz_block(e, didx):
    out = []
    for qi, (q, opts, correct, exp) in enumerate(e["quiz"], 1):
        name = f"ENG::quiz::d{didx}::q{qi}"
        letters = "ABCD"
        ol = "".join(
            f'<label class="qopt"><input type="radio" name="{name}" value="{oi}"> {letters[oi]}. {esc(o)}</label>'
            for oi, o in enumerate(opts)
        )
        out.append(
            f'<div class="quiz" data-correct="{correct}" data-name="{name}" data-k="{name}">'
            f'<div class="qq">{qi}. {esc(q)}</div>{ol}'
            f'<button class="qbtn" onclick="gradeQuiz(this)">对答案</button>'
            f'<div class="qexp">✅ 正确答案：{letters[correct]}。{esc(exp)}</div></div>'
        )
    return "".join(out)


def translate_block(e, didx):
    out = []
    for ti, (zh, en) in enumerate(e["translate"], 1):
        k = f"ENG::trans::d{didx}::t{ti}"
        out.append(
            f'<div class="trans"><div class="qq">{ti}. 把下面句子译成英文：{esc(zh)}</div>'
            f'<textarea class="tans" data-k="{k}" placeholder="在此输入你的翻译…"></textarea>'
            f'<details class="tref"><summary>参考答案（先自己写，再对照）</summary>'
            f'<div class="ref"><span class="en">{esc(en)}</span> '
            f'<button class="spk" data-t="{esc(en)}">🔊</button></div></details></div>'
        )
    return "".join(out)


def vocab_cards(words, keyprefix):
    rows = []
    for wi, (w, pos, zh, ex) in enumerate(words, 1):
        k = f"{keyprefix}::w{wi}"
        fid = f"w::{w}"
        rows.append(
            f'<div class="vcard"><input type="checkbox" class="mchk" data-k="{k}" title="已掌握">'
            f'<button class="fav" data-fid="{esc(fid)}" data-t="word" data-en="{esc(w)}" data-zh="{esc(zh)}" data-ex="{esc(ex)}" title="收藏">☆</button>'
            f'<button class="spk" data-t="{esc(w)}">🔊</button>'
            f'<div style="flex:1"><span class="w">{esc(w)}</span>'
            f'<span class="pos">{esc(pos)}</span><span class="vz">{esc(zh)}</span>'
            f'<span class="vex">{esc(ex)} <button class="spk" data-t="{esc(ex)}">🔊</button></span></div></div>'
        )
    return "".join(rows)


# ---- 每日计划面板 ----
day_cards = []
for idx, d in enumerate(DAYS, 1):
    e = ENRICH[idx - 1]
    rev = ""
    if idx >= 3:
        rd = DAYS[idx - 3]
        rev = (f'<div class="rev"><b>🔁 复习：第 {idx-2} 天「{esc(rd["theme"])}」的词卡</b>'
               + vocab_rows(rd["vocab"], f"ENG::rev::d{idx}") + "</div>")
    chk = f"ENG::done::d{idx}"
    day_cards.append(
        f'<section class="day" data-day="{idx}"><div class="day-h"><span class="daynum">Day {idx}</span>'
        f'<h2>{esc(d["theme"])}</h2>'
        f'<label class="hint"><input type="checkbox" class="chk" data-k="{chk}"> 完成打卡</label></div>'
        f'<div class="sec"><h3>📖 精读短文（约 7 分钟，先读英文→朗读跟读→再看中文核对）</h3>{passage_block(e)}</div>'
        f'<div class="sec"><h3>🎯 核心词汇 · 今日 12 词（约 7 分钟，点 🔊 听，☆ 收藏，勾选=已掌握）</h3>{vocab_cards(VOCAB[idx-1], f"ENG::voc::d{idx}")}</div>'
        f'<div class="sec"><h3>🔊 实用短语（约 4 分钟，点 🔊 听发音，☆ 收藏）</h3>{vocab_rows(d["vocab"], f"ENG::d{idx}")}</div>'
        f'<div class="sec"><h3>🗣️ 影子跟读（约 3 分钟，听一句跟读一句）</h3>{shadow_rows(d["shadow"])}</div>'
        f'<div class="sec"><h3>✅ 小测验（约 3 分钟，选完点"对答案"）</h3>{quiz_block(e, idx)}</div>'
        f'<div class="sec"><h3>✍️ 翻译练习（约 3 分钟，先自己写再看参考答案）</h3>{translate_block(e, idx)}</div>'
        f'{rev}'
        f'<div class="sec"><h3>🎵 今日歌曲跟唱（约 5 分钟，放松收尾）</h3>{song_block(d["song"])}</div>'
        f'</section>'
    )

# ---- 词汇总库面板（按主题）----
lib = []
for idx, d in enumerate(DAYS, 1):
    lib.append(f'<div class="theme-block"><h3>Day {idx} · {esc(d["theme"])}</h3>{vocab_rows(d["vocab"], f"ENG::lib::d{idx}")}</div>')

# ---- 核心词汇表面板（可搜索）----
voclib = []
for idx, d in enumerate(DAYS, 1):
    voclib.append(f'<div class="theme-block"><h3>Day {idx} · {esc(d["theme"])}</h3>{vocab_cards(VOCAB[idx-1], f"ENG::voclib::d{idx}")}</div>')

# ---- 单词自测：天数下拉 + VOCAB_DATA ----
import json as _json
ft_options = "<option value='all'>全部 360 词</option>" + "".join(
    f"<option value='{idx}'>Day {idx} · {esc(d['theme'])}</option>" for idx, d in enumerate(DAYS, 1)
)
_vd = []
for di, words in enumerate(VOCAB, 1):
    for (w, pos, zh, ex) in words:
        _vd.append({"d": di, "w": w, "p": pos, "z": zh, "e": ex})
vocab_data_js = "<script>var VOCAB_DATA=" + _json.dumps(_vd, ensure_ascii=False) + ";</script>"

# ---- 每日计划：日期选择下拉 ----
day_options = "<option value='all'>📚 显示全部 30 天</option>" + "".join(
    f"<option value='{idx}'>Day {idx} · {esc(d['theme'])}</option>" for idx, d in enumerate(DAYS, 1)
)

# ---- 歌单面板 ----
songs = []
for idx, d in enumerate(DAYS, 1):
    songs.append(f'<div class="theme-block"><h3>Day {idx}</h3>{song_block(d["song"])}</div>')

html = (
    "<!DOCTYPE html><html lang='zh'><head><meta charset='utf-8'>"
    "<meta name='viewport' content='width=device-width,initial-scale=1'>"
    "<title>英语每日训练</title>" + CSS + "</head><body>"
    "<header><h1>🎧 英语每日训练 · 30 天（每天约 30–40 分钟）</h1>"
    "<div class='progwrap'><div class='progbar' id='progbar'></div></div>"
    "<div class='progtext' id='progtext'></div>"
    "<div style='margin-top:8px'><button class='util' onclick='exportEng()'>💾 导出进度</button>"
    "<button class='util' onclick=\"document.getElementById('imp').click()\">📂 导入</button>"
    "<input type='file' id='imp' accept='.json' style='display:none' onchange='importEng(this)'></div>"
    "<div class='tabs'>"
    "<button onclick='showTab(0)'>📅 每日计划</button>"
    "<button onclick='showTab(1)'>⭐ 收藏夹</button>"
    "<button onclick='showTab(2)'>🎯 词汇表</button>"
    "<button onclick='showTab(3)'>📝 单词自测</button>"
    "<button onclick='showTab(4)'>🔊 短语库</button>"
    "<button onclick='showTab(5)'>🎵 歌单</button>"
    "</div></header><main>"
    # ===== 面板 0：每日计划 =====
    "<section class='panel'>"
    "<div class='daysel-bar'><button onclick='prevDay()'>◀ 前一天</button>"
    "<select id='daysel' onchange='showDay(this.value)'>" + day_options + "</select>"
    "<button onclick='nextDay()'>后一天 ▶</button></div>"
    "<details class='studylog'><summary>📅 学习记录（点击展开，看哪天学了什么）</summary><div id='studylog'></div></details>"
    "<p class='hint'>每天流程：📖 精读短文 → 🎯 核心词汇12词 → 🔊 实用短语 → 🗣️ 影子跟读 → ✅ 小测验(自动判分) → ✍️ 翻译练习 → 🔁 复习 → 🎵 歌曲跟唱收尾 → 打卡。打完卡会自动跳到下一天 😊</p>"
    + "".join(day_cards) + "</section>"
    # ===== 面板 1：收藏夹 =====
    "<section class='panel'>"
    "<p class='hint'>点任意单词/短语前的 ☆ 即可收藏到这里。也可以手动添加你自己的内容。</p>"
    "<div class='favadd'><b>➕ 自定义添加</b>"
    "<input id='fav_en' placeholder='英文（单词/短语/句子）'>"
    "<input id='fav_zh' placeholder='中文释义/备注（可选）'>"
    "<input id='fav_ex' placeholder='例句（可选）'>"
    "<button class='util' onclick='addCustomFav()'>添加到收藏夹</button></div>"
    "<div id='favlist'></div></section>"
    "<section class='panel'><p class='hint'>360 个核心进阶词（CET-6→7000）按天归档。可搜索（英文或中文均可），勾选=已掌握。建议每天先学当天 12 词，之后用「单词自测」反复抽查。</p>"
    "<input class='vsearch' id='vsearch' placeholder='🔍 搜索单词或中文释义…' oninput='filterVocab()'>"
    "<div id='vocablib'>" + "".join(voclib) + "</div></section>"
    "<section class='panel ftpanel'><p class='hint'>闪卡自测：看英文单词 → 先自己回想中文 → 点「显示释义」核对 → 如实点 ✓认识 / ✗没记住。随时抽查，巩固记忆。</p>"
    "<div class='ftbar'><label>范围：<select id='ftday'>" + ft_options + "</select></label>"
    "<button class='util' onclick='buildFT()'>▶ 开始 / 重练</button></div>"
    "<div class='flashcard' id='flashcard'><div class='fw'>点「开始 / 重练」抽卡</div></div>"
    "<div class='ftbtns'><button class='btn-speak' onclick='ftSpeak()'>🔊 读</button>"
    "<button class='btn-show' onclick='ftShow()'>显示释义</button>"
    "<button class='btn-know' onclick='ftNext(true)'>✓ 认识</button>"
    "<button class='btn-dunno' onclick='ftNext(false)'>✗ 没记住</button></div>"
    "<div class='ftscore' id='ftscore'></div></section>"
    "<section class='panel'><p class='hint'>所有实用短语按天归档，随时点 🔊 复习；勾选表示已掌握。</p>" + "".join(lib) + "</section>"
    "<section class='panel'><p class='hint'>30 首学习者友好的歌，点链接搜 MV/歌词跟唱。</p>" + "".join(songs) + "</section>"
    + "</main>" + vocab_data_js + JS + "</body></html>"
)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print(f"done -> {OUT} ; 天数={TOTAL}")
