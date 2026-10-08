# Arnold Masonry & Landscape: redesign demo

Free demo site built by Legend Creative to pitch ARNOLD Masonry & Landscape (Scott Arnold, master mason, est. 1985).
Their current site (arnoldmasonryandlandscape.com) loads blank.

**Pages:** `index.html` (Home), `services.html`, `work.html` (Our Work), `about.html`, `contact.html` (Free consultation).
To preview, open `index.html` in a browser. To put it online for free, drag this folder onto https://app.netlify.com/drop.

## Adding real photos (do this before the pitch call if you can)
Every photo spot shows stone-pattern art with a "PHOTO:" tag until a real photo exists.
Save their project photos (from Houzz or Instagram @ their account) into the `images/` folder using these names. They appear automatically.

| File name | Where it shows |
|---|---|
| hero.jpg | Big photo at the top of the homepage (best outdoor kitchen) |
| kitchen.jpg, fireplace.jpg, patio.jpg, walls.jpg | Services page + hover previews on the homepage |
| scott.jpg | Scott Arnold (Home + About) |
| sandy-springs-1.jpg / -2 / -3 | Featured Sandy Springs project (kitchen, chimney, fire pit/patio) |
| work-1.jpg … work-10.jpg | Our Work gallery, in order |

## Confirm with the client before going live
- Reviews: four placeholders on the homepage. Paste in their real Google reviews.
- Towns served (Sandy Springs, Buckhead, Dunwoody, Roswell, Alpharetta, Milton, Johns Creek): we assumed these from "North Atlanta."
- Budget options on the contact form start at $15k (research said $10k–$15k minimum).
- The service bullet lists (e.g. "pool coping", "seat walls") are typical masonry scope. Confirm they offer each one.
- The contact form shows a thank-you message but doesn't send anywhere yet. Hook it to their email (Netlify Forms or Formspree).

## Editing
The pages are generated from `_build.py` (all text lives there). Edit it, then run `python3 _build.py`.
Styles: `assets/css/site.css`. Animations: `assets/js/site.js` (GSAP, self-hosted).
