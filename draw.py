#!/usr/bin/env python3
"""Paint the front page for Saturday, 21 November 2026.

The program draws one 1024 by 1024 PNG with Pillow: a masthead, one
lead story in a coloured panel, four more stories on cards in a grid,
and a footer that names the sources. Every letter is drawn by code,
so the picture is exact and repeatable -- run it twice and the file
comes out byte for byte the same.

    python3 draw.py        # writes entry.png beside this file
"""

import math

from PIL import Image, ImageDraw, ImageFont

PAGE_W, PAGE_H = 1024, 1024
MARGIN = 36
GUTTER = 20

# Flat newsprint palette: warm paper, dark ink, one colour per story.
INK = {
    "paper": (246, 241, 231),
    "ink": (25, 25, 25),
    "grey": (90, 84, 72),
    "scarlet": (180, 35, 24),
    "deep": (22, 50, 79),
    "deep2": (30, 68, 104),
    "ocean": (14, 116, 144),
    "ocean2": (18, 139, 170),
    "rust": (180, 83, 9),
    "leaf": (22, 101, 52),
    "card": (255, 255, 255),
    "card_edge": (210, 203, 188),
    "coral": (255, 120, 100),
    "pale": (214, 226, 240),
    "hairline": (180, 172, 156),
    "snow": (255, 255, 255),
}

TYPEFACES = {
    "title_b": "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
    "title": "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    "body": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "body_b": "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
}


def typeface(kind, size):
    """Load one of the DejaVu faces at the given size."""
    return ImageFont.truetype(TYPEFACES[kind], size)


def split_lines(pen, text, face, max_width):
    """Chop text into lines that each fit inside max_width pixels."""
    words = text.split()
    done = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        if pen.textlength(trial, font=face) <= max_width:
            current = trial
        else:
            if current:
                done.append(current)
            current = word
    if current:
        done.append(current)
    return done


# ---------------------------------------------------------------- icons

