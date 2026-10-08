# Forever Outdoors: redesign demo

Free demo site by Legend Creative. Colors, tagline and wording are matched to their current site.

**Pages:** Home, Services, Gallery, About, Contact. Open `index.html` to preview.
To put it online for free, drag this folder onto https://app.netlify.com/drop.

## Photos
Every photo spot shows placeholder art with a "PHOTO:" tag. To use real photos, save them into `images/` with these names and they appear automatically.

| File name | Where it shows |
|---|---|
| hero.jpg | Big photo at the top of the homepage |
| composite-deck.jpg | Composite decks (Services page + homepage) |
| wood-deck.jpg | Wood decks (Services page + homepage) |
| porch.jpg | Porches (Services page + homepage) |
| patio.jpg | Paver patios (Services page + homepage) |
| kitchen.jpg | Outdoor kitchens (Services page + homepage) |
| fire.jpg | Fire features (Services page + homepage) |
| walls.jpg | Retaining walls (Services page + homepage) |
| makeover.jpg | Backyard makeovers (Services page + homepage) |
| feature.jpg | composite deck with railings (homepage) |
| about.jpg | our team on a deck build (About page) |
| work-1.jpg | Gallery: Covered outdoor kitchen |
| work-2.jpg | Gallery: Composite deck |
| work-3.jpg | Gallery: Screened porch |
| work-4.jpg | Gallery: Paver patio |
| work-5.jpg | Gallery: Fire pit & seating |
| work-6.jpg | Gallery: Wood deck & stairs |
| work-7.jpg | Gallery: Retaining wall |
| work-8.jpg | Gallery: Covered porch |
| work-9.jpg | Gallery: Multi-level deck |
| work-10.jpg | Gallery: Backyard makeover |

## Confirm with the client before going live
- Reviews: the four review cards are placeholders. Paste in real Google reviews.
- The contact form shows a thank-you message but doesn't send anywhere yet. Connect it to their email (Netlify Forms or Formspree).
- No reviews section, because no review data was found. Add one if they have Google reviews.
- Their live site's footer labels outdoor kitchens as 'Siding Services', and the 'Our Services' menu link goes nowhere. Good talking points.
- Towns under 'Areas we serve' are assumed. Confirm.
- Confirm they're Trex and TimberTech installers before going live.

## Editing
All text lives in `site.py`. Edit it, then run `python3 site.py`. The shared layout lives in `sites/_engine/`.
