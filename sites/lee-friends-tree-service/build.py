#!/usr/bin/env python3
"""Builds the Lee Friend's Tree Service preview site.

Every page is generated from the BUSINESS facts below, so the name, phone,
hours, towns, and schema stay identical everywhere. Run: python3 build.py
Anything wrapped in confirm() renders as a visible [CONFIRM: ...] tag and is
collected into CONFIRM-LIST.md.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://www.leefriendstreeservice.com"
TODAY = "2026-10-26"

CONFIRMS = []


def confirm(note):
    if note not in CONFIRMS:
        CONFIRMS.append(note)
    return f'<mark class="confirm">[CONFIRM: {html.escape(note)}]</mark>'


def plain(s):
    """Visible text of an HTML fragment, used so schema matches the page exactly."""
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


# ---------------------------------------------------------------- facts
B = {
    "name": "Lee Friend's Tree Service, Inc.",
    "short": "Lee Friend's Tree Service",
    "phone": "(770) 466-5112",
    "tel": "+17704665112",
    "city": "Loganville",
    "region": "GA",
    "zip": "30052",
    "founded": "1989",
    "arborist": "Jennifer Perrone",
    "facebook": "https://www.facebook.com/p/Lee-Friends-Tree-Service-Inc-100064569017757/",
    "maps": "https://www.google.com/maps/place/Lee+Friend's+Tree+Service+Inc/data=!4m2!3m1!1s0x0:0x2d093d0eab3b6f0e",
    "review": "https://search.google.com/local/writereview?placeid=ChIJ67Hz9G7I9YgRDm87qw49CS0",
    "email": "leefriendstree@gmail.com",
    "tagline": "Quality customer service through all seasons",
    "geo": (33.8390, -83.9007),
}
HOURS = [
    ("Monday–Friday", "8:00 AM–5:00 PM", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "08:00", "17:00"),
    ("Saturday", "9:00 AM–5:00 PM", ["Saturday"], "09:00", "17:00"),
    ("Sunday", "Closed", [], None, None),
]
TOWNS = ["Loganville", "Grayson", "Snellville", "Monroe", "Lawrenceville", "Lilburn", "Tucker", "Atlanta",
         "Sandy Springs", "Brookhaven", "Dunwoody", "Johns Creek", "Suwanee", "Buford", "Duluth", "Norcross",
         "Peachtree Corners", "Stone Mountain", "Conyers", "Covington", "Decatur", "Smyrna", "Athens",
         "Statham", "Winder", "Bethlehem", "Auburn", "Braselton"]
TOWN_PAGES = {"Loganville": "loganville-ga", "Grayson": "grayson-ga", "Snellville": "snellville-ga", "Monroe": "monroe-ga"}
AREAS = "areas-we-serve/"  # same URL as the current site

# Current-site URLs this rebuild drops, and where they should 301-redirect at launch.
REDIRECTS = {
    "/tucker-ga/": "/areas-we-serve/", "/atlanta-ga/": "/areas-we-serve/",
    "/sandy-springs-ga/": "/areas-we-serve/", "/brookhaven-ga/": "/areas-we-serve/", "/dunwoody-ga/": "/areas-we-serve/",
    "/johns-creek-ga/": "/areas-we-serve/", "/suwanee-ga/": "/areas-we-serve/", "/buford-ga/": "/areas-we-serve/",
    "/gallery/": "/", "/thank-you/": "/contact/", "/eco-friendly/": "/services/wood-recycling/",
    "/tree-service-in-<town>-ga/ (old city pages)": "/areas-we-serve/",
}

C_YEAR = "Founding year: the current site says 1989 everywhere, but some outside listings say 1991. Confirm 1989"
C_HOURS = "Business hours: these match the current site; confirm with the owner"
C_INSURED = "Licensed and insured: the current site says 'licensed tree removal contractors' and 'fully insured'. Confirm, and add license or insurance details if the owner wants them shown"
C_ARBORIST = "Jennifer Perrone is the ISA Certified Arborist on staff (the current site never names the arborist; public listings name her)"
C_STREET = "Show the street address (3474 Johnson Rd) publicly? If yes, it is added to every page and the schema"


# ---------------------------------------------------------------- icons (authored, one 1.75 stroke)
ICON = {
    "removal": '<path d="M12 21v-6"/><path d="M7.5 15h9L12 3 7.5 15Z"/><path d="M4 9.5l3 1.2M20 9.5l-3 1.2"/><path d="M9 21h6"/>',
    "trimming": '<circle cx="6" cy="18" r="2.6"/><circle cx="12.5" cy="19.5" r="2.6"/><path d="M7.8 16.2 19 4.5M11.2 17.3 15 9"/><path d="M15 9l4-4.5"/>',
    "storm": '<path d="M7 12a4 4 0 1 1 1.3-7.8A5 5 0 0 1 18 6a3 3 0 0 1 0 6H7Z"/><path d="m12 13-2 4h3l-2 4"/>',
    "stump": '<ellipse cx="12" cy="9" rx="7" ry="3"/><path d="M5 9v7c0 1.7 3.1 3 7 3s7-1.3 7-3V9"/><ellipse cx="12" cy="9" rx="3.5" ry="1.3"/><path d="M5 16l-2 3M19 16l2 3"/>',
    "recycling": '<path d="M5 19c0-8 5-13 14-14-1 9-6 14-14 14Z"/><path d="M5 19 13 11"/>',
    "firewood": '<circle cx="7" cy="16" r="3"/><circle cx="17" cy="16" r="3"/><circle cx="12" cy="9" r="3"/><circle cx="7" cy="16" r=".8"/><circle cx="17" cy="16" r=".8"/><circle cx="12" cy="9" r=".8"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/>',
    "check": '<path d="m5 12 4.5 4.5L19 7"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "camera": '<path d="M4 8h3l2-3h6l2 3h3v11H4Z"/><circle cx="12" cy="13" r="3.5"/>',
    "family": '<circle cx="8" cy="7" r="2.5"/><circle cx="16" cy="7" r="2.5"/><path d="M3.5 20v-4a4.5 4.5 0 0 1 9 0M11.5 20v-4a4.5 4.5 0 0 1 9 0"/>',
    "shield": '<path d="M12 3 5 6v6c0 4.5 3 7.5 7 9 4-1.5 7-4.5 7-9V6Z"/><path d="m9 12 2 2 4-4"/>',
    "badge": '<circle cx="12" cy="9" r="5.5"/><path d="m8.5 13.5-1.5 7 5-2.5 5 2.5-1.5-7"/>',
    "bolt": '<path d="M13 3 5 14h6l-1 7 8-11h-6Z"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "facebook": '<path d="M14 21v-7h3l.5-3.5H14V8.5c0-1 .4-1.7 1.8-1.7h1.8V3.7A20 20 0 0 0 15 3.5c-2.6 0-4.4 1.6-4.4 4.5v2.5H7.6V14h3v7"/>',
}


def icon(name, cls="ico"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICON[name]}</svg>')


# ---------------------------------------------------------------- services
# Slugs match the current site's URLs so existing search rankings carry over.
SERVICES = [
    {
        "slug": "tree-removal-services", "name": "Tree Removal", "icon": "removal",
        "title": "Tree Removal in Loganville, GA | Lee Friend's Tree Service",
        "meta": "Safe removal of hazardous, dead, and unwanted trees in Loganville, GA and Metro Atlanta, with a certified arborist on staff. Free estimates: (770) 466-5112.",
        "line": "Hazardous, dead, and unwanted trees taken down safely, piece by piece when they stand close to a house.",
        "answer": "Lee Friend's Tree Service removes hazardous, dead, and unwanted trees for homes and businesses in Loganville, GA and across Gwinnett, Walton, and Metro Atlanta. Our certified arborist helps you decide whether a tree truly needs to come down, and every job ends with the debris cleared away.",
        "what": "Tree removal means cutting a tree down in controlled sections, lowering the pieces safely, and hauling the wood away. A tree with open space around it can sometimes be felled whole; a tree beside a house, fence, or driveway is taken down in pieces so nothing falls where it shouldn't.",
        "includes": ["Hazardous tree removal", "Dead tree removal", "Clearing space for projects", "Tree debris removal and hauling", "Full property tree removal"],
        "when": ["The tree is dead or rotting, with bare limbs or peeling bark.",
                 "It leans toward your house, driveway, or a neighbor's property.",
                 "The trunk is cracked, split, or hollow.",
                 "A storm has damaged it beyond saving.",
                 "It hangs over your roof or crowds a structure.",
                 "You need room for an addition, pool, or backyard upgrade."],
        "steps": [("Call for a free estimate", f"Call {B['phone']} or send the quote form with a few details about the tree."),
                  ("We assess the tree", "We look at the tree, what's around it, and the safest way to take it down, then explain what needs to be done and why."),
                  ("The crew takes it down", "Trees near buildings come down in sections, so your roof, fence, and lawn stay protected."),
                  ("Clean-up and recycling", "We haul the wood and clear the debris. Branches become mulch, and good logs go to local mills or become firewood.")],
        "faq": [
            ("How much does tree removal cost in Loganville?",
             "It depends on the tree's size, how close it is to your house or power lines, and its condition. We give free, no-obligation estimates that spell out the scope and cost up front. " + confirm("Typical tree removal price range, if the owner wants one published")),
            ("Is stump grinding included with tree removal?",
             "Stump grinding is a separate service you can add to any removal. " + confirm("Whether stump grinding is quoted separately or bundled")),
            ("Can you remove a tree that's right next to my house?",
             "Yes. Trees close to houses, fences, and garages are taken down in small sections, so pieces never drop onto the roof. One customer's 100-year-old pine stood between a wood fence, a driveway, and an attached garage."),
            ("Do I need a permit to remove a tree?",
             "Some cities in the Atlanta area require a permit for certain trees, and many homeowners don't need one. We know the permit requirements in the areas we serve, so ask us when we come out to look at the tree."),
        ],
    },
    {
        "slug": "tree-trimming-services", "name": "Tree Trimming & Pruning", "icon": "trimming",
        "title": "Tree Trimming & Pruning in Loganville, GA | Lee Friend's Tree Service",
        "meta": "Tree trimming and pruning in Loganville, GA: dead wood removal, roof and building clearance, and utility line clearance, with a certified arborist on staff.",
        "line": "Dead wood out, roofs and lines cleared, and trees trimmed without unnecessary cutting.",
        "answer": "Lee Friend's Tree Service trims and prunes trees for homes and businesses in Loganville, GA and the surrounding area, with a certified arborist on staff. We remove dead wood, clear roofs, buildings, and utility lines, and trim without unnecessary cutting.",
        "what": "Pruning is cutting specific branches for a reason: to remove dead or diseased wood, clear a roof or driveway, let in sunlight, or reduce wind resistance. Each job is matched to the tree's type, size, and surroundings, and each cut is made where the tree can seal the wound.",
        "includes": ["Building clearance trimming", "Dead wood removal", "Utility line clearance", "Curb appeal improvement", "Full property trimming", "Large tree trimming"],
        "when": ["Dead or broken branches hang over the house, deck, or driveway.",
                 "Limbs scratch the roof or block gutters.",
                 "Branches crowd the power lines to your house.",
                 "The canopy blocks so much sunlight the lawn won't grow.",
                 "You want trees ready before storm season.",
                 "The property simply looks overgrown."],
        "steps": [("Call for a free estimate", f"Call {B['phone']} or send the quote form and tell us which trees concern you."),
                  ("We look at each tree", "We point out dead wood, weak limbs, and clearance problems, and explain what we'd cut and why."),
                  ("Careful cuts", "The crew removes the chosen branches, lowering larger limbs so they don't damage what's below."),
                  ("Clean-up", "Branches are chipped into mulch and the yard is left clean.")],
        "faq": [
            ("When is the best time to prune trees in Georgia?",
             "Late winter, while most trees are dormant, is a good time for routine pruning. Dead, broken, or dangerous limbs should come out any time of year, and trimming before storm season lowers the risk of limbs coming down."),
            ("Do you top trees?",
             "The International Society of Arboriculture (ISA) advises against topping because it weakens trees and causes fast, weak regrowth. Thinning and crown reduction are better ways to make a tree smaller. " + confirm("Confirm the crews do not top trees")),
            ("Do you trim trees for businesses?",
             "Yes. We trim for homeowners and for commercial properties, keeping buildings, parking areas, and walkways clear."),
        ],
    },
    {
        "slug": "storm-damage-tree-removal", "name": "Storm Damage Tree Removal", "icon": "storm",
        "title": "Storm Damage Tree Removal in Loganville, GA | Lee Friend's Tree Service",
        "meta": "Fast storm damage tree removal in Loganville, GA: fallen trees cleared from homes, cars, and driveways, with insurance coordination. Call (770) 466-5112.",
        "line": "Fallen trees cleared off homes, cars, and driveways, with help coordinating your insurance claim.",
        "answer": "Lee Friend's Tree Service removes storm-damaged and fallen trees in Loganville, GA and across Gwinnett, Walton, and Metro Atlanta, and coordinates directly with your insurance company. Call (770) 466-5112 as soon as everyone is safe.",
        "what": "Storm damage tree removal is the clean-up after wind or rain brings down a tree or big limbs. It covers trees on rooftops, cars, sheds, fences, and driveways, hanging limbs that could still fall, and hauling away the debris.",
        "includes": ["Fallen tree clean-up", "Tree removal from homes", "Car and driveway clearing", "Emergency site response", "Insurance coordination"],
        "when": ["A tree or large limb has fallen on your house, garage, or car.",
                 "A downed tree blocks your driveway or fence line.",
                 "Limbs are cracked and hanging in the canopy after a storm.",
                 "A tree is newly leaning, or the soil around its roots has lifted.",
                 "You need the damage documented for an insurance claim."],
        "steps": [("Get safe, then call", f"Keep everyone away from the tree and any wires. If power lines are involved, call Georgia Power. Then call us at {B['phone']}."),
                  ("Quick on-site assessment", "We look at how the tree is resting and what it's pressing on, then plan a safe way to lift it off."),
                  ("Removal and clean-up", "The crew removes the tree, branches, and debris without causing more damage to your property."),
                  ("Insurance coordination", "We document the damage for your insurance report and coordinate directly with your insurance company.")],
        "faq": [
            ("Does homeowners insurance cover a fallen tree?",
             "Usually yes, when a storm knocks a tree onto a covered structure such as your house, garage, or fence. Policies often don't pay to remove a tree that fell without hitting anything, or one that fell because it was already dead. Check your own policy; we document the damage and coordinate directly with your insurance company."),
            ("What should I do first when a tree falls on my house?",
             "Get everyone out of the damaged part of the house and stay away from the tree and any downed wires. Call Georgia Power if lines are involved, take photos for your insurance company, then call us."),
            ("Do you handle emergency storm damage?",
             f"Yes. We respond quickly to trees on homes, vehicles, and driveways. Call {B['phone']}. " + confirm("After-hours and weekend emergency availability (an old Duluth page says 24/7)")),
        ],
    },
    {
        "slug": "stump-grinding-services", "name": "Stump Grinding", "icon": "stump",
        "title": "Stump Grinding in Loganville, GA | Lee Friend's Tree Service",
        "meta": "Stump grinding below ground level for homes and businesses in Loganville, GA. No digging, multiple stumps in one visit, clean finish. Call (770) 466-5112.",
        "line": "Stumps ground below ground level, with no digging, so you can mow, plant, or build over the spot.",
        "answer": "Lee Friend's Tree Service grinds tree stumps below ground level for homes and businesses in Loganville, GA and the surrounding area. We grind instead of digging stumps out, which is faster, costs less, and leaves the rest of your yard intact.",
        "what": "Stump grinding uses a commercial grinder with a spinning, toothed wheel to shred the stump just below grade. The spot can then be covered with soil, grass, or mulch, and the roots left underground slowly break down. There's no digging or excavation.",
        "includes": ["Grinding unsightly stumps", "Removing tripping hazards", "Several stumps in one visit", "Residential and commercial properties", "Clean-up of the grindings"],
        "when": ["An old stump is in the way of mowing.",
                 "You want to plant grass, a garden, or a new tree in that spot.",
                 "The stump is attracting pests.",
                 "It's a tripping hazard near a walkway or driveway.",
                 "You're preparing the space for sod, a walkway, or construction."],
        "steps": [("Call for a free estimate", f"Call {B['phone']} or send the quote form. Tell us how many stumps and roughly how wide they are."),
                  ("We check the area", "We take extra care around sidewalks, driveways, and structures before grinding."),
                  ("Grinding", "The grinder cuts the stump down below ground level, with depth matched to the stump's size and location."),
                  ("Clean-up", "We haul the grindings away or leave them as mulch, whichever you prefer.")],
        "faq": [
            ("How long does stump grinding take?",
             "Often about an hour. One customer had two medium-sized stumps ground and the area cleaned up in about an hour; larger stumps take longer."),
            ("How deep do you grind a stump?",
             "Just below ground level, deep enough to cover the spot with soil, grass, or mulch. We adjust the depth to the stump's size and location."),
            ("Do you dig out stumps and roots?",
             "No. We grind stumps instead of digging them out, which is less invasive and less costly, and leaves the rest of your lawn intact."),
        ],
    },
    {
        "slug": "wood-recycling", "name": "Eco-Friendly Wood Recycling", "icon": "recycling",
        "title": "Eco-Friendly Wood Recycling in Loganville, GA | Lee Friend's Tree Service",
        "meta": "Lee Friend's Tree Service recycles tree waste in Loganville, GA into mulch, milled wood, and firewood instead of sending it to landfills. Call (770) 466-5112.",
        "line": "The wood we cut becomes mulch, milled wood, and firewood instead of landfill.",
        "answer": "Lee Friend's Tree Service recycles the wood from its jobs in Loganville, GA instead of sending it to a landfill. Branches become mulch, hardwood and pine logs go to local mills, and leftover hardwood is split and seasoned into firewood.",
        "what": "Wood recycling means every part of a tree we cut gets a second use. Small debris goes through our chipper and becomes wood chips for mulch and landscaping. Larger hardwood and pine logs are delivered to local mills, where they're turned into paper, furniture, or milled wood. Leftover hardwood is cut and split into firewood.",
        "includes": ["Garden mulch sharing", "Firewood splitting", "Log transport to local mills", "Hardwood repurposing", "Recycled mulch for landscaping"],
        "when": ["You'd like your tree job to send nothing to the landfill.",
                 "You want wood chips for garden beds, paths, or play areas.",
                 "You'd like seasoned firewood cut from local trees."],
        "steps": [("Chipping", "Smaller debris goes through our wood chipper and becomes chips for mulching and landscaping."),
                  ("Sorting the logs", "Larger hardwood and pine pieces are set aside for the mill."),
                  ("To the mill", "Those logs are delivered to local mills and turned into paper, furniture, or milled wood products."),
                  ("Firewood", "Leftover hardwood is cut, split, and seasoned for firewood.")],
        "faq": [
            ("Can I get free wood chips?",
             f"Yes, wood chips are free. Call {B['phone']} to ask. " + confirm("How free wood chips work: drop-off, pickup, minimum load, waiting list")),
            ("What happens to the wood from my trees?",
             "We recycle it. Branches become mulch, hardwood and pine logs go to local mills for paper, furniture, and lumber, and leftover hardwood becomes seasoned firewood."),
            ("Do you deliver mulch?",
             "Yes. We deliver recycled wood mulch for landscaping projects. Call to ask what's available."),
        ],
    },
    {
        "slug": "firewood-company", "name": "Firewood Sales", "icon": "firewood",
        "title": "Firewood for Sale in Loganville, GA | Lee Friend's Tree Service",
        "meta": "Seasoned, low-moisture hardwood firewood in Loganville, GA, cut and split from local tree work. Delivery or pickup. Call Lee Friend's at (770) 466-5112.",
        "line": "Seasoned, low-moisture hardwood, cut and split by our own crew, delivered or ready for pickup.",
        "answer": "Lee Friend's Tree Service sells seasoned hardwood firewood in Loganville, GA, with local delivery or pickup. We cut, split, and season it ourselves from our own tree work, so it's dry, lights easily, and burns clean.",
        "what": "Seasoned firewood is wood that has been split and left to dry until most of its moisture is gone. Dry hardwood catches fire easily, burns longer and steadier, and makes less smoke than green wood. Ours is cut to practical sizes that fit most fireplaces, stoves, and fire pits.",
        "includes": ["Seasoned hardwood for steady burning", "Clean cuts sized for easy stacking", "Low moisture for easy lighting", "Supply sourced from our tree work", "Delivery or pickup"],
        "when": ["You heat with a fireplace or wood stove.",
                 "You want wood for a fire pit or outdoor cooking.",
                 "You run a restaurant with wood-fired equipment.",
                 "You'd rather buy local wood than shipped-in bundles."],
        "steps": [("Call to order", f"Call {B['phone']} and tell us how much wood you need."),
                  ("Choose delivery or pickup", "We deliver locally, or you can pick it up. " + confirm("Firewood delivery area and fee")),
                  ("Stack and enjoy", "Keep it off the ground and covered on top so it stays dry.")],
        "faq": [
            ("Do you deliver firewood?",
             "Yes, local firewood delivery is available, and you can also pick it up. " + confirm("Firewood delivery area and fee")),
            ("What kind of firewood do you sell?",
             "Seasoned, low-moisture hardwood cut and split from our own tree work. " + confirm("Which species are usually in stock (oak, hickory, etc.)")),
            ("How much does a load of firewood cost?",
             confirm("Firewood prices and load sizes (cord, half cord, truckload)")),
        ],
    },
]
SV = {s["slug"]: s for s in SERVICES}

# ---------------------------------------------------------------- general FAQ (FAQ page)
GENERAL_FAQ = [
    ("How much does tree removal cost in Loganville?", SERVICES[0]["faq"][0][1]),
    ("Does homeowners insurance cover a fallen tree?", SERVICES[2]["faq"][0][1]),
    ("Why hire an ISA Certified Arborist?",
     "A Certified Arborist has formal training in tree biology, health assessment, and proper pruning, and keeps the credential current with continuing education. Instead of simply cutting branches, our arborist looks at each tree's structure and condition, so you get advice that protects the tree and your property."),
    ("How can I check that your arborist is certified?",
     f"You can verify {B['arborist']}'s ISA credential at treesaregood.org, the International Society of Arboriculture's public site, using its Verify a Certified Arborist search."),
    ("What's the best way to find a licensed tree removal service in Loganville?",
     "Check that the company is licensed and insured and has been in business for years. Lee Friend's Tree Service has served Loganville and the Metro Atlanta area since 1989."),
    ("How long does stump grinding take?", SERVICES[3]["faq"][0][1]),
    ("Do you offer free estimates?",
     f"Yes. Estimates are free and no-obligation. Call {B['phone']}; we can often come out the same day."),
    ("Do you handle emergency storm damage?", SERVICES[2]["faq"][2][1]),
    ("Do you deliver firewood?", SERVICES[5]["faq"][0][1]),
    ("Are you licensed and insured?", "Yes. Lee Friend's Tree Service, Inc. is licensed and fully insured. " + confirm(C_INSURED)),
    ("Do you work for businesses as well as homeowners?",
     "Yes. We handle residential and commercial tree work, from a single backyard tree to trees along parking lots, walkways, and entrances."),
    ("What areas do you serve?",
     "We're based in Loganville, GA and serve Gwinnett, Walton, and the Metro Atlanta area, including Grayson, Snellville, Monroe, Lawrenceville, and Athens. See our service areas page for all 28 towns."),
    ("What happens to the wood from my trees?", SERVICES[4]["faq"][1][1]),
    ("Can I get free wood chips?", SERVICES[4]["faq"][0][1]),
    ("When is the best time to prune trees in Georgia?", SERVICES[1]["faq"][0][1]),
]

# ---------------------------------------------------------------- town pages (unique content each)
TOWN_DETAIL = {
    "Loganville": {
        "title": "Tree Service in Loganville, GA | Lee Friend's Tree Service",
        "meta": "Lee Friend's Tree Service is based in Loganville, GA 30052: tree removal, trimming, storm clean-up, stump grinding, and firewood since 1989. (770) 466-5112.",
        "h1": "Tree Service in Loganville, GA",
        "answer": "Lee Friend's Tree Service is based right here in Loganville, GA 30052, and has served the town since 1989. We handle tree removal, trimming and pruning, storm damage, stump grinding, wood recycling, and firewood on both the Walton and Gwinnett sides of town.",
        "sections": [
            ("Where in Loganville are you located?",
             "We're based in Loganville, GA 30052. " + confirm(C_STREET),
             "Being local means the crew, trucks, and chipper don't have far to travel, and we know the roads and neighborhoods on both sides of the county line."),
            ("Do you work on both the Walton and Gwinnett sides of Loganville?",
             "Yes. Loganville sits mostly in Walton County with part of the city in Gwinnett County, and we serve both.",
             "Wherever your address falls, the service, the crew, and the arborist are the same."),
            ("What tree problems are common in Loganville yards?",
             "Tall pines that snap or uproot in storms, and big hardwoods with dead limbs over houses, are the calls we hear most often around Loganville.",
             "Loganville sits in Georgia's Piedmont, where loblolly pines, water oaks, sweetgums, and tulip poplars fill many yards and red clay soil holds the roots. Pines tend to fail in high wind, and older water oaks often decay from the inside, so a look from a certified arborist can catch problems before a storm does. " + confirm("Add one recent Loganville job (street or neighborhood, tree, photo) to make this page even more local")),
        ],
        "faq": [
            ("Is Lee Friend's Tree Service local to Loganville?",
             "Yes. We're a family-owned tree service based in Loganville, GA, serving the area since 1989."),
            ("Which county is Loganville in?",
             "Loganville is mostly in Walton County, with part of the city in Gwinnett County. We serve both."),
        ],
    },
    "Grayson": {
        "title": "Tree Service in Grayson, GA | Lee Friend's Tree Service",
        "meta": "Tree removal, trimming, storm damage clean-up, and stump grinding in Grayson, GA, from a family tree service next door in Loganville. Free estimates.",
        "h1": "Tree Service in Grayson, GA",
        "answer": "Lee Friend's Tree Service serves Grayson, GA from our home base next door in Loganville. Grayson homeowners call us for tree removal, trimming over roofs and driveways, emergency storm clean-up, and stump grinding.",
        "sections": [
            ("How close are you to Grayson?",
             "Grayson is Loganville's neighbor on the Gwinnett County side, so it's one of the closest towns we serve.",
             "Short travel means we can respond quickly to emergency calls in Grayson."),
            ("Why do Grayson trees fall in storms?",
             "Grayson's red clay soil can loosen its grip on roots during heavy spring rains, and severe storms move through from May through September.",
             "Trees that look healthy can develop hidden weaknesses, which is why regular inspections matter here. Our arborist can spot a weakened root plate or limb before the next storm finds it."),
            ("Can you trim trees that hang over a Grayson home?",
             "Yes. Keeping branches off roofs, gutters, and driveways is some of the most common work we do in Grayson.",
             "Every job starts with an assessment of your property and a plan that puts safety first, and we leave the yard clean when we're done. " + confirm("Add one recent Grayson job (neighborhood, tree, photo) for local proof")),
        ],
        "faq": [
            ("Do you serve all of Grayson, GA?",
             "Yes, we serve Grayson and the surrounding parts of Gwinnett County."),
            ("Do you grind stumps in Grayson?",
             "Yes. We grind stumps below ground level in Grayson, often in the same visit as a removal."),
        ],
    },
    "Snellville": {
        "title": "Tree Service in Snellville, GA | Lee Friend's Tree Service",
        "meta": "Storm damage tree removal, trimming, stump grinding, and tree removal in Snellville, GA, with insurance coordination. Call Lee Friend's at (770) 466-5112.",
        "h1": "Tree Service in Snellville, GA",
        "answer": "Lee Friend's Tree Service handles tree removal, trimming, storm damage clean-up, and stump grinding in Snellville, GA, a short drive west of our Loganville base along US-78.",
        "sections": [
            ("Do you handle storm-damaged trees in Snellville?",
             "Yes. When a storm brings a tree down on a Snellville house, car, or driveway, we remove it and coordinate directly with your insurance company.",
             f"Get everyone clear of the tree and any wires, call Georgia Power if lines are involved, then call us at {B['phone']}."),
            ("Do you work for Snellville businesses?",
             "Yes. Along with homes, we take care of trees on commercial properties in Snellville.",
             "That includes removing hazardous trees, trimming limbs away from buildings, parking areas, and entrances, and grinding stumps. " + confirm("Add a Snellville commercial or residential job (with photo) for local proof")),
        ],
        "faq": [
            ("How far is Snellville from your shop?",
             "Snellville is just west of Loganville along US-78, so it's part of our everyday service area."),
            ("Will you help with my insurance claim after a storm in Snellville?",
             "Yes. Storm damage removal includes insurance coordination: we document the damage and work directly with your insurance company."),
        ],
    },
    "Monroe": {
        "title": "Tree Service in Monroe, GA | Lee Friend's Tree Service",
        "meta": "Tree removal, stump grinding, storm clean-up, and seasoned hardwood firewood in Monroe and Walton County, GA. Call Lee Friend's at (770) 466-5112.",
        "h1": "Tree Service in Monroe, GA",
        "answer": "Lee Friend's Tree Service serves Monroe, GA, the Walton County seat, from our base in Loganville. Monroe customers call us for tree removal, stump grinding, storm clean-up, and seasoned hardwood firewood.",
        "sections": [
            ("Do you serve Monroe and the rest of Walton County?",
             "Yes. Loganville is in Walton County too, so Monroe and the county around it are home territory for us.",
             "We work on in-town lots and on larger rural properties around Monroe."),
            ("Can you handle big trees on larger Walton County lots?",
             "Yes. We remove large and hazardous trees, clear storm damage, and grind stumps on properties of any size.",
             "On bigger properties, good hardwood and pine logs from the job go to local mills instead of a landfill, and branches become mulch."),
            ("Can I get firewood delivered in Monroe?",
             "Local firewood delivery is available. " + confirm("Confirm firewood delivery reaches Monroe, and the fee"),
             "Our firewood is seasoned hardwood cut and split from our own tree work. " + confirm("Add one recent Monroe job (with photo) for local proof")),
        ],
        "faq": [
            ("Is Monroe in your service area?",
             "Yes. Monroe and the surrounding parts of Walton County are in our regular service area."),
            ("Do you grind stumps in Monroe?",
             "Yes. We grind stumps below ground level in Monroe, for homes and commercial properties."),
        ],
    },
}

# ---------------------------------------------------------------- reviews (verbatim from the current site; labeled Google Reviews there)
REVIEWS = [
    ("Beth Ediger", "I got about 5 quotes for a tree and stump removal and they provided the best value by far. The crew was friendly and considerate, did a great job cleaning up, and even ground up a little dead stump I’d had in my yard without me even asking. I was really impressed with their work and would definitely recommend them to anyone."),
    ("Gray McKenzie", "Have used them in the past and called about pine tree blown down across my fence. Immediately responsive, arranged on-site inspection and estimate that day. Next morning the crew was here, and the total job was done with great results. Couldn’t be happier – great customer service and interactions, very reasonable charges, great result. Highly recommend their services."),
    ("Tom McCoy", "Could not have done a better job. Very tight location for a 100 year old pine tree, between a wood fence, driveway and front of an attached garage. Not to mention we had to have GA Power drop the power lines before they could get started. Unfortunately GA Power ran 3 hours late costing Lee Friend’s several hours of downtime but instead of leaving and coming back later that day, they took the hit because they did not want us to be without power for an extended period of time. Their lead man John McGowan was especially professional and could not have been more informative. Thank You Lee Friend’s!"),
    ("Andi Snider", "I was looking for a good friend who needed an extremely large tree taken down. Over the past year, 2 trees came down during storms and did quite a bit of damage to her property. Lee Friend’s Tree Service was reasonable and professional. She was extremely pleased and I so grateful we chose them! Thank you for doing good business!"),
    ("JOSEPH KROPSCH", "These guys are absolute PROS – They Rock! Everything was done with perfection and care for our home and property. I would Highly recommend Cornbread and his crew to anyone needing a High Risk tree removal. Thank you guys so much!"),
    ("Elaina D", "We’ve used these guys twice and both times they have done a fantastic job, going above and beyond what was requested. They are friendly and do excellent work. Thank you!!!"),
    ("Jason Galofaro", "Cornbread and another crew came together and did a great safe job for us 6-20-24 , we will be using lee friends tree service again thanks again to all!"),
    ("Gail Silis", "We could not be happier. Excellent job done at an excellent price."),
    ("Celes Ros", "Service starts with the telephone call to the business, Lisa and Jennifer are so professional, welcoming and courteous they are the windows of what great service you will receive from Lee Friends Tree Service. The very skilled workers are amazing.they are professional, they are patient and thorough, most importantly they do not leave a mess. I am looking forward to having them come back in the future to remove more trees and I do highly recommend their services. Thank you!"),
    ("R Lynn", "I reached out to them for Stump Removal based on other good reviews. Great price compared to another company. Very nice people, responsive, contacted me about their arrival time and Derrick did a great job on removal of both of the stumps. Took about an hour to remove and clean-up area to remove two medium sized stumps. I wouldn’t hesitate to use them again."),
    ("Brian97cobra", "I contacted Lee’s tree service and they were actually able to come same day and give me a quote. i did call and have 2 other quotes that were higher for all of the trees i needed limbs removed. They had scheduled to come friday to do the work but had finished up a job early and called me and came today. The work they performed was Exceptional and did an Amazing job. I honestly cant say enough good things about this company. i have already recommended them to 2 other people i know. Great customer service. Great prices. Great service work. Great overall company. A+++ would recommend them to anyone"),
    ("Ash Khan", "Have used their tree services on multiple occassions and have always been completely satisfied. Getting ready to call them again. Keep up the good work!"),
]
HOME_REVIEWS = ["Beth Ediger", "Gray McKenzie", "Tom McCoy"]


# ---------------------------------------------------------------- schema
def hours_spec():
    out = []
    for _, _, days, o, c in HOURS:
        if days:
            out.append({"@type": "OpeningHoursSpecification", "dayOfWeek": days, "opens": o, "closes": c})
    return out


def business_schema():
    return {
        "@type": "LocalBusiness",
        "@id": SITE + "/#business",
        "name": B["name"],
        "url": SITE + "/",
        "telephone": B["phone"],
        "description": plain(HOME_FIRST),
        "foundingDate": B["founded"],
        "address": {"@type": "PostalAddress", "addressLocality": B["city"], "addressRegion": B["region"],
                    "postalCode": B["zip"], "addressCountry": "US"},
        "geo": {"@type": "GeoCoordinates", "latitude": B["geo"][0], "longitude": B["geo"][1]},
        "openingHoursSpecification": hours_spec(),
        "areaServed": [{"@type": "City", "name": f"{t}, GA"} for t in TOWNS],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Tree services",
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": s["name"],
                                 "url": f"{SITE}/services/{s['slug']}/"}} for s in SERVICES],
        },
        "employee": {"@id": SITE + "/about/#arborist"},
        "sameAs": [B["facebook"], B["maps"]],
    }


def arborist_schema():
    return {
        "@type": "Person",
        "@id": SITE + "/about/#arborist",
        "name": B["arborist"],
        "jobTitle": "ISA Certified Arborist",
        "worksFor": {"@id": SITE + "/#business"},
        "hasCredential": {"@type": "EducationalOccupationalCredential", "name": "ISA Certified Arborist",
                          "credentialCategory": "certification",
                          "recognizedBy": {"@type": "Organization", "name": "International Society of Arboriculture",
                                           "url": "https://www.isa-arbor.com/"}},
        "knowsAbout": ["Tree removal", "Tree pruning", "Storm damage", "Arboriculture"],
    }


def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in faqs]}


def crumbs_schema(trail):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(trail)]}


# ---------------------------------------------------------------- page chrome
HOME_FIRST = (f"Lee Friend's Tree Service is a family-owned tree service in Loganville, GA, with an ISA Certified "
              f"Arborist on staff, serving Gwinnett, Walton, and the Metro Atlanta area since {B['founded']}.")

NAV = [("Services", "services/"), ("Service Areas", AREAS), ("Reviews", "testimonials/"), ("About", "about/"), ("FAQ", "faq/"), ("Contact", "contact/")]


def wordmark(p):
    return (f'<a class="wordmark" href="{p}" aria-label="{html.escape(B["name"])} home">'
            f'<span class="wm-top">Lee Friend’s</span><span class="wm-sub">Tree Service, Inc.</span></a>')


def header(p, current):
    cur = ' aria-current="page"'
    links = "".join(f'<li><a href="{p}{u}"{cur if u == current else ""}>{n}</a></li>' for n, u in NAV)
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap topbar-in">
  <span>{icon('pin')} Loganville, GA {B['zip']}</span>
  <span class="tb-hours">{icon('clock')} Mon–Fri 8–5 · Sat 9–5</span>
</div></div>
<header class="site-head"><div class="wrap head-in">
  {wordmark(p)}
  <nav class="nav" aria-label="Main">
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="nav-list">{icon('menu')}<span>Menu</span></button>
    <ul id="nav-list">{links}</ul>
  </nav>
  <a class="btn btn-call head-call" href="tel:{B['tel']}">{icon('phone')}<span>{B['phone']}</span></a>
</div></header>"""


