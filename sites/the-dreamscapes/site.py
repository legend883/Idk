"""The Dreamscapes demo. Edit text below, then run: python3 site.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_engine"))
from engine import build, theme, svg_uri, stars, write_readme  # noqa: E402

TEAL, TEAL_DK, BLUE, YELLOW = "#12806e", "#0b5a4d", "#1878a8", "#f2c230"
SWOOSH = svg_uri(f'<svg xmlns="http://www.w3.org/2000/svg" width="260" height="30"><path d="M0 22 C 60 2, 130 2, 260 18 V30 H0Z" fill="{TEAL}"/><path d="M0 26 C 70 10, 150 8, 260 24" fill="none" stroke="{YELLOW}" stroke-width="4"/></svg>')
MARK = ('<svg class="logo-mark" viewBox="0 0 48 48" aria-hidden="true">'
        f'<rect x="8" y="5" width="34" height="36" rx="4" fill="{TEAL}"/><path d="M8 5h20L8 30z" fill="{BLUE}"/>'
        f'<path d="M3 40c10-2 18-10 20-20 1-5 6-9 12-9-6 3-8 8-9 12-2 9-10 17-23 17z" fill="{YELLOW}"/></svg>')

CONFIG = {
    "name": "The Dreamscapes",
    "logo": {"name": "Dreamscapes", "sub": "Design &middot; Build &middot; Maintain", "mark": MARK},
    "phone": "678-574-4008", "tel": "+16785744008",
    "address": "4337 Dallas Acworth Hwy<br>Acworth, GA 30101",
    "cta": "Free estimate",
    "theme_color": "#ffffff",
    "footer_blurb": "Design, build and maintain. Landscape design, outdoor living and lawn care for Acworth, Cobb and Cherokee County homeowners.",
    "footer_right": "Acworth, Georgia",
    "fonts_url": "https://fonts.googleapis.com/css2?family=Gloock&family=Nunito+Sans:ital,opsz,wght@0,6..12,400;0,6..12,600;0,6..12,800;0,6..12,900;1,6..12,400&display=swap",
    "theme_css": theme(
        f"""
