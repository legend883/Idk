# Design: Lee Friend's Tree Service

World: feed-store print. A Georgia farm co-op print shop: two-color printing on kraft, stamped seals, kraft tags.

## Tokens (source: assets/site.css `:root`)
| Token | Value | Role |
|---|---|---|
| --pine | #1d3a29 | Hero, header, pine bands (carries whole regions) |
| --pine-deep | #13281c | Headings on kraft, top bar, footer |
| --pine-mid | #2e5a3f | Hover on pine |
| --kraft | #d8bf91 | Kraft bands, seal strip, woodcut ink on pine |
| --kraft-light | #e8d8b6 | Page ground, boards, tags, form |
| --kraft-dark | #9c7845 | Rules, dashed photo slots |
| --gold | #d6b43a | Wordmark and footer name (nod to the gold lettering in their current logo) |
| --saw | #c4450c | Call buttons, closing CTA band, focus ring (white text) |
| --confirm-bg | #fff07a | [CONFIRM] tags (preview only) |

## Type
- Display: Zilla Slab 600/700 (self-hosted). Headings, wordmark, reviews.
- Body: Public Sans 400/600/700 (self-hosted).
- Stamp: Big Shoulders Stencil Display 800. Seals, the "Since" stamp, step numerals.

## Components
- Seal: circular double-ring stamp; pending seals are dashed.
- Board: services as a ruled price board (no prices), round pine icon, pill "Details".
- Tag: reviews on kraft tags with a punched hole.
- Steps: stencil numerals over a kraft rule (real sequences only).
- Photo slot: dashed hatched frame with [CONFIRM] caption and ready alt text.
- Call bar: fixed orange bar on screens under 860px.

## Motion
One moment: credential seals press in on load. Nothing else animates. Off under reduced motion.
