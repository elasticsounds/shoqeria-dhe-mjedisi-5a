# PDF page 97 — Provoje veten (after "Veçoritë kulturore të popujve të Kosovës"). Question 2: several apply → multi-select reader activity (tick() in build.py).
L = 'Provoje veten'
CSS = '''#content.book.p2 .p2-choice{display:block;margin:0 0 8px;padding:10px 14px;border:2px solid #cdb8dc;border-radius:12px;background:#fff;font:400 20px/1.4 var(--book-heading);color:var(--book-ink);cursor:pointer}
#content.book.p2 .p2-choice input{width:22px;height:22px;margin:0 10px 0 0;vertical-align:-4px;accent-color:#794282}
#content.book.p2 .p2-choice:has(input:checked){border-color:#794282;background:#f3ecf8}
#content.book.p2 .p2-choice:has(input:focus-visible){outline:3px solid #075a70;outline-offset:2px}
'''
section(title('Provoje veten', practice=True),
  task('1.', 'Shkruaj tri elemente të kulturës në përgjithësi.',
       body='<div class="p2-numbered">' + ''.join(f'<b aria-hidden="true">{n}.</b>' + field('line', f'Elementi {n} i kulturës') for n in ('a', 'b', 'c')) + '</div>'),
  lesson=L, practice=True)
section(rule(True),
  task('2.', ('Cilat nga elementet e mëposhtme nuk janë pjesë e kulturës së popujve që banojnë në Kosovë?',
              'Cilat nga këto elemente nuk janë pjesë e kulturës së popujve që jetojnë në Kosovë?'),
       # key: everything except the lahuta (a traditional instrument) is NOT part of the culture — owner to confirm
       body=''.join(tick(t(o, o), ok) for o, ok in (('a) Bejsbolli;', True), ('b) Muzika hip-hop;', True), ('c) Sushi;', True), ('ç) Lahuta;', False), ('d) Gjuha angleze.', True)))),
  practice=True, css=CSS)
section(rule(True),
  task('3.', ('Cilët janë disa faktorë që përcaktojnë kulturën e një vendi?', 'Cilët janë disa faktorë që e formojnë kulturën e një vendi?'),
       body=field('lined', 'Cilët janë disa faktorë që përcaktojnë kulturën e një vendi?', rows=4)),
  task('4.', ('Shpjego me fjalët e tua se çfarë është “Besa” në kulturën kosovare.', 'Shpjego me fjalët e tua:\nçfarë është “Besa” në kulturën kosovare?'),
       body=field('lined', 'Shpjego me fjalët e tua se çfarë është “Besa” në kulturën kosovare.', rows=4)),
  practice=True)