.logo b {{ font-family: 'Nunito Sans', sans-serif; font-weight: 900; letter-spacing: .08em; text-transform: uppercase; font-size: 1.45rem; color: {BLUE}; }}
.site-header .logo span {{ color: {TEAL}; letter-spacing: .32em; font-size: .62rem; opacity: 1; }}
.site-footer .logo b {{ color: #fff; }}
.nav a:not(.btn) {{ color: {TEAL}; font-weight: 800; }}
.nav a[aria-current="page"] {{ color: {BLUE}; }}
.hero--split {{ background: linear-gradient(180deg, #eef7f5, #ffffff); }}
.hero--split h1 {{ font-size: clamp(2.8rem, 1.4rem + 5vw, 5.4rem); }}
.hero--split .hl {{ color: {TEAL}; }}
.hero--split .grid > .photo {{ border-radius: 28px 28px 28px 120px; }}
.hero--split .grid > .photo .ph-label {{ left: auto; right: .8rem; }}
@media (max-width: 900px) {{ .hero--split .grid > .photo {{ border-radius: 20px 20px 20px 70px; }} }}
.tile .go {{ color: {TEAL_DK}; }}
.trust svg {{ color: {YELLOW}; }}
.statement em {{ color: {YELLOW}; }}
""",
        bg="#ffffff", **{"bg-2": "#eef7f5"}, ink="#13302b", **{"ink-2": "#34514b"}, muted="#56706a",
        **{"line": "rgba(19,48,43,.1)", "line-strong": "rgba(19,48,43,.22)"},
        accent=YELLOW, **{"accent-hi": "#f7cf52", "accent-ink": TEAL_DK, "accent-text": TEAL, "accent-on-dark": YELLOW},
        **{"accent-2": TEAL, "accent-2-hi": "#169680", "accent-2-ink": "#ffffff"},
        focus=BLUE, **{"focus-ring": "rgba(24,120,168,.3)"}, star=YELLOW,
        dark=TEAL_DK, **{"dark-ink": "#ffffff", "dark-ink-2": "#cfe7e1"},
        **{"header-bg": "#ffffff", "header-ink": "#13302b"},
        **{"trust-bg": TEAL, "trust-ink": "#ffffff", "trust-line": "rgba(255,255,255,.2)"},
        **{"band-bg": BLUE, "band-ink": "#ffffff", "band-ink-2": "#d6eaf4", "on-light-accent": TEAL_DK},
        **{"footer-bg": "#0a3d35", "footer-head": YELLOW},
        **{"pagehead-bg": "#eef7f5", "pagehead-ink": "#13302b", "pagehead-ink-2": "#34514b"},
        **{"callbar-call": TEAL, "callbar-call-ink": "#ffffff"},
        **{"f-display": "'Gloock', serif", "f-body": "'Nunito Sans', sans-serif"},
        **{"display-weight": "400", "display-tracking": "-0.01em", "display-leading": "1.04"},
        **{"radius-btn": "8px", "radius-img": "20px", "radius-lg": "24px", "radius-input": "10px"},
        joint=SWOOSH, **{"joint-h": "30px", "joint-size": "260px 30px"},
    ),
    "topbar": [],
    "hero": {
        "variant": "split",
        "title": "Let us design &amp; build the landscape <span class=\"hl\">of your dreams.</span>",
        "sub": "Over 30 years of landscape design and 20 years of lawn care in Acworth. We design it, build it and keep it beautiful.",
        "second": ("View portfolio", "work.html"), "second_cls": "btn--alt",
        "photo_label": "lit patio, fire feature and garden at dusk", "photo_kind": "garden",
        "proof": ["<b>30+ years</b> of landscape design", "<b>20+ years</b> of lawn care"],
    },
    "trust": [
        ("leaf", "Design", "30+ years designing landscapes"),
        ("home", "Build", "Patios, kitchens and plantings"),
        ("check", "Maintain", "20+ years of lawn care"),
    ],
    "services_head": {"title": "Design. Build. Maintain.", "text": "One team for the whole life of your landscape, from the first sketch to the weekly mow."},
    "services_style": "tiles", "big_tiles": (0,),
    "services": [
        {"id": "design", "name": "Landscape design", "img": "design.jpg", "kind": "garden",
         "blurb": "Over 30 years of designing landscapes people love.",
         "intro": "Good landscapes are designed, not assembled. We plan plantings, hardscape and lighting together so the whole yard works as one.",
         "bullets": ["Custom landscape design", "Planting plans", "Hardscape layout", "Lighting design"]},
        {"id": "outdoor-living", "name": "Outdoor living", "img": "outdoor-living.jpg", "kind": "stone",
         "blurb": "Outdoor kitchens, fire features and patios.",
         "intro": "Outdoor kitchens, fire features and gathering spaces built into the landscape.",
         "bullets": ["Outdoor kitchens", "Fire pits and fire features", "Seat walls", "Patio lighting"]},
        {"id": "hardscaping", "name": "Hardscaping &amp; patios", "img": "hardscape.jpg", "kind": "pavers",
         "blurb": "Patios, walkways and stepping stones.",
         "intro": "Patios, walkways and walls that tie the house to the garden.",
         "bullets": ["Paver and stone patios", "Walkways and stepping stones", "Retaining walls", "Steps"]},
        {"id": "lawn", "name": "Lawn care &amp; maintenance", "img": "lawn.jpg", "kind": "garden",
         "blurb": "20+ years of keeping Acworth lawns healthy.",
         "intro": "We don&rsquo;t just build it and leave. Our maintenance crews keep your landscape looking the way it did on day one.",
         "bullets": ["Mowing and edging", "Fertilization and weed control", "Shrub pruning", "Seasonal cleanups"]},
        {"id": "planting", "name": "Planting", "img": "planting.jpg", "kind": "garden",
         "blurb": "Trees, shrubs, perennials and color.",
         "intro": "The right plants in the right places, chosen for Georgia&rsquo;s climate.",
         "bullets": ["Trees and shrubs", "Perennials and seasonal color", "Bed installation", "Mulch and pine straw"]},
        {"id": "drainage", "name": "Grading, drainage &amp; irrigation", "img": "drainage.jpg", "kind": "garden",
         "blurb": "Water where you want it, and nowhere else.",
         "intro": "Proper grading, drainage and irrigation keep the landscape healthy and the house dry.",
         "bullets": ["Grading", "Drainage solutions", "Irrigation systems", "Irrigation repair"]},
    ],
    "home_order": ["feature", "statement", "process", "area"],
    "feature": {
        "title": "Decades of dreams, <span class=\"hl\">built</span>", "img": "feature.jpg", "photo_label": "stepping stones through a garden", "kind": "garden",
        "body": ["With more than 30 years of landscape design and over 20 years of lawn care behind us, we&rsquo;ve learned what makes a landscape beautiful on day one and still beautiful years later.",
                 "That&rsquo;s why we design, build and maintain: so the dream doesn&rsquo;t fade after the crew leaves."],
        "checks": ["30+ years of landscape design", "20+ years of lawn care", "Design, build and maintenance in one place"],
        "link": ("About The Dreamscapes", "about.html"), "cls": "alt",
    },
    "statement": {"cls": "dark", "text": "Your dream landscape, <em>designed, built and maintained</em> by one team.",
                  "sub": "Call 678-574-4008 for a free estimate."},
    "process": {"title": "How we bring it to life", "text": "From the first conversation to the first mow.", "steps": [
        ("Free estimate", "We visit, listen and walk the property with you."),
        ("Design", "A landscape plan built around your dream and your budget."),
        ("Build", "Our crews install the hardscape, plantings and lighting."),
        ("Maintain", "Keep it beautiful with ongoing care."),
    ]},
    "reviews": {"title": "", "big": "", "label": "", "town": "Acworth"},
    "area": {"title": "Proudly serving", "towns": ["Acworth", "Kennesaw", "Woodstock", "Dallas", "Cartersville", "Marietta", "Canton", "Cherokee County"]},
    "band": {"title": "Ready to build your dream landscape?", "text": "Get a free estimate from The Dreamscapes.", "btn_cls": ""},
    "work_cats": {"design": "Landscapes", "living": "Outdoor living", "hardscape": "Hardscape", "lawn": "Lawn care"},
    "work": [
        ("living", "Lit patio &amp; fire feature", "Acworth", "wide", "stone"),
        ("design", "Garden &amp; stepping stones", "Acworth", "", "garden"),
        ("hardscape", "Stone patio", "Cobb County", "", "pavers"),
        ("design", "Front yard design", "Cherokee County", "", "garden"),
        ("lawn", "Lawn renovation", "Acworth", "", "garden"),
        ("living", "Outdoor kitchen", "Acworth", "", "stone"),
        ("design", "Backyard landscape", "Cobb County", "wide", "garden"),
        ("hardscape", "Retaining wall", "Acworth", "", "stone"),
        ("lawn", "Maintained landscape", "Acworth", "", "garden"),
        ("hardscape", "Paver walkway", "Cherokee County", "", "pavers"),
    ],
    "pages": {
        "services": {"title": "Design. Build. Maintain.", "lede": "Landscape design, outdoor living, hardscaping, planting, drainage, irrigation and lawn care in Acworth and beyond."},
        "work": {"title": "Portfolio", "lede": "Landscapes and outdoor living spaces we&rsquo;ve designed, built and maintained."},
        "about": {"title": "About The Dreamscapes", "lede": "Designing, building and maintaining dream landscapes from our home in Acworth, Georgia.",
                  "story": {"title": "30 years of dream landscapes", "img": "about.jpg", "photo_label": "The Dreamscapes team", "kind": "garden",
                            "body": ["We&rsquo;ve spent more than 30 years designing landscapes and over 20 years caring for lawns across Acworth and the surrounding area.",
                                     "Our mission hasn&rsquo;t changed: let us design and build the landscape of your dreams, then keep it that way."],
                            "checks": [], "link": ("Get a free estimate", "contact.html")},
                  "values_title": "What sets us apart", "values_cls": "dark",
                  "values": [("Design expertise", "Three decades of creating landscapes that fit the home and the family."),
                             ("Quality builds", "Hardscapes, plantings and lighting installed with care."),
                             ("Long-term care", "Lawn and landscape maintenance that protects your investment.")]},
        "contact": {"title": "Get a free estimate", "lede": "Tell us about your dream landscape. We&rsquo;ll call to set up a visit.",
                    "chips": ["Landscape design", "Outdoor living", "Patio or hardscape", "Lawn care", "Planting", "Drainage or irrigation"],
                    "submit": "Request my free estimate", "done": "We&rsquo;ll call you to schedule your free estimate."},
    },
    "meta": {
        "home": ("The Dreamscapes | Landscape Design, Build & Maintain in Acworth, GA", "Let us design and build the landscape of your dreams. 30+ years of landscape design. Call 678-574-4008."),
        "services": ("Services | The Dreamscapes", "Landscape design, outdoor living, hardscaping, planting, drainage, irrigation and lawn care."),
        "work": ("Portfolio | The Dreamscapes", "Landscapes designed and built by The Dreamscapes."),
        "about": ("About | The Dreamscapes", "30+ years of landscape design in Acworth, GA."),
        "contact": ("Free Estimate | The Dreamscapes", "Get a free landscape estimate. Call 678-574-4008."),
    },
}

if __name__ == "__main__":
    build(CONFIG, Path(__file__).parent)
    write_readme(CONFIG, Path(__file__).parent, [
        "Their site has a Testimonials page. Copy their real testimonials into a reviews section.",
        "Their site has a Careers page. Add one if they want it.",
        "Towns under 'Proudly serving' are assumed. Confirm.",
    ])
