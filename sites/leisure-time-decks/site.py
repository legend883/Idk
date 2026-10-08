"""Leisure Time Decks demo. Edit text below, then run: python3 site.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_engine"))
from engine import build, theme, svg_uri, stars, write_readme  # noqa: E402

GOLD, BLACK = "#e8b431", "#141414"
BOARDS = svg_uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="120" height="30"><rect width="120" height="30" fill="{BLACK}"/><rect x="2" y="3" width="76" height="10" rx="1.5" fill="{GOLD}"/><rect x="82" y="3" width="36" height="10" rx="1.5" fill="#c99520"/><rect x="-20" y="17" width="58" height="10" rx="1.5" fill="#c99520"/><rect x="42" y="17" width="76" height="10" rx="1.5" fill="{GOLD}"/></svg>')
MARK = ('<svg class="logo-mark" viewBox="0 0 48 48" aria-hidden="true">'
        f'<path d="M4 24 24 7l20 17h-7L24 13 11 24z" fill="{GOLD}" stroke="{BLACK}" stroke-width="1.5" stroke-linejoin="round"/>'
        f'<rect x="10" y="27" width="28" height="4" fill="{BLACK}"/><rect x="10" y="34" width="28" height="4" fill="{BLACK}"/><rect x="12" y="38" width="3" height="6" fill="{BLACK}"/><rect x="33" y="38" width="3" height="6" fill="{BLACK}"/></svg>')

CONFIG = {
    "name": "Leisure Time Decks",
    "logo": {"name": "Leisure Time Decks", "sub": "Think Outside the House&trade;", "mark": MARK},
    "phone": "404-997-3325", "tel": "+14049973325",
    "address": "Atlanta, Georgia",
    "cta": "Get a quote",
    "theme_color": "#ffffff",
    "footer_blurb": "Atlanta&rsquo;s premier deck, porch and outdoor fireplace builder. Building decks for over 30 years.",
    "footer_right": "Think Outside the House&trade;",
    "fonts_url": "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Karla:ital,wght@0,400;0,500;0,700;1,400&display=swap",
    "theme_css": theme(
        f"""
