# PDF page 89 — Provoje veten (after “Lidhja e Prizrenit”); one question per section.
L = 'Provoje veten'
def col(head, name_label, text_label):
    h = ('<p class="p89-name">' + t(head) + '</p>') if head else field('line', name_label)
    return '<div class="p2-col">' + h + field('lined', text_label, rows=5) + '</div>'
section(title('Provoje veten', practice=True),
  task('1.', ('Identifiko udhëheqësit e Lidhjes së Prizrenit në shtatoren e dhënë.', 'Shiko shtatoren.\nGjej kush janë udhëheqësit e Lidhjes së Prizrenit.'),
       ('Hulumto dhe shkruaj për secilin prej tyre.', 'Hulumto dhe shkruaj për secilin prej tyre.'),
       body=figure('pg089_im001.png', 'Shtatore me tre udhëheqës të Lidhjes së Prizrenit: dy burra në këmbë dhe një i ulur në mes, para një flamuri; pas tyre shihet Shtëpia e Lidhjes.') +
            '<div class="p2-cols" style="--cols:3">' +
            col(None, 'Emri i udhëheqësit të parë në shtatore', 'Shkruaj për udhëheqësin e parë') +
            col('Ymer Prizreni', '', 'Shkruaj për Ymer Prizrenin') +
            col(None, 'Emri i udhëheqësit të tretë në shtatore', 'Shkruaj për udhëheqësin e tretë') + '</div>'),
  lesson=L, practice=True,
  css='''#content.book.p2 .p89-name{margin:0;min-height:52px;padding:10px 0;font:600 20px/1.5 var(--book-heading);color:var(--book-ink);text-align:center}
#content.book.p2 .prx-fields .b-lesson-figure{max-width:420px;margin:0 auto 20px}
''')
section(rule(True),
  task('2.', ('Shkruaj për Lidhjen e Prizrenit dhe qëllimin e themelimit të saj.', 'Shkruaj për Lidhjen e Prizrenit.\nShkruaj edhe pse u themelua ajo.'),
       body=field('lined', 'Shkruaj për Lidhjen e Prizrenit dhe qëllimin e themelimit të saj.', rows=4)), practice=True)
section(rule(True),
  task('3.', 'Lexo dhe puno sipas kërkesave.',
       body='<p class="p2-quote">' +
            t('“Ashtu sikurse nuk jemi dhe as duam të bëhemi turq, po ashtu do të kundërshtojmë me gjithë fuqinë tonë për të mos u shndërruar as në sllavë, as në austriakë dhe as në grekë.',
              '“Ne nuk jemi turq dhe nuk duam të bëhemi turq.\nNe do të kundërshtojmë me gjithë fuqinë që të mos bëhemi as sllavë, as austriakë, as grekë.') + ' ' +
            t('Ne veç duam të jemi shqiptarë.”', 'Ne duam të jemi vetëm shqiptarë.”') + '</p>' +
            '<p class="p89-source">' + t('Pjesë nga letra që “Lidhja e Prizrenit” i dërgoi delegacionit anglez në “Kongresin e Berlinit”, 1878.',
                                         'Kjo është pjesë nga një letër.\n“Lidhja e Prizrenit” ia dërgoi letrën delegacionit anglez në “Kongresin e Berlinit”, në vitin 1878.') + '</p>' +
            '<p class="prx-instruction">' + t('Nga teksti më lart, shkruaji fjalët që tregojnë se Lidhja e Prizrenit ishte e vendosur në qëllimet e saj.',
                                              'Shiko tekstin më lart.\nShkruaji fjalët që tregojnë se Lidhja e Prizrenit ishte e vendosur në qëllimet e saj.') + '</p>' +
            field('lined', 'Shkruaji fjalët që tregojnë se Lidhja e Prizrenit ishte e vendosur në qëllimet e saj.', rows=2)),
  practice=True,
  css='#content.book.p2 .p89-source{margin:0 0 20px;font:400 20px/1.5 var(--book-heading);color:var(--book-ink)}\n')
