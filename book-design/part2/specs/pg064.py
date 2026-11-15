# PDF page 64 — lesson start: "Fëmijët gëzojnë të drejta".
L = 'Fëmijët gëzojnë të drejta'
CSS = '''#content.book.p2 .p64-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;margin:16px 0 0}
#content.book.p2 .p64-card{display:grid;gap:8px;align-content:start;padding:14px;border-radius:12px;background:#fff}
#content.book.p2 .p64-card .b-lesson-figure{margin:0 auto;max-width:260px}
#content.book.p2 .p64-card .b-lesson-figure img{height:180px;object-fit:contain;border-radius:0}
#content.book.p2 .p64-card label{display:block;text-align:center;font:600 22px/1.4 var(--book-heading);color:var(--book-ink);padding:0}
#content.book.p2 .p64-card input.prx-field{display:block;width:100%;max-width:100%;min-height:52px;margin:0;padding:10px 14px;border:2px solid #6d6472;border-radius:10px;background:#fff;color:var(--book-ink);font:400 20px/1.5 var(--book-heading);box-shadow:none}
#content.book.p2 .p64-card input.prx-field:focus-visible{outline:3px solid #075a70;outline-offset:2px;border-color:#075a70}
@media(max-width:700px){#content.book.p2 .p64-grid{grid-template-columns:minmax(0,1fr)}#content.book.p2 .p64-card label{font-size:20px}}
'''
PICS = [('pg064_im001.png', 'Shumë duar me ngjyra të ndryshme lëkure bashkojnë grushtet në një rreth.', 'Tolerancë'),
        ('pg064_im002.png', 'Një kafaz i hapur dhe tre zogj që fluturojnë të lirë.', 'Liri'),
        ('pg064_im003.png', 'Një pëllumb i bardhë me krahë të hapur mban një degë ulliri në sqep.', 'Paqe'),
        ('pg064_im004.png', 'Shumë duar me ngjyra të ndryshme lëkure mbajnë së bashku një zemër të kuqe.', 'Dashuri')]
def card(f, alt, word):
    i = f'item-{P.fn + 1}'
    return ('<div class="p64-card"><figure class="b-lesson-figure">' + img(f, alt) + '</figure><label for="' + i + '">' + t(word) + '</label>' +
            field('line', '') + '</div>')
section(title(L), keywords('konventë, e drejtë, mbështetje, fëmijë, respekt.'),
  panel('thought', 'Shpreh mendimin tënd', items(
      ('Diskutoni rreth fotografive të mëposhtme.', 'Flisni për fotografitë më poshtë.'),
      ('Shkruani nga një fjali me secilën prej fjalëve të dhëna.', 'Shkruani një fjali me secilën fjalë.')),
    '<div class="p64-grid">' + ''.join(card(*p) for p in PICS) + '</div>'),
  lesson=L, stype='text_and_images', css=CSS)
section(rule(),
  text(para(
    ('Situatë: - Familja e Bledit kishte kohë që jetonte në Zvicër.', 'Situata:\nFamilja e Bledit jetonte prej kohësh në Zvicër.'),
    ('Si fëmijë ishim kuriozë për shokët e rinj të Bledit dhe për shkollën që po ndiqte atje.',
     'Ne fëmijët ishim kuriozë për shokët e rinj të Bledit.\nIshim kuriozë edhe për shkollën e tij atje.'),
    ('Ne e dinim që e drejta për arsimim është një e drejtë themelore e cilitdo fëmijë që jeton në Republikën e Kosovës dhe në mbarë botën.',
     'Ne e dinim se çdo fëmijë ka të drejtë të shkojë në shkollë.\nKjo vlen në Republikën e Kosovës dhe në gjithë botën.'),
    ('Shkëmbyem kontakte me Bledin, sepse donim të dinim më shumë për rregullat e shkollimit, programet apo mësimet që do të ndiqte ai.',
     'Ne morëm kontaktet e Bledit.\nDonim të dinim më shumë për rregullat e shkollës, programet dhe mësimet e tij.'),
    ('Të drejtat e fëmijëve, edhe pse mbrohen nga Konventa Ndërkombëtare, mund të mos respektohen njëlloj në të gjitha vendet e botës.',
     'Konventa Ndërkombëtare i mbron të drejtat e fëmijëve.\nPor këto të drejta nuk respektohen njësoj në të gjitha vendet e botës.'))))
section(rule(), heading('deepen', 'Thello dijet'),
  text(para(
    ('Në të kaluarën, por edhe sot në disa vende të botës, fëmijët janë trajtuar keq dhe nuk janë respektuar.',
     'Në të kaluarën, fëmijët janë trajtuar keq dhe nuk janë respektuar.\nKjo ndodh edhe sot në disa vende të botës.'),
    ('Shpeshherë ata janë përballur me padrejtësi dhe ndonjëherë edhe me dhunë, në shkollë, në familje apo në vendin ku jetojnë.',
     'Shpesh fëmijët kanë përjetuar padrejtësi.\nNdonjëherë kanë përjetuar edhe dhunë: në shkollë, në familje ose në vendin ku jetojnë.'),
    ('Të drejtat e fëmijëve janë krijuar për t’i mbrojtur ata, për t’ua siguruar kujdesin mjekësor, shtëpinë, shkollën, lojërat dhe për t’ua dhënë mundësinë që të marrin pjesë në jetën shoqërore si të gjithë të tjerët.',
     'Të drejtat e fëmijëve janë krijuar për t’i mbrojtur fëmijët.\nAto u sigurojnë kujdes mjekësor, shtëpi, shkollë dhe lojëra.\nAto u japin mundësi të marrin pjesë në jetën shoqërore si të gjithë të tjerët.')),
   '<p><strong>' + t('Pse në botë ka fëmijë që punojnë edhe pse janë nën moshën e punës?',
                     'Pse në botë ka fëmijë që punojnë, edhe pse janë shumë të vegjël për punë?') + '</strong></p>'))
