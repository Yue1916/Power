# -*- coding: utf-8 -*-
"""生成【普吉岛旅游英语速查手册】单文件 HTML：index.html
- 按场景分 tab；每句可 🔊 朗读、☆ 收藏；区分「你可以说 / 你可能听到」；每场景配实用贴士
- 自带浏览器 TTS 发音；收藏/自定义存 localStorage(命名空间 TRIP::)；适配 iPad 大字
运行： python Travel/_travel.py
"""
import os
import html as _html

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "index.html")


def esc(s):
    return _html.escape(s, quote=True)


# 每个场景：图标、名称、tip、say[(en,zh)]、hear[(en,zh)]
SCENES = [
    {"icon": "✈️", "name": "机场 & 入境",
     "tip": "入境可能被要求出示返程机票和酒店订单，提前截图备好。落地航站楼可买 AIS / True 流量卡。",
     "say": [("I'm here on holiday.", "我是来度假的。"),
              ("I'll be staying for seven days.", "我会待七天。"),
              ("I'm staying at a hotel in Patong.", "我住在芭东的一家酒店。"),
              ("Where is the baggage claim?", "行李提取处在哪里？"),
              ("Where can I get a taxi or Grab?", "哪里可以打车或叫 Grab？"),
              ("I'd like a SIM card with data, please.", "我想要一张有流量的电话卡。"),
              ("Where is the ATM?", "取款机在哪里？")],
     "hear": [("What's the purpose of your visit?", "你此行的目的是什么？"),
               ("How long will you stay?", "你会待多久？"),
               ("Where are you staying?", "你住在哪里？"),
               ("Please look at the camera.", "请看镜头。"),
               ("Do you have a return ticket?", "你有返程机票吗？")]},
    {"icon": "🚕", "name": "交通 · 打车",
     "tip": "tuk-tuk 突突车基本不打表、要砍价；强烈建议装 Grab / Bolt 打车 App，价格透明。上车前先谈好价钱。",
     "say": [("How much to Patong Beach?", "到芭东海滩多少钱？"),
              ("Can you use the meter?", "能打表吗？"),
              ("That's too expensive. Can you lower it?", "太贵了，能便宜点吗？"),
              ("Can you do two hundred baht?", "200 铢行吗？"),
              ("Please take me to this address.", "请送我到这个地址。（给他看手机）"),
              ("Please stop here.", "在这里停就行。"),
              ("Can you wait for ten minutes?", "能等我十分钟吗？")],
     "hear": [("Where are you going?", "你要去哪里？"),
               ("The meter is broken.", "表坏了。（常见说辞，可坚持或换一辆）"),
               ("Fixed price, four hundred baht.", "固定价，400 铢。"),
               ("Get in, get in.", "上车上车。")]},
    {"icon": "🏨", "name": "酒店",
     "tip": "可能收现金押金或刷卡预授权。退房前查一下迷你吧有没有被计费。",
     "say": [("I have a reservation under Yue.", "我用 Yue 这个名字订了房。"),
              ("Can I check in early?", "能提前入住吗？"),
              ("Can I leave my luggage here?", "能把行李寄存在这里吗？"),
              ("The air conditioner isn't working.", "空调坏了。"),
              ("Could I get some extra towels?", "能多给我几条毛巾吗？"),
              ("Is breakfast included?", "含早餐吗？"),
              ("Can I have a late checkout?", "能晚一点退房吗？")],
     "hear": [("May I see your passport?", "可以看一下你的护照吗？"),
               ("Here's your key card.", "这是你的房卡。"),
               ("Breakfast is from seven to ten.", "早餐时间是 7 点到 10 点。"),
               ("Checkout is at eleven.", "退房时间是 11 点。")]},
    {"icon": "🍽️", "name": "餐厅 · 点餐",
     "tip": "泰餐默认偏辣，务必说清辣度！「Not spicy, please」或泰语「mai phet（不辣）」很好用。",
     "say": [("A table for two, please.", "两位，谢谢。"),
              ("Not spicy, please.", "请不要辣。（最重要的一句）"),
              ("A little spicy is okay.", "微辣可以。"),
              ("I'm allergic to seafood.", "我对海鲜过敏。"),
              ("What do you recommend?", "你有什么推荐？"),
              ("Is this very spicy?", "这个很辣吗？"),
              ("Water, please. No ice.", "请给我水，不要冰。"),
              ("Can I get the bill, please?", "可以买单吗？")],
     "hear": [("How spicy would you like?", "要多辣？"),
               ("For here or to go?", "堂食还是打包？"),
               ("Anything to drink?", "喝点什么吗？"),
               ("Enjoy your meal.", "请慢用。")]},
    {"icon": "🛍️", "name": "购物 & 砍价",
     "tip": "夜市、步行街砍价是常态，通常从对折开始谈；装作走开往往会被叫住降价。商场/超市是明码标价，不砍。",
     "say": [("How much is this?", "这个多少钱？"),
              ("That's too expensive.", "太贵了。"),
              ("Can you give me a discount?", "能给我打个折吗？"),
              ("If I buy two, can it be cheaper?", "买两个能便宜点吗？"),
              ("I'll think about it.", "我再想想。（常能逼出低价）"),
              ("Okay, deal.", "好，成交。"),
              ("Do you take card?", "可以刷卡吗？")],
     "hear": [("Special price for you.", "给你个特价。"),
               ("How much do you want to pay?", "你想出多少钱？"),
               ("This is my last price.", "这是我的最低价了。")]},
    {"icon": "🏝️", "name": "出海 & 景点",
     "tip": "皮皮岛、斯米兰群岛是热门，建议提前 1–2 天订。问清是否含国家公园门票、午餐和酒店接送。",
     "say": [("I'd like to book an island tour.", "我想订一个海岛一日游。"),
              ("Does it include lunch and hotel pickup?", "含午餐和酒店接送吗？"),
              ("What time is the pickup?", "几点来接我？"),
              ("Is snorkeling gear included?", "含浮潜装备吗？"),
              ("I can't swim very well.", "我不太会游泳。"),
              ("Two adults, please.", "两个大人，谢谢。"),
              ("How long is the boat ride?", "坐船要多久？")],
     "hear": [("Pickup is at seven thirty in the morning.", "早上 7:30 来接。"),
               ("Please wait in the lobby.", "请在大堂等候。"),
               ("Don't forget your sunscreen.", "别忘了防晒霜。"),
               ("Please wear your life jacket.", "请穿好救生衣。")]},
    {"icon": "💆", "name": "按摩 & 海滩",
     "tip": "泰式按摩给 20–100 铢小费是惯例。海滩租伞租椅先谈好价钱和时长。",
     "say": [("How much for a one-hour Thai massage?", "泰式按摩一小时多少钱？"),
              ("Gentle, please.", "请轻一点。"),
              ("Stronger, please.", "请重一点。"),
              ("That hurts a little.", "有点疼。"),
              ("How much to rent an umbrella and a chair?", "租一把伞和一张椅子多少钱？"),
              ("For the whole day?", "是一整天吗？")],
     "hear": [("Oil or Thai massage?", "精油按摩还是泰式按摩？"),
               ("Lie down, please.", "请躺下。"),
               ("Turn over, please.", "请翻个身。"),
               ("Is the pressure okay?", "力度可以吗？")]},
    {"icon": "🆘", "name": "应急 & 求助",
     "tip": "泰国旅游警察热线 1155（讲英语）。普吉有国际医院（Bangkok Hospital Phuket）。记得备好旅游保险信息。",
     "say": [("Can you help me?", "你能帮我吗？"),
              ("Where is the nearest pharmacy?", "最近的药店在哪里？"),
              ("I have a stomachache.", "我肚子疼。"),
              ("I need medicine for diarrhea.", "我需要治腹泻的药。"),
              ("I lost my phone.", "我把手机弄丢了。"),
              ("Please call the police.", "请帮我叫警察。"),
              ("I need to go to the hospital.", "我需要去医院。"),
              ("Where is the restroom?", "洗手间在哪里？")],
     "hear": [("Are you okay?", "你还好吗？"),
               ("What happened?", "发生什么事了？"),
               ("Do you have insurance?", "你有保险吗？")]},
]

