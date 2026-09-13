# -*- coding: utf-8 -*-
"""生成普吉行程 App 图标（热带渐变 + 文字）"""
from PIL import Image, ImageDraw, ImageFont

def gradient(size, c1, c2):
    base = Image.new("RGB", (size, size), c1); top = Image.new("RGB", (size, size), c2)
    mask = Image.new("L", (size, size)); md = mask.load()
    for y in range(size):
        for x in range(size):
            md[x, y] = int(255 * ((x + y) / (2 * size)))
    base.paste(top, (0, 0), mask); return base.convert("RGBA")

def make(size):
    r = int(size * 0.22)
    grad = gradient(size, (14, 165, 164), (56, 189, 248))  # teal -> sky
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, size, size], radius=r, fill=255)
    icon = Image.new("RGBA", (size, size), (0, 0, 0, 0)); icon.paste(grad, (0, 0), mask)
    d = ImageDraw.Draw(icon)
    txt = "\U0001F3DD"  # 🏝
    drawn = False
    for fp in ["seguiemj.ttf", "seguisym.ttf"]:
        try:
            f = ImageFont.truetype(fp, int(size * 0.5))
            bb = d.textbbox((0, 0), txt, font=f, embedded_color=True)
            w, h = bb[2] - bb[0], bb[3] - bb[1]
            d.text(((size - w) / 2 - bb[0], (size - h) / 2 - bb[1]), txt, font=f, embedded_color=True)
            drawn = True; break
        except Exception:
            continue
    if not drawn:
        for fp in ["msyhbd.ttc", "msyh.ttc", "simhei.ttf"]:
            try:
                f = ImageFont.truetype(fp, int(size * 0.34))
                t = "普吉"
                bb = d.textbbox((0, 0), t, font=f)
                w, h = bb[2] - bb[0], bb[3] - bb[1]
                d.text(((size - w) / 2 - bb[0], (size - h) / 2 - bb[1]), t, font=f, fill=(255, 255, 255, 255))
                drawn = True; break
            except Exception:
                continue
    return icon

make(512).save("icon-512.png"); make(180).save("apple-touch-icon.png"); print("icons generated")
