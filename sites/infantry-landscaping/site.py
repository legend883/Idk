"""Infantry Landscaping demo. Edit text below, then run: python3 site.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_engine"))
from engine import build, theme, svg_uri, stars, write_readme  # noqa: E402

OLIVE, OLIVE_DK, KHAKI = "#4f5938", "#2f3521", "#c9c19a"
RIBBON = svg_uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="36" height="20"><rect width="36" height="20" fill="{OLIVE}"/><path d="M0 20 L10 0 H18 L8 20Z M18 20 L28 0 H36 L26 20Z" fill="{KHAKI}"/></svg>')
MARK = ('<svg class="logo-mark" viewBox="0 0 48 48" aria-hidden="true">'
        f'<circle cx="24" cy="24" r="21.5" fill="#fff" stroke="#111" stroke-width="3"/>'
        f'<path d="M24 11.5l3.3 7.6 8.2.7-6.2 5.4 1.9 8-7.2-4.3-7.2 4.3 1.9-8-6.2-5.4 8.2-.7z" fill="{OLIVE}"/>'
        '<path d="M9 36h30" stroke="#111" stroke-width="2.4"/></svg>')

CONFIG = {
    "name": "Infantry Landscaping",
    "logo": {"name": "Infantry Landscaping", "sub": "Veteran Owned &amp; Operated", "mark": MARK},
    "phone": "(678) 539-8007", "tel": "+16785398007",
    "address": "3355 Lenox Rd NE, Ste 1000<br>Atlanta, GA 30326",
    "cta": "Request a quote",
    "theme_color": OLIVE,
    "footer_blurb": "Veteran-owned and operated. We build astonishing outdoor spaces for homes and businesses throughout Metro Atlanta.",
    "footer_right": "Licensed &amp; insured &middot; BBB accredited",
    "fonts_url": "https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@600;700;800&family=Poppins:wght@400;500;600;700&display=swap",
    "theme_css": theme(
        f"""