# 泰语必备：(泰语读音, 中文, 英文对应)
THAI = [
    ("Sawadee kha / khap", "你好", "Hello"),
    ("Khop khun kha / khap", "谢谢", "Thank you"),
    ("Chai", "是 / 对", "Yes"),
    ("Mai", "不 / 不是", "No"),
    ("Mai phet", "不辣", "Not spicy"),
    ("Tao rai?", "多少钱？", "How much?"),
    ("Phaeng pai", "太贵了", "Too expensive"),
    ("Aroy", "好吃", "Delicious"),
    ("Mai pen rai", "没关系 / 不客气", "No problem / You're welcome"),
    ("Khor thot", "对不起 / 借过", "Excuse me / Sorry"),
    ("Hong nam yu nai?", "洗手间在哪？", "Where is the toilet?"),
    ("Chuay duay!", "救命！/ 帮帮我！", "Help!"),
]

CSS = """
<style>
*{box-sizing:border-box;}
body{font-family:-apple-system,"Segoe UI","Microsoft YaHei",sans-serif;margin:0;background:#eef7f7;color:#13303a;line-height:1.75;}
header{position:sticky;top:0;z-index:10;background:#0e8a8a;color:#fff;padding:14px 20px;box-shadow:0 2px 6px rgba(0,0,0,.15);}
header h1{margin:0 0 4px;font-size:18px;}
header .sub{font-size:13px;opacity:.9;}
.tabs{display:flex;gap:6px;margin-top:10px;flex-wrap:wrap;}
.tabs button{border:none;background:rgba(255,255,255,.15);color:#fff;padding:8px 14px;border-radius:8px 8px 0 0;cursor:pointer;font-size:14px;}
.tabs button.active{background:#eef7f7;color:#0e8a8a;font-weight:600;}
.tabs button.fav{background:#f5c518;color:#3a2f00;}
.tabs button.fav.active{background:#ffd94a;color:#3a2f00;}
main{max-width:860px;margin:0 auto;padding:20px 16px 80px;}
.panel{display:none;} .panel.show{display:block;}
.util{background:#13a0a0;color:#fff;border:none;border-radius:8px;padding:6px 12px;cursor:pointer;font-size:13px;margin-right:6px;}
.tipbox{background:#fff8e6;border:1px solid #f0d98a;border-radius:8px;padding:10px 14px;margin:10px 0 16px;font-size:14px;}
.tipbox b{color:#8a6d00;}
.grp-h{font-size:15px;font-weight:700;margin:16px 0 6px;padding-left:4px;border-left:4px solid #0e8a8a;}
.grp-h.hear{border-left-color:#e08a00;color:#8a5a00;}
.prow{display:flex;align-items:flex-start;gap:8px;padding:8px 10px;background:#fff;border:1px solid #d7e8e8;border-radius:8px;margin:6px 0;}
.prow .pc{flex:1;}
.prow .pen{font-weight:600;font-size:15.5px;}
.prow .pzh{color:#555;display:block;margin-top:2px;}
.spk{border:1px solid #9cd0d0;background:#f0fafa;color:#0e8a8a;border-radius:14px;padding:3px 11px;cursor:pointer;font-size:13px;flex:none;}
.spk:hover{background:#dcf2f2;}
.fav{border:none;background:none;cursor:pointer;font-size:18px;color:#ccc;flex:none;line-height:1.2;padding:0 2px;}
.fav.on{color:#f5a623;}
.thai .prow .pen{font-size:17px;color:#0e8a8a;}
.hint{color:#5a7470;font-size:13px;}
/* 收藏夹 */
.favadd{background:#fff8e6;border:1px solid #f0d98a;border-radius:8px;padding:12px 14px;margin-bottom:12px;}
.favadd input{width:100%;padding:8px 10px;border:1px solid #9cd0d0;border-radius:6px;font-size:15px;margin:4px 0;}
.favrow .fdel{border:none;background:#fde8e8;color:#d1242f;border-radius:6px;padding:3px 9px;cursor:pointer;font-size:13px;flex:none;}
/* 分账记账 */
.acct-box{background:#fff;border:1px solid #d7e8e8;border-radius:10px;padding:12px 14px;margin:12px 0;}
.acct-h{font-weight:700;color:#0e8a8a;margin-bottom:8px;}
.acct-cfg{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;font-size:14px;}
.acct-cfg label{white-space:nowrap;}
.acct-cfg input{width:90px;padding:5px 8px;border:1px solid #9cd0d0;border-radius:6px;font-size:14px;margin-left:4px;}
.acct-form input,.acct-form select{padding:8px 10px;border:1px solid #9cd0d0;border-radius:6px;font-size:15px;}
.acct-form>input{width:100%;margin:4px 0;}
.acct-form-row{display:flex;gap:8px;margin:4px 0;}
.acct-form-row input{flex:1;min-width:0;}
.acct-sum{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:12px 0;}
.ac-card{background:#fff;border:1px solid #d7e8e8;border-radius:10px;padding:10px 12px;}
.ac-c-t{font-size:13px;color:#5a7470;}
.ac-c-big{font-size:20px;font-weight:800;color:#0e8a8a;margin:2px 0;}
.ac-c-big.neg{color:#d1242f;}
.ac-c-sub{font-size:12px;color:#5a7470;}
.acct-list{margin-top:8px;}
.ac-item{display:flex;align-items:center;gap:10px;background:#fff;border:1px solid #d7e8e8;border-left:4px solid #0e8a8a;border-radius:8px;padding:8px 12px;margin:6px 0;}
.ac-item.ac-A{border-left-color:#e08a00;} .ac-item.ac-B{border-left-color:#8a5ad0;}
.ac-it-main{flex:1;min-width:0;} .ac-it-desc{font-weight:600;} .ac-it-meta{display:block;font-size:12px;color:#5a7470;}
.ac-it-amt{font-weight:700;color:#13303a;flex:none;}
/* iPad 触屏大字（电脑端不受影响）*/
@media (pointer:coarse) and (min-width:768px){
  html{-webkit-text-size-adjust:100%;text-size-adjust:100%;}
  body{font-size:32px;line-height:1.9;}
  main{width:90%;max-width:none;margin:0 auto;padding:16px 0 72px;}
  header{padding:12px 16px 0;}
  header h1{font-size:32px;} header .sub{font-size:24px;}
  .tabs button{font-size:30px;padding:14px 24px;}
  .util{font-size:24px;padding:12px 20px;}
  .tipbox{font-size:27px;}
  .grp-h{font-size:30px;}
  .prow .pen{font-size:31px;}
  .prow .pzh{font-size:28px;}
  .thai .prow .pen{font-size:34px;}
  .spk{font-size:24px;padding:8px 18px;}
  .fav{font-size:34px;}
  .hint{font-size:24px;}
  .favadd input,.favrow{font-size:29px;}
  .acct-h{font-size:28px;} .acct-cfg{font-size:25px;} .acct-cfg input{width:150px;font-size:25px;}
  .acct-form input,.acct-form select{font-size:27px;}
  .ac-c-t{font-size:22px;} .ac-c-big{font-size:33px;} .ac-c-sub{font-size:21px;}
  .ac-it-desc{font-size:27px;} .ac-it-meta{font-size:21px;} .ac-it-amt{font-size:27px;}
}
@media(max-width:640px){main{padding:16px 8px 60px;}}
</style>
"""

