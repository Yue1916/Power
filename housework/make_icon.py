# -*- coding: utf-8 -*-
"""生成家务打卡 App 图标（渐变圆角背景 + 扫帚/对勾）"""
from PIL import Image, ImageDraw, ImageFont

def rounded(size, radius, color):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, size, size], radius=radius, fill=color)
    return img

def gradient(size, c1, c2):
    base = Image.new("RGB", (size, size), c1)
    top = Image.new("RGB", (size, size), c2)
    mask = Image.new("L", (size, size))
    md = mask.load()
    for y in range(size):
        for x in range(size):
            md[x, y] = int(255 * ((x + y) / (2 * size)))
    base.paste(top, (0, 0), mask)
    return base.convert("RGBA")

def make(size):
    r = int(size * 0.22)
    grad = gradient(size, (0, 184, 148), (47, 107, 255))   # teal -> blue
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, size, size], radius=r, fill=255)
    icon = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    icon.paste(grad, (0, 0), mask)

    d = ImageDraw.Draw(icon)
    # 尝试用 emoji/字体画一个对勾符号；失败则手绘对勾
    txt = "\u2713"  # ✓
    drawn = False
    for fp in ["seguisym.ttf", "seguiemj.ttf", "arialbd.ttf", "msyhbd.ttc"]:
        try:
            f = ImageFont.truetype(fp, int(size * 0.6))
            bb = d.textbbox((0, 0), txt, font=f)
            w, h = bb[2] - bb[0], bb[3] - bb[1]
            d.text(((size - w) / 2 - bb[0], (size - h) / 2 - bb[1]), txt,
                   font=f, fill=(255, 255, 255, 255))
            drawn = True
            break
        except Exception:
            continue
    if not drawn:
        lw = int(size * 0.08)
        d.line([(size*0.28, size*0.52), (size*0.44, size*0.68), (size*0.74, size*0.34)],
               fill=(255, 255, 255, 255), width=lw, joint="curve")
    return icon

make(512).save("icon-512.png")
make(180).save("apple-touch-icon.png")
print("icons generated")
