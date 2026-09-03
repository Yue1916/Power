# -*- coding: utf-8 -*-
"""把 学习笔记 目录下所有 .md 渲染成【单个】带两级 tab 的 HTML 学习手册。
  主 tab = 领域（文件）；子 tab = 任务说明 X.Y（文件内的 ## 小节）。
  附加：
    - 每个子 tab 可在任意位置插入「我的笔记」（自动保存）
    - 每道练习题有「我的答案」输入框（自动判分）
    - 每道练习题可「☆ 收藏」，汇总到独立的「⭐ 收藏」tab
    - 顶部可导出/导入备份（笔记 + 答案 + 收藏，存 localStorage）
输出： 学习笔记/AIF-C01-学习手册.html
更新笔记后重新运行： python 学习笔记/_render_html.py
"""
import os
import glob
import re
import json
import markdown

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_FILE = os.path.join(BASE, "AIF-C01-学习手册.html")

MD_EXT = ["tables", "fenced_code", "toc", "sane_lists"]

CSS = """
<style>
  *{box-sizing:border-box;}
  body{font-family:-apple-system,"Segoe UI","Microsoft YaHei",sans-serif;
       margin:0;color:#1f2328;background:#f4f6f8;line-height:1.7;}
  header{position:sticky;top:0;z-index:10;background:#0b5cad;color:#fff;
         padding:14px 24px 0;box-shadow:0 2px 6px rgba(0,0,0,.15);}
  header h1{margin:0 0 10px;font-size:18px;font-weight:600;}
  .tabs{display:flex;flex-wrap:wrap;gap:4px;align-items:center;}
  .tabs button{border:none;background:rgba(255,255,255,.15);color:#fff;
       padding:9px 16px;border-radius:8px 8px 0 0;cursor:pointer;font-size:14px;}
  .tabs button:hover{background:rgba(255,255,255,.28);}
  .tabs button.tab.active{background:#f4f6f8;color:#0b5cad;font-weight:600;}
  .tabs button.tab.fav{background:#f5c518;color:#3a2f00;}
  .tabs button.tab.fav.active{background:#ffd94a;color:#3a2f00;}
  .tabs .util{border-radius:8px;background:#1a73c7;font-size:13px;padding:7px 12px;}
  .tabs .util.first{margin-left:auto;}
  main{max-width:920px;margin:0 auto;padding:24px 24px 80px;}
  .panel{display:none;}
  .panel.show{display:block;}
  body.expand .panel{display:block;}
  .domain-head{background:#fff;border-radius:10px;padding:20px 32px 4px;
               box-shadow:0 1px 4px rgba(0,0,0,.06);margin-bottom:14px;}
  .subtabs{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:14px;}
  .subtabs button{border:1px solid #c3d4e6;background:#fff;color:#0b5cad;
       padding:7px 16px;border-radius:20px;cursor:pointer;font-size:13px;}
  .subtabs button:hover{background:#eaf3fc;}
  .subtabs button.active{background:#0969da;color:#fff;border-color:#0969da;font-weight:600;}
  body.expand .subtabs{display:none;}
  .subpanel{display:none;background:#fff;border-radius:10px;padding:22px 32px;
            box-shadow:0 1px 4px rgba(0,0,0,.06);}
  .subpanel.show{display:block;}
  body.expand .subpanel{display:block;margin-bottom:16px;}
  h1{border-bottom:2px solid #218bff;padding-bottom:8px;color:#0b5cad;font-size:23px;margin-top:6px;}
  h2{border-bottom:1px solid #d0d7de;padding-bottom:6px;margin-top:6px;color:#0969da;}
  h3{margin-top:22px;color:#24292f;}
  h4{margin-top:16px;color:#57606a;}
  table{border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;}
  th,td{border:1px solid #d0d7de;padding:8px 12px;text-align:left;vertical-align:top;}
  th{background:#f6f8fa;font-weight:600;}
  tr:nth-child(even){background:#fbfcfd;}
  code{background:#eff1f3;padding:2px 6px;border-radius:4px;
       font-family:Consolas,monospace;font-size:90%;}
  pre{background:#f6f8fa;padding:14px;border-radius:6px;overflow:auto;}
  pre code{background:none;padding:0;}
  blockquote{border-left:4px solid #218bff;margin:12px 0;padding:6px 16px;
             background:#f0f7ff;color:#3a4149;}
  ul,ol{padding-left:26px;}
  li{margin:4px 0;}
  strong{color:#0b5cad;}
  hr{border:none;border-top:1px solid #d0d7de;margin:26px 0;}
  a{color:#0969da;}
  details{background:#f6f8fa;border:1px solid #d0d7de;border-radius:6px;
          padding:8px 14px;margin:8px 0;}
  details[open]{background:#f0f7ff;border-color:#218bff;}
  summary{cursor:pointer;font-weight:600;color:#0b5cad;}
  details[open] summary{margin-bottom:8px;border-bottom:1px dashed #c3d4e6;padding-bottom:6px;}
  /* 我的答案 */
  .ansbox{margin:8px 0;display:flex;align-items:center;gap:8px;flex-wrap:wrap;
          background:#fffef7;border:1px dashed #e0c56b;border-radius:6px;padding:6px 12px;}
  .ansinput{width:170px;border:1px solid #c3d4e6;border-radius:6px;padding:6px 10px;font-size:14px;}
  .ansmark{font-weight:600;font-size:13px;}
  .ansmark.ok{color:#1a7f37;}
  .ansmark.no{color:#cf222e;}
  /* 题卡与收藏 */
  .qcard{position:relative;border:1px solid #e6e6e6;border-radius:8px;
         padding:14px 16px 10px;margin:14px 0;background:#fff;}
  .collectbtn{position:absolute;top:8px;right:10px;border:1px solid #e0c56b;
              background:#fffdf3;color:#8a6d00;border-radius:14px;padding:3px 12px;
              font-size:12px;cursor:pointer;}
  .collectbtn:hover{background:#fff6d8;}
  .collectbtn.active{background:#f5c518;color:#3a2f00;border-color:#e0b000;font-weight:600;}
  .qtag{font-size:13px;color:#8a6d00;font-weight:600;margin-bottom:6px;}
  .rmcollect{color:#cf222e;cursor:pointer;font-weight:600;margin-left:10px;font-size:12px;}
  .rmcollect:hover{text-decoration:underline;}
  .goreview{color:#0969da;cursor:pointer;font-weight:600;margin-left:12px;font-size:12px;}
  .goreview:hover{text-decoration:underline;}
  .qcard.flash{animation:flashbg 1.6s ease;}
  @keyframes flashbg{0%{background:#fff7cc;box-shadow:0 0 0 3px #f5c518;}100%{background:#fff;box-shadow:none;}}
  /* 课程速览目录 */
  .lesson-toc{background:#eef6ff;border:1px solid #cfe2f7;border-radius:8px;
              padding:9px 14px;margin:12px 0 18px;font-size:13px;line-height:2;}
  .toclink{color:#0969da;cursor:pointer;}
  .toclink:hover{text-decoration:underline;}
  .lesson-anchor{display:inline-block;width:0;height:0;overflow:hidden;}
  .lesson-hi{animation:lessonhi 1.6s ease;}
  @keyframes lessonhi{0%{background:#fff7cc;}100%{background:transparent;}}
  /* 行内自由笔记 */
  .gapctl{min-height:8px;line-height:1;}
  .gapadd{opacity:0;font-size:12px;color:#0969da;cursor:pointer;display:inline-block;
          padding:2px 10px;border:1px dashed #9dc3ea;border-radius:10px;background:#f5faff;
          transition:opacity .12s;}
  .subpanel:hover .gapadd{opacity:.28;}
  .gapctl:hover .gapadd{opacity:1;background:#e7f2ff;}
  .inote{width:100%;min-height:60px;border:1px solid #e0c56b;border-left:4px solid #f0b429;
         border-radius:6px;padding:8px 10px;margin:6px 0;background:#fffdf3;
         font-family:inherit;font-size:14px;resize:vertical;}
  .inote-tools{display:block;text-align:right;}
  .inote-del{font-size:12px;color:#cf222e;cursor:pointer;opacity:.7;}
  .inote-del:hover{opacity:1;}
</style>
"""

