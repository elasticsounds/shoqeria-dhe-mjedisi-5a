#!/usr/bin/env python3
"""Split one reader page into several sections (one per group of top-level blocks) and register them.

Usage (from the bundle root):
  python3 book-design/split-section.py pg023_sec001.html 3 5
    -> keeps blocks [0..2] in pg023_sec001.html, blocks [3..4] in pg023_sec002.html, the rest in pg023_sec003.html.
  Block indexes are the top-level children of the page's <section> (print them with --list).
  A leading .b-page-rule / .b-page-title is repeated as a .b-page-rule (same colour) on every new section.

Updates: new HTML files (same head/styles/scripts, new title-id/data-section-id), content/pages.json (inserted after the
original, same page_number), every page's <meta name="page-section-id"> (1-based reading position), imsmanifest.xml and
the offline cache keys. Afterwards run: node book-design/rebuild-cache.cjs
"""
import json, re, subprocess, sys
from html.parser import HTMLParser

def top_level_blocks(section_html):
    """Return [(start, end)] spans of the direct children elements of the section body."""
    class P(HTMLParser):
        def __init__(s):
            super().__init__(convert_charrefs=False); s.depth = 0; s.spans = []; s.start = None
        VOID = {'img', 'input', 'br', 'hr', 'meta', 'link', 'source', 'col', 'wbr'}
        def handle_starttag(s, tag, attrs):
            if s.depth == 0: s.start = s.getpos()
            if tag not in s.VOID: s.depth += 1
            elif s.depth == 0: s.spans.append((s.start, s.getpos(), True))
        def handle_startendtag(s, tag, attrs):
            if s.depth == 0: s.spans.append((s.getpos(), s.getpos(), True))
        def handle_endtag(s, tag):
            s.depth -= 1
            if s.depth == 0: s.spans.append((s.start, s.getpos(), False))
    p = P(); p.feed(section_html)
    lines = section_html.split('\n'); offs = [0]
    for l in lines: offs.append(offs[-1] + len(l) + 1)
    pos = lambda lc: offs[lc[0] - 1] + lc[1]
    out = []
    for a, b, void in p.spans:
        start = pos(a)
        end = section_html.index('>', pos(b)) + 1
        out.append((start, end))
    return out

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    src = args[0]; cuts = [int(x) for x in args[1:]]
    html = open(src).read()
    m = re.search(r'(<section\b[^>]*>)(.*)(</section>)', html, re.S)
    sec_open, body, sec_close = m.group(1), m.group(2), m.group(3)
    spans = top_level_blocks(body)
    blocks = [body[a:b] for a, b in spans]
    if '--list' in sys.argv:
        for i, b in enumerate(blocks): print(i, re.sub(r'\s+', ' ', b)[:110])
        return
    base = re.match(r'(pg\d{3})_sec(\d{3})\.html$', src)
    stem, first_no = base.group(1), int(base.group(2))
    rule = ''
    if blocks and re.match(r'<(?:div|header)[^>]*class="[^"]*\bb-page-(?:rule|title)\b', blocks[0]):
        practice = 'is-practice' in blocks[0]
        rule = f'<div class="b-page-rule{" is-practice" if practice else ""}" aria-hidden="true"></div>'
    groups = []; prev = 0
    for c in cuts + [len(blocks)]: groups.append(blocks[prev:c]); prev = c
    spine = json.load(open('content/pages.json'))
    hrefs = [p['href'] for p in spine]; idx = hrefs.index(src)
    names = [src] + [f'{stem}_sec{first_no + i:03d}.html' for i in range(1, len(groups))]
    for n in names[1:]:
        if n in hrefs: sys.exit(f'{n} already exists in the reading order; renumber first.')
    old_id = src[:-5]
    for gi, (name, grp) in enumerate(zip(names, groups)):
        new_id = name[:-5]
        content = '\n'.join(grp)
        if gi > 0 and rule and not re.match(r'<(?:div|header)[^>]*class="[^"]*\bb-page-(?:rule|title)\b', grp[0]):
            content = rule + '\n' + content
        new_sec_open = sec_open.replace(f'data-section-id="{old_id}"', f'data-section-id="{new_id}"')
        out = html[:m.start()] + new_sec_open + '\n' + content + '\n' + sec_close + html[m.end():]
        out = out.replace(f'<meta name="title-id" content="{old_id}">', f'<meta name="title-id" content="{new_id}">')
        open(name, 'w').write(out)
        fields = re.findall(r'<(?:input|textarea|select)\b[^>]*\bid="([^"]+)"', content)
        print(f'{name}: {len(grp)} blocks, fields {fields}')
    # reading order
    raw = open('content/pages.json').read(); ind = 2 if '\n  {' in raw else None
    pn = spine[idx].get('page_number')
    for k, n in enumerate(names[1:], 1):
        e = {'section_id': n[:-5], 'href': n}
        if pn is not None: e['page_number'] = pn
        spine.insert(idx + k, e)
    open('content/pages.json', 'w').write(json.dumps(spine, ensure_ascii=False, indent=ind) + ('\n' if raw.endswith('\n') else ''))
    changed = 0
    for i, p in enumerate(spine, 1):
        s = open(p['href']).read()
        t = re.sub(r'(<meta name="page-section-id" content=")\d+(")', rf'\g<1>{i}\2', s, count=1)
        if t != s: open(p['href'], 'w').write(t); changed += 1
    print(f'reading order: {len(spine)} pages, position markers updated: {changed}')
    # SCORM manifest
    man = open('imsmanifest.xml').read(); a = f'<file href="{src}"/>'
    if a in man:
        man = man.replace(a, a + ''.join(f'<file href="{n}"/>' for n in names[1:])); open('imsmanifest.xml', 'w').write(man)
    # offline cache keys (contents are filled by rebuild-cache.cjs)
    js = ("const fs=require('fs');const src=fs.readFileSync('book-design/rebuild-cache.cjs','utf8');"
          "const parse=eval('('+src.match(/function parse\\(s\\)\\{[\\s\\S]*?\\n?return \\{prefix[^}]*\\};\\}/)[0].replace('function parse','function')+')');"
          "const f='assets/offline-preloader.js';const c=parse(fs.readFileSync(f,'utf8'));"
          f"for(const k of {json.dumps(['./' + n for n in names[1:]])})if(!(k in c.value))c.value[k]='';"
          "fs.writeFileSync(f,c.prefix+JSON.stringify(c.value)+c.suffix);")
    subprocess.run(['node', '-e', js], check=True)
    print('manifest + cache keys updated; now run: node book-design/rebuild-cache.cjs')

if __name__ == '__main__':
    main()
