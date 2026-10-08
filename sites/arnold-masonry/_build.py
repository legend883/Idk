"""Builds the static pages. Edit content here, then run: python3 _build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
PHONE = "(770) 345-2686"
TEL = "+17703452686"
ADDRESS = "6065 Roswell Rd, Suite 450<br>Atlanta, GA 30328"

ICONS = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<symbol id="i-phone" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" d="M5 3.5h3.2l1.6 4.2-2.1 1.4a11.5 11.5 0 0 0 7.2 7.2l1.4-2.1 4.2 1.6V19a1.9 1.9 0 0 1-2 1.9C10.6 20.4 3.6 13.4 3.1 5.5A1.9 1.9 0 0 1 5 3.5Z"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" d="M4 12h15m-6-6 6 6-6 6"/></symbol>
<symbol id="i-star" viewBox="0 0 24 24"><path fill="currentColor" d="m12 2.8 2.8 5.9 6.4.8-4.7 4.4 1.2 6.4L12 17.2l-5.7 3.1 1.2-6.4-4.7-4.4 6.4-.8z"/></symbol>
<symbol id="i-photo" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" d="M3.5 7.5h3.6l1.6-2.5h6.6l1.6 2.5h3.6v11.5h-17z"/><circle cx="12" cy="12.8" r="3.6" fill="none" stroke="currentColor" stroke-width="1.6"/></symbol>
<symbol id="i-menu" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" d="M4 7h16M4 12h16M4 17h16"/></symbol>
</svg>"""


def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} aria-hidden="true"><use href="#i-{name}"/></svg>'


def stars():
    return '<span class="stars" aria-hidden="true">' + icon("star") * 5 + "</span>"


def photo(src, label, cls="", alt=""):
    """Image slot: shows the real photo when images/<src> exists, a labelled stone placeholder otherwise."""
    c = f"photo {cls}".strip()
    return (
        f'<figure class="{c}"><img src="images/{src}" alt="{alt or label}" loading="lazy" decoding="async">'
        f'<figcaption class="ph-label">{icon("photo")}<span>Photo: {label}</span></figcaption></figure>'
    )


COURSES = '<div class="courses" aria-hidden="true"><i class="c1"></i><i class="c2"></i><i class="c3"></i></div>'

NAV = [("index.html", "Home"), ("services.html", "Services"), ("work.html", "Our Work"), ("about.html", "About")]


def header(current):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV
    )
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="mark" href="index.html" aria-label="Arnold Masonry and Landscape, home"><b>ARNOLD</b><span>Masonry &amp; Landscape</span><svg class="swoosh" viewBox="0 0 200 8" preserveAspectRatio="none" aria-hidden="true"><path d="M2 6 C 60 0, 140 0, 198 5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">{icon("menu")}<span>Menu</span></button>
    <nav class="nav" id="nav" aria-label="Main">
      {links}
      <a class="tel" href="tel:{TEL}">{icon("phone")}<span class="num">{PHONE}</span></a>
      <a class="btn" href="contact.html">Request a quote</a>
    </nav>
  </div>
</header>"""


def footer():
    return f"""<footer class="site-footer on-dark">
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="mark" href="index.html"><b>ARNOLD</b><span>Masonry &amp; Landscape</span></a>
        <p style="margin-top:1.4rem;max-width:32ch">Master masons building outdoor kitchens, fireplaces and stone patios across North Atlanta since 1985.</p>
      </div>
      <div>
        <p class="fh">What we build</p>
        <ul>
          <li><a href="services.html#kitchens">Outdoor kitchens</a></li>
          <li><a href="services.html#fireplaces">Fireplaces &amp; chimneys</a></li>
          <li><a href="services.html#patios">Patios &amp; pool decks</a></li>
          <li><a href="services.html#walls">Walls, steps &amp; columns</a></li>
        </ul>
      </div>
      <div>
        <p class="fh">Company</p>
        <ul>
          <li><a href="about.html">Our story</a></li>
          <li><a href="work.html">Our work</a></li>
          <li><a href="contact.html">Free consultation</a></li>
        </ul>
      </div>
      <div>
        <p class="fh">Visit or call</p>
        <address>{ADDRESS}<br><a class="num" href="tel:{TEL}">{PHONE}</a></address>
      </div>
    </div>
    <div class="legal"><span>&copy; <span data-year>2026</span> Arnold Masonry &amp; Landscape. Est. 1985.</span><span>Atlanta, Georgia</span></div>
  </div>
