"""The Rick's Group demo. Edit text below, then run: python3 site.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_engine"))
from engine import build, theme, svg_uri, stars, write_readme, ph_pavers, ph_garden  # noqa: E402

NAVY, LIME, BLUE = "#091830", "#7fba24", "#5e7bac"
PAVERS = svg_uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="64" height="24"><rect width="64" height="24" fill="{NAVY}"/><rect x="2" y="2" width="28" height="9" rx="2" fill="{LIME}"/><rect x="34" y="2" width="28" height="9" rx="2" fill="#6a9f1c"/><rect x="-14" y="13" width="28" height="9" rx="2" fill="#6a9f1c"/><rect x="18" y="13" width="28" height="9" rx="2" fill="{BLUE}"/><rect x="50" y="13" width="28" height="9" rx="2" fill="{LIME}"/></svg>')
MARK = ('<svg class="logo-mark" viewBox="0 0 48 48" aria-hidden="true">'
        f'<path d="M24 6c5 7 5 15 0 22-5-7-5-15 0-22Z" fill="{LIME}"/>'
        f'<path d="M24 28c-2-8-8-13-17-14 1 9 7 14 17 14Z" fill="{LIME}"/><path d="M24 28c2-8 8-13 17-14-1 9-7 14-17 14Z" fill="{LIME}"/>'
        f'<path d="M24 28c-6-1-12 1-18 6 7 3 13 2 18-6Zm0 0c6-1 12 1 18 6-7 3-13 2-18-6Z" fill="#6a9f1c"/><path d="M24 28v14" stroke="{LIME}" stroke-width="2"/></svg>')

CONFIG = {
    "name": "The Rick's Group",
    "logo": {"name": "The Rick&rsquo;s Group", "sub": "Landscape Management", "mark": MARK},
    "phone": "(678) 451-6465", "tel": "+16784516465",
    "email": "info@thericksgroupga.com",
    "address": "Buford, GA 30518",
    "hours": "Mon&ndash;Fri, 8:00 AM to 4:00 PM",
    "cta": "Get a free quote",
    "theme_color": NAVY,
    "footer_blurb": "Hardscaping and landscaping for homes, businesses, multi-family communities and HOAs across north Metro Atlanta.",
    "footer_right": "Buford, Georgia",
    "fonts_url": "https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,400;0,500;0,700;0,800;1,400&family=Gelasio:wght@600&display=swap",
    "theme_css": theme(
        f"""
