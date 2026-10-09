# -*- coding: utf-8 -*-
"""ConvertPolo personalized lead deck, white background, reveal.js. Usage: py build.py specs/<slug>.json"""
import json, sys, html as H
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
SRC = Path(__file__).resolve().parent; REPO = SRC.parent
spec = json.load(open(sys.argv[1], encoding="utf-8"))
slug = spec["slug"]; first = spec.get("first_name") or spec["lead_name"].split()[0]; company = spec["company"]

TEAM = [("anirban","Anirban Chakraborty","Founder & CEO"),("saurabh","Saurabh Patwa","Co-Founder"),("ansuya","Ansuya Poudel","Brand & Growth Content Lead"),
        ("jatin","Jatin Kumar Singh","CRO Analyst"),("ankita","Ankita Daga","UX UI Design Lead"),("mahendra","Mahendra Kanojiya","Team Lead"),
        ("kishan","Kishan Rai","Frontend Developer"),("visha","Vishwajay Sharma","QA Engineer")]
CASES = [("theater.jpg","Theater","+38.95%","revenue per visitor","Mobile experience redesign","theater-mobile-experience-redesign"),
         ("anothersole.png","AnotherSole","+185%","revenue","Product discovery and shopping journey","anothersole-product-discovery-improvement"),
         ("roshambo.jpg","Roshambo","+36.13%","revenue per visitor","Targeted UX experiments","roshambo"),
         ("tryevolv.jpg","TryEvolv","+200%","ecommerce conversion","Website experience rebuilt","tryevolv"),
         ("deodap.jpg","DeoDap","+69.26%","conversion rate","Better product discovery","deodap-product-discovery"),
         ("timespro.jpg","TimesPro","+180%","Apply Nows","+443% engagement","timespro")]
CLIENTS = ["l1","l2","l11","l12","l14","l15","l16","l17","l18","l19","l113"]

def foot():
    return '<div class="foot"><img src="../assets/logo.svg" alt="ConvertPolo"><span>convertpolo.com</span></div>'

def slide(inner, cls=""):
    return f'<section class="{cls}"><div class="in">{inner}</div>{foot()}</section>'

s = spec["saw"]
shot = f'<figure class="shotwrap"><div class="shot"><div class="bar"><i></i><i></i><i></i><span>{H.escape(spec["website"].replace("https://","").replace("http://","").strip("/"))}</span></div><img src="../assets/{slug}_{spec["shot"]}" alt=""></div><figcaption>{s["shot_caption"]}</figcaption></figure>' if spec.get("shot") else ""
stats = "".join(f'<div><b>{v}</b><span>{l}</span></div>' for v, l in s.get("stats", []))
paras = "".join(f"<p>{p}</p>" for p in s["paragraphs"])

ideas = "".join(f'<article><span class="lab">TEST 0{i+1}</span><h3>{it["head"]}</h3><dl><dt>Hypothesis</dt><dd>{it["hypothesis"]}</dd><dt>Change</dt><dd>{it["change"]}</dd><dt>Measured by</dt><dd>{it["metric"]}</dd></dl></article>' for i, it in enumerate(spec["ideas"]))
team = "".join(f'<div class="m"><img src="../assets/team/{f}.png" alt="{n}"><b>{n}</b><span>{r}</span></div>' for f, n, r in TEAM)
cases = "".join(f'<a class="case" href="https://convertpolo.com/casestudies/{u}/" target="_blank"><img src="../assets/cs/{f}" alt=""><div class="ct"><b>{v}</b><span>{m}</span><h3>{n}</h3><p>{d}</p></div></a>' for f, n, v, m, d, u in CASES)
logos = "".join(f'<img src="../assets/clients/{c}.png" alt="">' for c in CLIENTS)
lead_logo = f'<img src="../assets/{slug}_{spec["lead_logo"]}" alt="{H.escape(company)}" class="leadlogo">' if spec.get("lead_logo") else f'<span class="leadname">{H.escape(company)}</span>'

