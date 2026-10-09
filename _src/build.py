# -*- coding: utf-8 -*-
"""ConvertPolo personalized lead deck, white background, reveal.js, vertical navigation. Usage: py build.py specs/<slug>.json"""
import json, sys, html as H
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
SRC = Path(__file__).resolve().parent; REPO = SRC.parent
spec = json.load(open(sys.argv[1], encoding="utf-8"))
slug = spec["slug"]; company = spec["company"]
esc = H.escape

TEAM = [("anirban","Anirban Chakraborty","Founder & CEO"),("saurabh","Saurabh Patwa","Co-Founder"),("ansuya","Ansuya Poudel","Brand & Growth Content Lead"),
        ("jatin","Jatin Kumar Singh","CRO Analyst"),("ankita","Ankita Daga","UX UI Design Lead"),("mahendra","Mahendra Kanojiya","Team Lead"),
        ("kishan","Kishan Rai","Frontend Developer"),("visha","Vishwajay Sharma","QA Engineer")]
CASES = [("hp_anothersole.png","AnotherSole","+185%","revenue","anothersole-product-discovery-improvement"),
         ("hp_theater.png","Theater","+38.95%","revenue per visitor","theater-mobile-experience-redesign"),
         ("roshambo.png","Roshambo","+36.13%","revenue per visitor","roshambo"),
         ("tryevolv.png","TryEvolv","+200%","ecommerce conversion","tryevolv"),
         ("deodap.png","DeoDap","+69.26%","conversion rate","deodap-product-discovery"),
         ("timespro.png","TimesPro","+180%","applications","timespro")]
CLIENTS = ["l1","l2","l11","l12","l14","l15","l16","l17","l18","l19","l113"]

def foot(): return '<div class="foot"><img src="../assets/logo.svg" alt="ConvertPolo"><span>convertpolo.com</span></div>'
def slide(inner, cls=""): return f'<section class="{cls}"><div class="in">{inner}</div>{foot()}</section>'

site = spec["website"].replace("https://","").replace("http://","").strip("/")
lead_logo = f'<img src="../assets/{slug}_{spec["lead_logo"]}" alt="{esc(company)}" class="leadlogo">' if spec.get("lead_logo") else f'<span class="leadname">{esc(company)}</span>'
shot_img = f'<img src="../assets/{slug}_{spec["shot"]}" alt="">' if spec.get("shot") else ""

s = spec["saw"]
stats = "".join(f'<div><b>{v}</b><span>{l}</span></div>' for v, l in s.get("stats", []))
paras = "".join(f"<p>{p}</p>" for p in s["paragraphs"])
ideas = "".join(f'<div class="idea"><h3>{it["head"]}</h3>{"".join(f"<p>{l}</p>" for l in it["lines"])}</div>' for it in spec["ideas"])
team = "".join(f'<div class="m"><img src="../assets/team/{f}.png" alt="{n}"><b>{n}</b><span>{r}</span></div>' for f, n, r in TEAM)
cases = "".join(f'<a class="case" href="https://convertpolo.com/casestudies/{u}/" target="_blank"><div class="ci"><img src="../assets/cs/{f}" alt=""></div><div class="ct"><b>{v}</b> {m}<span>{n}</span></div></a>' for f, n, v, m, u in CASES)
logos = "".join(f'<img src="../assets/clients/{c}.png" alt="">' for c in CLIENTS)

slides = [
 f'''<section class="cover"><div class="in">
  <div class="brand"><img src="../assets/logo.svg" alt="ConvertPolo"><i></i>{lead_logo}</div>
  <div class="cv"><p class="pre">Prepared for {esc(spec["lead_name"])}</p><h1>{esc(company)}</h1><p class="sub">{esc(spec.get("cover_line",""))}</p></div>
  <div class="hero">{shot_img}</div>
  </div>{foot()}</section>''',
 slide(f'<h2>What we saw on {esc(spec["domain"])}</h2><div class="two"><div class="saw">{paras}<div class="stats">{stats}</div><span class="src">{s.get("source","")}</span></div><figure class="frame">{shot_img}<figcaption>{esc(s.get("shot_caption",""))}</figcaption></figure></div>'),
 slide(f'<h2>Where we would start</h2><div class="ideas">{ideas}</div>'),
 slide(f'<h2>Who we are</h2><div class="who"><div class="wl"><p>ConvertPolo is a conversion rate optimization agency for ecommerce and D2C brands, and a strategic partner of VWO.</p><p>Research, design, development, QA and analysis sit in one team. We work as an extension of yours and run every change as an A/B test against a control.</p><img src="../assets/vwo.png" alt="VWO" class="vwo"></div><div class="team">{team}</div></div>'),
 slide(f'<h2>Our work</h2><div class="cases">{cases}</div><div class="logos"><div class="track">{logos}{logos}</div></div>'),
 f'''<section class="talk"><div class="in"><h2>Let's talk</h2>
  <div class="tk"><div><p class="big">Thirty minutes with Anirban Chakraborty, our founder, on what this would look like on {esc(spec["domain"])}.</p><a class="btn" href="{spec.get("booking_url","https://calendly.com/anirban-convertpolo")}" target="_blank">Book a call</a><div class="pair">{lead_logo}<i></i><img src="../assets/logo.svg" alt="ConvertPolo"></div><p class="contact">convertpolo.com · info@convertpolo.com</p></div>
  <div class="mosaic"><img src="../assets/cs/hp_kisah.png" alt=""><img src="../assets/cs/hp_gehna.png" alt=""><img src="../assets/cs/hp_nooe.png" alt=""><img src="../assets/cs/hp_sparify.png" alt=""></div></div></div>{foot()}</section>''',
]