def hours_dl():
    rows = "".join(f"<div><dt>{d}</dt><dd>{h}</dd></div>" for d, h, *_ in HOURS)
    return f'<dl class="hours">{rows}</dl>'


def footer(p):
    svc = "".join(f'<li><a href="{p}services/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)
    towns = "".join(f'<li><a href="{p}{u}/">{t}, GA</a></li>' for t, u in TOWN_PAGES.items())
    return f"""<footer class="site-foot">
  <div class="wrap foot-grid">
    <div class="foot-id">
      <p class="foot-name">{B['name']}</p>
      <p class="foot-tag">{B['tagline']}</p>
      <p>Family-owned tree service in Loganville, GA {B['zip']}. ISA Certified Arborist {B['arborist']} on staff. Residential and commercial.</p>
      <p><a class="foot-phone" href="tel:{B['tel']}">{B['phone']}</a></p>
      {hours_dl()}
      <p class="small">{confirm(C_HOURS)}</p>
      <p class="foot-links"><a class="social" href="{B['facebook']}" rel="noopener">{icon('facebook')} Facebook</a>
         <a class="social" href="{B['maps']}" rel="noopener">{icon('pin')} Google Maps</a>
         <a class="social" href="{B['review']}" rel="noopener">{icon('badge')} Leave us a review</a></p>
    </div>
    <div><p class="foot-h">Services</p><ul>{svc}</ul></div>
    <div><p class="foot-h">Towns</p><ul>{towns}<li><a href="{p}{AREAS}">All service areas</a></li></ul>
      <p class="foot-h">Company</p><ul><li><a href="{p}about/">About &amp; credentials</a></li><li><a href="{p}testimonials/">Customer reviews</a></li><li><a href="{p}faq/">FAQ</a></li><li><a href="{p}contact/">Contact &amp; free estimate</a></li></ul></div>
  </div>
  <div class="wrap foot-base"><p>© {TODAY[:4]} {B['name']} · Private preview, not the live site.</p></div>
</footer>
<a class="callbar" href="tel:{B['tel']}">{icon('phone')}<span>Call {B['phone']}</span></a>"""


def page(path, title, meta, body, current="", schema_extra=(), trail=None):
    depth = path.count("/")
    p = "../" * depth
    graph = [business_schema(), arborist_schema(), *schema_extra]
    if trail:
        graph.append(crumbs_schema(trail))
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    canon = SITE + "/" + path.replace("index.html", "")
    crumbs = ""
    if trail and len(trail) > 1:
        items = "".join(
            (f'<li><a href="{p}{u.lstrip("/")}">{n}</a></li>' if i < len(trail) - 1 else f'<li aria-current="page">{n}</li>')
            for i, (n, u) in enumerate(trail))
        crumbs = f'<nav class="crumbs wrap" aria-label="Breadcrumb"><ol>{items}</ol></nav>'
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(meta)}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(meta)}">
<meta property="og:url" content="{canon}">
<meta name="theme-color" content="#1d3a29">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{p}assets/fonts/zilla-slab-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{p}assets/fonts/public-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{p}assets/site.css">
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
{header(p, current)}
{crumbs}
<main id="main">
{body.replace('{P}', p)}
</main>
{footer(p)}
<script src="{p}assets/site.js" defer></script>
</body>
</html>
"""
    # Folder links point at index.html so pages also work opened from disk or on hosts without directory indexes.
    doc = re.sub(r'href="((?:\.\./)*[\w./-]*/)?((?:#[\w-]+)?)"',
                 lambda m: m.group(0) if m.group(1) is None else f'href="{m.group(1)}index.html{m.group(2)}"', doc)
    doc = doc.replace('href=""', 'href="index.html"')
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc)
    PAGES.append((path, title, meta))


PAGES = []


# ---------------------------------------------------------------- shared blocks
def photo(alt, note, cls=""):
    """Placeholder until real job photos arrive. Most photos on the current site are stock, so none are reused as job photos."""
    return (f'<figure class="photo-slot {cls}"><div class="ph" role="img" aria-label="{html.escape(alt)}">{icon("camera")}</div>'
            f'<figcaption>{confirm(note)}<span class="alt-note">Alt text ready: “{html.escape(alt)}”</span></figcaption></figure>')


def review_tag(name, text):
    return (f'<li class="tag"><span class="tag-hole" aria-hidden="true"></span><blockquote><p>{html.escape(text)}</p></blockquote>'
            f'<p class="tag-who"><strong>{html.escape(name)}</strong><span>Google review</span></p></li>')


def faq_block(faqs, heading="Questions customers ask"):
    items = "".join(f'<details class="qa"><summary><h3>{html.escape(q)}</h3></summary><p>{a}</p></details>' for q, a in faqs)
    return f'<section class="band band-kraft"><div class="wrap narrow"><h2>{heading}</h2><div class="qa-list">{items}</div></div></section>'


def towns_block(service=None, intro=None):
    lis = "".join(
        f'<li><a href="{{P}}{TOWN_PAGES[t]}/">{t}</a></li>' if t in TOWN_PAGES else f"<li>{t}</li>" for t in TOWNS)
    q = f"Which towns do you serve for {service.lower()}?" if service else "Which towns do you serve?"
    a = intro or ("We serve Loganville and 27 nearby towns across Gwinnett, Walton, and Metro Atlanta.")
    return f"""<section class="band band-pine towns"><div class="wrap">
  <h2>{q}</h2>
  <p class="answer">{a}</p>
  <ul class="town-list">{lis}</ul>
  <p><a class="link-light" href="{{P}}{AREAS}">See all service areas</a></p>
