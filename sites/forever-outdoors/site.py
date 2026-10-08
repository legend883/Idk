"""Forever Outdoors demo. Edit text below, then run: python3 site.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_engine"))
from engine import build, theme, svg_uri, stars, write_readme  # noqa: E402

NAVY, NAVY_DK, STEEL, GREY = "#0b3354", "#072238", "#5f8db1", "#8a8f95"
RIDGE = svg_uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="300" height="36"><path d="M0 36 L40 14 L62 24 L100 4 L140 26 L170 16 L210 30 L250 10 L300 34 V36Z" fill="{NAVY}"/><path d="M0 36 L30 26 L70 32 L120 20 L160 34 L200 24 L240 32 L280 22 L300 28 V36Z" fill="{STEEL}" opacity=".55"/></svg>')
MARK = ('<svg class="logo-mark" viewBox="0 0 56 40" aria-hidden="true" style="width:62px;height:44px">'
        f'<path d="M4 22c8-14 22-18 34-10 6 4 10 4 14 2-6 12-20 16-32 8-6-4-11-4-16 0Z" fill="{NAVY}"/>'
        f'<path d="M14 24l7-9 5 6 4-4 8 9" fill="none" stroke="#fff" stroke-width="1.8"/>'
        f'<path d="M44 30l3-7 3 7h-2v3h-2v-3z" fill="{NAVY}"/><path d="M8 34c10 4 30 4 42-4" fill="none" stroke="{NAVY}" stroke-width="2.4"/></svg>')

CONFIG = {
    "name": "Forever Outdoors",
    "logo": {"name": "Forever <i>Outdoors</i>", "sub": "Outdoor Living &middot; Milton, GA", "mark": MARK},
    "phone": "(770) 231-0520", "tel": "+17702310520",
    "address": "Milton, GA 30004",
    "cta": "Get a free quote",
    "theme_color": "#ffffff",
    "footer_blurb": "Custom outdoor living solutions designed for your lifestyle and built to last. Decks, porches, patios and more in Milton and North Metro Atlanta.",
    "footer_right": "Milton, Georgia",
    "fonts_url": "https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=Poppins:wght@400;500;600&display=swap",
    "theme_css": theme(
        f"""
