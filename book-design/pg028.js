/* Source page 28 word search. Found words are kept in this browser (localStorage).
   init() runs on load and again on 'adt:page-changed': the reader's dock swaps pages in place without re-running page scripts. */
(function(){
function init(){
  var rows=[['O','Xh','A','K','U','L','Q','O','D','A','D'],['C','X','V','P','K','J','E','H','G','L','Y'],['K','U','Ll','Ë','G','U','R','I','P','O','E'],['A','D','U','R','Y','R','P','I','Y','E','R'],['S','D','S','Dh','A','Z','I','X','B','N','M'],['O','O','R','E','D','G','Ç','A','T','I','H'],['Ll','B','Zh','S','Sh','T','Ë','P','I','K','J'],['E','O','M','E','M','O','D','E','R','N','E'],['A','R','K','I','T','E','K','T','U','R','Ë'],['T','R','A','D','I','C','I','O','N','A','L']];
  var words=['Kullë guri','përdhese','qerpiç','çati','arkitekturë','tradicional','oda','kasolle','oxhak','moderne'];
  var key='adt5a.pg028.wordsearch.v1', found={}, selected=[], cells=[], root=document.querySelector('.wordsearch28') || document.querySelector('[data-family="wordsearch"]');
  if(!root||root.dataset.wsReady)return;root.dataset.wsReady='1';
  var table=root.querySelector('table'), body=table.querySelector('tbody');
  if(!body.children.length){rows.forEach(function(row){var tr=document.createElement('tr');row.forEach(function(letter){var td=document.createElement('td');td.textContent=letter;tr.appendChild(td)});body.appendChild(tr)})}
  var list=root.querySelector('.word-list') || root.querySelector('[data-id="pg028_n0019"]');
  list.textContent=''; words.forEach(function(w,i){var span=document.createElement('span');span.textContent=w;span.dataset.word=w;list.appendChild(span);list.appendChild(document.createTextNode(i===words.length-1?'.':', '))});
  var tools=root.querySelector('.ws-tools');
  if(!tools){tools=document.createElement('div');tools.className='ws-tools';tools.innerHTML='<p>Zgjidh shkronjat me radhë për të formuar një fjalë.</p><button type="button" class="ws-clear">Pastro zgjedhjen</button> <button type="button" class="ws-reset">Fshi fjalët e gjetura</button><p class="ws-status" role="status" aria-live="polite"></p>';table.parentElement.insertAdjacentElement('afterend',tools)}
  var status=tools.querySelector('.ws-status');
  function load(){try{var v=JSON.parse(localStorage.getItem(key)||'{}');found=v && typeof v==='object'?v:{}}catch(e){found={}}}
  function save(){try{localStorage.setItem(key,JSON.stringify(found))}catch(e){}}
  function norm(s){return s.toLocaleLowerCase('sq').replace(/\s/g,'')}
  function refresh(){var marked={};Object.keys(found).forEach(function(w){if(Array.isArray(found[w]))found[w].forEach(function(n){marked[n]=true})});cells.forEach(function(b,i){b.classList.toggle('is-found',!!marked[i]);b.classList.toggle('is-current',selected.indexOf(i)!==-1);b.setAttribute('aria-pressed',selected.indexOf(i)!==-1 || !!marked[i]?'true':'false')});list.querySelectorAll('[data-word]').forEach(function(s){s.classList.toggle('word-found',!!found[s.dataset.word])})}
  function choose(index){
    if(selected.length && selected[selected.length-1]===index){selected.pop();status.textContent='Zgjedhja u ndryshua.';refresh();return}
    if(selected.indexOf(index)!==-1){status.textContent='Kjo shkronjë është tashmë e zgjedhur.';return}
    if(selected.length){var last=selected[selected.length-1],dr=Math.floor(index/11)-Math.floor(last/11),dc=index%11-last%11;if(Math.abs(dr)>1||Math.abs(dc)>1||(!dr&&!dc)){status.textContent='Zgjidh një shkronjë ngjitur.';return}if(selected.length>1){var prev=selected[selected.length-2],pr=Math.floor(last/11)-Math.floor(prev/11),pc=last%11-prev%11;if(dr!==pr||dc!==pc){status.textContent='Vazhdo në të njëjtin drejtim.';return}}}
    selected.push(index);var forward=selected.map(function(n){return rows[Math.floor(n/11)][n%11]}).join(''),backward=selected.slice().reverse().map(function(n){return rows[Math.floor(n/11)][n%11]}).join('');var match=words.find(function(w){return norm(w)===norm(forward)||norm(w)===norm(backward)});
    if(match){found[match]=selected.slice();save();selected=[];status.textContent='U gjet: '+match+'. '+Object.keys(found).length+' nga '+words.length+' fjalë.'}else status.textContent='Zgjedhja: '+forward+'.';refresh();
  }
  Array.from(body.rows).forEach(function(tr,r){Array.from(tr.cells).forEach(function(td,c){var letter=td.textContent.trim(),b=document.createElement('button'),index=r*11+c;b.type='button';b.textContent=letter;b.setAttribute('aria-label','Rreshti '+(r+1)+', kolona '+(c+1)+': '+letter);b.setAttribute('aria-pressed','false');b.tabIndex=index? -1:0;td.textContent='';td.appendChild(b);cells.push(b);b.addEventListener('click',function(){choose(index)});b.addEventListener('keydown',function(e){var delta={ArrowLeft:-1,ArrowRight:1,ArrowUp:-11,ArrowDown:11}[e.key];if(delta===undefined)return;var next=index+delta;if(next<0||next>=110||(delta===-1&&c===0)||(delta===1&&c===10))return;e.preventDefault();b.tabIndex=-1;cells[next].tabIndex=0;cells[next].focus()})})});
  tools.querySelector('.ws-clear').addEventListener('click',function(){selected=[];status.textContent='Zgjedhja u pastrua.';refresh()});tools.querySelector('.ws-reset').addEventListener('click',function(){found={};selected=[];save();status.textContent='Fjalët e gjetura u fshinë.';refresh()});
  window.addEventListener('storage',function(e){if(e.key===key&&root.isConnected){load();selected=[];refresh()}});load();refresh();
}
init();
document.addEventListener('adt:page-changed',function(){init();});
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);
})();
