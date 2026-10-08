"""Atlanta Porch & Patio demo. Edit text below, then run: python3 site.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_engine"))
from engine import build, theme, svg_uri, stars  # noqa: E402

ORANGE = "#fe5c25"
RAIL = svg_uri('<svg xmlns="http://www.w3.org/2000/svg" width="40" height="40"><rect width="40" height="6" fill="#111"/><rect y="34" width="40" height="6" fill="#111"/><rect x="17" y="6" width="6" height="28" fill="#111"/></svg>')

MARK = ('<svg class="logo-mark" viewBox="0 0 48 48" aria-hidden="true" style="width:54px;height:46px">'
        '<path d="M3 22 L36 6 V40" fill="none" stroke="#fff" stroke-width="3.2" stroke-linecap="square"/>'
        '<path d="M14 18 V40 M25 13 V40 M6 30 H36 M3 40 H40" fill="none" stroke="#fff" stroke-width="2.6"/>'
        f'<rect x="1" y="43" width="42" height="3.4" fill="{ORANGE}"/></svg>')

CONFIG = {
    "name": "Atlanta Porch & Patio",
    "logo": {"name": "Atlanta Porch &amp; Patio", "script": "Extraordinary <span style=\"font-family:var(--f-body);font-size:.62rem;letter-spacing:.12em;text-transform:uppercase\">Outdoor Living</span>", "sub": "Extraordinary Outdoor Living", "mark": MARK},
    "phone": "(678) 398-7077", "tel": "+16783987077",
    "email": "betterdesigns@atlantaporchandpatio.com",
    "address": "1785 Roswell Rd<br>Marietta, GA 30062",
    "cta": "Free consultation",
    "theme_color": "#000000",
    "footer_blurb": "Custom screened porches, decks and patios for metro Atlanta homes. Extraordinary outdoor living, designed and built by our Marietta team.",
    "footer_right": "Marietta, Georgia",
    "fonts_url": "https://fonts.googleapis.com/css2?family=Archivo:wght@600;800&family=Figtree:wght@400;500;700;800&family=Allura&display=swap",
    "theme_css": theme(
        """