JS = """
<script>
var activeSub = {};
var curTab = 0;
var scrollPos = {};           // 记录每个 "tab_sub" 的滚动位置
function saveScroll(tab,sub){
  if(document.body.classList.contains('expand')) return;
  scrollPos[tab+'_'+sub]=window.scrollY||window.pageYOffset||0;
}
function restoreScroll(tab,sub){
  var y=scrollPos[tab+'_'+sub]||0;
  requestAnimationFrame(function(){window.scrollTo(0,y);});
}
function displaySub(i,j){       // 仅切换显示，不动滚动
  activeSub[i]=j;
  var panel=document.getElementById('p'+i);
  if(!panel) return;
  panel.querySelectorAll('.subpanel').forEach(function(sp,idx){sp.classList.toggle('show',idx===j);});
  panel.querySelectorAll('.subtabs button').forEach(function(b,idx){b.classList.toggle('active',idx===j);});
  localStorage.setItem('AIF::ui::sub'+i,j);
}
function showSub(i,j){          // 点击子 tab：先存当前子页滚动，再恢复目标子页滚动
  saveScroll(i, activeSub[i]||0);
  displaySub(i,j);
  restoreScroll(i,j);
}
function showTab(i){            // 点击主 tab：先存旧 tab 滚动，切换后恢复目标 tab 滚动
  saveScroll(curTab, activeSub[curTab]||0);
  document.body.classList.remove('expand');
  document.getElementById('expandBtn').textContent='📖 全部展开';
  document.querySelectorAll('.panel').forEach(function(p,idx){p.classList.toggle('show',idx===i);});
  document.querySelectorAll('.tabs button.tab').forEach(function(b,idx){b.classList.toggle('active',idx===i);});
  displaySub(i, activeSub[i]||0);
  curTab=i;
  restoreScroll(i, activeSub[i]||0);
  localStorage.setItem('AIF::ui::tab',i);
}
function toggleExpand(){
  var on=document.body.classList.toggle('expand');
  document.getElementById('expandBtn').textContent = on ? '🔖 单页模式' : '📖 全部展开';
  if(on){document.querySelectorAll('.tabs button.tab').forEach(function(b){b.classList.remove('active');});}
  else{showTab(parseInt(localStorage.getItem('AIF::ui::tab')||'0'));}
}

// ---- 笔记 / 答案 持久化 ----
function normLetters(s){return (String(s).match(/[A-Da-d]/g)||[]).map(function(c){return c.toUpperCase();}).sort().join('');}
function gradeAns(el){
  var mark=el.parentElement.querySelector('.ansmark');
  if(!mark) return;
  var val=normLetters(el.value), cor=el.dataset.correct||'';
  if(!val){mark.textContent='';mark.className='ansmark';return;}
  if(val===cor){mark.textContent='✓ 正确';mark.className='ansmark ok';}
  else{mark.textContent='✗ 待复习';mark.className='ansmark no';}
}
function loadPersisted(){
  document.querySelectorAll('[data-k]').forEach(function(el){
    var v=localStorage.getItem(el.dataset.k);
    if(v!==null) el.value=v;
    if(el.classList.contains('ansinput')) gradeAns(el);
  });
}
document.addEventListener('input',function(e){
  var el=e.target;
  if(el.dataset && el.dataset.k){
    localStorage.setItem(el.dataset.k, el.value);
    if(el.classList.contains('ansinput')){
      // 同一题在正文和收藏 tab 可能出现两次，同步判分
      document.querySelectorAll('.ansinput[data-k="'+el.dataset.k+'"]').forEach(function(o){if(o!==el)o.value=el.value;gradeAns(o);});
    }
  }
});

// ---- 收藏题 ----
function getCollect(){try{return JSON.parse(localStorage.getItem('AIF::collect')||'{}');}catch(e){return {};}}
function setCollect(o){localStorage.setItem('AIF::collect',JSON.stringify(o));}
function toggleCollect(btn){
  var qid=btn.dataset.qid, o=getCollect();
  if(o[qid]){ delete o[qid]; }
  else{
    var card=btn.closest('.qcard').cloneNode(true);
    var b=card.querySelector('.collectbtn'); if(b) b.remove();
    o[qid]={label:btn.dataset.qlabel||'', html:card.innerHTML};
  }
  setCollect(o); syncCollectButtons(); renderCollection();
}
function removeCollect(qid){var o=getCollect(); delete o[qid]; setCollect(o); syncCollectButtons(); renderCollection();}
function jumpAnchor(id){
  var el=document.getElementById(id); if(!el) return;
  var hdr=document.querySelector('header'); var off=(hdr?hdr.offsetHeight:0)+10;
  var y=el.getBoundingClientRect().top+window.pageYOffset-off;
  window.scrollTo({top:(y<0?0:y),behavior:'smooth'});
  var blk=el.closest('blockquote'); if(blk){blk.classList.remove('lesson-hi');void blk.offsetWidth;blk.classList.add('lesson-hi');setTimeout(function(){blk.classList.remove('lesson-hi');},1700);}
}
function gotoReview(qid){
  var m=(typeof QMAP!=='undefined')?QMAP[qid]:null; if(!m) return;
  saveScroll(curTab, activeSub[curTab]||0);
  document.body.classList.remove('expand');
  document.getElementById('expandBtn').textContent='📖 全部展开';
  document.querySelectorAll('.panel').forEach(function(p,idx){p.classList.toggle('show',idx===m[0]);});
  document.querySelectorAll('.tabs button.tab').forEach(function(b,idx){b.classList.toggle('active',idx===m[0]);});
  displaySub(m[0], m[1]);
  curTab=m[0];
  localStorage.setItem('AIF::ui::tab',m[0]);
  // 跳到该任务学习内容的开头（"任务说明 X.Y" 标题处），从头复习
  setTimeout(function(){
    var el=document.getElementById('p'+m[0]+'s'+m[1]);
    var hdr=document.querySelector('header');
    var off=(hdr?hdr.offsetHeight:0)+10;
    if(el){var y=el.getBoundingClientRect().top+window.pageYOffset-off; window.scrollTo({top:(y<0?0:y),behavior:'smooth'});}
    else{window.scrollTo({top:0,behavior:'smooth'});}
  },80);
}
function syncCollectButtons(){
  var o=getCollect();
  document.querySelectorAll('.collectbtn').forEach(function(b){
    var on=!!o[b.dataset.qid];
    b.classList.toggle('active',on);
    b.textContent = on ? '★ 已收藏' : '☆ 收藏';
  });
}
function renderCollection(){
  var o=getCollect(), list=document.getElementById('collectionList');
  if(!list) return;
  var cnt=document.getElementById('collectCount'); if(cnt) cnt.textContent=Object.keys(o).length;
  var keys=Object.keys(o);
  if(keys.length===0){ list.innerHTML='<p style="color:#6a737d">还没有收藏题目。在任意练习题右上角点“☆ 收藏”即可加入这里。</p>'; return; }
  list.innerHTML='';
  keys.forEach(function(qid){
    var item=o[qid];
    var card=document.createElement('div'); card.className='qcard';
    var hdr=document.createElement('div'); hdr.className='qtag';
    hdr.textContent='📌 '+(item.label||'');
    var go=document.createElement('span'); go.className='goreview'; go.textContent='📖 去复习';
    go.onclick=function(){gotoReview(qid);};
    var rm=document.createElement('span'); rm.className='rmcollect'; rm.textContent='✕ 移除';
    rm.onclick=function(){removeCollect(qid);};
    hdr.appendChild(go); hdr.appendChild(rm);
    var body=document.createElement('div'); body.innerHTML=item.html;
    card.appendChild(hdr); card.appendChild(body); list.appendChild(card);
  });
  loadPersisted();
}

// ---- 导出 / 导入备份 ----
function exportData(){
  var o={};
  for(var i=0;i<localStorage.length;i++){var k=localStorage.key(i);
    if(k.indexOf('AIF::')===0 && k.indexOf('AIF::ui::')!==0) o[k]=localStorage.getItem(k);}
  var blob=new Blob([JSON.stringify(o,null,2)],{type:'application/json'});
  var a=document.createElement('a'); a.href=URL.createObjectURL(blob);
  a.download='我的笔记与答案备份_AIF.json'; a.click();
}
function importData(input){
  var f=input.files[0]; if(!f) return;
  var r=new FileReader();
  r.onload=function(){
    try{var o=JSON.parse(r.result);
      Object.keys(o).forEach(function(k){localStorage.setItem(k,o[k]);});
      loadPersisted(); syncCollectButtons(); renderCollection();
      alert('导入完成，已恢复你的笔记、答案与收藏。');
    }catch(err){alert('文件格式有误，导入失败。');}
  };
  r.readAsText(f); input.value='';
}

// ---- 行内自由笔记 ----
function sig(s){var h=5381;s=s||'';for(var i=0;i<s.length;i++){h=((h*33)^s.charCodeAt(i))>>>0;}return h.toString(36);}
function makeNote(key,val){
  var box=document.createElement('div');
  var tools=document.createElement('div'); tools.className='inote-tools';
  var del=document.createElement('span'); del.className='inote-del'; del.textContent='✕ 删除';
  var ta=document.createElement('textarea'); ta.className='inote'; ta.dataset.k=key;
  ta.placeholder='我的笔记…（自动保存）'; if(val) ta.value=val;
  del.onclick=function(){localStorage.removeItem(key); box.remove();};
  tools.appendChild(del); box.appendChild(ta); box.appendChild(tools);
  return box;
}
function initInlineNotes(){
  document.querySelectorAll('.subpanel').forEach(function(sp){
    var kids=Array.from(sp.children);
    var seen={};
    function gapKey(prevText){var b=sig(prevText);seen[b]=(seen[b]||0)+1;return 'AIF::inote::'+sp.id+'::'+b+'_'+seen[b];}
    function buildGap(prevText){
      var wrap=document.createElement('div'); wrap.className='gapctl';
      var add=document.createElement('span'); add.className='gapadd'; add.textContent='➕ 加笔记';
      var key=gapKey(prevText);
      add.onclick=function(){
        if(wrap.querySelector('textarea')){wrap.querySelector('textarea').focus();return;}
        var n=makeNote(key,''); wrap.appendChild(n); n.querySelector('textarea').focus();
      };
      wrap.appendChild(add);
      var saved=localStorage.getItem(key);
      if(saved){wrap.appendChild(makeNote(key,saved));}
      return wrap;
    }
    kids.forEach(function(kid,idx){
      var prev = idx===0 ? 'TOP' : kids[idx-1].textContent.trim().slice(0,80);
      sp.insertBefore(buildGap(prev), kid);
    });
    var last = kids.length ? kids[kids.length-1].textContent.trim().slice(0,80) : 'END';
    sp.appendChild(buildGap(last));
  });
}

window.addEventListener('DOMContentLoaded',function(){
  document.querySelectorAll('.panel').forEach(function(p,i){
    activeSub[i]=parseInt(localStorage.getItem('AIF::ui::sub'+i)||'0');
  });
  loadPersisted();
  initInlineNotes();
  syncCollectButtons();
  renderCollection();
  showTab(parseInt(localStorage.getItem('AIF::ui::tab')||'0'));
});
</script>
"""


