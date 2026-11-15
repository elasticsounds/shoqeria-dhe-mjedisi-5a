# PDF page 78 — Provoje veten (one question per section). Task 2 is a letter-scramble as a reader fill-in-the-blank activity
# (Submit button, sounds, popup): Të / barabartë / para / ligjit.
L = 'Provoje veten'
section(title('Provoje veten', practice=True),
  task('1.', ('Si e kupton shprehjen: “Sjellja e mirë qytetare nënkupton respektimin e ligjit dhe marrjen e përgjegjësive”?',
              'Si e kupton këtë shprehje:\n“Sjellja e mirë qytetare nënkupton respektimin e ligjit dhe marrjen e përgjegjësive”?'),
       body=field('lined', 'Si e kupton shprehjen për sjelljen e mirë qytetare?', rows=6)),
  lesson=L, practice=True)
KEY = ['të', 'barabartë', 'para', 'ligjit']
ROWS = [['Ë', 'T'], ['A', 'B', 'R', 'Ë', 'A', 'B', 'T', 'R', 'A'], ['A', 'R', 'A', 'P'], ['T', 'I', 'Gj', 'L', 'I']]
def scramble(n, letters):
    tiles = ''.join(f'<span class="p78-tile">{c}</span>' for c in letters)
    return (f'<div class="p78-row"><p class="p78-tiles" aria-label="Shkronjat e fjalës {n}: {", ".join(letters)}">{tiles}</p>'
            + '<div class="p78-ans">' + keyed(field('line', f'Fjala {n} e formuar nga shkronjat {", ".join(letters)}'), KEY[n - 1]) + '</div></div>')
section(rule(True),
  task('2.', ('Renditi shkronjat për t’i formuar fjalët dhe më pas fjalinë e duhur.',
              'Renditi shkronjat dhe formo fjalët.\nPastaj formo fjalinë e duhur.'),
       ('Shkruaje fjalinë e formuar.', 'Shkruaje fjalinë që formove.'),
       body=''.join(scramble(n, r) for n, r in enumerate(ROWS, 1)) +
            '<p class="p2-flabel p78-sentence">' + t('Fjalia e formuar:') + '</p>' +
            keyed(field('lined', 'Shkruaje fjalinë e formuar.', rows=2), 'Të barabartë para ligjit', 'Të barabartë para ligjit.', 'Të barabartë para ligjit!')),
  practice=True,
  css='''#content.book.p2 .p78-row{display:grid;margin:0 0 10px;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;align-items:center}
#content.book.p2 .p78-tiles{margin:0;font-size:0;line-height:0}
#content.book.p2 .p78-tile{display:inline-block;min-width:48px;height:52px;margin:0 -2px 4px 0;padding:0 6px;border:2px solid var(--book-ink);background:#fff;font:600 22px/48px var(--book-heading);color:var(--book-ink);text-align:center;vertical-align:top}
#content.book.p2 .p78-sentence{margin:16px 0 6px}
@media(max-width:700px){#content.book.p2 .p78-row{grid-template-columns:minmax(0,1fr);gap:6px}#content.book.p2 .p78-tile{min-width:36px;height:44px;padding:0 3px;font-size:20px;line-height:40px}}
''')
section(rule(True),
  '<div class="prx-step"><p class="prx-instruction">' + t('3.') + ' ' +
  t('Gjeni fotografi përmes së cilave tregohet respektimi ose mosrespektimi i ligjit.', 'Gjeni fotografi që tregojnë respektimin ose mosrespektimin e ligjit.') + ' ' +
  t('Me fotot e grumbulluara krijoni një poster dhe vendoseni atë në klasë.', 'Me fotot që mblodhët krijoni një poster.\nVendoseni posterin në klasë.') + ' ' +
  t('Diskutoni rreth tij.', 'Diskutoni për posterin.') + '</p></div>',
  practice=True)
