# AINautics: design system ("Flight Manual")

The site is styled like a premium aviation handbook. Solid handbook-blue cover sections alternate with
cool white pages. The site is divided into numbered chapters, one per audience, and each chapter's
colored index tab stays pinned to the right edge on desktop. Photos are shown as white-matted
"Fig." plates with captions.

## Colors
| Token | Hex | Use |
|---|---|---|
| blue | #1633B5 | Cover, contact section, Pilots tab, main links |
| blue-ink | #0A1230 | Text, dark sections (flight path, Ambassadors, footer) |
| paper | #F2F4F7 | Page background |
| paper-2 | #E6EAF1 | Alternate section (Pilots) |
| rule | #C9D0DE | Hairline rules |
| yellow | #FFC629 | Main action buttons, Business tab, iFlyDrone panel |
| magenta | #B0126E | Schools tab, the "New program" flag (K-5) |

## Type
- Display: Archivo, 125% width, weight 800 (headings, numbers, labels, buttons)
- Body: Public Sans 400/700
- Sentence case everywhere. No all-caps labels.

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