def domain_label(name):
    parts = name.split("-")
    if parts[0] == "00":
        return "总览"
    if len(parts) > 1:
        m = re.match(r"(领域\d+)", parts[1])
        if m:
            return m.group(1)
        return parts[1]
    return name


def sub_label(heading):
    h = heading.lstrip("#").strip()
    m = re.search(r"任务说明\s*(\d+\.\d+)", h)
    if m:
        return m.group(1)
    if "领域概述" in h:
        return "概述"
    return h[:12]


def split_sections(text):
    parts = re.split(r"(?m)^(##\s+.*)$", text)
    head = parts[0]
    sections = []
    for k in range(1, len(parts), 2):
        heading = parts[k]
        body = parts[k + 1] if k + 1 < len(parts) else ""
        sections.append((heading, body))
    return head, sections


def add_lesson_anchors(html, base):
    """给每一课（"第 N 课…"）加锚点，并返回可点击的「课程速览」目录条。"""
    lessons = []

    def repl(m):
        title = m.group(1).strip()
        aid = base + "L" + str(len(lessons) + 1)
        lessons.append((aid, title))
        return f'<span id="{aid}" class="lesson-anchor"></span><strong>{m.group(1)}</strong>'

    html2 = re.sub(r"<strong>(第\s*\d+\s*课[^<]*)</strong>", repl, html)
    if not lessons:
        return html2, ""
    links = " · ".join(
        f"<a class=\"toclink\" onclick=\"jumpAnchor('{aid}')\">{title}</a>"
        for aid, title in lessons
    )
    toc = f'<div class="lesson-toc">📚 本任务课程速览：{links}</div>'
    return html2, toc


