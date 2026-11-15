# PDF page 70 — lesson start: "Jam qytetar me të drejta dhe përgjegjësi".
L = 'Jam qytetar me të drejta dhe përgjegjësi'
def _duty(file, alt, label, letters, what):
    return ('<div class="b-lesson-media"><figure class="b-lesson-figure">' + img(file, alt) + '</figure><div class="p2-col"><p class="p2-flabel">' + t(label, label) + '</p>' +
            ''.join(f'<div class="p2-numbered"><b aria-hidden="true">{l}.</b>' + field('line', f'Detyra {l}: {what}') + '</div>' for l in letters) + '</div></div>')
section(title(L), keywords('qytetar aktiv, e drejtë, përgjegjësi, pjesëmarrje.'),
  panel('thought', 'Shpreh mendimin tënd', items(('Shkruaj dy detyra që duhet t’i përmbushësh për të qenë:', 'Shkruaj dy detyra që duhet t’i kryesh për të qenë:'))),
  _duty('pg070_im001.png', 'Nxënës ulur nëpër banka në një klasë me vizatime të varura në mur.', 'nxënës i përgjegjshëm në shkollë', ('a', 'b'), 'nxënës i përgjegjshëm në shkollë'),
  _duty('pg070_im002.png', 'Fëmijë dhe të rritur në një park lojërash me pemë përreth.', 'fëmijë i përgjegjshëm në komunitet.', ('c', 'ç'), 'fëmijë i përgjegjshëm në komunitet'),
  lesson=L, stype='text_and_images',
  css='#content.book.p2 .b-lesson-media{grid-template-columns:minmax(0,220px) minmax(0,1fr);align-items:center}\n'
      '#content.book.p2 .b-lesson-media input.prx-field{display:block;width:100%;min-height:52px;padding:10px 14px;border:2px solid #6d6472;border-radius:10px;background:#fff;font:400 20px/1.5 var(--book-heading);color:var(--book-ink)}\n'
      '@media(max-width:700px){#content.book.p2 .b-lesson-media{grid-template-columns:minmax(0,1fr)}#content.book.p2 .b-lesson-media img{max-width:220px}}\n')
section(rule(),
  text(para(
    ('Ndihem i sigurt kur mendoj se në vendin tim mbrohen të drejtat e fëmijëve.', 'Ndihem i sigurt, sepse vendi im i mbron të drejtat e fëmijëve.'),
    ('Një vend demokratik nuk i shkel asnjëherë të drejtat e qytetarëve të tij.', 'Një vend demokratik i respekton gjithmonë të drejtat e qytetarëve të tij.'),
    ('Detyra e institucioneve është t’i mbrojë fëmijët e qytetarët e vet.', 'Institucionet kanë për detyrë t’i mbrojnë fëmijët dhe qytetarët.'),
    ('Fëmijët duhet të flasin për rregullat që duan t’i ndryshojnë ose t’i përmirësojnë.', 'Fëmijët duhet të flasin për rregullat që duan t’i ndryshojnë ose t’i bëjnë më të mira.'),
    ('Kështu, ata ndihmojnë për ta bërë shoqërinë më të mirë në të ardhmen.', 'Kështu, ata ndihmojnë që shoqëria të bëhet më e mirë në të ardhmen.'))),
  figure('pg070_im003.png', 'Një familje e buzëqeshur, babai, vajza, djali dhe nëna, shtrirë pranë njëri-tjetrit në bar në një park.'),
  stype='text_and_images')
