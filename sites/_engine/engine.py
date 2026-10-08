"""Shared site generator for Legend Creative demo sites.

Each client folder has a site.py with a CONFIG dict; run `python3 site.py` there.
Output is a self-contained static site (HTML + assets) in that folder.
"""
import random
import re
import shutil
import urllib.request
from pathlib import Path

ENGINE = Path(__file__).parent

ICON_PATHS = {
    "phone": '<path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" d="M5 3.5h3.2l1.6 4.2-2.1 1.4a11.5 11.5 0 0 0 7.2 7.2l1.4-2.1 4.2 1.6V19a1.9 1.9 0 0 1-2 1.9C10.6 20.4 3.6 13.4 3.1 5.5A1.9 1.9 0 0 1 5 3.5Z"/>',
    "arrow": '<path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M4 12h15m-6-6 6 6-6 6"/>',
    "star": '<path fill="currentColor" d="m12 2.8 2.8 5.9 6.4.8-4.7 4.4 1.2 6.4L12 17.2l-5.7 3.1 1.2-6.4-4.7-4.4 6.4-.8z"/>',
    "photo": '<path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" d="M3.5 7.5h3.6l1.6-2.5h6.6l1.6 2.5h3.6v11.5h-17z"/><circle cx="12" cy="12.8" r="3.6" fill="none" stroke="currentColor" stroke-width="1.6"/>',
    "menu": '<path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M4 7h16M4 12h16M4 17h16"/>',
    "check": '<circle cx="12" cy="12" r="9.2" fill="none" stroke="currentColor" stroke-width="1.6"/><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="m7.8 12.3 2.8 2.8 5.6-5.8"/>',
    "shield": '<path fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round" d="M12 2.8 4.5 5.6v5.6c0 4.6 3.1 8.6 7.5 10 4.4-1.4 7.5-5.4 7.5-10V5.6z"/><path fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" d="m8.8 12 2.3 2.3 4.3-4.6"/>',
    "medal": '<circle cx="12" cy="14.5" r="5.5" fill="none" stroke="currentColor" stroke-width="1.7"/><path fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round" d="M8.6 10.2 6 3h4l2 4.5L14 3h4l-2.6 7.2"/><path fill="currentColor" d="m12 11.8.9 1.9 2 .2-1.5 1.4.4 2-1.8-1-1.8 1 .4-2-1.5-1.4 2-.2z"/>',
    "flag": '<path fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" d="M5 21V4m0 0h11l-2 4 2 4H5"/>',
    "leaf": '<path fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" d="M5 19c0-8 5-13 15-14-1 10-6 15-14 15M5 19l7-7"/>',
    "clock": '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.7"/><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" d="M12 7v5l3.2 2"/>',
    "dollar": '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.7"/><path fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" d="M14.8 9.2c-.5-1-1.6-1.6-2.8-1.6-1.6 0-2.8.9-2.8 2.1 0 2.9 5.8 1.6 5.8 4.6 0 1.3-1.3 2.2-3 2.2-1.3 0-2.5-.6-3-1.7M12 6v1.6m0 8.9V18"/>',
    "home": '<path fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round" d="M3.5 11 12 4l8.5 7M6 9.5V20h12V9.5"/><path fill="none" stroke="currentColor" stroke-width="1.7" d="M10 20v-5.5h4V20"/>',
    "users": '<circle cx="9" cy="8.5" r="3.3" fill="none" stroke="currentColor" stroke-width="1.7"/><path fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" d="M3 19.5c.6-3.3 3-5 6-5s5.4 1.7 6 5M15.5 5.6a3.2 3.2 0 0 1 0 6M17.5 14.7c1.9.6 3.1 2.2 3.5 4.8"/>',
    "chat": '<path fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round" d="M4 5.5h16v10.5h-9l-4.5 3.5V16H4z"/>',
}


def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} aria-hidden="true"><use href="#i-{name}"/></svg>'


def sprite():
    syms = "".join(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICON_PATHS.items())
    return f'<svg width="0" height="0" style="position:absolute" aria-hidden="true">{syms}</svg>'


def stars(n=5):
    return '<span class="stars" aria-hidden="true">' + icon("star") * n + "</span>"


