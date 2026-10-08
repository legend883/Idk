# Leisure Time Decks: redesign demo

Free demo site by Legend Creative. Colors, tagline and wording are matched to their current site.

**Pages:** Home, Services, Gallery, About, Contact. Open `index.html` to preview.
To put it online for free, drag this folder onto https://app.netlify.com/drop.

## Photos
Every photo spot shows placeholder art with a "PHOTO:" tag. To use real photos, save them into `images/` with these names and they appear automatically.

| File name | Where it shows |
|---|---|
| hero.jpg | Big photo at the top of the homepage |
| deck.jpg | Custom decks (Services page + homepage) |
| porch.jpg | Porches (Services page + homepage) |
| kitchen.jpg | Outdoor kitchens (Services page + homepage) |
| fireplace.jpg | Outdoor fireplaces & firepits (Services page + homepage) |
| pergola.jpg | Pergolas & gazebos (Services page + homepage) |
| sunroom.jpg | Sunrooms & patios (Services page + homepage) |
| feature.jpg | covered porch over a deck (homepage) |
| about.jpg | a finished deck at dusk (About page) |
| work-1.jpg | Gallery: Two-level deck in the trees |
| work-2.jpg | Gallery: Screened porch |
| work-3.jpg | Gallery: Composite deck & stairs |
| work-4.jpg | Gallery: Outdoor fireplace |
| work-5.jpg | Gallery: Covered porch |
| work-6.jpg | Gallery: Pergola over deck |
| work-7.jpg | Gallery: Wraparound deck |
| work-8.jpg | Gallery: Outdoor kitchen |
| work-9.jpg | Gallery: Gazebo |
| work-10.jpg | Gallery: Fire pit & patio |

## Confirm with the client before going live
- Reviews: the four review cards are placeholders. Paste in real Google reviews.
- The contact form shows a thank-you message but doesn't send anywhere yet. Connect it to their email (Netlify Forms or Formspree).
- Founding year 1989 is from research, and their site says 'over 30 years'. Confirm.
- No street address found. The site shows 'Atlanta, Georgia'.
- Towns under 'Building across metro Atlanta' are assumed.
- Their current site shows raw code at the top of the homepage, and its headlines overlap. Point this out on the call.

## Editing
All text lives in `site.py`. Edit it, then run `python3 site.py`. The shared layout lives in `sites/_engine/`.
