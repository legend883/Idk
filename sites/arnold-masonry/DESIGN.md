# Design: "Carved in Stone"

The site reads as a carved granite cornerstone: inscriptional Roman capitals incised into a speckled granite ground.

## Tokens (matched to the client's live site and logo)
- Charcoal-blue ground `#1e2327` (raised `#283037`, deep `#151a1d`) with a light speckle granite texture
- White text `#f3f5f4`; carved type `#d6dcda`; muted `#a6b0b3`
- Leaf green, their "Request a Quote" color `#5a9770`. Button fill is `#467b5b` (white text at AA contrast), hover `#5a9770`. Light green `#7fbf93` for stars and focus
- Slate blue, their secondary button `#627a90` (fill `#546b80`)
- Near-black `#13171a` for the project passage and the footer; green closing band
- Green swoosh under the wordmark, echoing their logo

## Type
- Display: Cinzel 500–700 (self-hosted). Incised with `text-shadow: 0 1px 0 rgba(255,255,255,.55), 0 -1px 1px rgba(0,0,0,.42)`
- Body: Hanken Grotesk 400–600. Fluid scale `--step--1` … `--step-5` (max 6rem)

## Components
Square corners (2px). 1px mortar rules instead of cards. Running-bond stone "courses" as section joints.
Buttons: brick primary, ghost outline, light-on-brick. Stone-pattern photo placeholders (`assets/stone-*.svg`) that hide once a real image loads.

## Motion
Signature: headings chisel in letter by letter (blur and drop), then the cut shadow deepens. Brick courses lay in course by course.
Hero photo clip-reveal and a gentle parallax. Everything is off under `prefers-reduced-motion`.
