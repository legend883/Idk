# Design: The $20 Auction

World: a living Saturday comic. The page is a comic page; every screen is made of panels.

## Tokens (source: sites/twenty-dollar-auction/src/styles.css `:root`)
| Token | Value | Role |
|---|---|---|
| --ink | #14110F | Panel borders, text, host desk ground |
| --paper | #FFFFFF | Panel fill |
| --ground | #FFE14D | Page ground (process yellow) |
| --ground-dot | #F2A900 | Ben-Day halftone dots on the ground (11px grid) |
| --caption | #FFE94D | Narration caption boxes, top-bid balloon, primary buttons |
| --cyan | #00AEEF | Process cyan fills, focus ring |
| --magenta | #EC008C | Process magenta fills, selection |
| --red | #E4002B | Splash panel, SOLD burst, destructive and gavel buttons |
| --cash | #00A651 | Money tags, bid buttons |
| --warn | #FF8200 | Low-money state ($3 or less) |
| --desk | #191513 | Host desk panel (controls live only here) |

Player ink colors: #E4002B #0072CE #00A651 #FF8200 #7B2CBF #00B5B8 #E6007E #6B4226.

## Type
- Display: Bangers (Google Fonts), fallback Luckiest Guy / Trebuchet MS. Headings, buttons, money, captions, balloons.
- Body: Comic Neue 700, fallback Trebuchet MS. Running text, labels.
- Money uses tabular numerals in Bangers on a green price-tag shape.

## Components
- Panel: white, 3px ink border, 4px radius; audience panels tilt ±0.5deg at rest.
- Caption box: yellow fill, 3px ink border, Bangers.
- Button: 3px ink border with 6px bottom edge that compresses on press; colors from process inks.
- Speech balloon: bids; current top bid is the largest, yellow, with tail.
- Starburst: authored SVG polygon behind revealed items and the SOLD! splash.
- Host desk: black panel, separate from the stage and player panels; hideable for TV.
- Creation renderers: SVG drawn from structured win data (src/js/art.js), 11 kinds.

## Motion
One authored moment per action: item slam on reveal, SOLD! burst slam plus confetti and a money ticker on a win, new feature pops into the creation. All disabled under prefers-reduced-motion.

## Single theme
Deliberately light-only: the comic page world. Background and every color are set explicitly.
