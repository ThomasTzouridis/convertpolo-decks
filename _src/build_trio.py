# -*- coding: utf-8 -*-
"""ConvertPolo lead deck, C&F slide order, three design templates.
Usage: py build_trio.py specs/<slug>.json  ->  <slug>-a/ (Ledger), <slug>-b/ (Night), <slug>-c/ (Swiss)"""
import json, sys, html as H
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
SRC = Path(__file__).resolve().parent; REPO = SRC.parent
S = json.load(open(sys.argv[1], encoding="utf-8")); e = H.escape
C = e(S["company"])

STEPS = [("Research", "Analytics, session recordings, voice of customer"), ("Hypotheses", "Ranked by expected impact and speed"),
         ("Design and build", "Our designers and developers, not your roadmap"), ("QA and launch", "Every test verified before a visitor sees it"),
         ("Analyze", "Statistical significance, not gut feeling"), ("Iterate", "Winners roll out, learnings feed the next test")]
TEAM = [("anirban", "Anirban Chakraborty", "Founder & CEO"), ("saurabh", "Saurabh Patwa", "Co-Founder"),
        ("ansuya", "Ansuya Poudel", "Brand & Growth"), ("ankita", "Ankita Daga", "UX UI Design Lead")]
CASES = [("anothersole_big.jpg", "Anothersole", "+185%", "Revenue", "Footwear D2C. Rebuilt product discovery and the shopping journey.", "https://convertpolo.com/casestudies/anothersole-product-discovery-improvement/"),
         ("roshambo_big.jpg", "Roshambo", "+36.13%", "Revenue per visitor", "Eyewear. Targeted UX experiments across the store.", "https://convertpolo.com/casestudies/how-roshambo-boosted-revenue-per-visitor-by-36-13-with-targeted-ux-experiments/"),
         ("theater_big.jpg", "Theater", "+38%", "Revenue per visitor", "Fashion. Mobile experience redesign.", "https://convertpolo.com/casestudies/theater-mobile-experience-redesign/"),
         ("beyondbyvera_big.png", "Beyond by Vera", "+53%", "Conversion", "Premium fashion. Slide-out cart and a timed recovery popup.", "https://convertpolo.com/casestudies/beyond-by-vera/")]
LOGOS = ["l1", "l2", "l3", "l4", "l5", "l6", "l7", "l8", "l9", "l11", "l12", "l14", "l15", "l16", "l17", "l18", "l19", "l113"]
WHO = ("ConvertPolo only does conversion. We run the whole experimentation program for e-commerce and D2C brands, "
       "from research and hypotheses to design, development, QA and analysis, as an extension of your team.")
WHO_FACTS = [("120+", "online shops under CRO management"), ("VWO", "official agency partner"), ("Month 3", "when test results typically start to show")]

A = "../assets/"
cp_logo = f'<img class="cplogo" src="{A}logo.svg" alt="ConvertPolo">'
lead_logo = f'<img class="leadlogo" src="{A}{S["logo"]}" alt="{C}">'
pts = S["points"]

def sec(inner, cls="", n=None, theme=""):
    num = f'<span class="pg">{n:02d}</span>' if n else ""
    return f'<section class="{cls}"><div class="in">{inner}</div><div class="foot">{cp_logo}<span>ConvertPolo × {C}</span>{num}</div></section>'

def h(title, kicker=""):
    k = f'<p class="kick">{kicker}</p>' if kicker else ""
    return f'{k}<h2>{title}</h2>'