slides = [
 # 1 cover
 f'''<section class="cover"><div class="in">
  <div class="brand"><img src="../assets/logo.svg" alt="ConvertPolo"><i></i>{lead_logo}</div>
  <div class="cv"><span class="eyebrow">Conversion rate optimization</span>
  <h1>Prepared for {H.escape(spec["lead_name"])}<br><em>{H.escape(company)}</em></h1>
  <p class="sub">{spec.get("cover_line","What we saw on your store, two tests we would run first, and the brands where we already ran this play.")}</p></div>
  <svg class="chart" viewBox="0 0 520 300" aria-hidden="true"><path d="M20 240 C 120 236, 220 240, 500 232" fill="none" stroke="#C9C2BE" stroke-width="3" stroke-dasharray="8 8"/><path d="M20 240 C 110 228, 200 200, 300 160 S 440 70, 500 40" fill="none" stroke="#E45D25" stroke-width="6" stroke-linecap="round"/><path d="M20 240 C 110 228, 200 200, 300 160 S 440 70, 500 40 L500 232 C 220 240, 120 236, 20 240Z" fill="#E45D25" fill-opacity=".08"/><circle cx="500" cy="40" r="8" fill="#E45D25"/><text x="492" y="26" text-anchor="end" font-family="Lato,sans-serif" font-weight="700" font-size="15" fill="#E45D25">Variant</text><text x="492" y="258" text-anchor="end" font-family="Lato,sans-serif" font-size="13" fill="#8A827E">Control</text></svg>
  </div>{foot()}</section>''',
 # 2 what we saw
 slide(f'<h2>What we saw on <em>{H.escape(spec["domain"])}</em></h2><div class="two"><div class="saw">{paras}<div class="stats">{stats}</div><span class="src">{s.get("source","")}</span></div>{shot}</div>'),
 # 3 tests
 slide(f'<h2>Two tests we would run first on <em>{H.escape(company)}</em></h2><div class="tests">{ideas}</div><p class="rule">Every change runs against a live control. Winners stay, losers get written down.</p>'),
 # 4 who we are
 slide(f'<h2>Who we <em>are</em></h2><div class="who"><div class="wl"><p>ConvertPolo is a conversion rate optimization agency for ecommerce and D2C brands.</p><p>Research, hypothesis, design, development, QA and analysis, in one team that works as an extension of yours.</p><p>Everything is rooted in data, experimentation and real user psychology.</p><div class="badges"><img src="../assets/vwo.png" alt="VWO partner"><span>Strategic partner</span></div></div><div class="team">{team}</div></div>'),
 # 5 work
 slide(f'<h2>We have run this play <em>before</em></h2><div class="cases">{cases}</div><div class="logos"><div class="track">{logos}{logos}</div></div>'),
 # 6 talk
 f'''<section class="talk"><div class="in"><h2>Let's talk about <em>{H.escape(company)} x ConvertPolo</em></h2>
  <div class="tk"><div><a class="btn" href="{spec.get("booking_url","https://calendly.com/anirban-convertpolo")}" target="_blank">Book a call</a><p class="note">Anirban Chakraborty, our founder, runs these calls.</p><div class="pair">{lead_logo}<i></i><img src="../assets/logo.svg" alt="ConvertPolo"></div><p class="contact">convertpolo.com · info@convertpolo.com</p></div>
  <div class="teamgrid">{"".join(f'<img src="../assets/team/{f}.png" alt="">' for f,_,_ in TEAM)}</div></div></div>{foot()}</section>''',
]

