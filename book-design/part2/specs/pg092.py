# PDF page 92 — Provoje veten (after "Pavarësia e Kosovës"). One task per section.
L = 'Provoje veten'
section(title('Provoje veten', practice=True),
  task('1.', 'Shkruaj një tekst me temën: “Shpallja e pavarësisë është vullneti i popullit”.',
       body=field('lined', 'Shkruaj një tekst me temën: “Shpallja e pavarësisë është vullneti i popullit”.', rows=6)),
  lesson=L, practice=True)
section(rule(True),
  task('2.', 'Përshkruaj se si e feston Pavarësinë e Kosovës.',
       body=field('lined', 'Përshkruaj se si e feston Pavarësinë e Kosovës.', rows=5)),
  practice=True)
# The PDF prints a large empty box for the leaflet: a plain writing/planning box here.
section(rule(True),
  task('3.', ('Përgatiteni një fletëpalosje: “Kosova - shtet i pavarur”.', 'Përgatitni një fletëpalosje.\nTema është: “Kosova - shtet i pavarur”.'),
       body=field('area', 'Hapësirë për fletëpalosjen “Kosova - shtet i pavarur”', rows=8)),
  practice=True, css='#content.book.p2.prx textarea.prx-field.p92-leaflet,#content.book.p2.prx .prx-fields textarea:not(.prx-lined){min-height:300px;border-color:#794282}\n')
