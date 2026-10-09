# -*- coding: utf-8 -*-
"""ConvertPolo personalized lead deck, white, reveal.js, vertical navigation. Usage: py build.py specs/<slug>.json"""
import json, sys, html as H
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
SRC = Path(__file__).resolve().parent; REPO = SRC.parent
spec = json.load(open(sys.argv[1], encoding="utf-8"))
slug = spec["slug"]; company = spec["company"]; esc = H.escape

STEPS = [("Research","Analytics, session recordings, voice of customer"),("Hypotheses","Ranked by expected impact and speed"),("Design and build","Our designers and developers, not your roadmap"),
         ("QA and launch","Every test verified before a visitor sees it"),("Analyze","Statistical significance, not gut feeling"),("Iterate","Winners roll out, learnings feed the next test")]
TEAM = [("anirban","Anirban Chakraborty","Founder & CEO"),("saurabh","Saurabh Patwa","Co-Founder"),("ansuya","Ansuya Poudel","Brand & Growth"),("ankita","Ankita Daga","UX UI Design Lead")]
CLIENTS = ["l1","l2","l11","l12","l14","l15","l16","l17","l18","l19","l113"]

def foot(): return '<div class="foot"><img src="../assets/logo.svg" alt="ConvertPolo"><span>convertpolo.com</span></div>'
def slide(inner, cls=""): return f'<section class="{cls}"><div class="in">{inner}</div>{foot()}</section>'

lead_logo = f'<img src="../assets/{slug}_{spec["lead_logo"]}" alt="{esc(company)}" class="leadlogo">' if spec.get("lead_logo") else f'<span class="leadname">{esc(company)}</span>'
shot = f'<img src="../assets/{slug}_{spec["shot"]}" alt="">' if spec.get("shot") else ""

o = spec["outside"]
stats = "".join(f'<div><b>{v}</b><span>{l}</span><small>{n}</small></div>' for v, l, n in o["stats"])
mx = max(v for _, v in o["sources"])
bars = "".join(f'<div class="bar"><span>{l}</span><i style="width:{v/mx*100:.0f}%"></i><em>{v}%</em></div>' for l, v in o["sources"])
fronts = "".join(f'<div class="front"><span>0{i+1}</span><h3>{f["head"]}</h3><p>{f["text"]}</p></div>' for i, f in enumerate(spec["fronts"]))
proof = spec["proof"]
cases = "".join(f'<a class="case" href="{c["url"]}" target="_blank"><div class="ci"><img src="../assets/cs/{c["img"]}" alt=""></div><div class="ct"><b>{c["lift"]}</b><em>{c["metric"]}</em><span>{c["name"]}</span><p>{c["text"]}</p></div></a>' for c in proof["cases"])
steps = "".join(f'<div class="step"><span>0{i+1}</span><b>{h}</b><p>{t}</p></div>' for i, (h, t) in enumerate(STEPS))
team = "".join(f'<div class="m"><img src="../assets/team/{f}.png" alt="{n}"><div><b>{n}</b><span>{r}</span></div></div>' for f, n, r in TEAM)
logos = "".join(f'<img src="../assets/clients/{c}.png" alt="">' for c in CLIENTS)

