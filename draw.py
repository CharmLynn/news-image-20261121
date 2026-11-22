#!/usr/bin/env python3
"""Draw the front page for Saturday, 21 November 2026.

One 1024 by 1024 PNG: a newspaper front page with a masthead, a lead
story in a teal panel, four more stories in a two-by-two grid, and a
footer naming the sources. Pillow draws every letter, so the output is
exact and repeatable: run this file twice and the bytes match.
"""

import math

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
EDGE = 36
GAP = 20

PALETTE = {
    "bg": (246, 241, 231), "fg": (25, 25, 25), "dim": (90, 84, 72),
    "red": (180, 35, 24), "navy": (22, 50, 79), "navy2": (30, 68, 104),
    "teal": (14, 116, 144), "amber": (180, 83, 9), "green": (22, 101, 52),
    "card": (255, 255, 255), "cardline": (210, 203, 188),
    "salmon": (255, 120, 100), "mist": (214, 226, 240),
    "rule": (180, 172, 156), "white": (255, 255, 255),
}

FONTS = {
    "serif_b": "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
    "serif": "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    "sans": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "sans_b": "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
}


def font(kind, size):
    """Load a DejaVu font at the given size."""
    return ImageFont.truetype(FONTS[kind], size)


def wrap(dc, text, fnt, width):
    """Break text into lines no wider than width pixels."""
    words = text.split()
    lines, line, i = [], "", 0
    while i < len(words):
        trial = (line + " " + words[i]).strip()
        if dc.textlength(trial, font=fnt) <= width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = words[i]
        i += 1
    if line:
        lines.append(line)
    return lines


# ------------------------------------------------------------------ glyphs

