# 產生 7 個頁面（共用導覽列與頁尾）。執行：python3 build.py
P=[("index","首頁","Home"),("world","世界觀","World"),("gameplay","遊戲玩法","Gameplay"),("characters","角色圖鑑","Characters"),("compendium","遊戲圖鑑","Compendium"),("collection","作品典藏","Collection"),("about","關於我們","About")]
def page(k,title,body,head=""):
    nav="".join(f'<li><a href="{f}.html"{" aria-current=page" if f==k else ""}>{z}</a></li>' for f,z,_ in P)
    return f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}｜蝕古不化 SabotAGE</title><link rel="stylesheet" href="css/style.css"></head><body>
<header class="nav"><div class="wrap"><a class="logo" href="index.html">蝕古不化<small>SABOTAGE</small></a><nav aria-label="主選單"><ul id="menu">{nav}</ul></nav><a class="btn" href="gameplay.html">前往體驗</a><button class="menu-btn" aria-expanded="false" aria-controls="menu">選單</button></div></header>
<main>{body}</main>
<footer><div class="wrap"><div class="grid"><div><strong class="logo">蝕古不化 SABOTAGE</strong><p class="muted">原創台灣民俗恐怖桌遊。【待補：學校／系所／畢業展資訊】</p></div><ul>{"".join(f'<li><a href="{f}.html">{z}</a></li>' for f,z,_ in P[:4])}</ul><ul>{"".join(f'<li><a href="{f}.html">{z}</a></li>' for f,z,_ in P[4:])}<li>【待補：社群連結】</li></ul></div><p class="muted" style="margin-top:2rem">© 2026 蝕古不化 SabotAGE ｜畢業專題作品</p></div></footer><script src="js/main.js"></script></body></html>'''
def sh(n,t,sub=""): return f'<div class="sh"><span class="stamp">{n}</span><div><h2>{t}</h2>{f"<p class=muted>{sub}</p>" if sub else ""}</div></div>'
def ph(t,c=""): return f'<div class="ph {c}">【圖片待補】{t}</div>'
def sec(cls,n,t,inner,sub=""): return f'<section class="{cls}"><div class="wrap">{sh(n,t,sub)}{inner}</div></section>'
def head(t,sub): return f'<div class="page-head"><div class="wrap"><span class="label">機密檔案</span><h1 style="font-size:var(--fs-2xl)">{t}</h1><p class="muted">{sub}</p></div></div>'
def cards(items,cls="grid"): return f'<div class="{cls}">'+"".join(items)+'</div>'
def dcard(t,cat="",extra="",label=""): return f'<details class="card" data-cat="{cat}">'+f'<summary>{ph(t,"card")}<h3 style="margin-top:.5rem">{t}</h3></summary><div><p>{label}【內容待補】{extra}</p></div></details>'
LOREM="【文案待補】此處放入專題實際內容。"
out={}
# HOME
feat=[("動態地塊","地塊拼接建構建築"),("雙層地圖","現實與特殊空間探索"),("節氣事件","節氣影響局勢"),("HP／SAN","生存與理智系統"),("多陣營結局","選擇決定走向")]
out["index"]=('''<section class="hero"><div class="wrap split"><div><span class="label">檔案編號【待補】</span><h1>當歷史被遺忘，<br>究竟誰才是<br>真正的破壞者？</h1><p class="lead">一座被遺忘的老建築，一場關於保存與拆除的博弈。【簡介待補】</p><div class="row"><a class="btn" href="world.html">探索世界觀</a><a class="btn ghost" href="gameplay.html">了解遊戲玩法</a></div></div>'''+ph("主視覺：台灣歷史建築＋超自然氛圍","tall")+'</div></section>'
+sec("paper","壹","遊戲簡介",f'<div class="split"><p>{LOREM}遊戲類型：【待補】。核心概念：【待補】。</p>{ph("遊戲介紹圖")}</div>')
+sec("dark","貳","核心特色",cards([f'<div class="frame"><h3>{a}</h3><p class="muted">{b}</p></div>' for a,b in feat]))
+sec("crimson","參","世界觀預覽",f'<div class="split">{ph("歷史建築")}<div><p>{LOREM}</p><a class="btn ghost" href="world.html">進入世界觀</a></div></div>')
+sec("paper","肆","遊戲配件預覽",cards([ph(x,"sq") for x in["遊戲版圖","卡牌","地塊","配件"]]))
+sec("dark","伍","角色預覽",cards([ph(x,"card") for x in["保存派","拆除派","道士"]],"grid scroll-x")+'<p style="margin-top:1.5rem"><a class="btn ghost" href="characters.html">查看全部角色</a></p>')
+sec("crimson","陸","多重結局",f'<p>你的每個選擇，都會改寫這座建築的命運。{LOREM}</p>'+cards([f'<div class="frame"><h3>結局 {x}</h3><p class="muted">【待補】</p></div>' for x in"ABC"]))
+'<section class="paper"><div class="wrap" style="text-align:center"><h2>走進這座建築</h2><p style="margin:1rem 0 2rem">先認識規則，再翻閱典藏。</p><a class="btn" href="gameplay.html">前往體驗</a> <a class="btn ghost" href="collection.html">瀏覽作品典藏</a></div></section>')
# WORLD
out["world"]=(head("世界觀","現實與異常之間的歷史建築")
+'<div class="wrap" style="padding-top:2rem"><div class="chips" role="group" aria-label="空間切換"><button class="chip" data-space="real" aria-pressed="true">現實空間</button><button class="chip" data-space="spirit" aria-pressed="false">特殊空間</button></div></div>'
+sec("","壹","故事序章",f'<p>{LOREM}</p>')
+sec("dark","貳","虛構世界背景",f'<div class="split"><p>{LOREM}</p>{ph("建築插畫")}</div>')
+sec("","參","文資保存危機",f'<p>{LOREM}（勿自行編造史實，請填入專題研究資料）</p>')
+'<section><div class="wrap">'+sh("肆","主地圖探索")+f'<div class="world-real"><h3>現實空間</h3><p>{LOREM}</p>{ph("現實空間地圖","tall")}</div><div class="world-spirit"><h3>特殊空間</h3><p>{LOREM}</p>{ph("特殊空間地圖","tall")}</div></div></section>'
+sec("dark","伍","特殊空間探索",cards([dcard(f"特殊空間 {i}") for i in"一二三"])))
# GAMEPLAY
mech=["動態地塊拼接","雙層地圖探索","節氣變數","HP／SAN 生存系統","多陣營協商與衝突"]
out["gameplay"]=(head("遊戲玩法","圖解規則，一次看懂")
+sec("paper","壹","遊戲概覽",'<div class="stats">'+"".join(f'<div class="frame"><h3>【待補】</h3><p>{x}</p></div>' for x in["遊玩人數","遊戲時間","建議年齡","遊戲類型"])+'</div>')
+sec("dark","貳","遊戲目標",f'<p>{LOREM}</p>')
+sec("","參","遊戲流程",'<ol class="steps">'+"".join(f'<li><h3>【流程名稱待補】</h3><p class="muted">{LOREM}</p></li>' for _ in range(4))+'</ol>')
+sec("paper","肆","核心機制",'<div class="grid">'+"".join(dcard(m,"",f"　{ph('機制圖解')}") for m in mech)+'</div>')
+sec("dark","伍","勝利條件",f'<p>{LOREM}</p>')
+sec("crimson","陸","多重結局",f'<p>{LOREM}</p>')
+sec("paper","柒","遊戲配件總覽",cards([ph(x,"sq") for x in["版圖","卡牌","地塊","指示物"]]))
+sec("dark","捌","完整規則書",'<a class="btn" href="#">下載規則書 PDF【連結待補】</a>'))
# CHARACTERS
fac=["保存派","拆除派","地主","政府","網紅","道士","靈體"]
chips=lambda t:f'<div class="chips" data-target="{t}" role="group" aria-label="篩選"><button class="chip" data-f="all" aria-pressed="true">全部</button>'+"".join(f'<button class="chip" data-f="{f}" aria-pressed="false">{f}</button>' for f in fac)+'</div>'
out["characters"]=(head("角色圖鑑","各方勢力，各懷目的")
+sec("paper","壹","角色介紹",f'<p>{LOREM}</p>')
+sec("dark","貳","陣營分類與角色圖鑑",chips("#gal")+'<div id="gal" class="grid">'+"".join(f'<details class="card" data-cat="{f}"><summary>{ph(f+"・肖像","card")}<h3 style="margin-top:.5rem">【角色名稱待補】</h3><p class="muted">{f}</p></summary><div><p><strong>能力：</strong>【待補】</p><p><strong>個人目標：</strong>【待補】</p></div></details>' for f in fac)+'</div>')
+sec("paper","參","陣營關係圖",ph("陣營關係圖（合作／對立／中立）","tall")))
# COMPENDIUM
def gal(id,cats,n=6): return f'<div class="chips" data-target="#{id}"><button class="chip" data-f="all" aria-pressed="true">全部</button>'+"".join(f'<button class="chip" data-f="{c}" aria-pressed="false">{c}</button>' for c in cats)+f'</div><div id="{id}" class="grid">'+"".join(dcard(f"卡牌 {i+1}",cats[i%len(cats)],"　觸發條件／效果【待補】") for i in range(n))+'</div>'
tabs=[("ev","事件卡"),("it","物件卡"),("so","節氣卡"),("ti","地塊卡")]
tile='<div class="split"><div><div class="tilemap" id="tilemap">'+"".join(f'<button aria-pressed="false" data-n="地塊 {i+1}">{i+1}</button>' for i in range(12))+'</div><p style="margin-top:1rem"><button class="btn" id="toggle-state" aria-pressed="false">切換為損毀</button></p></div><div class="frame"><h3 id="tile-name">請點選地塊</h3><p id="tile-state" class="muted">完好／損毀對照【待補】</p><p>功能、擺放條件、遊戲效果【待補】</p></div></div><h3 style="margin:3rem 0 1rem">地塊總覽</h3>'+cards([ph(f"地塊 {i+1}","sq") for i in range(8)])
out["compendium"]=(head("遊戲圖鑑","事件、物件、節氣與地塊的完整檔案")
+'<section class="dark"><div class="wrap"><div class="chips" data-tabs="c" role="tablist">'+"".join(f'<button class="chip" role="tab" data-t="{i}" aria-selected="{"true" if i=="ev" else "false"}">{t}</button>' for i,t in tabs)+'</div>'
+f'<div role="tabpanel" data-group="c" id="ev">{gal("g1",["類型 A","類型 B"])}</div><div role="tabpanel" data-group="c" id="it" hidden>{gal("g2",["類型 A","類型 B"])}</div><div role="tabpanel" data-group="c" id="so" hidden>{gal("g3",["吉","凶"])}</div><div role="tabpanel" data-group="c" id="ti" hidden>{tile}</div></div></section>')
# COLLECTION
def ed(t,items): return sec("paper" if t in("包裝","視覺識別","周邊") else "dark","",'')
blocks=[("包裝",["盒裝正面／背面／側面","包裝結構展開","開箱攝影"]),("遊戲配件",["主遊戲版圖","特殊空間版圖","卡牌與地塊","指示物與配件"]),("視覺識別",["Logo","字體","色彩系統","圖形與插畫系統","品牌應用"]),("周邊",["海報","明信片","貼紙","徽章"]),("產品攝影",["整體","細節特寫","遊戲情境","桌面造景"])]
col=head("作品典藏","完整實體設計成果與品牌識別")
for i,(t,its) in enumerate(blocks):
    col+=sec("paper" if i%2==0 else "dark","一二三四五"[i],t,'<div class="editorial">'+"".join(ph(x,"tall" if j%3==0 else "") for j,x in enumerate(its))+'</div>')
out["collection"]=col
# ABOUT
out["about"]=(head("關於我們","設計理念、議題轉譯與團隊")
+"".join(sec("paper" if i%2==0 else "dark","一二三五"[i] if False else "壹貳參肆伍"[i],t,f'<p>{LOREM}</p>') for i,t in enumerate(["設計動機","設計理念","文資保存議題"]))
+sec("crimson","肆","議題轉為遊戲機制",'<div class="split"><div class="frame"><h3>真實議題</h3><p>【待補】</p></div><div class="frame"><h3>遊戲機制</h3><p>【待補】</p></div></div><p style="margin-top:1rem">'+ph("議題→機制→玩家體驗 流程圖")+'</p>')
+sec("paper","伍","設計與開發歷程",'<ol class="steps">'+"".join('<li><h3>【階段待補】</h3></li>' for _ in range(4))+'</ol>')
+sec("dark","陸","團隊成員",cards([f'<div class="tile-card">{ph("照片","sq")}<h3>【姓名】</h3><p class="muted">【職責】</p></div>' for _ in range(4)]))
+sec("paper","柒","畢業展資訊",'<div class="frame"><p>展覽名稱／時間／地點：【待補】</p></div>'))
for k,z,_ in P: open(k+".html","w",encoding="utf-8").write(page(k,z,out[k]))