JS = """
<script>
function speak(t){try{window.speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(t);u.lang='en-US';u.rate=0.9;window.speechSynthesis.speak(u);}catch(e){}}
document.addEventListener('click',function(e){var el=e.target;
  if(el.classList&&el.classList.contains('spk')){speak(el.dataset.t);}
  if(el.classList&&el.classList.contains('fav')){toggleFav(el);}
});
function showTab(i){
  document.querySelectorAll('.panel').forEach(function(p,x){p.classList.toggle('show',x===i);});
  document.querySelectorAll('.tabs button').forEach(function(b,x){b.classList.toggle('active',x===i);});
  localStorage.setItem('TRIP::tab',i);window.scrollTo(0,0);
}
function getFavs(){try{return JSON.parse(localStorage.getItem('TRIP::favs')||'{}');}catch(e){return {};}}
function setFavs(o){localStorage.setItem('TRIP::favs',JSON.stringify(o));}
function toggleFav(btn){var favs=getFavs();var id=btn.dataset.fid;
  if(favs[id])delete favs[id];else favs[id]={en:btn.dataset.en,zh:btn.dataset.zh||''};
  setFavs(favs);refreshStars();renderFavs();}
function removeFav(id){var favs=getFavs();delete favs[id];setFavs(favs);refreshStars();renderFavs();}
function addCustomFav(){var en=document.getElementById('fav_en').value.trim();if(!en){alert('请填写英文内容');return;}
  var favs=getFavs();favs['c::'+Date.now()]={en:en,zh:document.getElementById('fav_zh').value.trim()};
  setFavs(favs);document.getElementById('fav_en').value='';document.getElementById('fav_zh').value='';
  renderFavs();alert('已添加到收藏夹 ⭐');}
function refreshStars(){var favs=getFavs();document.querySelectorAll('.fav').forEach(function(b){
  var on=!!favs[b.dataset.fid];b.classList.toggle('on',on);b.textContent=on?'★':'☆';});}
function esc2(s){return (s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function renderFavs(){var favs=getFavs();var box=document.getElementById('favlist');if(!box)return;
  var ids=Object.keys(favs);
  if(!ids.length){box.innerHTML='<p class="hint">还没有收藏。到各场景点 ☆ 收藏常用句，或在上面自定义添加，出行时集中看这一页。</p>';return;}
  box.innerHTML=ids.map(function(id){var f=favs[id];
    return '<div class="prow"><button class="spk" data-t="'+(f.en||'').replace(/"/g,'&quot;')+'">🔊</button>'+
      '<div class="pc"><span class="pen">'+esc2(f.en)+'</span>'+(f.zh?'<span class="pzh">'+esc2(f.zh)+'</span>':'')+'</div>'+
      '<button class="fdel" onclick="removeFav(\\''+id.replace(/'/g,"\\\\'")+'\\')">✕</button></div>';}).join('');}
// ===== 旅行记账（一本 ¥20000 公款账）=====
var ACCT=null;
function acctDefault(){return {budget:20000,rate:20,cash:26000,allow:6000,items:[]};}
function acctGet(){try{return JSON.parse(localStorage.getItem('TRIP::acct')||'null');}catch(e){return null;}}
function acctSave(){localStorage.setItem('TRIP::acct',JSON.stringify(ACCT));}
function acctToday(){var d=new Date();return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2);}
function acToRmb(a,c){return c==='RMB'?a:a*ACCT.rate/100;}
function acFmt(n){return (Math.round(n*100)/100).toLocaleString();}
function acctBoot(){ACCT=acctGet()||acctDefault();
  if(ACCT.people!==undefined||ACCT.cash===undefined){ACCT=acctDefault();}
  var s=function(id,v){var el=document.getElementById(id);if(el)el.value=v;};
  s('ac_budget',ACCT.budget);s('ac_rate',ACCT.rate);s('ac_cash',ACCT.cash);s('ac_allow',ACCT.allow);
  var d=document.getElementById('ac_date');if(d&&!d.value)d.value=acctToday();
  acctRender();}
function acctCfg(){var g=function(id){return parseFloat(document.getElementById(id).value);};
  ACCT.budget=g('ac_budget')||0;ACCT.rate=g('ac_rate')||20;ACCT.cash=g('ac_cash')||0;ACCT.allow=g('ac_allow')||0;
  acctSave();acctRender();alert('设置已保存');}
function acctAdd(){var amt=parseFloat(document.getElementById('ac_amt').value);
  if(!amt||amt<=0){alert('请先填写金额');return;}
  ACCT.items.push({id:'e'+Date.now(),date:document.getElementById('ac_date').value||acctToday(),
    desc:(document.getElementById('ac_desc').value||'').trim()||'(未填用途)',amt:amt,
    cur:document.getElementById('ac_cur').value});
  acctSave();document.getElementById('ac_amt').value='';document.getElementById('ac_desc').value='';acctRender();}
function acctDel(id){if(!confirm('删除这笔记录？'))return;ACCT.items=ACCT.items.filter(function(x){return x.id!==id;});acctSave();acctRender();}
function acCard(t,big,sub,neg){return '<div class="ac-card"><div class="ac-c-t">'+t+'</div><div class="ac-c-big'+(neg?' neg':'')+'">'+big+'</div><div class="ac-c-sub">'+sub+'</div></div>';}
function acctRender(){if(!ACCT)return;
  var pubRmb=0,pubThb=0;
  ACCT.items.forEach(function(it){pubRmb+=acToRmb(it.amt,it.cur);if(it.cur==='THB')pubThb+=it.amt;});
  var allowRmb=acToRmb(ACCT.allow,'THB');
  var spentRmb=pubRmb+allowRmb;
  var leftRmb=ACCT.budget-spentRmb;
  var pubCash=ACCT.cash-ACCT.allow;
  var cashLeft=pubCash-pubThb;
  var sum=document.getElementById('ac_sum');
  if(sum)sum.innerHTML=
    acCard('预算 ¥'+acFmt(ACCT.budget),'剩 ¥'+acFmt(leftRmb),'已花 ¥'+acFmt(spentRmb)+'（含零花 ¥'+acFmt(allowRmb)+'）',leftRmb<0)+
    acCard('泰铢现金','剩 ฿'+acFmt(cashLeft),'公用现金 ฿'+acFmt(pubCash)+' · 已发零花 ฿'+acFmt(ACCT.allow),cashLeft<0)+
    acCard('公用开销(不含零花)','¥'+acFmt(pubRmb),'共 '+ACCT.items.length+' 笔 · 其中泰铢付 ฿'+acFmt(pubThb));
  var list=document.getElementById('ac_list');
  if(list){if(!ACCT.items.length){list.innerHTML='<p class="hint">还没有记账。上面「记一笔公用开销」填金额、选币种，点「加入账单」即可。</p>';}
    else{list.innerHTML=ACCT.items.slice().reverse().map(function(it){var cur=it.cur==='THB'?'฿':'¥';
      return '<div class="ac-item"><div class="ac-it-main"><span class="ac-it-desc">'+esc2(it.desc)+'</span><span class="ac-it-meta">'+it.date+'</span></div><span class="ac-it-amt">'+cur+acFmt(it.amt)+'</span><button class="fdel" onclick="acctDel(\\''+it.id+'\\')">✕</button></div>';}).join('');}}}
window.addEventListener('DOMContentLoaded',function(){
  refreshStars();renderFavs();acctBoot();
  showTab(parseInt(localStorage.getItem('TRIP::tab')||'0'));
});
</script>
"""


