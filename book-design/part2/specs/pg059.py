# PDF page 59 — continuation of "Ndërmjetësimi mes bashkëmoshatarëve": Thello dijet and the 5 steps.
L = 'Ndërmjetësimi mes bashkëmoshatarëve'
CSS = '''#content.book.p2 .p59-steps{display:grid;gap:16px;margin:0}
#content.book.p2 .p59-step{display:grid;grid-template-columns:64px minmax(0,1fr);gap:16px;align-items:start;margin:0;padding:18px 20px;border:2px solid #c8b4d9;border-radius:16px;background:#ece2f3}
#content.book.p2 .p59-num{display:block;width:64px;height:64px;border:6px solid #9b73b7;border-radius:50%;background:#fff;text-align:center;font:700 30px/52px var(--book-heading);color:var(--book-ink)}
#content.book.p2 .p59-step h3{margin:0 0 8px;font:600 22px/1.4 var(--book-heading);color:var(--book-ink)}
#content.book.p2 .p59-step ul{margin:0;padding:0;list-style:none}
#content.book.p2 .p59-step li{position:relative;margin:0 0 6px;padding-left:1.1em;font:400 22px/1.5 var(--book-heading);color:var(--book-ink)}
#content.book.p2 .p59-step li::before{content:"•";position:absolute;left:0}
@media(max-width:700px){#content.book.p2 .p59-step{grid-template-columns:minmax(0,1fr);padding:16px}#content.book.p2 .p59-step h3,#content.book.p2 .p59-step li{font-size:20px}#content.book.p2 .p59-num{width:52px;height:52px;line-height:40px;font-size:24px}}
'''
section(rule(), heading('deepen', 'Thello dijet'),
  text(para(
    ('Ndërmjetësimi është një mënyrë për të ndihmuar njerëzit që nuk po merren vesh.', 'Ndërmjetësimi i ndihmon njerëzit që nuk merren vesh.'),
    ('Një person i tretë ndihmon ata që janë në mosmarrëveshje që të flasin dhe të gjejnë zgjidhje.',
     'Një person i tretë i ndihmon ata të flasin.\nAi i ndihmon të gjejnë një zgjidhje.'),
    ('Qëllimi i ndërmjetësimit mes bashkëmoshatarëve është që konfliktet të zgjidhen çdoherë përmes bisedës.',
     'Qëllimi është që konfliktet mes bashkëmoshatarëve të zgjidhen gjithmonë me bisedë.'),
    ('Pra, personi i tretë që përfshihet në një konflikt si ndërmjetësues nuk mban anën e asnjërit dhe, kështu, ndihmon në zgjidhjen e konfliktit.',
     'Ndërmjetësuesi nuk mban anën e askujt.\nKështu ai ndihmon që konflikti të zgjidhet.'),
    ('Në shkollë, nxënësit dhe mësuesit veprojnë si ndërmjetësues për të zgjidhur konfliktet mes palëve të përfshira.',
     'Në shkollë, nxënësit dhe mësuesit mund të jenë ndërmjetësues.\nAta ndihmojnë për të zgjidhur konfliktet.'),
    ('Ndërmjetësimi është vlerë për të jetuar në paqe.', 'Ndërmjetësimi na ndihmon të jetojmë në paqe.'))),
  lesson=L)
STEPS = [
 ('Hapi 1: Prezantimi dhe mbajtja e seancës', [
   ('Dëshiroju mirëseardhje palëve të përfshira në konflikt;', 'Uroju mirëseardhje palëve në konflikt.'),
   ('Bëji palët të ndihen rehat;', 'Bëji palët të ndihen rehat.'),
   ('Krijo atmosferë pozitive;', 'Krijo atmosferë të mirë.'),
   ('Trego mirësi;', 'Trego mirësi.'),
   ('Ofro qartësi dhe besim në procesin e ndërmjetësimit.', 'Shpjego qartë ndërmjetësimin.\nBëji palët të kenë besim.')]),
 ('Hapi 2: Dëgjimi i historive', [
   ('Mblidh sa më shumë informacion për faktet që nevojiten, të kuptosh mirë se çfarë ka ndodhur në konflikt (kur?, ku?, kush?, çfarë?, si?);',
    'Mblidh sa më shumë informacion.\nKupto mirë çfarë ka ndodhur: kur, ku, kush, çfarë dhe si.'),
   ('Bëji palët të ndihen se po i dëgjon dhe po i mirëkupton.', 'Tregoju palëve se po i dëgjon dhe po i kupton.')]),
 ('Hapi 3: Nxjerrja e vlerave, e kuptimit dhe e nevojave', [
   ('Ndihmoje secilën palë të mendojë çfarë është e rëndësishme për të në këtë konflikt.', 'Ndihmoje secilën palë të mendojë çfarë është e rëndësishme për të.'),
   ('Ndihmoji të kuptojnë pse ky rast ka rëndësi për ta.', 'Ndihmoji të kuptojnë pse ky rast ka rëndësi për ta.'),
   ('Kupto çfarë duan dhe për çfarë kanë më shumë nevojë.', 'Kupto çfarë duan dhe për çfarë kanë më shumë nevojë.'),
   ('Ndihmoji të flasin hapur me njëri-tjetrin për ndjenjat dhe nevojat e tyre.', 'Ndihmoji të flasin hapur për ndjenjat dhe nevojat e tyre.')]),
 ('Hapi 4: Gjetja dhe testimi i mundësive bashkërisht', [
   ('Kërkoni nga palët të mendojnë për zgjidhje që i marrin parasysh ndjenjat dhe nevojat e të dyja palëve.',
    'Kërkoni nga palët të mendojnë për zgjidhje.\nZgjidhja duhet të jetë e mirë për të dyja palët.'),
   ('Pyesni nëse palët pajtohen me zgjidhjen që ju e propozoni si ndërmjetësues.', 'Pyesni palët nëse pajtohen me zgjidhjen që propozoni ju.')]),
 ('Hapi 5: Arritja e marrëveshjes', [
   ('Shpjegoni qartë secilën zgjidhje për të cilën pajtohen palët: çfarë do të thotë, kush do ta zbatojë dhe deri kur duhet të kryhet.',
    'Shpjegoni qartë çdo zgjidhje:\nçfarë do të thotë, kush do ta bëjë dhe deri kur.'),
   ('Kujdes: punët dhe përgjegjësitë mund t’u caktohen vetëm atyre që janë të pranishëm në bisedë.',
    'Kujdes: punët mund t’u jepen vetëm atyre që janë në bisedë.'),
   ('Nëse palët duan marrëveshje me shkrim, përdorni një model të thjeshtë për ta shkruar atë.',
    'Nëse palët duan marrëveshje me shkrim, shkruajeni me një model të thjeshtë.')])]
section(rule(),
  text(para(('Procesi i ndërmjetësimit kalon në 5 hapa konkretë:', 'Ndërmjetësimi ka 5 hapa:'))),
  '<div class="p59-steps">' + ''.join(
     f'<div class="p59-step"><b class="p59-num" aria-hidden="true">{n}</b><div>' + T(h, tag='h3')[0] +
     '<ul>' + ''.join(T(a, b, tag='li')[0] for a, b in lis) + '</ul></div></div>' for n, (h, lis) in enumerate(STEPS, 1)) + '</div>',
  css=CSS)