.site-header .logo b {{ font-family: 'Oswald', sans-serif; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; font-size: 1.3rem; color: {NAVY}; }}
.site-header .logo .lt > span {{ display: none; }}
.logo b i {{ font-style: normal; color: {GREY}; }}
.site-footer .logo b {{ font-family: 'Oswald', sans-serif; text-transform: uppercase; letter-spacing: .06em; }}
.site-footer .logo b i {{ color: #b6c3cf; }}
.hero--overlay h1 {{ max-width: 13ch; }}
.hero--overlay .accent-bar {{ background: {STEEL}; }}
.trust svg {{ color: #9fc0da; }}
.statement em {{ color: #9fc0da; }}
""",
        bg="#ffffff", **{"bg-2": "#f1f4f7"}, ink="#14202b", **{"ink-2": "#37434f"}, muted="#5a6672",
        accent=NAVY, **{"accent-hi": "#114673", "accent-ink": "#ffffff", "accent-text": NAVY, "accent-on-dark": "#9fc0da"},
        **{"accent-2": "#3f6f94", "accent-2-hi": STEEL, "accent-2-ink": "#ffffff"},
        focus=STEEL, **{"focus-ring": "rgba(95,141,177,.35)"}, star="#f0b429",
        dark=NAVY_DK, **{"dark-ink": "#ffffff", "dark-ink-2": "#c4d2de"},
        **{"header-bg": "#ffffff", "header-ink": "#14202b", "nav-current": NAVY},
        **{"trust-bg": NAVY, "trust-ink": "#ffffff", "trust-line": "rgba(255,255,255,.14)"},
        **{"band-bg": NAVY, "band-ink": "#ffffff", "band-ink-2": "#c4d2de", "on-light-accent": NAVY},
        **{"footer-bg": NAVY_DK, "footer-head": "#9fc0da"},
        **{"pagehead-bg": NAVY, "pagehead-ink": "#ffffff", "pagehead-ink-2": "#c4d2de"},
        **{"callbar-call": "#14202b", "callbar-call-ink": "#ffffff"},
        **{"f-display": "'Oswald', sans-serif", "f-body": "'Poppins', sans-serif"},
        **{"display-weight": "700", "display-case": "uppercase", "display-tracking": "0.01em", "display-leading": "1.02"},
        **{"radius-btn": "0px", "radius-img": "0px", "radius-lg": "0px", "radius-input": "0px"},
        joint=RIDGE, **{"joint-h": "36px", "joint-size": "300px 36px"},
    ),
    "topbar": [],
    "hero": {
        "variant": "overlay",
        "title": "Transform your <span class=\"hl\">outdoor living</span> space",
        "sub": "Custom outdoor living solutions designed for your lifestyle and built to last. Decks, porches, patios, outdoor kitchens and more across Milton and North Metro Atlanta.",
        "second": ("Talk with us", "contact.html"),
        "photo_label": "covered outdoor kitchen and lounge", "photo_kind": "stone",
        "proof": ["<b>Trex</b> &amp; <b>TimberTech</b> composite decking", "Based in <b>Milton, GA</b>"],
    },
    "trust": [
        ("home", "Custom design", "Built for your lifestyle"),
        ("shield", "Built to last", "Low-maintenance materials"),
        ("check", "Trex &amp; TimberTech", "Composite decking options"),
        ("chat", "Free quotes", "Talk with us about your space"),
    ],
    "services_head": {"title": "Built for the way you live outside", "text": "From a composite deck that never needs staining to a full backyard makeover with a kitchen and fire."},
    "services_style": "tiles", "big_tiles": (0,),
    "services": [
        {"id": "composite-decks", "name": "Composite decks", "img": "composite-deck.jpg", "kind": "composite",
         "blurb": "Trex and TimberTech decks that skip the yearly staining.",
         "intro": "Composite decking looks like wood without the sanding, sealing and splinters. We build with leading brands like Trex and TimberTech.",
         "bullets": ["Trex decking", "TimberTech decking", "Multi-level decks", "Composite and aluminum railings"]},
        {"id": "wood-decks", "name": "Wood decks", "img": "wood-deck.jpg", "kind": "deck",
         "blurb": "Classic wood decks, framed solid and finished clean.",
         "intro": "A well-built wood deck is a classic for good reason. We frame it right and finish it to last.",
         "bullets": ["Pressure-treated and cedar decks", "Stairs and landings", "Built-in benches", "Deck repairs and replacements"]},
        {"id": "porches", "name": "Porches", "img": "porch.jpg", "kind": "porch",
         "blurb": "Covered and screened porches that extend your home.",
         "intro": "Add a covered or screened porch and get a room you&rsquo;ll use most of the year.",
         "bullets": ["Covered porches", "Screened porches", "Porch ceilings, fans and lighting", "TV and entertainment setups"]},
        {"id": "patios", "name": "Paver patios", "img": "patio.jpg", "kind": "pavers",
         "blurb": "Paver patios and walkways on a solid base.",
         "intro": "A paver patio built on a proper base stays flat and handsome for years.",
         "bullets": ["Paver patios", "Walkways", "Steps and borders", "Patio expansions"]},
        {"id": "kitchens", "name": "Outdoor kitchens", "img": "kitchen.jpg", "kind": "stone",
         "blurb": "Grill, prep and gather under one roof.",
         "intro": "Outdoor kitchens with room to cook, serve and hang out, often under a covered porch.",
         "bullets": ["Grill islands and counters", "Stone and stacked-stone finishes", "Refrigerator and storage space", "TV and lighting"]},
        {"id": "fire", "name": "Fire features", "img": "fire.jpg", "kind": "stone",
         "blurb": "Fire pits and fireplaces for cool nights.",
         "intro": "A fire feature gives the backyard a place to gather after dark.",
         "bullets": ["Fire pits", "Outdoor fireplaces", "Seat walls", "Gas and wood-burning options"]},
        {"id": "walls", "name": "Retaining walls", "img": "walls.jpg", "kind": "stone",
         "blurb": "Level the yard and hold the slope.",
         "intro": "Retaining walls that turn a slope into usable space.",
         "bullets": ["Block retaining walls", "Stone walls", "Terraced yards", "Drainage behind every wall"]},
        {"id": "makeovers", "name": "Backyard makeovers", "img": "makeover.jpg", "kind": "garden",
         "blurb": "The whole backyard, planned and built together.",
         "intro": "Deck, patio, kitchen and fire, designed as one space and built by one team.",
         "bullets": ["Full backyard design", "Phased projects", "Combined deck and patio builds", "Lighting and finishing touches"]},
    ],
    "home_order": ["feature", "statement", "process", "area"],
    "feature": {
        "title": "Designed for your lifestyle", "img": "feature.jpg", "photo_label": "composite deck with railings", "kind": "composite",
        "body": ["Every family uses its backyard differently. We start by learning how you want to spend time outside, then design a space built around it.",
                 "Then we build it with materials meant to last, so you spend your weekends enjoying it, not maintaining it."],
        "checks": ["Composite decking from Trex and TimberTech", "Decks, porches, patios and kitchens", "One team from design to build"],
        "link": ("About Forever Outdoors", "about.html"), "cls": "alt",
    },
    "statement": {"cls": "dark", "text": "Built to last, <em>so you can enjoy it forever.</em>",
                  "sub": "Low-maintenance materials, solid construction and a design made for your family."},
    "process": {"title": "How it works", "text": "Talk with us, and we&rsquo;ll take it from there.", "steps": [
        ("Talk with us", "Tell us what you&rsquo;re picturing and how you&rsquo;ll use the space."),
        ("Free quote", "We visit, measure and give you a clear quote."),
        ("Build", "Our team builds it with materials made to last."),
        ("Enjoy", "Step outside into your new outdoor living space."),
    ]},
    "reviews": {"title": "", "big": "", "label": "", "town": "Milton"},
    "area": {"title": "Areas we serve", "towns": ["Milton", "Alpharetta", "Roswell", "Johns Creek", "Cumming", "Canton", "Woodstock", "Crabapple"]},
    "band": {"title": "Ready to transform your backyard?", "text": "Get a free quote on your deck, porch, patio or outdoor kitchen.", "btn_cls": "btn--light"},
    "work_cats": {"decks": "Decks", "porches": "Porches", "patios": "Patios &amp; walls", "living": "Kitchens &amp; fire"},
    "work": [
        ("living", "Covered outdoor kitchen", "Milton", "wide", "stone"),
        ("decks", "Composite deck", "North Metro Atlanta", "", "composite"),
        ("porches", "Screened porch", "North Metro Atlanta", "", "porch"),
        ("patios", "Paver patio", "North Metro Atlanta", "", "pavers"),
        ("living", "Fire pit &amp; seating", "North Metro Atlanta", "", "stone"),
        ("decks", "Wood deck &amp; stairs", "North Metro Atlanta", "", "deck"),
        ("patios", "Retaining wall", "North Metro Atlanta", "wide", "stone"),
        ("porches", "Covered porch", "North Metro Atlanta", "", "porch"),
        ("decks", "Multi-level deck", "North Metro Atlanta", "", "composite"),
        ("living", "Backyard makeover", "North Metro Atlanta", "", "garden"),
    ],
    "pages": {
        "services": {"title": "Our services", "lede": "Composite and wood decks, porches, paver patios, outdoor kitchens, fire features, retaining walls and full backyard makeovers."},
        "work": {"title": "Gallery", "lede": "Outdoor living spaces we&rsquo;ve built in Milton and North Metro Atlanta."},
        "about": {"title": "Outdoor living, built to last", "lede": "Forever Outdoors designs and builds custom outdoor living spaces in Milton and North Metro Atlanta.",
                  "story": {"title": "Your backyard, forever better", "img": "about.jpg", "photo_label": "our team on a deck build", "kind": "composite",
                            "body": ["We build decks, porches, patios, outdoor kitchens and fire features designed around how your family lives, and built with materials that last.",
                                     "Based in Milton, we serve homeowners across North Metro Atlanta."],
                            "checks": [], "link": ("Get a free quote", "contact.html")},
                  "values_title": "What we believe", "values_cls": "dark",
                  "values": [("Design for life", "Your space should fit how you actually live outside."),
                             ("Build to last", "Quality materials and solid construction, every time."),
                             ("Easy to work with", "Clear quotes, clear communication and a clean job site.")]},
        "contact": {"title": "Get a free quote", "lede": "Tell us about your project and we&rsquo;ll be in touch.",
                    "chips": ["Composite deck", "Wood deck", "Porch", "Paver patio", "Outdoor kitchen", "Fire feature", "Retaining wall", "Backyard makeover"],
                    "submit": "Request my free quote", "done": "We&rsquo;ll call you to talk about your project."},
    },
    "meta": {
        "home": ("Forever Outdoors | Decks, Porches & Outdoor Living in Milton, GA", "Custom decks, porches, patios and outdoor kitchens in Milton and North Metro Atlanta. Call (770) 231-0520."),
        "services": ("Services | Forever Outdoors", "Composite and wood decks, porches, patios, outdoor kitchens, fire features and retaining walls."),
        "work": ("Gallery | Forever Outdoors", "Outdoor living projects by Forever Outdoors."),
        "about": ("About | Forever Outdoors", "Custom outdoor living, built to last, in Milton, GA."),
        "contact": ("Free Quote | Forever Outdoors", "Get a free quote. Call (770) 231-0520."),
    },
}

if __name__ == "__main__":
    build(CONFIG, Path(__file__).parent)
    write_readme(CONFIG, Path(__file__).parent, [
        "No reviews section, because no review data was found. Add one if they have Google reviews.",
        "Their live site's footer labels outdoor kitchens as 'Siding Services', and the 'Our Services' menu link goes nowhere. Good talking points.",
        "Towns under 'Areas we serve' are assumed. Confirm.",
        "Confirm they're Trex and TimberTech installers before going live.",
    ])