def process_questions(html, name, label):
    """1) 在每个「答案解析」details 前插入「我的答案」输入框（自动判分）。
       2) 把每道练习题打包成 .qcard 并加「☆ 收藏」按钮。"""
    acount = {"n": 0}

    def ansrepl(m):
        acount["n"] += 1
        body = m.group(1)
        am = re.search(r"<strong>([^<]*)</strong>", body)
        correct = ""
        if am:
            correct = "".join(sorted(set(re.findall(r"[A-D]", am.group(1).upper()))))
        key = f"AIF::ans::{name}::{label}::q{acount['n']}"
        box = (
            '<div class="ansbox">✍️ 我的答案：'
            f'<input class="ansinput" data-k="{key}" data-correct="{correct}" '
            'placeholder="填 A/B/C/D，多选如 AC" autocomplete="off">'
            '<span class="ansmark"></span></div>'
        )
        return box + m.group(0)

    html = re.sub(
        r"<details><summary>答案[^<]*</summary>(.*?)</details>", ansrepl, html, flags=re.S
    )

    qcount = {"n": 0}
    qids = []
    dl = domain_label(name)

    def wraprepl(m):
        qcount["n"] += 1
        qid = f"{name}::{label}::q{qcount['n']}"
        qids.append(qid)
        qlabel = f"{dl} · {label} · Q{qcount['n']}"
        btn = (
            f'<button class="collectbtn" data-qid="{qid}" data-qlabel="{qlabel}" '
            'onclick="toggleCollect(this)">☆ 收藏</button>'
        )
        return f'<div class="qcard" data-qid="{qid}">{btn}{m.group(0)}</div>'

    html = re.sub(r"<p><strong>Q.*?</details>", wraprepl, html, flags=re.S)
    return html, qids


