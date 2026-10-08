"""ITM Landscape demo. Edit text below, then run: python3 site.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_engine"))
from engine import build, theme, svg_uri, stars, write_readme  # noqa: E402

LIME, GREEN_DK, INK, BADGE = "#6abf3a", "#2f6b17", "#1a2214", "#1d3a8a"
SPROUTS = svg_uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="48" height="26"><rect y="20" width="48" height="6" fill="{GREEN_DK}"/><path d="M12 20c0-6-4-10-9-11 1 6 4 9 9 11zm0 0c0-7 4-12 10-13-1 7-5 11-10 13z" fill="{LIME}"/><path d="M36 20c0-4-3-7-6-8 0 4 3 6 6 8zm0 0c0-5 3-8 7-9-1 5-3 7-7 9z" fill="#57a52c"/></svg>')
MARK = ('<svg class="logo-mark" viewBox="0 0 48 48" aria-hidden="true">'
        f'<path d="M22 38c0-14-6-24-18-28 2 14 8 24 18 28z" fill="{LIME}"/><path d="M22 38c2-12 10-20 22-22-2 12-10 20-22 22z" fill="#57a52c"/>'
        f'<path d="M22 38c-1-8-1-15 2-22" stroke="{GREEN_DK}" stroke-width="2" fill="none"/></svg>')

CONFIG = {
    "name": "ITM Landscape",
    "logo": {"name": "ITM <i>Landscape</i>", "sub": "Beautiful. Reliable. Local.", "mark": MARK},
    "phone": "678-773-0380", "tel": "+16787730380",
    "email": "office@itmlandscape.com",
    "address": "995 Cripple Creek Dr<br>Lawrenceville, GA 30043",
    "cta": "Get a quote",
    "theme_color": "#ffffff",
    "footer_blurb": "ITM Landscape designs and maintains functional outdoor environments for residential and commercial properties across Greater Atlanta.",
    "footer_right": "Voted Best of Gwinnett 2025",
    "fonts_url": "https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,400;0,500;0,600;0,700;0,800;1,700&display=swap",
    "theme_css": theme(
        f"""
