# PDF page 61 — chapter and lesson start: "Të drejtat tona".
L = 'Të drejtat tona'
CSS = '''#content.book.p2 .p61-name{margin:0 0 10px;font:600 22px/1.4 var(--book-heading)}
#content.book.p2 .p61-quote{font-weight:400}
#content.book.p2 .p61-by{margin:8px 0 0;text-align:right;font:400 20px/1.4 var(--book-heading)}
'''
section(title(L, kicker='E drejta e secilit garanton të drejtën e të gjithëve'), keywords('e drejta jonë, liri, barazi, drejtësi, institucion.'),
  panel('thought', 'Shpreh mendimin tënd', items(
    ('Çfarë ndodh në një komunitet ku njerëzit nuk kanë njohuri për të drejtat e tyre?', 'Çfarë ndodh në një komunitet ku njerëzit nuk i njohin të drejtat e tyre?'),
    ('Po në rastin kur njerëzit i njohin të drejtat e tyre?', 'Po kur njerëzit i njohin të drejtat e tyre?'))),
  media('pg061_im001.png', 'Një vajzë me syze mban dorën te mjekra dhe mendon.',
    para(
      ('Të drejtat e njeriut janë themeli i lirisë, i paqes dhe i drejtësisë, pasi të gjithë njerëzit lindin të lirë e të barabartë në të drejta.',
       'Të drejtat e njeriut janë baza e lirisë, e paqes dhe e drejtësisë.\nTë gjithë njerëzit lindin të lirë.\nTë gjithë kanë të drejta të barabarta.'),
      ('Njerëzit kanë luftuar për mbrojtjen dhe respektimin e të drejtave të tyre, duke e përmirësuar edhe jetën në shoqërinë e tyre.',
       'Njerëzit kanë luftuar për t’i mbrojtur të drejtat e tyre.\nKështu e kanë bërë jetën në shoqëri më të mirë.')),
    para(
      ('Njerëzve në botë u ka ndodhur shumë herë që t’u shkelen dhe të mos u respektohen të drejtat e tyre.',
       'Shumë herë, njerëzve në botë u janë shkelur të drejtat.'),
      ('Kështu, ata çdoherë kanë luftuar për to, duke e përmirësuar edhe jetën në shoqërinë demokratike.',
       'Prandaj ata gjithmonë kanë luftuar për të drejtat e tyre.\nKështu e kanë bërë më të mirë jetën në shoqërinë demokratike.'),
      ('Njerëzit janë të barabartë, pa marrë parasysh racën, gjininë, moshën, kulturën apo çfarëdo faktori tjetër.',
       'Njerëzit janë të barabartë.\nNuk ka rëndësi raca, gjinia, mosha ose kultura.'),
      ('Në rast të shkeljes së të drejtave, njerëzit çdoherë duhet të kërkojnë ndihmë nga institucionet e duhura, si shkolla, policia etj. dhe asnjëherë nuk duhet të heshtin e të pajtohen me atë situatë, pasi të drejtat e tyre mbrohen me ligj.',
       'Kur u shkelen të drejtat, njerëzit duhet të kërkojnë ndihmë.\nNdihmë japin institucionet, si shkolla dhe policia.\nNjerëzit nuk duhet të heshtin.\nLigji i mbron të drejtat e tyre.'))),
  lesson=L, stype='text_and_images')
section(rule(),
  media('pg061_im002.png', 'Fotografi bardhë e zi e Eleanor Roosevelt-it, një grua e moshuar e buzëqeshur me një laps në dorë.',
    body='<div class="b-lesson-text"><p class="p61-name">' + t('Anna Eleanor Roosevelt') + '</p>' +
      para(
        ('Lindi në Nju-Jork më 11 tetor 1884.', 'Ajo lindi në Nju-Jork më 11 tetor 1884.'),
        ('Ajo ishte kryetarja e parë e Komisionit të OKB-së për të Drejtat e Njeriut dhe mbikëqyri hartimin e Deklaratës Universale të të Drejtave të Njeriut.',
         'Ajo ishte kryetarja e parë e Komisionit të OKB-së për të Drejtat e Njeriut.\nAjo drejtoi shkrimin e Deklaratës Universale të të Drejtave të Njeriut.'),
        ('Mbrojti të drejtat e grave në vendin e punës.', 'Ajo mbrojti të drejtat e grave në punë.'),
        ('Konsiderohet një nga gratë më të vlerësuara në botë.', 'Ajo është një nga gratë më të vlerësuara në botë.')) +
      '<p class="p2-quote p61-quote">' + t('Në të gjithë botën ka shumë njerëz të cilët nuk gëzojnë të drejtat më elementare dhe bazike, të cilat duhen pranuar në çdo cep të botës si të drejta të qenësishme të të gjithë individëve, pa të cilat asnjë qenie njerëzore nuk mund të jetojë dinjitetshëm dhe e lirë.',
        'Në botë ka shumë njerëz që nuk i kanë as të drejtat më të thjeshta.\nKëto të drejta duhet t’i ketë çdo njeri, kudo në botë.\nPa to, askush nuk mund të jetojë me dinjitet dhe i lirë.') + '</p>' +
      '<p class="p61-by">' + t('Eleanor Roosevelt') + '</p></div>'),
  css=CSS, stype='text_and_images')
