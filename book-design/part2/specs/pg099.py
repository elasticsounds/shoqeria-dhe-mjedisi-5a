# PDF page 99 — Provoje veten: end-of-book test, questions 11–16 and the self-evaluation box.
L = 'Provoje veten'
CSS = '''#content.book.p2.prx input.prx-field.p2-blank{display:inline-block;width:var(--w,11em);max-width:100%;min-height:44px;margin:4px 2px;padding:4px 10px;vertical-align:middle}
#content.book.p2 .p2-fill{margin:0 0 28px;font:400 22px/2.2 var(--book-heading);color:var(--book-ink)}
#content.book.p2 .p2-fill .prx-lined{margin-top:6px}
#content.book.p2 .p2-eval{margin:0;padding:22px 26px;border:3px solid #3fae49;border-radius:18px;background:#fff}
#content.book.p2 .p2-eval h2{margin:0 0 10px;font:600 22px/1.4 var(--book-heading);color:var(--book-ink)}
#content.book.p2 .p2-eval .p2-fill{margin:0}
@media(max-width:700px){#content.book.p2 .p2-fill{font-size:20px}}
'''
def blank(label, w=11, *answers):
    f = field('line', label).replace('class="prx-field"', f'class="prx-field p2-blank" style="--w:{w}em"')
    return keyed(f, *answers) if answers else open_answer(f)
def plain_blank(label, w=11):   # outside an activity (the self-evaluation box)
    return field('line', label).replace('class="prx-field"', f'class="prx-field p2-blank" style="--w:{w}em"')
def fill(*parts): return '<div class="p2-fill">' + ' '.join(parts) + '</div>'
# Answer keys from pages 88 and 95; the items of each list are accepted in any order.
LEADERS = ('Ymer Prizreni', 'Abdyl Frashëri', 'Sulejman Vokshi')
SERBS = ('Mitrovicën e Veriut', 'Mitrovica e Veriut', 'Mitrovicë', 'Mitrovicën', 'Graçanicë', 'Graçanica', 'Shtërpcë', 'Shtërpca')
GORANI = ('Opojë', 'Opoja', 'Dragash', 'Dragashi')
section(rule(True),
  fill(t('11. Qëllimi i Lidhjes së Prizrenit ishte', '11. Qëllimi i Lidhjes së Prizrenit ishte'), open_answer(field('lined', 'Qëllimi i Lidhjes së Prizrenit', rows=2))),
  fill(t('12. Lidhja e Prizrenit u drejtua nga :', '12. Kush e drejtoi Lidhjen e Prizrenit?'),
       blank('Drejtuesi i parë i Lidhjes së Prizrenit', 12, *LEADERS) + ',', blank('Drejtuesi i dytë i Lidhjes së Prizrenit', 12, *LEADERS), t('dhe'),
       blank('Drejtuesi i tretë i Lidhjes së Prizrenit', 12, *LEADERS)),
  fill(t('13. Ndryshimi i popullsisë së Kosovës përgjatë historisë varet nga:', '13. Nga se varet ndryshimi i popullsisë së Kosovës gjatë historisë?'),
       open_answer(field('line', 'Nga se varet ndryshimi i popullsisë së Kosovës'))),
  lesson=L, practice=True, css=CSS)
section(rule(True),
  fill(t('14. Cilat etni jetojnë në Kosovë?', '14. Cilat etni jetojnë në Kosovë?'), open_answer(field('lined', 'Cilat etni jetojnë në Kosovë', rows=2))),
  fill(t('15. Serbët në Kosovë jetojnë në', '15. Serbët në Kosovë jetojnë në'), blank('Vendi i parë ku jetojnë serbët', 10, *SERBS) + ',', blank('Vendi i dytë ku jetojnë serbët', 10, *SERBS) + ',',
       blank('Vendi i tretë ku jetojnë serbët', 10, *SERBS) + '.',
       t('Goranët jetojnë në', 'Goranët jetojnë në'), blank('Vendi i parë ku jetojnë goranët', 10, *GORANI), t('dhe'), blank('Vendi i dytë ku jetojnë goranët', 10, *GORANI) + ',',
       t('kurse turqit jetojnë në', 'Turqit jetojnë në'), blank('Vendi ku jetojnë turqit', 10, 'Prizren', 'Prizreni') + '.'),
  fill(t('16. Cili aspekt i kulturës tregon prejardhjen ilire të shqiptarëve?', '16. Cila pjesë e kulturës tregon se shqiptarët vijnë nga ilirët?'),
       open_answer(field('lined', 'Cili aspekt i kulturës tregon prejardhjen ilire të shqiptarëve', rows=2))),
  practice=True, css=CSS)
section(rule(True),
  '<div class="p2-eval"><h2>' + t('Vlerësimi:') + '</h2>' +
  fill(t('Ti ke arritur të përgjigjesh saktë në', 'Ti je përgjigjur saktë në'), plain_blank('Numri i pyetjeve ku je përgjigjur saktë', 4), t('pyetje.', 'pyetje.')) +
  '<p class="p2-fill">' + t('Diskuto me mësuesen/in për përgjigjet që ke dhënë.', 'Diskuto me mësuesen ose mësuesin për përgjigjet e tua.') + '</p></div>',
  practice=True, css=CSS)