</div></section>"""


def cta_block(heading="Have a tree that needs looking at?"):
    return f"""<section class="cta"><div class="wrap cta-in">
  <h2>{heading}</h2>
  <p>Call and talk to the family that runs the business. Estimates are free, and we can often come out the same day.</p>
  <div class="cta-actions">
    <a class="btn btn-call btn-big" href="tel:{B['tel']}">{icon('phone')}<span>Call {B['phone']}</span></a>
    <a class="btn btn-ghost" href="{{P}}contact/#quote">Request a free estimate</a>
  </div>
</div></section>"""


def seal(top, mid, bottom, cls="", note=""):
    return (f'<li class="seal {cls}"><span class="seal-ring"><span class="seal-top">{top}</span>'
            f'<span class="seal-mid">{mid}</span><span class="seal-bot">{bottom}</span></span>{note}</li>')


def cred_strip():
    return f"""<section class="creds" aria-labelledby="creds-h"><div class="wrap">
  <h2 id="creds-h" class="sr-only">Credentials</h2>
  <ul class="seal-row">
    {seal('ISA', 'Certified Arborist', B['arborist'], 'seal-a')}
    {seal('Fully', 'Licensed &amp; Insured', 'Residential · Commercial', 'seal-b', confirm(C_INSURED))}
    {seal('BBB', 'Profile', 'Rating', 'seal-c seal-pending', confirm("BBB profile: does the company have one? If not, remove this seal"))}
    {seal('Since', B['founded'], 'Loganville, GA', 'seal-d', confirm(C_YEAR))}
  </ul>