def glyph_sun(dc, x, y, s, c):
    """A sun with eight rays, for the climate story."""
    cx, cy = x + s * 0.5, y + s * 0.5
    w = max(3, s // 26)
    dc.ellipse([cx - s * 0.24, cy - s * 0.24, cx + s * 0.24, cy + s * 0.24],
               fill=c)
    for k in range(8):
        a = math.radians(k * 45)
        dc.line([cx + s * 0.32 * math.cos(a), cy + s * 0.32 * math.sin(a),
                 cx + s * 0.46 * math.cos(a), cy + s * 0.46 * math.sin(a)],
                fill=c, width=w)


def glyph_bars(dc, x, y, s, c):
    """Prison bars, for the cartel capture story."""
    w = max(3, s // 22)
    for k in range(4):
        px = x + s * (0.12 + 0.24 * k)
        dc.rectangle([px, y + s * 0.08, px + s * 0.10, y + s * 0.92],
                     fill=c)
    dc.rectangle([x + s * 0.06, y + s * 0.08, x + s * 0.94, y + s * 0.18],
                 fill=c)
    dc.rectangle([x + s * 0.06, y + s * 0.82, x + s * 0.94, y + s * 0.92],
                 fill=c)


def glyph_burst(dc, x, y, s, c):
    """An explosion burst, for the missile strike story."""
    cx, cy = x + s * 0.5, y + s * 0.52
    pts = []
    for k in range(16):
        r = s * (0.46 if k % 2 == 0 else 0.20)
        a = math.radians(k * 22.5)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    dc.polygon(pts, fill=c)
    dc.ellipse([cx - s * 0.10, cy - s * 0.10, cx + s * 0.10, cy + s * 0.10],
               fill=PALETTE["bg"])


def glyph_ship(dc, x, y, s, c):
    """A cargo ship on waves, for the Baltic drone strike story."""
    w = max(3, s // 26)
    # hull
    dc.polygon([(x + s * 0.06, y + s * 0.42), (x + s * 0.94, y + s * 0.42),
                (x + s * 0.82, y + s * 0.66), (x + s * 0.18, y + s * 0.66)],
               fill=c)
    # bridge block and funnel
    dc.rectangle([x + s * 0.58, y + s * 0.14, x + s * 0.78, y + s * 0.42],
                 fill=c)
    dc.rectangle([x + s * 0.26, y + s * 0.22, x + s * 0.38, y + s * 0.42],
                 fill=c)
    # waves
    for ry in (0.76, 0.88):
        for k in range(3):
            cx = x + s * (0.18 + 0.32 * k)
            dc.arc([cx - s * 0.14, y + s * ry - s * 0.07,
                    cx + s * 0.14, y + s * ry + s * 0.07],
                   start=180, end=360, fill=c, width=w)


def glyph_mosquito(dc, x, y, s, c):
    """A mosquito with two wings, for the dengue trial story."""
    w = max(3, s // 26)
    cx, cy = x + s * 0.5, y + s * 0.55
    # wings
    dc.ellipse([x + s * 0.08, y + s * 0.10, x + s * 0.46, y + s * 0.48],
               outline=c, width=w)
    dc.ellipse([x + s * 0.54, y + s * 0.10, x + s * 0.92, y + s * 0.48],
               outline=c, width=w)
    # body
    dc.ellipse([cx - s * 0.09, cy - s * 0.22, cx + s * 0.09, cy + s * 0.22],
               fill=c)
    # head and legs
    dc.ellipse([cx - s * 0.07, cy - s * 0.32, cx + s * 0.07, cy - s * 0.20],
               fill=c)
    for lx in (0.30, 0.50, 0.70):
        dc.line([x + s * lx, cy + s * 0.10, x + s * (lx - 0.12),
                 y + s * 0.92], fill=c, width=w)
        dc.line([x + s * lx, cy + s * 0.10, x + s * (lx + 0.12),
                 y + s * 0.92], fill=c, width=w)


# ------------------------------------------------------------------ content

LEAD = ("CLIMATE",
        "COP31 talks run into\novertime in Antalya",
        "Negotiators miss the Friday deadline, deadlocked over a "
        "draft deal with no mention of fossil fuels; a third text "
        "is due on Saturday.")

# Each story: kicker, colour key, glyph, headline, body.
STORIES = [
    ("JUSTICE", "navy", glyph_bars,
     "Mexico captures 'El Chapo Isidro'",
     "Special forces seize FBI most-wanted Fausto Isidro Meza "
     "Flores in Guasave; four soldiers and seven gunmen are "
     "killed."),
    ("WAR", "red", glyph_burst,
     "Russian strike hits Zelensky's home city",
     "Ballistic missiles hit Kryvyi Rih on Friday night; a boy of "
     "7 and a woman of 20 are killed and 60 people are wounded."),
    ("WAR AT SEA", "teal", glyph_ship,
     "Drones set Russian cargo ship ablaze",
     "The Sparta II, bound for Kaliningrad, is hit in the Gulf of "
     "Finland; its crew of 16 is evacuated as it drifts into "
     "Finnish waters."),
    ("SCIENCE", "green", glyph_mosquito,
     "Mosquitoes cut dengue by 69% in Brazil trial",
     "Wolbachia-carrying mosquitoes cut dengue and chikungunya in "
     "schoolchildren in Belo Horizonte, researchers report."),
]

SOURCES = ("Sources: Reuters · AP · Al Jazeera · Hurriyet Daily News · "
           "The Straits Times")
NOTE = "All events happened or were first reported on 21 November 2026."


# ------------------------------------------------------------------ drawing

def masthead(dc):
    """Title, date and tagline, with a rule underneath."""
    dc.text((EDGE, 34), "THE WORLD IN ONE DAY", font=font("sans_b", 26),
            fill=PALETTE["red"])
    dc.text((EDGE, 66), "Saturday, 21 November 2026", font=font("serif_b", 50),
            fill=PALETTE["fg"])
    dc.text((EDGE, 136), "Five stories that defined the day  ·  reported "
            "around the world", font=font("sans", 24), fill=PALETTE["dim"])
    dc.line([(EDGE, 176), (W - EDGE, 176)], fill=PALETTE["fg"], width=4)


def lead_panel(dc):
    """The lead story in a teal panel with a sun glyph."""
    top, height = 194, 264
    width = W - 2 * EDGE
    dc.rounded_rectangle([EDGE, top, EDGE + width, top + height], radius=10,
                         fill=PALETTE["teal"])
    px = EDGE + width - 250
    dc.rounded_rectangle([px + 8, top + 8, EDGE + width - 8, top + height - 8],
                         radius=8, fill=(18, 139, 170))
    glyph_sun(dc, px + 45, top + 58, 160, PALETTE["mist"])
    tx = EDGE + 28
    dc.text((tx, top + 22), LEAD[0], font=font("sans_b", 24),
            fill=PALETTE["salmon"])
    y = top + 58
    for ln in LEAD[1].split("\n"):
        dc.text((tx, y), ln, font=font("serif_b", 46), fill=PALETTE["white"])
        y += 54
    bf = font("sans", 23)
    y += 8
    for ln in wrap(dc, LEAD[2], bf, px - tx - 30):
        dc.text((tx, y), ln, font=bf, fill=PALETTE["mist"])
        y += 30


def cards(dc):
    """Four stories in a two-by-two grid of white cards."""
    top = 482
    cw = (W - 2 * EDGE - GAP) // 2
    ch = 216
    for pos, (kick, col, glyph, head, body) in enumerate(STORIES):
        x = EDGE + (pos % 2) * (cw + GAP)
        y = top + (pos // 2) * (ch + GAP)
        colour = PALETTE[col]
        dc.rounded_rectangle([x, y, x + cw, y + ch], radius=10,
                             fill=PALETTE["card"], outline=PALETTE["cardline"],
                             width=2)
        glyph(dc, x + 18, y + 16, 48, colour)
        dc.text((x + 78, y + 26), kick, font=font("sans_b", 20), fill=colour)
        hf, bf = font("serif_b", 29), font("sans", 19)
        yt = y + 74
        for ln in wrap(dc, head, hf, cw - 36)[:2]:
            dc.text((x + 18, yt), ln, font=hf, fill=PALETTE["fg"])
            yt += 35
        yt += 4
        for ln in wrap(dc, body, bf, cw - 36)[:3]:
            dc.text((x + 18, yt), ln, font=bf, fill=PALETTE["dim"])
            yt += 24
    return top + 2 * ch + GAP


def footer(dc, bottom):
    """Source line and date note under a hairline rule."""
    y = bottom + 12
    dc.line([(EDGE, y), (W - EDGE, y)], fill=PALETTE["rule"], width=2)
    ff = font("sans", 18)
    dc.text((EDGE, y + 10), SOURCES, font=ff, fill=PALETTE["dim"])
    dc.text((EDGE, y + 34), NOTE, font=ff, fill=PALETTE["dim"])


def build():
    """Render the page and save it as entry.png."""
    img = Image.new("RGB", (W, H), PALETTE["bg"])
    dc = ImageDraw.Draw(img)
    masthead(dc)
    lead_panel(dc)
    footer(dc, cards(dc))
    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    build()
