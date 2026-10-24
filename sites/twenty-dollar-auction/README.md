# The $20 Auction: Build Your Dream

A family bidding party game for 2 to 8 players on one shared phone, tablet, laptop or TV.

## Play it
- **Easiest:** open `index.html` in any web browser (double-click it). No install, no internet needed except for fonts and AI paintings.
- **Put it online:** upload `index.html` to any free static host (GitHub Pages, Netlify Drop). It is one self-contained file.

## How it works
- Everyone starts with $20. The host reveals one item at a time; players bid (out loud, or secretly by passing the device).
- The highest bid wins and pays exactly that. Nobody else pays. Nobody can go below $0.
- Every win is drawn into the player's creation right away (house, hero, pizza, movie poster, theme park...).
- At the end the family votes on six awards. The biggest spender does not automatically win.
- Games save in the browser, so a refresh keeps everyone's money.

## AI paintings
After each win the game asks **Pollinations.ai** (free, no account) for a painting that lists every feature the player owns.
While it paints you see a loader; if it fails, the last good painting stays and there is a **Try again** button.
To use a different image service, change `T.AI.buildUrl` in `src/js/ai-sound.js` (it takes a prompt and returns an image URL).
Inside the Claude artifact viewer outside images are blocked, so AI paintings are switched off there; the drawn creations still work.

## Editing
Source lives in `src/`. Mode data (all 30 modes, 10+ rounds each, several random items per round) is in `src/js/modes-*.js`.
Add a mode by adding an object to one of those files, or make one inside the game with **Make your own mode**.
After editing, run `python3 build.py` to rebuild `index.html` and `artifact.html`.
