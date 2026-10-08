# Design: "Carved in Stone"

The site reads as a carved granite cornerstone: inscriptional Roman capitals incised into a speckled granite ground.

## Tokens
- Granite ground `#d6d2ca` (hi `#e4e0d8`, lo `#bfbab0`) with a procedural speckle + cloud texture
- Iron ink `#1e1c1a`; carved type `#4a4640`; muted `#57524b`
- Georgia red-clay brick `#8b3a22` (hover `#a4482c`, pressed `#6e2c19`); on-brick text `#f6e6dc`. It's committed across whole bands: the CTA band, the brick courses, and the service-row hover
- Slate `#26292a` for the dark project passage and the footer; slate text `#e2ddd4` / `#a9a49b`
- Mortar `#ece9e3` for the form surface

## Type
- Display: Cinzel 500–700 (self-hosted). Incised with `text-shadow: 0 1px 0 rgba(255,255,255,.55), 0 -1px 1px rgba(0,0,0,.42)`
- Body: Hanken Grotesk 400–600. Fluid scale `--step--1` … `--step-5` (max 6rem)

## Components
Square corners (2px). 1px mortar rules instead of cards. Running-bond brick "courses" as section joints.
Buttons: brick primary, ghost outline, light-on-brick. Stone-pattern photo placeholders (`assets/stone-*.svg`) that hide once a real image loads.

## Motion
Signature: headings chisel in letter by letter (blur and drop), then the cut shadow deepens. Brick courses lay in course by course.
Hero photo clip-reveal and a gentle parallax. Everything is off under `prefers-reduced-motion`.
