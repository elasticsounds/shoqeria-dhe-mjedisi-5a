# PDF page 60 — Provoje veten (one question per section).
L = 'Provoje veten'
section(title('Provoje veten', practice=True),
  task('1.', 'Shkruaj si e kupton procesin e ndërmjetësimit:',
       body='<p class="p2-quote">' + t('“Fjala e mirë i hap të gjitha dyert!”', '“Fjala e mirë i hap të gjitha dyert!”') + '</p>' +
            field('lined', 'Shkruaj si e kupton procesin e ndërmjetësimit: “Fjala e mirë i hap të gjitha dyert!”', rows=5)),
  lesson=L, practice=True)
section(rule(True),
  task('2.', 'Shkruaj hapat e procesit të ndërmjetësimit.',
       body=field('lined', 'Shkruaj hapat e procesit të ndërmjetësimit.', rows=5)), practice=True)
section(rule(True),
  '<aside class="b-lesson-thought is-research">' +
  '<p class="p2-step">' + t('Zgjidhni një nxënës që ka pasur përvojën më të mirë të ndërmjetësimit dhe dy nxënës të tjerë, të cilët e improvizojnë (imagjinojnë) një rast konflikti apo mosmarrëveshjeje.',
                            'Zgjidhni një nxënës që ka ndërmjetësuar më mirë.\nZgjidhni edhe dy nxënës të tjerë.\nAta dy luajnë një konflikt të imagjinuar.') + '</p>' +
  '<p class="p2-step">' + t('Të gjithë nxënësit le të shohin se si po e zgjidh konfliktin ndërmjetësuesi i caktuar.',
                            'Të gjithë nxënësit shohin si e zgjidh konfliktin ndërmjetësuesi.') + '</p></aside>',
  practice=True)