.logo b {{ font-style: italic; font-weight: 800; font-size: 1.55rem; color: {LIME}; letter-spacing: -0.01em; }}
.logo b i {{ font-size: .7em; color: {GREEN_DK}; letter-spacing: .02em; text-transform: uppercase; }}
.site-footer .logo b i {{ color: #b8e39b; }}
.site-header .logo span {{ text-transform: none; letter-spacing: .04em; font-size: .74rem; }}
.nav a:not(.btn) {{ text-transform: uppercase; font-weight: 700; letter-spacing: .02em; font-size: .92rem; }}
.hero--overlay .kick-script {{ font-family: 'Barlow', sans-serif; font-weight: 700; font-size: clamp(.9rem, .8rem + .4vw, 1.1rem); letter-spacing: .32em; text-transform: uppercase; color: #fff; }}
.hero--overlay .accent-bar {{ display: none; }}
.hero--overlay h1 {{ max-width: 17ch; }}
.trust svg {{ color: {LIME}; }}
.statement em {{ color: {LIME}; }}
""",
        bg="#ffffff", **{"bg-2": "#f3f8ef"}, ink=INK, **{"ink-2": "#3b4634"}, muted="#5c6855",
        **{"line": "rgba(26,34,20,.1)", "line-strong": "rgba(26,34,20,.22)"},
        accent=LIME, **{"accent-hi": "#7bcc4c", "accent-ink": "#10200a", "accent-text": GREEN_DK, "accent-on-dark": LIME},
        **{"accent-2": GREEN_DK, "accent-2-hi": "#3a7f1e", "accent-2-ink": "#ffffff"},
        focus=GREEN_DK, **{"focus-ring": "rgba(106,191,58,.35)"}, star="#f5b72b",
        dark="#1c3311", **{"dark-ink": "#ffffff", "dark-ink-2": "#cfe0c4"},
        **{"topbar-bg": BADGE, "topbar-ink": "#ffffff", "header-bg": "#ffffff", "header-ink": INK, "nav-current": GREEN_DK},
        **{"trust-bg": INK, "trust-ink": "#ffffff", "trust-line": "rgba(255,255,255,.12)"},
        **{"band-bg": LIME, "band-ink": "#10200a", "band-ink-2": "#1f3712"},
        **{"footer-bg": "#121a0d", "footer-head": LIME},
        **{"pagehead-bg": "#f3f8ef", "pagehead-ink": INK, "pagehead-ink-2": "#3b4634"},
        **{"callbar-call": INK, "callbar-call-ink": "#ffffff"},
        **{"f-display": "'Barlow', sans-serif", "f-body": "'Barlow', sans-serif"},
        **{"display-weight": "700", "display-tracking": "-0.02em", "display-leading": "1.02"},
        **{"radius-btn": "4px", "radius-img": "8px", "radius-lg": "12px", "radius-input": "6px"},
        joint=SPROUTS, **{"joint-h": "26px", "joint-size": "48px 26px"},
        **{"btn-case": "uppercase", "btn-tracking": ".04em"},
    ),
    "topbar": [("medal", "Voted Best of Gwinnett 2025"), ("users", "Residential &amp; commercial")],
    "hero": {
        "variant": "overlay",
        "script": "Beautiful. Reliable. Local.",
        "title": "Landscaping for homes &amp; businesses in <span class=\"hl\">Lawrenceville &amp; Metro Atlanta</span>",
        "sub": "ITM Landscape designs and maintains functional outdoor environments for residential and commercial properties across Greater Atlanta.",
        "second": ("Commercial services", "services.html#commercial"),
        "photo_label": "stone water feature and plantings", "photo_kind": "garden",
        "proof": ["<b>Voted Best of Gwinnett 2025</b>", "Family owned &middot; <b>Lawrenceville</b> &amp; <b>Alpharetta</b>"],
    },
    "trust": [
        ("medal", "Best of Gwinnett 2025", "Voted by Gwinnett Magazine readers"),
        ("home", "Residential", "Lawn care and landscape projects"),
        ("users", "Commercial", "Properties across Greater Atlanta"),
        ("leaf", "Family run", "Led by Eric and Tori Soles"),
    ],
    "services_head": {"title": "Everything your property needs", "text": "Weekly lawn maintenance, new installation projects and commercial grounds care, from one local team."},
    "services_style": "tiles", "big_tiles": (0,),
    "services": [
        {"id": "lawn", "name": "Lawn maintenance", "img": "lawn.jpg", "kind": "garden",
         "blurb": "Reliable, scheduled care that keeps your lawn sharp.",
         "intro": "Dependable weekly and seasonal lawn care for homes across Gwinnett and North Fulton.",
         "bullets": ["Mowing, edging and blowing", "Fertilization and weed control", "Shrub trimming", "Seasonal cleanups and leaf removal"]},
        {"id": "installation", "name": "Installation projects", "img": "installation.jpg", "kind": "garden",
         "blurb": "Landscape design and installation, start to finish.",
         "intro": "New beds, plantings, sod and complete landscape makeovers, designed for function and beauty.",
         "bullets": ["Landscape design", "Planting and bed installation", "Sod installation", "Mulch and pine straw"]},
        {"id": "hardscape", "name": "Hardscaping &amp; retaining walls", "img": "hardscape.jpg", "kind": "pavers",
         "blurb": "Patios, walkways and walls that last.",
         "intro": "Patios, walkways and retaining walls built on a solid base.",
         "bullets": ["Paver patios", "Walkways", "Retaining walls", "Steps and borders"]},
        {"id": "outdoor-living", "name": "Outdoor kitchens &amp; living", "img": "outdoor-living.jpg", "kind": "stone",
         "blurb": "Kitchens, fire features and gathering spaces.",
         "intro": "Outdoor kitchens and gathering spaces that extend your living area.",
         "bullets": ["Outdoor kitchens", "Fire pits", "Seating areas", "Outdoor lighting"]},
        {"id": "drainage", "name": "Drainage, irrigation &amp; lighting", "img": "drainage.jpg", "kind": "garden",
         "blurb": "Water and light, managed right.",
         "intro": "Drainage that protects the property, irrigation that keeps it green and lighting that shows it off.",
         "bullets": ["Drainage solutions", "Irrigation installation and repair", "Landscape lighting", "Tree care"]},
        {"id": "commercial", "name": "Commercial", "img": "commercial.jpg", "kind": "garden",
         "blurb": "Grounds care for businesses and communities.",
         "intro": "Professional, reliable grounds maintenance and landscape projects for commercial properties across Greater Atlanta.",
         "bullets": ["Commercial grounds maintenance", "Entrance and common-area landscapes", "Seasonal color", "Installation projects"]},
    ],
    "home_order": ["feature", "statement", "process", "area"],
    "feature": {
        "title": "A local family business", "img": "feature.jpg", "photo_label": "Eric and Tori Soles", "kind": "garden",
        "body": ["ITM Landscape is run by Eric and Tori Soles, with roots that go back to Eric&rsquo;s father, Eddie. We live and work here, and we take care of every property like it&rsquo;s in our own neighborhood.",
                 "Gwinnett Magazine readers voted us Best of Gwinnett 2025."],
        "checks": ["Voted Best of Gwinnett 2025", "Residential and commercial", "Offices in Lawrenceville and Alpharetta"],
        "link": ("Meet our team", "about.html"), "cls": "alt",
    },
    "statement": {"cls": "dark", "text": "Beautiful. Reliable. <em>Local.</em>",
                  "sub": "Three words we work by on every property, every week."},
    "process": {"title": "Getting started is easy", "text": "From the first call to a property you&rsquo;re proud of.", "steps": [
        ("Call or request a quote", "Tell us about your property and what it needs."),
        ("Property visit", "We walk it with you and put together a plan."),
        ("Get to work", "Our crews install, maintain or both."),
        ("Stay beautiful", "Reliable ongoing care, season after season."),
    ]},
    "reviews": {"title": "", "big": "", "label": "", "town": "Lawrenceville"},
    "area": {"title": "Service areas", "towns": ["Lawrenceville", "Alpharetta", "Johns Creek", "Duluth", "Suwanee", "Snellville", "Grayson", "Dacula"]},
    "band": {"title": "Let&rsquo;s bring your landscaping vision to life today!", "text": "Get a quote for lawn maintenance, a landscape project or commercial grounds care.", "btn_cls": "btn--dark"},
    "work_cats": {"installation": "Installation", "hardscape": "Hardscape", "lawn": "Lawn care", "commercial": "Commercial"},
    "work": [
        ("installation", "Water feature &amp; plantings", "Lawrenceville", "wide", "garden"),
        ("hardscape", "Paver patio", "Gwinnett County", "", "pavers"),
        ("lawn", "Weekly lawn care", "Lawrenceville", "", "garden"),
        ("installation", "Front yard makeover", "Alpharetta", "", "garden"),
        ("hardscape", "Retaining wall", "Gwinnett County", "", "stone"),
        ("commercial", "Commercial entrance", "Greater Atlanta", "", "garden"),
        ("installation", "Backyard landscape", "Johns Creek", "wide", "garden"),
        ("hardscape", "Outdoor kitchen", "Gwinnett County", "", "stone"),
        ("lawn", "Sod installation", "Lawrenceville", "", "garden"),
        ("commercial", "Office park grounds", "Greater Atlanta", "", "garden"),
    ],
    "pages": {
        "services": {"title": "Our services", "lede": "Lawn maintenance, installation projects, hardscaping, outdoor living, drainage, irrigation, lighting and commercial grounds care."},
        "work": {"title": "Installation projects", "lede": "Landscapes and outdoor spaces we&rsquo;ve built across Gwinnett and Greater Atlanta."},
        "about": {"title": "About ITM Landscape", "lede": "A family-run landscape company serving homes and businesses from Lawrenceville and Alpharetta.",
                  "story": {"title": "Rooted in family", "img": "about.jpg", "photo_label": "the ITM Landscape team", "kind": "garden",
                            "body": ["ITM Landscape is led by Eric and Tori Soles. Eric&rsquo;s father, Eddie, is part of our story too, and that family approach runs through everything we do.",
                                     "Today we design and maintain functional outdoor environments for residential and commercial properties across Greater Atlanta, and we were voted Best of Gwinnett 2025."],
                            "checks": [], "link": ("Get a quote", "contact.html")},
                  "values_title": "Beautiful. Reliable. Local.", "values_cls": "dark",
                  "values": [("Beautiful", "Landscapes designed to make your property look its best."),
                             ("Reliable", "Crews that show up on schedule, week after week."),
                             ("Local", "A Gwinnett family business that knows this area.")]},
        "contact": {"title": "Get a quote", "lede": "Tell us about your home or business. We&rsquo;ll call to set up a visit.",
                    "chips": ["Lawn maintenance", "Landscape installation", "Hardscaping", "Outdoor kitchen", "Drainage or irrigation", "Lighting", "Commercial property"],
                    "submit": "Request my quote", "done": "We&rsquo;ll call you to talk about your property."},
    },
    "meta": {
        "home": ("ITM Landscape | Landscaping in Lawrenceville & Metro Atlanta", "Voted Best of Gwinnett 2025. Lawn maintenance, landscape installation and commercial grounds care. Call 678-773-0380."),
        "services": ("Services | ITM Landscape", "Lawn maintenance, installation projects, hardscaping, drainage, irrigation and commercial services."),
        "work": ("Projects | ITM Landscape", "Landscape installation projects by ITM Landscape."),
        "about": ("About | ITM Landscape", "Family-run landscape company in Lawrenceville, GA. Voted Best of Gwinnett 2025."),
        "contact": ("Get a Quote | ITM Landscape", "Get a landscaping quote. Call 678-773-0380."),
    },
}

if __name__ == "__main__":
    build(CONFIG, Path(__file__).parent)
    write_readme(CONFIG, Path(__file__).parent, [
        "Their site has a Bill Pay page. Link it in the menu once we have the payment URL.",
        "Their Alpharetta office address isn't listed. Add it if they want both locations shown.",
        "The 'Family run' wording comes from Eric, Tori and Eddie Soles being named on their site. Confirm they're happy with it.",
        "Towns under 'Service areas' are assumed. Confirm.",
    ])
