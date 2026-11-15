# PDF page 69 — Provoje veten: word search (8 directions) + sentences. Reader custom activity (Submit, sounds, confetti).
L = 'Provoje veten'
GRID = ['A I R O R U K O R P', 'V R I M T I N A D O', 'O O L Gj N I B C U L', 'K Z S Y P O M S P I', 'A R F K E X Z I A C',
        'T K J A C Q E R M I', 'I N Y T H B N C O A', 'S I T A B C V Z N O', 'P R O K U R O R I A']
WORDS = ['avokati', 'prokuroria', 'gjykata', 'policia']   # answer key: col 1 down, row 9 (also row 1 backwards), col 4 down from Gj, col 10 down
grid = ('<table class="ws-grid" aria-label="Tabela e shkronjave: 9 rreshta dhe 10 kolona"><tbody>' +
        ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r.split()) + '</tr>' for r in GRID) + '</tbody></table>')
# interactive word search: book-design/wordsearch.js (choose first and last letter; mouse, touch or keyboard)
game = ('<div class="ws" data-wordsearch data-words="' + ','.join(WORDS) + '" data-store="pg069.wordsearch" data-page-script="./book-design/wordsearch.js">' +
        '<p class="ws-help">' + t('Zgjidh shkronjën e parë të fjalës dhe pastaj shkronjën e fundit.', 'Shtyp shkronjën e parë të fjalës.\nPastaj shtyp shkronjën e fundit.') + ' ' +
        t('Me tastierë, lëviz me shigjeta dhe shtyp Enter.', 'Me tastierë: lëviz me shigjeta.\nShtyp Enter për të zgjedhur.') + '</p>' + grid +
        '<p class="ws-status" role="status" aria-live="polite"></p>' +
        '<h3 class="ws-words-title" id="p69-found">' + t('Fjalët që duhen gjetur') + '</h3><ul class="ws-words" aria-labelledby="p69-found">' +
        ''.join(f'<li data-word="{w}"><span class="ws-mark" aria-hidden="true"></span>{w}<span class="ws-state"></span></li>' for w in WORDS) + '</ul>' +
        '<div class="ws-tools"><button type="button" class="ws-clear">Pastro zgjedhjen</button><button type="button" class="ws-reset">Fillo nga e para</button></div></div>')
