# PDF page 58 — continuation of "Ndërmjetësimi mes bashkëmoshatarëve".
L = 'Ndërmjetësimi mes bashkëmoshatarëve'
TIP = '''#content.book.p2 .p58-tip{margin:0;padding:18px 22px;border-radius:16px;background:#794282;color:#fff;font:600 22px/1.5 var(--book-heading)}
@media(max-width:700px){#content.book.p2 .p58-tip{font-size:20px}}
'''
section(rule(),
  '<h2 class="p2-subhead" style="text-align:left">' + t('Transformimi i konfliktit:') + '</h2>',
  figure('pg058_im001.png', 'Katër skica me figura njerëzish: dy persona të ndarë në konflikt; një person i tretë ndërhyn mes tyre; dy personat afrohen dhe bisedojnë; në fund lidhen me një urë dhe bashkëpunojnë.'),
  panel('discussion', 'Diskuto', items(
    ('Analizoji fotografitë e sipërshënuara dhe trego se çfarë po vëren.', 'Shiko fotografitë më lart.\nTrego çfarë vëren.'),
    ('Prej fotografisë së parë kur personat janë në konflikt, pastaj si ndërhyn ndërmjetësuesi, si palët bashkëbisedojnë dhe në fund si bashkëpunojnë.',
     'Në fotografinë e parë, personat janë në konflikt.\nPastaj ndërhyn ndërmjetësuesi.\nMë pas palët bisedojnë.\nNë fund palët bashkëpunojnë.'))),
  lesson=L, stype='text_and_images')
section(rule(), panel('questions', 'Pyetje për ty', questions(
    'Trego një rast kur mund të kesh qenë ndërmjetësues.',
    ('Si je ndier kur dy persona janë pajtuar me ndihmën tënde?', 'Si je ndier kur dy persona u pajtuan me ndihmën tënde?'))),
  '<p class="p58-tip">' + t('Këshillë: Për të ndërmjetësuar një rast konflikti, duhet ta bëni me dëshirë, pra në mënyrë vullnetare.',
                           'Këshillë:\nNdërmjetësoni një konflikt vetëm kur e bëni me dëshirë.') + '</p>', css=TIP)
