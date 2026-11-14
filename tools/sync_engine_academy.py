"""Copy Engine Academy from the THECAR project into this repo and make it an installable web app.

Run after every change to the source file:
    python tools/sync_engine_academy.py
Then commit and push. The iPhone/iPad build and the web app both update from docs/engine-academy/.
"""
import hashlib
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.environ.get(
    "ENGINE_ACADEMY_SRC",
    r"C:\Users\danny\OneDrive\Documents\ChatGPT\THECAR\learning-game\engine-academy.html",
)
OUT = os.path.join(ROOT, "docs", "engine-academy")

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#000000">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Engine Academy">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="icon" href="icon-192.png">
"""

SW_REGISTER = """
<script>
// Offline support when served over https (GitHub Pages). Skipped inside the iOS app, which bundles the files.
if ("serviceWorker" in navigator && location.protocol === "https:") {
  navigator.serviceWorker.register("sw.js").catch(() => {});
}
</script>
"""


def main():
    src = open(SRC, encoding="utf-8").read()
    # Drop the source's own charset/viewport lines; HEAD supplies them.
    src = re.sub(r'^\s*<meta charset="utf-8">\s*\n', "", src)
    src = re.sub(r'^\s*<meta name="viewport"[^>]*>\s*\n', "", src)
    html = HEAD + src + SW_REGISTER
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    # Bump the service-worker cache name so phones pick up the new version.
    ver = hashlib.sha256(html.encode("utf-8")).hexdigest()[:10]
    sw_path = os.path.join(OUT, "sw.js")
    sw = open(sw_path, encoding="utf-8").read()
    sw = re.sub(r'const VERSION = "[^"]*";', f'const VERSION = "{ver}";', sw)
    with open(sw_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(sw)
    print(f"synced {len(html):,} bytes, cache version {ver}")


if __name__ == "__main__":
    sys.exit(main())