def icon_sun(pen, left, top, size, colour):
    """Sun disc with eight rays, for the climate lead."""
    cx = left + size * 0.5
    cy = top + size * 0.5
    stroke = max(3, size // 26)
    pen.ellipse(
        [cx - size * 0.24, cy - size * 0.24,
         cx + size * 0.24, cy + size * 0.24],
        fill=colour,
    )
    for step in range(8):
        angle = math.radians(step * 45)
        pen.line(
            [cx + size * 0.32 * math.cos(angle),
             cy + size * 0.32 * math.sin(angle),
             cx + size * 0.46 * math.cos(angle),
             cy + size * 0.46 * math.sin(angle)],
            fill=colour, width=stroke,
        )


def icon_bars(pen, left, top, size, colour):
    """Four prison bars with rails, for the cartel capture."""
    bar = max(3, size // 22)
    for index in range(4):
        bx = left + size * (0.12 + 0.24 * index)
        pen.rectangle(
            [bx, top + size * 0.08, bx + size * 0.10, top + size * 0.92],
            fill=colour,
        )
    pen.rectangle(
        [left + size * 0.06, top + size * 0.08,
         left + size * 0.94, top + size * 0.18],
        fill=colour,
    )
    pen.rectangle(
        [left + size * 0.06, top + size * 0.82,
         left + size * 0.94, top + size * 0.92],
        fill=colour,
    )


def icon_burst(pen, left, top, size, colour):
    """Twelve-point blast, for the missile strike."""
    cx = left + size * 0.5
    cy = top + size * 0.52
    points = []
    for index in range(24):
        radius = size * (0.46 if index % 2 == 0 else 0.20)
        angle = math.radians(index * 15)
        points.append(
            (cx + radius * math.cos(angle), cy + radius * math.sin(angle))
        )
    pen.polygon(points, fill=colour)
    pen.ellipse(
        [cx - size * 0.10, cy - size * 0.10,
         cx + size * 0.10, cy + size * 0.10],
        fill=INK["paper"],
    )


def icon_ship(pen, left, top, size, colour):
    """Cargo ship over two wave lines, for the Baltic strike."""
    stroke = max(3, size // 26)
    pen.polygon(
        [(left + size * 0.06, top + size * 0.42),
         (left + size * 0.94, top + size * 0.42),
         (left + size * 0.82, top + size * 0.66),
         (left + size * 0.18, top + size * 0.66)],
        fill=colour,
    )
    pen.rectangle(
        [left + size * 0.58, top + size * 0.14,
         left + size * 0.78, top + size * 0.42],
        fill=colour,
    )
    pen.rectangle(
        [left + size * 0.26, top + size * 0.22,
         left + size * 0.38, top + size * 0.42],
        fill=colour,
    )
    for row in (0.76, 0.88):
        for index in range(3):
            wx = left + size * (0.18 + 0.32 * index)
            pen.arc(
                [wx - size * 0.14, top + size * row - size * 0.07,
                 wx + size * 0.14, top + size * row + size * 0.07],
                start=180, end=360, fill=colour, width=stroke,
            )


def icon_bug(pen, left, top, size, colour):
    """Mosquito with two wings, for the dengue trial."""
    stroke = max(3, size // 26)
    cx = left + size * 0.5
    cy = top + size * 0.55
    pen.ellipse(
        [left + size * 0.08, top + size * 0.10,
         left + size * 0.46, top + size * 0.48],
        outline=colour, width=stroke,
    )
    pen.ellipse(
        [left + size * 0.54, top + size * 0.10,
         left + size * 0.92, top + size * 0.48],
        outline=colour, width=stroke,
    )
    pen.ellipse(
        [cx - size * 0.09, cy - size * 0.22,
         cx + size * 0.09, cy + size * 0.22],
        fill=colour,
    )
    pen.ellipse(
        [cx - size * 0.07, cy - size * 0.32,
         cx + size * 0.07, cy - size * 0.20],
        fill=colour,
    )
    for leg in (0.30, 0.50, 0.70):
        pen.line(
            [left + size * leg, cy + size * 0.10,
             left + size * (leg - 0.12), top + size * 0.92],
            fill=colour, width=stroke,
        )
        pen.line(
            [left + size * leg, cy + size * 0.10,
             left + size * (leg + 0.12), top + size * 0.92],
            fill=colour, width=stroke,
        )


# ---------------------------------------------------------------- stories

# The lead: kicker, headline lines, standfirst.
LEAD_KICKER = "CLIMATE"
LEAD_HEAD = ["COP31 talks run into", "overtime in Antalya"]
LEAD_BODY = (
    "Negotiators miss the Friday deadline, deadlocked over a draft "
    "deal with no mention of fossil fuels; a third text is due on "
    "Saturday."
)

# The four cards: kicker, ink colour, icon, headline, standfirst.
GRID = [
    (
        "JUSTICE", "deep", icon_bars,
        "Mexico captures 'El Chapo Isidro'",
        "Special forces seize FBI most-wanted Fausto Isidro Meza "
        "Flores in Guasave; four soldiers and seven gunmen are "
        "killed.",
    ),
    (
        "WAR", "scarlet", icon_burst,
        "Russian strike hits Zelensky's home city",
        "Ballistic missiles hit Kryvyi Rih on Friday night; a boy "
        "of 7 and a woman of 20 are killed and 60 people are "
        "wounded.",
    ),
    (
        "WAR AT SEA", "ocean", icon_ship,
        "Drones set Russian cargo ship ablaze",
        "The Sparta II, bound for Kaliningrad, is hit in the Gulf "
        "of Finland; its crew of 16 is evacuated as it drifts into "
        "Finnish waters.",
    ),
    (
        "SCIENCE", "leaf", icon_bug,
        "Mosquitoes cut dengue by 69% in Brazil trial",
        "Wolbachia-carrying mosquitoes cut dengue and chikungunya "
        "in schoolchildren in Belo Horizonte, researchers report.",
    ),
]

SOURCE_LINE = (
    "Sources: Reuters · AP · Al Jazeera · Hurriyet Daily News · "
    "The Straits Times"
)
DATE_LINE = "All events happened or were first reported on 21 November 2026."


# ---------------------------------------------------------------- painting

def paint_header(pen):
    """Newspaper name, date, tagline and a heavy rule."""
    pen.text(
        (MARGIN, 34), "THE WORLD IN ONE DAY",
        font=typeface("body_b", 26), fill=INK["scarlet"],
    )
    pen.text(
        (MARGIN, 66), "Saturday, 21 November 2026",
        font=typeface("title_b", 50), fill=INK["ink"],
    )
    pen.text(
        (MARGIN, 136),
        "Five stories that defined the day  ·  reported around the world",
        font=typeface("body", 24), fill=INK["grey"],
    )
    pen.line(
        [(MARGIN, 176), (PAGE_W - MARGIN, 176)],
        fill=INK["ink"], width=4,
    )


def paint_lead(pen):
    """Lead story: a teal panel, sun icon on the right."""
    top = 194
    height = 264
    width = PAGE_W - 2 * MARGIN
    pen.rounded_rectangle(
        [MARGIN, top, MARGIN + width, top + height],
        radius=10, fill=INK["ocean"],
    )
    icon_left = MARGIN + width - 250
    pen.rounded_rectangle(
        [icon_left + 8, top + 8, MARGIN + width - 8, top + height - 8],
        radius=8, fill=INK["ocean2"],
    )
    icon_sun(pen, icon_left + 45, top + 58, 160, INK["pale"])
    text_left = MARGIN + 28
    pen.text(
        (text_left, top + 22), LEAD_KICKER,
        font=typeface("body_b", 24), fill=INK["coral"],
    )
    cursor = top + 58
    for line in LEAD_HEAD:
        pen.text(
            (text_left, cursor), line,
            font=typeface("title_b", 46), fill=INK["snow"],
        )
        cursor += 54
    body_face = typeface("body", 23)
    cursor += 8
    for line in split_lines(pen, LEAD_BODY, body_face, icon_left - text_left - 30):
        pen.text((text_left, cursor), line, font=body_face, fill=INK["pale"])
        cursor += 30


def paint_card(pen, left, top, width, height, story):
    """One grid card: icon, kicker, headline, standfirst."""
    kicker, colour_key, icon, headline, standfirst = story
    colour = INK[colour_key]
    pen.rounded_rectangle(
        [left, top, left + width, top + height],
        radius=10, fill=INK["card"], outline=INK["card_edge"], width=2,
    )
    icon(pen, left + 18, top + 16, 48, colour)
    pen.text(
        (left + 78, top + 26), kicker,
        font=typeface("body_b", 20), fill=colour,
    )
    head_face = typeface("title_b", 29)
    body_face = typeface("body", 19)
    cursor = top + 74
    for line in split_lines(pen, headline, head_face, width - 36)[:2]:
        pen.text((left + 18, cursor), line, font=head_face, fill=INK["ink"])
        cursor += 35
    cursor += 4
    for line in split_lines(pen, standfirst, body_face, width - 36)[:3]:
        pen.text((left + 18, cursor), line, font=body_face, fill=INK["grey"])
        cursor += 24


def paint_grid(pen):
    """Four cards in a two-by-two grid; returns the grid's bottom."""
    top = 482
    card_w = (PAGE_W - 2 * MARGIN - GUTTER) // 2
    card_h = 216
    for position, story in enumerate(GRID):
        left = MARGIN + (position % 2) * (card_w + GUTTER)
        top_edge = top + (position // 2) * (card_h + GUTTER)
        paint_card(pen, left, top_edge, card_w, card_h, story)
    return top + 2 * card_h + GUTTER


def paint_footer(pen, bottom):
    """Hairline rule, source line and date line."""
    rule_y = bottom + 12
    pen.line(
        [(MARGIN, rule_y), (PAGE_W - MARGIN, rule_y)],
        fill=INK["hairline"], width=2,
    )
    foot_face = typeface("body", 18)
    pen.text((MARGIN, rule_y + 10), SOURCE_LINE, font=foot_face, fill=INK["grey"])
    pen.text((MARGIN, rule_y + 34), DATE_LINE, font=foot_face, fill=INK["grey"])


def render():
    """Paint the whole page and save it as entry.png."""
    page = Image.new("RGB", (PAGE_W, PAGE_H), INK["paper"])
    pen = ImageDraw.Draw(page)
    paint_header(pen)
    paint_lead(pen)
    paint_footer(pen, paint_grid(pen))
    page.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    render()
