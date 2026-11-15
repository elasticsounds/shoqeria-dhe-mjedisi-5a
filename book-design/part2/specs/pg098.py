# PDF page 98 — Provoje veten: end-of-book test, questions 1–10 (continues on page 99). Reader activities: question 1 is multiple choice, the rest are
# fill-in-the-blank sections checked with the reader's Submit button (see keyed()/choice() in build.py).
L = 'Provoje veten'
CSS = '''#content.book.p2.prx input.prx-field.p2-blank{display:inline-block;width:var(--w,11em);max-width:100%;min-height:44px;margin:4px 2px;padding:4px 10px;vertical-align:middle}
#content.book.p2 .p2-fill{margin:0 0 28px;font:400 22px/2.2 var(--book-heading);color:var(--book-ink)}
#content.book.p2 .p2-fill .prx-lined{margin-top:6px}
#content.book.p2 .p2-choice{display:block;margin:0 0 8px;padding:10px 14px;border:2px solid #cdb8dc;border-radius:12px;background:#fff;font:400 20px/1.4 var(--book-heading);color:var(--book-ink);cursor:pointer}
#content.book.p2 .p2-choice input{width:22px;height:22px;margin:0 10px 0 0;vertical-align:-4px;accent-color:#794282}
#content.book.p2 .p2-choice:has(input:checked){border-color:#794282;background:#f3ecf8}
#content.book.p2 .p2-choice:has(input:focus-visible){outline:3px solid #075a70;outline-offset:2px}
#content.book.p2 .p2-group{margin:0 0 28px;padding:0;border:0}
#content.book.p2 .p2-group legend{margin:0 0 10px;padding:0;font:400 22px/1.5 var(--book-heading)}
@media(max-width:700px){#content.book.p2 .p2-fill,#content.book.p2 .p2-group legend{font-size:20px}}
'''
def blank(label, w=11, *answers):
    f = field('line', label).replace('class="prx-field"', f'class="prx-field p2-blank" style="--w:{w}em"')
    return keyed(f, *answers) if answers else open_answer(f)
def fill(*parts): return '<div class="p2-fill">' + ' '.join(parts) + '</div>'
# Answer keys come from the lesson pages (79, 80, 82, 84, 87, 88). Lists (tribes, leaders, places) accept the items in any order.
SLAVS = ('serbët', 'serbë', 'kroatët', 'kroatë', 'malazezët', 'malazezë', 'sllovenët', 'sllovenë')
section(title('Provoje veten', practice=True),
  '<fieldset class="p2-group"><legend>' + t('1. Ilirët janë:', '1. Ilirët janë:') + '</legend>' +
    choice('pg098-q1', 'a', t('a. popull dardan.', 'a. popull dardan.')) + choice('pg098-q1', 'b', t('b. populli më i vjetër në Ballkan.', 'b. populli më i vjetër në Ballkan.'), True) +
    choice('pg098-q1', 'c', t('c. popull sllav.', 'c. popull sllav.')) + '</fieldset>',
  lesson=L, practice=True, css=CSS)
section(rule(True),
  fill(t('2. Territori ku jetonin ilirët quhej', '2. Territori ku jetonin ilirët quhej'), blank('Si quhej territori ku jetonin ilirët?', 11, 'Iliri', 'Iliria'), '.'),
  fill(t('3. Cili ishte emri i Kosovës në lashtësi?', '3. Cili ishte emri i Kosovës në kohët e lashta?'), keyed(field('line', 'Emri i Kosovës në lashtësi'), 'Dardani', 'Dardania')),
  fill(t('4. Prejardhja e emrit dardan vjen nga fjala shqipe', '4. Emri dardan vjen nga fjala shqipe'), blank('Fjala shqipe nga vjen emri dardan', 11, 'dardhë', 'dardha'), '.'),
  practice=True, css=CSS)
section(rule(True),
  fill(t('5. Dardania në shek. I para erës sonë u pushtua nga Perandoria', '5. Në shekullin e parë para erës sonë, Dardaninë e pushtoi Perandoria'), blank('Perandoria që e pushtoi Dardaninë', 11, 'Romake'), '.'),
  fill(t('6. Në krye të Perandorisë Romake ishte', '6. Në krye të Perandorisë Romake ishte'), blank('Kush ishte në krye të Perandorisë Romake', 16, 'perandori', 'perandor', 'një perandor', 'perandori romak'), '.'),
  fill(t('7. Gjatë shekujve', '7. Gjatë shekujve'), blank('Shekulli i parë', 4, 'VI', '6'), t('dhe'), blank('Shekulli i dytë', 4, 'VII', '7') + ',',
       t('në Dardani u vendosën fiset', 'në Dardani u vendosën fiset'), blank('Fiset që u vendosën në Dardani'),
       t('e më vonë erdhën fiset sllave, si:', 'Më vonë erdhën fiset sllave, si:'),
       blank('Fisi sllav 1', 8, *SLAVS) + ',', blank('Fisi sllav 2', 8, *SLAVS) + ',', blank('Fisi sllav 3', 8, *SLAVS), t('dhe'), blank('Fisi sllav 4', 8, *SLAVS), '.'),
  practice=True, css=CSS)
section(rule(True),
  fill(t('8. Arsyet pse popujt e tjerë e pushtonin Dardaninë ishin:', '8. Pse e pushtonin popujt e tjerë Dardaninë?\nArsyet ishin:'),
       '<div class="p2-numbered">' + ''.join(f'<b aria-hidden="true">{n}.</b>' + open_answer(field('line', f'Arsyeja {n}')) for n in ('a', 'b')) + '</div>'),
  fill(t('9. Shkruaj kur u zhvillua dhe çfarë di për Betejën e Kosovës.', '9. Shkruaj kur u zhvillua Beteja e Kosovës.\nShkruaj çfarë di për të.'),
       open_answer(field('lined', 'Kur u zhvillua dhe çfarë di për Betejën e Kosovës', rows=4))),
  fill(t('10. Kur u mbajt Lidhja e Prizrenit?', '10. Kur u mbajt Lidhja e Prizrenit?'),
       blank('Kur u mbajt Lidhja e Prizrenit', 16, '10 qershor 1878', 'më 10 qershor 1878', 'më 10 qershor të vitit 1878', '10 qershor të vitit 1878',
             'në vitin 1878', 'më 1878', 'viti 1878', '1878', '10.06.1878', '10.6.1878')),
  practice=True, css=CSS)
