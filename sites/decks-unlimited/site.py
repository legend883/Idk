"""Decks & Porches Unlimited demo. Edit text below, then run: python3 site.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_engine"))
from engine import build, theme, svg_uri, stars, write_readme  # noqa: E402

CEDAR, CEDAR_DK, STAIN, BLUE = "#3e210d", "#26140a", "#b8692c", "#1f77ab"
PLANKS_HDR = svg_uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="400" height="120"><rect width="400" height="120" fill="{CEDAR}"/><rect x="0" width="96" height="120" fill="#432310"/><rect x="100" width="96" height="120" fill="#3a1f0c"/><rect x="200" width="96" height="120" fill="#46260f"/><rect x="300" width="96" height="120" fill="#371d0b"/><g fill="#1c0e05"><rect x="96" width="4" height="120"/><rect x="196" width="4" height="120"/><rect x="296" width="4" height="120"/><rect x="396" width="4" height="120"/></g></svg>')
RAIL = svg_uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="32" height="34"><rect width="32" height="7" fill="{STAIN}"/><rect y="28" width="32" height="6" fill="{CEDAR}"/><rect x="12" y="7" width="8" height="21" fill="#9a5622"/></svg>')
MARK = ('<svg class="logo-mark" viewBox="0 0 48 48" aria-hidden="true">'
        f'<path d="M4 20 24 6l20 14" fill="none" stroke="#fff" stroke-width="3" stroke-linejoin="round"/>'
        f'<rect x="6" y="24" width="36" height="5" rx="1" fill="{STAIN}"/><rect x="6" y="31" width="36" height="5" rx="1" fill="#9a5622"/>'
        '<rect x="9" y="36" width="4" height="8" fill="#fff"/><rect x="35" y="36" width="4" height="8" fill="#fff"/></svg>')

CONFIG = {
    "name": "Decks & Porches Unlimited",
    "logo": {"name": "Decks &amp; Porches Unlimited", "sub": "Buford &middot; North Metro Atlanta", "mark": MARK},
    "phone": "770-945-3288", "tel": "+17709453288",
    "address": "Buford, Georgia",
    "cta": "Free consultation",
    "theme_color": "#000000",
    "footer_blurb": "Custom decks, porches and sunrooms built to last. Designing and installing high-quality decks for Georgia homeowners for more than 35 years.",
    "footer_right": "Buford &amp; North Metro Atlanta",
    "fonts_url": "https://fonts.googleapis.com/css2?family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&family=Source+Sans+3:wght@400;500;600;700;800&display=swap",
    "theme_css": theme(
        f"""