</footer>
<nav class="callbar" aria-label="Quick contact">
  <a href="tel:{TEL}">{icon("phone")}Call</a>
  <a href="contact.html">Request a quote {icon("arrow")}</a>
</nav>"""


def band(title="Let&rsquo;s walk your backyard.", text="Tell us what you&rsquo;re picturing. We&rsquo;ll come out, look at the space, and talk through what it would take to build it in stone."):
    return f"""<section class="band">
  <div class="wrap row">
    <div>
      <h2 data-chisel>{title}</h2>
      <p class="lede" style="margin-top:1.2rem">{text}</p>
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:1rem 1.6rem;align-items:center">
      <a class="btn btn--light" href="contact.html">Request a quote {icon("arrow")}</a>
      <a class="tel" href="tel:{TEL}">{icon("phone")}<span class="num">{PHONE}</span></a>
    </div>
  </div>
</section>"""


def page(name, title, desc, body):
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#1e2327">
<link rel="preload" href="assets/fonts/Cinzel-0.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/site.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body>
{ICONS}
{header(name)}
<main id="main">
{body}
</main>
{footer()}
<script src="assets/js/vendor/gsap.min.js" defer></script>
<script src="assets/js/vendor/ScrollTrigger.min.js" defer></script>
<script src="assets/js/vendor/SplitText.min.js" defer></script>
<script src="assets/js/site.js" defer></script>
</body>
</html>
"""
    (ROOT / name).write_text(html)


# ── Home ───────────────────────────────────────────────
SERVICES = [
    ("kitchens", "I", "Outdoor kitchens", "Stone and brick grill islands, bar counters and full kitchens, built as permanent masonry.", "kitchen.jpg"),
    ("fireplaces", "II", "Fireplaces &amp; chimneys", "Outdoor fireplaces, custom chimneys and fire pits that draw right and age well.", "fireplace.jpg"),
    ("patios", "III", "Patios &amp; pool decks", "Flagstone, brick and natural stone patios and pool decks, set on a proper base.", "patio.jpg"),
    ("walls", "IV", "Walls, steps &amp; columns", "Retaining walls, stone stairs, columns and the brick and stone details that tie it all together.", "walls.jpg"),
]

index_rows = "".join(
    f"""<a class="index-row reveal" href="services.html#{sid}">
      <span class="no">{no}</span><h3>{name}</h3><p>{blurb}</p>{icon("arrow", "arrow")}
      {photo(img, name.replace("&amp;", "&"), "peek")}
    </a>"""
    for sid, no, name, blurb, img in SERVICES
)

home = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div class="slab">
      <h1 data-chisel="hero" aria-label="Arnold">ARNOLD</h1>
      <p class="inscr" aria-label="Masonry and Landscape, serving Atlanta since 1985"><span>Masonry &amp; Landscape</span><span>Since 1985</span></p>
      <div class="rule" aria-hidden="true"></div>
      <p class="promise hero-in">Changing the landscape and hardscape of Atlanta.</p>
      <p class="hero-in" style="color:var(--iron-2);max-width:44ch;margin-bottom:1.6rem">Luxury outdoor living: stone kitchens, fireplaces and patios, built by master masons since 1985.</p>
      <div class="actions hero-in">
        <a class="btn" href="contact.html">Request a quote {icon("arrow")}</a>
        <a class="btn btn--blue" href="work.html">View gallery</a>
        <a class="tel" href="tel:{TEL}">{icon("phone")}<span class="num">{PHONE}</span></a>
      </div>
      <div class="hero-proof hero-in">
        <span>{stars()} <b class="num">4.8</b> on Google</span>
        <span><b>41 years</b> of masonry in North Atlanta</span>
      </div>
    </div>
    {photo("hero.jpg", "stone outdoor kitchen at dusk", "hero-photo", "A stone outdoor kitchen with a chimney, built by Arnold Masonry")}
  </div>
