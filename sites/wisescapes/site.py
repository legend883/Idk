"""Wisescapes demo. Edit text below, then run: python3 site.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_engine"))
from engine import build, theme, svg_uri, stars, write_readme  # noqa: E402

TEAL, TEAL_DK, CREAM, FOREST = "#2a717d", "#1c4f58", "#fbf9f5", "#3f5a2e"
CONTOUR = svg_uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="240" height="34"><path d="M0 8 C 40 0, 80 16, 120 8 S 200 0, 240 8" fill="none" stroke="{TEAL}" stroke-width="1.5"/><path d="M0 17 C 40 9, 80 25, 120 17 S 200 9, 240 17" fill="none" stroke="{TEAL}" stroke-opacity=".6" stroke-width="1.5"/><path d="M0 26 C 40 18, 80 34, 120 26 S 200 18, 240 26" fill="none" stroke="{TEAL}" stroke-opacity=".35" stroke-width="1.5"/></svg>')
MARK = ('<svg class="logo-mark" viewBox="0 0 48 48" aria-hidden="true">'
        f'<circle cx="24" cy="14" r="10" fill="{FOREST}"/><circle cx="15" cy="17" r="6.5" fill="#557a3c"/><circle cx="33" cy="17" r="6.5" fill="#557a3c"/>'
        f'<path d="M24 14v16" stroke="#4a3a2a" stroke-width="2.6"/><path d="M8 30h32" stroke="{TEAL}" stroke-width="1.6"/>'
        '<path d="M24 30c-2 5-6 8-11 10M24 30c2 5 6 8 11 10M24 30v12M24 33c-3 2-7 3-12 3M24 33c3 2 7 3 12 3" stroke="#4a3a2a" stroke-width="1.3" fill="none"/></svg>')

CONFIG = {
    "name": "Wisescapes",
    "logo": {"name": "Wisescapes", "sub": "Creative Outdoor Solutions", "mark": MARK},
    "phone": "770-672-1526", "tel": "+17706721526",
    "email": "jw@wisescapes.com",
    "address": "7175 Tributary Ct<br>Cumming, GA 30040",
    "cta": "Schedule a consultation",
    "theme_color": CREAM,
    "footer_blurb": "Creative outdoor solutions. Landscape design and outdoor living, crafted locally in Cumming and Forsyth County.",
    "footer_right": "Crafted locally in Cumming, Georgia",
    "fonts_url": "https://fonts.googleapis.com/css2?family=Gilda+Display&family=Mulish:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap",
    "theme_css": theme(
        f"""