def slides(theme):
    hl = {"a": "<em>{}</em>", "b": '<span class="hl">{}</span>', "c": '<span class="hl">{}</span>'}[theme]
    out = []
    # 1 cover
    if theme == "a":
        out.append(f'''<section class="cover"><div class="in"><div class="brand">{cp_logo}<i></i>{lead_logo}</div>
<div class="cv"><p class="kick">A conversion read, October 2026</p><h1>Prepared for<br><em>{e(S["full_name"])}</em></h1><p class="who">{e(S["role"])}, {C}</p></div>
<figure class="hero"><img src="{A}{S["shot"]}" alt=""><figcaption>{e(S["domain"])}, homepage</figcaption></figure></div></section>''')
    elif theme == "b":
        out.append(f'''<section class="cover"><div class="glow"></div><div class="in"><div class="brand">{cp_logo}<i>×</i>{lead_logo}</div>
<div class="cv"><p class="kick">// conversion read · {e(S["domain"])}</p><h1>Prepared for {e(S["full_name"])}</h1><p class="who">{e(S["role"])}, {C}</p></div>
<div class="browser"><div class="bar"><b></b><b></b><b></b><span>{e(S["domain"])}</span></div><img src="{A}{S["shot"]}" alt=""></div></div></section>''')
    else:
        out.append(f'''<section class="cover"><div class="band"><div class="brand"><img class="cplogo" src="{A}logo_white.svg" alt="ConvertPolo"></div><div class="cv"><p class="kick">Conversion read</p><h1>Prepared for {e(S["full_name"])}</h1><p class="who">{e(S["role"])}, {C}</p></div><p class="date">October 2026</p></div>
<div class="right"><div class="ll">{lead_logo}</div><img class="shot" src="{A}{S["shot"]}" alt=""></div></section>''')
    # 2 what we saw
    saw = f'<p>{e(S["saw"][0])}</p><p>{e(S["saw"][1])}</p><p class="key">{hl.format(e(S["saw"][2]))}</p>'
    out.append(sec(f'{h("What we saw at <span class=co>" + C + "</span>", "01 · First look")}<div class="saw"><div class="txt">{saw}</div><div class="pic"><img src="{A}{S["shot"]}" alt=""></div></div>', "s-saw", 2))
    # 3 where it could convert harder
    pp = "".join(f'<div class="pt"><span class="no">0{i+1}</span><h3>{e(p["head"])}</h3><p>{e(p["text"])}</p></div>' for i, p in enumerate(pts))
    st = "".join(f'<div class="st"><b>{v}</b><span>{e(l)}</span><small>{e(s)}</small></div>' for v, l, s in S["stats"])
    out.append(sec(f'{h("Where " + e(S["domain"]) + " could convert harder", "02 · Findings")}<div class="find"><div class="pts">{pp}</div><div class="side"><div class="phone"><img src="{A}{S["shot_mobile"]}" alt=""></div><div class="stats">{st}</div></div></div>', "s-find", 3))
    # 4 how we could help
    tt = "".join(f'<div class="tt"><span class="no">Test 0{i+1}</span><h3>{e(t["head"])}</h3><p>{e(t["text"])}</p><p class="metric"><span>Measured by</span>{e(t["metric"])}</p></div>' for i, t in enumerate(S["tests"]))
    out.append(sec(f'{h("How we could help " + C, "03 · First tests")}<div class="tests">{tt}</div><div class="math"><p>{e(S["math"])}</p><p class="note">{e(S["tests_note"])}</p></div>', "s-help", 4))
    # 5 who we are
    tm = "".join(f'<div class="m"><img src="{A}team/{f}.png" alt="{n}"><b>{n}</b><span>{r}</span></div>' for f, n, r in TEAM)
    wf = "".join(f'<div class="wf"><b>{v}</b><span>{l}</span></div>' for v, l in WHO_FACTS)
    out.append(sec(f'{h("Who we are", "04 · ConvertPolo")}<div class="who2"><div><p class="lead">{WHO}</p><div class="wfs">{wf}</div></div><div class="team">{tm}</div></div>', "s-who", 5))
    # 6 how we work together
    sp = "".join(f'<div class="step"><span class="no">0{i+1}</span><b>{a}</b><p>{b}</p></div>' for i, (a, b) in enumerate(STEPS))
    out.append(sec(f'{h("How we work together", "05 · The program")}<p class="lead">Fully managed. You approve, we run everything else, one test after the next.</p><div class="steps">{sp}</div>', "s-work", 6))
    # 7 some of our work
    cs = "".join(f'<a class="case" href="{u}" target="_blank"><div class="ci"><img src="{A}cs/{img}" alt=""></div><div class="ct"><b>{lift}</b><em>{e(m)}</em><span>{e(n)}</span><p>{e(t)}</p></div></a>' for img, n, lift, m, t, u in CASES)
    lg = "".join(f'<img src="{A}clients/{l}.png" alt="">' for l in LOGOS)
    out.append(sec(f'{h("Some of our work", "06 · Results")}<div class="cases">{cs}</div><div class="logos"><div class="track">{lg}{lg}</div></div>', "s-cases", 7))
    # 8 let's talk
    sd = S["sender"]
    out.append(sec(f'''{h("Let's talk about " + C + " × ConvertPolo", "07 · Next step")}<div class="talk"><div><p class="big">{e(S["talk_text"])}</p>
<a class="btn" href="{S["booking_url"]}" target="_blank">Book a call</a><p class="contact">{e(S["booking_url"].replace("https://", ""))}<br>convertpolo.com</p></div>
<div class="card"><img src="{A}{sd["photo"]}" alt=""><b>{e(sd["name"])}</b><span>{e(sd["role"])}</span><div class="pair">{lead_logo}<i></i>{cp_logo}</div></div></div>''', "s-talk", 8))
    return out

