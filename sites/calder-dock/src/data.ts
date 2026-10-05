// Business details are placeholders until the client confirms them.
export const business = {
  name: 'Calder Dock & Marine',
  short: 'Calder',
  water: 'Lake Norman',
  region: 'Lake Norman, North Carolina',
  phone: '(704) 555-0142',
  phoneHref: 'tel:+17045550142',
  email: 'hello@calderdock.com',
  hours: 'Mon–Fri 7–5 · Site visits by appointment',
  license: 'NC Licensed General Contractor · License # pending',
  position: '35°31′ N · 80°55′ W',
}

// AI-generated stand-in photography (Higgsfield, GPT Image 2.5). Replace with real job photos.
const CDN = 'https://d8j0ntlcm91z4.cloudfront.net/user_2y9epIre1Mp5IxObA3BfNJCh26e'
export const photos = {
  hero: `${CDN}/hf_20261005_210916_c4eaa432-3abc-47da-9d09-9e77f8d1dd75.png`,
  piledriver: `${CDN}/hf_20261005_210917_dc7a361d-1013-4140-8729-bf7d72e2ce63.png`,
  hardware: `${CDN}/hf_20261005_210917_d3bf4ec7-19a9-4139-8849-67cd1b487d78.png`,
  aerialLift: `${CDN}/hf_20261005_210917_55ae97f3-4f25-4223-8a21-98a1e0a52d8d.png`,
  floating: `${CDN}/hf_20261005_210917_e813c4f1-6dfa-49df-84af-d49d5407dc4f.png`,
  boathouse: `${CDN}/hf_20261005_210916_7cb17e9c-b891-409c-94d6-4cdcdda16b36.png`,
  marina: `${CDN}/hf_20261005_210918_01a5b41a-cbc6-43ac-b73f-8cb25dcdc1cd.png`,
  seawall: `${CDN}/hf_20261005_210918_7a25eec6-f79a-49c7-955f-5ffe0a157ee9.png`,
  hands: `${CDN}/hf_20261005_210916_34599c42-2230-421a-967c-021d2b83a912.png`,
  evening: `${CDN}/hf_20261005_210918_66cec890-d618-4ad5-88c7-f80f5aa5f31e.png`,
}

export type Project = {
  id: string
  name: string
  water: string
  type: string
  /** Approximate position on the project chart, 0–1. */
  at: [number, number]
  photo: string
  alt: string
  piles: number
  span: number
  decking: string
  note: string
}

// Illustrative projects for layout; swap for real jobs before launch.
export const projects: Project[] = [
  {
    id: 'heron',
    name: 'Heron Point',
    water: 'Main channel',
    type: 'Covered two-slip boathouse',
    at: [0.2, 0.36],
    photo: photos.hero,
    alt: 'Covered two-slip boathouse with hardwood deck on a misty lake at sunrise',
    piles: 38,
    span: 86,
    decking: 'Ipe hardwood',
    note: 'Main-channel exposure: heavier pile spacing and through-bolted bracing for wake load.',
  },
  {
    id: 'cedar',
    name: 'Cedar Cove',
    water: 'Shallow cove',
    type: 'L-dock with boat lift',
    at: [0.38, 0.72],
    photo: photos.aerialLift,
    alt: 'Aerial view of an L-shaped wooden dock with a wake boat on a lift beside a lawn',
    piles: 24,
    span: 64,
    decking: 'Pressure-treated pine',
    note: 'Lift set on its own pile cluster so the dock never carries the boat’s weight.',
  },
  {
    id: 'holloway',
    name: 'Holloway Bend',
    water: 'Deep bend',
    type: 'Floating dock & gangway',
    at: [0.55, 0.28],
    photo: photos.floating,
    alt: 'Floating dock with grey composite decking and kayaks at golden hour',
    piles: 4,
    span: 48,
    decking: 'Composite',
    note: 'Too deep for economical piling: an anchored float that rides every water level.',
  },
  {
    id: 'mill',
    name: 'Mill Branch',
    water: 'Creek mouth',
    type: 'Two-story boathouse, roof deck',
    at: [0.72, 0.66],
    photo: photos.boathouse,
    alt: 'Two-story boathouse with rooftop sundeck and pontoon boat on a lift',
    piles: 42,
    span: 72,
    decking: 'Ipe & cedar',
    note: 'Roof deck engineered for gathering loads; stair tower set on independent piles.',
  },
  {
    id: 'sandy',
    name: 'Sandy Run',
    water: 'Wind-exposed point',
    type: 'Seawall & riprap',
    at: [0.86, 0.3],
    photo: photos.seawall,
    alt: 'Curved stone riprap and concrete seawall along a lakefront lawn',
    piles: 0,
    span: 140,
    decking: '—',
    note: 'Eroding bank stabilized with filter fabric, riprap and a low wall before the new dock.',
  },
  {
    id: 'pine',
    name: 'Pine Ridge',
    water: 'Community cove',
    type: 'HOA marina, 24 covered slips',
    at: [0.1, 0.8],
    photo: photos.marina,
    alt: 'Community marina with rows of covered boat slips and a wide wooden walkway',
    piles: 160,
    span: 410,
    decking: 'Pressure-treated pine',
    note: 'Phased build so members kept slips through the season.',
  },
]

