# PDF page 90 — lesson start: Pavarësia e Kosovës. The last sentence of the page continues on page 91; it is kept whole here.
L = 'Pavarësia e Kosovës'
section(title(L), keywords('NEWBORN, NATO, UÇK, deklaratë, pavarësi.'),
  gallery(('pg090_im001.png', 'Monumenti “NEWBORN” në Prishtinë: shkronja të mëdha të verdha në një shesh të qytetit.', None),
          ('pg090_im002.png', 'Flamuri i Kosovës: i kaltër, me hartën e Kosovës në ngjyrë të artë dhe gjashtë yje të bardhë sipër saj.', None), cols=2),
  panel('thought', 'Shpreh mendimin tënd',
    '<ul><li>' + t('Çfarë përfaqësojnë 6 yjet në flamurin e Kosovës?', 'Çfarë tregojnë 6 yjet në flamurin e Kosovës?') + '</li><li>' +
    t('Në cilin qytet gjendet monumenti “NEWBORN”?', 'Në cilin qytet është monumenti “NEWBORN”?') + ' ' +
    t('Çfarë përfaqëson ky monument?', 'Çfarë tregon ky monument?') + '</li><li>' +
    t('Çfarë di për Pavarësinë e Kosovës?', 'Çfarë di për Pavarësinë e Kosovës?') + ' ' +
    t('Çfarë ju sjell ndër mend Pavarësia e Kosovës?', 'Çfarë mendoni kur dëgjoni për Pavarësinë e Kosovës?') + ' ' +
    t('Plotësoni rrathët e mëposhtëm me disa nga faktet më të rëndësishme për pavarësinë.',
      'Shkruani në rrathët më poshtë disa nga faktet më të rëndësishme për pavarësinë.') + '</li></ul>'),
  '<div class="p90-facts">' + field('area', 'Fakti 1 për Pavarësinë e Kosovës', rows=3) +
  '<p class="p90-centre">' + t('Pavarësia e Kosovës') + '</p>' +
  ''.join(field('area', f'Fakti {n} për Pavarësinë e Kosovës', rows=3) for n in (2, 3, 4, 5)) + '</div>',
  lesson=L, stype='text_and_images',
  css='''#content.book.p2 .p90-facts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;align-items:center;margin:0 0 24px}
#content.book.p2 .p90-centre{margin:0;font:600 22px/1.4 var(--book-heading);color:var(--book-ink);text-align:center}
#content.book.p2 .p90-facts textarea.prx-field{display:block;width:100%;max-width:100%;min-height:120px;margin:0;padding:18px 24px;border:2px solid var(--book-purple-ink);border-radius:60px;background:#fff;color:var(--book-ink);font:400 20px/1.5 var(--book-heading);box-shadow:none;resize:vertical}
#content.book.p2 .p90-facts textarea.prx-field:focus-visible{outline:3px solid #075a70;outline-offset:2px}
@media(max-width:700px){#content.book.p2 .p90-facts{grid-template-columns:minmax(0,1fr)}#content.book.p2 .p90-centre{order:-1;font-size:20px}#content.book.p2 .p90-facts textarea.prx-field{border-radius:28px}}
''')
section(rule(), text(para(
    ('Pas shkëputjes së një pjese të territoreve shqiptare nga sundimi osman në vitin 1912, u krijua shteti i pavarur shqiptar.',
     'Në vitin 1912, një pjesë e tokave shqiptare u nda nga sundimi osman.\nKështu u krijua shteti i pavarur shqiptar.'),
    ('Kosova, ndërkohë, mbeti jashtë Shqipërisë së pavarur pasi u pushtua nga Serbia dhe u bë pjesë e shtetit të sllavëve të jugut, të sunduar nga serbët, kroatët dhe sllovenët.',
     'Kosova mbeti jashtë Shqipërisë së pavarur.\nAtë e pushtoi Serbia.\nKosova u bë pjesë e shtetit të sllavëve të jugut.\nKëtë shtet e sundonin serbët, kroatët dhe sllovenët.'),
    ('Ajo mbeti për gati 90 vjet nën sundimin jugosllav.', 'Kosova mbeti gati 90 vjet nën sundimin jugosllav.'),
    ('Kosova është vendi i fundit që fitoi mëvetësinë, si rrjedhojë e shpërbërjes së Federatës Jugosllave më 1991.',
     'Federata Jugosllave u shpërbë në vitin 1991.\nKosova ishte vendi i fundit që u bë i pavarur pas kësaj.'),
    ('Për shumë vjet, populli i Kosovës vuajti mungesën e të drejtave dhe lirive themelore si pasojë e pushtimit serb.',
     'Për shumë vjet, populli i Kosovës nuk kishte të drejtat dhe liritë themelore.\nKjo ndodhi për shkak të pushtimit serb.'))))