.site-header .logo b {{ font-size: 1.35rem; letter-spacing: -0.01em; }}
.site-header .logo span {{ text-transform: none; letter-spacing: .02em; font-size: .82rem; font-weight: 700; opacity: 1; }}
.hero--split h1 {{ font-size: clamp(2.8rem, 1.4rem + 5.2vw, 5.6rem); }}
.hero--split .hl {{ background: linear-gradient(transparent 62%, {GOLD} 62% 92%, transparent 92%); color: inherit; }}
.hero--split .grid > .photo {{ outline: 4px solid {GOLD}; outline-offset: 12px; }}
.trust svg {{ color: {GOLD}; }}
.tile .go {{ color: {BLACK}; }}
.statement em {{ color: {GOLD}; }}
@media (max-width: 900px) {{ .hero--split .grid > .photo {{ outline-offset: 7px; outline-width: 3px; }} }}
""",
        bg="#ffffff", **{"bg-2": "#faf6ec"}, ink=BLACK, **{"ink-2": "#3a3a3a"}, muted="#5f5f5f",
        accent=GOLD, **{"accent-hi": "#f2c24a", "accent-ink": BLACK, "accent-text": "#8a6304", "accent-on-dark": GOLD},
        **{"accent-2": BLACK, "accent-2-hi": "#000", "accent-2-ink": "#ffffff"},
        focus="#8a6304", **{"focus-ring": "rgba(232,180,49,.4)"}, star=GOLD,
        dark=BLACK, **{"dark-ink": "#ffffff", "dark-ink-2": "#cfcfcf"},
        **{"header-bg": "#ffffff", "header-ink": BLACK},
        **{"trust-bg": BLACK, "trust-ink": "#ffffff", "trust-line": "rgba(255,255,255,.14)"},
        **{"band-bg": GOLD, "band-ink": BLACK, "band-ink-2": "#2c2208"},
        **{"footer-bg": BLACK, "footer-head": GOLD},
        **{"pagehead-bg": "#faf6ec", "pagehead-ink": BLACK, "pagehead-ink-2": "#3a3a3a"},
        **{"callbar-call": BLACK, "callbar-call-ink": "#ffffff"},
        **{"f-display": "'Bricolage Grotesque', sans-serif", "f-body": "'Karla', sans-serif"},
        **{"display-weight": "800", "display-tracking": "-0.03em", "display-leading": "0.98"},
        **{"radius-btn": "8px", "radius-img": "10px", "radius-lg": "14px", "radius-input": "8px"},
        joint=BOARDS, **{"joint-h": "30px", "joint-size": "120px 30px"},
    ),
    "topbar": [],
    "hero": {
        "variant": "split",
        "title": "Think outside <span class=\"hl\">the house.</span>",
        "sub": "Atlanta&rsquo;s premier deck, porch and outdoor fireplace builder. We&rsquo;ve been building decks for over 30 years.",
        "second": ("Explore our gallery", "work.html"), "second_cls": "btn--alt",
        "photo_label": "multi-level deck in the trees", "photo_kind": "deck",
        "proof": [f"{stars()} <b>4.9</b> on HomeAdvisor", "<b>30+ years</b> building Atlanta decks"],
    },
    "trust": [
        ("home", "30+ years", "Building decks since 1989"),
        ("star", "4.9 on HomeAdvisor", "Rated by Atlanta homeowners"),
        ("check", "Decks to fireplaces", "One builder for the whole backyard"),
    ],
    "services_head": {"title": "Decks, porches &amp; everything around them", "text": "We started with decks. Over 30 years we&rsquo;ve added porches, outdoor kitchens and fireplaces, so your whole backyard comes from one builder."},
    "services_style": "tiles", "big_tiles": (0,),
    "services": [
        {"id": "decks", "name": "Custom decks", "img": "deck.jpg", "kind": "deck",
         "blurb": "Single-level, multi-level and wraparound decks, built for Atlanta&rsquo;s hills.",
         "intro": "Atlanta lots slope, and that&rsquo;s where we shine. We build custom decks of every shape and height, framed solid and finished clean.",
         "bullets": ["Wood and composite decks", "Multi-level and second-story decks", "Stairs, landings and railings", "Deck lighting"]},
        {"id": "porches", "name": "Porches", "img": "porch.jpg", "kind": "porch",
         "blurb": "Screened and covered porches that feel like part of the house.",
         "intro": "A screened porch adds a room you&rsquo;ll use most of the year. We match the roofline and trim so it looks like it was always there.",
         "bullets": ["Screened porches", "Covered porches", "Deck-to-porch conversions", "Ceiling fans and lighting"]},
        {"id": "kitchens", "name": "Outdoor kitchens", "img": "kitchen.jpg", "kind": "stone",
         "blurb": "Grill stations and full outdoor kitchens.",
         "intro": "Cook where the party is. We build outdoor kitchens on decks, porches and patios.",
         "bullets": ["Grill islands and counters", "Bar seating", "Covered kitchen areas", "Power and lighting"]},
        {"id": "fireplaces", "name": "Outdoor fireplaces &amp; firepits", "img": "fireplace.jpg", "kind": "stone",
         "blurb": "The warm center of the backyard.",
         "intro": "An outdoor fireplace or fire pit keeps everyone outside long after sunset.",
         "bullets": ["Stone outdoor fireplaces", "Fire pits", "Fireplaces on covered porches", "Built-in seating"]},
        {"id": "pergolas", "name": "Pergolas &amp; gazebos", "img": "pergola.jpg", "kind": "deck",
         "blurb": "Shade and shelter for the deck or patio.",
         "intro": "A pergola or gazebo gives an outdoor space shade, shape and a reason to linger.",
         "bullets": ["Pergolas", "Gazebos", "Shade structures over decks", "Stained or painted finishes"]},
        {"id": "sunrooms", "name": "Sunrooms &amp; patios", "img": "sunroom.jpg", "kind": "pavers",
         "blurb": "Sunrooms, stone patios and retaining walls.",
         "intro": "From a sunroom off the kitchen to a stone patio below the deck.",
         "bullets": ["Sunrooms", "Stone patios", "Retaining walls", "Walkways and steps"]},
    ],
    "home_order": ["feature", "statement", "process", "reviews", "area"],
    "feature": {
        "title": "Built on 30 years of experience", "img": "feature.jpg", "photo_label": "covered porch over a deck", "kind": "porch",
        "body": ["Leisure Time Decks has been building in Atlanta since 1989. We&rsquo;ve seen every slope, every soil and every kind of backyard, and we know how to build on all of them.",
                 "That experience shows up in the framing you never see and the finish you see every day."],
        "checks": ["Building Atlanta decks since 1989", "Decks, porches, kitchens and fireplaces", "4.9 rating on HomeAdvisor"],
        "link": ("Our story", "about.html"), "cls": "alt",
    },
    "statement": {"cls": "dark", "text": "Your best room might be <em>outside the house.</em>",
                  "sub": "Morning coffee on the deck. Dinner on the porch. A fire on a cool night. We build the spaces where that happens."},
    "process": {"title": "How we build", "text": "Straightforward from the first call to the final board.", "steps": [
        ("Quote", "We visit, measure and talk through what you want."),
        ("Design", "A layout and a clear price before anything is built."),
        ("Build", "Our crew builds it solid, safe and to code."),
        ("Relax", "We walk it with you. Then it&rsquo;s leisure time."),
    ]},
    "reviews": {"title": "Our reputation", "score": "4.9", "label": "HomeAdvisor rating from Atlanta homeowners", "town": "Atlanta", "cls": "alt"},
    "area": {"title": "Building across metro Atlanta", "towns": ["Atlanta", "Decatur", "Brookhaven", "Sandy Springs", "Dunwoody", "Tucker", "Smyrna", "Marietta"]},
    "band": {"title": "Ready to think outside the house?", "text": "Get a quote for your deck, porch or outdoor fireplace.", "btn_cls": "btn--dark"},
    "work_cats": {"decks": "Decks", "porches": "Porches", "fire": "Kitchens &amp; fire", "more": "Pergolas &amp; more"},
    "work": [
        ("decks", "Two-level deck in the trees", "Atlanta", "wide", "deck"),
        ("porches", "Screened porch", "Atlanta", "", "porch"),
        ("decks", "Composite deck &amp; stairs", "Atlanta", "", "composite"),
        ("fire", "Outdoor fireplace", "Atlanta", "", "stone"),
        ("porches", "Covered porch", "Atlanta", "", "porch"),
        ("more", "Pergola over deck", "Atlanta", "", "deck"),
        ("decks", "Wraparound deck", "Atlanta", "wide", "deck"),
        ("fire", "Outdoor kitchen", "Atlanta", "", "stone"),
        ("more", "Gazebo", "Atlanta", "", "deck"),
        ("fire", "Fire pit &amp; patio", "Atlanta", "", "pavers"),
    ],
    "pages": {
        "services": {"title": "What we build", "lede": "Custom decks, porches, outdoor kitchens, fireplaces and more, from Atlanta&rsquo;s premier deck builder."},
        "work": {"title": "Gallery", "lede": "Decks, porches and outdoor rooms we&rsquo;ve built across Atlanta.", "band_title": "Like what you see?"},
        "about": {"title": "Building Atlanta decks since 1989", "lede": "Leisure Time Decks is Atlanta&rsquo;s premier deck, porch and outdoor fireplace builder.",
                  "story": {"title": "Over 30 years outside the house", "img": "about.jpg", "photo_label": "a finished deck at dusk", "kind": "deck",
                            "body": ["We&rsquo;ve been building decks in Atlanta since 1989. Along the way we added porches, outdoor kitchens, fireplaces, pergolas and sunrooms, so homeowners can get the whole backyard from one builder.",
                                     "After more than 30 years, our approach is the same: build it solid, finish it clean and stand behind it."],
                            "checks": [], "link": ("Get a quote", "contact.html")},
                  "values_title": "Why homeowners choose us",
                  "values": [("Experience", "More than 30 years of building on Atlanta&rsquo;s slopes and soils."),
                             ("Craftsmanship", "Solid framing and clean finishes, inside and out."),
                             ("Reputation", "A 4.9 rating on HomeAdvisor from Atlanta homeowners.")]},
        "contact": {"title": "Get a quote", "lede": "Tell us about your deck, porch or outdoor project. We&rsquo;ll call to set up a visit.",
                    "chips": ["Deck", "Porch", "Outdoor kitchen", "Fireplace or fire pit", "Pergola or gazebo", "Sunroom", "Not sure yet"],
                    "submit": "Request my quote", "done": "We&rsquo;ll call you to set up a time to see your space."},
    },
    "meta": {
        "home": ("Leisure Time Decks | Atlanta's Premier Deck & Porch Builder", "Custom decks, porches, outdoor kitchens and fireplaces in Atlanta. Building decks for over 30 years. Call 404-997-3325."),
        "services": ("Services | Leisure Time Decks", "Custom decks, screened porches, outdoor kitchens, fireplaces, pergolas and sunrooms in Atlanta."),
        "work": ("Gallery | Leisure Time Decks", "Decks and porches built by Leisure Time Decks."),
        "about": ("About | Leisure Time Decks", "Atlanta's premier deck builder since 1989."),
        "contact": ("Get a Quote | Leisure Time Decks", "Get a quote for your deck or porch. Call 404-997-3325."),
    },
}

if __name__ == "__main__":
    build(CONFIG, Path(__file__).parent)
    write_readme(CONFIG, Path(__file__).parent, [
        "Founding year 1989 is from research, and their site says 'over 30 years'. Confirm.",
        "No street address found. The site shows 'Atlanta, Georgia'.",
        "Towns under 'Building across metro Atlanta' are assumed.",
        "Their current site shows raw code at the top of the homepage, and its headlines overlap. Point this out on the call.",
    ])