# ── Placeholder art ────────────────────────────────────
def _grain(opacity=0.3):
    return (f'<defs><filter id="g"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="4"/>'
            f'<feColorMatrix values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 {opacity} 0"/></filter>'
            '<linearGradient id="v" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".1"/><stop offset="1" stop-color="#000" stop-opacity=".18"/></linearGradient></defs>')


def ph_ashlar(seed, tones, mortar, w=1200, h=900):
    r = random.Random(seed)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice"><rect width="{w}" height="{h}" fill="{mortar}"/>', _grain()]
    y = 0
    while y < h:
        rh = r.choice([70, 90, 110, 130]); x = -r.randint(0, 120)
        while x < w:
            bw = r.randint(140, 320)
            o.append(f'<rect x="{x+3}" y="{y+3}" width="{bw-7}" height="{rh-7}" rx="3" fill="{r.choice(tones)}"/><rect x="{x+3}" y="{y+3}" width="{bw-7}" height="{rh-7}" rx="3" fill="url(#v)"/>')
            x += bw
        y += rh
    o.append(f'<rect width="{w}" height="{h}" filter="url(#g)"/></svg>')
    return "".join(o)


def ph_pavers(seed, tones, joint, w=1200, h=900):
    r = random.Random(seed)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice"><rect width="{w}" height="{h}" fill="{joint}"/>', _grain(0.25)]
    s = 60
    for row in range(-2, h // s + 3):
        for col in range(-2, w // s + 3):
            x = col * s * 2 + (row % 2) * s; y = row * s
            o.append(f'<rect x="{x+2}" y="{y+2}" width="{s*2-4}" height="{s-4}" rx="4" fill="{r.choice(tones)}"/>')
    o.append(f'<rect width="{w}" height="{h}" fill="url(#v)"/><rect width="{w}" height="{h}" filter="url(#g)"/></svg>')
    return "".join(o)


def ph_planks(seed, tones, gap, w=1200, h=900):
    r = random.Random(seed)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice"><rect width="{w}" height="{h}" fill="{gap}"/>', _grain(0.22)]
    y = 0; bh = 64
    while y < h:
        x = -r.randint(0, 400)
        while x < w:
            bw = r.randint(420, 900); c = r.choice(tones)
            o.append(f'<rect x="{x+3}" y="{y+3}" width="{bw-6}" height="{bh-6}" rx="2" fill="{c}"/>')
            for _ in range(3):
                gy = y + r.randint(14, bh - 14)
                o.append(f'<path d="M{x+10} {gy} q {bw/3:.0f} {r.randint(-6,6)} {bw-20} 0" stroke="#000" stroke-opacity=".08" stroke-width="2" fill="none"/>')
            x += bw
        y += bh
    o.append(f'<rect width="{w}" height="{h}" fill="url(#v)"/><rect width="{w}" height="{h}" filter="url(#g)"/></svg>')
    return "".join(o)


def ph_garden(seed, greens, sky, w=1200, h=900):
    r = random.Random(seed)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice"><rect width="{w}" height="{h}" fill="{sky}"/>', _grain(0.2)]
    bands = len(greens)
    for i, g in enumerate(greens):
        base = h * (0.35 + 0.55 * i / bands)
        pts = " ".join(f"{x},{base + r.randint(-40, 40):.0f}" for x in range(-100, w + 200, 150))
        o.append(f'<path d="M-100 {h} L {pts.replace(" ", " L ")} L {w+100} {h} Z" fill="{g}"/>')
        for _ in range(5):
            cx = r.randint(0, w); cy = base + r.randint(-10, 50); rad = r.randint(30, 90)
            o.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rad}" ry="{rad*0.75:.0f}" fill="{greens[min(i+1, bands-1)]}" opacity=".9"/>')
    o.append(f'<rect width="{w}" height="{h}" fill="url(#v)"/><rect width="{w}" height="{h}" filter="url(#g)"/></svg>')
    return "".join(o)


PH_DEFAULTS = {
    "stone": lambda: ph_ashlar(7, ["#b9b2a6", "#a89f92", "#c4bdb1", "#9c9387", "#b3a593", "#8f8a80", "#ad8c76"], "#d8d2c7"),
    "pavers": lambda: ph_pavers(5, ["#b8ab98", "#a39684", "#c7bba8", "#8e8476", "#ab9f8e", "#9a8f80"], "#6d665c"),
    "deck": lambda: ph_planks(3, ["#9a6b4b", "#a8775a", "#8d6045", "#b38463", "#946650"], "#3a2a20"),
    "composite": lambda: ph_planks(9, ["#7a7672", "#8a857f", "#6d6965", "#958f88", "#807b75"], "#2c2a28"),
    "garden": lambda: ph_garden(2, ["#7c9c5a", "#5f8445", "#4b6e37", "#3a5a2c"], "#cfd9c7"),
    "porch": lambda: ph_planks(12, ["#d9d6cf", "#cfcbc3", "#e2dfd8", "#c6c1b8"], "#8f8a82"),
}


def photo(src, label, kind="stone", cls="", alt=""):
    c = f"photo {cls}".strip()
    return (f'<figure class="{c}" style="background-image:url(assets/ph-{kind}.svg)"><img src="images/{src}" alt="{alt or label}" loading="lazy" decoding="async">'
            f'<figcaption class="ph-label">{icon("photo")}<span>Photo: {label}</span></figcaption></figure>')


# ── Fonts ──────────────────────────────────────────────
def fetch_fonts(url, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    css_path = out_dir.parent / "css" / "fonts.css"
    if css_path.exists():
        return
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"})
    css = urllib.request.urlopen(req).read().decode()
    blocks = re.findall(r"/\* (\S+) \*/\s*(@font-face \{.*?\})", css, re.S)
    out, seen = [], {}
    for sub, b in blocks:
        if sub != "latin":
            continue
        u = re.search(r"url\((https://[^)]+)\)", b).group(1)
        fam = re.search(r"font-family: '([^']+)'", b).group(1).replace(" ", "")
        if u not in seen:
            name = f"{fam}-{len(seen)}.woff2"; seen[u] = name
            urllib.request.urlretrieve(u, out_dir / name)
        out.append(b.replace(u, "../fonts/" + seen[u]))
    css_path.write_text("\n".join(out) + "\n")


# ── Page parts ─────────────────────────────────────────
NAV = [("index.html", "Home"), ("services.html", "Services"), ("work.html", "Gallery"), ("about.html", "About")]


def header(c, current):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV)
    lg = c["logo"]
    mark = lg.get("mark", "")
    sub = f'<span class="script">{lg["script"]}</span>' if lg.get("script") else (f'<span>{lg["sub"]}</span>' if lg.get("sub") else "")
    top = ""
    if c.get("topbar"):
        badges = "".join(f"<span>{icon(i)}{t}</span>" for i, t in c["topbar"])
        top = f'<div class="topbar"><div class="wrap"><div class="badges">{badges}</div><a class="tel" href="tel:{c["tel"]}">{icon("phone")}<span class="num">{c["phone"]}</span></a></div></div>'
    return f"""<a class="skip" href="#main">Skip to content</a>
{top}
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="{c['name']}, home">{mark}<span class="lt"><b>{lg['name']}</b>{sub}</span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">{icon("menu")}<span>Menu</span></button>
    <nav class="nav" id="nav" aria-label="Main">
      {links}
      <a class="tel" href="tel:{c['tel']}">{icon("phone")}<span class="num">{c['phone']}</span></a>
      <a class="btn" href="contact.html">{c['cta']}</a>
    </nav>
  </div>
</header>"""


def footer(c):
    svc = "".join(f'<li><a href="services.html#{s["id"]}">{s["name"]}</a></li>' for s in c["services"][:5])
    email = f'<br><a href="mailto:{c["email"]}">{c["email"]}</a>' if c.get("email") else ""
    hours = f'<br>{c["hours"]}' if c.get("hours") else ""
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="logo" href="index.html">{c['logo'].get('mark', '')}<span class="lt"><b>{c['logo']['name']}</b>{f'<span>{c["logo"]["sub"]}</span>' if c['logo'].get('sub') else ''}</span></a>
        <p style="margin-top:1.4rem;max-width:34ch;opacity:.85">{c['footer_blurb']}</p>
      </div>
      <div><p class="fh">Services</p><ul>{svc}</ul></div>
      <div><p class="fh">Company</p><ul><li><a href="about.html">About us</a></li><li><a href="work.html">Gallery</a></li><li><a href="contact.html">{c['cta']}</a></li></ul></div>
      <div><p class="fh">Contact</p><address>{c['address']}<br><a class="num" href="tel:{c['tel']}">{c['phone']}</a>{email}{hours}</address></div>
    </div>
    <div class="legal"><span>&copy; <span data-year>2026</span> {c['name']}.</span><span>{c['footer_right']}</span></div>
  </div>
</footer>
<nav class="callbar" aria-label="Quick contact">
  <a href="tel:{c['tel']}">{icon("phone")}Call</a>
  <a href="contact.html">{c['cta']} {icon("arrow")}</a>
</nav>"""


def band(c, title=None, text=None):
    b = c["band"]
    return f"""<section class="band">
  <div class="wrap row-cta">
    <div>
      <h2 data-split>{title or b['title']}</h2>
      <p class="lede">{text or b['text']}</p>
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:1rem 1.6rem;align-items:center">
      <a class="btn {b.get('btn_cls', 'btn--light')}" href="contact.html">{c['cta']} {icon("arrow")}</a>
      <a class="tel" href="tel:{c['tel']}">{icon("phone")}<span class="num">{c['phone']}</span></a>
    </div>
  </div>
</section>"""


def joint():
    return '<div class="joint" aria-hidden="true"></div>'


def page(c, out, name, title, desc, body):
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="{c['theme_color']}">
<link rel="stylesheet" href="assets/css/fonts.css">
<link rel="stylesheet" href="assets/css/base.css">
<link rel="stylesheet" href="assets/css/theme.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body>
{sprite()}
{header(c, name)}
<main id="main">
{body}
</main>
{footer(c)}
<script src="assets/js/vendor/gsap.min.js" defer></script>
<script src="assets/js/vendor/ScrollTrigger.min.js" defer></script>
<script src="assets/js/vendor/SplitText.min.js" defer></script>
<script src="assets/js/site.js" defer></script>
</body>
</html>
"""
    (out / name).write_text(html)


# ── Sections ───────────────────────────────────────────
def hero(c):
    h = c["hero"]
    script = f'<span class="kick-script script">{h["script"]}</span>' if h.get("script") else ""
    proof = "".join(f"<span>{p}</span>" for p in h.get("proof", []))
    proof = f'<div class="proof hero-in">{proof}</div>' if proof else ""
    second = f'<a class="btn {h.get("second_cls", "btn--ghost")}" href="{h["second"][1]}">{h["second"][0]}</a>' if h.get("second") else ""
    actions = f"""<div class="actions hero-in"><a class="btn" href="contact.html">{c['cta']} {icon("arrow")}</a>{second}<a class="tel" href="tel:{c['tel']}">{icon("phone")}<span class="num">{c['phone']}</span></a></div>"""
    ph = photo("hero.jpg", h["photo_label"], h["photo_kind"], "hero-photo")
    body = f"""{script}<h1 data-split="hero">{h['title']}</h1><p class="sub hero-in">{h['sub']}</p>{actions}{proof}"""
    v = h["variant"]
    if v == "overlay":
        return f'<section class="hero hero--overlay">{ph}<div class="wrap"><span class="accent-bar" aria-hidden="true"></span>{body}</div></section>'
    if v == "panel":
        return f'<section class="hero hero--panel"><div class="wrap"><div class="stage">{ph}<div class="panel">{body}</div></div></div></section>'
    return f'<section class="hero hero--split"><div class="wrap grid"><div>{body}</div>{ph}</div></section>'


def trust(c):
    if not c.get("trust"):
        return ""
    items = "".join(f'<div class="t">{icon(i)}<div><b>{b}</b><span>{s}</span></div></div>' for i, b, s in c["trust"])
    return f'<section class="trust" aria-label="Why homeowners choose us" style="--trust-n:{len(c["trust"])}"><div class="wrap">{items}</div></section>'


def services_home(c):
    sv = c["services"]
    if c.get("services_style") == "rows":
        inner = "".join(f"""<a class="row reveal" href="services.html#{s['id']}"><h3>{s['name']}</h3><p>{s['blurb']}</p>{icon("arrow", "arrow")}{photo(s['img'], s['name'].replace('&amp;', '&'), s['kind'], 'peek')}</a>""" for s in sv)
        grid = f'<div class="rows">{inner}</div>'
    else:
        tiles = []
        for i, s in enumerate(sv[:5] if 0 in c.get("big_tiles", (0,)) else sv[:6]):
            big = " big" if i in c.get("big_tiles", (0,)) else ""
            tiles.append(f"""<a class="tile{big} reveal" href="services.html#{s['id']}">{photo(s['img'], s['name'].replace('&amp;', '&'), s['kind'])}<div class="tx"><h3>{s['name']}</h3><p>{s['blurb']}</p><span class="go">{icon("arrow")}</span></div></a>""")
        grid = f'<div class="tiles">{"".join(tiles)}</div>'
    sh = c["services_head"]
    return f"""<section class="section{' ' + sh.get('cls', '') if sh.get('cls') else ''}" aria-labelledby="svc-h">
  <div class="wrap">
    <div class="section-head"><h2 id="svc-h" data-split>{sh['title']}</h2><p class="lede">{sh['text']}</p></div>
    {grid}
  </div>
</section>"""


def feature(c, f, flip=False):
    checks = "".join(f"<li>{icon('check')}<span>{x}</span></li>" for x in f.get("checks", []))
    checks = f'<ul class="checks">{checks}</ul>' if checks else ""
    paras = "".join(f"<p{' class=\"lede\"' if i == 0 else ''}>{p}</p>" for i, p in enumerate(f["body"]))
    link = f'<a class="{f.get("link_cls", "textlink")}" href="{f["link"][1]}">{f["link"][0]} {icon("arrow")}</a>' if f.get("link") else ""
    return f"""<section class="section{' ' + f['cls'] if f.get('cls') else ''}">
  <div class="wrap feature{' flip' if flip else ''}">
    {photo(f['img'], f['photo_label'], f['kind'], 'reveal')}
    <div class="reveal"><h2 data-split>{f['title']}</h2>{paras}{checks}{link}</div>
  </div>
</section>"""


def statement(c):
    s = c.get("statement")
    if not s:
        return ""
    return f'<section class="section {s.get("cls", "dark")}"><div class="wrap"><p class="statement reveal">{s["text"]}</p>{("<p class=\"lede reveal\" style=\"margin-top:1.6rem\">" + s["sub"] + "</p>") if s.get("sub") else ""}</div></section>'


def process(c):
    p = c["process"]
    steps = "".join(f'<li class="reveal"><span class="step" aria-hidden="true">{i+1:02d}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(p["steps"]))
    return f"""<section class="section{' ' + p['cls'] if p.get('cls') else ''}" aria-labelledby="proc-h">
  <div class="wrap">
    <div class="section-head"><h2 id="proc-h" data-split>{p['title']}</h2><p class="lede">{p['text']}</p></div>
    <ol class="process">{steps}</ol>
  </div>
</section>"""


def reviews(c):
    r = c["reviews"]
    quotes = "".join(f'<figure class="reveal">{stars()}<blockquote>[{"Paste a real Google review here. We&rsquo;ll use your best four." if i == 0 else "Google review from a homeowner."}]</blockquote><figcaption>Homeowner, {r["town"]}</figcaption></figure>' for i in range(4))
    score = f'<div class="score num" aria-label="Rated {r["score"]} out of 5">{r["score"]}</div>' if r.get("score") else f'<div class="score num">{r["big"]}</div>'
    return f"""<section class="section{' ' + r.get('cls', '') if r.get('cls') else ''}" aria-labelledby="rev-h">
  <div class="wrap reviews">
    <div class="reveal"><h2 id="rev-h" style="font-size:var(--step-3);margin-bottom:1.6rem" data-split>{r['title']}</h2>{score}<div class="score-meta">{stars()}<span class="small">{r['label']}</span></div></div>
    <div class="quotes">{quotes}</div>
  </div>
</section>"""


def area(c):
    a = c["area"]
    items = "".join(f"<li>{x}</li>" for x in a["towns"])
    return f"""<section class="section" style="padding-top:0" aria-labelledby="area-h">
  <div class="wrap"><h2 id="area-h" style="font-size:var(--step-2);margin-bottom:1.4rem">{a['title']}</h2><ul class="area reveal">{items}</ul></div>
</section>"""


# ── Build ──────────────────────────────────────────────
def build(c, out):
    out = Path(out)
    assets = out / "assets"
    (assets / "css").mkdir(parents=True, exist_ok=True)
    (assets / "js" / "vendor").mkdir(parents=True, exist_ok=True)
    (out / "images").mkdir(exist_ok=True)
    shutil.copy(ENGINE / "assets/css/base.css", assets / "css/base.css")
    shutil.copy(ENGINE / "assets/js/site.js", assets / "js/site.js")
    for f in (ENGINE / "assets/js/vendor").iterdir():
        shutil.copy(f, assets / "js/vendor" / f.name)
    (assets / "css/theme.css").write_text(c["theme_css"])
    fetch_fonts(c["fonts_url"], assets / "fonts")
    kinds = c.get("ph", {})
    for k in {"stone", "pavers", "deck", "composite", "garden", "porch"}:
        (assets / f"ph-{k}.svg").write_text(kinds[k]() if k in kinds else PH_DEFAULTS[k]())

    # Home
    sections = [hero(c), trust(c), services_home(c)]
    for item in c["home_order"]:
        if item == "feature":
            sections.append(feature(c, c["feature"]))
        elif item == "feature2":
            sections.append(feature(c, c["feature2"], flip=True))
        elif item == "statement":
            sections.append(statement(c))
        elif item == "process":
            sections.append(process(c))
        elif item == "reviews":
            sections.append(reviews(c))
        elif item == "area":
            sections.append(area(c))
        elif item == "joint":
            sections.append(joint())
    sections.append(joint())
    sections.append(band(c))
    page(c, out, "index.html", c["meta"]["home"][0], c["meta"]["home"][1], "\n".join(sections))

    # Services
    svc = []
    for s in c["services"]:
        bullets = "".join(f"<li>{icon('check')}<span>{b}</span></li>" for b in s["bullets"])
        svc.append(f"""<section class="svc wrap" id="{s['id']}" aria-labelledby="{s['id']}-h">
  {photo(s['img'], s['name'].replace('&amp;', '&').lower(), s['kind'])}
  <div class="reveal"><h2 id="{s['id']}-h" data-split>{s['name']}</h2><p class="lede">{s['intro']}</p><ul class="checks">{bullets}</ul><a class="btn" href="contact.html">{c['cta']} {icon("arrow")}</a></div>
</section>""")
    jump = "".join(f'<a href="#{s["id"]}">{s["name"]}</a>' for s in c["services"])
    sp = c["pages"]["services"]
    body = f"""<section class="page-head"><div class="wrap"><span class="crumb"><a href="index.html">Home</a> / Services</span><h1 data-split>{sp['title']}</h1><p class="lede">{sp['lede']}</p><nav class="jump" aria-label="Services on this page">{jump}</nav></div></section>
{''.join(svc)}
<div style="height:var(--section)"></div>{joint()}{band(c)}"""
    page(c, out, "services.html", c["meta"]["services"][0], c["meta"]["services"][1], body)

    # Gallery
    cats = {}
    for w in c["work"]:
        cats.setdefault(w[0], None)
    filt = '<button aria-pressed="true" data-filter="all">All projects</button>' + "".join(
        f'<button aria-pressed="false" data-filter="{k}">{c["work_cats"][k]}</button>' for k in cats)
    items = "".join(f"""<article class="item {size} reveal" data-cat="{cat}">{photo(f'work-{i+1}.jpg', t.replace('&amp;', '&').lower(), kind)}<h3>{t}</h3><p>{loc}</p></article>"""
                    for i, (cat, t, loc, size, kind) in enumerate(c["work"]))
    wp = c["pages"]["work"]
    body = f"""<section class="page-head"><div class="wrap"><span class="crumb"><a href="index.html">Home</a> / Gallery</span><h1 data-split>{wp['title']}</h1><p class="lede">{wp['lede']}</p></div></section>
<section class="section" style="padding-top:clamp(2.5rem,5vw,4rem)"><div class="wrap"><div class="filters" role="group" aria-label="Filter projects">{filt}</div><div class="gallery">{items}</div></div></section>
{joint()}{band(c, wp.get('band_title'), wp.get('band_text'))}"""
    page(c, out, "work.html", c["meta"]["work"][0], c["meta"]["work"][1], body)

    # About
    ap = c["pages"]["about"]
    vals = "".join(f'<div class="reveal"><h3>{t}</h3><p>{d}</p></div>' for t, d in ap["values"])
    body = f"""<section class="page-head"><div class="wrap"><span class="crumb"><a href="index.html">Home</a> / About</span><h1 data-split>{ap['title']}</h1><p class="lede">{ap['lede']}</p></div></section>
{feature(c, ap['story'])}
<section class="section {ap.get('values_cls', 'alt')}"><div class="wrap"><h2 data-split style="margin-bottom:clamp(2.5rem,5vw,3.5rem);max-width:18ch">{ap['values_title']}</h2><div class="values">{vals}</div></div></section>
{area(c)}
{joint()}{band(c)}"""
    page(c, out, "about.html", c["meta"]["about"][0], c["meta"]["about"][1], body)

    # Contact
    cp = c["pages"]["contact"]
    chips = "".join(f'<label><input type="checkbox" name="type" value="{x}"><span>{x}</span></label>' for x in cp["chips"])
    email_block = f'<div class="aside-block"><h3>Email</h3><p><a href="mailto:{c["email"]}">{c["email"]}</a></p></div>' if c.get("email") else ""
    hours_block = f'<div class="aside-block"><h3>Hours</h3><p>{c["hours"]}</p></div>' if c.get("hours") else ""
    body = f"""<section class="page-head"><div class="wrap"><span class="crumb"><a href="index.html">Home</a> / Contact</span><h1 data-split>{cp['title']}</h1><p class="lede">{cp['lede']}</p></div></section>
<section class="section" style="padding-top:clamp(2.5rem,5vw,4rem)">
  <div class="wrap contact">
    <form class="form" novalidate>
      <div class="grid">
        <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" required><p class="err">Please tell us your name.</p></div>
        <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required><p class="err">We need a phone number to call you back.</p></div>
        <div class="field"><label for="f-email">Email <span class="opt">(optional)</span></label><input id="f-email" name="email" type="email" autocomplete="email"><p class="err">That email doesn&rsquo;t look right. Check for a typo.</p></div>
        <div class="field"><label for="f-town">Town or neighborhood</label><input id="f-town" name="town" autocomplete="address-level2" placeholder="e.g. {c['area']['towns'][0]}"></div>
        <fieldset class="field full"><legend>What can we help with? <span class="opt">(pick any)</span></legend><div class="chips">{chips}</div></fieldset>
        <div class="field full"><label for="f-msg">Tell us about your project <span class="opt">(optional)</span></label><textarea id="f-msg" name="message" placeholder="What you have in mind, timing, anything we should know&hellip;"></textarea></div>
      </div>
      <div class="submit-row"><button class="btn" type="submit">{cp['submit']} {icon("arrow")}</button><span class="small">Or call <a class="num" href="tel:{c['tel']}">{c['phone']}</a></span></div>
      <div class="done" role="status" aria-live="polite" tabindex="-1"><h2>Thank you. We&rsquo;ve got it.</h2><p class="lede">{cp['done']} If it&rsquo;s easier, call us at <a class="num" href="tel:{c['tel']}">{c['phone']}</a>.</p></div>
    </form>
    <aside>
      <div class="aside-block"><h3>Call us</h3><a class="tel num" href="tel:{c['tel']}">{c['phone']}</a></div>
      {email_block}
      <div class="aside-block"><h3>Office</h3><p>{c['address']}</p></div>
      {hours_block}
      <div class="aside-block"><h3>Where we work</h3><p>{', '.join(c['area']['towns'])}.</p></div>
    </aside>
  </div>
</section>"""
    page(c, out, "contact.html", c["meta"]["contact"][0], c["meta"]["contact"][1], body)
    print("built", out.name)


THEME_DEFAULTS = {
    "bg": "#ffffff", "bg-2": "#f4f2ee", "ink": "#16181a", "ink-2": "#3b3f44", "muted": "#5f656b",
    "line": "rgba(0,0,0,.1)", "line-strong": "rgba(0,0,0,.22)", "card": "#ffffff",
    "accent": "#333", "accent-hi": "#444", "accent-ink": "#fff", "accent-text": "#333", "accent-on-dark": "#fff",
    "accent-2": "#555", "accent-2-hi": "#666", "accent-2-ink": "#fff",
    "focus": "#333", "focus-ring": "rgba(0,0,0,.15)", "error": "#b3261e", "star": "#f2b01e",
    "dark": "#15171a", "dark-ink": "#f3f3f1", "dark-ink-2": "#b9bcbf",
    "topbar-bg": "#15171a", "topbar-ink": "#fff", "header-bg": "#fff", "header-ink": "#16181a", "nav-current": "inherit",
    "scrim": "rgba(0,0,0,.82)", "panel-bg": "rgba(255,255,255,.9)", "panel-ink": "#16181a", "panel-ink-2": "#3b3f44",
    "trust-bg": "#15171a", "trust-ink": "#fff", "trust-line": "rgba(255,255,255,.14)", "trust-icon": "#fff",
    "band-bg": "#15171a", "band-ink": "#fff", "band-ink-2": "rgba(255,255,255,.85)", "on-light-accent": "#16181a",
    "footer-bg": "#0f1113", "footer-ink": "#e9e9e7", "footer-head": "#fff", "footer-line": "rgba(255,255,255,.14)",
    "pagehead-bg": "#f4f2ee", "pagehead-ink": "#16181a", "pagehead-ink-2": "#3b3f44",
    "input-bg": "#fff", "input-line": "rgba(0,0,0,.25)",
    "callbar-call": "#16181a", "callbar-call-ink": "#fff",
    "f-display": "system-ui", "f-body": "system-ui", "f-script": "cursive",
    "display-weight": "800", "display-tracking": "-0.01em", "display-case": "none", "display-leading": "1.06",
    "radius-btn": "4px", "radius-img": "4px", "radius-lg": "6px", "radius-input": "4px",
    "joint": "none", "joint-h": "26px", "joint-size": "auto 100%",
    "logo-size": "1.25rem", "logo-weight": "800", "logo-tracking": "0.01em", "logo-case": "none", "f-logo": "var(--f-display)",
    "nav-size": "var(--step-0)", "btn-case": "none", "btn-tracking": "0.01em",
}


def theme(extra_css="", **tokens):
    t = dict(THEME_DEFAULTS)
    t.update({k.replace("_", "-"): v for k, v in tokens.items()})
    body = "\n".join(f"  --{k}: {v};" for k, v in t.items())
    return f":root {{\n{body}\n}}\n{extra_css}\n"


def svg_uri(svg):
    import urllib.parse
    return 'url("data:image/svg+xml,' + urllib.parse.quote(svg, safe=" =:/,'") + '")'


def write_readme(c, out, confirm):
    out = Path(out)
    rows = [("hero.jpg", "Big photo at the top of the homepage")]
    rows += [(s["img"], f"{s['name'].replace('&amp;', '&')} (Services page + homepage)") for s in c["services"]]
    for k in ("feature", "feature2"):
        if c.get(k):
            rows.append((c[k]["img"], c[k]["photo_label"] + " (homepage)"))
    rows.append((c["pages"]["about"]["story"]["img"], c["pages"]["about"]["story"]["photo_label"] + " (About page)"))
    rows += [(f"work-{i+1}.jpg", f"Gallery: {w[1].replace('&amp;', '&')}") for i, w in enumerate(c["work"])]
    table = "\n".join(f"| {a} | {b} |" for a, b in rows)
    conf = "\n".join(f"- {x}" for x in confirm)
    (out / "README.md").write_text(f"""# {c['name']}: redesign demo

Free demo site by Legend Creative. Colors, tagline and wording are matched to their current site.

**Pages:** Home, Services, Gallery, About, Contact. Open `index.html` to preview.
To put it online for free, drag this folder onto https://app.netlify.com/drop.

## Photos
Every photo spot shows placeholder art with a "PHOTO:" tag. To use real photos, save them into `images/` with these names and they appear automatically.

| File name | Where it shows |
|---|---|
{table}

## Confirm with the client before going live
- Reviews: the four review cards are placeholders. Paste in real Google reviews.
- The contact form shows a thank-you message but doesn't send anywhere yet. Connect it to their email (Netlify Forms or Formspree).
{conf}

## Editing
All text lives in `site.py`. Edit it, then run `python3 site.py`. The shared layout lives in `sites/_engine/`.
""")
