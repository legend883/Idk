# ITM Landscape: redesign demo

Free demo site by Legend Creative. Colors, tagline and wording are matched to their current site.

**Pages:** Home, Services, Gallery, About, Contact. Open `index.html` to preview.
To put it online for free, drag this folder onto https://app.netlify.com/drop.

## Photos
Every photo spot shows placeholder art with a "PHOTO:" tag. To use real photos, save them into `images/` with these names and they appear automatically.

| File name | Where it shows |
|---|---|
| hero.jpg | Big photo at the top of the homepage |
| lawn.jpg | Lawn maintenance (Services page + homepage) |
| installation.jpg | Installation projects (Services page + homepage) |
| hardscape.jpg | Hardscaping & retaining walls (Services page + homepage) |
| outdoor-living.jpg | Outdoor kitchens & living (Services page + homepage) |
| drainage.jpg | Drainage, irrigation & lighting (Services page + homepage) |
| commercial.jpg | Commercial (Services page + homepage) |
| feature.jpg | Eric and Tori Soles (homepage) |
| about.jpg | the ITM Landscape team (About page) |
| work-1.jpg | Gallery: Water feature & plantings |
| work-2.jpg | Gallery: Paver patio |
| work-3.jpg | Gallery: Weekly lawn care |
| work-4.jpg | Gallery: Front yard makeover |
| work-5.jpg | Gallery: Retaining wall |
| work-6.jpg | Gallery: Commercial entrance |
| work-7.jpg | Gallery: Backyard landscape |
| work-8.jpg | Gallery: Outdoor kitchen |
| work-9.jpg | Gallery: Sod installation |
| work-10.jpg | Gallery: Office park grounds |

## Confirm with the client before going live
- Reviews: the four review cards are placeholders. Paste in real Google reviews.
- The contact form shows a thank-you message but doesn't send anywhere yet. Connect it to their email (Netlify Forms or Formspree).
- Their site has a Bill Pay page. Link it in the menu once we have the payment URL.
- Their Alpharetta office address isn't listed. Add it if they want both locations shown.
- The 'Family run' wording comes from Eric, Tori and Eddie Soles being named on their site. Confirm they're happy with it.
- Towns under 'Service areas' are assumed. Confirm.

## Editing
All text lives in `site.py`. Edit it, then run `python3 site.py`. The shared layout lives in `sites/_engine/`.
