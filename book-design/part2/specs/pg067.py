# PDF page 67 — lesson start: "Institucionet që na mbrojnë".
L = 'Institucionet që na mbrojnë'
PICS = [('pg067_im001.png', 'Logo e një institucioni me një figurë njeriu, hartën e Kosovës dhe mbishkrimin “Republika e Kosovës, Avokati i Popullit”.'),
        ('pg067_im002.png', 'Një çekiç gjykatësi prej druri në një sallë gjyqi, me një stemë në mur.'),
        ('pg067_im003.png', 'Stemë në formë ylli me ngjyra blu dhe të verdhë, me hartën e Kosovës në mes dhe fjalët “Kosovo Police”.'),
        ('pg067_im004.png', 'Stemë blu në formë mburoje me një peshore në mes dhe gjashtë yje sipër.')]
section(title(L), keywords('institucion, avokat, gjykatë, prokurori, polici.'),
  panel('thought', 'Shpreh mendimin tënd', items('Trego për institucionet që na mbrojnë.', 'Shkruaj emrat e institucioneve të mëposhtme.')),
  '<div class="p67-grid">' + ''.join(
      f'<div class="p67-item"><figure class="b-lesson-figure">{img(f, a)}</figure>' + field('line', f'Emri i institucionit në figurën {n}') + '</div>'
      for n, (f, a) in enumerate(PICS, 1)) + '</div>',
  lesson=L, stype='text_and_images',
  css='#content.book.p2 .p67-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:28px}\n'
      '#content.book.p2 .p67-item{display:grid;gap:12px;align-content:end}\n'
      '#content.book.p2 .p67-item .b-lesson-figure{margin:0}\n'
      '#content.book.p2 .p67-item img{width:auto;max-width:100%;height:200px;margin:0 auto;object-fit:contain;border-radius:8px}\n'
      '#content.book.p2 .p67-item input.prx-field{display:block;width:100%;min-height:52px;padding:10px 14px;border:2px solid #6d6472;border-radius:10px;background:#fff;font:400 20px/1.5 var(--book-heading);color:var(--book-ink)}\n'
      '@media(max-width:700px){#content.book.p2 .p67-grid{grid-template-columns:minmax(0,1fr)}#content.book.p2 .p67-item img{height:160px}}\n')
