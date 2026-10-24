# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

delegated: a dependency-free static web app (HTML, CSS, vanilla JS modules) in `sites/twenty-dollar-auction/`, so it opens from any browser or free static host with no build step or server. The owner said "I just want to play it", so it must open and work with zero setup.

## Users

The owner's own family and friends at game night: 2 to 8 players of mixed ages (kids, teens, adults) crowded around one shared phone, tablet, laptop, or TV. One person acts as host and runs the controls; everyone else watches the shared screen and shouts bids.

## Product Purpose

The $20 Auction: Build Your Dream is a party game. Every player gets $20 of play money, the host reveals one item at a time, players bid, and the winner pays their bid and adds the item to a personal creation (a dream house, superhero, day of food, and 27 more modes). Success is a family understanding the rules in under a minute, laughing through the auctions, and arguing happily over whose creation is best at the end.

## Positioning

The creation is visual and grows with every win: each player's house, hero, menu, or poster is drawn from their structured list of won items and keeps everything earlier, so the money decisions become a picture people react to. Winners are chosen by family vote, never by money spent.

## Operating Context

Played in one room on one shared device, often passed between hands or cast to a TV. The host reads the item aloud, collects shouted bids, types or taps them in, and ends the auction. Sessions last 15 to 40 minutes; families replay with different modes.

## Capabilities and Constraints

- 2 to 8 players, each starting with exactly $20; whole-dollar bids only, never above a player's remaining money, never negative; losers never pay; unclaimed items allowed; host can skip items or end early.
- 30 built-in modes in three categories, each with at least 10 rounds and several random item options per round; host can add custom modes and items.
- Future items stay hidden until the host reveals them.
- Visuals: a built-in illustrated renderer draws every creation from its structured data and updates instantly after each win. On top, an optional AI painting is requested from the free Pollinations image service (confirmed by the owner); while loading, show a loader; on failure, keep the previous image and offer Retry, never pretend it updated.
- Game state persists in the browser between rounds and reloads.
- Final results with side-by-side comparison, family voting categories, and image saving.

## Brand Commitments

Name: "The $20 Auction: Build Your Dream". No client branding; this is a personal family game.

## Evidence on Hand

No existing assets, art, or brand. All item names, descriptions, and illustrations are authored for the game. Movie mode uses generic, legally safe archetypes rather than real actors' likenesses.

## Product Principles

1. Understandable in one minute: one big action at a time, plain words, huge numbers.
2. Money rules are sacred: the state never lies about balances, wins, or images.
3. The creation is the star: every win visibly changes the picture.
4. The host runs the show; players watch the stage.
5. Replayable: randomized items and many modes make every game different.

## Accessibility & Inclusion

Readable from across a room by children and adults; large touch targets for passing one phone around; reduced-motion respected; sound can be muted.