CSS = """
:root{--o:#E45D25;--ink:#222;--soft:#6F6A67;--hair:#ECE8E5}
.reveal{font-family:Lato,Helvetica,Arial,sans-serif;color:var(--ink)}
.reveal .slides section{text-align:left;padding:0;width:1280px;height:720px;box-sizing:border-box;background:#fff}
.reveal .slides section .in{position:absolute;left:80px;right:80px;top:64px;bottom:70px}
.reveal h1,.reveal h2,.reveal h3{font-family:"Bricolage Grotesque",Lato,sans-serif;font-weight:700;letter-spacing:-.02em;color:var(--ink);text-transform:none;margin:0}
.reveal h1{font-size:72px;line-height:1}.reveal h2{font-size:40px;line-height:1.1;margin-bottom:34px}.reveal h3{font-size:24px;line-height:1.25;margin-bottom:10px}
.reveal p{font-size:19px;line-height:1.5;margin:0 0 14px;color:#333}
.foot{position:absolute;left:80px;right:80px;bottom:26px;display:flex;justify-content:space-between;align-items:center;font-size:12px;color:var(--soft)}
.foot img{height:18px}
.cover .brand{display:flex;align-items:center;gap:22px}.cover .brand img{height:32px}.cover .brand i{width:1px;height:36px;background:var(--hair)}
.leadname{font-family:"Bricolage Grotesque",sans-serif;font-weight:700;font-size:24px}.leadlogo{height:34px;max-width:190px;object-fit:contain}
.cover .cv{position:absolute;left:0;top:150px;width:520px}.cover .pre{font-size:18px;color:var(--soft);margin-bottom:14px}.cover .sub{font-size:20px;color:#333;margin-top:22px;max-width:460px}
.cover .hero{position:absolute;right:0;top:110px;width:560px;height:400px;border-radius:10px;overflow:hidden;box-shadow:0 30px 60px -30px rgba(0,0,0,.35);border:1px solid var(--hair)}
.cover .hero img{width:100%;height:100%;object-fit:cover;object-position:top;display:block}
.two{display:grid;grid-template-columns:1fr 1.1fr;gap:60px;align-items:start}
.stats{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--ink);margin-top:14px;padding-top:12px}
.stats b{display:block;font-family:"Bricolage Grotesque",sans-serif;font-size:30px;font-weight:700;letter-spacing:-.02em}.stats div:nth-child(2n) b{color:var(--o)}
.stats span{font-size:12px;color:var(--soft)}.src{display:block;font-size:12px;color:var(--soft);margin-top:16px}
.frame{margin:0}.frame img{display:block;width:100%;height:380px;object-fit:cover;object-position:top;border-radius:10px;border:1px solid var(--hair);box-shadow:0 30px 60px -30px rgba(0,0,0,.35)}
.frame figcaption{font-size:12px;color:var(--soft);margin-top:10px}
.ideas{display:grid;grid-template-columns:1fr 1fr;gap:60px}.idea p{font-size:18px}.idea h3{padding-top:14px;border-top:3px solid var(--o)}
.who{display:grid;grid-template-columns:1fr 1.3fr;gap:60px}.who .wl p{font-size:18px}.vwo{height:30px;margin-top:8px}
.team{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}.team img{width:100%;aspect-ratio:1/1.05;object-fit:cover;object-position:top;display:block;border-radius:8px;background:#F4F1EF}
.team b{display:block;font-size:13px;margin-top:8px;line-height:1.2}.team span{font-size:11px;color:var(--soft)}
.cases{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}.case{display:block;text-decoration:none;color:var(--ink)}
.ci{border-radius:8px;overflow:hidden;border:1px solid var(--hair);height:140px;background:#F4F1EF}.ci img{display:block;width:100%;height:100%;object-fit:cover;object-position:top}
.ct{padding:10px 2px 0;font-size:14px;color:var(--soft)}.ct b{font-family:"Bricolage Grotesque",sans-serif;font-size:26px;font-weight:700;color:var(--o);letter-spacing:-.02em;margin-right:4px}.ct span{display:block;color:var(--ink);font-weight:700;font-size:15px;margin-top:2px}
.logos{margin-top:22px;overflow:hidden;-webkit-mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)}
.logos .track{display:flex;gap:60px;width:max-content;animation:cl 45s linear infinite;align-items:center}.logos img{height:30px;width:auto;filter:grayscale(1);opacity:.7}
@keyframes cl{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.talk .tk{display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center}.big{font-size:22px;max-width:460px}
.btn{display:inline-block;background:var(--o);color:#fff;text-decoration:none;font-family:"Bricolage Grotesque",sans-serif;font-weight:700;font-size:19px;padding:16px 34px;border-radius:40px;margin-top:10px}
.pair{display:flex;align-items:center;gap:22px;margin-top:40px}.pair img{height:30px}.pair i{width:1px;height:34px;background:var(--hair)}
.contact{font-size:14px;color:var(--soft);margin-top:16px}
.mosaic{display:grid;grid-template-columns:1fr 1fr;gap:14px}.mosaic img{width:100%;height:190px;object-fit:cover;object-position:top;border-radius:8px;border:1px solid var(--hair)}
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