BASE = """
.reveal .slides section{text-align:left;padding:0;width:1280px;height:720px;box-sizing:border-box}
.reveal .slides section .in{position:absolute;left:80px;right:80px;top:56px;bottom:74px}
.reveal h1,.reveal h2,.reveal h3{text-transform:none;margin:0}
.reveal p{margin:0 0 12px}
.foot{position:absolute;left:80px;right:80px;bottom:26px;display:flex;gap:18px;align-items:center;font-size:12px}.foot .cplogo{height:17px}.foot .pg{margin-left:auto;margin-right:56px}
.kick{font-size:12px!important;letter-spacing:.14em;text-transform:uppercase;margin-bottom:10px!important}
.saw{display:grid;grid-template-columns:1fr 1.15fr;gap:56px;align-items:start;margin-top:26px}.saw .txt p{font-size:20px;line-height:1.5}
.saw .pic img{width:100%;display:block}
.find{display:grid;grid-template-columns:1fr 330px;gap:44px;margin-top:22px}.pts{display:grid;grid-template-columns:1fr 1fr;gap:26px 34px}
.pt h3{font-size:19px;line-height:1.2;margin:4px 0 6px}.pt p{font-size:14px;line-height:1.48}.pt .no{font-size:12px}
.side{display:grid;grid-template-columns:130px 1fr;gap:18px}.phone img{width:130px;height:282px;object-fit:cover;object-position:top;display:block}
.stats{display:grid;gap:12px}.st b{display:block;font-size:30px;line-height:1}.st span{display:block;font-size:12.5px;line-height:1.3;margin-top:3px}.st small{display:block;font-size:10.5px;margin-top:1px}
.tests{display:grid;grid-template-columns:repeat(3,1fr);gap:28px;margin-top:26px}.tt h3{font-size:22px;margin:6px 0 10px}.tt p{font-size:15.5px;line-height:1.5}
.metric span{display:block;font-size:11px;letter-spacing:.12em;text-transform:uppercase;margin-bottom:2px}.metric{font-size:14.5px!important}
.math{margin-top:30px}.math p{font-size:18px;max-width:900px}.math .note{font-size:14px}
.who2{display:grid;grid-template-columns:1fr 1fr;gap:60px;margin-top:24px}.lead{font-size:19px;line-height:1.5;max-width:620px}
.wfs{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:22px}.wf b{display:block;font-size:30px}.wf span{display:block;font-size:13px;line-height:1.35;margin-top:4px}
.team{display:grid;grid-template-columns:1fr 1fr;gap:22px}.m{display:grid;grid-template-columns:72px 1fr;grid-template-rows:auto auto;column-gap:14px;align-items:end}
.m img{grid-row:span 2;width:72px;height:72px;object-fit:cover;object-position:top;filter:grayscale(1)}.m b{font-size:15px}.m span{font-size:12.5px;align-self:start}
.steps{display:grid;grid-template-columns:repeat(6,1fr);gap:20px;margin-top:36px}.step b{display:block;font-size:17px;margin:8px 0 6px}.step p{font-size:14px;line-height:1.45}
.cases{display:grid;grid-template-columns:repeat(4,1fr);gap:22px;margin-top:22px}.case{display:block;text-decoration:none}.ci{height:150px;overflow:hidden}.ci img{width:100%;height:100%;object-fit:cover;object-position:top;display:block}
.ct{padding-top:12px}.ct b{font-size:30px;margin-right:6px}.ct em{font-style:normal;font-size:11px;letter-spacing:.1em;text-transform:uppercase}.ct span{display:block;font-weight:700;font-size:15px;margin-top:4px}.ct p{font-size:13px;line-height:1.4;margin-top:3px}
.logos{margin-top:30px;overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent);mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent)}
.logos .track{display:flex;gap:54px;width:max-content;animation:cl 50s linear infinite;align-items:center}.logos img{height:28px;width:auto;filter:grayscale(1)}
@keyframes cl{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.talk{display:grid;grid-template-columns:1.3fr 1fr;gap:70px;margin-top:30px}.big{font-size:24px!important;line-height:1.45;max-width:560px;margin-bottom:28px!important}
.btn{display:inline-block;text-decoration:none;font-size:18px;padding:16px 36px}.contact{font-size:14px;margin-top:18px!important;line-height:1.6}
.card{display:grid;justify-items:start;gap:4px}.card>img{width:150px;height:150px;object-fit:cover;object-position:top;filter:grayscale(1);margin-bottom:10px}.card b{font-size:18px}.card span{font-size:14px}
.pair{display:flex;align-items:center;gap:20px;margin-top:26px}.pair img{height:26px}.pair i{width:1px;height:30px}
.leadlogo{height:34px;width:auto}
.s-help .tests{margin-top:40px;gap:34px}.s-help .tt h3{font-size:26px;margin:10px 0 14px}.s-help .tt p{font-size:17.5px}.s-help .metric{font-size:16px!important;margin-top:18px!important}
.s-help .math{margin-top:48px}.s-help .math p{font-size:26px;line-height:1.35;max-width:1000px}.s-help .math .note{font-size:16px;margin-top:8px}
.s-who .who2{margin-top:44px}.s-who .lead{font-size:22px}.s-who .wfs{margin-top:48px}.s-who .wf b{font-size:40px}.s-who .wf span{font-size:15px}
.s-who .wf b{font-size:34px;white-space:nowrap}.s-who .who2{grid-template-columns:1fr 1.05fr;gap:48px}
.s-who .team{gap:40px 22px}.s-who .m{grid-template-columns:104px 1fr;column-gap:16px}.s-who .m img{width:104px;height:104px}.s-who .m b{font-size:18px}.s-who .m span{font-size:14.5px}
.s-work .lead{margin-top:28px;font-size:22px;max-width:900px}.s-work .steps{margin-top:56px}.s-work .step{min-height:230px;box-sizing:border-box}
.s-work .step .no{font-size:38px!important;line-height:1}.s-work .step b{font-size:21px;margin:18px 0 10px}.s-work .step p{font-size:16px}
.s-cases .ci{height:230px}.s-cases .ct b{font-size:36px}.s-cases .ct p{font-size:14.5px}.s-cases .logos{margin-top:44px}.s-cases .logos img{height:34px}
.s-talk .talk{margin-top:56px}.s-talk .big{font-size:32px!important;max-width:640px;margin-bottom:40px!important}.s-talk .btn{font-size:21px;padding:20px 44px}
.s-talk .card>img{width:210px;height:210px}.s-talk .card b{font-size:22px}.s-talk .card span{font-size:16px}
"""

