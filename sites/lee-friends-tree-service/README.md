# Lee Friend's Tree Service – website preview

Private preview of a new site for Lee Friend's Tree Service, Inc. (Loganville, GA).

- Edit facts, copy, services, towns and FAQs in `build.py`, then run `python3 build.py` to regenerate every page, `sitemap.xml`, `robots.txt`, and `CONFIRM-LIST.md`.
- Preview locally: `python3 -m http.server` in this folder, then open http://localhost:8000.
- `CONFIRM-LIST.md` lists every fact to verify with the owner. Each shows on the pages as a yellow [CONFIRM] tag.

## Before going live
1. Resolve every item in CONFIRM-LIST.md (the `confirm(...)` calls in build.py).
2. Remove `<meta name="robots" content="noindex, nofollow">` (in `page()` in build.py) and swap robots.txt for the commented launch version.
3. Add real photos (replace `photo(...)` slots), add the BBB / ISA / Google Maps URLs to `sameAs`.
4. Connect the quote form to an inbox or form service.
