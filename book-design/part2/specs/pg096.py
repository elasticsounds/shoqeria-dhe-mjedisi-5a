# PDF page 96 — continuation of "Veçoritë kulturore të popujve të Kosovës".
L = 'Veçoritë kulturore të popujve të Kosovës'
# six written questions: three per section, each with its own answer box
section(rule(), panel('questions', 'Pyetje për ty', questions(
    ('Përmend disa elemente që tregojnë përkatësinë kombëtare shqiptare të kulturës në Kosovë.', 'Përmend disa elemente që tregojnë se kultura në Kosovë është shqiptare.'),
    ('Cili aspekt i kulturës tregon prejardhjen ilire të shqiptarëve?', 'Cila pjesë e kulturës tregon se shqiptarët vijnë nga ilirët?'),
    ('Cilat janë disa veçori të hershme të shqiptarëve?', 'Cilat janë disa veçori të vjetra të shqiptarëve?'))), lesson=L)
section(rule(), panel('questions', 'Pyetje për ty', questions(
    'Ku vërehen më shumë elementet moderne?',
    'Cilat komunitete jetojnë në Kosovë?',
    ('Në cilat lokalitete janë të përqendruar ata?', 'Në cilat vende jetojnë më shumë ato?')), toc=False))
section(rule(),
  figure('pg096_im001.png', 'Ndërtesa e Bibliotekës Kombëtare të Kosovës, me shumë kube të bardha dhe e mbështjellë me rrjetë metalike, e rrethuar me gjelbërim.',
         caption='Biblioteka Kombëtare e Kosovës “Pjetër Bogdani”'),
  panel('research', None,
    '<p class="p2-step">' + t('Hulumto:', 'Hulumto:') + '</p>',
    '<p class="p2-step">' + t('Si festohen festat dhe cilat janë traditat në zonat e ndryshme të Kosovës?', 'Si festohen festat në zona të ndryshme të Kosovës?\nCilat janë traditat atje?') + '</p>'),
  panel('internet', None, '<p class="p2-step">' + t('Bashkë me ndihmën e prindërve ose të mësuesit, hulumto në internet dhe gjej informacione për kulturën e popujve që jetojnë në Kosovë.',
        'Hulumto në internet me ndihmën e prindërve ose të mësuesit.\nGjej informacione për kulturën e popujve që jetojnë në Kosovë.') + '</p>'),
  stype='text_and_images')
section(rule(), heading('deepen', 'Thello dijet'),
  text(para(
    ('Gjuha shqipe është pasardhëse e gjuhës së ilirëve.', 'Gjuha shqipe vjen nga gjuha e ilirëve.'),
    ('Sot, në institucione të ndryshme, në televizione, në gazeta etj., përdoret gjuha standarde shqipe, si në Kosovë, ashtu edhe në Shqipëri.',
     'Sot përdoret gjuha standarde shqipe në institucione, në televizione dhe në gazeta.\nAjo përdoret në Kosovë dhe në Shqipëri.'))))