slides = [
 f'''<section class="cover"><div class="in">
  <div class="brand"><img src="../assets/logo.svg" alt="ConvertPolo"><i></i>{lead_logo}</div>
  <div class="cv"><p class="pre">Prepared for {esc(spec["lead_name"])}, {esc(spec["lead_meta"])}</p><h1>{esc(spec["cover_title"])}</h1><p class="sub">{esc(spec["cover_sub"])}</p></div>
  <div class="hero">{shot}</div></div>{foot()}</section>''',
 slide(f'<h2>{esc(spec["domain"])}, from the outside</h2><div class="two"><div><div class="stats">{stats}</div><p class="lead">{o["text"]}</p></div><div class="bars"><p class="lab">Where the visitors come from</p>{bars}<p class="src">{esc(o["source"])}</p></div></div>'),
 slide(f'<h2>Where we would start</h2><div class="fronts">{fronts}</div>'),
 slide(f'<h2>{esc(proof["title"])}</h2><p class="lead">{proof["intro"]}</p><div class="cases">{cases}</div>'),
 slide(f'<h2>How we work</h2><p class="lead">Fully managed. You approve, we run everything else.</p><div class="steps">{steps}</div><div class="teamrow">{team}</div>'),
 f'''<section class="talk"><div class="in"><h2>Let's talk</h2>
  <div class="tk"><div><p class="big">{esc(spec["talk_text"])}</p><a class="btn" href="{spec["booking_url"]}" target="_blank">Book a call</a><p class="contact">{esc(spec["booking_url"].replace("https://",""))}<br>info@convertpolo.com · convertpolo.com</p><div class="pair">{lead_logo}<i></i><img src="../assets/logo.svg" alt="ConvertPolo"></div></div>
  <div class="mosaic"><img src="../assets/cs/mobile_grid.png" alt=""><div class="logos"><div class="track">{logos}{logos}</div></div></div></div></div>{foot()}</section>''',
]

