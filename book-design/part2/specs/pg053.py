# PDF page 53 — lesson start: "Ne na bashkon toleranca".
L = 'Ne na bashkon toleranca'
section(title(L), keywords('tolerancë, mirëkuptim, dashuri, respekt, bashkëpunim.'),
  panel('thought', 'Shpreh mendimin tënd', items('Trego ku e ke dëgjuar fjalën tolerancë.')),
  media('pg053_im001.png', 'Një djalë me syze rri ulur me një libër të hapur dhe ngre gishtin lart; pranë tij janë një çantë shkolle dhe disa libra.',
        body='<div class="p2-says">' + para(('Çfarë është toleranca?', 'Çfarë është toleranca?')) +
             para(('Shpesh i dëgjoj njerëzit që flasin për tolerancën.', 'Shpesh dëgjoj që njerëzit flasin për tolerancën.')) +
             para(('A është aq e rëndësishme?', 'A është toleranca aq e rëndësishme?')) + '</div>'),
  lesson=L, stype='text_and_images')
section(rule(),
  text(para(('Nxënësit e klasës së pestë diskutuan për tolerancën.', 'Nxënësit e klasës së pestë folën për tolerancën.'),
            ('Tolerancë për mua do të thotë:', 'Për mua, tolerancë do të thotë:'))),
  '<div class="p2-cards" style="--cols:4">' + ''.join(f'<p class="p2-card">{t(s, s)}</p>' for s in (
      'I respektoj dhe i vlerësoj të tjerët.', 'I respektoj ata që janë ndryshe nga unë.', 'I pranoj njerëzit ashtu siç janë.', 'Pranoj mendimin ndryshe.')) + '</div>',
  figure('pg053_im002.png', 'Katër nxënës ulur në një tryezë lexojnë librat e tyre dhe mendojnë.'),
  css='@media(max-width:900px){#content.book.p2 .p2-cards{grid-template-columns:repeat(2,minmax(0,1fr))}}\n', stype='text_and_images')
