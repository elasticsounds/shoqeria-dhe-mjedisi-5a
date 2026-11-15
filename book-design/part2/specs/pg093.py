# PDF page 93 — lesson start: "Ndryshimet në popullsinë e Kosovës".
L = 'Ndryshimet në popullsinë e Kosovës'
def prompt(q, easy, label, rows=3):
    return f'<div class="b-lesson-prompt"><label for="item-{P.fn + 1}">{t(q, easy)}</label>{field("lined", "", rows=rows)}</div>'
section(title(L), keywords('popullsi, etni, komunitet, histori.'),
  panel('thought', 'Shpreh mendimin tënd', items('Çfarë di për popullsinë e Kosovës?', 'Si ka ndryshuar ajo gjatë viteve?')),
  text(para(
    ('Popullsia e Kosovës ka ndryshuar përgjatë historisë.', 'Popullsia e Kosovës ka ndryshuar gjatë historisë.'),
    ('Aktualisht, ajo varet nga zhvillimi ekonomik, nataliteti dhe migrimi i popullsisë.',
     'Sot, popullsia varet nga tri gjëra:\n- zhvillimi ekonomik\n- numri i lindjeve\n- largimi i njerëzve nga vendi')),
   para(
    ('Për arsye të luftërave dhe kushtet e vështira për të jetuar, shumë kosovarë kanë migruar.',
     'Shumë kosovarë janë larguar nga vendi.\nArsyet ishin luftërat dhe jeta e vështirë.'),
    ('Ata largohen nga vendi për të siguruar kushte më të përshtatshme jetese.', 'Ata largohen që të jetojnë më mirë.'),
    ('Si rezultat i lindshmërisë së lartë dhe vdekshmërisë së ulët, Kosova ka popullsinë me moshën më të re në Evropë, mosha mesatare e së cilës është rreth 34 vjeçe.',
     'Në Kosovë lindin shumë fëmijë dhe vdesin pak njerëz.\nPrandaj Kosova ka popullsinë më të re në Evropë.\nMosha mesatare është rreth 34 vjeç.'),
    ('Popullsia kosovare ka një jetëgjatësi të lartë, mesatarisht rreth 80 vjet.', 'Njerëzit në Kosovë jetojnë gjatë, mesatarisht rreth 80 vjet.'))),
  figure('pg093_im001.png', 'Dy grafika për popullsinë e Kosovës: një hartë që tregon si ka ndryshuar numri i banorëve nëpër qytete dhe një grafikë me popullsinë rezidente në vitin 2021: 1,773,971 banorë, si dhe numrat për vitet 2016-2020.',
         caption='(Të dhënat sipas Agjencisë së Statistikave të Kosovës - ASK)'),
  lesson=L, stype='text_and_images')
section(rule(),
  panel('questions', 'Pyetje për ty',
    questions(('Çka ndikon për të pasur moshë mesatare të re të popullsisë?', 'Çfarë ndikon që popullsia të ketë moshë mesatare të re?')),
    prompt('A është përparësi që Kosova ka popullsinë më të re në Evropë? Argumento pse.',
           'A është përparësi që Kosova ka popullsinë më të re në Evropë?\nTrego pse.', ''),
    prompt('Jetëgjatësia mesatare në Kosovë është rreth 80 vjet. A mendon se në të ardhmen do të rritet? Pse?',
           'Njerëzit në Kosovë jetojnë mesatarisht rreth 80 vjet.\nA mendon se në të ardhmen do të jetojnë më gjatë?\nPse?', '')))
section(rule(),
  panel('internet', None, '<p class="p2-step">' + t('Bashkë me ndihmën e prindërve apo të mësuesit, hulumto në internet dhe gjej informacione ku tregohet se sa është rritur popullsia e Kosovës gjatë 30 viteve të fundit.',
        'Hulumto në internet me ndihmën e prindërve ose të mësuesit.\nGjej sa është rritur popullsia e Kosovës gjatë 30 viteve të fundit.') + '</p>'),
  heading('deepen', 'Thello dijet'),
  text(para(
    ('Agjencia e Statistikave të Kosovës vlerëson se shqiptarët sot përbëjnë rreth 90% të popullsisë.',
     'Agjencia e Statistikave të Kosovës thotë se rreth 90% e popullsisë sot janë shqiptarë.'),
    ('Komunitetet e tjera janë: serbët, pastaj turqit, boshnjakët, goranët, romët, ashkalinjtë, egjiptianët etj.',
     'Komunitetet e tjera janë:\n- serbët\n- turqit\n- boshnjakët\n- goranët\n- romët\n- ashkalinjtë\n- egjiptianët'))))
