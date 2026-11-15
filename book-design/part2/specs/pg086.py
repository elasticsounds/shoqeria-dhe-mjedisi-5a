# PDF page 86 — Provoje veten (after “Beteja e Kosovës”); one question per section.
L = 'Provoje veten'
section(title('Provoje veten', practice=True),
  task('1.', ('Hulumto dhe shkruaj për rolin e Teodor Muzakës në Betejën e Kosovës.',
              'Hulumto për Teodor Muzakën.\nShkruaj çfarë bëri ai në Betejën e Kosovës.'),
       body=field('lined', 'Hulumto dhe shkruaj për rolin e Teodor Muzakës në Betejën e Kosovës.', rows=6)),
  lesson=L, practice=True)
def row(n, hint, labels, short=False):
    return ('<div class="p86-row' + (' is-short' if short else '') + '"><div class="p86-fields" style="--n:%d">' % n + ''.join(field('line', l) for l in labels) +
            '</div><p class="p86-hint">' + t(hint) + '</p></div>')
section(rule(True),
  task('2.', 'Plotëso sipas kërkesave.',
       body='<h2 class="p2-subhead">' + t('Beteja e Kosovës') + '</h2>' +
            row(2, '(dy mbiemra)', ['Mbiemri i parë për Betejën e Kosovës', 'Mbiemri i dytë për Betejën e Kosovës']) +
            row(3, '(tri folje)', ['Folja e parë për Betejën e Kosovës', 'Folja e dytë për Betejën e Kosovës', 'Folja e tretë për Betejën e Kosovës']) +
            row(1, '(një fjali)', ['Një fjali për Betejën e Kosovës']) +
            row(1, '(një sinonim)', ['Një sinonim për Betejën e Kosovës'], short=True)),
  practice=True,
  css='''#content.book.p2 .p86-row{width:100%;max-width:760px;margin:0 auto 16px}
#content.book.p2 .p86-row.is-short{max-width:380px}
#content.book.p2 .p86-fields{display:grid;grid-template-columns:repeat(var(--n),minmax(0,1fr));gap:12px}
#content.book.p2 .p86-hint{margin:6px 0 0;font:400 20px/1.4 var(--book-heading);color:var(--book-ink);text-align:center}
@media(max-width:700px){#content.book.p2 .p86-fields{grid-template-columns:minmax(0,1fr)}}
''')
