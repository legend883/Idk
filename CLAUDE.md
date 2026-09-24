# Legend Creative – Website Builds

This repo is used to build client websites. For ANY website, landing page, or UI work, always use
the design tools installed here. Do not produce a generic, template-looking site.

## Required workflow for every website build

1. **impeccable**: load the `impeccable` skill first. If there is no PRODUCT.md, run its init
   interview (ask about the business, customers, feeling, and reference sites) before designing.
2. **ui-ux-pro-max**: run its `--design-system` search for the client's industry and style to pick
   the layout pattern, colors, fonts, and GSAP scroll-animation presets. Persist it with `--persist`.
3. **frontend-design**: follow its principles for a distinctive, non-templated look.
4. **theme-factory**: use it when the client has no brand colors or fonts yet.
5. **Magic UI MCP** (`magicuidesign-mcp`): search it and use its real components for animated
   effects (text reveals, animated backgrounds, marquees, number tickers, shiny buttons, etc.)
   instead of hand-writing them.
6. **webapp-testing**: before showing the user, open the site in the browser, screenshot desktop
   and mobile, fix what looks off, and share the screenshots.
7. Finish with an `impeccable` polish pass.

## Per-client organization

Put each client's site in its own folder: `sites/<client-name>/`.

## Working with the user

The user runs a web design business and is not a developer. Explain things in plain language,
skip jargon, and always show screenshots of the result. Commit and push finished work.
