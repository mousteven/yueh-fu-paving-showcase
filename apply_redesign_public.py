# -*- coding: utf-8 -*-
"""岳父工程學徒網頁視覺重新設計:token系統、嵌入字型、分類導覽、局部元件美化。
只改CSS+header nav markup+nav JS,不動其餘內容文字。"""
from pathlib import Path

ROOT = Path(r"C:\Users\User\Projects\岳父工程學徒-公開版")
HTML = ROOT / "index.html"
FONTDIR = Path(r"C:\Users\User\AppData\Local\Temp\claude\C--Users-User-Projects\a8011cfe-8561-4dfd-87cd-530fe61c1b0a\scratchpad\fonts")

b64_400 = (FONTDIR / "plexmono-400.b64.txt").read_text()
b64_600 = (FONTDIR / "plexmono-600.b64.txt").read_text()
b64_700 = (FONTDIR / "plexmono-700.b64.txt").read_text()

html = HTML.read_text(encoding="utf-8")

OLD_STYLE_START = html.index("<style>")
OLD_STYLE_END = html.index("</style>") + len("</style>")
old_style_block = html[OLD_STYLE_START:OLD_STYLE_END]

new_style_block = f"""<style>
@font-face{{
  font-family:'Plex Tech'; font-style:normal; font-weight:400; font-display:swap;
  src:url(data:font/woff2;base64,{b64_400}) format('woff2');
  unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212;
}}
@font-face{{
  font-family:'Plex Tech'; font-style:normal; font-weight:600; font-display:swap;
  src:url(data:font/woff2;base64,{b64_600}) format('woff2');
  unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212;
}}
@font-face{{
  font-family:'Plex Tech'; font-style:normal; font-weight:700; font-display:swap;
  src:url(data:font/woff2;base64,{b64_700}) format('woff2');
  unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212;
}}
:root{{
  --bg:#EAE1CE;
  --surface:#DDD1B2;
  --surface-2:#CDBD9C;
  --ink:#241E19;
  --ink-soft:#5B5040;
  --line:#B5A379;
  --brick:#A0402A;
  --brick-soft:#C36C4A;
  --moss:#4C6A3B;
  --moss-soft:#7A9161;
  --amber:#A87A2A;
  --slate:#3D5468;
  --slate-soft:#6C8598;
  --font-cjk:-apple-system,BlinkMacSystemFont,"PingFang TC","Microsoft JhengHei","Noto Sans TC","Segoe UI",sans-serif;
  --font-tech:'Plex Tech',ui-monospace,"SF Mono","Cascadia Code",Consolas,monospace;
}}
@media (prefers-color-scheme: dark){{
  :root:not([data-theme="light"]){{
    --bg:#181410; --surface:#221C15; --surface-2:#2C2418;
    --ink:#EFE7D6; --ink-soft:#B7AB92; --line:#443925;
    --brick:#DD8058; --brick-soft:#B85B3D; --moss:#9BB07E; --moss-soft:#748C5C; --amber:#D7A44E;
    --slate:#8CA6BA; --slate-soft:#5E7688;
  }}
}}
:root[data-theme="dark"]{{
  --bg:#181410; --surface:#221C15; --surface-2:#2C2418;
  --ink:#EFE7D6; --ink-soft:#B7AB92; --line:#443925;
  --brick:#DD8058; --brick-soft:#B85B3D; --moss:#9BB07E; --moss-soft:#748C5C; --amber:#D7A44E;
  --slate:#8CA6BA; --slate-soft:#5E7688;
}}
*{{box-sizing:border-box;}}
html,body{{height:100%;}}
body{{
  margin:0; background:var(--bg); color:var(--ink);
  font-family:var(--font-cjk);
  display:flex; flex-direction:column;
}}
.mono{{font-family:var(--font-tech); letter-spacing:.02em;}}
h1,h2,h3{{text-wrap:balance;}}

/* top bar / grouped nav */
header{{
  display:flex; align-items:center; gap:16px; flex-wrap:wrap;
  padding:14px 20px; border-bottom:2px solid var(--ink);
  background:var(--surface);
}}
header h1{{font-size:17px; margin:0; font-weight:800; white-space:nowrap;}}
.nav{{display:flex; flex-direction:column; gap:7px; margin-left:auto; align-items:flex-end;}}
.cat-row{{display:flex; gap:6px; flex-wrap:wrap; justify-content:flex-end;}}
.cat-btn{{
  font:inherit; font-size:13.5px; font-weight:700; cursor:pointer;
  padding:8px 16px; border-radius:6px; border:1px solid var(--line);
  background:transparent; color:var(--ink-soft);
}}
.cat-btn.active{{background:var(--ink); color:var(--bg); border-color:var(--ink);}}
.tab-row{{display:flex; gap:6px; flex-wrap:wrap; justify-content:flex-end;}}
.tab-btn{{
  font:inherit; font-size:12.5px; font-weight:700; cursor:pointer;
  padding:6px 13px; border-radius:999px; border:1px solid var(--slate-soft);
  background:transparent; color:var(--slate);
}}
.tab-btn.active{{background:var(--slate); color:var(--bg); border-color:var(--slate);}}

.view{{display:none; flex:1; min-height:0;}}
.view.active{{display:flex;}}

/* ===== gallery view (continuous scroll feed) ===== */
#view-gallery{{overflow-y:auto; flex-direction:column;}}
.feed{{flex:1; padding:20px 24px 60px; max-width:920px; margin:0 auto; width:100%;}}
.dot{{width:8px; height:8px; border-radius:50%; flex:none; display:inline-block;}}
.dot.g{{background:var(--moss);}}
.dot.y{{background:var(--amber);}}
.dot.n{{background:var(--brick);}}

@media (max-width:720px){{
  header{{flex-wrap:wrap; padding:12px 14px; gap:10px;}}
  header h1{{font-size:15px;}}
  .nav{{margin-left:0; width:100%; align-items:stretch;}}
  .cat-row, .tab-row{{justify-content:flex-start; overflow-x:auto; flex-wrap:nowrap;}}
  .feed{{padding:14px 14px 60px;}}
  .grid{{grid-template-columns:repeat(auto-fill,minmax(96px,1fr)); gap:6px;}}
}}
.folder-section{{margin-bottom:36px; padding-bottom:32px; border-bottom:1px solid var(--line);}}
.folder-section:last-child{{border-bottom:none;}}
.panel-header{{margin-bottom:14px; position:relative; padding-left:14px; border-left:3px solid var(--brick);}}
.panel-header h2{{font-size:19px; margin:0 0 6px; font-weight:800; display:flex; align-items:center; gap:9px;}}
.panel-header .folder-count{{font-size:11.5px; font-weight:600; color:var(--ink-soft); font-family:var(--font-tech);}}
.panel-header p{{font-size:13.5px; color:var(--ink-soft); max-width:70ch; margin:0 0 10px;}}
.facts{{list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:5px;}}
.facts li{{
  font-size:12.5px; color:var(--ink); background:var(--surface);
  border:1px solid var(--line); border-left:3px solid var(--moss);
  padding:6px 10px; border-radius:4px; max-width:80ch;
}}
.legend{{display:flex; gap:14px; padding:10px 0 16px; font-size:11.5px; color:var(--ink-soft); flex-wrap:wrap; max-width:920px; margin:0 auto; width:100%; padding-left:24px; padding-right:24px;}}
.legend span{{display:flex; align-items:center; gap:5px;}}
@media (max-width:720px){{.legend{{padding-left:14px; padding-right:14px;}}}}

.grid{{
  display:grid; grid-template-columns:repeat(auto-fill,minmax(140px,1fr));
  gap:8px; margin-top:14px;
}}
.thumb{{
  aspect-ratio:1; border-radius:5px; overflow:hidden; cursor:pointer;
  border:1px solid var(--line); background:var(--surface-2); position:relative;
  content-visibility:auto; contain-intrinsic-size:140px 140px;
  transition:transform .15s ease;
}}
.thumb:hover{{transform:scale(1.03);}}
@media (prefers-reduced-motion:reduce){{.thumb{{transition:none;}} .thumb:hover{{transform:none;}}}}
.thumb img{{width:100%; height:100%; object-fit:cover; display:block;}}

/* lightbox */
.lightbox{{
  display:none; position:fixed; inset:0; background:rgba(10,8,6,.92);
  z-index:50; align-items:center; justify-content:center; flex-direction:column;
}}
.lightbox.open{{display:flex;}}
.lightbox img{{max-width:92vw; max-height:80vh; border-radius:4px;}}
.lightbox .lb-caption{{color:#EDE6D6; font-size:12.5px; margin-top:12px; font-family:var(--font-tech);}}
.lb-close, .lb-prev, .lb-next{{
  position:absolute; background:none; border:none; color:#EDE6D6; cursor:pointer;
  font-size:28px; padding:10px;
}}
.lb-close{{top:10px; right:16px;}}
.lb-prev{{left:8px; top:50%; transform:translateY(-50%);}}
.lb-next{{right:8px; top:50%; transform:translateY(-50%);}}

/* ===== notes view ===== */
#view-notes{{overflow-y:auto; justify-content:center;}}
.notes-wrap{{max-width:760px; padding:36px 24px 80px; line-height:1.75;}}
.notes-wrap h2{{font-size:22px; font-weight:800; margin:36px 0 10px;}}
.notes-wrap h2:first-child{{margin-top:0;}}
.notes-wrap h3{{font-size:16px; font-weight:800; margin:22px 0 8px; color:var(--brick);}}
.notes-wrap p{{margin:0 0 12px; font-size:14.5px;}}
.notes-wrap ul, .notes-wrap ol{{margin:0 0 14px; padding-left:20px; font-size:14.5px;}}
.notes-wrap li{{margin-bottom:6px;}}
.callout{{
  background:color-mix(in srgb, var(--moss) 12%, var(--surface));
  border:1px solid color-mix(in srgb, var(--moss) 40%, var(--line));
  border-left:4px solid var(--moss); border-radius:4px;
  padding:12px 16px; font-size:13.5px; margin:14px 0;
}}
.quote{{
  border-left:3px solid var(--line); padding:2px 0 2px 14px;
  color:var(--ink-soft); font-size:13.5px; margin:10px 0;
}}
table{{width:100%; border-collapse:collapse; font-size:13px; margin:12px 0 18px;}}
th{{text-align:left; font-size:11px; text-transform:uppercase; letter-spacing:.05em; color:var(--ink-soft); border-bottom:2px solid var(--ink); padding:6px 8px;}}
td{{padding:7px 8px; border-bottom:1px solid var(--line); vertical-align:top; font-variant-numeric:tabular-nums;}}
.tw{{overflow-x:auto; border:1px solid var(--line); border-radius:6px;}}
code{{background:var(--surface-2); padding:1px 5px; border-radius:3px; font-family:var(--font-tech); font-size:.92em;}}
.price-box{{
  background:var(--surface); border:1px solid var(--line); border-radius:6px; border-left:3px solid var(--slate);
  padding:16px 18px; font-family:var(--font-tech); font-size:13.5px; line-height:2; margin:12px 0;
  font-variant-numeric:tabular-nums;
}}
.callout.warn{{
  background:color-mix(in srgb, var(--brick) 10%, var(--surface));
  border-color:color-mix(in srgb, var(--brick) 40%, var(--line));
  border-left-color:var(--brick);
}}
.lede{{color:var(--ink-soft); font-size:13.5px; margin-bottom:18px;}}

/* changelog (timeline rail) */
#view-changelog{{overflow-y:auto; justify-content:center;}}
.changelog-wrap{{max-width:760px; padding:36px 24px 80px; line-height:1.7; margin:0 auto; width:100%;}}
.log-entry{{margin-bottom:0; padding:0 0 24px 20px; border-left:2px solid var(--line); position:relative;}}
.log-entry::before{{content:""; position:absolute; left:-5px; top:4px; width:8px; height:8px; border-radius:50%; background:var(--brick);}}
.log-entry:last-child{{border-left-color:transparent;}}
.log-date{{font-size:15px; font-weight:800; margin-bottom:12px; display:flex; align-items:center; gap:8px; font-family:var(--font-tech);}}
.log-date .log-new{{font-size:10px; font-weight:700; padding:2px 8px; border-radius:999px; background:var(--brick); color:#fff; font-family:var(--font-cjk);}}
.log-list{{list-style:none; margin:0; padding:0; display:flex; flex-direction:column; gap:11px;}}
.log-item{{font-size:13.5px; padding-left:16px; position:relative;}}
.log-item::before{{content:"–"; position:absolute; left:0; color:var(--ink-soft);}}
.log-tags{{display:inline-flex; gap:5px; flex-wrap:wrap; margin-left:6px; vertical-align:middle;}}
.log-tag{{font-size:10.5px; font-weight:700; padding:1px 8px; border-radius:999px; background:var(--surface-2); color:var(--moss); white-space:nowrap; display:inline-block;}}

/* workflow steps */
.flow{{display:flex; flex-direction:column; gap:0;}}
.step{{display:grid; grid-template-columns:34px 1fr; gap:0;}}
.step .rail{{position:relative;}}
.step .num{{
  font-size:12px; font-weight:700; color:var(--bg); background:var(--brick); font-family:var(--font-tech);
  border-radius:50%; width:26px; height:26px; display:flex; align-items:center; justify-content:center;
}}
.step .stem{{position:absolute; top:26px; bottom:-10px; left:12px; width:2px; background:var(--line);}}
.step:last-child .stem{{display:none;}}
.step-body{{padding:0 0 20px 14px;}}
.step-body .st-title{{font-weight:800; font-size:14.5px; margin-bottom:3px;}}
.step-body .st-desc{{font-size:13px; color:var(--ink-soft);}}

/* scope cards */
.scope-grid{{display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:14px 0;}}
@media (max-width:520px){{.scope-grid{{grid-template-columns:1fr;}}}}
.scope-card{{background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:13px 15px;}}
.scope-card .sc-title{{font-weight:800; font-size:13.5px; margin-bottom:4px; color:var(--moss);}}
.scope-card .sc-desc{{font-size:12.5px; color:var(--ink-soft);}}

.checklist{{display:flex; flex-direction:column; gap:9px; margin:14px 0;}}
.check-item{{display:grid; grid-template-columns:auto 1fr; gap:11px; background:var(--surface); border:1px solid var(--line); border-radius:7px; padding:12px 14px;}}
.check-item .ck-box{{width:16px; height:16px; border:2px solid var(--ink-soft); border-radius:4px; margin-top:2px; flex:none;}}
.check-item .ck-title{{font-weight:800; font-size:13.5px; margin-bottom:3px;}}
.check-item .ck-desc{{font-size:12.5px; color:var(--ink-soft);}}

/* tools */
.tool-card{{background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:14px 16px; margin-bottom:10px;}}
.tool-card .tc-head{{display:flex; align-items:baseline; gap:8px; margin-bottom:5px; flex-wrap:wrap;}}
.tool-card .tc-name{{font-weight:800; font-size:14.5px;}}
.tool-card .tc-tag{{font-size:10.5px; font-weight:700; padding:2px 8px; border-radius:999px; background:var(--surface-2); color:var(--ink-soft); font-family:var(--font-tech);}}
.tool-card .tc-tag.free{{color:var(--moss);}}
.tool-card .tc-desc{{font-size:13px; color:var(--ink);}}
.tool-card .tc-use{{font-size:12px; color:var(--ink-soft); margin-top:6px; font-style:italic;}}

/* quiz */
.quiz-controls{{display:flex; gap:8px; flex-wrap:wrap; margin-bottom:16px; align-items:center;}}
.chip{{
  font:inherit; font-size:12px; font-weight:700; cursor:pointer;
  padding:6px 12px; border-radius:999px; border:1px solid var(--line); background:var(--bg); color:var(--ink-soft);
}}
.chip.active{{background:var(--moss); border-color:var(--moss); color:var(--bg);}}
.shuffle-btn{{
  font:inherit; font-size:12.5px; font-weight:700; cursor:pointer; margin-left:auto;
  padding:7px 14px; border-radius:6px; border:1px solid var(--brick); background:var(--brick); color:#fff;
}}
.q-card{{background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:16px 18px; margin-bottom:12px;}}
.q-card .q-cat{{font-size:10.5px; font-weight:700; text-transform:uppercase; letter-spacing:.05em; color:var(--brick); margin-bottom:6px; font-family:var(--font-tech);}}
.q-card .q-text{{font-size:14.5px; font-weight:700; margin-bottom:10px;}}
.reveal-btn{{
  font:inherit; font-size:12.5px; font-weight:700; cursor:pointer;
  padding:7px 13px; border-radius:6px; border:1px solid var(--moss); background:transparent; color:var(--moss);
}}
.answer-box{{
  display:none; margin-top:12px; padding:11px 14px; border-radius:6px;
  background:var(--bg); border:1px solid var(--line); border-left:3px solid var(--moss);
}}
.answer-box.shown{{display:block;}}
.answer-box .a-val{{font-weight:700; font-size:14px; margin-bottom:4px; font-family:var(--font-tech);}}
.answer-box .a-explain{{font-size:12.5px; color:var(--ink-soft);}}

/* calculator */
.calc-card{{background:var(--surface); border:1px solid var(--line); border-radius:10px; padding:18px; margin-bottom:14px;}}
.calc-card h3{{margin:0 0 3px;}}
.calc-card .card-note{{font-size:12px; color:var(--ink-soft); margin:0 0 14px;}}
.field-row{{display:flex; gap:10px; margin-bottom:12px; align-items:flex-end; flex-wrap:wrap;}}
.field{{flex:1; min-width:100px;}}
.field label{{display:block; font-size:11px; color:var(--ink-soft); font-weight:700; margin-bottom:5px;}}
.field .unit{{font-size:10.5px; color:var(--ink-soft); font-weight:400;}}
input[type="number"]{{
  width:100%; font:inherit; font-size:17px; padding:10px 11px;
  border:1.5px solid var(--line); border-radius:7px; background:var(--bg); color:var(--ink);
  font-family:var(--font-tech); font-variant-numeric:tabular-nums;
}}
input:focus{{outline:2px solid var(--brick); outline-offset:1px; border-color:var(--brick);}}
.op{{font-size:17px; color:var(--ink-soft); padding-bottom:11px; flex:none;}}
.mode-toggle{{display:flex; gap:6px; margin-bottom:14px;}}
.mode-btn{{
  flex:1; font:inherit; font-size:12px; font-weight:700; cursor:pointer;
  padding:7px; border-radius:6px; border:1px solid var(--line); background:var(--bg); color:var(--ink-soft);
}}
.mode-btn.active{{background:var(--moss); color:var(--bg); border-color:var(--moss);}}
.result{{background:var(--ink); color:var(--bg); border-radius:8px; padding:14px 16px; margin-top:4px;}}
.result .r-label{{font-size:10.5px; text-transform:uppercase; letter-spacing:.07em; opacity:.65; margin-bottom:4px;}}
.result .r-value{{font-size:clamp(22px,6vw,28px); font-weight:700; font-family:var(--font-tech); font-variant-numeric:tabular-nums;}}
.result .r-value .unit{{font-size:14px; font-weight:600; opacity:.75; margin-left:4px;}}
.result .r-sub{{font-size:11.5px; opacity:.7; margin-top:5px;}}
.result-grid{{display:grid; grid-template-columns:1fr 1fr; gap:10px;}}
@media (max-width:420px){{.result-grid{{grid-template-columns:1fr;}}}}
.calc-trick{{
  background:color-mix(in srgb, var(--moss) 10%, var(--surface-2));
  border:1px solid color-mix(in srgb, var(--moss) 35%, var(--line));
  border-left:3px solid var(--moss); border-radius:5px;
  padding:9px 12px; font-size:12px; margin-top:11px; color:var(--ink);
}}
.calc-trick b{{color:var(--moss);}}

/* embedded diagram cards */
.diagram-card{{background:var(--surface); border:1px solid var(--line); border-radius:8px; padding:14px; margin-bottom:14px; overflow-x:auto;}}
.diagram-card .dc-title{{font-weight:800; font-size:13px; margin-bottom:8px; color:var(--brick);}}
.diagram-card svg{{width:100%; height:auto; display:block; max-width:520px; margin:0 auto; background:#EDF0F3; border-radius:4px;}}
details.diagram-toggle{{margin-bottom:14px;}}
details.diagram-toggle summary{{
  cursor:pointer; font-weight:800; font-size:13.5px; color:var(--brick);
  padding:10px 14px; background:var(--surface); border:1px solid var(--line); border-radius:8px;
  list-style:none;
}}
details.diagram-toggle summary::-webkit-details-marker{{display:none;}}
details.diagram-toggle summary::before{{content:"▸ "; }}
details.diagram-toggle[open] summary::before{{content:"▾ "; }}
details.diagram-toggle[open] summary{{border-radius:8px 8px 0 0; border-bottom:none;}}
details.diagram-toggle .diagram-card{{margin-bottom:0; border-radius:0 0 8px 8px; border-top:none;}}
</style>"""