</div></section>"""


TREE_SVG = """<svg class="hero-tree" viewBox="0 0 480 420" aria-hidden="true" focusable="false">
  <path class="canopy" d="M70 228c-34-6-52-36-40-64 8-20 28-30 48-28-4-30 18-56 48-60 10-30 42-48 74-40 18-22 52-28 78-12 26-14 60-6 74 20 32-2 58 22 58 52 26 8 40 34 32 60 18 18 18 48-2 64-6 28-34 44-62 38-14 20-42 28-64 18-20 14-48 14-66 0-22 12-50 10-66-6-24 8-50 0-62-18-26 4-48-6-50-24Z"/>
  <g class="limbs" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="M220 330c-2-40-6-70-20-96-16-30-44-52-82-64M206 238c-6-30-2-62 12-92M224 300c10-44 34-78 74-100 22-12 44-16 70-12M298 200c4-26-2-52-16-74M150 182c-14-18-34-28-60-30M262 236c26 2 48 12 66 30M180 214c-22 4-44 16-60 34"/>
  </g>
  <path class="trunk" d="M196 392c14-30 18-64 14-104l28-4c-4 44 2 80 18 108Z"/>
  <path class="ground" d="M60 396c50-10 104-14 160-14s110 4 160 14"/>
</svg>"""


# ---------------------------------------------------------------- HOME
def build_home():
    svc_rows = "".join(f"""<li class="board-row">
      <span class="board-ico">{icon(s['icon'])}</span>
      <div class="board-text"><h3><a href="{{P}}services/{s['slug']}/">{s['name']}</a></h3><p>{s['line']}</p></div>
      <a class="board-go" href="{{P}}services/{s['slug']}/" aria-label="{s['name']} details">Details</a>
    </li>""" for s in SERVICES)
    why = [
        ("family", "Family-run since " + B["founded"], "A husband-and-wife team started the company and still runs it. You talk to the owners, not a call center."),
        ("badge", "ISA Certified Arborist on staff", f"{B['arborist']} is an ISA Certified Arborist, so decisions about pruning, saving, or removing a tree rest on real training."),
        ("shield", "Licensed and insured", "Your home and our crew are protected on every job, and we leave no mess behind. " + confirm(C_INSURED)),
        ("recycling", "Wood that gets a second life", "Instead of the landfill, branches become mulch, logs go to local mills, and leftover hardwood becomes firewood. Wood chips are free."),
        ("bolt", "Free, same-day estimates", "Estimates are free and no-obligation, and customers often tell us we came out the same day they called."),
    ]
    why_html = "".join(f'<li>{icon(i, "ico why-ico")}<div><h3>{h}</h3><p>{t}</p></div></li>' for i, h, t in why)
    rev = "".join(review_tag(n, q) for n, q in REVIEWS if n in HOME_REVIEWS)
    body = f"""