</section>

{COURSES}

<section class="section" aria-labelledby="build-h">
  <div class="wrap">
    <div class="section-head">
      <h2 id="build-h" class="cut-h" data-chisel>What we build</h2>
      <p class="lede">Everything here is laid by masons, in brick and natural stone. No kits, no veneer panels pretending to be stone.</p>
    </div>
    <div class="index">{index_rows}</div>
  </div>
</section>

<section class="section" style="padding-top:0" aria-labelledby="line-h">
  <div class="wrap lineage">
    {photo("scott.jpg", "Scott Arnold on a job site", "reveal", "Scott Arnold, master mason and founder")}
    <div class="reveal">
      <h2 id="line-h" class="cut-h" data-chisel style="margin-bottom:1.6rem">Learned by hand. Signed since 1985.</h2>
      <p class="lede">At seventeen, Scott Arnold moved from Long Island to Atlanta and went to work in construction. An older master mason took him under his wing and taught him the trade the way it has always been taught: on the job, one course at a time.</p>
      <p>In 1985 Scott put his own name on the work. Four decades later, ARNOLD is still a company of masons, building the kind of stonework that gets handed down with the house.</p>
      <a class="textlink" href="about.html" style="margin-top:0.8rem">Read our story {icon("arrow")}</a>
    </div>
  </div>
</section>

<section class="section on-dark" aria-labelledby="proj-h">
  <div class="wrap">
    <div class="section-head">
      <h2 id="proj-h" data-chisel>A backyard in Sandy Springs, built in stone</h2>
      <p class="lede">One project, start to finish: a stone kitchen and chimney anchoring a flagstone patio, a fire pit, and the retaining walls that made the slope usable.</p>
    </div>
    <div class="project">
      {photo("sandy-springs-1.jpg", "Sandy Springs outdoor stone kitchen", "big reveal")}
      {photo("sandy-springs-2.jpg", "custom chimney", "sm reveal")}
      {photo("sandy-springs-3.jpg", "fire pit and flagstone patio", "sm reveal")}
    </div>
    <div class="spec reveal">
      <div><a class="btn btn--ghost" href="work.html">See more of our work {icon("arrow")}</a></div>
      <dl>
        <dt>Location</dt><dd>Sandy Springs, Georgia</dd>
        <dt>Kitchen</dt><dd>Outdoor stone kitchen</dd>
        <dt>Fire</dt><dd>Custom chimney and a stone fire pit</dd>
        <dt>Ground</dt><dd>Flagstone patio</dd>
        <dt>Structure</dt><dd>Retaining walls</dd>
      </dl>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="proc-h">
  <div class="wrap">
    <div class="section-head">
      <h2 id="proc-h" class="cut-h" data-chisel>How a project comes together</h2>
      <p class="lede">You deal with us from the first walk around the yard to the final walkthrough.</p>
    </div>
    <ol class="process">
      <li class="reveal"><span class="step" aria-hidden="true">I</span><h3>Consultation</h3><p>We visit, walk the space with you, and talk about how you want to use it: cooking, entertaining, a quiet fire on a cold night.</p></li>
      <li class="reveal"><span class="step" aria-hidden="true">II</span><h3>Design</h3><p>A layout drawn for your yard, with stone and brick chosen together and a clear written proposal.</p></li>
      <li class="reveal"><span class="step" aria-hidden="true">III</span><h3>Build</h3><p>Masons lay it by hand, on a proper footing, with the drainage and structure no one sees but everyone relies on.</p></li>
      <li class="reveal"><span class="step" aria-hidden="true">IV</span><h3>Walkthrough</h3><p>We go over every detail with you before we call it done. Then it&rsquo;s yours for the next few decades.</p></li>
    </ol>
  </div>