section(title('Provoje veten', practice=True),
  task('1.', ('Gjej në tetëkahore emrat e institucioneve që të mbrojnë.', 'Gjej në tabelën me shkronja emrat e institucioneve që të mbrojnë.'),
       ('Ngjyrosi katrorët me ngjyra të ndryshme, sipas fjalëve të gjetura, dhe shkruaj nga një fjali për to.',
        'Gjej fjalët në tabelë.\nPastaj shkruaj nga një fjali për secilën fjalë.'),
       body='<p class="p69-words">' + t('Avokati, prokuroria, gjykata, policia.') + '</p>' + game +
            '<p class="ws-write">' + t('Shkruaj nga një fjali për secilën fjalë.') + '</p>' +
            field('lined', 'Shkruaj nga një fjali për secilën fjalë të gjetur: avokati, prokuroria, gjykata, policia.', rows=4)),
  lesson=L, practice=True, stype='activity_custom',   # the reader shows its Submit button; wordsearch.js registers the check
  css="""#content.book.p2 .p69-words{margin:0 0 8px;font:600 22px/1.5 var(--book-heading)}
#content.book.p2 .ws{--wc:#cde9d6;--wb:#1e6b3a;margin:0 0 20px}
#content.book.p2 .ws-help,#content.book.p2 .ws-write{margin:0 0 12px;font:400 20px/1.5 var(--book-heading);color:var(--book-ink)}
#content.book.p2 .ws-write{font-weight:600}
#content.book.p2 .ws-grid{width:min(100%,600px);margin:0 auto;table-layout:fixed;border-collapse:collapse;background:#fff}
#content.book.p2 .ws-grid td{padding:0;border:2px solid var(--book-ink);text-align:center;font:600 22px/1 var(--book-heading);color:var(--book-ink);height:48px}
#content.book.p2 .ws-live .ws-grid td{height:auto}
#content.book.p2 .ws-cell{display:block;width:100%;aspect-ratio:1/1;padding:0;border:0;border-radius:0;background:#fff;color:var(--book-ink);font:600 22px/1 var(--book-heading);cursor:pointer;touch-action:manipulation}
#content.book.p2 .ws-cell:hover{background:#f3ecf8}
#content.book.p2 .ws-cell:focus-visible{position:relative;z-index:1;outline:4px solid #075a70;outline-offset:-4px}
#content.book.p2 .ws-cell.is-found{font-weight:700;box-shadow:inset 0 0 0 3px var(--wb)}
#content.book.p2 .ws-cell.is-found{background:var(--wc)}
#content.book.p2 .ws-cell.is-current{background:#ffc23d;box-shadow:inset 0 0 0 3px #5c3d00}
#content.book.p2 .ws-cell.is-start{box-shadow:inset 0 0 0 5px #5c3d00}
#content.book.p2 .ws-status{min-height:60px;margin:12px 0 4px;font:600 20px/1.5 var(--book-heading);color:var(--book-ink);text-align:center}
#content.book.p2 .ws-words-title{margin:0 0 8px;font:600 20px/1.5 var(--book-heading);color:var(--book-ink)}
#content.book.p2 .ws-words{list-style:none;margin:0 0 16px;padding:0}
#content.book.p2 .ws-words li{display:inline-block;margin:0 8px 8px 0;padding:6px 16px;border:2px solid #6b6b6b;border-radius:999px;background:#fff;font:400 20px/1.5 var(--book-heading);color:var(--book-ink)}
#content.book.p2 .ws-words li.is-found{border-color:var(--wb);background:var(--wc);font-weight:600}
#content.book.p2 .ws-words li.is-found .ws-mark::before{content:"✓ "}
#content.book.p2 .ws-tools button{min-height:48px;margin:0 8px 8px 0;padding:8px 18px;border:2px solid var(--book-purple-ink);border-radius:999px;background:#fff;color:var(--book-purple-ink);font:600 20px/1.3 var(--book-heading);cursor:pointer}
#content.book.p2 .ws-tools button:hover{background:#f3ecf8}
#content.book.p2 .ws-tools button:focus-visible{outline:3px solid #075a70;outline-offset:2px}
#content.book.p2 .ws:not(.ws-live) :is(.ws-help,.ws-status,.ws-words-title,.ws-words,.ws-tools){display:none}
@media(max-width:700px){#content.book.p2 .ws-grid td,#content.book.p2 .ws-cell{font-size:20px}#content.book.p2 .p69-words{font-size:20px}}
.ws-toasts{position:fixed;top:16px;left:50%;transform:translateX(-50%);z-index:300;width:min(92vw,30rem)}
.ws-toast{position:relative;display:flex;align-items:center;gap:12px;padding:12px 16px;border-left:4px solid #16a34a;border-radius:8px;background:#dcfce7;box-shadow:0 10px 15px -3px rgba(0,0,0,.2);font-family:BookPoppins,Poppins,sans-serif}
.ws-toast.is-warn{border-left-color:#ca8a04;background:#fef9c3}
.ws-toast span{font-size:28px;line-height:1}.ws-toast p{flex:1;margin:0;font:500 20px/1.4 BookPoppins,Arial,sans-serif;color:#1f2937}
.ws-toast button{position:absolute;top:-10px;right:-10px;width:32px;height:32px;border:1px solid #6b7280;border-radius:999px;background:#fff;color:#374151;font-size:20px;line-height:1;cursor:pointer}
.ws-toast button:focus-visible{outline:3px solid #075a70;outline-offset:2px}
@media(forced-colors:active){#content.book.p2 .ws-cell.is-found{outline:3px solid Highlight;outline-offset:-3px}#content.book.p2 .ws-cell.is-current{outline:3px dashed Highlight;outline-offset:-3px}}
""")
