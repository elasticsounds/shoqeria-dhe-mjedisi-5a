# PDF page 66 — Provoje veten (one task per section).
L = 'Provoje veten'
LETTERS = ['a', 'b', 'c', 'ç', 'd', 'dh', 'e', 'ë', 'f', 'g']
section(title('Provoje veten', practice=True),
  task('1.',
       ('Imagjinoni një situatë ku një shok juaji ndodhet rastësisht në një anije kozmike dhe ju mund t’i dërgoni dhjetë gjëra për të jetuar normalisht.',
        'Imagjinoni këtë situatë:\nNjë shok juaji ndodhet rastësisht në një anije kozmike.\nJu mund t’i dërgoni dhjetë gjëra që të jetojë normalisht.'),
       ('Bëni një listë me gjërat që do t’ia dërgonit.', 'Bëni një listë me gjërat që do t’ia dërgonit.'),
       ('Diskutoni me njëri-tjetrin në klasë nëse keni planifikuar gjëra të njëjta.', 'Diskutoni në klasë: a keni zgjedhur gjëra të njëjta?'),
       ('Pse?', 'Pse?'),
       body='<div class="p66-list">' + ''.join(
           f'<div class="p2-numbered"><b aria-hidden="true">{l}.</b>' + field('line', f'Gjëja {l}') + '</div>' for l in LETTERS) + '</div>'),
  lesson=L, practice=True,
  css='#content.book.p2 .p66-list{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px 24px}\n'
      '@media(max-width:700px){#content.book.p2 .p66-list{grid-template-columns:minmax(0,1fr)}}\n')

def _row(n, right=None, resp=None):
    a = t(right, right, tag='p', cls='p66-given') if right else field('area', f'E drejta {n}', rows=2)
    b = t(resp, resp, tag='p', cls='p66-given') if resp else field('area', f'Përgjegjësia për të drejtën {n}', rows=2)
    return f'<div class="p66-row"><b aria-hidden="true">{n}.</b><div class="p66-cell"><span class="p66-lab" aria-hidden="true">E drejta</span>{a}</div><div class="p66-cell"><span class="p66-lab" aria-hidden="true">Përgjegjësia</span>{b}</div></div>'

section(rule(True),
  task('2.', ('Çdo e drejtë ka përgjegjësinë e saj.', 'Çdo e drejtë ka edhe një përgjegjësi.'),
       ('Plotësoje tabelën me disa të drejta dhe përgjegjësitë përkatëse.', 'Plotësoje tabelën.\nShkruaj disa të drejta dhe përgjegjësitë e tyre.'),
       body='<div class="p66-table"><div class="p66-row p66-head"><b>' + t('Nr.') + '</b><div class="p66-cell">' + t('E drejta', tag='p', cls='p66-h') +
            '</div><div class="p66-cell">' + t('Përgjegjësia', tag='p', cls='p66-h') + '</div></div>' +
            _row(1, 'E drejta për ta shprehur mendimin.', 'Përgjegjësia për të mos i fyer të tjerët.') +
            _row(2, 'E drejta për t’u arsimuar.', 'Përgjegjësia për të mësuar.') + _row(3) + _row(4) + _row(5) + '</div>'),
  practice=True,
  css='#content.book.p2 .p66-table{border:2px solid var(--book-purple-ink);border-radius:16px;overflow:hidden;background:#fff}\n'
      '#content.book.p2 .p66-row{display:grid;grid-template-columns:56px minmax(0,1fr) minmax(0,1fr);gap:12px;align-items:center;padding:12px 16px;border-top:1px solid #e4d9ec}\n'
      '#content.book.p2 .p66-row>b{font:600 20px/1.3 var(--book-heading)}\n'
      '#content.book.p2 .p66-head{border-top:0;background:var(--book-purple-ink);color:#fff}\n'
      '#content.book.p2 .p66-head b span,#content.book.p2 .p66-h{margin:0;font:600 20px/1.3 var(--book-heading);color:#fff}\n'
      '#content.book.p2 .p66-given{margin:0;font:400 20px/1.4 var(--book-heading)}\n'
      '#content.book.p2 .p66-lab{display:none;font:600 20px/1.3 var(--book-heading);margin-bottom:4px}\n'
      '#content.book.p2 .p66-cell textarea.prx-field{min-height:64px}\n'
      '@media(max-width:700px){#content.book.p2 .p66-head{display:none}#content.book.p2 .p66-row{grid-template-columns:minmax(0,1fr)}#content.book.p2 .p66-lab{display:block}}\n')

STATEMENTS = ['Unë respektoj prindërit e mi.', 'Unë gjithmonë i kryej me rregull detyrat e shtëpisë.',
              'Në shtëpi punojmë të gjithë së bashku.', 'Unë gjithmonë respektoj rregullat e lojës.']
def _rate(k, s):
    P.fn += 1; base = P.fn
    opts = ''.join(f'<label class="p66-box"><input type="radio" name="vetevleresim-{k}" id="item-{base}-{n}" data-activity-item="item-{base}-{n}" value="{n}" aria-label="{s} {n} nga 5"><span aria-hidden="true">{n}</span></label>' for n in range(1, 6))
    return f'<div class="p66-rate"><p class="p66-given">{t(s, s)}</p><div class="p66-boxes" role="radiogroup" aria-label="{s}">{opts}</div></div>'

section(rule(True),
  task('3.', ('Vetëvlerësim!', 'Vlerëso veten!'),
       ('Zgjidh një ngjyrë dhe ngjyros sa më shumë katrorë, numri i të cilëve tregon më së miri se sa je ne gjendje të kryesh përgjegjësitë në jetën e përditshme.',
        'Zgjidh sa katrorë do të ngjyrosësh, nga 1 deri në 5.\nMë shumë katrorë do të thotë: i kryej më mirë përgjegjësitë e mia çdo ditë.'),
       body=''.join(_rate(k, s) for k, s in enumerate(STATEMENTS, 1))),
  practice=True,
  css='#content.book.p2 .p66-given{margin:0;font:400 20px/1.4 var(--book-heading)}\n'
      '#content.book.p2 .p66-rate{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:12px 20px;align-items:center;padding:12px 0;border-top:1px solid #e4d9ec}\n'
      '#content.book.p2 .p66-rate:first-child{border-top:0}\n'
      '#content.book.p2 .p66-boxes{display:grid;grid-template-columns:repeat(5,48px);gap:6px}\n'
      '#content.book.p2 .p66-box{position:relative;display:block;width:48px;height:48px;margin:0;border:2px solid #f0a020;border-radius:8px;background:#fff;cursor:pointer;font-size:20px}\n'
      '#content.book.p2 .p66-box input{position:absolute;inset:0;width:100%;height:100%;min-height:0;margin:0;opacity:0;cursor:pointer}\n'
      '#content.book.p2 .p66-box span{display:block;font:600 20px/44px var(--book-heading);text-align:center;color:#4a4550}\n'
      '#content.book.p2 .p66-box:is(:has(input:checked),:has(~ .p66-box input:checked)){background:#ffb149}\n'
      '#content.book.p2 .p66-box:is(:has(input:checked),:has(~ .p66-box input:checked)) span{color:#231f20}\n'
      '#content.book.p2 .p66-box:has(input:focus-visible){outline:3px solid #075a70;outline-offset:2px}\n'
      '@media(max-width:700px){#content.book.p2 .p66-rate{grid-template-columns:minmax(0,1fr)}}\n')