<section class="hero"><div class="wrap hero-in">
  <div class="hero-copy">
    <h1>{HOME_FIRST}</h1>
    <p class="hero-confirm">{confirm(C_YEAR)} {confirm(C_ARBORIST)}</p>
    <p class="hero-sub">Tree removal, trimming, storm clean-up, stump grinding, and seasoned firewood for homes and businesses.</p>
    <div class="hero-actions">
      <a class="btn btn-call btn-big" href="tel:{B['tel']}">{icon('phone')}<span>Call {B['phone']}</span></a>
      <a class="btn btn-ghost" href="{{P}}contact/#quote">Request a free estimate</a>
    </div>
  </div>
  <div class="hero-art">
    {TREE_SVG}
    <div class="stamp" aria-hidden="true"><span>Since</span><strong>{B['founded']}</strong><span>Loganville GA</span></div>
  </div>
</div></section>
{cred_strip()}
<section class="band band-kraft" id="services"><div class="wrap">
  <div class="section-head">
    <h2>What tree services do you offer?</h2>
    <p class="answer">We remove, trim, and prune trees, clear storm damage, grind stumps, recycle wood, and sell seasoned firewood, for homes and businesses.</p>
  </div>
  <ul class="board">{svc_rows}</ul>
</div></section>
<section class="band why"><div class="wrap why-grid">
  <div class="why-head">
    <h2>Why choose Lee Friend's Tree Service?</h2>
    <p class="answer">Because a family that has done this work since {B['founded']} runs every job, with a certified arborist making the calls about your trees.</p>
    {photo("Lee Friend's Tree Service crew and truck on a job in Loganville GA", "Real crew or family photo. Most current-site photos are stock; the one real crew shot is home-imge-1.webp (loader carrying a log)")}
  </div>
  <ul class="why-list">{why_html}</ul>
