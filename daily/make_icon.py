from PIL import Image, ImageDraw

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def make(size, path):
    SS = 4
    S = size * SS
    img = Image.new("RGB", (S, S), (0, 0, 0))
    d = ImageDraw.Draw(img)

    # 渐变背景：紫 -> 粉
    c1 = (124, 92, 255)   # #7c5cff
    c2 = (248, 113, 160)  # #f871a0
    for y in range(S):
        d.line([(0, y), (S, y)], fill=lerp(c1, c2, y / (S - 1)))

    unit = S / 180.0
    cx, cy = S / 2, S / 2 + 6 * unit

    body = (255, 250, 252)     # 近白
    body_sh = (255, 209, 224)  # 浅粉阴影
    ink = (124, 92, 255)       # 紫（细节）
    gold = (255, 207, 92)

    def ell(x, y, rx, ry, fill):
        d.ellipse([x - rx, y - ry, x + rx, y + ry], fill=fill)

    # 耳朵
    ell(cx - 30 * unit, cy - 40 * unit, 12 * unit, 14 * unit, body_sh)
    # 腿
    for lx in (-34, -8, 16, 40):
        d.rounded_rectangle([cx + lx * unit, cy + 30 * unit, cx + (lx + 16) * unit, cy + 52 * unit],
                            radius=6 * unit, fill=body_sh)
    # 身体
    ell(cx, cy, 60 * unit, 46 * unit, body)
    # 鼻子
    ell(cx + 44 * unit, cy + 4 * unit, 18 * unit, 15 * unit, body_sh)
    d.ellipse([cx + 40 * unit, cy - 4 * unit, cx + 48 * unit, cy + 4 * unit], fill=ink)
    d.ellipse([cx + 40 * unit, cy + 6 * unit, cx + 48 * unit, cy + 14 * unit], fill=ink)
    # 眼睛
    ell(cx + 20 * unit, cy - 12 * unit, 4.5 * unit, 4.5 * unit, ink)
    # 投币口
    d.rounded_rectangle([cx - 16 * unit, cy - 40 * unit, cx + 14 * unit, cy - 33 * unit],
                        radius=3.5 * unit, fill=ink)
    # 金币（落入投币口）
    ell(cx - 1 * unit, cy - 58 * unit, 13 * unit, 13 * unit, gold)
    d.ellipse([cx - 6 * unit, cy - 63 * unit, cx + 4 * unit, cy - 53 * unit],
              outline=(214, 164, 54), width=int(2 * unit))

    img = img.resize((size, size), Image.LANCZOS)
    img.save(path)
    print("saved", path)

make(180, "apple-touch-icon.png")
make(512, "icon-512.png")