THEMES = {
"a": ("Ledger", "https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;1,9..144,400;1,9..144,600&family=Inter:wght@400;500;600&display=swap", """
:root{--bg:#F3EEE4;--ink:#16302A;--acc:#C4532F;--mut:#6E6A5E;--rule:#D8CFBE}
.reveal{font-family:Inter,sans-serif;color:var(--ink)}.reveal .slides section{background:var(--bg)}
.reveal h1,.reveal h2,.reveal h3{font-family:Fraunces,serif;font-weight:600;color:var(--ink);letter-spacing:-.01em}
.reveal h2{font-size:44px;line-height:1.08;padding-bottom:18px;border-bottom:1px solid var(--ink)}.reveal h2 .co{font-style:italic;font-weight:400;color:var(--acc)}
.reveal p{color:#2C3B36}.kick{color:var(--acc)}.foot{color:var(--mut);border-top:1px solid var(--rule);padding-top:12px;bottom:20px}.foot .pg{font-family:Fraunces,serif;font-size:15px;color:var(--ink)}
.cover .brand{display:flex;align-items:center;gap:22px}.cover .brand .cplogo{height:30px}.cover .brand i{width:1px;height:34px;background:var(--ink)}
.cover .cv{position:absolute;left:0;top:170px;width:520px}.cover h1{font-size:68px;line-height:1.02;font-weight:400}.cover h1 em{color:var(--acc);font-weight:400}
.cover .who{font-size:19px;margin-top:22px!important;color:var(--mut)}
.cover .hero{position:absolute;right:0;top:96px;width:560px;margin:0}.cover .hero img{width:100%;display:block;border:1px solid var(--ink);padding:10px;background:#fff}
.cover .hero figcaption{font-size:12px;color:var(--mut);margin-top:10px;font-style:italic;font-family:Fraunces,serif}
.saw .key{border-left:3px solid var(--acc);padding-left:22px;font-family:Fraunces,serif;font-size:23px!important;line-height:1.4!important}.saw .key em{font-style:italic;color:var(--ink)}
.saw .pic img{border:1px solid var(--ink);padding:8px;background:#fff}
.pt{border-top:1px solid var(--ink);padding-top:10px}.pt .no,.tt .no,.step .no{font-family:Fraunces,serif;font-style:italic;color:var(--acc);font-size:16px}
.phone img{border:1px solid var(--ink);border-radius:16px;padding:5px;background:#fff}.st{border-top:1px solid var(--rule);padding-top:8px}.st b{font-family:Fraunces,serif;font-weight:600;color:var(--acc)}.st small{color:var(--mut)}
.tt{border-top:1px solid var(--ink);padding-top:14px}.metric span{color:var(--acc)}.math{border-top:1px solid var(--rule);padding-top:18px}.math p{font-family:Fraunces,serif;font-size:21px}.math .note{font-family:Inter;color:var(--mut)}
.wf{border-top:1px solid var(--ink);padding-top:10px}.wf b{font-family:Fraunces,serif;color:var(--acc);font-weight:600}.m img{border-radius:50%}.m span{color:var(--mut)}
.step{border-top:1px solid var(--ink);padding-top:12px}.step p{color:var(--mut)}
.ci{border:1px solid var(--ink)}.ct b{font-family:Fraunces,serif;color:var(--acc)}.ct em{color:var(--mut)}.ct span,.case{color:var(--ink)}.ct p{color:var(--mut)}.logos img{opacity:.55}
.big{font-family:Fraunces,serif}.btn{background:var(--ink);color:var(--bg);font-family:Fraunces,serif;font-style:italic}.contact{color:var(--mut)}
.card>img{border-radius:50%}.card span{color:var(--mut)}.pair i{background:var(--ink)}
.reveal .controls{color:var(--acc)}.reveal .progress{color:var(--acc)}
"""),
"b": ("Night", "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap", """
:root{--bg:#0C0D12;--panel:#15161E;--line:#262833;--ink:#ECEAE4;--mut:#8C8C98;--acc:#8F7CFF;--acc2:#3DDC97}
.reveal{font-family:"Space Grotesk",sans-serif;color:var(--ink)}.reveal .slides section{background:var(--bg)}
.reveal h1,.reveal h2,.reveal h3{font-family:"Space Grotesk",sans-serif;font-weight:700;color:var(--ink);letter-spacing:-.025em}
.reveal h2{font-size:42px;line-height:1.08}.reveal h2 .co{color:var(--acc)}.reveal p{color:#C9C7C1}
.kick,.no,.metric span,.st small,.foot span,.ct em{font-family:"JetBrains Mono",monospace!important}.kick{color:var(--acc2);letter-spacing:.06em}
.foot{color:var(--mut)}.foot .pg{font-family:"JetBrains Mono";color:var(--acc)}
.leadlogo{filter:brightness(0) invert(1)}
.cover{overflow:hidden}.cover .glow{position:absolute;width:900px;height:900px;left:180px;top:-420px;background:radial-gradient(circle,rgba(143,124,255,.35),transparent 60%)}
.cover .brand{display:flex;align-items:center;gap:18px;color:var(--mut);font-family:"JetBrains Mono"}.cover .brand .cplogo{height:28px}.cover .brand i{font-style:normal}
.cover .cv{position:absolute;left:0;top:96px;width:100%;text-align:center}.cover h1{font-size:62px;line-height:1.05}.cover .who{font-size:18px;color:var(--mut);margin-top:12px!important}
.browser{position:absolute;left:150px;right:150px;top:330px;height:420px;border:1px solid var(--line);border-radius:14px 14px 0 0;overflow:hidden;background:var(--panel);box-shadow:0 -20px 80px rgba(143,124,255,.25)}
.browser .bar{height:34px;display:flex;align-items:center;gap:7px;padding:0 14px;border-bottom:1px solid var(--line)}.browser .bar b{width:10px;height:10px;border-radius:50%;background:#3A3C48}
.browser .bar span{margin-left:16px;font-family:"JetBrains Mono";font-size:12px;color:var(--mut)}.browser img{width:100%;display:block}
.saw .key .hl{display:block;background:var(--panel);border:1px solid var(--acc);border-radius:12px;padding:18px 22px;color:var(--ink);font-size:19px;line-height:1.45}
.saw .pic img{border:1px solid var(--line);border-radius:12px}
.pt,.tt,.step,.wf{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:16px 18px}.pts{gap:16px}.pt h3{font-size:18px}.pt p{font-size:13.5px}.no{color:var(--acc);font-size:12px}
.phone img{border:1px solid var(--line);border-radius:18px}.st b{color:var(--acc2);font-weight:700}.st span{color:var(--ink)}.st small{color:var(--mut)}
.tt .no{color:var(--acc)}.metric{border-top:1px dashed var(--line);padding-top:10px}.metric span{color:var(--acc2)}.math p{color:var(--ink)}.math .note{color:var(--mut)}
.wf b{color:var(--acc2)}.m img{border-radius:12px}.m span{color:var(--mut)}.step{padding:14px}.step p{color:var(--mut)}.steps{gap:12px}
.case{background:var(--panel);border:1px solid var(--line);border-radius:12px;overflow:hidden;color:var(--ink)}.ct{padding:12px 14px 14px}.ct b{color:var(--acc2)}.ct em{color:var(--mut)}.ct p{color:var(--mut)}
.logos img{filter:grayscale(1) brightness(0) invert(1);opacity:.45}
.btn{background:var(--acc);color:#0C0D12;border-radius:999px;font-weight:700}.contact{color:var(--mut);font-family:"JetBrains Mono";font-size:13px!important}
.card{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:26px}.card>img{border-radius:14px}.card span{color:var(--mut)}.pair i{background:var(--line)}
.reveal .controls{color:var(--acc)}.reveal .progress{color:var(--acc)}
"""),
"c": ("Swiss", "https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;800;900&family=IBM+Plex+Sans:wght@400;500;600&display=swap", """
:root{--ink:#0A0F1F;--blue:#2340F5;--tint:#EDF0FF;--mut:#5A6072;--rule:#D9DCE6}
.reveal{font-family:"IBM Plex Sans",sans-serif;color:var(--ink)}.reveal .slides section{background:#fff}
.reveal h1,.reveal h2,.reveal h3{font-family:Archivo,sans-serif;font-weight:800;color:var(--ink);letter-spacing:-.03em}
.reveal h2{font-size:48px;line-height:1.02}.reveal h2 .co{color:var(--blue)}.reveal p{color:#262B3A}
.reveal .slides section:not(.cover)::before{content:"";position:absolute;left:0;top:0;bottom:0;width:22px;background:var(--blue)}
.kick{color:var(--blue);font-weight:600}.foot{color:var(--mut)}.foot .pg{font-family:Archivo;font-weight:900;font-size:20px;color:var(--blue)}
.cover .band{position:absolute;left:0;top:0;bottom:0;width:600px;background:var(--blue);padding:56px 70px;box-sizing:border-box;color:#fff}
.cover .band .cplogo{height:30px}.cover .cv{position:absolute;left:70px;right:60px;top:200px}
.cover .kick{color:#B9C3FF}.cover h1{font-size:70px;line-height:.98;color:#fff;font-weight:900}.cover .who{color:#DDE2FF;font-size:19px;margin-top:22px!important}.cover .date{position:absolute;left:70px;bottom:40px;color:#B9C3FF;font-size:13px;letter-spacing:.14em;text-transform:uppercase}
.cover .right{position:absolute;left:600px;right:0;top:0;bottom:0;background:var(--tint)}.cover .ll{position:absolute;left:60px;top:56px}.cover .shot{position:absolute;left:76px;top:150px;width:calc(100% - 136px);height:460px;object-fit:cover;object-position:left top;box-shadow:-16px 16px 0 var(--blue)}
.saw .key .hl{display:block;background:var(--blue);color:#fff;padding:20px 24px;font-size:19px;line-height:1.45;font-weight:500}
.saw .pic img{box-shadow:12px 12px 0 var(--tint)}
.pt{border-top:4px solid var(--ink);padding-top:10px}.no{font-family:Archivo;font-weight:900;color:var(--blue);font-size:13px!important}.pt h3{font-weight:800}
.phone img{border:3px solid var(--ink);border-radius:14px}.st{background:var(--tint);padding:8px 12px}.st b{font-family:Archivo;font-weight:900;color:var(--blue)}.st small{color:var(--mut)}
.tt{background:var(--tint);padding:20px 22px}.tt h3{font-weight:800}.metric span{color:var(--blue);font-weight:600}.math{background:var(--ink);padding:18px 24px;margin-top:22px}.math p{color:#fff;margin:0 0 4px}.math .note{color:#AEB4C8;margin:0}
.wf{border-top:4px solid var(--blue);padding-top:10px}.wf b{font-family:Archivo;font-weight:900;color:var(--blue)}.m span{color:var(--mut)}
.step{border-top:4px solid var(--ink);padding-top:12px}.step .no{font-size:28px!important}.step p{color:var(--mut)}
.case{color:var(--ink)}.ct b{font-family:Archivo;font-weight:900;color:var(--blue)}.ct em{color:var(--mut)}.ct p{color:var(--mut)}.logos img{opacity:.6}
.btn{background:var(--blue);color:#fff;font-family:Archivo;font-weight:800}.contact{color:var(--mut)}
.card{background:var(--tint);padding:26px;justify-self:stretch}.card span{color:var(--mut)}.pair i{background:var(--ink)}
.reveal .controls{color:var(--blue)}.reveal .progress{color:var(--blue)}
"""),
}

for key, (name, font, css) in THEMES.items():
    cp_logo = f'<img class="cplogo" src="{A}{"logo_white.svg" if key == "b" else "logo.svg"}" alt="ConvertPolo">'
    page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex, nofollow">
<title>ConvertPolo for {C}</title><link rel="stylesheet" href="{font}">
<link rel="stylesheet" href="../vendor/reset.css"><link rel="stylesheet" href="../vendor/reveal.css"><style>{BASE}{css}</style></head>
<body><div class="reveal"><div class="slides"><section>{"".join(slides(key))}</section></div></div>
<script src="../vendor/reveal.js"></script><script>Reveal.initialize({{width:1280,height:720,margin:0,hash:true,controls:true,progress:true,transition:'slide',center:false}});</script></body></html>'''
    out = REPO / f'{S["slug"]}-{key}'; out.mkdir(exist_ok=True)
    (out / "index.html").write_text(page, encoding="utf-8")
    print("built", name, out / "index.html")