export const towns = ['Mooresville', 'Cornelius', 'Davidson', 'Huntersville', 'Denver', 'Sherrills Ford', 'Terrell', 'Troutman', 'Catawba']

export const services = [
  {
    key: 'fixed',
    name: 'Fixed piling docks',
    line: 'Timber piles driven to refusal, through-bolted framing, decks set for the high-water mark.',
  },
  {
    key: 'float',
    name: 'Floating docks',
    line: 'For deep water and changing levels: anchored floats with hinged gangways that stay walkable.',
  },
  {
    key: 'house',
    name: 'Boathouses & roof decks',
    line: 'Covered slips, storage and sun decks, engineered as structures, not afterthoughts.',
  },
  {
    key: 'lift',
    name: 'Boat & PWC lifts',
    line: 'Sized to your boat and set on their own piles so the dock never carries the load.',
  },
  {
    key: 'wall',
    name: 'Seawalls & shoreline',
    line: 'Riprap, walls and erosion control that protect the bank your dock depends on.',
  },
  {
    key: 'repair',
    name: 'Repairs & re-decking',
    line: 'Pile sistering, new framing and decking: honest advice on when to repair and when to rebuild.',
  },
] as const

export const decking = [
  { name: 'Pressure-treated pine', feel: 'Classic, warm', upkeep: 'Seal every 2–3 years', life: 'Good' },
  { name: 'Composite', feel: 'Even, splinter-free', upkeep: 'Wash yearly', life: 'Long' },
  { name: 'Ipe hardwood', feel: 'Dense, rich, cool underfoot', upkeep: 'Oil to keep color, or let it silver', life: 'Longest' },
  { name: 'Aluminum & grate', feel: 'Light, lets light through', upkeep: 'Minimal', life: 'Long' },
]

export const process = [
  {
    leg: 'Site sounding',
    body: 'We walk the shoreline with you, sound the depth where the dock will run, check the bank and the lakebed, and listen to how you use the water.',
  },
  {
    leg: 'Design & engineering',
    body: 'A drawn plan and section: pile layout, deck height for the high-water mark, lift and roof loads. One fixed-price proposal, line by line.',
  },
  {
    leg: 'Permits',
    body: 'We prepare and file the lake-use and county paperwork and handle the back-and-forth. You sign; we chase.',
  },
  {
    leg: 'Build',
    body: 'Barge-mounted crew and pile driver, a clean site every evening, and a weekly photo update until the last board is down.',
  },
  {
    leg: 'Walkthrough & care',
    body: 'We walk the finished dock together, hand over the drawings, and come back each spring for a hardware check.',
  },
]

export const faqs = [
  {
    q: 'Do I need a permit to build or replace a dock?',
    a: 'Almost always. Most lakes in our area are managed by a utility or lake authority with shoreline rules on size, setbacks and materials, plus county building permits. We prepare and file everything and tell you up front how long approvals usually take.',
  },
  {
    q: 'Fixed or floating — which is right for my lot?',
    a: 'It comes down to depth, bottom conditions and how much the water level moves. Shallow, firm bottoms favor a fixed piling dock; deep water or big level swings favor a float. The site sounding visit answers this with measurements, not guesses.',
  },
  {
    q: 'How long does a new dock take?',
    a: 'Design and permits usually take longer than the build itself. Once approved, most residential docks are built in a few weeks; boathouses take longer. Your proposal includes a schedule.',
  },
  {
    q: 'Can you repair my existing dock instead of replacing it?',
    a: 'Often, yes. If the piles are sound we can re-frame and re-deck. If they are not, we will show you why and price both options so you can decide.',
  },
  {
    q: 'Do you build for HOAs, marinas and businesses?',
    a: 'Yes — community docks, covered slip rows, restaurant tie-ups and phased replacements, with one project lead from proposal to punch list.',
  },
]