def prow(en, zh):
    fid = f"t::{en}"
    return (f'<div class="prow"><button class="fav" data-fid="{esc(fid)}" data-en="{esc(en)}" data-zh="{esc(zh)}" title="收藏">☆</button>'
            f'<button class="spk" data-t="{esc(en)}">🔊</button>'
            f'<div class="pc"><span class="pen">{esc(en)}</span><span class="pzh">{esc(zh)}</span></div></div>')


# 场景面板
scene_panels = []
for s in SCENES:
    say_rows = "".join(prow(en, zh) for en, zh in s["say"])
    hear_rows = "".join(prow(en, zh) for en, zh in s["hear"])
    scene_panels.append(
        "<section class='panel'>"
        f"<div class='tipbox'><b>💡 贴士：</b>{esc(s['tip'])}</div>"
        "<div class='grp-h'>🗣️ 你可以说</div>" + say_rows +
        "<div class='grp-h hear'>👂 你可能听到（练听力）</div>" + hear_rows +
        "</section>"
    )

# 泰语面板
thai_rows = "".join(
    f'<div class="prow"><button class="fav" data-fid="{esc("th::"+ph)}" data-en="{esc(ph)}" data-zh="{esc(zh+" / "+en)}" title="收藏">☆</button>'
    f'<div class="pc"><span class="pen">{esc(ph)}</span><span class="pzh">{esc(zh)}　（{esc(en)}）</span></div></div>'
    for ph, zh, en in THAI
)
thai_panel = ("<section class='panel thai'>"
              "<div class='tipbox'><b>💡 贴士：</b>句尾加 kha（女）/ khap（男）更礼貌。全程用英语也完全没问题，这几句是加分项。泰语发音朗读按钮对泰语不准，故未提供。</div>"
              + thai_rows + "</section>")

