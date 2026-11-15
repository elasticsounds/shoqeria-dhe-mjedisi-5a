# PDF page 65 — continuation of "Fëmijët gëzojnë të drejta" (lesson starts on page 64).
L = 'Fëmijët gëzojnë të drejta'
section(rule(),
  panel('questions', 'Pyetje për ty', questions(
    'Cilat janë të drejtat e fëmijëve në Kosovë?',
    ('Po të drejtat e fëmijëve në vendet e tjera të botës?', 'Cilat janë të drejtat e fëmijëve në vendet e tjera të botës?'),
    ('A janë respektuar të drejtat e fëmijëve në të kaluarën?', 'A janë respektuar të drejtat e fëmijëve dikur?'))), lesson=L)
section(rule(),
  panel('questions', 'Pyetje për ty', questions(
    'Po sot, a respektohen të drejtat e fëmijëve?',
    ('A janë të njëjta të drejtat që duhet të gëzojnë fëmijët në të gjithë botën?', 'A duhet të kenë fëmijët të njëjtat të drejta në të gjithë botën?'),
    ('A ka raste që këto të drejta shkelen? Pse?', 'A ka raste kur këto të drejta nuk respektohen?\nPse?')), toc=False))
section(rule(),
  figure('pg065_im001.png', 'Katër fëmijë të buzëqeshur mbajnë së bashku një tabelë të madhe të bardhë; njëri prej tyre ngre dorën.'),
  '<div class="p2-says">' + ''.join(para((s, s)) for s in (
      'Ne jemi fëmijët e botës, na trajtoni njëlloj!',
      'Secili nga ne ka një emër dhe një atdhe!',
      'Nëse sëmuremi, kujdesuni për ne!',
      'Na strehoni dhe na ushqeni!',
      'Ne kemi nevojë për një familje!',
      'Na mbroni nga ata që na keqtrajtojnë!')) +
      para(('Secila e drejtë ka përgjegjësitë që ne duhet t’i kryejmë!', 'Çdo e drejtë ka edhe përgjegjësi.\nNe duhet t’i kryejmë ato!')) + '</div>',
  stype='text_and_images', css='#content.book.p2 .p2-says{margin-bottom:32px}\n')
section(rule(),
  panel('research', None,
    '<p class="p2-step">' + t('Bashkë me ndihmën e prindërve apo të mësuesit, hulumto në internet dhe gjej raste ku tregohen shkelje të të drejtave të fëmijëve.',
                             'Hulumto në internet me ndihmën e prindërve ose të mësuesit.\nGjej raste kur nuk janë respektuar të drejtat e fëmijëve.') + '</p>',
    '<p class="p2-step">' + t('Diskutojini së bashku me shoqet e shokët e klasës.', 'Diskutoni për to me shoqet dhe shokët e klasës.') + '</p>',
    '<p class="p2-step">' + t('Çfarë mësove nga këto raste?', 'Çfarë mësove nga këto raste?') + '</p>',
    '<p class="p2-step">' + t('Cili është qëndrimi yt?', 'Çfarë mendon ti për to?') + '</p>'))
section(rule(),
  panel('discussion', 'Diskuto',
    para(('Në nenin 31.1. të Konventës së të Drejtave të Fëmijëve, thuhet: “Shtetet Palë i njohin fëmijës të drejtën të pushojë dhe të argëtohet, të praktikojë lojëra dhe veprimtari çlodhëse, në përputhje me moshën, si dhe të marrë pjesë lirisht në jetën kulturore dhe artistike.”',
          'Konventa e të Drejtave të Fëmijëve thotë në nenin 31.1:\nFëmija ka të drejtë të pushojë dhe të argëtohet.\nFëmija ka të drejtë të luajë lojëra që i përshtaten moshës së tij.\nFëmija ka të drejtë të marrë pjesë lirisht në jetën kulturore dhe artistike.')),
    items('Si zbatohet kjo e drejtë e fëmijëve në familjen tënde?', 'Si zbatohet kjo e drejtë te fëmijët e tjerë?')),
  css='#content.book.p2 .b-lesson-thought p{margin-bottom:12px}\n')
section(rule(),
  heading('deepen', 'Thello dijet'),
  text(para(
    ('Fëmijët kanë nevojë për kujdes të mirë shëndetësor, arsimim, ushqim, mjedis të pastër etj.',
     'Fëmijët kanë nevojë për:\n- kujdes të mirë për shëndetin\n- arsimim\n- ushqim\n- mjedis të pastër'),
    ('Ata duhet të mbrohen nga çdo lloj dhune, si rrahja, fyerjet, trajtimi i keq, puna e rrezikshme apo keqpërdorimi që dëmton trupin dhe mendjen e tyre.',
     'Fëmijët duhet të mbrohen nga çdo lloj dhune.\nDhunë janë: rrahja, fyerjet, trajtimi i keq dhe puna e rrezikshme.\nDhuna dëmton trupin dhe mendjen e fëmijëve.'),
    ('Fëmijët kanë të drejtë për pushim dhe argëtim, të praktikojnë lojëra dhe veprimtari argëtuese në përputhje me moshën.',
     'Fëmijët kanë të drejtë të pushojnë dhe të argëtohen.\nAta kanë të drejtë të luajnë lojëra që i përshtaten moshës së tyre.'),
    ('Fëmijët me nevoja të veçanta, kanë nevojë për kujdes dhe mbështetje të shoqërisë dhe të shtetit.',
     'Fëmijët me nevoja të veçanta kanë nevojë për kujdes.\nShoqëria dhe shteti duhet t’i mbështesin ata.'))))
