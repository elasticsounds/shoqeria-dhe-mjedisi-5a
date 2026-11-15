# PDF page 77 — continuation of "Të barabartë para ligjit".
L = 'Të barabartë para ligjit'
FIELD_CSS = '''#content.book.p2 .b-lesson-thought input.prx-field{display:block;width:100%;max-width:100%;min-height:52px;margin:0;padding:10px 14px;border:2px solid #4f6b3a;border-radius:10px;background:#fff;color:var(--book-ink);font:400 20px/1.5 var(--book-heading);box-shadow:none}
#content.book.p2 .b-lesson-thought input.prx-field:focus-visible{outline:3px solid #075a70;outline-offset:2px;border-color:#075a70}
#content.book.p2 .b-lesson-thought .p2-numbered{margin:12px 0 0}
'''
section(rule(), panel('questions', 'Pyetje për ty', questions(
    'Kush i mbron të drejtat e tua?',
    ('Cilat janë ligjet më themelore për rregullimin e jetës në komunitet?', 'Cilat janë ligjet më të rëndësishme që e rregullojnë jetën në komunitet?'),
    ('Cilat janë disa prej të drejtave themelore të fëmijëve që mbrohen me ligj?', 'Cilat janë disa të drejta të fëmijëve që i mbron ligji?'))), lesson=L)
section(rule(), panel('discussion', 'Diskuto',
    items(
      ('Diskutojmë së bashku Nenin 7 të Deklaratës Universale të të Drejtave të Njeriut: “Të gjithë janë të barabartë para ligjit dhe kanë të drejtë pa asnjë diskriminim të mbrohen barabar nga ligji.”',
       'Diskutojmë së bashku Nenin 7 të Deklaratës Universale të të Drejtave të Njeriut.\nNeni 7 thotë:\n“Të gjithë janë të barabartë para ligjit dhe kanë të drejtë pa asnjë diskriminim të mbrohen barabar nga ligji.”'),
      ('Shkruaj tri fjali për rëndësinë që ka zbatimi i ligjit:', 'Shkruaj tri fjali.\nTrego pse është i rëndësishëm zbatimi i ligjit.')),
    '<div class="p2-numbered">' + ''.join(f'<b aria-hidden="true">{n}.</b>' + field('line', f'Fjalia {n} për rëndësinë që ka zbatimi i ligjit') for n in (1, 2, 3)) + '</div>'),
  css=FIELD_CSS)
section(rule(), panel('discussion', None,
    '<p class="p2-step p77-lead">' + t('Punë në grupe:') + '</p>',
    '<p class="p2-step">' + t('Ndahuni në grupe dhe diskutoni për të drejtat dhe barazinë në situatat e dhëna:',
                             'Ndahuni në grupe.\nDiskutoni për të drejtat dhe barazinë në këto situata:') + '</p>',
    '<p class="p2-step">' + t('Grupi 1 - Kur një fëmijë përjashtohet nga loja.', 'Grupi 1: Kur një fëmijë përjashtohet nga loja.') + '</p>',
    '<p class="p2-step">' + t('Grupi 2 - Kur vetëm disa nxënës lejohen të luajnë.', 'Grupi 2: Kur vetëm disa nxënës lejohen të luajnë.') + '</p>',
    '<p class="p2-step">' + t('Grupi 3 - Vajzat nuk lejohen të marrin pjesë në një aktivitet.', 'Grupi 3: Kur vajzat nuk lejohen të marrin pjesë në një aktivitet.') + '</p>'),
  css='#content.book.p2 .b-lesson-thought .p77-lead{font-weight:600}\n')
section(rule(), panel('research', None,
    '<p class="p2-step">' + t('Bashkë me ndihmën e prindërve apo të mësuesit, hulumto në internet dhe gjej një rast, ku mendon se njerëzit nuk janë trajtuar në mënyrë të barabartë para ligjit.',
                             'Hulumto në internet me ndihmën e prindërve ose të mësuesit.\nGjej një rast ku njerëzit nuk janë trajtuar njësoj para ligjit.') + '</p>',
    '<p class="p2-step">' + t('Diskutojeni së bashku me shoqet e shokët e klasës dhe analizojeni rastin.',
                             'Diskutojeni rastin me shoqet dhe shokët e klasës.\nAnalizojeni së bashku.') + '</p>'))
section(rule(), heading('deepen', 'Thello dijet'),
  text(para(
    ('Të gjithë njerëzit duhet të kenë të drejta të barabarta përpara ligjit.', 'Të gjithë njerëzit duhet të kenë të drejta të barabarta para ligjit.'),
    ('Në një shtet demokratik, është shumë e rëndësishme që secili të trajtohet drejt dhe me ndershmëri nga ligji.',
     'Në një shtet demokratik, ligji duhet ta trajtojë secilin drejt dhe me ndershmëri.\nKjo është shumë e rëndësishme.'),
    ('Gjykatat mbrojnë në mënyrë të barabartë të gjithë njerëzit, sepse përballë ligjit të gjithë janë të barabartë.',
     'Gjykatat i mbrojnë të gjithë njerëzit njësoj.\nPara ligjit, të gjithë janë të barabartë.'),
    ('Njerëzit kanë të drejtë që të mbrohen nga çdo padrejtësi.', 'Njerëzit kanë të drejtë të mbrohen nga çdo padrejtësi.'))))
