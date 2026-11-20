#!/usr/bin/env python3
"""Render 1024x1024 world-news front page for 20 Nov 2026 (6 stories, illustrated)."""
from PIL import Image, ImageDraw, ImageFont
import math
W = H = 1024
PAPER = (243, 237, 224); INK = (16, 16, 22); NAVY = (14, 32, 58); RED = (172, 22, 32)
GOLD = (190, 146, 38); TEAL = (10, 88, 94); GREY = (74, 74, 84); LIGHT = (208, 198, 176)
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
f_mast = ImageFont.truetype(BOLD, 58); f_date = ImageFont.truetype(REG, 24)
f_head = ImageFont.truetype(BOLD, 19); f_body = ImageFont.truetype(REG, 13)
f_kick = ImageFont.truetype(BOLD, 14); f_tag = ImageFont.truetype(BOLD, 17)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 112], fill=NAVY)
d.text((34, 12), "THE WORLD IN ONE DAY", font=f_mast, fill=(244, 238, 222))
d.text((36, 80), "FRIDAY \u00b7 20 NOVEMBER 2026 \u00b7 WORLD EDITION No. 20", font=f_date, fill=GOLD)
d.text((W-320, 84), "\u2691  PEACE DECLARATION ISSUED", font=f_tag, fill=(244, 238, 222))
d.line([30, 124, W-30, 124], fill=INK, width=3)

# banner headline strip
d.rectangle([30, 130, W-30, 196], fill=(238, 226, 200))
d.text((44, 142), "BANNER: THREE PRESIDENTS, ONE TABLE \u2014 \u201cA NUCLEAR WAR CANNOT BE WON\u201d", font=f_tag, fill=INK)
d.line([30, 202, W-30, 202], fill=INK, width=2)

# ---------- panel geometry (3 x 2 grid) ----------
col_w = (W - 60 - 32) // 3
cols = [(30, 30 + col_w), (30 + col_w + 16, 30 + 2 * col_w + 16), (30 + 2 * col_w + 32, 30 + 3 * col_w + 32)]
bh = 304
rows_y = [214, 214 + bh + 14]
assert rows_y[1] + bh < H - 118, (rows_y[1] + bh, H - 118)

def wrap(text, font, width):
    words = text.split(" "); lines = []; cur = ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) > width: lines.append(cur); cur = w_
        else: cur = t
    lines.append(cur)
    return lines

