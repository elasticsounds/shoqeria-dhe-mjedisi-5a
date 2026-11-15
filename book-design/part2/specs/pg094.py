# PDF page 94 — Provoje veten (reading + multiple choice as a reader activity: Submit button, sounds, result popup).
# Keys: q1 a (text on this page), q2 c (page 93: about 90%), q3 c (see the note at the question).
L = 'Provoje veten'
CSS = '''#content.book.p2 .p2-choice{display:block;margin:0 0 8px;padding:10px 14px;border:2px solid #cdb8dc;border-radius:12px;background:#fff;font:400 20px/1.4 var(--book-heading);color:var(--book-ink);cursor:pointer}
#content.book.p2 .p2-choice input{width:22px;height:22px;margin:0 10px 0 0;vertical-align:-4px;accent-color:#794282}
#content.book.p2 .p2-choice:has(input:checked){border-color:#794282;background:#f3ecf8}
#content.book.p2 .p2-choice:has(input:focus-visible){outline:3px solid #075a70;outline-offset:2px}
#content.book.p2 .p2-q{margin:20px 0 10px;font:600 20px/1.4 var(--book-heading)}
#content.book.p2 .p2-group{margin:0 0 8px;padding:0;border:0}
#content.book.p2 .p2-group .chk-fb{margin:4px 0 16px}
'''
def group(name, q, easy, opts, key):
    out = f'<fieldset class="p2-group"><legend class="p2-q">{t(q, easy)}</legend>'
    for v, o in opts: out += choice(name, v, t(o, o), v == key)
    return out + '</fieldset>'
section(title('Provoje veten', practice=True),
  task('1.', ('Lexoje tekstin e mëposhtëm për t’i gjetur përgjigjet e sakta të pyetjeve në pyetësorin e mëposhtëm.',
              'Lexoje tekstin më poshtë.\nPastaj gjej përgjigjet e sakta në pyetësor.'),
       body=text(para(
         ('Popullsia e Kosovës, gjatë 100 viteve të fundit (1921-2021), ka ndryshuar shumë; ajo është rritur për rreth 4.5 herë.',
          'Popullsia e Kosovës ka ndryshuar shumë gjatë 100 viteve të fundit (1921-2021).\nAjo është rritur rreth 4.5 herë.'),
         ('Ndërsa, numri i popullsisë që jeton sot në Kosovë, sipas të dhënave të vitit 2024 nga Agjencia e Statistikave e Kosovës, është rreth 1.6 milionë banorë.',
          'Sot në Kosovë jetojnë rreth 1.6 milionë banorë.\nKëto të dhëna janë të vitit 2024, nga Agjencia e Statistikave e Kosovës.')))),
  lesson=L, practice=True)
section(rule(True),
  task('2.', 'Rrethoni përgjigjen e saktë.',
       body=group('pg094-q1', 'Sa është numri i banorëve që jetojnë sot në Kosovë?', 'Sa banorë jetojnë sot në Kosovë?',
                  (('a', 'a) Rreth 1.6 milionë;'), ('b', 'b) Rreth 1.7 milionë;'), ('c', 'c) Rreth 1.8 milionë.')), 'a') +
            group('pg094-q2', 'Sa për qind e popullsisë së Kosovës përbëhet nga komuniteti etnik shqiptar?', 'Sa për qind e popullsisë së Kosovës janë shqiptarë?',
                  (('a', 'a) Rreth 60 %;'), ('b', 'b) Rreth 70 %;'), ('c', 'c) Rreth 90 %.')), 'c') +
            # The printed options are 66, 70 and 76 years, none of which fits the lesson ("rreth 80 vjet"). Owner's decision
            # (2026-11-15): option c is 78 years and is the correct answer.
            group('pg094-q3', 'Sa është jetëgjatësia mesatare e popullsisë në Kosovë?', 'Sa vjet jetojnë mesatarisht njerëzit në Kosovë?',
                  (('a', 'a) 66 vjet;'), ('b', 'b) 70 vjet;'), ('c', 'c) 78 vjet.')), 'c')),
  practice=True, css=CSS)