</section>

<section class="section" style="padding-top:0" aria-labelledby="rev-h">
  <div class="wrap reviews">
    <div class="reveal">
      <h2 id="rev-h" class="sr-only">Reviews</h2>
      <div class="score num" aria-label="Rated 4.8 out of 5">4.8</div>
      <div class="score-meta">{stars()}<span class="small">Average Google rating from North Atlanta homeowners. 4.7 on Yelp.</span></div>
    </div>
    <div class="quotes">
      <figure class="reveal"><blockquote class="todo">[Google review from a homeowner. We&rsquo;ll place your four best reviews here.]</blockquote><figcaption>Homeowner, North Atlanta</figcaption></figure>
      <figure class="reveal"><blockquote class="todo">[Google review from a homeowner.]</blockquote><figcaption>Homeowner, North Atlanta</figcaption></figure>
      <figure class="reveal"><blockquote class="todo">[Google review from a homeowner.]</blockquote><figcaption>Homeowner, North Atlanta</figcaption></figure>
      <figure class="reveal"><blockquote class="todo">[Google review from a homeowner.]</blockquote><figcaption>Homeowner, North Atlanta</figcaption></figure>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0" aria-labelledby="area-h">
  <div class="wrap">
    <h2 id="area-h" class="small" style="font-family:var(--f-body);font-size:var(--step--1);letter-spacing:.04em;font-weight:600;margin-bottom:1.2rem;color:var(--iron-3)">Building across North Atlanta</h2>
    <p class="area reveal"><span>Atlanta</span><span>Sandy Springs</span><span>Buckhead</span><span>Dunwoody</span><span>Roswell</span><span>Alpharetta</span><span>Milton</span><span>Johns Creek</span></p>
  </div>
</section>

{COURSES}
{band()}
"""

page("index.html", "Arnold Masonry & Landscape | Outdoor Kitchens & Stonework in North Atlanta",
     "Master masons since 1985. Stone outdoor kitchens, fireplaces, chimneys and patios built by hand across North Atlanta.", home)

# ── Services ───────────────────────────────────────────
SVC_DETAIL = {
    "kitchens": ("Outdoor kitchens", "A kitchen outside should be built like the house, not bolted together. We build ours as real masonry, in stone or brick, sized for how you cook and how many people end up standing around it.",
                 ["Grill islands and grill enclosures", "Bar and serving counters with seating", "Room for your appliances, sinks and storage", "Stone or brick to match your home", "Paired with a fireplace, patio or pergola"]),
    "fireplaces": ("Fireplaces &amp; chimneys", "An outdoor fireplace becomes the reason everyone stays outside after dark. We design the firebox and chimney so it draws properly, and finish it in stone that suits the house.",
                   ["Outdoor fireplaces", "Custom stone and brick chimneys", "Fire pits", "Hearths and seat walls", "Kitchen and fireplace combinations"]),
    "patios": ("Patios &amp; pool decks", "A patio is only as good as what&rsquo;s under it. We start with the base and drainage, then lay flagstone, brick or natural stone that stays flat and handsome for decades.",
               ["Flagstone and natural stone patios", "Brick patios and walkways", "Pool decks and coping", "Stone steps and landings", "Drainage built in from the start"]),
    "walls": ("Walls, steps &amp; columns", "The structural masonry that turns a sloped or awkward yard into usable space, and the details that make it look like it was always there.",
              ["Retaining walls", "Stone stairs", "Brick and stone columns", "Seat walls and garden walls", "Brick and stone repair and rebuilding"]),
}
SVC_CTA = {"kitchens": "Plan an outdoor kitchen", "fireplaces": "Plan a fireplace", "patios": "Plan a patio", "walls": "Plan walls or steps"}
svc_sections = "".join(
    f"""<section class="svc wrap" id="{sid}" aria-labelledby="{sid}-h">
  {photo(img, SVC_DETAIL[sid][0].replace("&amp;", "&").lower())}
  <div class="reveal">
    <h2 id="{sid}-h" class="cut-h" data-chisel>{SVC_DETAIL[sid][0]}</h2>
    <p class="lede">{SVC_DETAIL[sid][1]}</p>
    <ul>{"".join(f"<li>{x}</li>" for x in SVC_DETAIL[sid][2])}</ul>
    <a class="btn" href="contact.html">{SVC_CTA[sid]} {icon("arrow")}</a>
  </div>
