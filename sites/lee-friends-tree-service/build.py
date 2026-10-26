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

C_YEAR = "Founding year: the current site says 1989, other listings say 1991. Pick one"
C_HOURS = "Business hours (the current Eco-Friendly page lists Saturday as closed)"
C_INSURED = "Licensed and insured: confirm, and list license or insurance details if the owner wants them shown"
C_ARBORIST = "Jennifer Perrone is still on staff as the ISA Certified Arborist"
C_STREET = "Show the street address (3474 Johnson Rd) publicly? If yes, it is added to every page and the schema"
C_ESTIMATES = "Free estimates: only the old Duluth page says estimates are free. Confirm before publishing"


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
SERVICES = [
    {
        "slug": "tree-removal", "name": "Tree Removal", "icon": "removal",
        "title": "Tree Removal in Loganville, GA | Lee Friend's Tree Service",
        "meta": "Safe removal of dead, leaning, and unwanted trees in Loganville, GA and Metro Atlanta, with an ISA Certified Arborist on staff. Call (770) 466-5112.",
        "line": "Dead, leaning, and unwanted trees taken down safely, piece by piece when they stand close to a house.",
        "answer": "Lee Friend's Tree Service removes hazardous, dead, and unwanted trees for homes and businesses in Loganville, GA and across Gwinnett, Walton, and Metro Atlanta. Our ISA Certified Arborist helps you decide whether a tree truly needs to come down.",
        "what": "Tree removal means cutting a tree down in controlled sections, lowering the pieces safely, and hauling the wood away. A tree with open space around it can sometimes be felled whole; a tree beside a house, fence, or driveway is taken down in pieces so nothing falls where it shouldn't.",
        "when": ["The tree is dead or dying, with bare limbs or peeling bark.",
                 "It leans toward your house, driveway, or a neighbor's property.",
                 "The trunk is cracked, split, or hollow.",
                 "A storm has damaged it beyond saving.",
                 "Roots are lifting a foundation, driveway, or sidewalk.",
                 "You need room for an addition, pool, or garden."],
        "steps": [("Call or request a quote", f"Call {B['phone']} or send the quote form with a few details about the tree."),
                  ("We look at the tree", "We check the tree, what's around it, and the safest way to take it down, then give you a price."),
                  ("The crew takes it down", "Large trees near buildings come down in sections, lowered with ropes so your lawn and roof stay protected."),
                  ("Clean-up and recycling", "We rake and blow the area clean. Branches become mulch, and good logs go to local mills or become firewood.")],
        "faq": [
            ("How much does tree removal cost in Loganville?",
             "It depends on the tree's size, where it stands, and how hard it is to reach, so we price each job after seeing the tree. " + confirm("Typical tree removal price range, if the owner wants one published")),
            ("Is stump grinding included with tree removal?",
             "Stump grinding is a separate service you can add to any removal. " + confirm("Whether stump grinding is quoted separately or bundled")),
            ("Can you remove a tree that's right next to my house?",
             "Yes. Trees close to houses are taken down in small sections and lowered with ropes, so pieces never drop onto the roof."),
            ("Do I need a permit to remove a tree?",
             "Some cities and counties in the Atlanta area require a permit for certain trees, while many homeowners in unincorporated areas don't need one. Check with your city before a large removal, and ask us if you're unsure. " + confirm("Whether Lee Friend's helps customers with tree removal permits")),
        ],
    },
    {
        "slug": "tree-trimming-pruning", "name": "Tree Trimming & Pruning", "icon": "trimming",
        "title": "Tree Trimming & Pruning in Loganville, GA | Lee Friend's Tree Service",
        "meta": "Tree trimming and pruning in Loganville, GA guided by an ISA Certified Arborist: dead limbs, roof clearance, and healthier, safer trees. Call (770) 466-5112.",
        "line": "Dead limbs out, roof and driveway cleared, and trees shaped to grow strong.",
        "answer": "Lee Friend's Tree Service trims and prunes trees for homes and businesses in Loganville, GA and the surrounding area, with an ISA Certified Arborist on staff. Good pruning removes dead and risky limbs and keeps a tree healthy for years.",
        "what": "Pruning is cutting specific branches for a reason: to remove dead or diseased wood, clear a roof or driveway, let in light, or fix a weak branch structure. Each cut is made at the right spot on the branch so the tree can seal the wound.",
        "when": ["Dead or broken branches hang over the house, deck, or driveway.",
                 "Limbs rub the roof or block gutters.",
                 "Branches crowd power lines to the house or the street.",
                 "The canopy is so thick that the lawn under it won't grow.",
                 "You want trees ready before storm season.",
                 "A young tree needs shaping so it grows a strong structure."],
        "steps": [("Call or request a quote", f"Call {B['phone']} or send the quote form and tell us which trees concern you."),
                  ("We look at each tree", "We point out dead wood, weak limbs, and clearance problems, and explain what we'd cut and why."),
                  ("Careful cuts", "The crew removes the chosen branches with clean cuts, roping larger limbs down so they don't damage what's below."),
                  ("Clean-up and recycling", "Every branch is chipped into mulch and the yard is left clean.")],
        "faq": [
            ("When is the best time to prune trees in Georgia?",
             "Late winter, while most trees are dormant, is a good time for routine pruning. Dead, broken, or dangerous limbs should come out any time of year."),
            ("Do you top trees?",
             "The International Society of Arboriculture (ISA) advises against topping because it weakens trees and causes fast, weak regrowth. Thinning and crown reduction are better ways to make a tree smaller. " + confirm("Confirm the crews do not top trees")),
            ("How often should trees be trimmed?",
             "Most mature yard trees benefit from a check every few years, and younger trees from more frequent shaping. Trees over a roof or driveway may need attention sooner."),
        ],
    },
    {
        "slug": "storm-damage-tree-removal", "name": "Storm Damage Tree Removal", "icon": "storm",
        "title": "Storm Damage Tree Removal in Loganville, GA | Lee Friend's Tree Service",
        "meta": "Storm-damaged and fallen tree removal in Loganville, GA, including clean-up and help coordinating with your insurance company. Call (770) 466-5112.",
        "line": "Fallen trees cleared off homes, cars, and driveways, with help coordinating your insurance claim.",
        "answer": "Lee Friend's Tree Service removes storm-damaged and fallen trees in Loganville, GA and across Gwinnett, Walton, and Metro Atlanta, and helps coordinate with your insurance company. Call (770) 466-5112 as soon as everyone is safe.",
        "what": "Storm damage tree removal is the clean-up after wind, ice, or lightning brings down a tree or big limbs. It covers trees on houses, cars, fences, and driveways, plus split or hanging limbs that could still fall.",
        "when": ["A tree or large limb has fallen on your house, garage, or car.",
                 "A downed tree blocks your driveway or street access.",
                 "Limbs are cracked and hanging in the canopy after a storm.",
                 "A tree is newly leaning, or the soil around its roots has lifted.",
                 "You need photos and documentation for an insurance claim."],
        "steps": [("Get safe, then call", f"Keep everyone away from the tree and any wires. If power lines are involved, call Georgia Power first. Then call us at {B['phone']}."),
                  ("We assess the damage", "We look at how the tree is resting and what it's pressing on, then plan a safe way to lift it off."),
                  ("Removal and clean-up", "The crew cuts and lifts the tree away in sections and clears fallen limbs and debris from the property."),
                  ("Insurance coordination", "We give you the details your insurance company asks for and help coordinate with them.")],
        "faq": [
            ("Does homeowners insurance cover a fallen tree?",
             "Usually yes, when a tree falls on a covered structure such as your house, garage, or fence because of a storm. Policies often don't pay to remove a tree that fell without hitting anything, or one that fell because it was already dead. Check your own policy, and we'll help coordinate with your insurance company."),
            ("What should I do first when a tree falls on my house?",
             "Get everyone out of the damaged part of the house and stay away from the tree and any downed wires. Call Georgia Power if lines are involved, take photos for your insurance company, then call us."),
            ("Do you handle emergency storm damage?",
             f"Yes. Call {B['phone']} and we'll get to you as fast as we can. " + confirm("After-hours and weekend emergency availability (an old Duluth page says 24/7)")),
        ],
    },
    {
        "slug": "stump-grinding", "name": "Stump Grinding", "icon": "stump",
        "title": "Stump Grinding in Loganville, GA | Lee Friend's Tree Service",
        "meta": "Stump grinding below ground level for homes and businesses in Loganville, GA and Metro Atlanta. Full stump removal available. Call (770) 466-5112.",
        "line": "Stumps ground below ground level so you can plant grass, mow, or build over the spot.",
        "answer": "Lee Friend's Tree Service grinds tree stumps below ground level for homes and businesses in Loganville, GA and the surrounding area. Full stump removal is also available if you want the stump gone entirely.",
        "what": "Stump grinding uses a machine with a spinning, toothed wheel to chew the stump into wood chips, below the level of the soil. The roots left underground slowly break down. Full stump removal pulls the stump and main roots out of the ground instead.",
        "when": ["An old stump is in the way of mowing.",
                 "You want to plant grass, a garden, or a new tree in that spot.",
                 "The stump is sprouting new shoots.",
                 "It's attracting termites, ants, or fungus.",
                 "You're getting ready to sell the house or build."],
        "steps": [("Call or request a quote", f"Call {B['phone']} or send the quote form. Tell us how many stumps and roughly how wide they are."),
                  ("We check the area", "We look for anything near the stump, like sprinkler lines or a fence, before grinding."),
                  ("Grinding", "The grinder cuts the stump down below ground level."),
                  ("Clean-up", "We tidy the area. " + confirm("What happens to stump grinding chips: left to fill the hole, or hauled away"))],
        "faq": [
            ("How long does stump grinding take?",
             "It depends on the stump's width and roots, and most single stumps are done in one visit. " + confirm("Typical time per stump, for a direct answer")),
            ("How deep do you grind a stump?",
             "We grind stumps below ground level so the spot can be covered with soil and grass. " + confirm("Typical grinding depth in inches")),
            ("What's the difference between stump grinding and stump removal?",
             "Grinding turns the stump into chips below the soil and leaves the roots to break down. Removal pulls the stump and main roots out entirely, which leaves a bigger hole but clears the spot completely."),
        ],
    },
    {
        "slug": "wood-recycling", "name": "Eco-Friendly Wood Recycling", "icon": "recycling",
        "title": "Eco-Friendly Wood Recycling in Loganville, GA | Lee Friend's Tree Service",
        "meta": "Lee Friend's Tree Service recycles the wood it cuts in Loganville, GA into mulch, lumber, and firewood, and offers free wood chips. Call (770) 466-5112.",
        "line": "The wood we cut becomes mulch, lumber, and firewood, and the wood chips are free.",
        "answer": "Lee Friend's Tree Service recycles the wood from its jobs in Loganville, GA instead of sending it to a landfill. Branches become mulch, good hardwood and pine logs go to local mills for lumber, leftover hardwood becomes firewood, and wood chips are free.",
        "what": "Wood recycling means every part of a tree we cut gets a second use. Small branches go through a chipper and become mulch. Larger hardwood and pine logs are taken to local sawmills. Hardwood that isn't milled is split and seasoned into firewood.",
        "when": ["You'd like your tree job to send as little as possible to the landfill.",
                 "You want free wood chips for garden beds, paths, or play areas.",
                 "You'd like seasoned firewood cut from local trees."],
        "steps": [("Chipping", "Branches and small limbs go through the chipper on site and become wood chips."),
                  ("Sorting the logs", "Straight hardwood and pine logs are set aside for local mills."),
                  ("To the mill", "Those logs are delivered to local mills and sawn into lumber."),
                  ("Firewood", "Leftover hardwood is split and seasoned for firewood sales.")],
        "faq": [
            ("Can I get free wood chips?",
             f"Yes, wood chips are free. Call {B['phone']} to ask. " + confirm("How free wood chips work: drop-off, pickup, minimum load, waiting list")),
            ("What happens to the wood from my trees?",
             "Branches become mulch, good hardwood and pine logs go to local mills for lumber, and leftover hardwood is split into firewood."),
            ("Do you sell mulch?",
             confirm("The current site mentions bagged mulch recycling. Confirm whether mulch is sold and how")),
        ],
    },
    {
        "slug": "firewood", "name": "Firewood Sales", "icon": "firewood",
        "title": "Firewood for Sale in Loganville, GA | Lee Friend's Tree Service",
        "meta": "Seasoned hardwood firewood for sale in Loganville, GA, with delivery available or pickup. Call Lee Friend's Tree Service at (770) 466-5112.",
        "line": "Seasoned, low-moisture hardwood, delivered or ready for pickup.",
        "answer": "Lee Friend's Tree Service sells seasoned hardwood firewood in Loganville, GA, with delivery available or pickup. The wood is cut from local trees and seasoned to low moisture so it lights easily and burns clean.",
        "what": "Seasoned firewood is wood that has been split and left to dry until most of its moisture is gone. Dry hardwood catches fire easily, burns hotter, and makes less smoke and creosote than green wood.",
        "when": ["You heat with a wood stove or fireplace.",
                 "You want firewood for a fire pit or outdoor kitchen.",
                 "You'd rather buy wood cut from local trees than shipped-in bundles."],
        "steps": [("Call to order", f"Call {B['phone']} and tell us how much wood you need."),
                  ("Choose delivery or pickup", "We deliver, or you can pick it up. " + confirm("Firewood delivery area and fee")),
                  ("Stack and enjoy", "Keep it off the ground and covered on top so it stays dry.")],
        "faq": [
            ("Do you deliver firewood?",
             "Yes, firewood delivery is available, and you can also pick it up. " + confirm("Firewood delivery area and fee")),
            ("What kind of firewood do you sell?",
             "Seasoned hardwood with low moisture, split from local trees. " + confirm("Which species are usually in stock (oak, hickory, etc.)")),
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
     "An ISA Certified Arborist has passed the International Society of Arboriculture's exam on tree biology, pruning, and safety, and keeps the credential current with continuing education. It means the advice about whether to prune, save, or remove a tree comes from someone trained to judge tree health."),
    ("How can I check that your arborist is certified?",
     f"You can verify {B['arborist']}'s ISA credential at treesaregood.org, the International Society of Arboriculture's public site, using the Verify a Certified Arborist search."),
    ("How long does stump grinding take?", SERVICES[3]["faq"][0][1]),
    ("Do you offer free estimates?",
     f"Call {B['phone']} to set up an estimate; we can often come the same day. " + confirm(C_ESTIMATES)),
    ("Do you handle emergency storm damage?", SERVICES[2]["faq"][2][1]),
    ("Do you deliver firewood?", SERVICES[5]["faq"][0][1]),
    ("Are you licensed and insured?", "Yes, Lee Friend's Tree Service, Inc. is licensed and insured. " + confirm(C_INSURED)),
    ("Do you work for businesses as well as homeowners?",
     "Yes. We handle residential and commercial tree work, from a single backyard tree to trees on business properties."),
    ("What areas do you serve?",
     "We're based in Loganville, GA and serve Gwinnett, Walton, and the Metro Atlanta area, including Grayson, Snellville, Monroe, Lawrenceville, and Athens. See our service areas page for the full list."),
    ("What happens to the wood from my trees?", SERVICES[4]["faq"][1][1]),
    ("Can I get free wood chips?", SERVICES[4]["faq"][0][1]),
    ("When is the best time to prune trees in Georgia?", SERVICES[1]["faq"][0][1]),
]

# ---------------------------------------------------------------- town pages (unique content each)
TOWN_DETAIL = {
    "Loganville": {
        "title": "Tree Service in Loganville, GA | Lee Friend's Tree Service",
        "meta": "Lee Friend's Tree Service is based in Loganville, GA 30052: tree removal, trimming, storm clean-up, stump grinding, and firewood. Call (770) 466-5112.",
        "h1": "Tree Service in Loganville, GA",
        "answer": "Lee Friend's Tree Service is based right here in Loganville, GA 30052, so Loganville is home ground for our crew. We handle tree removal, trimming and pruning, storm damage, stump grinding, wood recycling, and firewood on both the Walton and Gwinnett sides of town.",
        "sections": [
            ("Where in Loganville are you located?",
             "We're based in Loganville, GA 30052. " + confirm(C_STREET),
             "Being local means the crew, trucks, and chipper don't have far to travel, and we know the roads and neighborhoods on both sides of the county line."),
            ("Do you work on both the Walton and Gwinnett sides of Loganville?",
             "Yes. Loganville sits mostly in Walton County with part of the city in Gwinnett County, and we serve both.",
             "Wherever your address falls, the service, the price, and the arborist are the same."),
            ("What tree problems are common in Loganville yards?",
             "Tall pines that snap or uproot in storms, and big hardwoods with dead limbs over houses, are the calls we hear most often around Loganville.",
             "Loganville sits in Georgia's Piedmont, where loblolly pines, water oaks, sweetgums, and tulip poplars fill many yards. Pines tend to fail in high wind, and water oaks often decay from the inside as they age, so a look from a certified arborist can catch problems before a storm does. " + confirm("Add one recent Loganville job (street or neighborhood, tree, photo) to make this page even more local")),
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
        "meta": "Tree removal, trimming, storm clean-up, and stump grinding in Grayson, GA, from a family tree service next door in Loganville. Call (770) 466-5112.",
        "h1": "Tree Service in Grayson, GA",
        "answer": "Lee Friend's Tree Service serves Grayson, GA from our home base next door in Loganville. Grayson homeowners call us for tree removal, trimming over roofs and driveways, storm clean-up, and stump grinding.",
        "sections": [
            ("How close are you to Grayson?",
             "Grayson is Loganville's neighbor on the Gwinnett County side, so it's one of the closest towns we serve.",
             "Our crew works in Grayson regularly, which keeps travel short and scheduling simple."),
            ("Can you trim trees that hang over a Grayson home?",
             "Yes. Clearing limbs off roofs, gutters, and driveways is some of the most common work we do in Grayson.",
             "Our ISA Certified Arborist can tell you which limbs should come out for safety and which can stay, so you get the clearance you need without harming the tree."),
            ("What should Grayson homeowners know before removing a tree?",
             "Grayson is in Gwinnett County, and tree rules can differ between the city and unincorporated parts of the county, so check before a large removal.",
             "If a tree is in a front yard, near the street, or in a neighborhood with an HOA, ask your HOA and the city whether approval is needed. " + confirm("Add one recent Grayson job (neighborhood, tree, photo) for local proof")),
        ],
        "faq": [
            ("Do you serve all of Grayson, GA?",
             "Yes, we serve Grayson and the surrounding parts of Gwinnett County."),
            ("Do you grind stumps in Grayson?",
             "Yes. We grind stumps below ground level in Grayson, and full stump removal is also available."),
        ],
    },
    "Snellville": {
        "title": "Tree Service in Snellville, GA | Lee Friend's Tree Service",
        "meta": "Storm damage tree removal, trimming, stump grinding, and tree removal in Snellville, GA, with help coordinating insurance. Call (770) 466-5112.",
        "h1": "Tree Service in Snellville, GA",
        "answer": "Lee Friend's Tree Service handles tree removal, trimming, storm damage clean-up, and stump grinding in Snellville, GA, a short drive west of our Loganville base along US-78.",
        "sections": [
            ("Do you handle storm-damaged trees in Snellville?",
             "Yes. When a storm brings a tree down on a Snellville house, car, or driveway, we remove it and help coordinate with your insurance company.",
             f"Get everyone clear of the tree and any wires, call Georgia Power if lines are involved, then call us at {B['phone']}."),
            ("Do you work for Snellville businesses?",
             "Yes. Along with homes, we take care of trees on commercial properties in Snellville.",
             "That includes removing hazardous trees, trimming limbs away from buildings and parking areas, and grinding stumps. " + confirm("Add a Snellville commercial or residential job (with photo) for local proof")),
        ],
        "faq": [
            ("How far is Snellville from your shop?",
             "Snellville is just west of Loganville along US-78, so it's part of our everyday service area."),
            ("Will you help with my insurance claim after a storm in Snellville?",
             "Yes. Storm damage removal includes insurance coordination: we give your insurance company the details it asks for."),
        ],
    },
    "Monroe": {
        "title": "Tree Service in Monroe, GA | Lee Friend's Tree Service",
        "meta": "Tree removal, stump grinding, storm clean-up, and seasoned firewood delivery in Monroe and Walton County, GA. Call Lee Friend's at (770) 466-5112.",
        "h1": "Tree Service in Monroe, GA",
        "answer": "Lee Friend's Tree Service serves Monroe, GA, the Walton County seat, from our base in Loganville. Monroe customers call us for tree removal, stump grinding, storm clean-up, and seasoned hardwood firewood.",
        "sections": [
            ("Do you serve Monroe and the rest of Walton County?",
             "Yes. Loganville is in Walton County too, so Monroe and the county around it are home territory for us.",
             "We work on in-town lots and on larger rural properties around Monroe."),
            ("Can you handle big trees on larger Walton County lots?",
             "Yes. We remove large and hazardous trees, clear storm damage, and grind stumps on properties of any size.",
             "On bigger properties, good hardwood and pine logs from the job can go to local mills for lumber instead of a landfill, and branches become mulch."),
            ("Can I get firewood delivered in Monroe?",
             "Firewood delivery is available. " + confirm("Confirm firewood delivery reaches Monroe, and the fee"),
             "Our firewood is seasoned hardwood cut from local trees. " + confirm("Add one recent Monroe job (with photo) for local proof")),
        ],
        "faq": [
            ("Is Monroe in your service area?",
             "Yes. Monroe and the surrounding parts of Walton County are in our regular service area."),
            ("Do you grind stumps in Monroe?",
             "Yes. We grind stumps below ground level in Monroe, and full stump removal is also available."),
        ],
    },
}

# ---------------------------------------------------------------- reviews (from current site, via search excerpts)
REVIEWS = [
    ("I got about 5 quotes for a tree and stump removal and they provided the best value by far. The crew was friendly and considerate, did a great job cleaning up, and even ground up a little dead stump I'd had in my yard without me even asking.",
     confirm("Reviewer name for the 'best value' review, and check the wording against the current Testimonials page")),
    ("… Lisa and Jennifer are so professional, welcoming and courteous …",
     confirm("Full text and reviewer name for the 'Lisa and Jennifer' review (only an excerpt could be read)")),
    ("… could come same day and give me a quote …",
     confirm("Full text and reviewer name for the 'same day quote' review (only an excerpt could be read)")),
]


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
        "sameAs": [B["facebook"]],
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

NAV = [("Services", "services/"), ("Service Areas", "service-areas/"), ("About", "about/"), ("FAQ", "faq/"), ("Contact", "contact/")]


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
    towns = "".join(f'<li><a href="{p}service-areas/{u}/">{t}, GA</a></li>' for t, u in TOWN_PAGES.items())
    return f"""<footer class="site-foot">
  <div class="wrap foot-grid">
    <div class="foot-id">
      <p class="foot-name">{B['name']}</p>
      <p>Family-owned tree service in Loganville, GA {B['zip']}. ISA Certified Arborist {B['arborist']} on staff. Residential and commercial.</p>
      <p><a class="foot-phone" href="tel:{B['tel']}">{B['phone']}</a></p>
      {hours_dl()}
      <p class="small">{confirm(C_HOURS)}</p>
      <p><a class="social" href="{B['facebook']}" rel="noopener">{icon('facebook')} Facebook</a>
         {confirm("Google Maps / Google Business Profile link from the current site")}</p>
    </div>
    <div><p class="foot-h">Services</p><ul>{svc}</ul></div>
    <div><p class="foot-h">Towns</p><ul>{towns}<li><a href="{p}service-areas/">All service areas</a></li></ul>
      <p class="foot-h">Company</p><ul><li><a href="{p}about/">About &amp; credentials</a></li><li><a href="{p}faq/">FAQ</a></li><li><a href="{p}contact/">Contact &amp; quote</a></li></ul></div>
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
    return (f'<figure class="photo-slot {cls}"><div class="ph" role="img" aria-label="{html.escape(alt)}">{icon("camera")}</div>'
            f'<figcaption>{confirm(note)}<span class="alt-note">Alt text ready: “{html.escape(alt)}”</span></figcaption></figure>')


def faq_block(faqs, heading="Questions customers ask"):
    items = "".join(f'<details class="qa"><summary><h3>{html.escape(q)}</h3></summary><p>{a}</p></details>' for q, a in faqs)
    return f'<section class="band band-kraft"><div class="wrap narrow"><h2>{heading}</h2><div class="qa-list">{items}</div></div></section>'


def towns_block(service=None, intro=None):
    lis = "".join(
        f'<li><a href="{{P}}service-areas/{TOWN_PAGES[t]}/">{t}</a></li>' if t in TOWN_PAGES else f"<li>{t}</li>" for t in TOWNS)
    q = f"Which towns do you serve for {service.lower()}?" if service else "Which towns do you serve?"
    a = intro or ("We serve Loganville and 27 nearby towns across Gwinnett, Walton, and Metro Atlanta.")
    return f"""<section class="band band-pine towns"><div class="wrap">
  <h2>{q}</h2>
  <p class="answer">{a}</p>
  <ul class="town-list">{lis}</ul>
  <p><a class="link-light" href="{{P}}service-areas/">See all service areas</a></p>
</div></section>"""


def cta_block(heading="Have a tree that needs looking at?"):
    return f"""<section class="cta"><div class="wrap cta-in">
  <h2>{heading}</h2>
  <p>Call and talk to the family that runs the business. We can often come out the same day to give you a quote.</p>
  <div class="cta-actions">
    <a class="btn btn-call btn-big" href="tel:{B['tel']}">{icon('phone')}<span>Call {B['phone']}</span></a>
    <a class="btn btn-ghost" href="{{P}}contact/#quote">Request a quote online</a>
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
        ("shield", "Licensed and insured", "Your home and our crew are protected on every job. " + confirm(C_INSURED)),
        ("recycling", "Wood that gets a second life", "Branches become mulch, good logs go to local mills for lumber, and leftover hardwood becomes firewood. Wood chips are free."),
        ("bolt", "Same-day quotes", "Call in the morning and we can often come out that day to look at the tree and give you a price."),
    ]
    why_html = "".join(f'<li>{icon(i, "ico why-ico")}<div><h3>{h}</h3><p>{t}</p></div></li>' for i, h, t in why)
    rev = "".join(f'<li class="tag"><span class="tag-hole" aria-hidden="true"></span><blockquote><p>{q}</p></blockquote><p class="tag-who">{who}</p></li>' for q, who in REVIEWS)
    body = f"""
<section class="hero"><div class="wrap hero-in">
  <div class="hero-copy">
    <h1>{HOME_FIRST}</h1>
    <p class="hero-confirm">{confirm(C_YEAR)} {confirm(C_ARBORIST)}</p>
    <p class="hero-sub">Tree removal, trimming, storm clean-up, stump grinding, and seasoned firewood for homes and businesses.</p>
    <div class="hero-actions">
      <a class="btn btn-call btn-big" href="tel:{B['tel']}">{icon('phone')}<span>Call {B['phone']}</span></a>
      <a class="btn btn-ghost" href="{{P}}contact/#quote">Request a quote</a>
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
    {photo("Lee Friend's Tree Service crew and truck on a job in Loganville GA", "Crew or family photo from the current site's Gallery or About page")}
  </div>
  <ul class="why-list">{why_html}</ul>
</div></section>
<section class="band band-kraft reviews"><div class="wrap">
  <div class="section-head">
    <h2>What do customers say about Lee Friend's?</h2>
    <p class="answer">Customers mention fair prices, clean job sites, and a fast response. These reviews come from the company's current website.</p>
  </div>
  <ul class="tags">{rev}</ul>
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
      <a class="btn btn-ghost" href="{{P}}contact/#quote">Request a quote</a>
    </div>
  </div>
  <div class="page-hero-ico">{icon(s['icon'], 'ico big-ico')}</div>
</div></section>
<section class="band"><div class="wrap two-col">
  <div class="prose">
    <h2>What is {n}?</h2>
    <p class="answer">{s['what']}</p>
    <h2>When do you need {n}?</h2>
    <p class="answer">Call when a tree shows any of these signs, or if you're unsure and want an arborist's opinion.</p>
    <ul class="checks">{when}</ul>
  </div>
  {photo(f"{s['name']} by Lee Friend's Tree Service in Loganville GA", f"Real {n} photo from the current site's Gallery")}
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
  <p class="lead">Lee Friend's Tree Service, Inc. is a family-owned tree company in Loganville, GA, started in {B['founded']} by a husband-and-wife team and still run by them today, with ISA Certified Arborist {B['arborist']} on staff. {confirm(C_YEAR)}</p>
</div></section>
<section class="band"><div class="wrap two-col">
  <div class="prose">
    <h2>How did Lee Friend's Tree Service start?</h2>
    <p class="answer">The company began in {B['founded']} as a passion project for a husband-and-wife team who loved working outdoors.</p>
    <p>More than 30 years later, the same family still runs it, serving Loganville and the Metro Atlanta area with tree trimming, removal, storm clean-up, and eco-friendly wood recycling. {confirm("Owners' names and a few lines of the family story in their own words (who Lee is, how they started, family members in the business)")}</p>
    <h2>What makes the company different?</h2>
    <p class="answer">It's a family business that recycles nearly everything it cuts and keeps a certified arborist on staff.</p>
    <p>Branches become mulch, hardwood and pine logs go to local mills, and leftover hardwood is sold as seasoned firewood. Wood chips are free to anyone who wants them.</p>
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
    feature = "".join(f'<li><a href="{{P}}service-areas/{u}/"><span class="fa-town">{t}, GA</span><span class="fa-go">Tree service in {t}</span></a></li>'
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
  <p class="more">Not sure if you're in range? Call {B['phone']}. {confirm("Google Maps link to the business listing, for a 'Find us on Google Maps' link here")}</p>
</div></section>
<section class="band band-pine"><div class="wrap">
  <h2>What services do you offer in these towns?</h2>
  <p class="answer">Every service, everywhere we work.</p>
  <ul class="svc-links light">{"".join(f'<li><a href="{{P}}services/{s["slug"]}/">{icon(s["icon"])}<span>{s["name"]}</span></a></li>' for s in SERVICES)}</ul>
</div></section>
{cta_block()}
"""
    page("service-areas/index.html", "Tree Service Areas Near Loganville, GA | Lee Friend's Tree Service",
         "Lee Friend's Tree Service serves Loganville, Grayson, Snellville, Monroe, and 24 more towns in Gwinnett, Walton, and Metro Atlanta. Call (770) 466-5112.",
         body, current="service-areas/", trail=[("Home", "/"), ("Service Areas", "/service-areas/")])

    for t, slug in TOWN_PAGES.items():
        d = TOWN_DETAIL[t]
        secs = "".join(f'<h2>{q}</h2><p class="answer">{a}</p><p>{x}</p>' for q, a, x in d["sections"])
        others = "".join(f'<li><a href="{{P}}service-areas/{u}/">{o}, GA</a></li>' for o, u in TOWN_PAGES.items() if o != t)
        svcs = "".join(f'<li><a href="{{P}}services/{s["slug"]}/">{icon(s["icon"])}<span>{s["name"]} in {t}</span></a></li>' for s in SERVICES)
        body = f"""
<section class="page-hero"><div class="wrap">
  <h1>{d['h1']}</h1>
  <p class="lead">{d['answer']}</p>
  <div class="hero-actions">
    <a class="btn btn-call btn-big" href="tel:{B['tel']}">{icon('phone')}<span>Call {B['phone']}</span></a>
    <a class="btn btn-ghost" href="{{P}}contact/#quote">Request a quote</a>
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
  <ul class="feature-towns small">{others}<li><a href="{{P}}service-areas/"><span class="fa-town">All service areas</span></a></li></ul>
</div></section>
{cta_block(f"Need tree work in {t}?")}
"""
        page(f"service-areas/{slug}/index.html", d["title"], d["meta"], body, current="service-areas/",
             schema_extra=[faq_schema(d["faq"])],
             trail=[("Home", "/"), ("Service Areas", "/service-areas/"), (f"{t}, GA", f"/service-areas/{slug}/")])


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
    <p>Gwinnett, Walton, and the Metro Atlanta area. <a href="{{P}}service-areas/">See all 28 towns</a>.</p>
    <p><a class="social dark" href="{B['facebook']}" rel="noopener">{icon('facebook')} Find us on Facebook</a></p>
  </div>
  <form class="quote" id="quote" novalidate>
    <h2>Request a quote</h2>
    <p class="form-note">Tell us about the job and we'll call you back. {confirm("Where quote requests should be delivered (email address or form service) before launch")}</p>
    <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" required></div>
    <div class="field"><label for="f-phone">Phone number</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" required><p class="err" id="e-phone" hidden>Enter a phone number so we can call you back.</p></div>
    <div class="field"><label for="f-email">Email <span class="opt">(optional)</span></label><input id="f-email" name="email" type="email" autocomplete="email"></div>
    <div class="field"><label for="f-town">Town</label><input id="f-town" name="town" autocomplete="address-level2" list="town-list"><datalist id="town-list">{"".join(f'<option value="{t}">' for t in TOWNS)}</datalist></div>
    <div class="field"><label for="f-svc">What do you need?</label><select id="f-svc" name="service"><option value="">Choose a service</option>{svc_opts}<option>Not sure yet</option></select></div>
    <div class="field"><label for="f-msg">Tell us about the trees</label><textarea id="f-msg" name="message" rows="4" placeholder="For example: a big oak leaning toward the garage after last night's storm."></textarea></div>
    <button class="btn btn-call btn-big" type="submit">Send my quote request</button>
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
    build_contact()
    build_extras()
    print(f"Built {len(PAGES)} pages, {len(CONFIRMS)} confirm items")
