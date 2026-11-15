# PDF page 55 — Provoje veten (one question per section).
L = 'Provoje veten'
section(title('Provoje veten', practice=True),
  '<div class="prx-step"><p class="prx-instruction">' + t('1.') + ' ' + t('Lexo dhe puno sipas udhëzimeve.', 'Lexo dhe puno sipas udhëzimeve.') + '</p></div>',
  media('pg055_im001.png', 'Një mësues i buzëqeshur ndihmon një vajzë që shkruan; pranë tyre dy nxënës të tjerë punojnë me lapsa me ngjyra.',
    para(
      ('Situatë: Në klasën e Tanit dhe Dritës, nxënësit ishin ndarë në grupe dhe po diskutonin rreth muzikës.',
       'Situata:\nNë klasën e Tanit dhe të Dritës, nxënësit ishin ndarë në grupe.\nAta po flisnin për muzikën.'),
      ('Njëri grup thoshte se muzika klasike ishte muzika më e mirë, tjetri thoshte se muzikës hip-hop nuk i afrohej asnjë, ndërsa një grup tjetër ishte i mendimit se muzika popullore ishte muzika me vlerat më të mëdha.',
       'Një grup thoshte: muzika klasike është më e mira.\nNjë grup tjetër thoshte: muzika hip-hop është më e mira.\nGrupi i tretë thoshte: muzika popullore ka vlerat më të mëdha.'),
      ('Mësuesi kishte provuar të mbante rend të fjalës dhe qetësi, por më kot, nxënësit po i shprehnin mendimet e tyre përnjëherësh.',
       'Mësuesi u përpoq të mbante rregull dhe qetësi.\nPor nxënësit flisnin të gjithë njëherësh.'),
      ('Pastaj, mësuesi u tha: “Ju duhet të flisni me radhë, t’i jepni mendimet tuaja dhe t’i respektoni mendimet e të tjerëve.”',
       'Pastaj mësuesi u tha:\n“Flisni me radhë.\nJepni mendimet tuaja.\nRespektoni mendimet e të tjerëve.”'),
      ('Kështu, nxënësit morën një mësim të mirë: toleranca është shumë e rëndësishme për jetën në shoqëri.',
       'Kështu, nxënësit mësuan diçka të mirë:\ntoleranca është shumë e rëndësishme për jetën në shoqëri.')), reversed=True),
  '<h2 class="p2-subhead">' + t('Dritarja e tolerancës') + '</h2>',
  '<div class="p2-cols">' +
  ''.join(f'<div class="p2-col"><label for="item-{P.fn + 1}">{t(q, q)}</label>{field("lined", "", rows=4)}</div>' for q in (
      'Shkruaj për mungesën e tolerancës në situatën e dhënë.', 'Shkruaj disa fjali për tolerancën në situatën e dhënë.')) + '</div>',
  lesson=L, practice=True)
section(rule(True),
  task('2.', 'Shkruaj tri këshilla për një sjellje të mirë.',
       body='<div class="p2-numbered">' + ''.join(f'<b aria-hidden="true">{n}.</b>' + field('line', f'Këshilla {n} për një sjellje të mirë') for n in (1, 2, 3)) + '</div>'),
  practice=True)
section(rule(True),
  panel('research', None,
    '<p class="p2-step">' + t('Ndahuni në katër grupe.', 'Ndahuni në katër grupe.') + '</p>',
    '<p class="p2-step">' + t('Secili grup le të hulumtojë dhe të mbledhë materiale të ndryshme për tolerancën.', 'Secili grup hulumton dhe mbledh materiale për tolerancën.') + '</p>',
    '<p class="p2-step">' + t('(Grupet duhet të përgatitin nga një poster për tolerancën dhe ta vendosin në korridorët e shkollës).',
                             'Çdo grup përgatit një poster për tolerancën.\nVendoseni posterin në korridorin e shkollës.') + '</p>'),
  practice=True)