.site-header .logo b { color: #fff; font-size: 1.15rem; letter-spacing: .04em; text-transform: uppercase; }
.site-header .logo .script { font-size: 1.4rem; color: #fff; }
.hero--overlay h1 { max-width: 15ch; }
.hero .kick-script { font-size: clamp(2rem, 1.4rem + 2vw, 3.2rem); }
.band h2 { color: #111; }
.trust .t b { color: #fff; }
.section.dark .statement { max-width: 20ch; }
""",
        bg="#ffffff", **{"bg-2": "#f5f2ee"}, ink="#111111", **{"ink-2": "#33363a"}, muted="#5c6066",
        accent=ORANGE, **{"accent-hi": "#ff7444", "accent-ink": "#111111", "accent-text": "#c8410f", "accent-on-dark": ORANGE},
        focus="#c8410f", **{"focus-ring": "rgba(254,92,37,.28)"},
        dark="#000000", **{"dark-ink": "#ffffff", "dark-ink-2": "#c9c9c9"},
        **{"header-bg": "#000000", "header-ink": "#ffffff", "nav-current": ORANGE},
        scrim="rgba(0,0,0,.88)",
        **{"trust-bg": "#111111", "trust-ink": "#ffffff", "trust-line": "rgba(255,255,255,.14)", "trust-icon": ORANGE},
        **{"band-bg": ORANGE, "band-ink": "#111111", "band-ink-2": "#2a1408"},
        **{"footer-bg": "#000000", "footer-head": ORANGE},
        **{"pagehead-bg": "#000000", "pagehead-ink": "#ffffff", "pagehead-ink-2": "#d6d6d6"},
        **{"callbar-call": "#111111", "callbar-call-ink": "#ffffff"},
        **{"f-display": "'Archivo', sans-serif", "f-body": "'Figtree', sans-serif", "f-script": "'Allura', cursive"},
        **{"display-weight": "800", "display-case": "uppercase", "display-tracking": "0", "display-leading": "1"},
        **{"radius-btn": "6px", "radius-img": "2px", "radius-lg": "4px"},
        joint=RAIL, **{"joint-h": "40px", "joint-size": "40px 40px"},
        **{"btn-case": "uppercase", "btn-tracking": ".04em"},
    ),
    "topbar": [],
    "hero": {
        "variant": "overlay",
        "script": "Extraordinary Outdoor Living",
        "title": "Porches &amp; patios <span class=\"hl\">built to be lived on</span>",
        "sub": "Custom screened porches, decks and patios for metro Atlanta homes, designed and built by our Marietta team. It all starts with a free 10-minute consultation.",
        "second": ("See our work", "work.html"),
        "photo_label": "two-story porch and deck", "photo_kind": "porch",
        "proof": [f"{stars()} <b>280+</b> Google reviews", "Based in <b>Marietta</b>, building across metro Atlanta"],
    },
    "trust": [
        ("home", "Porch specialists", "Screened, covered and multi-level"),
        ("chat", "Free 10-minute consult", "Talk it through, no pressure"),
        ("dollar", "Cost &amp; benefit, upfront", "Know what you&rsquo;re paying for"),
        ("star", "280+ Google reviews", "From metro Atlanta homeowners"),
    ],
    "services_head": {"title": "What we build", "text": "Porches are our specialty, and we build the whole outdoor room around them, from the deck to the patio to the fire."},
    "services_style": "tiles", "big_tiles": (0,),
    "services": [
        {"id": "screened-porches", "name": "Screened porches", "img": "screened-porch.jpg", "kind": "porch",
         "blurb": "Bug-free evenings, rain or shine.",
         "intro": "A screened porch adds a room you&rsquo;ll actually use from March to November. We design it to match your house, so it looks like it was always there.",
         "bullets": ["New screened porches and screen-in conversions", "Covered porches and porticos", "Ceiling fans, lighting and TV wiring", "Rooflines matched to your home"]},
        {"id": "decks", "name": "Decks", "img": "deck.jpg", "kind": "deck",
         "blurb": "Single and multi-level decks, stairs and railings.",
         "intro": "From a simple deck off the kitchen to a two-story deck with a spiral staircase, built solid and finished clean.",
         "bullets": ["Wood and composite decking", "Multi-level decks and stairs", "Spiral staircases", "Black metal and wood railings"]},
        {"id": "patios", "name": "Stone &amp; paver patios", "img": "patio.jpg", "kind": "pavers",
         "blurb": "Flagstone, pavers and stone, built on a proper base.",
         "intro": "A patio extends the porch into the yard. We build stone and paver patios that stay level and drain right.",
         "bullets": ["Paver patios", "Natural stone and flagstone", "Steps, walls and borders", "Hardscape design"]},
        {"id": "kitchens", "name": "Outdoor kitchens", "img": "kitchen.jpg", "kind": "stone",
         "blurb": "Grill stations and full outdoor kitchens.",
         "intro": "Cook outside without running back and forth. We build outdoor kitchens sized to how you entertain.",
         "bullets": ["Grill islands and counters", "Bar seating", "Under a covered porch or out on the patio", "Lighting and power"]},
        {"id": "fireplaces", "name": "Outdoor fireplaces", "img": "fireplace.jpg", "kind": "stone",
         "blurb": "The centerpiece for cool Georgia nights.",
         "intro": "An outdoor fireplace turns a porch or patio into the place everyone ends up.",
         "bullets": ["Stone and brick fireplaces", "Fireplaces on covered porches", "Fire pits", "Seating built around the fire"]},
        {"id": "pergolas", "name": "Pergolas", "img": "pergola.jpg", "kind": "deck",
         "blurb": "Shade and structure over the patio.",
         "intro": "A pergola defines an outdoor room and takes the edge off the afternoon sun.",
         "bullets": ["Freestanding and attached pergolas", "Over patios and decks", "Stained or painted finishes", "Lighting and fans"]},
    ],
    "home_order": ["feature", "statement", "process", "reviews", "area"],
    "feature": {
        "title": "Your vision, <span class=\"hl\">our expertise</span>",
        "img": "team.jpg", "photo_label": "finished screened porch at dusk", "kind": "porch",
        "body": ["You know how you want to spend your evenings. We know how to build the porch, deck or patio that makes it happen, and make it look like part of the house.",
                 "We design and build every project ourselves, from the first sketch to the final walkthrough."],
        "checks": ["Free 10-minute consultation to start", "Clear cost and benefit before you commit", "One team from design through build"],
        "link": ("About our team", "about.html"),
    },
    "statement": {"cls": "dark", "text": "Extraordinary outdoor living starts with <em>a 10-minute conversation.</em>",
                  "sub": "Tell us what you&rsquo;re picturing. We&rsquo;ll tell you what it takes to build it."},
    "process": {"title": "How it works", "text": "Simple from the first call.", "steps": [
        ("Free consultation", "A quick 10-minute call about your space, your ideas and your budget."),
        ("Design", "We lay out the porch, deck or patio and show you the cost and benefit."),
        ("Build", "Our crew builds it clean, on schedule and to code."),
        ("Enjoy", "We walk it with you before we call it done. Then it&rsquo;s yours."),
    ]},
    "reviews": {"title": "What homeowners say", "big": "280+", "label": "Google reviews from metro Atlanta homeowners", "town": "Marietta", "cls": "alt"},
    "area": {"title": "Building across metro Atlanta", "towns": ["Marietta", "East Cobb", "Roswell", "Kennesaw", "Smyrna", "Sandy Springs", "Alpharetta", "Atlanta"]},
    "band": {"title": "Let&rsquo;s start crafting your dreams.", "text": "Book a free 10-minute consultation. Tell us what you want, and we&rsquo;ll tell you what it takes.", "btn_cls": "btn--dark"},
    "work_cats": {"porches": "Porches", "decks": "Decks", "patios": "Patios", "living": "Kitchens &amp; fire"},
    "work": [
        ("porches", "Two-story porch &amp; deck", "Metro Atlanta", "wide", "porch"),
        ("porches", "Screened porch", "Marietta", "", "porch"),
        ("decks", "Deck with spiral stair", "Metro Atlanta", "", "deck"),
        ("patios", "Paver patio", "Metro Atlanta", "", "pavers"),
        ("living", "Outdoor fireplace", "Metro Atlanta", "", "stone"),
        ("porches", "Covered porch", "Metro Atlanta", "", "porch"),
        ("decks", "Composite deck", "Metro Atlanta", "wide", "composite"),
        ("living", "Outdoor kitchen", "Metro Atlanta", "", "stone"),
        ("patios", "Stone patio &amp; steps", "Metro Atlanta", "", "pavers"),
        ("decks", "Pergola over deck", "Metro Atlanta", "", "deck"),
    ],
    "pages": {
        "services": {"title": "Porches, decks &amp; patios", "lede": "Everything you need for extraordinary outdoor living, designed and built by one Marietta team."},
        "work": {"title": "Inspiration", "lede": "Porches, decks and patios we&rsquo;ve built for homeowners across metro Atlanta."},
        "about": {"title": "Extraordinary outdoor living", "lede": "Atlanta Porch &amp; Patio designs and builds custom porches, decks and patios from our home base in Marietta.",
                  "story": {"title": "Built around how you live", "img": "about.jpg", "photo_label": "our crew on a porch build", "kind": "porch",
                            "body": ["Every project starts with a conversation about how you want to use the space: morning coffee, family dinners, the game on a Saturday night.",
                                     "From there we design it, show you the cost and benefit, and build it with our own team. We&rsquo;ve shared more than 2,000 project photos on Instagram, so you can see exactly how we work."],
                            "checks": [], "link": ("See the gallery", "work.html")},
                  "values_title": "What you can count on",
                  "values": [("Design first", "We plan the space around your house and your routine before anything gets built."),
                             ("Straight answers on cost", "You&rsquo;ll know the cost and benefit before you commit. No surprises."),
                             ("Built to be lived on", "Solid framing, clean finishes and details that hold up to Georgia weather.")]},
        "contact": {"title": "Let&rsquo;s start crafting your dreams", "lede": "Book your free 10-minute consultation. Tell us a little about your project and we&rsquo;ll call you.",
                    "chips": ["Screened porch", "Deck", "Patio", "Outdoor kitchen", "Fireplace", "Pergola", "Not sure yet"],
                    "submit": "Book my free consultation", "done": "We&rsquo;ll call you to set up your 10-minute consultation."},
    },
    "meta": {
        "home": ("Atlanta Porch & Patio | Screened Porches, Decks & Patios in Marietta", "Custom screened porches, decks and patios across metro Atlanta. Free 10-minute consultation. Call (678) 398-7077."),
        "services": ("Services | Atlanta Porch & Patio", "Screened porches, decks, stone and paver patios, outdoor kitchens, fireplaces and pergolas in metro Atlanta."),
        "work": ("Inspiration Gallery | Atlanta Porch & Patio", "Porches, decks and patios built by Atlanta Porch & Patio."),
        "about": ("About | Atlanta Porch & Patio", "Extraordinary outdoor living, designed and built in Marietta, GA."),
        "contact": ("Free Consultation | Atlanta Porch & Patio", "Book a free 10-minute consultation for your porch, deck or patio. Call (678) 398-7077."),
    },
}

if __name__ == "__main__":
    build(CONFIG, Path(__file__).parent)
    from engine import write_readme
    write_readme(CONFIG, Path(__file__).parent, [
        "Towns listed under 'Building across metro Atlanta' are assumed from their Marietta address.",
        "'280+ Google reviews' comes from research. Double-check the current count.",
        "Service bullet points are typical porch/deck scope. Confirm each one.",
    ])