</div></section>
<section class="band band-kraft reviews"><div class="wrap">
  <div class="section-head">
    <h2>What do customers say about Lee Friend's?</h2>
    <p class="answer">Customers on Google mention fair prices, careful work in tight spots, fast response, and crews that clean up after themselves.</p>
  </div>
  <ul class="tags">{rev}</ul>
  <p class="more"><a href="{{P}}testimonials/">Read all 12 customer reviews</a></p>
</div></section>
{towns_block()}
{cta_block("Need a tree looked at? Call the family.")}
"""
    page("index.html", "Tree Service in Loganville, GA | Lee Friend's Tree Service, Inc.",
         "Family-owned tree service in Loganville, GA with an ISA Certified Arborist on staff. Tree removal, trimming, storm damage, stump grinding, firewood. (770) 466-5112.",
         body, current="", trail=[("Home", "/")])


# ---------------------------------------------------------------- SERVICE PAGES
def build_services():
    for s in SERVICES:
        when = "".join(f"<li>{icon('check')}<span>{w}</span></li>" for w in s["when"])
        steps = "".join(f'<li><h3>{h}</h3><p>{t}</p></li>' for h, t in s["steps"])
        others = "".join(f'<li><a href="{{P}}services/{o["slug"]}/">{icon(o["icon"])}<span>{o["name"]}</span></a></li>'
                         for o in SERVICES if o is not s)
        n = s["name"].lower()
        svc_ld = {
            "@type": "Service", "@id": f"{SITE}/services/{s['slug']}/#service", "name": s["name"],
            "serviceType": s["name"], "description": plain(s["answer"]),
            "provider": {"@id": SITE + "/#business"},
            "areaServed": [{"@type": "City", "name": f"{t}, GA"} for t in TOWNS],
            "url": f"{SITE}/services/{s['slug']}/",
        }
        body = f"""
<section class="page-hero"><div class="wrap page-hero-in">
  <div>
    <h1>{s['name']} in Loganville, GA</h1>
    <p class="lead">{s['answer']}</p>
    <div class="hero-actions">
      <a class="btn btn-call btn-big" href="tel:{B['tel']}">{icon('phone')}<span>Call {B['phone']}</span></a>
      <a class="btn btn-ghost" href="{{P}}contact/#quote">Request a free estimate</a>
    </div>
  </div>
  <div class="page-hero-ico">{icon(s['icon'], 'ico big-ico')}</div>
</div></section>
<section class="band"><div class="wrap two-col">
  <div class="prose">
    <h2>What is {n}?</h2>
    <p class="answer">{s['what']}</p>
    <h3>What's included</h3>
    <ul class="includes">{"".join(f"<li>{x}</li>" for x in s["includes"])}</ul>
    <h2>When do you need {n}?</h2>
    <p class="answer">Call when a tree shows any of these signs, or if you're unsure and want an arborist's opinion.</p>
    <ul class="checks">{when}</ul>
  </div>
  {photo(f"{s['name']} by Lee Friend's Tree Service in Loganville GA", f"A real {n} job photo (the current site's {n} photo is stock)")}
</div></section>
<section class="band band-pine"><div class="wrap">
  <h2>How does {n} work with Lee Friend's?</h2>
  <p class="answer">Here's what happens from your first call to the finished job.</p>
  <ol class="steps">{steps}</ol>
</div></section>
{faq_block(s['faq'], f"Questions about {n}")}
<section class="band"><div class="wrap">
  <h2>What other tree services do you offer?</h2>
  <p class="answer">Most jobs combine a few of these. Ask about any of them when you call.</p>
  <ul class="svc-links">{others}</ul>
  <p class="more">Have another question? Read the <a href="{{P}}faq/">tree service FAQ</a> or learn <a href="{{P}}about/">about our family and arborist</a>.</p>