</section>"""
    for sid, _, _, _, img in SERVICES
)
services = f"""
<section class="page-head">
  <div class="wrap">
    <span class="crumb"><a href="index.html">Home</a> / Services</span>
    <h1 data-chisel>Built in stone, by masons</h1>
    <p class="lede">Outdoor kitchens, fireplaces, patios and structural masonry for North Atlanta homes. Every project is laid by hand, in brick and natural stone.</p>
    <nav class="jump" aria-label="Services on this page">{"".join(f'<a href="#{s[0]}">{s[2]}</a>' for s in SERVICES)}</nav>
  </div>
</section>
{svc_sections}
<div style="height:var(--section)"></div>
{COURSES}
{band()}
"""
page("services.html", "Services | Outdoor Kitchens, Fireplaces & Patios | Arnold Masonry",
     "Outdoor kitchens, fireplaces, chimneys, patios, pool decks, retaining walls and stone steps, built by master masons in North Atlanta.", services)

# ── Work ───────────────────────────────────────────────
WORK = [
    ("kitchens", "Outdoor stone kitchen &amp; chimney", "Sandy Springs", "wide"),
    ("fireplaces", "Outdoor fireplace", "North Atlanta", ""),
    ("patios", "Flagstone patio", "Sandy Springs", ""),
    ("kitchens", "Grill enclosure", "North Atlanta", ""),
    ("walls", "Retaining walls", "Sandy Springs", ""),
    ("fireplaces", "Stone fire pit", "Sandy Springs", ""),
    ("patios", "Pool deck", "North Atlanta", "wide"),
    ("walls", "Stone stairs &amp; columns", "North Atlanta", ""),
    ("kitchens", "Kitchen &amp; fireplace combination", "North Atlanta", ""),
    ("patios", "Brick patio &amp; walkway", "North Atlanta", ""),
]
work_items = "".join(
    f"""<article class="item {size} reveal" data-cat="{cat}">
  {photo(f"work-{i+1}.jpg", t.replace("&amp;", "&").lower())}
  <h3>{t}</h3><p>{loc}</p>
</article>"""
    for i, (cat, t, loc, size) in enumerate(WORK)
)
work = f"""
<section class="page-head">
  <div class="wrap">
    <span class="crumb"><a href="index.html">Home</a> / Our work</span>
    <h1 data-chisel>Forty years of work, still standing</h1>
    <p class="lede">A selection of outdoor kitchens, fireplaces, patios and walls we&rsquo;ve built around North Atlanta.</p>
  </div>
</section>
<section class="section" style="padding-top:clamp(2.5rem,5vw,4rem)">
  <div class="wrap">
    <div class="filters" role="group" aria-label="Filter projects">
      <button aria-pressed="true" data-filter="all">All work</button>
      <button aria-pressed="false" data-filter="kitchens">Outdoor kitchens</button>
      <button aria-pressed="false" data-filter="fireplaces">Fireplaces</button>
      <button aria-pressed="false" data-filter="patios">Patios &amp; decks</button>
      <button aria-pressed="false" data-filter="walls">Walls &amp; steps</button>
    </div>
    <div class="gallery">{work_items}</div>
  </div>
