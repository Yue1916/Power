from PIL import Image, ImageDraw

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def make(size, path):
    SS = 4  # 超采样抗锯齿
    S = size * SS
    img = Image.new("RGB", (S, S), (0, 0, 0))
    d = ImageDraw.Draw(img)

    # 对角渐变背景：蓝 -> 青
    c1 = (47, 107, 255)   # #2f6bff
    c2 = (0, 211, 167)    # #00d3a7
    maxd = 2 * (S - 1)
    for y in range(S):
        # 用行渐变近似（快且够用）
        t = y / (S - 1)
        d.line([(0, y), (S, y)], fill=lerp(c1, c2, t))

    cx, cy = S / 2, S / 2
    unit = S / 180.0

    # 金币圆盘
    gold = (255, 207, 92)      # #ffcf5c
    gold_edge = (214, 164, 54) # 深金描边
    R = 66 * unit
    d.ellipse([cx - R, cy - R, cx + R, cy + R], fill=gold_edge)
    Ri = 60 * unit
    d.ellipse([cx - Ri, cy - Ri, cx + Ri, cy + Ri], fill=gold)
    # 内圈装饰
    Rr = 50 * unit
    d.ellipse([cx - Rr, cy - Rr, cx + Rr, cy + Rr], outline=gold_edge, width=int(2.5 * unit))

    # ¥ 符号（深色）
    ink = (23, 96, 78)  # 深青绿
    w = int(8 * unit)
    def cap(x, y, r):
        d.ellipse([x - r, y - r, x + r, y + r], fill=ink)

    topL = (cx - 24 * unit, cy - 34 * unit)
    topR = (cx + 24 * unit, cy - 34 * unit)
    vtx  = (cx, cy - 2 * unit)
    # 两条斜臂
    d.line([topL, vtx], fill=ink, width=w)
    d.line([topR, vtx], fill=ink, width=w)
    cap(*topL, w / 2); cap(*topR, w / 2); cap(*vtx, w / 2)
    # 竖干
    d.rounded_rectangle([cx - w / 2, cy - 6 * unit, cx + w / 2, cy + 40 * unit], radius=w / 2, fill=ink)
    # 两条横杠
    barw = 26 * unit
    for yy in (cy + 8 * unit, cy + 22 * unit):
        d.rounded_rectangle([cx - barw, yy - w / 2, cx + barw, yy + w / 2], radius=w / 2, fill=ink)

    img = img.resize((size, size), Image.LANCZOS)
    img.save(path)
    print("saved", path)

make(180, "apple-touch-icon.png")
make(512, "icon-512.png")
