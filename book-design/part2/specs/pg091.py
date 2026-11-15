# PDF page 91 — continuation of Pavarësia e Kosovës (the sentence split across pages 90/91 is on page 90).
L = 'Pavarësia e Kosovës'
section(rule(), text(
  para(('Kjo gjendje e vështirë nxiti rezistencën popullore dhe formimin e Ushtrisë Çlirimtare të Kosovës.',
        'Gjendja ishte e vështirë.\nPrandaj populli filloi të rezistonte.\nU formua Ushtria Çlirimtare e Kosovës.'),
       ('Kosovës iu desh ta fitonte pavarësinë e saj nga Serbia e Millosheviçit, pas shumë përpjekjeve në rrethanat e vështira të pushtimit serb që zgjati 10 vjet (1989-1999).',
        'Kosova duhej ta fitonte pavarësinë nga Serbia e Millosheviçit.\nPushtimi serb zgjati 10 vjet, nga viti 1989 deri në vitin 1999.\nKjo kërkoi shumë përpjekje në kushte të vështira.')),
  para(('Qëndresa paqësore mbarëpopullore në Kosovë u drejtua nga Ibrahim Rugova.',
        'I gjithë populli i Kosovës rezistoi në mënyrë paqësore.\nKëtë qëndresë e drejtoi Ibrahim Rugova.'),
       ('Si pasojë e vështirësive për të siguruar pavarësinë, UÇK-ja organizoi rezistencën dhe çlirimin e Kosovës nga pushtimi serb.',
        'Ishte e vështirë të fitohej pavarësia.\nPrandaj UÇK-ja organizoi rezistencën dhe çlirimin e Kosovës nga pushtimi serb.'),
       ('Simbol i kësaj lufte është heroi Adem Jashari, bashkë me familjen e tij.', 'Heroi Adem Jashari dhe familja e tij janë simbol i kësaj lufte.'),
       ('Ndërhyrja e NATO-s në pranverë të vitit 1999 dhe rezistenca e armatosur e UÇK-së i dhanë fund sundimit të Serbisë.',
        'Në pranverën e vitit 1999 ndërhyri NATO-ja.\nUÇK-ja rezistoi me armë.\nKështu mori fund sundimi i Serbisë.'),
       ('Në Kosovë u vendosën trupat ndërkombëtare paqeruajtëse, ndërsa trupat serbe u detyruan të largoheshin.',
        'Në Kosovë erdhën trupat ndërkombëtare që ruajnë paqen.\nTrupat serbe u detyruan të largoheshin.'),
       ('Kështu, u krijuan rrethanat e përshtatshme për formimin e shtetit të pavarur të Kosovës.',
        'Kështu u krijuan kushtet për shtetin e pavarur të Kosovës.'),
       ('Pavarësia e Kosovës u shpall më 17 shkurt 2008.', 'Pavarësia e Kosovës u shpall më 17 shkurt 2008.'),
       ('Udhëheqja shtetërore bëri përgatitjen e dokumenteve dhe të simboleve të shtetit të Kosovës, si: Deklarata e Pavarësisë, Kushtetuta, Stema, Flamuri dhe Himni.',
        'Udhëheqësit e shtetit përgatitën dokumentet dhe simbolet e Kosovës:\n- Deklarata e Pavarësisë\n- Kushtetuta\n- Stema\n- Flamuri\n- Himni'),
       ('Kjo ishte një ngjarje e rëndësishme dhe historike për popullin e Kosovës.', 'Kjo ishte një ngjarje e rëndësishme dhe historike për popullin e Kosovës.'),
       ('Në Kuvendin e Kosovës u lexua Deklarata e Pavarësisë së Kosovës nga kryeminstri Hashim Thaçi.',
        'Kryeministri Hashim Thaçi e lexoi Deklaratën e Pavarësisë në Kuvendin e Kosovës.'),
       ('Ajo kurorëzoi një rrugëtim të gjatë dhe shumë të vështirë për banorët e saj.',
        'Kështu përfundoi me sukses një rrugë e gjatë dhe shumë e vështirë për banorët e Kosovës.'),
       ('Republika e Kosovës dhe banorët e saj gëzojnë në mënyrë të plotë të drejtat e tyre demokratike.',
        'Sot Republika e Kosovës dhe banorët e saj i kanë plotësisht të drejtat demokratike.'))), lesson=L)
# written questions on the left, the two photographs stacked on the right (one column on narrow screens)
section(rule(),
  '<div class="p91-split">' +
  panel('questions', 'Pyetje për ty', questions(
    ('Cilat ngjarje ndodhën deri te Pavarësia e Kosovës?', 'Çfarë ndodhi para Pavarësisë së Kosovës?'),
    ('Cilat ishin pasojat e dhunës së organizuar shtetërore të Serbisë kundër popullit të Kosovës?',
     'Shteti i Serbisë përdori dhunë kundër popullit të Kosovës.\nÇfarë pasojash pati kjo dhunë?'),
    'Përse NATO-ja ndihmoi Kosovën?',
    ('Për çfarë shërbeu vendosja e trupave ndërkombëtare në Kosovë?', 'Pse erdhën trupat ndërkombëtare në Kosovë?'))) +
  '<div class="p91-photos">' +
  figure('pg091_im001.png', 'Kryeministri lexon Deklaratën e Pavarësisë në Kuvendin e Kosovës, i rrethuar nga burra me kostume që rrinë në këmbë.', wide=False) +
  figure('pg091_im002.png', 'Njerëz të gëzuar festojnë pavarësinë dhe mbajnë flamurin e Kosovës.', wide=False) + '</div></div>',
  css='''#content.book.p2 .p91-split{display:grid;grid-template-columns:minmax(0,3fr) minmax(0,2fr);gap:28px;align-items:start}
#content.book.p2 .p91-split>.b-lesson-thought{margin:0}
#content.book.p2 .p91-photos .b-lesson-figure{margin:0 0 20px}
@media(max-width:900px){#content.book.p2 .p91-split{grid-template-columns:minmax(0,1fr)}}
''')
section(rule(),
  panel('internet', None,
    '<p class="p2-step">' + t('Bashkë me ndihmën e prindërve apo të mësuesit, hulumto në internet dhe gjej informacione mbi veprimtarinë e UÇK-së.',
                             'Kërko ndihmë nga prindërit ose nga mësuesi.\nHulumto në internet.\nGjej informacione për punën e UÇK-së.') + '</p>',
    '<p class="p2-step">' + t('Ndaje këtë informacion me shoqet dhe shokët e klasës.', 'Tregoju shoqeve dhe shokëve të klasës çfarë gjete.') + '</p>',
    '<p class="p2-step">' + t('Diskutoni së bashku rreth rolit të UÇK-së.', 'Flisni së bashku për rolin e UÇK-së.') + '</p>'),
  panel('glossary', 'Fjalorthi',
    para(('UÇK - Ushtria Çlirimtare e Kosovës.', 'UÇK do të thotë Ushtria Çlirimtare e Kosovës.')),
    para(('NATO - Organizata e Traktatit Atlantik të Veriut.', 'NATO do të thotë Organizata e Traktatit Atlantik të Veriut.'))))
