#!/usr/bin/env python3
"""Downloads the preview's sample photos into assets/photos/ as web-sized JPEGs.

These are AI-generated samples (Higgsfield), labeled "Sample photo" on every page.
Replace them with the owner's real job photos before launch (same file names).
Needs Pillow: pip install pillow. Run: python3 get-photos.py
"""
import io
import urllib.request
from pathlib import Path

from PIL import Image

BASE = "https://d8j0ntlcm91z4.cloudfront.net/user_2y9epIre1Mp5IxObA3BfNJCh26e/"
PHOTOS = {
    "hero": "hf_20261026_053000_ee4dc718-567d-4f91-b3da-c6c68d4089f2.png",
    "removal": "hf_20261026_053001_73ca0eae-758f-4439-bfaa-604bc2881ada.png",
    "trimming": "hf_20261026_053000_61cf7ed1-706a-4b1b-aec7-396c30c9e495.png",
    "storm": "hf_20261026_053000_a3c3b921-41d1-4e15-9396-d91067f1f6a8.png",
    "stump": "hf_20261026_052959_2add8953-11b6-434a-b148-5803de3fcb27.png",
    "recycling": "hf_20261026_053001_8a3d1f1f-f356-42fc-8201-dcb3b04c9bb6.png",
    "firewood": "hf_20261026_053001_6505442a-7e39-4e6a-b3fd-ef428b63fb33.png",
    "arborist": "hf_20261026_053001_664a633c-2a67-4f07-9cac-aeb1791a9027.png",
    "dusk": "hf_20261026_053001_683ae4e7-f33e-42ce-ab63-39a02d56e7e8.png",
    "aerial": "hf_20261026_052959_06c3e5a6-d902-47dc-bbcd-94bc9f5deda1.png",
}
WIDE = {"hero": 2200, "dusk": 2000, "aerial": 2000}

out = Path(__file__).parent / "assets" / "photos"
out.mkdir(parents=True, exist_ok=True)
for key, name in PHOTOS.items():
    with urllib.request.urlopen(BASE + name, timeout=60) as r:
        img = Image.open(io.BytesIO(r.read())).convert("RGB")
    width = WIDE.get(key, 1400)
    if img.width > width:
        img = img.resize((width, round(img.height * width / img.width)), Image.LANCZOS)
    img.save(out / f"{key}.jpg", "JPEG", quality=76, progressive=True, optimize=True)
    print(f"{key}.jpg {img.width}x{img.height} {(out / f'{key}.jpg').stat().st_size // 1024} KB")