assert old_style_block in html, "old style block not found verbatim"
html = html.replace(old_style_block, new_style_block)

# ---- header / nav markup ----
OLD_HEADER = """<header>
  <h1>🧱 岳父工程學徒</h1>
  <div class="tabs">
    <button class="tab-btn active" data-view="gallery" id="galleryTabBtn">相簿</button>
    <button class="tab-btn" data-view="changelog">更新日誌</button>
    <button class="tab-btn" data-view="survey">丈量作業SOP</button>
    <button class="tab-btn" data-view="calc">計算機</button>
    <button class="tab-btn" data-view="flow">產業流程</button>
    <button class="tab-btn" data-view="scope">岳父的範圍</button>
    <button class="tab-btn" data-view="checklist">獨立作業清單</button>
    <button class="tab-btn" data-view="walkthrough">新手總複習</button>
    <button class="tab-btn" data-view="global">國際借鏡</button>
    <button class="tab-btn" data-view="tools">AI工具箱</button>
    <button class="tab-btn" data-view="quiz">每日題目</button>
    <button class="tab-btn" data-view="notes">對話乾貨筆記</button>
  </div>
</header>"""

NEW_HEADER = """<header>
  <h1>🧱 岳父工程學徒</h1>
  <div class="nav">
    <div class="cat-row" id="catRow">
      <button class="cat-btn active" data-standalone="gallery" id="galleryTabBtn">相簿</button>
      <button class="cat-btn" data-standalone="changelog">更新日誌</button>
      <button class="cat-btn" data-cat="learn">學習內容</button>
      <button class="cat-btn" data-cat="practice">練習工具</button>
      <button class="cat-btn" data-cat="extra">延伸資源</button>
    </div>
    <div class="tab-row" id="tabRow"></div>
  </div>
</header>"""