</section>
{COURSES}
{band("Picture this in your yard?", "Every project starts with a visit. We&rsquo;ll look at your space and talk through what&rsquo;s possible.")}
"""
page("work.html", "Our Work | Stone Outdoor Kitchens & Fireplaces | Arnold Masonry",
     "Outdoor kitchens, fireplaces, patios and stone walls built by Arnold Masonry & Landscape across North Atlanta.", work)

# ── About ──────────────────────────────────────────────
about = f"""
<section class="page-head">
  <div class="wrap">
    <span class="crumb"><a href="index.html">Home</a> / About</span>
    <h1 data-chisel>A trade, handed down</h1>
    <p class="lede">ARNOLD Masonry &amp; Landscape is a company of master masons that has been building in Atlanta and North Atlanta since 1985.</p>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="story reveal">
      <div class="year">Age 17</div>
      <div class="body"><p>Scott Arnold moved from Long Island, New York, to Atlanta at seventeen and went straight to work in construction. Not long after, an older master mason took him under his wing and taught him the trade.</p><p>That&rsquo;s how masonry has always been learned: standing next to someone who knows, laying course after course until your hands understand what your eyes can&rsquo;t yet see.</p></div>
    </div>
    <div class="story reveal">
      <div class="year num">1985</div>
      <div class="body"><p>Scott started his own company and put the family name on it. Brick and stone were the foundation of the business from the first day, and they still are.</p></div>
    </div>
    <div class="story reveal">
      <div class="year">Today</div>
      <div class="body"><p>Four decades on, ARNOLD builds outdoor kitchens, fireplaces and chimneys, patios, pool decks, stairs, columns and walls for homeowners across North Atlanta, with the same standards Scott learned as an apprentice.</p></div>
    </div>
  </div>
</section>
<section class="section on-dark">
  <div class="wrap">
    <h2 data-chisel style="margin-bottom:clamp(2.5rem,5vw,4rem);max-width:18ch">What we hold ourselves to</h2>
    <div class="tenets">
      <div class="reveal"><h3>Built to outlast the house</h3><p>Proper footings, real stone and brick, and drainage done right. Masonry should be the last thing on your property that needs attention.</p></div>
      <div class="reveal"><h3>Masons, not middlemen</h3><p>We&rsquo;re a masonry company first. The people who design your project understand how it gets built.</p></div>
      <div class="reveal"><h3>Our name on every job</h3><p>ARNOLD has been the name on the work since 1985. We build every project like it&rsquo;s going to be judged forty years from now, because it will be.</p></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap lineage">
    {photo("scott.jpg", "Scott Arnold, master mason", "reveal", "Scott Arnold, master mason and founder")}
    <div class="reveal">
      <h2 class="cut-h" data-chisel style="margin-bottom:1.4rem">Meet Scott</h2>
      <p class="lede">Founder and master mason. Scott still walks projects with homeowners and cares about the details that only another mason would notice.</p>
      <a class="btn" href="contact.html" style="margin-top:1rem">Request a quote {icon("arrow")}</a>
    </div>
  </div>
</section>
{COURSES}
{band()}
"""
page("about.html", "About | Master Masons Since 1985 | Arnold Masonry & Landscape",
     "Scott Arnold learned masonry as an apprentice and founded ARNOLD Masonry & Landscape in Atlanta in 1985.", about)

# ── Contact ────────────────────────────────────────────
contact = f"""
<section class="page-head">
  <div class="wrap">
    <span class="crumb"><a href="index.html">Home</a> / Free consultation</span>
    <h1 data-chisel>Let&rsquo;s walk your backyard</h1>
    <p class="lede">Tell us a little about your project and the best way to reach you. We&rsquo;ll call to set up a visit.</p>
  </div>