.site-header .logo b {{ font-family: 'Saira Condensed', sans-serif; font-size: 1.5rem; text-transform: uppercase; letter-spacing: .02em; }}
.site-header .logo span {{ color: {OLIVE}; opacity: 1; }}
.nav a:not(.btn) {{ text-transform: uppercase; letter-spacing: .04em; font-weight: 600; font-size: .92rem; }}
.hero--overlay h1 {{ max-width: 14ch; }}
.hero--overlay .accent-bar {{ background: {KHAKI}; }}
.trust svg {{ color: {KHAKI}; }}
.tile .go {{ border-radius: 2px; }}
.process li {{ border-top-width: 4px; }}
""",
        bg="#ffffff", **{"bg-2": "#f3f2ec"}, ink="#1b1d16", **{"ink-2": "#3a3d31"}, muted="#5d6152",
        accent=OLIVE, **{"accent-hi": "#5d6943", "accent-ink": "#ffffff", "accent-text": OLIVE, "accent-on-dark": KHAKI},
        **{"accent-2": "#1b1d16", "accent-2-hi": "#000", "accent-2-ink": "#ffffff"},
        focus=OLIVE, **{"focus-ring": "rgba(79,89,56,.3)"}, star="#e8a923",
        dark=OLIVE_DK, **{"dark-ink": "#ffffff", "dark-ink-2": "#d4d6c6"},
        **{"topbar-bg": OLIVE, "topbar-ink": "#ffffff", "header-bg": "#ffffff", "header-ink": "#1b1d16", "nav-current": OLIVE},
        **{"trust-bg": "#1b1d16", "trust-ink": "#ffffff", "trust-line": "rgba(255,255,255,.12)"},
        **{"band-bg": OLIVE, "band-ink": "#ffffff", "band-ink-2": "#e6e8db", "on-light-accent": OLIVE_DK},
        **{"footer-bg": "#16180f", "footer-head": KHAKI},
        **{"pagehead-bg": OLIVE_DK, "pagehead-ink": "#ffffff", "pagehead-ink-2": "#d4d6c6"},
        **{"callbar-call": "#1b1d16", "callbar-call-ink": "#ffffff"},
        **{"f-display": "'Saira Condensed', sans-serif", "f-body": "'Poppins', sans-serif"},
        **{"display-weight": "800", "display-case": "uppercase", "display-tracking": "0.005em", "display-leading": "0.98"},
        **{"radius-btn": "2px", "radius-img": "2px", "radius-lg": "2px", "radius-input": "2px"},
        joint=RIBBON, **{"joint-h": "20px", "joint-size": "36px 20px"},
        **{"btn-case": "uppercase", "btn-tracking": ".06em"},
    ),
    "topbar": [("shield", "Licensed &amp; Insured"), ("flag", "Veteran Owned &amp; Operated"), ("medal", "BBB Accredited")],
    "hero": {
        "variant": "overlay",
        "title": "Top-rated landscaping <span class=\"hl\">Atlanta, GA</span>",
        "sub": "Infantry Landscaping is a veteran-owned and operated company that builds astonishing outdoor spaces for homes and businesses throughout Metro Atlanta.",
        "second": ("See our work", "work.html"),
        "photo_label": "boulder garden and landscape beds", "photo_kind": "garden",
        "proof": [f"{stars()} <b>4.8</b> on Google, 160+ reviews", "<b>Veteran</b> owned &amp; operated"],
    },
    "trust": [
        ("flag", "Veteran owned", "And operated, start to finish"),
        ("shield", "Licensed &amp; insured", "Protected on every job"),
        ("medal", "BBB accredited", "Accountable to our clients"),
        ("star", "4.8 on Google", "From 160+ reviews"),
    ],
    "services_head": {"title": "Every part of the property", "text": "Landscape, outdoor living, fences, irrigation, lawn and trees. One accountable crew for all of it."},
    "services_style": "tiles", "big_tiles": (),
    "services": [
        {"id": "landscape", "name": "Landscape design", "img": "landscape.jpg", "kind": "garden",
         "blurb": "Design and installation, from beds to boulders.",
         "intro": "We take your ideas from concept to reality with a landscape plan built for Georgia soil, sun and rain.",
         "bullets": ["Landscape design", "Planting and bed installation", "Boulders and natural stone", "Sod installation"]},
        {"id": "outdoor-living", "name": "Outdoor living", "img": "outdoor-living.jpg", "kind": "pavers",
         "blurb": "Patios, outdoor kitchens and retaining walls.",
         "intro": "Outdoor rooms built to be used: patios, kitchens, fire features and the walls that hold it all together.",
         "bullets": ["Patios and walkways", "Outdoor kitchens", "Retaining walls", "Outdoor lighting"]},
        {"id": "fences", "name": "Fences", "img": "fence.jpg", "kind": "deck",
         "blurb": "Privacy, security and a clean property line.",
         "intro": "Fences built straight, set deep and finished to last.",
         "bullets": ["Wood privacy fences", "Horizontal and modern styles", "Gates", "Repairs"]},
        {"id": "irrigation", "name": "Irrigation", "img": "irrigation.jpg", "kind": "garden",
         "blurb": "Sprinkler systems that water what needs it.",
         "intro": "A properly zoned irrigation system keeps the landscape healthy without wasting water.",
         "bullets": ["New irrigation systems", "Repairs and adjustments", "Drip irrigation for beds", "Seasonal start-up and shut-down"]},
        {"id": "lawn", "name": "Lawn care", "img": "lawn.jpg", "kind": "garden",
         "blurb": "Mowing, maintenance and a lawn you&rsquo;re proud of.",
         "intro": "Regular, reliable lawn care for homes and businesses.",
         "bullets": ["Mowing and edging", "Seasonal cleanups", "Aeration and seeding", "Mulch and pine straw"]},
        {"id": "trees", "name": "Tree services", "img": "trees.jpg", "kind": "garden",
         "blurb": "Trimming, removal and cleanup, done safely.",
         "intro": "Healthy trees and a safe property, handled by a crew that cleans up after itself.",
         "bullets": ["Tree trimming and pruning", "Tree removal", "Storm cleanup", "Planting new trees"]},
    ],
    "home_order": ["statement", "feature", "process", "reviews", "area"],
    "statement": {"cls": "dark", "text": "Our mission is to bring our clients&rsquo; dreams &amp; visions <em>from a concept into reality.</em>",
                  "sub": "Veteran owned and operated. The discipline and accountability we learned in service go into every yard we build."},
    "feature": {
        "title": "Discipline you can see in the details", "img": "feature.jpg", "photo_label": "crew installing a stone patio", "kind": "pavers",
        "body": ["We show up when we say we will, communicate clearly, and finish what we start. That&rsquo;s how we were trained, and it&rsquo;s how we run every job.",
                 "Licensed, insured and BBB accredited, with a 4.8 Google rating from more than 160 reviews."],
        "checks": ["Clear plan and written quote", "On-time crews and clean job sites", "Licensed, insured and BBB accredited"],
        "link": ("About Infantry Landscaping", "about.html"), "cls": "alt",
    },
    "process": {"title": "Mission plan", "text": "A clear plan from concept to reality.", "steps": [
        ("Recon", "We walk the property with you and learn what you want."),
        ("Plan", "A design and a written quote you can count on."),
        ("Execute", "Our crew builds it, on schedule and to standard."),
        ("Debrief", "We walk the finished project with you before we leave."),
    ]},
    "reviews": {"title": "Top-rated in Atlanta", "score": "4.8", "label": "Google rating from 160+ reviews", "town": "Atlanta", "cls": "alt"},
    "area": {"title": "Serving Metro Atlanta", "towns": ["Atlanta", "Buckhead", "Brookhaven", "Sandy Springs", "Dunwoody", "Decatur", "Vinings", "Smyrna"]},
    "band": {"title": "Ready to start your project?", "text": "Request a quote and we&rsquo;ll get you a plan. Veteran owned, licensed and insured.", "btn_cls": "btn--light"},
    "work_cats": {"landscape": "Landscape", "living": "Outdoor living", "fences": "Fences", "lawn": "Lawn &amp; trees"},
    "work": [
        ("landscape", "Boulder garden &amp; beds", "Metro Atlanta", "wide", "garden"),
        ("living", "Stone patio", "Metro Atlanta", "", "pavers"),
        ("fences", "Privacy fence", "Metro Atlanta", "", "deck"),
        ("landscape", "Front yard refresh", "Metro Atlanta", "", "garden"),
        ("living", "Retaining wall", "Metro Atlanta", "", "stone"),
        ("lawn", "Sod installation", "Metro Atlanta", "", "garden"),
        ("living", "Outdoor kitchen", "Metro Atlanta", "wide", "stone"),
        ("fences", "Horizontal fence &amp; gate", "Metro Atlanta", "", "deck"),
        ("lawn", "Tree removal &amp; cleanup", "Metro Atlanta", "", "garden"),
        ("landscape", "Commercial landscape", "Metro Atlanta", "", "garden"),
    ],
    "pages": {
        "services": {"title": "Our services", "lede": "Landscape, outdoor living, fences, irrigation, lawn and tree services for homes and businesses across Metro Atlanta."},
        "work": {"title": "Our work", "lede": "Outdoor spaces we&rsquo;ve built for homes and businesses throughout Metro Atlanta."},
        "about": {"title": "Veteran owned &amp; operated", "lede": "Infantry Landscaping builds astonishing outdoor spaces for homes and businesses throughout Metro Atlanta.",
                  "story": {"title": "From concept to reality", "img": "about.jpg", "photo_label": "the Infantry Landscaping crew", "kind": "garden",
                            "body": ["Our mission is to bring our clients&rsquo; dreams and visions from a concept into reality.",
                                     "As a veteran-owned and operated company, we run every job with the same discipline, accountability and attention to detail we learned in service. We&rsquo;re licensed, insured and BBB accredited."],
                            "checks": [], "link": ("Request a quote", "contact.html")},
                  "values_title": "What we stand for", "values_cls": "dark",
                  "values": [("Accountability", "We own every detail of the job, from the first meeting to the final walkthrough."),
                             ("Discipline", "On-time crews, clean job sites and work done to standard."),
                             ("Service", "We treat your property, and your time, with respect.")]},
        "contact": {"title": "Request a quote", "lede": "Tell us about your property and what you have in mind. We&rsquo;ll be in touch to set up a visit.",
                    "chips": ["Landscape design", "Outdoor living", "Fence", "Irrigation", "Lawn care", "Tree services", "Commercial property"],
                    "submit": "Request my quote", "done": "We&rsquo;ll call you to set up a time to see the property."},
    },
    "meta": {
        "home": ("Infantry Landscaping | Top-Rated Landscaping in Atlanta, GA", "Veteran-owned landscaping, outdoor living, fences, irrigation, lawn and tree services in Metro Atlanta. Call (678) 539-8007."),
        "services": ("Services | Infantry Landscaping", "Landscape design, outdoor living, fences, irrigation, lawn and tree services in Atlanta."),
        "work": ("Our Work | Infantry Landscaping", "Landscapes and outdoor spaces built by Infantry Landscaping."),
        "about": ("About | Infantry Landscaping", "Veteran owned and operated landscaping company in Atlanta, GA."),
        "contact": ("Request a Quote | Infantry Landscaping", "Request a landscaping quote. Call (678) 539-8007."),
    },
}

if __name__ == "__main__":
    build(CONFIG, Path(__file__).parent)
    write_readme(CONFIG, Path(__file__).parent, [
        "Logo uses a simple star badge. Swap in their soldier logo file when they send it.",
        "Towns under 'Serving Metro Atlanta' are assumed. Confirm the service area.",
        "The '160+ reviews' count is from research. Double-check the current number.",
        "Service bullet points are typical scope. Confirm each one.",
    ])
