# PDF page 63 — Provoje veten (one question per section). Task 1 is a V/G (true/false) table as the reader's
# true/false activity (Submit, sounds, popup). Key: rights 1, 2, 3 and 6 are true; 4 (discriminated) and 5 (exploited) are false.
L = 'Provoje veten'
CSS = '''#content.book.p2 table.p63-table{width:100%;border-collapse:separate;border-spacing:0;border:2px solid var(--book-purple-ink);border-radius:16px;overflow:hidden;background:#fff}
#content.book.p2 table.p63-table th,#content.book.p2 table.p63-table td{padding:12px 14px;border:0;border-top:1px solid #e4d9ec;font:400 20px/1.4 var(--book-heading);color:var(--book-ink);text-align:left;vertical-align:middle;background:transparent}
#content.book.p2 table.p63-table thead th{border-top:0;background:var(--book-purple-ink);color:#fff;font-weight:600}
#content.book.p2 table.p63-table :is(th,td).p63-c{width:96px;text-align:center}
#content.book.p2 .p63-opt{display:inline-flex;align-items:center;justify-content:center;min-height:44px;cursor:pointer}
#content.book.p2 table.p63-table td.p63-n{width:48px;font-weight:600}
#content.book.p2 table.p63-table input[type=radio]{width:32px;height:32px;min-width:32px;margin:0;accent-color:var(--book-purple-ink);cursor:pointer}
#content.book.p2 table.p63-table input[type=radio]:focus-visible{outline:3px solid #075a70;outline-offset:3px}
@media(max-width:700px){#content.book.p2 table.p63-table th,#content.book.p2 table.p63-table td{padding:10px 8px}#content.book.p2 table.p63-table :is(th,td).p63-c{width:70px}#content.book.p2 table.p63-table td.p63-n{width:34px}}
'''
ROWS = ['Të ketë kujdes shëndetësor', 'Të ketë të drejtën e arsimimit', 'Të trajtohet me dinjitet', 'Të diskriminohet', 'Të shfrytëzohet', 'Të argëtohet']
def row(n, s):
    # both radios of a row carry the row's item id; the reader compares the chosen value with window.correctAnswers[item]
    cells = ''.join(f'<td class="p63-c"><label class="p63-opt"><input type="radio" id="vg-{n}-{v.lower()}" data-activity-item="vg-{n}" name="p63-row-{n}" value="{v}" aria-label="{s}: {lab}">'
                    f'<span class="validation-mark hidden"></span></label></td>'
                    for v, lab in (('V', 'e vërtetë'), ('G', 'e gabuar')))
    return f'<tr><td class="p63-n">{n}.</td><td>{t(s, s)}</td>{cells}</tr>'
section(title('Provoje veten', practice=True),
  task('1.', ('Plotësoje tabelën me V (për e vërtetë) ose me G (për e gabuar).', 'Plotëso tabelën.\nZgjidh V për e vërtetë.\nZgjidh G për e gabuar.'),
       body='<table class="p63-table"><thead><tr><th scope="col">' + t('Nr.') + '</th><th scope="col">' +
            t('Të respektosh të drejtat e njeriut do të thotë që ai:') + '</th><th scope="col" class="p63-c">' + t('V') +
            '</th><th scope="col" class="p63-c">' + t('G') + '</th></tr></thead><tbody>' +
            ''.join(row(n, s) for n, s in enumerate(ROWS, 1)) + '</tbody></table>'),
  lesson=L, practice=True, css=CSS, stype='activity_true_false', answers={f'vg-{n}': v for n, v in enumerate('VVVGGV', 1)})
section(rule(True),
  task('2.', 'Shkruaj tri fjali për të treguar se në klasë respektohen të drejtat tona.',
       body=field('lined', 'Shkruaj tri fjali për të treguar se në klasë respektohen të drejtat tona.', rows=5)), practice=True)
section(rule(True),
  task('3.', ('Krijo një fletëpalosje për ndërgjegjësimin e njerëzve për mbrojtjen e të drejtave të tyre.',
              'Krijo një fletëpalosje.\nFletëpalosja u tregon njerëzve si t’i mbrojnë të drejtat e tyre.'),
       body='<figure class="b-lesson-figure" style="max-width:420px">' + img('pg063_im001.png', 'Një fletëpalosje e zbrazët me tri pjesë.') + '</figure>'),
  practice=True)
