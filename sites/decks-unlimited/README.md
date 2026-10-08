# Decks & Porches Unlimited: redesign demo

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
| sunroom.jpg | Sunrooms (Services page + homepage) |
| repair.jpg | Deck repair & resurfacing (Services page + homepage) |
| patio.jpg | Covered patios & more (Services page + homepage) |
| feature.jpg | finished deck and stairs (homepage) |
| about.jpg | our crew on a deck build (About page) |
| work-1.jpg | Gallery: Wood deck in the trees |
| work-2.jpg | Gallery: Screened porch |
| work-3.jpg | Gallery: Composite deck & stairs |
| work-4.jpg | Gallery: Sunroom addition |
| work-5.jpg | Gallery: Deck resurfacing |
| work-6.jpg | Gallery: Two-level deck |
| work-7.jpg | Gallery: Covered porch |
| work-8.jpg | Gallery: New railings |
| work-9.jpg | Gallery: Deck with pergola |
| work-10.jpg | Gallery: Porch-to-sunroom |

## Confirm with the client before going live
- Reviews: the four review cards are placeholders. Paste in real Google reviews.
- The contact form shows a thank-you message but doesn't send anywhere yet. Connect it to their email (Netlify Forms or Formspree).
- Logo uses a simple deck icon. Swap in their carpenter mascot logo when they send it.
- 'Deck repair & resurfacing' and 'Covered patios' come from a directory listing, not their site. Confirm.
- A directory shows a 4.9 Google rating from about 90 reviews, but that couldn't be confirmed, so no reviews section yet. Add one once confirmed.
- No street address or email found. Only Buford, GA is shown.
- Towns under 'Service area' are assumed. Confirm against their Service Area page.

## Editing
All text lives in `site.py`. Edit it, then run `python3 site.py`. The shared layout lives in `sites/_engine/`.
