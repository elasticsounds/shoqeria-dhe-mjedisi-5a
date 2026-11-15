# PDF page 83 — Provoje veten (after "Ardhja e popujve të tjerë në Kosovë"); one question per section.
L = 'Provoje veten'
section(title('Provoje veten', practice=True),
  task('1.', 'Shkruani emrat e disa popujve që erdhën në Dardani.',
       body=field('lined', 'Shkruani emrat e disa popujve që erdhën në Dardani.', rows=3)),
  lesson=L, practice=True)
section(rule(True),
  task('2.', 'Me cilët popuj bashkëjetonin shqiptarët në trojet e Dardanisë?',
       body=field('lined', 'Me cilët popuj bashkëjetonin shqiptarët në trojet e Dardanisë?', rows=2)), practice=True)
section(rule(True),
  task('3.', ('Formoni tri fjali për burimet e çmueshme natyrore që gjenden në Kosovë.',
              'Shkruani tri fjali për pasuritë natyrore që gjenden në Kosovë.'),
       body='<div class="p2-numbered">' + ''.join(f'<b aria-hidden="true">{n}.</b>' + field('line', f'Fjalia {n} për burimet e çmueshme natyrore në Kosovë') for n in (1, 2, 3)) + '</div>'),
  practice=True)
