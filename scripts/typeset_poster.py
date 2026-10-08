#!/usr/bin/env python3
"""
typeset_poster.py - High-end commercial typography layout engine for negative-space posters.
"""

import argparse
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def typeset_poster(
    image_path,
    output_path,
    label="AURA SERIES",
    headline="Hear Nothing.\nFeel Everything.",
    subheadline="Pure Titanium · 50dB Abyssal ANC\n深海级静谧声学系统 / 航空级钛金属架构",
    theme="dark" # "dark" text for light bg, "light" text for dark/vibrant bg
):
    img = Image.open(image_path).convert("RGBA")
    w, h = img.size

    overlay = Image.new("RGBA", (w, h), (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    # Font selection (macOS system fonts)
    font_large_path = "/System/Library/Fonts/HelveticaNeue.ttc"
    font_sub_path = "/System/Library/Fonts/Supplemental/Songti.ttc"

    font_label = ImageFont.truetype(font_large_path, int(h * 0.016), index=0)
    font_headline = ImageFont.truetype(font_large_path, int(h * 0.046), index=1)
    font_sub = ImageFont.truetype(font_large_path, int(h * 0.016), index=0)
    font_zh = ImageFont.truetype(font_sub_path, int(h * 0.015), index=0)

    if theme == "light":
        primary_color = (255, 255, 255, 245)
        secondary_color = (255, 255, 255, 180)
        line_color = (255, 255, 255, 220)
    else:
        primary_color = (29, 29, 31, 235)      # Apple Slate Black
        secondary_color = (110, 110, 115, 220) # Muted Gray
        line_color = (29, 29, 31, 180)

    # Position in top-left negative space
    x = int(w * 0.09)
    y = int(h * 0.09)

    # 1. Label / Kicker
    spaced_label = "   ".join(label.upper()) if " " not in label else label
    draw.text((x, y), spaced_label, font=font_label, fill=secondary_color)

    # 2. Headline
    lines = headline.split("\n")
    curr_y = y + int(h * 0.036)
    line_spacing = int(h * 0.052)
    for l in lines:
        draw.text((x, curr_y), l, font=font_headline, fill=primary_color)
        curr_y += line_spacing

    # 3. Separator rule
    curr_y += int(h * 0.012)
    draw.line([(x, curr_y), (x + int(w * 0.08), curr_y)], fill=line_color, width=2)
    curr_y += int(h * 0.016)

    # 4. Subheadline
    sub_lines = subheadline.split("\n")
    for i, sl in enumerate(sub_lines):
        f = font_zh if any('\u4e00' <= char <= '\u9fff' for char in sl) else font_sub
        draw.text((x, curr_y), sl, font=f, fill=secondary_color)
        curr_y += int(h * 0.028)

    # Composite & save
    final = Image.alpha_composite(img, overlay).convert("RGB")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    final.save(output_path, quality=95)
    return str(Path(output_path).resolve())

def main():
    parser = argparse.ArgumentParser(description="Typeset commercial typography onto negative space.")
    parser.add_argument("--image", required=True, help="Input image path")
    parser.add_argument("--out", required=True, help="Output poster path")
    parser.add_argument("--label", default="AURA SERIES", help="Top category label")
    parser.add_argument("--headline", default="Hear Nothing.\nFeel Everything.", help="Main headline (use \\n for lines)")
    parser.add_argument("--subheadline", default="Pure Titanium · 50dB Abyssal ANC\n深海级静谧声学系统 / 航空级钛金属架构", help="Subheadline")
    parser.add_argument("--theme", default="dark", choices=["dark", "light"], help="Text color theme")

    args = parser.parse_args()
    headline = args.headline.replace("\\n", "\n")
    subheadline = args.subheadline.replace("\\n", "\n")

    res = typeset_poster(args.image, args.out, args.label, headline, subheadline, args.theme)
    print(f"Successfully generated commercial poster: {res}")

if __name__ == "__main__":
    main()
