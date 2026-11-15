# PDF page 72 — Provoje veten (one task per section).
L = 'Provoje veten'
section(title('Provoje veten', practice=True),
  task('1.', ('Shkruaj tri cilësi që të bëjnë qytetar të përgjegjshëm:', 'Shkruaj tri cilësi të një qytetari të përgjegjshëm:'),
       body='<div class="p2-numbered">' + ''.join(f'<b aria-hidden="true">{l}.</b>' + field('line', f'Cilësia {l} e qytetarit të përgjegjshëm') for l in ('a', 'b', 'c')) + '</div>'),
  lesson=L, practice=True)
section(rule(True),
  task('2.', ('Lexo dhe vendos në kolonën përkatëse secilën nga përgjegjësitë që janë dhënë:', 'Lexo përgjegjësitë më poshtë.\nShkruaje secilën në kolonën e duhur:'),
       body='<p class="p72-list">' + t('kujdesem për lulet në shtëpi, ndihmoj për higjienën në lagje, kujdesem për gjyshen, ndihmoj vëllanë/motrën e vogël, ndihmoj fqinjët, ushqej macen në shtëpi, marr pjesë në krijimin e hapësirave gjelbëruese në shkollë, bëj blerjet në familje.',
            '- kujdesem për lulet në shtëpi\n- ndihmoj për pastërtinë në lagje\n- kujdesem për gjyshen\n- ndihmoj vëllanë ose motrën e vogël\n- ndihmoj fqinjët\n- ushqej macen në shtëpi\n- ndihmoj të krijohen hapësira të gjelbra në shkollë\n- bëj blerjet në familje') + '</p>' +
            '<div class="p2-cols">' + ''.join(
                f'<div class="p2-col"><label for="item-{P.fn + 1}">{t(h)}</label>{field("lined", "", rows=4)}</div>' for h in ('Përgjegjësi personale', 'Përgjegjësi qytetare')) + '</div>'),
  practice=True, css='#content.book.p2 .p72-list{margin:0 0 8px;padding:14px 18px;border-radius:12px;background:#fff8ea;font:400 20px/1.6 var(--book-heading)}\n')
section(rule(True),
  '<div class="prx-step"><p class="prx-instruction">' + t('3.') + ' ' +
  t('Organizoni një veprimtari për pastrimin e mjedisit në komunitetin tuaj dhe diskutoni në klasë për mënyrën e organizimit.',
    'Organizoni një veprimtari për të pastruar mjedisin në komunitetin tuaj.\nDiskutoni në klasë si do ta organizoni.') + '</p></div>',
  figure('pg072_im001.png', 'Katër fëmijë me doreza mbledhin mbeturina në një qese në një park.'),
  practice=True, stype='text_and_images')
