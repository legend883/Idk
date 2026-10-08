"""RC Pro Solutions demo. Edit text below, then run: python3 site.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_engine"))
from engine import build, theme, svg_uri, stars, write_readme  # noqa: E402

INK, CHAR, STONE = "#111315", "#1d2124", "#e9e5de"
LINE = svg_uri('<svg xmlns="http://www.w3.org/2000/svg" width="200" height="14"><rect width="200" height="14" fill="#ffffff"/><rect y="6" width="200" height="1.5" fill="#111315"/><rect x="96" y="2" width="8" height="8" transform="rotate(45 100 6)" fill="#111315"/></svg>')
MARK = ('<svg class="logo-mark" viewBox="0 0 48 48" aria-hidden="true">'
        '<path d="M5 22 24 8l19 14" fill="none" stroke="currentColor" stroke-width="3"/>'
        '<text x="24" y="40" text-anchor="middle" font-family="Playfair Display, serif" font-weight="700" font-size="17" fill="currentColor">RC</text></svg>')

CONFIG = {
    "name": "RC Pro Solutions",
    "logo": {"name": "RCPro <i>Solutions</i>", "sub": "Residential &amp; Commercial", "mark": MARK},
    "phone": "(678) 559-9990", "tel": "+16785599990",
    "address": "Kennesaw, GA 30144",
    "hours": "Mon&ndash;Sat, 8:00 AM to 5:00 PM",
    "cta": "Free quote",
    "theme_color": INK,
    "footer_blurb": "Exceptional hardscape and landscaping services for residential and commercial properties across Kennesaw and northwest Metro Atlanta.",
    "footer_right": "RC Pro Contracting Inc. &middot; Kennesaw, Georgia",
    "fonts_url": "https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=Montserrat:wght@400;500;600;700&display=swap",
    "theme_css": theme(
        """
