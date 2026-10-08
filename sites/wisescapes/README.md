# Wisescapes: redesign demo

Free demo site by Legend Creative. Colors, tagline and wording are matched to their current site.

**Pages:** Home, Services, Gallery, About, Contact. Open `index.html` to preview.
To put it online for free, drag this folder onto https://app.netlify.com/drop.

## Photos
Every photo spot shows placeholder art with a "PHOTO:" tag. To use real photos, save them into `images/` with these names and they appear automatically.

| File name | Where it shows |
|---|---|
| hero.jpg | Big photo at the top of the homepage |
| design.jpg | Landscape design (Services page + homepage) |
| patio.jpg | Patios & fireplaces (Services page + homepage) |
| kitchen.jpg | Outdoor kitchens (Services page + homepage) |
| deck.jpg | Decks (Services page + homepage) |
| walls.jpg | Retaining walls & erosion control (Services page + homepage) |
| drainage.jpg | Drainage solutions (Services page + homepage) |
| turf.jpg | Artificial turf (Services page + homepage) |
| lighting.jpg | Landscape lighting (Services page + homepage) |
| feature.jpg | patio and fireplace at dusk (homepage) |
| about.jpg | Wisescapes design session (About page) |
| work-1.jpg | Gallery: Patio & outdoor fireplace |
| work-2.jpg | Gallery: Front yard landscape |
| work-3.jpg | Gallery: Retaining wall & terraces |
| work-4.jpg | Gallery: Outdoor kitchen |
| work-5.jpg | Gallery: Backyard planting plan |
| work-6.jpg | Gallery: Fire pit patio |
| work-7.jpg | Gallery: Landscape lighting |
| work-8.jpg | Gallery: Deck & stairs |
| work-9.jpg | Gallery: Dry creek drainage |
| work-10.jpg | Gallery: Artificial turf yard |

## Confirm with the client before going live
- Reviews: the four review cards are placeholders. Paste in real Google reviews.
- The contact form shows a thank-you message but doesn't send anywhere yet. Connect it to their email (Netlify Forms or Formspree).
- Their current site shows two phone numbers (770-672-1526 and 770-895-0528). We used 770-672-1526, the one at the top of their homepage. Confirm.
- No reviews section, because no review data was found. Add one if they have Google reviews.
- Towns under 'Crafted locally for' are assumed from their Cumming address.

## Editing
All text lives in `site.py`. Edit it, then run `python3 site.py`. The shared layout lives in `sites/_engine/`.
