# AINautics: design system ("Flight Manual")

The site is styled like a premium aviation handbook. Solid handbook-blue cover sections alternate with
cool white pages. The site is divided into numbered chapters, one per audience, and each chapter's
colored index tab stays pinned to the right edge on desktop. Photos are shown as white-matted
"Fig." plates with captions.

## Colors (AINautics brand, taken from ainautics.com)
| Token | Hex | Use |
|---|---|---|
| black | #000000 | Header, cover, Ambassadors, contact, footer |
| char | #161616 | Flight-path section |
| red | #922D28 | AINautics brand red: buttons, accent rules, numbers, Schools tab, iFlyDrone panel |
| red-hover | #A8362F | Hover state, and red text on black |
| red-deep | #5E1C19 | Business tab |
| paper / paper-2 | #FFFFFF / #F4F4F4 | Pages |
| rule | #DADADA | Hairlines |

## Type (AINautics brand fonts)
- Headings: Poppins 600–800
- Body: Inter 400–700
- Sentence case. The red 5px rule under key headings echoes their site.

## Logo
The real white AINautics "Drone Air Innovations" logo, re-hosted on Higgsfield's CDN.

## Components
- Plate: white mat (10–14px), square corners, neutral soft shadow, "Fig. X.Y" caption
- Chapter tab: a colored square holding a big number and the chapter name set vertically
- Buttons: 2px radius, 48px min height. Primary is yellow on blue-ink; secondary is blue or outline
- Tables and lists: a 2px ink top rule, then 1px hairline rows

## Motion (GSAP 3.12.5 + ScrollTrigger, all off when reduced motion is on)
- The cover headline rises line by line, and the hero plate reveals like a developing print
- The flight-path line draws itself as you scroll
- Numbers count up once when they come into view
- The thumb-index tab tracks the chapter being read

## Imagery
All photos are AI-generated with Higgsfield (gpt_image_2_5), optimized to WebP, and hosted on
Higgsfield's CDN. Replace them with real AINautics photos before launch.