.logo b { font-family: 'Playfair Display', serif; font-weight: 700; font-size: 1.5rem; letter-spacing: -0.01em; }
.logo b i { font-family: 'Montserrat', sans-serif; font-style: normal; font-weight: 500; font-size: .62rem; letter-spacing: .38em; text-transform: uppercase; display: block; margin-top: .25rem; }
.site-header .logo .lt > span { font-size: .62rem; letter-spacing: .08em; text-transform: none; }
.nav a:not(.btn) { text-transform: uppercase; letter-spacing: .08em; font-size: .82rem; font-weight: 600; }
.hero--overlay { text-align: center; }
.hero--overlay .wrap { display: flex; flex-direction: column; align-items: center; }
.hero--overlay .accent-bar { display: none; }
.hero--overlay .kick-script { font-family: 'Montserrat', sans-serif; font-size: clamp(.9rem, .8rem + .4vw, 1.15rem); letter-spacing: .6em; text-transform: uppercase; color: #fff; margin-bottom: 1.4rem; }
.hero--overlay h1 { max-width: 16ch; font-size: clamp(2.8rem, 1.4rem + 5.4vw, 6rem); }
.hero--overlay h1 .hl { color: #fff; font-style: italic; }
.hero--overlay h1::after { content: ""; display: block; width: min(60vw, 520px); height: 2px; background: #fff; margin: 2rem auto 0; }
.hero--overlay .sub { margin-inline: auto; }
.hero--overlay .actions, .hero--overlay .proof { justify-content: center; }
.btn { text-transform: uppercase; letter-spacing: .14em; font-size: .82rem; font-weight: 600; }
.statement { font-style: italic; }
.hero--overlay .btn:not(.btn--alt), .site-header .nav .btn { --bg-btn: #ffffff; color: #111315; }
.hero--overlay .btn:not(.btn--alt):hover, .site-header .nav .btn:hover { --bg-btn: #e9e5de; }
.hero--overlay .btn--alt { --bg-btn: transparent; color: #fff; box-shadow: inset 0 0 0 1.5px #fff; }
.hero--overlay .btn--alt:hover { --bg-btn: rgba(255,255,255,.1); }
@media (max-width: 720px) { .callbar a:last-child { background: #ffffff; color: #111315; } }
.process .step { font-style: italic; }
""",
        bg="#ffffff", **{"bg-2": "#f4f2ee"}, ink=INK, **{"ink-2": "#3d4145"}, muted="#62676c",
        accent=INK, **{"accent-hi": "#2a2f33", "accent-ink": "#ffffff", "accent-text": INK, "accent-on-dark": "#ffffff"},
        **{"accent-2": "#ffffff", "accent-2-hi": STONE, "accent-2-ink": INK},
        focus=INK, **{"focus-ring": "rgba(17,19,21,.2)"}, star="#c9a24a",
        dark=CHAR, **{"dark-ink": "#ffffff", "dark-ink-2": "#c9cbcd"},
        **{"topbar-bg": INK, "topbar-ink": "#ffffff", "header-bg": INK, "header-ink": "#ffffff"},
        scrim="rgba(10,11,12,.9)",
        **{"trust-bg": CHAR, "trust-ink": "#ffffff", "trust-line": "rgba(255,255,255,.12)", "trust-icon": STONE},
        **{"band-bg": INK, "band-ink": "#ffffff", "band-ink-2": "#c9cbcd", "on-light-accent": INK},
        **{"footer-bg": "#0a0b0c", "footer-head": STONE},
        **{"pagehead-bg": CHAR, "pagehead-ink": "#ffffff", "pagehead-ink-2": "#c9cbcd"},
        **{"callbar-call": "#2a2f33", "callbar-call-ink": "#ffffff"},
        **{"f-display": "'Playfair Display', serif", "f-body": "'Montserrat', sans-serif"},
        **{"display-weight": "500", "display-tracking": "-0.01em", "display-leading": "1.06"},
        **{"radius-btn": "0px", "radius-img": "0px", "radius-lg": "0px", "radius-input": "0px"},
        joint=LINE, **{"joint-h": "14px", "joint-size": "200px 14px"},
    ),
    "topbar": [("clock", "Mon&ndash;Sat 8&ndash;5"), ("dollar", "Financing available"), ("users", "Residential &amp; commercial")],
    "hero": {
        "variant": "overlay",
        "script": "Exceptional",
        "title": "Hardscape &amp; <span class=\"hl\">Landscaping</span> Services",
        "sub": "We&rsquo;ll turn your property into the beautiful oasis you envision with our hardscaping and landscaping services.",
        "second": ("Financing your project", "contact.html"), "second_cls": "btn--alt",
        "photo_label": "paver patio and seat walls at dusk", "photo_kind": "pavers",
        "proof": ["<b>20+ years</b> of experience", "<b>Financing</b> available"],
    },
    "trust": [
        ("medal", "20+ years", "Of hardscape and landscape experience"),
        ("dollar", "Financing", "Available for your project"),
        ("users", "Residential &amp; commercial", "Homes and businesses"),
        ("clock", "Open six days", "Mon&ndash;Sat, 8 to 5"),
    ],
    "services_head": {"title": "Exceptional outdoor spaces", "text": "Hardscaping, outdoor living, decks and landscaping, designed and built by one experienced team."},
    "services_style": "rows",
    "services": [
        {"id": "hardscaping", "name": "Hardscaping", "img": "hardscaping.jpg", "kind": "pavers",
         "blurb": "Paver patios, walkways, seat walls and retaining walls.",
         "intro": "The foundation of an exceptional outdoor space. We build paver patios, walkways and walls on a properly prepared base so they last.",
         "bullets": ["Paver patios and walkways", "Seat walls and pillars", "Retaining walls", "Steps and borders"]},
        {"id": "outdoor-living", "name": "Outdoor living", "img": "outdoor-living.jpg", "kind": "stone",
         "blurb": "Outdoor kitchens, fire pits and gathering spaces.",
         "intro": "Turn your patio into a place to cook, gather and relax, with outdoor kitchens and fire features built to match.",
         "bullets": ["Outdoor kitchens", "Fire pits and fireplaces", "Pergolas", "Landscape lighting"]},
        {"id": "decks", "name": "Decks", "img": "deck.jpg", "kind": "composite",
         "blurb": "Wood and composite decks, built solid.",
         "intro": "Decks that connect your home to the yard, framed right and finished clean.",
         "bullets": ["Wood decks", "Composite decks", "Stairs and railings", "Deck-to-patio designs"]},
        {"id": "landscaping", "name": "Landscaping", "img": "landscaping.jpg", "kind": "garden",
         "blurb": "Landscape design, planting and sprinkler systems.",
         "intro": "Landscapes that frame the hardscape and complete the property.",
         "bullets": ["Landscape design", "Planting and beds", "Sod installation", "Sprinkler systems"]},
        {"id": "commercial", "name": "Commercial", "img": "commercial.jpg", "kind": "pavers",
         "blurb": "Hardscape and landscape for businesses.",
         "intro": "Professional hardscape and landscape work for commercial properties.",
         "bullets": ["Commercial hardscapes", "Entrances and walkways", "Retaining walls", "Landscape installation"]},
    ],
    "home_order": ["feature", "statement", "process", "area"],
    "feature": {
        "title": "Two decades of <i>exceptional</i> work", "img": "feature.jpg", "photo_label": "paver patio with fire pit", "kind": "pavers",
        "body": ["RC Pro Solutions brings more than 20 years of hardscape and landscape experience to every project, residential or commercial.",
                 "And with financing available, your project doesn&rsquo;t have to wait."],
        "checks": ["20+ years of experience", "Financing available", "Open Monday through Saturday"],
        "link": ("About RC Pro", "about.html"), "cls": "alt",
    },
    "statement": {"cls": "dark", "text": "The beautiful oasis you envision, <em>built to last.</em>",
                  "sub": "Ask about financing your project."},
    "process": {"title": "Our process", "text": "Clear from the first quote to the final walkthrough.", "steps": [
        ("Free quote", "We visit the property and listen to what you want."),
        ("Design", "A plan and a clear price, with financing options."),
        ("Build", "Our experienced crew builds it right."),
        ("Walkthrough", "We review every detail with you before we finish."),
    ]},
    "reviews": {"title": "", "big": "", "label": "", "town": "Kennesaw"},
    "area": {"title": "Service areas", "towns": ["Kennesaw", "Marietta", "Acworth", "Woodstock", "Powder Springs", "Dallas", "Canton", "Smyrna"]},
    "band": {"title": "Ready for an exceptional outdoor space?", "text": "Get a free quote. Financing available.", "btn_cls": "btn--light"},
    "work_cats": {"hardscape": "Hardscape", "living": "Outdoor living", "decks": "Decks", "landscape": "Landscape"},
    "work": [
        ("hardscape", "Paver patio &amp; seat walls", "Kennesaw", "wide", "pavers"),
        ("living", "Outdoor kitchen", "Northwest Metro Atlanta", "", "stone"),
        ("decks", "Composite deck", "Northwest Metro Atlanta", "", "composite"),
        ("landscape", "Front yard landscape", "Northwest Metro Atlanta", "", "garden"),
        ("hardscape", "Retaining wall", "Northwest Metro Atlanta", "", "stone"),
        ("living", "Fire pit patio", "Northwest Metro Atlanta", "", "pavers"),
        ("hardscape", "Paver walkway", "Northwest Metro Atlanta", "wide", "pavers"),
        ("decks", "Wood deck &amp; stairs", "Northwest Metro Atlanta", "", "deck"),
        ("landscape", "Sprinkler &amp; sod", "Northwest Metro Atlanta", "", "garden"),
        ("living", "Pergola &amp; lighting", "Northwest Metro Atlanta", "", "deck"),
    ],
    "pages": {
        "services": {"title": "Our services", "lede": "Hardscaping, outdoor living, decks, landscaping and commercial work across Kennesaw and northwest Metro Atlanta."},
        "work": {"title": "Gallery", "lede": "Hardscapes, outdoor living spaces and landscapes we&rsquo;ve built."},
        "about": {"title": "About RC Pro Solutions", "lede": "Exceptional hardscape and landscaping services for residential and commercial properties.",
                  "story": {"title": "Built on experience", "img": "about.jpg", "photo_label": "RC Pro crew on site", "kind": "pavers",
                            "body": ["Owner Robert has more than 20 years of experience in hardscaping and landscaping. RC Pro Solutions (RC Pro Contracting Inc.) was built on that experience and a simple goal: turn every property into the oasis its owner envisions.",
                                     "We serve homeowners and businesses across Kennesaw and northwest Metro Atlanta, and we offer financing so great projects don&rsquo;t have to wait."],
                            "checks": [], "link": ("Get a free quote", "contact.html")},
                  "values_title": "Our standards", "values_cls": "dark",
                  "values": [("Experience", "More than two decades of hardscape and landscape work."),
                             ("Quality", "Proper bases, clean lines and details done right."),
                             ("Flexibility", "Financing options and service six days a week.")]},
        "contact": {"title": "Get a free quote", "lede": "Tell us about your project. Ask about financing.",
                    "chips": ["Hardscaping", "Outdoor living", "Deck", "Landscaping", "Sprinkler system", "Commercial", "Financing info"],
                    "submit": "Request my free quote", "done": "We&rsquo;ll call you to talk through your project."},
    },
    "meta": {
        "home": ("RC Pro Solutions | Hardscape & Landscaping in Kennesaw, GA", "Exceptional hardscape and landscaping services for homes and businesses. Financing available. Call (678) 559-9990."),
        "services": ("Services | RC Pro Solutions", "Hardscaping, outdoor living, decks, landscaping and commercial services."),
        "work": ("Gallery | RC Pro Solutions", "Hardscape and landscape projects by RC Pro Solutions."),
        "about": ("About | RC Pro Solutions", "20+ years of hardscape and landscape experience in Kennesaw, GA."),
        "contact": ("Free Quote | RC Pro Solutions", "Get a free quote. Call (678) 559-9990."),
    },
}

if __name__ == "__main__":
    build(CONFIG, Path(__file__).parent)
    write_readme(CONFIG, Path(__file__).parent, [
        "Their menu lists 'ACE Resin'. We left it off because we don't know what it covers. Add it once confirmed.",
        "No reviews section, because no review data was found. Add one if they have Google reviews.",
        "Owner first name 'Robert' and '20+ years' are from research. Confirm.",
        "Towns under 'Service areas' are assumed. Confirm.",
    ])