</div></section>
{towns_block(s['name'], f"We offer {n} in Loganville and these nearby towns across Gwinnett, Walton, and Metro Atlanta.")}
{cta_block(f"Ready to talk about {n}?")}
"""
        page(f"services/{s['slug']}/index.html", s["title"], s["meta"], body, current="services/",
             schema_extra=[svc_ld, faq_schema(s["faq"])],
             trail=[("Home", "/"), ("Services", "/services/"), (s["name"], f"/services/{s['slug']}/")])

    rows = "".join(f"""<li class="board-row">
      <span class="board-ico">{icon(s['icon'])}</span>
      <div class="board-text"><h2 class="h3"><a href="{{P}}services/{s['slug']}/">{s['name']}</a></h2><p>{s['answer']}</p></div>
      <a class="board-go" href="{{P}}services/{s['slug']}/" aria-label="{s['name']} details">Details</a>
    </li>""" for s in SERVICES)
    body = f"""
<section class="page-hero"><div class="wrap">
  <h1>Tree Services in Loganville, GA</h1>
  <p class="lead">Lee Friend's Tree Service offers six services for homes and businesses in Loganville, GA and the Metro Atlanta area: tree removal, tree trimming and pruning, storm damage tree removal, stump grinding, eco-friendly wood recycling, and firewood sales.</p>
</div></section>
<section class="band band-kraft"><div class="wrap"><ul class="board">{rows}</ul></div></section>
{towns_block()}
{cta_block()}
"""
    page("services/index.html", "Tree Services in Loganville, GA | Lee Friend's Tree Service",
         "Tree removal, trimming and pruning, storm damage, stump grinding, wood recycling, and firewood in Loganville, GA. Family-owned. Call (770) 466-5112.",
         body, current="services/", trail=[("Home", "/"), ("Services", "/services/")])


# ---------------------------------------------------------------- ABOUT
def build_about():
    body = f"""
<section class="page-hero"><div class="wrap">
  <h1>About Lee Friend's Tree Service</h1>
  <p class="lead">Lee Friend's Tree Service, Inc. is a family-owned tree company in Loganville, GA, founded in {B['founded']} by a husband-and-wife team and still run by them today, with ISA Certified Arborist {B['arborist']} on staff. {confirm(C_YEAR)}</p>
</div></section>
<section class="band"><div class="wrap two-col">
  <div class="prose">
    <h2>How did Lee Friend's Tree Service start?</h2>
    <p class="answer">The company began in {B['founded']} as a passion project for a husband-and-wife team who loved working outdoors and wanted to build something meaningful.</p>
    <p>More than 30 years later, it has grown into a respected name in tree care, still offering direct, personal service from a local team that works for homeowners and businesses alike. Loganville is home, and the company has built its reputation here on reliable results and honest advice. {confirm("Owners' names and a few lines of the family story in their own words (who Lee is, how they started, family members in the business)")}</p>
    <h2>What makes the company different?</h2>
    <p class="answer">A certified arborist on staff, wood recycling on every job, and a mascot dog that adds personality to the crew.</p>
    <p>Every job, big or small, gets the same attention to detail. Branches become mulch, hardwood and pine logs go to local mills, and leftover hardwood is split and seasoned into firewood. {confirm("The mascot dog's name and a photo")}</p>
    <h2>Who will I work with?</h2>
    <p class="answer">The family that owns the business, and a crew customers often mention by name.</p>
    <p>In their reviews, customers thank Lisa and Jennifer for a welcoming first phone call, and crew members Cornbread, Derrick, and lead man John McGowan for careful, professional work. <a href="{{P}}testimonials/">Read the reviews</a>. {confirm("Roles of Lisa, Cornbread, Derrick, and John McGowan, and OK to name them on the site")}</p>
  </div>
  {photo("Owners of Lee Friend's Tree Service, the husband-and-wife team, in Loganville GA", "Photo of the owners")}
</div></section>
<section class="band band-kraft" id="arborist"><div class="wrap arborist">
  {photo(f"{B['arborist']}, ISA Certified Arborist at Lee Friend's Tree Service in Loganville GA", "Photo of Jennifer Perrone", "portrait")}
  <div class="prose">
    <h2>Who is your certified arborist?</h2>
    <p class="answer">{B['arborist']} is the ISA Certified Arborist at Lee Friend's Tree Service. {confirm(C_ARBORIST)}</p>
    <p>An ISA Certified Arborist has passed the International Society of Arboriculture's exam covering tree biology, pruning, diagnosis, and safe work practices, and keeps the credential current with continuing education. Jennifer's job is to look at your trees and give an honest answer about whether they should be pruned, treated, or removed.</p>
    <p>{confirm("Jennifer's bio: years of experience, ISA certification number, specialties, and anything she'd like customers to know")}</p>
    <p>Jennifer also appears in public listings as a member of the Georgia Arborist Association and on the City of Alpharetta's list of authorized tree removal contractors. {confirm("Confirm the Georgia Arborist Association membership and Alpharetta contractor listing are current before showing them")}</p>
    <p class="verify">You can verify her ISA credential yourself at <a href="https://www.treesaregood.org/findanarborist/verify" rel="noopener">treesaregood.org</a>, the International Society of Arboriculture's public site.</p>
  </div>
</div></section>
<section class="band band-pine" id="credentials"><div class="wrap">
  <h2>What credentials does Lee Friend's Tree Service have?</h2>
  <p class="answer">An ISA Certified Arborist on staff, licensed and insured, and in business since {B['founded']}.</p>
  <ul class="cred-list">
    <li>{icon('badge')}<div><h3>ISA Certified Arborist</h3><p>{B['arborist']}. <a class="link-light" href="https://www.treesaregood.org/findanarborist/verify" rel="noopener">Verify at treesaregood.org</a>. {confirm("Direct link to Jennifer Perrone's ISA profile or certification number")}</p></div></li>
    <li>{icon('shield')}<div><h3>Licensed &amp; insured</h3><p>{confirm(C_INSURED)}</p></div></li>
    <li>{icon('check')}<div><h3>Better Business Bureau</h3><p>{confirm("BBB profile URL and rating, or remove this item if there is no profile")}</p></div></li>
    <li>{icon('family')}<div><h3>Tree Care Industry Association (TCIA)</h3><p>{confirm("TCIA membership: confirm, or remove this item")}</p></div></li>
  </ul>
</div></section>
{cta_block("Want an arborist's opinion on your trees?")}
"""
    page("about/index.html", "About Lee Friend's Tree Service | Family Tree Service in Loganville, GA",
         "Meet the family behind Lee Friend's Tree Service in Loganville, GA, and ISA Certified Arborist Jennifer Perrone. Credentials, story, and how to verify.",
         body, current="about/", trail=[("Home", "/"), ("About", "/about/")])


# ---------------------------------------------------------------- FAQ
def build_faq():
    items = "".join(f'<div class="qa-open"><h2>{html.escape(q)}</h2><p>{a}</p></div>' for q, a in GENERAL_FAQ)
    body = f"""
<section class="page-hero"><div class="wrap">
  <h1>Tree Service FAQ for Loganville, GA</h1>
  <p class="lead">Straight answers to the questions homeowners in Loganville and Metro Atlanta ask most about tree removal, insurance, stump grinding, and firewood. Don't see yours? Call {B['phone']}.</p>
</div></section>
<section class="band band-kraft"><div class="wrap narrow faq-page">{items}
  <p class="more">More detail on each service: {", ".join(f'<a href="{{P}}services/{s["slug"]}/">{s["name"]}</a>' for s in SERVICES)}.</p>
</div></section>
{cta_block("Still have a question? Ask us.")}
"""
    page("faq/index.html", "Tree Service FAQ | Lee Friend's Tree Service, Loganville, GA",
         "Answers about tree removal cost in Loganville, GA, insurance for fallen trees, ISA certified arborists, stump grinding, storm damage, and firewood delivery.",
         body, current="faq/", schema_extra=[faq_schema(GENERAL_FAQ)], trail=[("Home", "/"), ("FAQ", "/faq/")])


# ---------------------------------------------------------------- SERVICE AREAS
def build_areas():
    feature = "".join(f'<li><a href="{{P}}{u}/"><span class="fa-town">{t}, GA</span><span class="fa-go">Tree service in {t}</span></a></li>'
                      for t, u in TOWN_PAGES.items())
    allt = "".join(f"<li>{t}, GA</li>" for t in TOWNS)
    body = f"""
<section class="page-hero"><div class="wrap">
  <h1>Tree Service Areas Around Loganville, GA</h1>
  <p class="lead">Lee Friend's Tree Service is based in Loganville, GA and serves 28 towns across Gwinnett County, Walton County, and the Metro Atlanta area.</p>
</div></section>
<section class="band band-kraft"><div class="wrap">
  <h2>Where are you based?</h2>
  <p class="answer">In Loganville, GA {B['zip']}, on the Walton and Gwinnett County line. {confirm(C_STREET)}</p>
  <ul class="feature-towns">{feature}</ul>
</div></section>
<section class="band"><div class="wrap">
  <h2>Which towns do you serve?</h2>
  <p class="answer">All of these, for every service we offer.</p>
  <ul class="all-towns">{allt}</ul>
  <p class="more">Not sure if you're in range? Call {B['phone']}. <a href="{B['maps']}" rel="noopener">Find us on Google Maps</a>.</p>