assert OLD_HEADER in html, "old header block not found verbatim"
html = html.replace(OLD_HEADER, NEW_HEADER)

# ---- nav JS (replace old flat tab-switch handler) ----
OLD_NAV_JS = """// tabs
document.querySelectorAll('.tab-btn').forEach(btn=>{
  btn.addEventListener('click', ()=>{
    document.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));
    document.getElementById('view-'+btn.dataset.view).classList.add('active');
  });
});

setTabCount();
renderFeed();"""

NEW_NAV_JS = """// grouped nav: 相簿/更新日誌是獨立按鈕,其餘10個分頁分3類,點類別才展開第二排
const NAV_CATS = {
  learn:    [{view:'survey', label:'丈量作業SOP'}, {view:'flow', label:'產業流程'}, {view:'scope', label:'岳父的範圍'}, {view:'checklist', label:'獨立作業清單'}, {view:'walkthrough', label:'新手總複習'}],
  practice: [{view:'calc', label:'計算機'}, {view:'quiz', label:'每日題目'}],
  extra:    [{view:'global', label:'國際借鏡'}, {view:'tools', label:'AI工具箱'}, {view:'notes', label:'對話乾貨筆記'}],
};
const VIEW_TO_CAT = {};
Object.entries(NAV_CATS).forEach(([cat, tabs]) => tabs.forEach(t => VIEW_TO_CAT[t.view] = cat));

function switchView(view){
  document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));
  document.getElementById('view-'+view).classList.add('active');
}

function renderTabRow(cat, activeView){
  const row = document.getElementById('tabRow');
  if(!cat){ row.innerHTML=''; return; }
  row.innerHTML = NAV_CATS[cat].map(t=>`<button class="tab-btn${t.view===activeView?' active':''}" data-view="${t.view}">${t.label}</button>`).join('');
  row.querySelectorAll('.tab-btn').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      row.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
      btn.classList.add('active');
      switchView(btn.dataset.view);
    });
  });
}

document.getElementById('catRow').querySelectorAll('.cat-btn').forEach(btn=>{
  btn.addEventListener('click', ()=>{
    document.getElementById('catRow').querySelectorAll('.cat-btn').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    if(btn.dataset.standalone){
      renderTabRow(null);
      switchView(btn.dataset.standalone);
    } else {
      const cat = btn.dataset.cat;
      const tabs = NAV_CATS[cat];
      const target = tabs[0].view;
      renderTabRow(cat, target);
      switchView(target);
    }
  });
});

setTabCount();
renderFeed();"""

assert OLD_NAV_JS in html, "old nav JS block not found verbatim"
html = html.replace(OLD_NAV_JS, NEW_NAV_JS)

HTML.write_text(html, encoding="utf-8")
print("done, new size:", len(html))
