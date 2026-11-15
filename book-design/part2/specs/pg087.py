# PDF page 87 — lesson start: “Lidhja e Prizrenit”.
L = '“Lidhja e Prizrenit”'
section(title(L), keywords('Lidhja, vilajet, qeveri, diplomaci, pavarësi.'),
  panel('thought', 'Shpreh mendimin tënd',
    items(('Trego çfarë di rreth Lidhjes së Prizrenit.', 'Trego çfarë di për Lidhjen e Prizrenit.'),
          ('Shpreh me një fjali se çfarë dëshiron të mësosh rreth Lidhjes së Prizrenit.',
           'Shkruaj një fjali.\nÇfarë dëshiron të mësosh për Lidhjen e Prizrenit?')),
    field('lined', 'Shpreh me një fjali se çfarë dëshiron të mësosh rreth Lidhjes së Prizrenit.', rows=2)),
  figure('pg087_im001.png', 'Shtëpia e Lidhjes së Prizrenit: ndërtesë e bardhë tradicionale me kat të sipërm të dalë dhe oborr me kalldrëm.'),
  lesson=L, stype='text_and_images')
section(rule(),
  media('pg087_im002.png', 'Pikturë e Kuvendit të Lidhjes së Prizrenit: burra me veshje tradicionale shqiptare rrinë ulur në një sallë, ndërsa njëri në mes flet në këmbë.',
    para(('Shqiptarët bënin luftëra të vazhdueshme për t’u çliruar nga pushtuesit osmanë.',
          'Shqiptarët luftonin vazhdimisht për t’u çliruar nga pushtuesit osmanë.'),
         ('Të gjithë shqiptarët u bashkuan në luftën për liri.', 'Të gjithë shqiptarët u bashkuan në luftën për liri.'),
         ('Më 10 qershor të vitit 1878, në Prizren, u mblodhën përfaqësues nga të gjitha vendet shqiptare dhe e formuan Lidhjen e Prizrenit.',
          'Më 10 qershor 1878, në Prizren u mblodhën përfaqësues nga të gjitha vendet shqiptare.\nAta e formuan Lidhjen e Prizrenit.'),
         ('Ajo e ushtroi veprimtarinë e saj në 4 provincat (vilajetet) e Perandorisë Osmane, të banuara kryesisht nga shqiptarë.',
          'Lidhja punoi në 4 provinca të Perandorisë Osmane.\nProvincat quheshin vilajete.\nNë to jetonin kryesisht shqiptarë.'),
         ('Qëllimi i Lidhjes ishte mbrojtja e këtyre territoreve dhe bashkimi i tyre.',
          'Lidhja donte t’i mbronte këto toka dhe t’i bashkonte.')),
    para(('Lidhja drejtohej nga një grup patriotësh shqiptarë, që kundërshtuan me forcë ndarjen e territoreve shqiptare ndërmjet Serbisë, Malit të Zi, Bullgarisë dhe Greqisë.',
          'Lidhjen e drejtonte një grup patriotësh shqiptarë.\nAta nuk donin që tokat shqiptare të ndaheshin mes Serbisë, Malit të Zi, Bullgarisë dhe Greqisë.'),
         ('Ata u përpoqën në çdo mënyrë që ta mbronin vendin nga rreziku i pushtimit të huaj.',
          'Ata bënë gjithçka për ta mbrojtur vendin nga pushtuesit e huaj.'),
         ('Këtë e tregon dhe vendimi që doli nga Kuvendi i themelimit të Lidhjes.',
          'Këtë e tregon edhe vendimi i Kuvendit që e themeloi Lidhjen.')), reversed=True),
  stype='text_and_images')
section(rule(), panel('questions', 'Pyetje për ty',
  '<p class="p2-quote">' + t('“Ne me gjithë zemër dëshirojmë që të jetojmë në paqe me fqinjët tanë, Serbinë, Malin e Zi, Greqinë dhe Bullgarinë...',
                             '“Ne duam me gjithë zemër të jetojmë në paqe me fqinjët tanë: Serbinë, Malin e Zi, Greqinë dhe Bullgarinë.') + ' ' +
      t('Ne nuk duam dhe nuk do të kërkojmë asgjë, veçse jemi të vendosur të mbrojmë atë që na përket neve.”',
        'Ne nuk kërkojmë asgjë.\nNe vetëm do ta mbrojmë atë që është jona.”') + '</p>',
  '<p class="p87-source">' + t('Pjesë nga Vendimi i Lidhjes së Prizrenit, 1878.') + '</p>',
  questions(('Si e kupton këtë pjesë të Vendimit të Lidhjes?', 'Si e kupton ti këtë pjesë të Vendimit të Lidhjes?')) +
  questions(('Cilat ishin vendet fqinje me territoret e banuara nga shqiptarët në kohën e themelimit të Lidhjes?',
     'Cilat vende ishin fqinje me tokat ku jetonin shqiptarët, kur u themelua Lidhja?')) +
  # the book says "underline"; in the reader the pupil types the words instead (owner's decision)
  questions(('Shkruaji fjalët që tregojnë se shqiptarët donin vetëm paqe.', 'Shkruaji fjalët që tregojnë se shqiptarët donin vetëm paqe.')) +
  questions(('Cili ishte qëllimi i themelimit të Lidhjes së Prizrenit?', 'Pse u themelua Lidhja e Prizrenit?'))),
  css='#content.book.p2 .p87-source{margin:0 0 16px;text-align:right;font:400 20px/1.5 var(--book-heading)}\n')