CSS = """
:root{--o:#E45D25;--ink:#2F2E2E;--soft:#6B6461;--hair:#E8E2DE;--blush:#FBEFE9}
.reveal{font-family:Lato,Helvetica,Arial,sans-serif;color:var(--ink)}
.reveal .slides section{text-align:left;padding:0;width:1280px;height:720px;box-sizing:border-box;background:#fff}
.reveal .slides section .in{position:absolute;left:72px;right:72px;top:56px;bottom:64px}
.reveal h1,.reveal h2,.reveal h3{font-family:"Bricolage Grotesque",Lato,sans-serif;font-weight:800;letter-spacing:-.02em;color:var(--ink);text-transform:none;margin:0}
.reveal h1{font-size:60px;line-height:1.02}.reveal h2{font-size:42px;line-height:1.08;margin-bottom:28px}.reveal h3{font-size:22px;line-height:1.2}
.reveal h1 em,.reveal h2 em{font-style:normal;color:var(--o)}
.reveal p{font-size:19px;line-height:1.5;margin:0 0 14px}
.foot{position:absolute;left:72px;right:72px;bottom:24px;display:flex;justify-content:space-between;align-items:center;border-top:1px solid var(--hair);padding-top:10px;font-size:12px;color:var(--soft)}
.foot img{height:20px}
.eyebrow{font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:var(--o);font-weight:700;display:block;margin-bottom:18px}
.cover .brand{display:flex;align-items:center;gap:22px}.cover .brand img{height:34px}.cover .brand i{width:2px;height:40px;background:var(--hair)}
.leadname{font-family:"Bricolage Grotesque",sans-serif;font-weight:800;font-size:26px}.leadlogo{height:36px;max-width:190px;object-fit:contain}
.cover .cv{position:absolute;left:0;top:170px;width:620px}.cover .sub{font-size:20px;color:var(--soft);max-width:560px}
.cover .chart{position:absolute;right:0;top:120px;width:480px}
.two{display:grid;grid-template-columns:1fr 1.1fr;gap:56px;align-items:start}
.stats{display:grid;grid-template-columns:repeat(4,1fr);border-top:2px solid var(--ink);margin-top:10px}
.stats div{padding-top:10px}.stats b{display:block;font-family:"Bricolage Grotesque",sans-serif;font-size:30px;font-weight:800;letter-spacing:-.02em}.stats div:nth-child(2n) b{color:var(--o)}
.stats span{font-size:12px;color:var(--soft)}.src{display:block;font-size:12px;color:var(--soft);margin-top:14px}
.shotwrap{margin:0}.shot{border:1px solid var(--hair);box-shadow:0 20px 50px -24px rgba(47,46,46,.45);background:#fff}
.shot .bar{display:flex;align-items:center;gap:6px;padding:8px 10px;border-bottom:1px solid var(--hair)}.shot .bar i{width:8px;height:8px;border-radius:50%;background:var(--hair)}
.shot .bar span{margin-left:8px;font-size:11px;color:var(--soft);background:#F7F3F1;padding:3px 10px;flex:1}
.shot img{display:block;width:100%;height:340px;object-fit:cover;object-position:top}
.shotwrap figcaption{font-size:12px;color:var(--soft);margin-top:8px}
.tests{display:grid;grid-template-columns:1fr 1fr;gap:32px}
.tests{margin-top:12px}.tests article{border:1px solid var(--hair);background:#fff}
.tests .lab{display:block;background:var(--blush);color:var(--o);font-weight:700;font-size:12px;letter-spacing:.12em;padding:12px 22px}
.tests h3{padding:18px 22px 6px}.tests dl{margin:0;padding:0 22px 18px}.tests dt{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--soft);font-weight:700;margin-top:12px}.tests dd{margin:3px 0 0;font-size:16px;line-height:1.4}
.rule{margin-top:26px;font-family:"Bricolage Grotesque",sans-serif;font-weight:600;font-size:18px}
.who{display:grid;grid-template-columns:1fr 1.25fr;gap:56px}.who .wl p{font-size:18px}
.badges{display:flex;align-items:center;gap:14px;margin-top:10px}.badges img{height:34px}.badges span{font-size:13px;color:var(--soft);border:1px solid var(--ink);padding:6px 12px;font-weight:700}
.team{display:grid;grid-template-columns:repeat(4,1fr);gap:18px 16px}.team .m{text-align:center}.team img{width:100%;aspect-ratio:1/1.1;object-fit:cover;object-position:top;display:block;border-radius:6px;background:var(--blush)}
.team b{display:block;font-size:13px;margin-top:8px;line-height:1.2}.team span{font-size:11px;color:var(--soft)}
.cases{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}.case{display:block;text-decoration:none;color:var(--ink);border:1px solid var(--hair)}
.case img{display:block;width:100%;height:104px;object-fit:cover;object-position:top}.ct{padding:10px 16px 12px}
.ct b{font-family:"Bricolage Grotesque",sans-serif;font-size:30px;font-weight:800;color:var(--o);letter-spacing:-.03em;margin-right:8px}.ct span{font-size:12px;color:var(--soft);text-transform:uppercase;letter-spacing:.08em}
.ct h3{font-size:17px;margin-top:4px}.ct p{font-size:13px;color:var(--soft);margin:2px 0 0}
.logos{margin-top:22px;overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)}
.logos .track{display:flex;gap:56px;width:max-content;animation:cl 40s linear infinite;align-items:center}.logos img{height:34px;width:auto;filter:grayscale(1);opacity:.75}
@keyframes cl{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.talk .tk{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center;margin-top:20px}
.btn{display:inline-block;background:var(--o);color:#fff;text-decoration:none;font-family:"Bricolage Grotesque",sans-serif;font-weight:700;font-size:20px;padding:18px 36px;border-radius:40px;box-shadow:0 12px 30px rgba(228,93,37,.35)}
.note{font-size:15px;color:var(--soft);margin-top:18px}.pair{display:flex;align-items:center;gap:22px;margin-top:26px}.pair img{height:32px}.pair i{width:2px;height:36px;background:var(--hair)}
.contact{font-size:14px;color:var(--soft);margin-top:18px}
.teamgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.teamgrid img{width:100%;aspect-ratio:1;object-fit:cover;object-position:top;border-radius:8px;background:var(--blush)}
.reveal .controls{color:var(--o)}.reveal .progress{color:var(--o)}
"""
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex, nofollow">
<title>ConvertPolo for {H.escape(company)}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Lato:wght@400;700&display=swap">
<link rel="stylesheet" href="../vendor/reset.css"><link rel="stylesheet" href="../vendor/reveal.css"><style>{CSS}</style></head>
<body><div class="reveal"><div class="slides">{"".join(slides)}</div></div>
<script src="../vendor/reveal.js"></script><script>Reveal.initialize({{width:1280,height:720,margin:0,hash:true,controls:true,progress:true,transition:'slide',center:false}});</script></body></html>'''
out = REPO / slug; out.mkdir(exist_ok=True)
(out / "index.html").write_text(page, encoding="utf-8")
print("built", out / "index.html", "slides", len(slides))
