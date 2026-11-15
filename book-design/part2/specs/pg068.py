# PDF page 68 — continuation of "Institucionet që na mbrojnë".
L = 'Institucionet që na mbrojnë'
section(rule(), panel('questions', 'Pyetje për ty', questions(
    ('A dini ndonjë rast ku institucionet i marrin nën mbrojtje fëmijët?', 'A dini ndonjë rast kur institucionet i mbrojnë fëmijët?'),
    'Cilat janë disa nga institucionet që ju mbrojnë?',
    ('Si mendoni se ndihet një fëmijë i pambrojtur?', 'Si ndihet një fëmijë që nuk e mbron askush?'),
    ('Si ndihet një fëmijë nën mbrojtjen e ligjit?', 'Si ndihet një fëmijë që e mbron ligji?'))), lesson=L)
section(rule(), panel('research', None,
    '<p class="p2-step">' + t('Bashkë me ndihmën e prindërve apo të mësuesit, hulumto në internet për një nga institucionet për mbrojtjen tënde.',
                             'Hulumto në internet me ndihmën e prindërve ose të mësuesit.\nKërko për një institucion që të mbron ty.') + '</p>',
    '<p class="p2-step">' + t('Fol për ndihmën dhe mbështetjen që ky institucion të ofron.', 'Trego si të ndihmon dhe si të mbështet ky institucion.') + '</p>',
    '<p class="p2-step">' + t('Diskuto me shoqet dhe shokët e klasës për informacionet e gjetura.', 'Diskuto me shoqet dhe shokët e klasës për atë që gjete.') + '</p>'))
section(rule(), heading('deepen', 'Thello dijet'),
  text(
    para(('Organet e drejtësisë janë institucione që na mbrojnë dhe kujdesen për drejtësinë.', 'Organet e drejtësisë janë institucione.\nAto na mbrojnë dhe kujdesen për drejtësinë.'),
         ('Ato duhet të jenë njohëse të mira të ligjit, me qëllim që të japin gjykime të paanshme dhe të marrin vendime të drejta.',
          'Ato duhet ta njohin mirë ligjin.\nKështu gjykojnë pa mbajtur anë dhe marrin vendime të drejta.')),
    para(('Avokati i popullit shqyrton kërkesat dhe ankesat që vijnë nga njerëzit.', 'Avokati i popullit i shqyrton kërkesat dhe ankesat e njerëzve.'),
         ('Ai i këshillon dhe i ndihmon për të mbrojtur të drejtat e tyre.', 'Ai i këshillon njerëzit.\nAi i ndihmon t’i mbrojnë të drejtat e tyre.'),
         ('Po ashtu, i përfaqëson ata në gjykatë nëse dikujt i është bërë padrejtësi.', 'Ai i përfaqëson njerëzit në gjykatë kur dikujt i është bërë padrejtësi.')),
    para(('Gjyqtarët janë njohës dhe interpretues të ligjeve, të cilët marrin vendime në mbrojtje të të drejtave dhe lirive të njeriut.',
          'Gjyqtarët i njohin dhe i shpjegojnë ligjet.\nAta marrin vendime që mbrojnë të drejtat dhe liritë e njeriut.')),
    para(('Prokurori është përfaqësues i shtetit.', 'Prokurori përfaqëson shtetin.'),
         ('Ai thotë nëse dikush ka bërë një shkelje dhe përpiqet ta provojë këtë në gjykatë.', 'Ai thotë nëse dikush e ka shkelur ligjin.\nAi përpiqet ta provojë këtë në gjykatë.')),
    para(('Policia është organ i zbatimit të ligjit.', 'Policia kujdeset që ligji të zbatohet.'),
         ('Ajo parandalon veprime që rrezikojnë jetën e qytetarëve dhe merr masa për mbrojtjen e lirive dhe të drejtave të njeriut.',
          'Ajo ndalon veprimet që rrezikojnë jetën e qytetarëve.\nAjo mbron liritë dhe të drejtat e njeriut.')),
    para(('Instituti Kombëtar i Shëndetësisë Publike është institucioni më i lartë shëndetësor në Kosovë.', 'Instituti Kombëtar i Shëndetësisë Publike është institucioni më i lartë për shëndetin në Kosovë.'),
         ('Ai kujdeset për shëndetin e njerëzve dhe merr masa për ta mbrojtur jetën dhe mirëqenien e tyre.', 'Ai kujdeset për shëndetin e njerëzve.\nAi mbron jetën dhe mirëqenien e tyre.'))))