.site-header .logo b {{ font-family: 'Gilda Display', serif; font-weight: 400; font-size: 1.6rem; color: {FOREST}; }}
.site-header .logo span {{ color: {TEAL}; letter-spacing: .14em; font-size: .64rem; }}
.site-footer .logo b {{ font-family: 'Gilda Display', serif; font-weight: 400; font-size: 1.5rem; }}
.nav a:not(.btn) {{ text-transform: uppercase; letter-spacing: .06em; font-size: .86rem; font-weight: 700; }}
.hero--overlay h1 {{ max-width: 16ch; font-size: clamp(2.8rem, 1.4rem + 5vw, 5.6rem); }}
.hero--overlay .hl {{ color: #bfe3e6; font-style: italic; }}
.hero--overlay .accent-bar {{ display: none; }}
.joint {{ background-color: {CREAM}; }}
.btn {{ text-transform: uppercase; letter-spacing: .06em; font-size: .92rem; }}
.statement em {{ font-style: italic; }}
""",
        bg=CREAM, **{"bg-2": "#eef3f1"}, ink="#1d2b2d", **{"ink-2": "#3a4a4c"}, muted="#5b6a6b", card="#ffffff",
        **{"line": "rgba(29,43,45,.1)", "line-strong": "rgba(29,43,45,.22)"},
        accent=TEAL, **{"accent-hi": "#338591", "accent-ink": "#ffffff", "accent-text": TEAL, "accent-on-dark": "#9fd3d8"},
        **{"accent-2": FOREST, "accent-2-hi": "#4b6b37", "accent-2-ink": "#ffffff"},
        focus=TEAL, **{"focus-ring": "rgba(42,113,125,.28)"}, star="#d9a521",
        dark=TEAL_DK, **{"dark-ink": "#ffffff", "dark-ink-2": "#cfe3e5"},
        **{"topbar-bg": "#f1eee7", "topbar-ink": "#1d2b2d", "header-bg": "#ffffff", "header-ink": "#1d2b2d", "nav-current": TEAL},
        **{"trust-bg": TEAL, "trust-ink": "#ffffff", "trust-line": "rgba(255,255,255,.2)", "trust-icon": "#ffffff"},
        **{"band-bg": TEAL_DK, "band-ink": "#ffffff", "band-ink-2": "#cfe3e5", "on-light-accent": TEAL_DK},
        **{"footer-bg": "#142f34", "footer-head": "#9fd3d8"},
        **{"pagehead-bg": "#eef3f1", "pagehead-ink": "#1d2b2d", "pagehead-ink-2": "#3a4a4c"},
        **{"callbar-call": FOREST, "callbar-call-ink": "#ffffff"},
        **{"f-display": "'Gilda Display', serif", "f-body": "'Mulish', sans-serif"},
        **{"display-weight": "400", "display-tracking": "-0.005em", "display-leading": "1.08"},
        **{"radius-btn": "2px", "radius-img": "0px", "radius-lg": "0px", "radius-input": "2px"},
        joint=CONTOUR, **{"joint-h": "34px", "joint-size": "240px 34px"},
    ),
    "topbar": [("chat", "Call or text today")],
    "hero": {
        "variant": "overlay",
        "title": "Dream outdoor spaces, <span class=\"hl\">crafted locally</span>",
        "sub": "Your landscape designer in Cumming, GA. Patios, fireplaces, outdoor kitchens and landscapes designed around how you want to live outside.",
        "second": ("View portfolio", "work.html"),
        "photo_label": "landscaped front yard and lawn", "photo_kind": "garden",
        "proof": ["Call or text <b>770-672-1526</b>", "Serving <b>Cumming &amp; Forsyth County</b>"],
    },
    "trust": [
        ("leaf", "Design-led", "Every project starts with a plan"),
        ("home", "Crafted locally", "Based right here in Cumming"),
        ("chat", "Call or text", "Reach us the way you like"),
        ("check", "Design to install", "One team, start to finish"),
    ],
    "services_head": {"title": "Creative outdoor solutions", "text": "Thoughtful design for the whole yard, from the patio and the fire to the plants, the light and the water that runs through it."},
    "services_style": "tiles", "big_tiles": (0,),
    "services": [
        {"id": "design", "name": "Landscape design", "img": "design.jpg", "kind": "garden",
         "blurb": "A plan for the whole yard, built around how you&rsquo;ll use it.",
         "intro": "Great landscapes start on paper. We design a plan that fits your property, your style and your budget, then bring it to life.",
         "bullets": ["Custom landscape plans", "Planting design", "Hardscape layout", "Phased plans you can build over time"]},
        {"id": "patios", "name": "Patios &amp; fireplaces", "img": "patio.jpg", "kind": "pavers",
         "blurb": "Stone patios with a fireplace or fire pit at the center.",
         "intro": "A patio is the room everything else in the yard revolves around. We design and build patios, outdoor fireplaces and fire pits that invite you to stay.",
         "bullets": ["Paver and natural stone patios", "Outdoor fireplaces", "Fire pits", "Seat walls"]},
        {"id": "kitchens", "name": "Outdoor kitchens", "img": "kitchen.jpg", "kind": "stone",
         "blurb": "Cook and entertain outside.",
         "intro": "An outdoor kitchen designed into the landscape, not dropped onto it.",
         "bullets": ["Grill islands", "Counters and bar seating", "Covered kitchen areas", "Lighting"]},
        {"id": "decks", "name": "Decks", "img": "deck.jpg", "kind": "deck",
         "blurb": "Decks that connect the house to the yard.",
         "intro": "We design decks that flow into the patio and landscape below.",
         "bullets": ["Wood and composite decks", "Stairs and landings", "Railings", "Deck-to-patio transitions"]},
        {"id": "walls", "name": "Retaining walls &amp; erosion control", "img": "walls.jpg", "kind": "stone",
         "blurb": "Hold the slope and stop the washout.",
         "intro": "North Georgia hills are beautiful until the soil starts moving. We build retaining walls and erosion control that keep it in place.",
         "bullets": ["Retaining walls", "Erosion control", "Terraced beds", "Slope stabilization"]},
        {"id": "drainage", "name": "Drainage solutions", "img": "drainage.jpg", "kind": "garden",
         "blurb": "Send the water where it belongs.",
         "intro": "Soggy lawns and wet basements usually have a simple cause. We find it and fix it.",
         "bullets": ["French drains", "Downspout drainage", "Dry creek beds", "Regrading"]},
        {"id": "turf", "name": "Artificial turf", "img": "turf.jpg", "kind": "garden",
         "blurb": "Green all year, no mowing.",
         "intro": "Artificial turf for the spots grass won&rsquo;t grow, and for families who&rsquo;d rather play than mow.",
         "bullets": ["Artificial lawns", "Pet-friendly turf", "Putting greens", "Proper base and drainage"]},
        {"id": "lighting", "name": "Landscape lighting", "img": "lighting.jpg", "kind": "garden",
         "blurb": "Enjoy the yard after dark.",
         "intro": "Lighting makes a landscape safe and beautiful at night.",
         "bullets": ["Path and step lighting", "Uplighting for trees and the house", "Patio and wall lights", "Low-voltage LED systems"]},
    ],
    "home_order": ["feature", "statement", "process", "area"],
    "feature": {
        "title": "Not just a landscaper. <span class=\"hl\">Your designer.</span>", "img": "feature.jpg", "photo_label": "patio and fireplace at dusk", "kind": "pavers",
        "body": ["Are you ready to turn your yard into the outdoor escape you&rsquo;ve always wanted? At Wisescapes, every project starts with design: how the space flows, where the sun falls, where the water goes.",
                 "Then we build it, so the finished yard looks like the plan."],
        "checks": ["A design made for your property", "Patios, fireplaces, kitchens and plantings", "Drainage and slopes handled right"],
        "link": ("About Wisescapes", "about.html"),
    },
    "statement": {"cls": "dark", "text": "Your outdoor escape is <em>closer than you think.</em>",
                  "sub": "Call or text 770-672-1526 to schedule a consultation."},
    "process": {"title": "From dream to done", "text": "A simple path from idea to finished yard.", "steps": [
        ("Consultation", "We walk the property and talk about how you want to use it."),
        ("Design", "A plan for the space, with materials and plantings chosen together."),
        ("Build", "We install it, from the stonework to the last plant."),
        ("Enjoy", "Step outside into the yard you&rsquo;ve been dreaming about."),
    ], "cls": "alt"},
    "reviews": {"title": "", "big": "", "label": "", "town": "Cumming"},
    "area": {"title": "Crafted locally for", "towns": ["Cumming", "Forsyth County", "Alpharetta", "Milton", "Johns Creek", "Suwanee", "Dawsonville", "Gainesville"]},
    "band": {"title": "Let&rsquo;s design your dream outdoor space.", "text": "Schedule a consultation, or call or text us any time.", "btn_cls": "btn--light"},
    "work_cats": {"design": "Landscapes", "patios": "Patios &amp; fire", "walls": "Walls &amp; drainage", "living": "Kitchens &amp; decks"},
    "work": [
        ("patios", "Patio &amp; outdoor fireplace", "Cumming", "wide", "pavers"),
        ("design", "Front yard landscape", "Forsyth County", "", "garden"),
        ("walls", "Retaining wall &amp; terraces", "Cumming", "", "stone"),
        ("living", "Outdoor kitchen", "Forsyth County", "", "stone"),
        ("design", "Backyard planting plan", "Cumming", "", "garden"),
        ("patios", "Fire pit patio", "Forsyth County", "", "pavers"),
        ("design", "Landscape lighting", "Cumming", "wide", "garden"),
        ("living", "Deck &amp; stairs", "Forsyth County", "", "deck"),
        ("walls", "Dry creek drainage", "Cumming", "", "garden"),
        ("design", "Artificial turf yard", "Forsyth County", "", "garden"),
    ],
    "pages": {
        "services": {"title": "Creative outdoor solutions", "lede": "Landscape design, patios, fireplaces, outdoor kitchens, decks, walls, drainage, turf and lighting in Cumming and Forsyth County."},
        "work": {"title": "Portfolio", "lede": "Outdoor spaces we&rsquo;ve designed and built in Cumming and Forsyth County."},
        "about": {"title": "Crafted locally in Cumming", "lede": "Wisescapes is a landscape design and outdoor living company rooted in Cumming, Georgia.",
                  "story": {"title": "Design first, then build", "img": "about.jpg", "photo_label": "Wisescapes design session", "kind": "garden",
                            "body": ["We&rsquo;re not just a landscaping crew. We design outdoor spaces, then build them: patios and fireplaces, kitchens and decks, plantings, lighting, and the walls and drainage that make it all work on a north Georgia hillside.",
                                     "We&rsquo;re local, so we know the soil, the slopes and the weather here."],
                            "checks": [], "link": ("Schedule a consultation", "contact.html")},
                  "values_title": "Our approach", "values_cls": "dark",
                  "values": [("Thoughtful design", "Every yard gets a plan built around how you&rsquo;ll actually use it."),
                             ("Local know-how", "North Georgia soil, slopes and storms, handled right."),
                             ("Craft in the details", "Clean stonework, healthy plantings and lighting that sets the mood.")]},
        "contact": {"title": "Schedule a consultation", "lede": "Tell us about your yard and what you&rsquo;re dreaming of. Prefer to talk? Call or text 770-672-1526.",
                    "chips": ["Landscape design", "Patio or fireplace", "Outdoor kitchen", "Deck", "Retaining wall", "Drainage", "Artificial turf", "Lighting"],
                    "submit": "Request my consultation", "done": "We&rsquo;ll reach out to schedule your consultation."},
    },
    "meta": {
        "home": ("Wisescapes | Landscape Designer in Cumming, GA", "Dream outdoor spaces, crafted locally. Landscape design, patios, fireplaces and outdoor living in Cumming and Forsyth County. Call or text 770-672-1526."),
        "services": ("Services | Wisescapes", "Landscape design, patios, outdoor kitchens, decks, retaining walls, drainage, artificial turf and lighting."),
        "work": ("Portfolio | Wisescapes", "Landscapes and outdoor living projects by Wisescapes."),
        "about": ("About | Wisescapes", "Landscape design and outdoor living, crafted locally in Cumming, GA."),
        "contact": ("Schedule a Consultation | Wisescapes", "Schedule a landscape design consultation. Call or text 770-672-1526."),
    },
}

if __name__ == "__main__":
    build(CONFIG, Path(__file__).parent)
    write_readme(CONFIG, Path(__file__).parent, [
        "Their current site shows two phone numbers (770-672-1526 and 770-895-0528). We used 770-672-1526, the one at the top of their homepage. Confirm.",
        "No reviews section, because no review data was found. Add one if they have Google reviews.",
        "Towns under 'Crafted locally for' are assumed from their Cumming address.",
    ])