</div></section>
<section class="band band-pine"><div class="wrap">
  <h2>What services do you offer in these towns?</h2>
  <p class="answer">Every service, everywhere we work.</p>
  <ul class="svc-links light">{"".join(f'<li><a href="{{P}}services/{s["slug"]}/">{icon(s["icon"])}<span>{s["name"]}</span></a></li>' for s in SERVICES)}</ul>
</div></section>
{cta_block()}
"""
    page(AREAS + "index.html", "Tree Service Areas Near Loganville, GA | Lee Friend's Tree Service",
         "Lee Friend's Tree Service serves Loganville, Grayson, Snellville, Monroe, and 24 more towns in Gwinnett, Walton, and Metro Atlanta. Call (770) 466-5112.",
         body, current=AREAS, trail=[("Home", "/"), ("Service Areas", "/" + AREAS)])

    for t, slug in TOWN_PAGES.items():
        d = TOWN_DETAIL[t]
        secs = "".join(f'<h2>{q}</h2><p class="answer">{a}</p><p>{x}</p>' for q, a, x in d["sections"])
        others = "".join(f'<li><a href="{{P}}{u}/">{o}, GA</a></li>' for o, u in TOWN_PAGES.items() if o != t)
        svcs = "".join(f'<li><a href="{{P}}services/{s["slug"]}/">{icon(s["icon"])}<span>{s["name"]} in {t}</span></a></li>' for s in SERVICES)
        body = f"""
<section class="page-hero"><div class="wrap">
  <h1>{d['h1']}</h1>
  <p class="lead">{d['answer']}</p>
  <div class="hero-actions">
    <a class="btn btn-call btn-big" href="tel:{B['tel']}">{icon('phone')}<span>Call {B['phone']}</span></a>
    <a class="btn btn-ghost" href="{{P}}contact/#quote">Request a free estimate</a>
  </div>
</div></section>
<section class="band"><div class="wrap two-col">
  <div class="prose">{secs}</div>
  {photo(f"Lee Friend's Tree Service crew working on a tree in {t} GA", f"A real job photo from {t}")}
</div></section>
<section class="band band-pine"><div class="wrap">
  <h2>Which tree services do you offer in {t}?</h2>
  <p class="answer">All six of our services are available in {t}.</p>
  <ul class="svc-links light">{svcs}</ul>
</div></section>
{faq_block(d['faq'], f"Questions from {t} customers")}
<section class="band"><div class="wrap">
  <h2>Do you serve towns near {t}?</h2>
  <p class="answer">Yes. We serve 28 towns around Loganville, including these.</p>
  <ul class="feature-towns small">{others}<li><a href="{{P}}{AREAS}"><span class="fa-town">All service areas</span></a></li></ul>
</div></section>
{cta_block(f"Need tree work in {t}?")}
"""
        page(f"{slug}/index.html", d["title"], d["meta"], body, current=AREAS,
             schema_extra=[faq_schema(d["faq"])],
             trail=[("Home", "/"), ("Service Areas", "/" + AREAS), (f"{t}, GA", f"/{slug}/")])


# ---------------------------------------------------------------- REVIEWS
def build_testimonials():
    tags = "".join(review_tag(n, q) for n, q in REVIEWS)
    body = f"""
<section class="page-hero"><div class="wrap">
  <h1>Customer Reviews of Lee Friend's Tree Service</h1>
  <p class="lead">Customers on Google give Lee Friend's Tree Service five stars for fair prices, careful work, fast response, and clean job sites. Here are 12 of their reviews, word for word.</p>
</div></section>
<section class="band band-kraft"><div class="wrap">
  <ul class="tags tags-all">{tags}</ul>
  <p class="more">Worked with us? <a href="{B['review']}" rel="noopener">Leave a review on Google</a> or <a href="{B['maps']}" rel="noopener">see us on Google Maps</a>.</p>
</div></section>
{cta_block("Ready to be our next happy customer?")}
"""
    page("testimonials/index.html", "Customer Reviews | Lee Friend's Tree Service, Loganville, GA",
         "Read 12 Google reviews of Lee Friend's Tree Service in Loganville, GA: fair prices, careful tree removal in tight spots, fast storm response, and clean job sites.",
         body, current="testimonials/", trail=[("Home", "/"), ("Reviews", "/testimonials/")])


# ---------------------------------------------------------------- CONTACT
def build_contact():
    svc_opts = "".join(f"<option>{s['name']}</option>" for s in SERVICES)
    body = f"""
<section class="page-hero"><div class="wrap">
  <h1>Contact Lee Friend's Tree Service in Loganville, GA</h1>
  <p class="lead">The fastest way to reach us is to call {B['phone']}. You can also send the quote form below and we'll call you back.</p>
</div></section>
<section class="band band-kraft"><div class="wrap contact-grid">
  <div class="contact-card">
    <h2>How do I reach you?</h2>
    <p class="answer">Call <a class="big-phone" href="tel:{B['tel']}">{B['phone']}</a></p>
    <h3>Hours</h3>
    {hours_dl()}
    <p class="small">{confirm(C_HOURS)}</p>
    <h3>Location</h3>
    <p>Loganville, GA {B['zip']} {confirm(C_STREET)}</p>
    <h3>Service area</h3>
    <p>Gwinnett, Walton, and the Metro Atlanta area. <a href="{{P}}{AREAS}">See all 28 towns</a>.</p>
    <h3>Email</h3>
    <p><a href="mailto:{B['email']}">{B['email']}</a> {confirm("Show this email on the Contact page? It appears on the current Suwanee page")}</p>
    <p class="foot-links"><a class="social dark" href="{B['facebook']}" rel="noopener">{icon('facebook')} Facebook</a>
       <a class="social dark" href="{B['maps']}" rel="noopener">{icon('pin')} Google Maps</a></p>
  </div>
  <form class="quote" id="quote" novalidate>
    <h2>Request a free estimate</h2>
    <p class="form-note">Tell us about the job and we'll call you back. {confirm("Where quote requests should be delivered (email address or form service) before launch")}</p>
    <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" required></div>
    <div class="field"><label for="f-phone">Phone number</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required><p class="err" id="e-phone" hidden>Enter a phone number so we can call you back.</p></div>
    <div class="field"><label for="f-email">Email <span class="opt">(optional)</span></label><input id="f-email" name="email" type="email" autocomplete="email"></div>
    <div class="field"><label for="f-town">Town</label><input id="f-town" name="town" autocomplete="address-level2" list="town-list"><datalist id="town-list">{"".join(f'<option value="{t}">' for t in TOWNS)}</datalist></div>
    <div class="field"><label for="f-svc">What do you need?</label><select id="f-svc" name="service"><option value="">Choose a service</option>{svc_opts}<option>Not sure yet</option></select></div>
    <div class="field"><label for="f-msg">Tell us about the trees</label><textarea id="f-msg" name="message" rows="4" placeholder="For example: a big oak leaning toward the garage after last night's storm."></textarea></div>
    <button class="btn btn-call btn-big" type="submit">Send my estimate request</button>
    <p class="form-status" role="status" aria-live="polite"></p>
  </form>
</div></section>
"""
    page("contact/index.html", "Contact & Free Quote | Lee Friend's Tree Service, Loganville, GA",
         "Call Lee Friend's Tree Service at (770) 466-5112 or request a quote online. Loganville, GA tree service, open Mon–Fri 8–5 and Sat 9–5.",
         body, current="contact/", trail=[("Home", "/"), ("Contact", "/contact/")])


# ---------------------------------------------------------------- extras
def build_extras():
    urls = "".join(
        f"  <url><loc>{SITE}/{p.replace('index.html', '')}</loc><lastmod>{TODAY}</lastmod></url>\n" for p, *_ in PAGES)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    (ROOT / "robots.txt").write_text(
        "# PRIVATE PREVIEW: blocks all crawlers. At launch replace with:\n"
        "#   User-agent: *\n#   Allow: /\n#   Sitemap: " + SITE + "/sitemap.xml\n"
        "User-agent: *\nDisallow: /\n")
    red = ["# Redirects to set up at launch", "",
           "These current-site URLs are not in the new site. Point each one (301 redirect) where shown so links and rankings carry over.",
           "All other current URLs (services, /about/, /faq/, /contact/, /testimonials/, /areas-we-serve/, /grayson-ga/) keep the same address.", ""]
    red += [f"- `{a}` → `{b}`" for a, b in REDIRECTS.items() if b]
    (ROOT / "REDIRECTS.md").write_text("\n".join(red) + "\n")
    lines = ["# [CONFIRM] checklist for Lee Friend's Tree Service", "",
             "Verify each item with the owner. Each one shows on the preview as a yellow [CONFIRM: ...] tag.", ""]
    lines += [f"{i}. {c}" for i, c in enumerate(CONFIRMS, 1)]
    (ROOT / "CONFIRM-LIST.md").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    build_home()
    build_services()
    build_about()
    build_faq()
    build_areas()
    build_testimonials()
    build_contact()
    build_extras()
    print(f"Built {len(PAGES)} pages, {len(CONFIRMS)} confirm items")