md_files = sorted(glob.glob(os.path.join(BASE, "*.md")))
panels = []
buttons = []
qmap = {}  # qid -> [tabIndex, subIndex]，供收藏 tab「去复习」跳转

for i, path in enumerate(md_files):
    name = os.path.splitext(os.path.basename(path))[0]
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    head_md, sections = split_sections(text)
    head_html = markdown.markdown(head_md, extensions=MD_EXT)

    if sections:
        subtabs = []
        subpanels = []
        for j, (heading, body) in enumerate(sections):
            label = sub_label(heading)
            sec_html = markdown.markdown(heading + "\n" + body, extensions=MD_EXT)
            sec_html, qids = process_questions(sec_html, name, label)
            sec_html, toc_html = add_lesson_anchors(sec_html, f"p{i}s{j}")
            if toc_html:
                if "</h2>" in sec_html:
                    sec_html = sec_html.replace("</h2>", "</h2>" + toc_html, 1)
                else:
                    sec_html = toc_html + sec_html
            for qid in qids:
                qmap[qid] = [i, j]
            subtabs.append(f'<button onclick="showSub({i},{j})">{label}</button>')
            subpanels.append(f'<div class="subpanel" id="p{i}s{j}">{sec_html}</div>')
        inner = (
            f'<div class="domain-head">{head_html}</div>'
            f'<div class="subtabs">{"".join(subtabs)}</div>'
            f'{"".join(subpanels)}'
        )
    else:
        inner = f'<div class="domain-head">{head_html}</div>'

    panels.append(f'<section class="panel" id="p{i}">{inner}</section>')
    buttons.append(f'<button class="tab" onclick="showTab({i})">{domain_label(name)}</button>')

