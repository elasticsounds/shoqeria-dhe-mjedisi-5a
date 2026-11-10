#!/usr/bin/env python3
"""Build a SCORM 1.2 package (zip) of the reader with only the files learners need.

  python3 book-design/build-scorm.py            -> dist/Shoqeria-dhe-mjedisi-5A-SCORM.zip
  python3 book-design/build-scorm.py --list     -> print what would be packaged

Included: every page in content/pages.json + index.html, cover.png, assets/, content/ (texts, audio,
navigation), images/, studio/assets/ (images used by pages) and the runtime part of book-design/
(components.css, responses.js, page scripts/styles, fonts/, images/).
Left out: editor history (studio/history*, studio/*.json), validation evidence, brand-guide
examples, build tools, git files. imsmanifest.xml is rewritten so its <file> list matches the
package exactly (also saved back to the repository copy).
"""
import json, os, re, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'dist' / 'Shoqeria-dhe-mjedisi-5A-SCORM.zip'

RUNTIME_DIRS = ['assets', 'content', 'images', 'studio/assets', 'book-design/fonts', 'book-design/images']
RUNTIME_FILES = ['index.html', 'cover.png', 'book-design/components.css', 'book-design/responses.js',
                 'book-design/pg028.css', 'book-design/pg028.js']
SKIP_NAMES = {'.DS_Store', 'Thumbs.db'}

def collect():
    spine = json.loads((ROOT / 'content/pages.json').read_text())
    files = {p['href'] for p in spine}
    files.update(f for f in RUNTIME_FILES if (ROOT / f).exists())
    for d in RUNTIME_DIRS:
        for p in (ROOT / d).rglob('*'):
            if p.is_file() and p.name not in SKIP_NAMES and not p.name.startswith('.'):
                files.add(p.relative_to(ROOT).as_posix())
    missing = [f for f in files if not (ROOT / f).exists()]
    if missing: sys.exit(f'Missing files: {missing[:10]}')
    return sorted(files)

def write_manifest(files):
    m = (ROOT / 'imsmanifest.xml').read_text()
    start = m.index('<resource ')
    head_end = m.index('>', start) + 1
    end = m.index('</resource>', head_end)
    body = '\n' + ''.join(f'      <file href="{f}"/>\n' for f in files) + '    '
    m = m[:head_end] + body + m[end:]
    launch = re.search(r'<resource [^>]*href="([^"]+)"', m).group(1)
    if launch not in files: sys.exit(f'Launch file {launch} is not in the package')
    (ROOT / 'imsmanifest.xml').write_text(m)
    return m

def main():
    files = collect()
    if '--list' in sys.argv:
        print('\n'.join(files)); print(len(files), 'files'); return
    manifest = write_manifest(files)
    OUT.parent.mkdir(exist_ok=True)
    tmp = OUT.with_suffix('.zip.part')
    stored = {'.mp3', '.png', '.jpg', '.jpeg', '.webp', '.woff2', '.woff', '.ttf', '.gif'}
    with zipfile.ZipFile(tmp, 'w') as z:
        z.writestr('imsmanifest.xml', manifest, compress_type=zipfile.ZIP_DEFLATED)
        for f in files:
            kind = zipfile.ZIP_STORED if Path(f).suffix.lower() in stored else zipfile.ZIP_DEFLATED
            z.write(ROOT / f, f, compress_type=kind)
    os.replace(tmp, OUT)
    size = sum((ROOT / f).stat().st_size for f in files)
    print(f'{OUT.relative_to(ROOT)}: {len(files)} files + imsmanifest.xml, '
          f'{size / 1e6:.1f} MB content, zip {OUT.stat().st_size / 1e6:.1f} MB')

if __name__ == '__main__':
    main()
