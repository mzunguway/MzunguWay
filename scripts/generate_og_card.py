from io import BytesIO
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
WIDTH, HEIGHT = 1200, 630

CREAM = "#F5F2EA"
WHITE = "#FFFFFF"
NAVY = "#101B2B"
MUTED = "#B9C2CE"
GOLD = "#B78A2D"
GOLD_LIGHT = "#D9BD7D"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    filename = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{filename}", size=size)


def spaced_text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fill: str, face: ImageFont.FreeTypeFont, spacing: int) -> None:
    x, y = xy
    for character in text:
        draw.text((x, y), character, fill=fill, font=face)
        bounds = draw.textbbox((x, y), character, font=face)
        x += bounds[2] - bounds[0] + spacing


def main() -> None:
    image = Image.new("RGB", (WIDTH, HEIGHT), CREAM)
    draw = ImageDraw.Draw(image)

    draw.ellipse((850, -175, 1330, 305), fill="#EEE4CD")
    draw.ellipse((-95, 455, 245, 795), fill="#ECE9E0")
    draw.rounded_rectangle((42, 42, 1158, 588), radius=38, fill=NAVY)

    draw.rounded_rectangle((79, 76, 475, 180), radius=20, fill=WHITE)
    logo_bytes = cairosvg.svg2png(
        url=str(ROOT / "brand-wordmark.svg"),
        output_width=340,
        output_height=97,
    )
    logo = Image.open(BytesIO(logo_bytes)).convert("RGBA")
    image.paste(logo, (106, 79), logo)

    spaced_text(draw, (80, 226), "CURATED DOMAIN NAMING STUDIO", GOLD_LIGHT, font(17, bold=True), 3)
    draw.text((76, 294), "Names worth building", fill=WHITE, font=font(60, bold=True))
    draw.text((76, 368), "a company around.", fill=WHITE, font=font(60, bold=True))

    draw.line((80, 487, 1120, 487), fill="#354052", width=2)
    spaced_text(draw, (80, 519), "AI  •  SECURITY  •  VOICE  •  TRUST", MUTED, font(17, bold=True), 1)
    right_text = "MzunguWay.com"
    right_box = draw.textbbox((0, 0), right_text, font=font(19, bold=True))
    draw.text((1120 - (right_box[2] - right_box[0]), 519), right_text, fill=GOLD_LIGHT, font=font(19, bold=True))

    image.save(ROOT / "og-card.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
