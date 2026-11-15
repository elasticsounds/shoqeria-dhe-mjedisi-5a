# PDF page 52 — Provoje veten (one question per section).
L = 'Provoje veten'
section(title('Provoje veten', practice=True),
  task('1.', 'Shkruaj dy raste kur je treguar mirëkuptues.',
       body='<div class="p2-numbered"><b aria-hidden="true">•</b>' + field('lined', 'Rasti i parë kur je treguar mirëkuptues', rows=2) +
            '<b aria-hidden="true">•</b>' + field('lined', 'Rasti i dytë kur je treguar mirëkuptues', rows=2) + '</div>'),
  lesson=L, practice=True)
section(rule(True),
  task('2.', 'Trego për ndonjë bashkëpunim të suksesshëm që ke pasur në klasën tënde.',
       body=field('lined', 'Trego për ndonjë bashkëpunim të suksesshëm që ke pasur në klasën tënde.', rows=6)), practice=True)
section(rule(True),
  task('3.', 'Si e kupton këtë thënie:',
       body='<p class="p2-quote">' + t('“Suksesi ynë vërtet është bazuar në bashkëpunim që në fillim”, - Bill Gates.',
                                       'Bill Gates ka thënë:\n“Suksesi ynë vërtet është bazuar në bashkëpunim që në fillim”.') + '</p>' +
            field('lined', 'Si e kupton thënien e Bill Gates për bashkëpunimin?', rows=4)), practice=True)
