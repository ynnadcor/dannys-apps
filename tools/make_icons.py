"""Draw the Engine Academy icon: black, M-style stripes, white I8. Run: python tools/make_icons.py"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
N = 1024
img = Image.new("RGB", (N, N), (0, 0, 0))
# soft top glow so the black reads as a surface, not a hole
glow = Image.new("L", (N, N), 0)
ImageDraw.Draw(glow).ellipse((-200, -520, N + 200, 520), fill=34)
glow = glow.filter(ImageFilter.GaussianBlur(120))
img.paste(Image.new("RGB", (N, N), (255, 255, 255)), (0, 0), glow)
d = ImageDraw.Draw(img)
cols = [(79, 168, 240), (43, 63, 158), (228, 53, 43)]
w, gap, x0, slant = 46, 16, 150, 120
for i, c in enumerate(cols):
    x = x0 + i * (w + gap)
    d.polygon([(x + slant, 250), (x + slant + w, 250), (x + w, 774), (x, 774)], fill=c)
try:
    f = ImageFont.truetype("C:/Windows/Fonts/bahnschrift.ttf", 520)
    f.set_variation_by_name("Bold Condensed")
except Exception:
    f = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 470)
t = "I8"
bb = d.textbbox((0, 0), t, font=f)
tx = 430 + (N - 430 - 90 - (bb[2] - bb[0])) // 2 - bb[0]
ty = (N - (bb[3] - bb[1])) // 2 - bb[1]
d.text((tx, ty), t, font=f, fill=(244, 244, 245))
img.save(os.path.join(root, "apps/engine-academy/Assets.xcassets/AppIcon.appiconset/icon-1024.png"))
for s in (512, 192, 180):
    img.resize((s, s), Image.LANCZOS).save(os.path.join(root, f"docs/engine-academy/icon-{s}.png"))
img.resize((512, 512), Image.LANCZOS).save(os.path.join(root, "docs/icons/engine-academy-512.png"))
print("icons written")
