# PDF page 100 — Fjalorthi (the book's glossary page). One data-id per entry.
L = 'Fjalorthi'
CSS = '''#content.book.p2 .p2-gloss{margin:0;padding:0;list-style:none}
#content.book.p2 .p2-gloss li{margin:0 0 12px;padding:14px 18px;border-radius:14px;background:#ece2f3;border:2px solid #c8b4d9;font:400 22px/1.5 var(--book-heading);color:var(--book-ink)}
@media(max-width:700px){#content.book.p2 .p2-gloss li{font-size:20px}}
'''
E = ['Artefakt - një objekt i ndërtuar nga njeriu, i gjetur nga gërmimet arkeologjike.',
     'Blegtori - degë e ekonomisë që merret me rritjen e bagëtive.',
     'Boza - pije freskuese me bazë misrin.',
     'Bujqësi - degë e ekonomisë që përfshin punimin e tokës dhe rritjen e bimëve.',
     'Dardani - Kosova në kohën e Ilirisë.',
     'Infrastrukturë - sistem ndërtimesh të ndryshme (infrastruktura rrugore, infrastruktura e shkollës etj.).',
     'Kompromis - marrëveshje e cila është rezultat i lëshimeve që bëjnë palët e përfshira.',
     'NATO - Organizata e Traktatit Atlantik të Veriut.',
     'Qerpiç - tulla për ndërtimin e shtëpive, të bëra prej dheut.',
     'Religjion - fe, besim.',
     'Shajak - material i punuar nga leshi.',
     'Shoqëri demokratike - shoqëri ku të gjithë njerëzit janë të lirë dhe kanë të drejta të barabarta.',
     'UÇK - Ushtria Çlirimtare e Kosovës.',
     'Universale - që i përket gjithë botës.']
section(title(L), '<ul class="p2-gloss">' + ''.join(T(e, tag='li')[0] for e in E[:7]) + '</ul>', lesson=L, css=CSS)
section(rule(), '<ul class="p2-gloss">' + ''.join(T(e, tag='li')[0] for e in E[7:]) + '</ul>', css=CSS)