.site-header .logo b {{ font-family: 'Gelasio', serif; font-weight: 600; font-size: 1.55rem; color: {BLUE}; letter-spacing: 0; }}
.site-header .logo span {{ color: {LIME}; opacity: 1; letter-spacing: .22em; font-size: .68rem; }}
.site-footer .logo b {{ font-family: 'Gelasio', serif; font-weight: 600; font-size: 1.4rem; }}
.site-header .logo b {{ color: #b9c8e4; }}
.hero--panel h1 {{ color: {NAVY}; font-size: clamp(2.5rem, 1.5rem + 4vw, 4.6rem); }}
.hero--panel h1 .hl {{ color: #4f7a12; display: block; font-size: .62em; letter-spacing: .02em; margin-top: .3em; text-transform: uppercase; }}
.row:hover :is(h3, p, .arrow) {{ color: {NAVY}; }}
.trust svg {{ color: {LIME}; }}
.section.dark .statement em {{ color: {LIME}; }}
""",
        bg="#ffffff", **{"bg-2": "#f2f5f9"}, ink=NAVY, **{"ink-2": "#2c3a52"}, muted="#56637a",
        **{"line": "rgba(9,24,48,.1)", "line-strong": "rgba(9,24,48,.2)"},
        accent=LIME, **{"accent-hi": "#8fcc31", "accent-ink": NAVY, "accent-text": "#4f7a12", "accent-on-dark": LIME},
        **{"topbar-bg": "#050e1d", "accent-2": "#4f6c9e", "accent-2-hi": BLUE, "accent-2-ink": "#ffffff"},
        focus=BLUE, **{"focus-ring": "rgba(94,123,172,.3)"}, star="#f2b01e",
        dark=NAVY, **{"dark-ink": "#ffffff", "dark-ink-2": "#c3cde0"},
        **{"header-bg": NAVY, "header-ink": "#ffffff", "nav-current": LIME},
        **{"panel-bg": "rgba(242,246,250,.9)", "panel-ink": NAVY, "panel-ink-2": "#2c3a52"},
        **{"trust-bg": "#0f2244", "trust-ink": "#ffffff", "trust-line": "rgba(255,255,255,.12)"},
        **{"band-bg": NAVY, "band-ink": "#ffffff", "band-ink-2": "#c3cde0", "on-light-accent": NAVY},
        **{"footer-bg": "#060f1f", "footer-head": LIME},
        **{"pagehead-bg": NAVY, "pagehead-ink": "#ffffff", "pagehead-ink-2": "#c3cde0"},
        **{"callbar-call": NAVY, "callbar-call-ink": "#ffffff"},
        **{"f-display": "'Fira Sans', sans-serif", "f-body": "'Fira Sans', sans-serif"},
        **{"display-weight": "700", "display-tracking": "-0.015em", "display-leading": "1.05"},
        **{"radius-btn": "999px", "radius-img": "18px", "radius-lg": "22px", "radius-input": "12px"},
        joint=PAVERS, **{"joint-h": "24px", "joint-size": "64px 24px"},
    ),
    "topbar": [("clock", "Mon&ndash;Fri 8&ndash;4"), ("medal", "Techo-Bloc Certified Installer"), ("dollar", "Financing available")],
    "ph": {"pavers": lambda: ph_pavers(8, ["#a7a49c", "#8f8c86", "#b9b5ac", "#7c7a76", "#9d998f"], "#4a4844"),
           "garden": lambda: ph_garden(4, ["#8cbc4a", "#6e9e33", "#557f27", "#3f631d"], "#d7e3ef")},
    "hero": {
        "variant": "panel",
        "title": "The Rick&rsquo;s Group <span class=\"hl\">Landscape Management</span>",
        "sub": "Discover the art of outdoor transformation. We design, build and maintain hardscapes and landscapes for homes, businesses, multi-family communities and HOAs across north Metro Atlanta.",
        "second": ("Financing available", "contact.html"), "second_cls": "btn--alt",
        "photo_label": "paver patio and landscaped yard", "photo_kind": "garden",
        "proof": [f"{stars()} <b>90+</b> five-star Google reviews", "<b>Techo-Bloc</b> Certified Installer"],
    },
    "trust": [
        ("medal", "Techo-Bloc Certified", "Installer of premium pavers and walls"),
        ("star", "90+ Google reviews", "Top-rated in north Metro Atlanta"),
        ("dollar", "Financing available", "Build now, pay over time"),
        ("users", "Homes to HOAs", "Residential, commercial, multi-family"),
    ],
    "services_head": {"title": "Hardscape. Landscape. Done right.", "text": "From a new paver patio to a retaining wall that finally fixes the slope, to keeping the whole property looking sharp all year."},
    "services_style": "rows",
    "services": [
        {"id": "hardscaping", "name": "Hardscaping", "img": "hardscaping.jpg", "kind": "pavers",
         "blurb": "Paver patios, walkways and driveways, installed to Techo-Bloc standards.",
         "intro": "As a Techo-Bloc Certified Installer, we build paver patios, walkways and outdoor rooms that stay level and look great for decades.",
         "bullets": ["Paver patios and walkways", "Driveways", "Steps and seat walls", "Techo-Bloc certified installation"]},
        {"id": "landscaping", "name": "Landscaping", "img": "landscaping.jpg", "kind": "garden",
         "blurb": "Landscape design and installation for curb appeal that lasts.",
         "intro": "Thoughtful plantings, clean beds and a design that suits your property, installed by our own crews.",
         "bullets": ["Landscape design", "Planting and bed installation", "Sod and seeding", "Mulch and pine straw"]},
        {"id": "retaining-walls", "name": "Retaining walls", "img": "walls.jpg", "kind": "pavers",
         "blurb": "Engineered walls that hold the hill and add usable space.",
         "intro": "A retaining wall turns a slope into usable yard. We build them on a proper base, with drainage behind them, so they stay put.",
         "bullets": ["Segmental block walls", "Natural stone walls", "Terraced gardens", "Wall caps and lighting"]},
        {"id": "drainage", "name": "Drainage solutions", "img": "drainage.jpg", "kind": "garden",
         "blurb": "Stop standing water and protect your foundation.",
         "intro": "Georgia storms find every low spot. We find where the water goes and give it somewhere better to go.",
         "bullets": ["French drains", "Downspout and gutter drains", "Grading", "Erosion control"]},
        {"id": "outdoor-living", "name": "Outdoor living", "img": "outdoor-living.jpg", "kind": "pavers",
         "blurb": "Outdoor kitchens, fire features and pergolas.",
         "intro": "Turn the patio into a place to cook, gather and stay out past dark.",
         "bullets": ["Outdoor kitchens", "Fire pits and fire features", "Pergolas", "Landscape lighting"]},
        {"id": "management", "name": "Landscape management", "img": "management.jpg", "kind": "garden",
         "blurb": "Ongoing care for homes, businesses, multi-family and HOAs.",
         "intro": "Reliable, scheduled care that keeps a property looking its best, from single homes to whole communities.",
         "bullets": ["Mowing and edging", "Seasonal cleanups", "Shrub and tree care", "Commercial, multi-family and HOA contracts"]},
    ],
    "home_order": ["feature", "statement", "process", "reviews", "area"],
    "feature": {
        "title": "Built by a certified installer", "img": "feature.jpg", "photo_label": "Techo-Bloc paver installation", "kind": "pavers",
        "body": ["Techo-Bloc only certifies installers who meet its standards for base preparation, compaction and finish. That&rsquo;s the standard we hold on every project, whatever brand you choose.",
                 "We also hold a Georgia Blue Card, so your project is handled with care for the water around it."],
        "checks": ["Techo-Bloc Certified Installer", "Georgia Blue Card holder", "Financing available on qualifying projects"],
        "link": ("About The Rick&rsquo;s Group", "about.html"),
    },
    "statement": {"cls": "dark", "text": "Top-rated on Google with <em>over 90 five-star reviews.</em>",
                  "sub": "Homeowners, property managers and HOA boards across north Metro Atlanta trust us with their properties."},
    "process": {"title": "From first call to finished yard", "text": "A clear plan, a fair quote and a crew that shows up.", "steps": [
        ("Free quote", "We visit, listen and look at the property, including slope and drainage."),
        ("Design", "You get a plan and a written quote. Ask about financing."),
        ("Build", "Our crews install it to certified-installer standards."),
        ("Care", "Keep it looking new with ongoing landscape management."),
    ], "cls": "alt"},
    "reviews": {"title": "What clients say", "big": "90+", "label": "Five-star Google reviews", "town": "North Metro Atlanta"},
    "area": {"title": "Serving north Metro Atlanta", "towns": ["Buford", "Sugar Hill", "Suwanee", "Duluth", "Lawrenceville", "Dacula", "Cumming", "Flowery Branch"]},
    "band": {"title": "Ready to transform your property?", "text": "Get a free quote today. Financing is available on qualifying projects.", "btn_cls": ""},
    "work_cats": {"hardscape": "Hardscape", "walls": "Retaining walls", "landscape": "Landscape", "living": "Outdoor living"},
    "work": [
        ("hardscape", "Paver patio &amp; walkway", "North Metro Atlanta", "wide", "pavers"),
        ("walls", "Terraced retaining wall", "North Metro Atlanta", "", "pavers"),
        ("landscape", "Front yard landscape", "North Metro Atlanta", "", "garden"),
        ("living", "Fire pit patio", "North Metro Atlanta", "", "pavers"),
        ("landscape", "HOA entrance planting", "North Metro Atlanta", "", "garden"),
        ("hardscape", "Paver driveway", "North Metro Atlanta", "", "pavers"),
        ("walls", "Block retaining wall", "North Metro Atlanta", "wide", "pavers"),
        ("living", "Outdoor kitchen", "North Metro Atlanta", "", "stone"),
        ("landscape", "Drainage &amp; regrade", "North Metro Atlanta", "", "garden"),
        ("hardscape", "Pool deck pavers", "North Metro Atlanta", "", "pavers"),
    ],
    "pages": {
        "services": {"title": "Our services", "lede": "Hardscaping, landscaping, retaining walls, drainage and ongoing landscape management for north Metro Atlanta."},
        "work": {"title": "Our work", "lede": "Hardscapes and landscapes we&rsquo;ve built for homes and communities across north Metro Atlanta."},
        "about": {"title": "About The Rick&rsquo;s Group", "lede": "A trusted north Metro Atlanta hardscaping and landscaping company serving north Georgia.",
                  "story": {"title": "The art of outdoor transformation", "img": "about.jpg", "photo_label": "our crew on site", "kind": "garden",
                            "body": ["With years of experience and countless satisfied clients, we specialize in hardscaping and landscaping for residential, commercial, multi-family developments and HOAs.",
                                     "We&rsquo;re a Techo-Bloc Certified Installer and Georgia Blue Card holder, and we&rsquo;re top-rated on Google with over 90 five-star reviews."],
                            "checks": [], "link": ("Get a free quote", "contact.html")},
                  "values_title": "How we work", "values_cls": "dark",
                  "values": [("Certified quality", "We install to Techo-Bloc certified-installer standards on every project."),
                             ("Clear quotes", "Written quotes with no surprises, and financing when you need it."),
                             ("Here for the long run", "We build it, then we can keep it looking great with ongoing care.")]},
        "contact": {"title": "Get a free quote", "lede": "Tell us about your property and we&rsquo;ll be in touch. Office hours are Monday to Friday, 8 to 4.",
                    "chips": ["Hardscaping", "Landscaping", "Retaining wall", "Drainage", "Outdoor living", "Landscape management", "Financing info"],
                    "submit": "Request my free quote", "done": "We&rsquo;ll call you during office hours to talk about your project."},
    },
    "meta": {
        "home": ("The Rick's Group | Hardscaping & Landscaping in North Metro Atlanta", "Techo-Bloc Certified hardscaping and landscaping for homes, businesses and HOAs in north Metro Atlanta. Financing available."),
        "services": ("Services | The Rick's Group", "Hardscaping, landscaping, retaining walls, drainage and landscape management."),
        "work": ("Our Work | The Rick's Group", "Hardscape and landscape projects across north Metro Atlanta."),
        "about": ("About | The Rick's Group", "Trusted north Metro Atlanta hardscaping and landscaping company."),
        "contact": ("Free Quote | The Rick's Group", "Get a free quote. Call (678) 451-6465."),
    },
}

if __name__ == "__main__":
    build(CONFIG, Path(__file__).parent)
    write_readme(CONFIG, Path(__file__).parent, [
        "Address is Buford, GA 30518 only (no street address found).",
        "Towns under 'Serving north Metro Atlanta' are assumed. Confirm the service area.",
        "Service bullet points are typical scope. Confirm each one.",
    ])
