# RC Pro Solutions: redesign demo

Free demo site by Legend Creative. Colors, tagline and wording are matched to their current site.

**Pages:** Home, Services, Gallery, About, Contact. Open `index.html` to preview.
To put it online for free, drag this folder onto https://app.netlify.com/drop.

## Photos
Every photo spot shows placeholder art with a "PHOTO:" tag. To use real photos, save them into `images/` with these names and they appear automatically.

| File name | Where it shows |
|---|---|
| hero.jpg | Big photo at the top of the homepage |
| hardscaping.jpg | Hardscaping (Services page + homepage) |
| outdoor-living.jpg | Outdoor living (Services page + homepage) |
| deck.jpg | Decks (Services page + homepage) |
| landscaping.jpg | Landscaping (Services page + homepage) |
| commercial.jpg | Commercial (Services page + homepage) |
| feature.jpg | paver patio with fire pit (homepage) |
| about.jpg | RC Pro crew on site (About page) |
| work-1.jpg | Gallery: Paver patio & seat walls |
| work-2.jpg | Gallery: Outdoor kitchen |
| work-3.jpg | Gallery: Composite deck |
| work-4.jpg | Gallery: Front yard landscape |
| work-5.jpg | Gallery: Retaining wall |
| work-6.jpg | Gallery: Fire pit patio |
| work-7.jpg | Gallery: Paver walkway |
| work-8.jpg | Gallery: Wood deck & stairs |
| work-9.jpg | Gallery: Sprinkler & sod |
| work-10.jpg | Gallery: Pergola & lighting |

## Confirm with the client before going live
- Reviews: the four review cards are placeholders. Paste in real Google reviews.
- The contact form shows a thank-you message but doesn't send anywhere yet. Connect it to their email (Netlify Forms or Formspree).
- Their menu lists 'ACE Resin'. We left it off because we don't know what it covers. Add it once confirmed.
- No reviews section, because no review data was found. Add one if they have Google reviews.
- Owner first name 'Robert' and '20+ years' are from research. Confirm.
- Towns under 'Service areas' are assumed. Confirm.

## Editing
All text lives in `site.py`. Edit it, then run `python3 site.py`. The shared layout lives in `sites/_engine/`.