CSS = """
:root{--o:#E45D25;--ink:#1F1D1C;--soft:#6F6A67;--hair:#ECE8E5;--tint:#FBF2ED}
.reveal{font-family:Lato,Helvetica,Arial,sans-serif;color:var(--ink)}
.reveal .slides section{text-align:left;padding:0;width:1280px;height:720px;box-sizing:border-box;background:#fff}
.reveal .slides section .in{position:absolute;left:80px;right:80px;top:60px;bottom:70px}
.reveal h1,.reveal h2,.reveal h3{font-family:"Bricolage Grotesque",Lato,sans-serif;font-weight:700;letter-spacing:-.02em;color:var(--ink);text-transform:none;margin:0}
.reveal h1{font-size:54px;line-height:1.05}.reveal h2{font-size:38px;line-height:1.1;margin-bottom:22px}.reveal h3{font-size:22px;line-height:1.25;margin-bottom:8px}
.reveal p{font-size:17px;line-height:1.5;margin:0 0 12px;color:#333}.lead{font-size:18px;max-width:560px;margin-bottom:26px}
.foot{position:absolute;left:80px;right:80px;bottom:26px;display:flex;justify-content:space-between;align-items:center;font-size:12px;color:var(--soft)}.foot img{height:18px}
.cover .brand{display:flex;align-items:center;gap:22px}.cover .brand img{height:32px}.cover .brand i{width:1px;height:36px;background:var(--hair)}
.leadname{font-family:"Bricolage Grotesque",sans-serif;font-weight:700;font-size:24px}.leadlogo{height:34px;max-width:190px;object-fit:contain}
.cover .cv{position:absolute;left:0;top:140px;width:540px}.cover .pre{font-size:16px;color:var(--soft);margin-bottom:16px}.cover .sub{font-size:19px;margin-top:22px;max-width:500px;color:#444}
.cover .hero{position:absolute;right:0;top:110px;width:540px;height:400px;border-radius:10px;overflow:hidden;box-shadow:0 30px 60px -30px rgba(0,0,0,.35);border:1px solid var(--hair)}
.cover .hero img{width:100%;height:100%;object-fit:cover;object-position:top;display:block}
.two{display:grid;grid-template-columns:1.1fr 1fr;gap:70px;align-items:start}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:26px}
.stats b{display:block;font-family:"Bricolage Grotesque",sans-serif;font-size:38px;font-weight:700;letter-spacing:-.02em;color:var(--o)}.stats span{display:block;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink);margin-top:2px}.stats small{display:block;font-size:12px;color:var(--soft);margin-top:4px;line-height:1.3}
.lab{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink);margin-bottom:14px}
.bar{display:grid;grid-template-columns:170px 1fr 56px;align-items:center;gap:12px;margin-bottom:12px;font-size:14px}.bar i{display:block;height:14px;background:var(--o);border-radius:2px}.bar:nth-child(n+4) i{background:#E8B59E}.bar em{font-style:normal;text-align:right;font-weight:700}
.src{font-size:12px;color:var(--soft);margin-top:14px}
.fronts{display:grid;grid-template-columns:repeat(3,1fr);gap:40px;margin-top:10px}.front span{display:block;font-family:"Bricolage Grotesque",sans-serif;font-size:14px;font-weight:700;color:var(--o);padding-bottom:10px;border-bottom:2px solid var(--o);margin-bottom:16px}.front p{font-size:15.5px}
.cases{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}.case{display:block;text-decoration:none;color:var(--ink)}
.ci{border-radius:8px;overflow:hidden;border:1px solid var(--hair);height:200px;background:#F4F1EF}.ci img{display:block;width:100%;height:100%;object-fit:cover;object-position:top}
.ct{padding:14px 2px 0}.ct b{font-family:"Bricolage Grotesque",sans-serif;font-size:30px;font-weight:700;color:var(--o);letter-spacing:-.02em;margin-right:8px}.ct em{font-style:normal;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--soft)}
.ct span{display:block;font-weight:700;font-size:16px;margin-top:4px}.ct p{font-size:14px;color:#444;margin-top:4px}
.steps{display:grid;grid-template-columns:repeat(6,1fr);gap:22px}.step span{display:block;font-family:"Bricolage Grotesque",sans-serif;color:var(--o);font-weight:700;font-size:14px;border-top:2px solid var(--o);padding-top:10px}.step b{display:block;font-size:16px;margin:6px 0 4px}.step p{font-size:13.5px;color:#555}
.teamrow{display:flex;gap:34px;margin-top:44px;padding-top:28px;border-top:1px solid var(--hair)}.m{display:flex;align-items:center;gap:12px}.m img{width:56px;height:56px;border-radius:50%;object-fit:cover;object-position:top;filter:grayscale(1)}.m b{display:block;font-size:14px}.m span{font-size:12px;color:var(--soft)}
.talk .tk{display:grid;grid-template-columns:1fr 1.1fr;gap:60px;align-items:center}.big{font-size:21px;max-width:440px;margin-bottom:18px}
.btn{display:inline-block;background:var(--o);color:#fff;text-decoration:none;font-family:"Bricolage Grotesque",sans-serif;font-weight:700;font-size:18px;padding:15px 32px;border-radius:40px}
.contact{font-size:14px;color:var(--soft);margin-top:18px;line-height:1.6}.pair{display:flex;align-items:center;gap:22px;margin-top:30px}.pair img{height:28px}.pair i{width:1px;height:32px;background:var(--hair)}
.mosaic img:first-child{width:100%;border-radius:10px;border:1px solid var(--hair);display:block}
.logos{margin-top:28px;overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent);mask-image:linear-gradient(90deg,transparent,#000 10%,#000 90%,transparent)}
.logos .track{display:flex;gap:50px;width:max-content;animation:cl 45s linear infinite;align-items:center}.logos img{height:26px;width:auto;filter:grayscale(1);opacity:.65}
@keyframes cl{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.reveal .controls{color:var(--o)}.reveal .progress{color:var(--o)}
"""
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex, nofollow">
<title>ConvertPolo for {esc(company)}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Lato:wght@400;700&display=swap">
<link rel="stylesheet" href="../vendor/reset.css"><link rel="stylesheet" href="../vendor/reveal.css"><style>{CSS}</style></head>
<body><div class="reveal"><div class="slides"><section>{"".join(slides)}</section></div></div>
<script src="../vendor/reveal.js"></script><script>Reveal.initialize({{width:1280,height:720,margin:0,hash:true,controls:true,progress:true,transition:'slide',center:false}});</script></body></html>'''
out = REPO / slug; out.mkdir(exist_ok=True)
(out / "index.html").write_text(page, encoding="utf-8")
print("built", out / "index.html", "slides", len(slides))
