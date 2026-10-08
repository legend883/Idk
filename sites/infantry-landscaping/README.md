# Infantry Landscaping: redesign demo

Free demo site by Legend Creative. Colors, tagline and wording are matched to their current site.

**Pages:** Home, Services, Gallery, About, Contact. Open `index.html` to preview.
To put it online for free, drag this folder onto https://app.netlify.com/drop.

## Photos
Every photo spot shows placeholder art with a "PHOTO:" tag. To use real photos, save them into `images/` with these names and they appear automatically.

| File name | Where it shows |
|---|---|
| hero.jpg | Big photo at the top of the homepage |
| landscape.jpg | Landscape design (Services page + homepage) |
| outdoor-living.jpg | Outdoor living (Services page + homepage) |
| fence.jpg | Fences (Services page + homepage) |
| irrigation.jpg | Irrigation (Services page + homepage) |
| lawn.jpg | Lawn care (Services page + homepage) |
| trees.jpg | Tree services (Services page + homepage) |
| feature.jpg | crew installing a stone patio (homepage) |
| about.jpg | the Infantry Landscaping crew (About page) |
| work-1.jpg | Gallery: Boulder garden & beds |
| work-2.jpg | Gallery: Stone patio |
| work-3.jpg | Gallery: Privacy fence |
| work-4.jpg | Gallery: Front yard refresh |
| work-5.jpg | Gallery: Retaining wall |
| work-6.jpg | Gallery: Sod installation |
| work-7.jpg | Gallery: Outdoor kitchen |
| work-8.jpg | Gallery: Horizontal fence & gate |
| work-9.jpg | Gallery: Tree removal & cleanup |
| work-10.jpg | Gallery: Commercial landscape |

## Confirm with the client before going live
- Reviews: the four review cards are placeholders. Paste in real Google reviews.
- The contact form shows a thank-you message but doesn't send anywhere yet. Connect it to their email (Netlify Forms or Formspree).
- Logo uses a simple star badge. Swap in their soldier logo file when they send it.
- Towns under 'Serving Metro Atlanta' are assumed. Confirm the service area.
- The '160+ reviews' count is from research. Double-check the current number.
- Service bullet points are typical scope. Confirm each one.

## Editing
All text lives in `site.py`. Edit it, then run `python3 site.py`. The shared layout lives in `sites/_engine/`.
