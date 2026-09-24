# Legend Creative – Website Workspace

This repository holds Claude Code skills (in `.claude/skills/`) that load automatically
whenever Claude Code works in this repo:

- **frontend-design**: distinctive, non-template visual design (typography, color, layout, motion)
- **theme-factory**: ready-made color and font themes to apply to a site
- **ui-ux-pro-max**: searchable library of 50+ styles, 190+ color palettes, font pairings, landing-page layouts and scroll-animation (GSAP) presets
- **impeccable**: design-director skill with commands like `/impeccable bolder`, `animate`, `polish`, `critique`, `overdrive`
- **webapp-testing**: lets Claude open the site in a real browser and screenshot it to check its own work

Sources: https://github.com/anthropics/skills (frontend-design, theme-factory, webapp-testing),
https://github.com/nextlevelbuilder/ui-ux-pro-max-skill, https://github.com/pbakaus/impeccable

## Connectors (MCP)

`.mcp.json` connects the **Magic UI** component library (https://magicui.design), so Claude can pull in
ready-made animated pieces: text effects, animated backgrounds, logo marquees, and more.
