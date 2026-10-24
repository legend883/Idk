# The $20 Auction (realistic, 2-player)

Live game: https://twenty-dollar-build.higgsfield.app (sign in with Higgsfield to play)

This version replaced the cartoon one in `sites/twenty-dollar-auction/`.
It runs as a Higgsfield app, so the AI can edit each winner's real photo.

- 2 players, $20 each, 5 random items per game from 12 modes (country, car, house, bagel,
  burger, pizza, sundae, gaming setup, bedroom, theme park, sneaker, superhero).
- Starting photos and item photos were made once with Higgsfield (gpt_image_2_5, low quality)
  and ship with the app. `modes.py` holds the prompts, `jobmap.json`/`urls.txt` the source images.
- Each win runs one photo edit (gpt_image_2, low, 1k, about 0.5 credits) on that player's latest
  picture, so earlier wins are kept. Higgsfield asks for approval before each edit.
- Finished games are saved per user (Higgsfield D1 database) under the "My games" tab.

The app's source code lives in the Higgsfield project for this site (React + TanStack Start).
