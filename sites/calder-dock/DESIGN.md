# Calder Dock & Marine — Design

World: **a nautical chart of the client's water.** Every claim is plotted (depths, piles, jobs). Built code-first from the direction contract in `/.impeccable/surfaces/sites-calder-dock-src-app-tsx.md`.

## Tokens (src/index.css `@theme`)

| Role | Token | Value |
|---|---|---|
| Ground (chart paper) | `paper` / `paper-2` | #f6f8f7 / #edf2f1 |
| Shallow water bands | `shoal` / `shoal-2` / `shoal-deep` | #b7d9e8 / #d6eaf2 / #8fc3db |
| Land tint (inside charts only) | `land` / `land-line` | #efe0ae / #9c8650 |
| Chart ink | `ink` / `ink-2` / `ink-3` | #0d1c26 / #34495a / #5a6f7e |
| Contour linework | `contour` | #3a7ea6 |
| Actions, pins, notes (aids-to-navigation magenta) | `magenta` / `magenta-dark` / `magenta-tint` | #a3166f / #7e0f55 / #f6e3ef |
| Night chart (commercial band, footer) | `night` / `night-2` / `night-line` / `night-ink` / `night-dim` | #07161e / #0d2430 / #2a6880 / #d9ecf2 / #8fb3c1 |

Color strategy: committed — chart blue owns whole bands (towns strip, engineering, site-visit), magenta is the only action color.

## Type

- **Archivo Variable** (self-hosted, width axis). Display `.display` = wdth 118 / wt 760 / -0.028em; `.display-md` = wdth 112 / wt 720. Labels `.caps` = wdth 125, uppercase, 0.14em.
- **Spectral Italic** `.hydro` — only for water names, soundings, captions (charts letter hydrography in italic).
- Numbers in data use `.tnum`.

## Components

- `NauticalChart` — procedural chart (seeded height field → depth-band fill, marching-squares contours, soundings, graduated neat-line border, optional sonar-sweep reveal).
- `DockPlan` — plan-view dock symbol laid from the nearest shore to a pin.
- `CompassRose` — magenta rose, 5° ticks.
- `SectionAA` — signature interaction: engineering section where the water level scrubs with scroll (pinned ≥1024px) or a range slider; float + gangway follow the water.
- Magic UI (source pulled from magicuidesign/magicui): `TextAnimate` (hero H1), `BlurFade`, `Marquee` (towns), `NumberTicker` (project stats), `Ripple` (active pin).
- Buttons: `.btn-primary` (magenta, 2px radius, soft offset shadow), `.btn-ghost` (underlined ink). Frames: `.neat` hairline neat-line around photo plates.

## Motion

One orchestrated moment per section: hero sonar sweep + word reveal; pins ripple; engineering water scrub. All respect `prefers-reduced-motion`.

## Imagery provenance

All photos are AI-generated stand-ins (Higgsfield · GPT Image 2.5, prompts kept in the Higgsfield job history; URLs in `src/data.ts`). Replace with real job photos before launch.
