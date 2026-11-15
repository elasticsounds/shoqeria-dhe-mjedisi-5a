#!/usr/bin/env python3.13
"""Cut an illustration or photo out of the source PDF into images/.

  crop.py <pdf page> <x0> <y0> <x1> <y1> <out name> [--erase x0,y0,x1,y1 ...]

Coordinates are pixels in the 150-dpi page renders (1332 x 1805). Output is rendered at 220 dpi.
--erase removes printed text/page numbers inside a box (same coordinates): dark pixels are replaced by the
nearest background colour on the same row, so text printed over a flat-colour shape disappears cleanly.
Needs Pillow (python3.13 on this machine) and pdftoppm.
"""
import subprocess, sys, tempfile
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parents[2]
PDF = next(ROOT.glob('*.pdf'))
a = sys.argv[1:]; page = int(a[0]); x0, y0, x1, y1 = map(int, a[1:5]); out = a[5]
erase = [tuple(map(int, e.split(','))) for i, e in enumerate(a[6:]) if a[6:][i - 1] == '--erase'] if '--erase' in a else []
S = 220 / 150
with tempfile.TemporaryDirectory() as d:
    subprocess.run(['pdftoppm', '-f', str(page), '-l', str(page), '-r', '220', '-x', str(round(x0 * S)), '-y', str(round(y0 * S)),
                    '-W', str(round((x1 - x0) * S)), '-H', str(round((y1 - y0) * S)), '-png', '-singlefile', str(PDF), f'{d}/c'], check=True)
    im = Image.open(f'{d}/c.png').convert('RGB')
px = im.load()
for ex0, ey0, ex1, ey1 in erase:
    X0, Y0, X1, Y1 = [round(v * S) for v in (ex0 - x0, ey0 - y0, ex1 - x0, ey1 - y0)]
    X0, Y0, X1, Y1 = max(X0, 0), max(Y0, 0), min(X1, im.width), min(Y1, im.height)
    for y in range(Y0, Y1):
        bg = px[max(X0 - 3, 0), y]
        for x in range(X0, X1):
            r, g, b = px[x, y]
            if min(r, g, b) < 200 and max(r, g, b) - min(r, g, b) < 60 or sum((r, g, b)) < 420: px[x, y] = bg
            elif abs(r - bg[0]) + abs(g - bg[1]) + abs(b - bg[2]) > 40 and sum((r, g, b)) > 700: bg = (r, g, b)   # crossed onto white
            elif abs(r - bg[0]) + abs(g - bg[1]) + abs(b - bg[2]) < 40: bg = (r, g, b)
            else: px[x, y] = bg
# --flatten x0,y0,x1,y1: for text printed across a flat-colour shape and the white page: every pixel in the box that is
# not the shape colour becomes the shape colour up to the shape's edge on that row, and white beyond it.
flat = [tuple(map(int, e.split(','))) for i, e in enumerate(a[6:]) if a[6:][i - 1] == '--flatten'] if '--flatten' in a else []
from collections import Counter
for fx0, fy0, fx1, fy1 in flat:
    X0, Y0, X1, Y1 = [round(v * S) for v in (fx0 - x0, fy0 - y0, fx1 - x0, fy1 - y0)]
    X0, Y0, X1, Y1 = max(X0, 0), max(Y0, 0), min(X1, im.width), min(Y1, im.height)
    shape = Counter(px[x, y] for y in range(Y0, Y1, 3) for x in range(X0, X1, 3) if sum(px[x, y]) < 740).most_common(1)[0][0]
    near = lambda c: sum(abs(c[i] - shape[i]) for i in range(3)) < 24
    for y in range(Y0, Y1):
        edge = max([x for x in range(im.width) if near(px[x, y])] or [-1])
        for x in range(X0, X1):
            if not near(px[x, y]): px[x, y] = shape if x <= edge else (255, 255, 255)
im.save(ROOT / 'images' / out, optimize=True)
print(out, im.size)