def panel(i, kick, head, body, accent, draw_icon):
    x, xe = cols[i % 3]
    y = rows_y[i // 3]
    d.rectangle([x, y, xe, y + bh], outline=INK, width=2, fill=PAPER)
    d.rectangle([x, y, xe, y + 32], fill=accent)
    d.text((x + 12, y + 9), f"{i+1}.  {kick}", font=f_kick, fill=(244, 238, 222))
    ty = y + 42
    for ln in wrap(head, f_head, xe - x - 24)[:2]:
        d.text((x + 12, ty), ln, font=f_head, fill=INK); ty += 24
    # illustration box
    ib_x, ib_y, ib_h = x + 12, ty + 6, 132
    d.rectangle([ib_x, ib_y, xe - 12, ib_y + ib_h], fill=(230, 222, 202), outline=INK, width=1)
    draw_icon((ib_x + xe - 12) / 2, ib_y + ib_h / 2)
    ty = ib_y + ib_h + 10
    for ln in wrap(body, f_body, xe - x - 24)[:3]:
        d.text((x + 12, ty), ln, font=f_body, fill=GREY); ty += 17
    return x, y

# icon 1: three leader silhouettes + table + sun
def icon_leaders(cx, cy):
    d.ellipse([cx-110, cy-44, cx-70, cy-4], fill=INK)      # head 1
    d.rectangle([cx-104, cy-2, cx-76, cy+40], fill=INK)
    d.ellipse([cx-20, cy-48, cx+20, cy-8], fill=INK)       # head 2 (center, taller)
    d.rectangle([cx-14, cy-6, cx+14, cy+42], fill=INK)
    d.ellipse([cx+70, cy-44, cx+110, cy-4], fill=INK)      # head 3
    d.rectangle([cx+76, cy-2, cx+104, cy+40], fill=INK)
    d.rectangle([cx-120, cy+42, cx+120, cy+50], fill=NAVY) # table
    # sun rays
    d.ellipse([cx+118, cy-60, cx+140, cy-38], fill=GOLD)
    for a in range(0, 360, 45):
        r1, r2 = 13, 19
        d.line([cx+129+ r1*math.cos(math.radians(a)), cy-49 + r1*math.sin(math.radians(a)),
                cx+129 + r2*math.cos(math.radians(a)), cy-49 + r2*math.sin(math.radians(a))], fill=GOLD, width=2)

# icon 2: tower with impact burst
def icon_tower(cx, cy):
    for k, wdt in enumerate([34, 26, 18]):
        top = cy + 46 - k*34
        d.rectangle([cx-wdt//2, top, cx+wdt//2, top+30], outline=INK, width=2, fill=(210, 200, 178))
    d.line([cx-10, cy+46, cx-4, cy-46], fill=RED, width=3)   # incoming trajectory
    d.line([cx-22, cy+40, cx-2, cy-52], fill=RED, width=2)
    for a in range(0, 360, 40):
        d.line([cx, cy-50, cx + 16*math.cos(math.radians(a)), cy-50 + 16*math.sin(math.radians(a))], fill=RED, width=2)
    d.polygon([(cx-8, cy-58), (cx+8, cy-58), (cx, cy-70)], fill=RED)

# icon 3: NATO map (east-west) with arrows and flag
def icon_map(cx, cy):
    d.ellipse([cx-100, cy-44, cx+100, cy+46], outline=INK, width=2, fill=(214, 206, 186))
    d.line([cx-60, cy-40, cx-64, cy+44], fill=INK, width=2)
    d.line([cx+10, cy-44, cx+4, cy+46], fill=INK, width=2)
    d.text((cx-92, cy-6), "EU", font=f_kick, fill=NAVY)
    d.text((cx-46, cy-2), "UA", font=f_kick, fill=RED)
    d.text((cx+36, cy-6), "RU", font=f_kick, fill=INK)
    d.line([cx-70, cy-16, cx+26, cy-34], fill=TEAL, width=3)
    d.polygon([(cx+30, cy-36), (cx+20, cy-30), (cx+22, cy-40)], fill=TEAL)
    d.text((cx-40, cy+26), "NATO \u2194 land swap", font=ImageFont.truetype(REG, 11), fill=GREY)

# icon 4: barrel + falling chart
def icon_oil(cx, cy):
    d.rectangle([cx-116, cy+20, cx+60, cy+50], outline=INK, width=2, fill=(196, 118, 40))
    d.ellipse([cx-116, cy+12, cx+60, cy+28], fill=(224, 160, 74))
    d.text((cx-104, cy+28), "BRENT", font=f_kick, fill=INK)
    pts = [(cx+70 + k*5, cy-44 + v) for k, v in enumerate([0, 6, 3, 10, 7, 14, 12, 20])]
    d.line(pts, fill=RED, width=3)
    d.polygon([(pts[-1][0]+4, pts[-1][1]-6), (pts[-1][0]-6, pts[-1][1]-2), (pts[-1][0]+2, pts[-1][1]+8)], fill=RED)
    d.text((cx+62, cy+30), "-15%", font=f_tag, fill=RED)

# icon 5: chip with flag halves
def icon_chip(cx, cy):
    d.rectangle([cx-36, cy-36, cx+36, cy+36], outline=INK, width=2, fill=(40, 70, 110))
    d.rectangle([cx-24, cy-24, cx+24, cy+24], fill=GOLD)
    d.text((cx-18, cy-12), "AI", font=ImageFont.truetype(BOLD, 26), fill=INK)
    for k in range(-30, 31, 15):
        d.line([cx+k, cy-36, cx+k, cy-48], fill=INK, width=2)
        d.line([cx+k, cy+36, cx+k, cy+48], fill=INK, width=2)
        d.line([cx-36, cy+k, cx-48, cy+k], fill=INK, width=2)
        d.line([cx+36, cy+k, cx+48, cy+k], fill=INK, width=2)
    d.line([cx-90, cy-50, cx-60, cy-30], fill=RED, width=3)
    d.text((cx-96, cy+20), "US rules", font=f_kick, fill=RED)
    d.text((cx+56, cy+20), "Beijing", font=f_kick, fill=NAVY)

# icon 6: pills + chart up
def icon_pills(cx, cy):
    d.rectangle([cx-70, cy-8, cx-10, cy+24], outline=INK, width=2, fill=(226, 226, 230))
    d.ellipse([cx-70, cy-8, cx-10, cy+4], fill=(150, 190, 210))
    d.line([cx-40, cy-8, cx-40, cy+24], fill=INK, width=2)
    d.ellipse([cx+8, cy-16, cx+44, cy+20], outline=INK, width=2, fill=(240, 200, 120))
    d.line([cx+26, cy-16, cx+26, cy+20], fill=INK, width=2)
    pts = [(cx+56 + k*7, cy+34 - v) for k, v in enumerate([4, 8, 6, 12, 10, 16])]
    d.line(pts, fill=TEAL, width=3)
    d.text((cx+56, cy-6), "steady", font=f_kick, fill=TEAL)

stories = [
    ("SUMMIT \u00b7 SHENZHEN", "Xi, Putin, Trump sign first trilateral peace pact",
     "Historic 3-way US\u2013Russia\u2013China summit ends with a joint declaration and a nuclear-risk dialogue.", TEAL, icon_leaders),
    ("SAUDI ARABIA", "Houthi missile strike rocks Riyadh skyscraper",
     "A projectile struck the PIF tower \u2014 militants now overlook the Red Sea's key shipping lanes.", RED, icon_tower),
    ("UKRAINE", "US floats NATO membership-for-land deal",
     "Trump's envoys sound out Kyiv and Europe on ending the war by trading territory for NATO membership.", NAVY, icon_map),
    ("ENERGY", "Oil cools 15% as Hormuz flows grow",
     "Benchmarks retreat as traders weigh Middle East risks against rising Gulf and Suez shipments.", GOLD, icon_oil),
    ("TECH \u00b7 AI", "China's AI industry faces Nvidia withdrawal",
     "New US rules after the Nvidia scandal threaten the chip supply behind China's AI champions.", RED, icon_chip),
    ("BUSINESS", "Novartis calms investors on patents",
     "The drugmaker lays out growth plans through a coming wave of patent expirations; shares steady.", TEAL, icon_pills),
]

for i, s in enumerate(stories):
    panel(i, *s)

# ---------- pull-quote strip to fill the gap ----------
qy = rows_y[1] + bh + 14
d.rectangle([30, qy, W-30, qy + 56], fill=(238, 226, 200), outline=INK, width=2)
d.text((48, qy + 8), "\u201cPeace among major countries brings stability to the world.\u201d", font=ImageFont.truetype(BOLD, 20), fill=INK)
d.text((48, qy + 36), "\u2014 joint statement of the Shenzhen summit, yesterday", font=f_body, fill=GREY)

# ---------- footer data strip ----------
fy = H - 108
d.rectangle([30, fy, W-30, fy + 78], fill=NAVY)
d.text((48, fy + 12), "MARKETS", font=f_kick, fill=GOLD)
d.text((48, fy + 38), "Brent \u25bc 15% \u00b7 Hormuz flows \u25b2 \u00b7 Novartis \u25b2 2%", font=f_body, fill=(210, 218, 232))
d.line([420, fy + 8, 420, fy + 70], fill=(70, 90, 120), width=2)
d.text((440, fy + 12), "OF NOTE", font=f_kick, fill=GOLD)
d.text((440, fy + 38), "AI chips, oil lanes and NATO maps moved the world today.", font=f_body, fill=(210, 218, 232))
d.line([W-30, fy + 78, 30, fy + 78], fill=INK, width=3)

img.save("/root/makefun/news20/entry.png")
print("bytes:", __import__("os").path.getsize("/root/makefun/news20/entry.png"))
