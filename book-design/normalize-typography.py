#!/usr/bin/env python3
"""Normalize typography across the page-specific <style> blocks.

Rules (see brand-guide.html for the type system):
  * Two families only: Poppins (headings, rubric headings, labels, UI) and
    Amiri (reading text). Comic Sans / `cursive` / page-local Poppins aliases /
    Merriweather are folded into these. Rubric headings use the
    `--book-rubric` token so the face can be swapped in one place.
  * No text below MIN_PX: viewport/container-scaled sizes are wrapped in
    max(MIN_PX, ...); fixed sizes below the floor are raised.
  * Absolute line-heights paired with a scaled size become unitless ratios so
    lines never overlap when the floor kicks in.
  * PDF-canvas pages switch to their flow layout below CANVAS_BREAKPOINT
    (previously 600-700px), i.e. wherever the canvas would need sub-16px text.
  * No justified text; near-black ink colours use the --book-ink token.

Idempotent: running it twice makes no further changes.
Usage: python3 normalize-typography.py [--dry-run]   (run from anywhere)
Afterwards run `node rebuild-cache.cjs` to resync the offline cache.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MIN_PX = 16
CANVAS_BREAKPOINT = 900
POPPINS = "BookPoppins,Arial,sans-serif"
RUBRIC = "var(--book-rubric,BookPoppins,Arial,sans-serif)"
INK = "var(--book-ink,#231f20)"
NEAR_BLACK = {"#30313a", "#282831", "#292b33", "#252631", "#282333", "#282a32",
              "#2b2b2b", "#1f1f1f", "#1f2937", "#30303a", "#2a2b33", "#222", "#333", "#222222", "#333333"}

stats = {}
def bump(k, n=1): stats[k] = stats.get(k, 0) + n

# ---------- value helpers ----------
def split_top(s, seps=" /"):
    """Split a CSS value into tokens at top-level whitespace and '/', keeping '/' as a token."""
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch == "(": depth += 1
        elif ch == ")": depth -= 1
        if depth == 0 and ch in seps:
            if cur: out.append(cur); cur = ""
            if ch == "/": out.append("/")
            continue
        cur += ch
    if cur: out.append(cur)
    return out

SIZE_RE = re.compile(r"^(?:[\d.]+(?:px|cqw|vw|em|rem|pt|%)|calc\(.*\)|clamp\(.*\)|max\(.*\)|min\(.*\))$")

def floor_size(v):
    """Return a size expression that never renders below MIN_PX."""
    v = v.strip()
    m = re.fullmatch(r"([\d.]+)px", v)
    if m:
        if float(m.group(1)) < MIN_PX: bump("px raised"); return f"{MIN_PX}px"
        return v
    if v.startswith(f"max({MIN_PX}px"): return v
    m = re.fullmatch(r"clamp\(\s*([\d.]+)px\s*,(.*)\)", v)
    if m:
        if float(m.group(1)) < MIN_PX: bump("clamp raised"); return f"clamp({MIN_PX}px,{m.group(2)})"
        return v
    if re.search(r"cqw|vw|var\(--(u|pt)\)", v):
        bump("scaled size floored"); return f"max({MIN_PX}px,{v})"
    return v  # em / % / inherit: relative to an already-floored parent

def scaled_amount(v):
    """Numeric coefficient for ratio maths: 1.877cqw -> ('cqw',1.877); calc(12 * var(--u)) -> ('u',12)."""
    m = re.fullmatch(r"([\d.]+)(cqw|vw)", v.strip())
    if m: return (m.group(2), float(m.group(1)))
    m = re.fullmatch(r"calc\(\s*(?:([\d.]+)\s*\*\s*var\(--(u|pt)\)|var\(--(u|pt)\)\s*\*\s*([\d.]+))\s*\)", v.strip())
    if m:
        return (m.group(2) or m.group(3), float(m.group(1) or m.group(4)))
    return None

def lh_ratio(size, lh):
    a, b = scaled_amount(size), scaled_amount(lh)
    if a and b and a[0] == b[0] and a[1]:
        bump("line-height made unitless"); return f"{b[1] / a[1]:.3g}"
    return lh

def is_comic(fam):
    return "comic sans" in fam.lower() or re.fullmatch(r"\s*cursive\s*", fam) is not None

def norm_family(fam):
    f = fam.strip()
    low = f.lower()
    if is_comic(f) or re.search(r"(^|,)\s*cursive\s*$", low): bump("rubric family"); return RUBRIC, True
    if re.match(r"(pagepoppins|pg48poppins|page49poppins|page28poppins)\b", low):
        bump("alias family"); return re.sub(r"^\w+", "BookPoppins", f), False
    if low.startswith("merriweather"): bump("merriweather"); return POPPINS, False
    return f, False

# ---------- declaration block ----------
def process_block(body, canvas):
    decls = []
    depth, cur = 0, ""
    for ch in body:  # split on top-level ';'
        if ch == "(": depth += 1
        elif ch == ")": depth -= 1
        if ch == ";" and depth == 0: decls.append(cur); cur = ""
        else: cur += ch
    decls.append(cur)
    parsed = []
    for d in decls:
        if ":" in d and not d.strip().startswith("--"):
            k, v = d.split(":", 1); parsed.append([k, v])
        else: parsed.append([None, d])
    props = {k.strip().lower(): i for i, (k, v) in enumerate(parsed) if k}
    rubric = False
    size_expr = None
    for item in parsed:
        k, v = item
        if not k: continue
        key = k.strip().lower()
        imp = ""
        vv = v
        m = re.search(r"\s*!important\s*$", vv)
        if m: imp = m.group(0); vv = vv[:m.start()]
        lead = re.match(r"\s*", vv).group(0); vv = vv.strip()
        if key == "font-family":
            nv, r = norm_family(vv); rubric |= r; vv = nv
        elif key == "font-size":
            vv = floor_size(vv); size_expr = item
        elif key == "font" and vv not in ("inherit", "initial", "unset"):
            toks = split_top(vv)
            # locate size token: first token matching a size, preceded only by style/weight words
            si = next((i for i, t in enumerate(toks) if SIZE_RE.match(t)), None)
            if si is not None:
                orig_size = toks[si]
                rest = toks[si + 1:]
                lh = None
                if rest and rest[0] == "/": lh = rest[1]; fam = " ".join(rest[2:])
                else: fam = " ".join(rest)
                pre = toks[:si]
                fam = ",".join(p.strip() for p in fam.split(","))
                nfam, r = norm_family(fam) if fam else (fam, False)
                if r:
                    rubric = True
                    pre = ["600" if t in ("400", "normal") else t for t in pre]
                    if not any(re.fullmatch(r"\d{3}|bold", t) for t in pre): pre.append("600")
                new_size = floor_size(orig_size)
                if lh is not None and new_size != orig_size: lh = lh_ratio(orig_size, lh)
                vv = " ".join(pre + [new_size + (("/" + lh) if lh else "")] + ([nfam] if nfam else []))
        elif key == "text-align" and vv == "justify":
            vv = "left"; bump("justify removed")
        elif key == "color" and vv.lower() in NEAR_BLACK:
            vv = INK; bump("ink unified")
        elif key == "transform" and re.fullmatch(r"scaleX\([.\d]+\)", vv):
            vv = "none"; bump("condensed text unscaled")
        item[1] = lead + vv + imp
    # separate line-height paired with a floored scaled font-size
    if size_expr is not None and "line-height" in props:
        lh_item = parsed[props["line-height"]]
        old_size = None
        m = re.match(rf"\s*max\({MIN_PX}px,(.*)\)\s*$", size_expr[1])
        if m: old_size = m.group(1)
        if old_size:
            nv = lh_ratio(old_size, lh_item[1].strip())
            if nv != lh_item[1].strip(): lh_item[1] = nv
    if rubric:
        for item in parsed:
            if item[0] and item[0].strip().lower() == "font-weight" and item[1].strip() in ("400", "normal"):
                item[1] = "600"
    return ";".join((f"{k}:{v}" if k else v) for k, v in parsed)

def process_css(css, canvas):
    # remove page-local Poppins alias faces (BookPoppins is defined in components.css)
    css, n = re.subn(r"@font-face\s*\{[^}]*font-family:\s*(?:PagePoppins|Pg48Poppins|Page49Poppins|Page28Poppins)[^}]*\}", "", css)
    bump("alias @font-face removed", n)
    if canvas:
        css, n = re.subn(r"(@media\s*\(\s*max-width\s*:\s*)(600|640|700)(px\s*\))", rf"\g<1>{CANVAS_BREAKPOINT}\3", css)
        bump("canvas breakpoint raised", n)
    out, i = [], 0
    # walk blocks: anything between '{' and its '}' that has no nested '{' is a declaration block
    for m in re.finditer(r"\{([^{}]*)\}", css):
        head = css[i:m.start()]
        out.append(head)
        prelude = head.rsplit("}", 1)[-1].rsplit("{", 1)[-1].strip()
        body = m.group(1)
        if prelude.startswith("@font-face"): out.append("{" + body + "}")
        else: out.append("{" + process_block(body, canvas) + "}")
        i = m.end()
    out.append(css[i:])
    return "".join(out)

FULL_FACES = ("@font-face{font-family:BookPoppins;src:url('./book-design/fonts/Poppins-400.ttf');font-weight:400}"
              "@font-face{font-family:BookPoppins;src:url('./book-design/fonts/Poppins-600.ttf');font-weight:600}"
              "@font-face{font-family:BookPoppins;src:url('./book-design/fonts/Poppins-700.ttf');font-weight:700}"
              "@font-face{font-family:BookAmiri;src:url('./book-design/fonts/Amiri-400.ttf');font-weight:400}"
              "@font-face{font-family:BookAmiri;src:url('./book-design/fonts/Amiri-700.ttf');font-weight:700}")

def process_html(s):
    styles = "".join(re.findall(r"<style[^>]*>(.*?)</style>", s, re.S))
    canvas = bool(re.search(r"cqw|var\(--(u|pt)\)", styles)) and "position:absolute" in styles.replace(" ", "")
    s = re.sub(r"(<style[^>]*>)(.*?)(</style>)", lambda m: m.group(1) + process_css(m.group(2), canvas) + m.group(3), s, flags=re.S)
    if canvas:  # art crops swapped in by <picture> must follow the same breakpoint
        s, n = re.subn(r'(<source media="\(max-width:\s*)(600|640|700)(px\)")', rf"\g<1>{CANVAS_BREAKPOINT}\3", s)
        bump("picture breakpoint raised", n)
    s = re.sub(r'(\sstyle=")([^"]*)(")', lambda m: m.group(1) + process_block(m.group(2), canvas) + m.group(3), s)
    # standalone page with a partial font set: give it every weight it now uses
    s = s.replace("@font-face{font-family:BookPoppins;src:url('./book-design/fonts/Poppins-400.ttf')}@font-face{font-family:BookAmiri;src:url('./book-design/fonts/Amiri-400.ttf')}", FULL_FACES)
    return s

# ---------- rubric headings: one family/weight everywhere ----------
RUBRICS = {"Pyetje për ty", "Diskuto", "Thello dijet", "Shpreh mendimin tënd", "Fjalorthi"}
SKIP_RUBRIC = {"pg003_sec001.html", "pg005_sec001.html"}  # contents list and icon legend use these words as entries
RUBRIC_EL = re.compile(r"<(h[1-4]|p|span|div)(\s[^>]*)?>((?:(?!<(?:h[1-4]|p|div)\b).)*?)</\1>", re.S)

def tag_rubrics(s):
    """Add class b-rubric to the outermost element whose whole text is a rubric label."""
    def add(m):
        tag, attrs, inner = m.group(1), m.group(2) or "", m.group(3)
        if re.sub(r"<[^>]+>", "", inner).strip() not in RUBRICS or "b-rubric" in attrs: return m.group(0)
        bump("rubric heading tagged")
        attrs = re.sub(r'\sclass="', ' class="b-rubric ', attrs, count=1) if ' class="' in attrs else attrs + ' class="b-rubric"'
        return f"<{tag}{attrs}>{inner}</{tag}>"
    return RUBRIC_EL.sub(add, s)

def main():
    dry = "--dry-run" in sys.argv
    spine = json.loads((ROOT / "content/pages.json").read_text())
    targets = [ROOT / p["href"] for p in spine]
    changed = []
    for f in targets:
        s = f.read_text(); n = process_html(s)
        if f.name not in SKIP_RUBRIC: n = tag_rubrics(n)
        if n != s:
            changed.append(f.name)
            if not dry: f.write_text(n)
    for css in [ROOT / "book-design/pg028.css"]:
        s = css.read_text(); n = process_css(s, True)
        if n != s:
            changed.append(css.name)
            if not dry: css.write_text(n)
    print(("Would change " if dry else "Changed ") + f"{len(changed)} files")
    for k, v in sorted(stats.items()): print(f"  {k}: {v}")

if __name__ == "__main__":
    main()