.site-header {{ background: {PLANKS_HDR} left top / 400px 100% repeat-x; }}
.site-header.is-stuck {{ box-shadow: 0 12px 30px -18px rgba(0,0,0,.8); }}
.logo b {{ font-family: 'Libre Caslon Text', serif; font-weight: 400; font-size: 1.5rem; letter-spacing: 0; color: #fff; text-shadow: 0 2px 6px rgba(0,0,0,.5); }}
.site-header .logo span {{ color: #e9c9a6; opacity: 1; letter-spacing: .14em; font-size: .66rem; }}
.nav a:not(.btn) {{ color: #fff; font-weight: 600; text-shadow: 0 1px 4px rgba(0,0,0,.5); }}
.hero--overlay h1 {{ max-width: 18ch; font-size: clamp(2.5rem, 1.3rem + 4.6vw, 5.2rem); }}
.hero--overlay .hl {{ color: #f0c79c; }}
.hero--overlay .accent-bar {{ background: {STAIN}; }}
.trust svg {{ color: #f0c79c; }}
.statement em {{ color: #f0c79c; font-style: italic; }}
.process .step {{ font-style: italic; }}
@media (max-width: 560px) {{ .site-header .logo b {{ font-size: 1.05rem; }} }}
""",
        bg="#ffffff", **{"bg-2": "#f7f1ea"}, ink="#1f140c", **{"ink-2": "#46372b"}, muted="#6a5a4c",
        **{"line": "rgba(62,33,13,.12)", "line-strong": "rgba(62,33,13,.25)"},
        accent=BLUE, **{"accent-hi": "#2589c2", "accent-ink": "#ffffff", "accent-text": BLUE, "accent-on-dark": "#8fd0f2"},
        **{"accent-2": STAIN, "accent-2-hi": "#c97a3a", "accent-2-ink": "#1f140c"},
        focus=BLUE, **{"focus-ring": "rgba(31,119,171,.3)"}, star="#f2b01e",
        dark=CEDAR_DK, **{"dark-ink": "#ffffff", "dark-ink-2": "#e2d2c2"},
        **{"topbar-bg": "#000000", "topbar-ink": "#ffffff", "header-bg": CEDAR, "header-ink": "#ffffff", "nav-current": "#f0c79c"},
        **{"trust-bg": "#000000", "trust-ink": "#ffffff", "trust-line": "rgba(255,255,255,.14)"},
        **{"band-bg": CEDAR, "band-ink": "#ffffff", "band-ink-2": "#e2d2c2", "on-light-accent": CEDAR},
        **{"footer-bg": "#000000", "footer-head": "#f0c79c"},
        **{"pagehead-bg": CEDAR_DK, "pagehead-ink": "#ffffff", "pagehead-ink-2": "#e2d2c2"},
        **{"callbar-call": "#000000", "callbar-call-ink": "#ffffff"},
        **{"f-display": "'Libre Caslon Text', serif", "f-body": "'Source Sans 3', sans-serif"},
        **{"display-weight": "700", "display-case": "uppercase", "display-tracking": "0.01em", "display-leading": "1.08"},
        **{"radius-btn": "4px", "radius-img": "4px", "radius-lg": "6px", "radius-input": "4px"},
        joint=RAIL, **{"joint-h": "34px", "joint-size": "32px 34px"},
    ),
    "topbar": [("chat", "Request a free consultation")],
    "hero": {
        "variant": "overlay",
        "title": "Custom deck builders in <span class=\"hl\">Buford &amp; North Metro Atlanta</span>",
        "sub": "Enjoy a beautiful, safe outdoor space with custom decks, porches and sunrooms built to last. We&rsquo;ve been designing and installing high-quality decks for Georgia homeowners for more than 35 years.",
        "second": ("See the gallery", "work.html"), "second_cls": "btn--alt",
        "photo_label": "wood deck with railings in the trees", "photo_kind": "deck",
        "proof": ["<b>35+ years</b> building Georgia decks", "Based in <b>Buford</b>"],
    },
    "trust": [
        ("home", "35+ years", "Designing and building decks"),
        ("shield", "Built to last", "Safe, solid construction"),
        ("chat", "Free consultation", "Call 770-945-3288"),
        ("check", "Decks to sunrooms", "One builder for it all"),
    ],
    "services_head": {"title": "Decks, porches &amp; sunrooms", "text": "Beautiful, safe outdoor spaces designed for your home and built to last."},
    "services_style": "tiles", "big_tiles": (0,),
    "services": [
        {"id": "decks", "name": "Custom decks", "img": "deck.jpg", "kind": "deck",
         "blurb": "Wood and composite decks, designed for your home and your yard.",
         "intro": "Every deck we build is designed for the house it&rsquo;s attached to and the yard it overlooks, then framed solid so it stays safe for decades.",
         "bullets": ["Wood and composite decks", "Multi-level and second-story decks", "Stairs, landings and railings", "Built to code, built to last"]},
        {"id": "porches", "name": "Porches", "img": "porch.jpg", "kind": "porch",
         "blurb": "Screened and covered porches.",
         "intro": "A screened or covered porch gives you an outdoor room you can use rain or shine, without the bugs.",
         "bullets": ["Screened porches", "Covered porches", "Deck-to-porch conversions", "Ceiling fans and lighting"]},
        {"id": "sunrooms", "name": "Sunrooms", "img": "sunroom.jpg", "kind": "porch",
         "blurb": "Bright rooms you can enjoy all year.",
         "intro": "A sunroom brings the outdoors in, so you can enjoy the view in every season.",
         "bullets": ["Sunroom additions", "Porch-to-sunroom conversions", "Windows and finishes", "Matched to your home"]},
        {"id": "repair", "name": "Deck repair &amp; resurfacing", "img": "repair.jpg", "kind": "composite",
         "blurb": "Make an old deck safe and good-looking again.",
         "intro": "If the frame is sound, a new surface and railings can make an old deck feel brand new. If it isn&rsquo;t, we&rsquo;ll tell you.",
         "bullets": ["Safety inspections", "Board and railing replacement", "Resurfacing with new decking", "Stair repair"]},
        {"id": "patios", "name": "Covered patios &amp; more", "img": "patio.jpg", "kind": "deck",
         "blurb": "Pergolas, covers and outdoor upgrades.",
         "intro": "Shade, shelter and upgrades that make your outdoor space more comfortable.",
         "bullets": ["Covered patios", "Pergolas", "Lighting", "Built-in benches and planters"]},
    ],
    "home_order": ["feature", "statement", "process", "area"],
    "feature": {
        "title": "More than 35 years of decks", "img": "feature.jpg", "photo_label": "finished deck and stairs", "kind": "deck",
        "body": ["Decks Unlimited has been designing and installing decks for Georgia homeowners for more than 35 years. We know what holds up to Georgia sun, storms and humidity, and what doesn&rsquo;t.",
                 "That experience goes into every deck, porch and sunroom we build."],
        "checks": ["35+ years of deck building", "Custom designs, not cookie-cutter kits", "Free consultation to start"],
        "link": ("About us", "about.html"), "cls": "alt",
    },
    "statement": {"cls": "dark", "text": "A beautiful, safe outdoor space, <em>built to last.</em>",
                  "sub": "Request a free consultation: 770-945-3288."},
    "process": {"title": "How we build", "text": "From the first conversation to the final board.", "steps": [
        ("Free consultation", "We talk about your space, your ideas and your budget."),
        ("Design", "A custom plan for your deck, porch or sunroom."),
        ("Build", "Our crew builds it safe, solid and to code."),
        ("Enjoy", "We walk it with you. Then it&rsquo;s time to relax."),
    ]},
    "reviews": {"title": "", "big": "", "label": "", "town": "Buford"},
    "area": {"title": "Service area", "towns": ["Buford", "Sugar Hill", "Suwanee", "Cumming", "Dacula", "Flowery Branch", "Braselton", "Lawrenceville"]},
    "band": {"title": "Ready for your new deck?", "text": "Request a free consultation today.", "btn_cls": ""},
    "work_cats": {"decks": "Decks", "porches": "Porches", "sunrooms": "Sunrooms", "repair": "Repair &amp; resurfacing"},
    "work": [
        ("decks", "Wood deck in the trees", "Buford", "wide", "deck"),
        ("porches", "Screened porch", "North Metro Atlanta", "", "porch"),
        ("decks", "Composite deck &amp; stairs", "North Metro Atlanta", "", "composite"),
        ("sunrooms", "Sunroom addition", "North Metro Atlanta", "", "porch"),
        ("repair", "Deck resurfacing", "North Metro Atlanta", "", "composite"),
        ("decks", "Two-level deck", "North Metro Atlanta", "", "deck"),
        ("porches", "Covered porch", "North Metro Atlanta", "wide", "porch"),
        ("repair", "New railings", "North Metro Atlanta", "", "deck"),
        ("decks", "Deck with pergola", "North Metro Atlanta", "", "deck"),
        ("sunrooms", "Porch-to-sunroom", "North Metro Atlanta", "", "porch"),
    ],
    "pages": {
        "services": {"title": "Our services", "lede": "Custom decks, porches, sunrooms, deck repair and outdoor upgrades in Buford and North Metro Atlanta."},
        "work": {"title": "Gallery", "lede": "Decks, porches and sunrooms we&rsquo;ve built for Georgia homeowners."},
        "about": {"title": "About Decks Unlimited", "lede": "Designing and installing high-quality decks for Georgia homeowners for more than 35 years.",
                  "story": {"title": "35 years of building it right", "img": "about.jpg", "photo_label": "our crew on a deck build", "kind": "deck",
                            "body": ["For more than 35 years, Decks &amp; Porches Unlimited has built custom decks, porches and sunrooms for homeowners across Buford and North Metro Atlanta.",
                                     "Our goal hasn&rsquo;t changed: a beautiful, safe outdoor space, built to last."],
                            "checks": [], "link": ("Request a free consultation", "contact.html")},
                  "values_title": "What you can count on", "values_cls": "dark",
                  "values": [("Experience", "More than 35 years of designing and building decks."),
                             ("Safety", "Solid framing and code-compliant construction on every job."),
                             ("Craftsmanship", "Custom work that looks great and lasts.")]},
        "contact": {"title": "Request a free consultation", "lede": "Tell us about your project. Prefer to talk? Call 770-945-3288.",
                    "chips": ["New deck", "Porch", "Sunroom", "Deck repair", "Covered patio or pergola", "Not sure yet"],
                    "submit": "Request my free consultation", "done": "We&rsquo;ll call you to set up your free consultation."},
    },
    "meta": {
        "home": ("Decks & Porches Unlimited | Custom Deck Builders in Buford, GA", "Custom decks, porches and sunrooms in Buford and North Metro Atlanta. 35+ years. Call 770-945-3288."),
        "services": ("Services | Decks & Porches Unlimited", "Custom decks, porches, sunrooms, deck repair and covered patios."),
        "work": ("Gallery | Decks & Porches Unlimited", "Decks, porches and sunrooms by Decks Unlimited."),
        "about": ("About | Decks & Porches Unlimited", "35+ years building decks in Georgia."),
        "contact": ("Free Consultation | Decks & Porches Unlimited", "Request a free consultation. Call 770-945-3288."),
    },
}

if __name__ == "__main__":
    build(CONFIG, Path(__file__).parent)
    write_readme(CONFIG, Path(__file__).parent, [
        "Logo uses a simple deck icon. Swap in their carpenter mascot logo when they send it.",
        "'Deck repair & resurfacing' and 'Covered patios' come from a directory listing, not their site. Confirm.",
        "A directory shows a 4.9 Google rating from about 90 reviews, but that couldn't be confirmed, so no reviews section yet. Add one once confirmed.",
        "No street address or email found. Only Buford, GA is shown.",
        "Towns under 'Service area' are assumed. Confirm against their Service Area page.",
    ])