# 收藏 tab（放在最后）
fav_index = len(md_files)
buttons.append(f'<button class="tab fav" onclick="showTab({fav_index})">⭐ 收藏</button>')
panels.append(
    f'<section class="panel" id="p{fav_index}">'
    '<div class="domain-head"><h1>⭐ 我的收藏题</h1>'
    '<p>已收藏 <strong id="collectCount">0</strong> 道题。在任意练习题右上角点“☆ 收藏”加入；'
    '这里可直接作答、看解析、点“✕ 移除”。收藏会随顶部“导出”一起备份。</p></div>'
    '<div id="collectionList"></div></section>'
)

utils = (
    "<button class='util first' id='expandBtn' onclick='toggleExpand()'>📖 全部展开</button>"
    "<button class='util' onclick='exportData()'>💾 导出</button>"
    "<button class='util' onclick=\"document.getElementById('impf').click()\">📂 导入</button>"
    "<input type='file' id='impf' accept='.json' onchange='importData(this)' style='display:none'>"
)

html = (
    "<!DOCTYPE html><html lang='zh'><head><meta charset='utf-8'>"
    "<meta name='viewport' content='width=device-width,initial-scale=1'>"
    "<title>AIF-C01 学习手册</title>" + CSS + "</head><body>"
    "<header><h1>AWS Certified AI Practitioner (AIF-C01) 学习手册</h1>"
    "<div class='tabs'>" + "".join(buttons) + utils + "</div></header>"
    "<main>" + "".join(panels) + "</main>"
    "<script>var QMAP=" + json.dumps(qmap, ensure_ascii=False) + ";</script>"
    + JS + "</body></html>"
)

with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

# 同时输出 index.html（用于 GitHub Pages，网址更简洁）
with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

print(f"done: {len(md_files)} md -> {OUT_FILE} (+ index.html)")