# 收藏面板
fav_panel = ("<section class='panel'>"
             "<p class='hint'>把你最可能用到的句子点 ☆ 收藏到这里，出行当天集中看、现场快速翻。也可以自定义添加。</p>"
             "<div class='favadd'><b>➕ 自定义添加</b>"
             "<input id='fav_en' placeholder='英文（你想记的句子）'>"
             "<input id='fav_zh' placeholder='中文备注（可选）'>"
             "<button class='util' onclick='addCustomFav()'>添加到收藏夹</button></div>"
             "<div id='favlist'></div></section>")

# 旅行记账面板（一本 ¥20000 公款账）
acct_panel = (
    "<section class='panel'>"
    "<div class='tipbox'><b>💰 旅行记账说明：</b>只记这 <b>¥20000 公款</b>一本账。每笔花销可记<b>人民币或泰铢</b>，按固定汇率折算累计。两对各 ฿3000（共 ฿6000）零花已从预算扣除、明细不记。记录只存本机，可在顶部「导出」备份。</div>"
    "<div class='acct-box'><div class='acct-h'>⚙️ 设置（可改）</div><div class='acct-cfg'>"
    "<label>总预算 ¥<input id='ac_budget' type='number'></label>"
    "<label>汇率 100฿=¥<input id='ac_rate' type='number' step='0.1'></label>"
    "<label>换的泰铢现金 ฿<input id='ac_cash' type='number'></label>"
    "<label>已发零花(不记账) ฿<input id='ac_allow' type='number'></label>"
    "<button class='util' onclick='acctCfg()'>保存设置</button></div></div>"
    "<div class='acct-sum' id='ac_sum'></div>"
    "<div class='acct-box'><div class='acct-h'>➕ 记一笔公用开销</div><div class='acct-form'>"
    "<input id='ac_date' type='date'>"
    "<input id='ac_desc' placeholder='用途，如 午餐 / 打车 / 门票 / 酒店'>"
    "<div class='acct-form-row'>"
    "<input id='ac_amt' type='number' placeholder='金额'>"
    "<select id='ac_cur'><option value='THB'>฿ 泰铢(现金)</option><option value='RMB'>¥ 人民币</option></select>"
    "</div><button class='util' onclick='acctAdd()'>加入账单</button></div></div>"
    "<div class='acct-list' id='ac_list'></div>"
    "</section>"
)

