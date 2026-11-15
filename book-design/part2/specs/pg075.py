# PDF page 75 — Provoje veten (one question per section).
L = 'Provoje veten'
section(title('Provoje veten', practice=True),
  task('1.', ('Si e kupton shprehjen: “Liria e çdo individi shkon deri aty ku nuk cenohet (preket) liria e të tjerëve”?',
              'Si e kupton këtë shprehje:\n“Liria e çdo individi shkon deri aty ku nuk cenohet (preket) liria e të tjerëve”?'),
       body=field('lined', 'Si e kupton shprehjen për lirinë e çdo individi?', rows=3)),
  lesson=L, practice=True)
section(rule(True),
  task('2.', 'Shkruaj disa arsye se përse duhet ta respektojmë njëri-tjetrin.',
       body='<div class="p75-why"><p class="p75-topic">' + t('Ta respektojmë njëri-tjetrin') + '</p><div class="p75-reasons"><p class="p2-flabel">' + t('Pse?') + '</p>' +
            ''.join(field('line', f'Arsyeja {n} pse duhet ta respektojmë njëri-tjetrin') for n in (1, 2, 3, 4, 5)) + '</div></div>'),
  practice=True,
  css='''#content.book.p2 .p75-why{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2.4fr);border:2px solid var(--book-ink);border-radius:12px;overflow:hidden}
#content.book.p2 .p75-topic{margin:0;padding:18px;align-content:center;border-right:2px solid var(--book-ink);background:#fff8ea;font:600 22px/1.4 var(--book-heading)}
#content.book.p2 .p75-reasons{display:grid;gap:10px;padding:14px}
#content.book.p2 .p75-reasons .p2-flabel{margin:0;text-align:center}
@media(max-width:700px){#content.book.p2 .p75-why{grid-template-columns:minmax(0,1fr)}#content.book.p2 .p75-topic{border-right:0;border-bottom:2px solid var(--book-ink);font-size:20px}}
''')
section(rule(True),
  task('3.', ('Bëni një listë të përgjegjësive që ju duhet të merrni në klasë, me qëllim që të keni bashkëpunim të mirë mes vete.',
              'Bëni një listë të përgjegjësive që duhet t’i merrni në klasë.\nKështu do të bashkëpunoni mirë me njëri-tjetrin.'),
       body=field('lined', 'Lista e përgjegjësive që ju duhet të merrni në klasë', rows=6)),
  practice=True)