</section>
<section class="section" style="padding-top:clamp(2.5rem,5vw,4rem)">
  <div class="wrap contact">
    <form class="form" novalidate>
      <div class="grid">
        <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" required><p class="err">Please tell us your name.</p></div>
        <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required><p class="err">We need a phone number to call you back.</p></div>
        <div class="field"><label for="f-email">Email <span class="opt">(optional)</span></label><input id="f-email" name="email" type="email" autocomplete="email"><p class="err">That email doesn&rsquo;t look right. Check for a typo.</p></div>
        <div class="field"><label for="f-town">Town or neighborhood</label><input id="f-town" name="town" autocomplete="address-level2" placeholder="e.g. Sandy Springs"></div>
        <fieldset class="field full"><legend>What are you thinking about? <span class="opt">(pick any)</span></legend>
          <div class="chips">
            <label><input type="checkbox" name="type" value="Outdoor kitchen"><span>Outdoor kitchen</span></label>
            <label><input type="checkbox" name="type" value="Fireplace or fire pit"><span>Fireplace or fire pit</span></label>
            <label><input type="checkbox" name="type" value="Patio or pool deck"><span>Patio or pool deck</span></label>
            <label><input type="checkbox" name="type" value="Walls, steps or columns"><span>Walls, steps or columns</span></label>
            <label><input type="checkbox" name="type" value="Not sure yet"><span>Not sure yet</span></label>
          </div>
        </fieldset>
        <fieldset class="field full"><legend>Rough budget <span class="opt">(optional)</span></legend>
          <div class="chips">
            <label><input type="radio" name="budget" value="$15k-$30k"><span>$15k&ndash;$30k</span></label>
            <label><input type="radio" name="budget" value="$30k-$60k"><span>$30k&ndash;$60k</span></label>
            <label><input type="radio" name="budget" value="$60k+"><span>$60k+</span></label>
            <label><input type="radio" name="budget" value="Not sure"><span>Not sure yet</span></label>
          </div>
        </fieldset>
        <div class="field full"><label for="f-msg">Anything else? <span class="opt">(optional)</span></label><textarea id="f-msg" name="message" placeholder="How you&rsquo;d use the space, timing, photos you&rsquo;ve saved&hellip;"></textarea></div>
      </div>
      <div class="submit-row">
        <button class="btn" type="submit">Request my consultation {icon("arrow")}</button>
        <span class="small">Or call <a class="num" href="tel:{TEL}">{PHONE}</a></span>
      </div>
      <div class="done" role="status" aria-live="polite" tabindex="-1">
        <h2 class="cut-h">Thank you. We&rsquo;ve got it.</h2>
        <p class="lede">We&rsquo;ll call you to set up a time to walk the space. If it&rsquo;s easier, call us any time at <a class="num" href="tel:{TEL}">{PHONE}</a>.</p>
      </div>
    </form>
    <aside>
      <div class="aside-block"><h3>Call us</h3><a class="tel num" href="tel:{TEL}">{PHONE}</a></div>
      <div class="aside-block"><h3>Office</h3><p>{ADDRESS}</p><p style="margin-top:.6rem"><a class="textlink" href="https://maps.google.com/?q=6065+Roswell+Rd+Suite+450+Atlanta+GA+30328" rel="noopener">Get directions {icon("arrow")}</a></p></div>
      <div class="aside-block"><h3>Where we build</h3><p>Atlanta and North Atlanta: Sandy Springs, Buckhead, Dunwoody, Roswell, Alpharetta, Milton, Johns Creek.</p></div>
      <div class="aside-block"><h3>What happens next</h3><p>We call you, set a time to visit, walk the space together, and follow up with a design and a written proposal.</p></div>
    </aside>
  </div>
</section>
"""
page("contact.html", "Free Design Consultation | Arnold Masonry & Landscape",
     "Request a design consultation for an outdoor kitchen, fireplace, patio or stonework in North Atlanta. Call (770) 345-2686.", contact)

print("built")