# tab 按钮
tab_btns = "".join(f"<button onclick='showTab({i})'>{esc(s['icon'])} {esc(s['name'])}</button>" for i, s in enumerate(SCENES))
tab_btns += f"<button onclick='showTab({len(SCENES)})'>🇹🇭 泰语必备</button>"
tab_btns += f"<button class='fav' style=\"color:inherit\" onclick='showTab({len(SCENES)+1})'>⭐ 收藏夹</button>"
tab_btns += f"<button onclick='showTab({len(SCENES)+2})'>💰 旅行记账</button>"

html = (
    "<!DOCTYPE html><html lang='zh'><head><meta charset='utf-8'>"
    "<meta name='viewport' content='width=device-width,initial-scale=1'>"
    "<title>普吉岛旅游英语速查</title>" + CSS + "</head><body>"
    "<header><h1>🏝️ 普吉岛旅游英语速查手册</h1>"
    "<div class='sub'>按场景查 · 点 🔊 听发音 · ☆ 收藏常用句 · 区分「你说 / 你听到」</div>"
    "<div style='margin-top:8px'><button class='util' onclick=\"(function(){var o={};for(var i=0;i<localStorage.length;i++){var k=localStorage.key(i);if(k.indexOf('TRIP::')===0)o[k]=localStorage.getItem(k);}var b=new Blob([JSON.stringify(o)],{type:'application/json'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='普吉旅游收藏备份.json';a.click();})()\">💾 导出收藏</button></div>"
    "<div class='tabs'>" + tab_btns + "</div></header><main>"
    + "".join(scene_panels) + thai_panel + fav_panel + acct_panel +
    "</main>" + JS + "</body></html>"
)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)
print(f"done -> {OUT} ; 场景数={len(SCENES)}")
