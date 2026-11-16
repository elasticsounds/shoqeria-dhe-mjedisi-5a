/* Word search for reader pages (first used on page 69). Loaded through data-page-script by responses.js.
 *
 * Markup (see book-design/part2/specs/pg069.py):
 *   <div data-wordsearch data-words="avokati,prokuroria" data-store="pg069.wordsearch" data-page-script="./book-design/wordsearch.js">
 *     <table class="ws-grid"><tr><td>A</td>…</tr></table>      letters; a cell may hold a digraph (Gj)
 *     <ul class="ws-words"><li data-word="avokati">… <span class="ws-state"></span></li></ul>
 *     <button class="ws-clear">, <button class="ws-reset">, <p class="ws-status" role="status">
 *
 * How it is used: choose the first letter of a word, then the last one; the letters between are filled in.
 * Works with mouse, touch and keyboard (arrow keys, Home/End, Enter or Space, Escape). No dragging is needed.
 * Found words turn green and are named in the cell labels and in the word list, so colour is never the only signal.
 * Found words are kept in this browser through window.adtResponses.
 *
 * Feedback uses the reader's activity system where it can: the section is an activity_custom, registered with
 * window.adtRegisterCustomActivity, so the reader shows its Submit button and, on success, plays its sound and fires the
 * confetti. A found word plays the reader's "right" sound, a wrong selection its "wrong" sound (assets/sounds). When the
 * last word is found the puzzle submits itself. The reader's popup is not available to page scripts, so toast() below
 * shows one that looks the same.
 */
(function () {
  var audio = {};
  function play(name) {
    try {
      var a = audio[name] || (audio[name] = new Audio('./assets/sounds/' + name + '.mp3'));
      a.volume = 0.5; a.pause(); a.currentTime = 0; var p = a.play(); if (p && p.catch) p.catch(function () {});
    } catch (_) {}
  }
  function toast(ok, msg) {
    var box = document.getElementById('ws-toasts');
    if (!box) { box = document.createElement('div'); box.id = 'ws-toasts'; box.className = 'ws-toasts'; document.body.appendChild(box); }
    box.textContent = '';
    var t = document.createElement('div'); t.className = 'ws-toast ' + (ok ? 'is-ok' : 'is-warn'); t.setAttribute('role', 'status');
    var e = document.createElement('span'); e.setAttribute('aria-hidden', 'true'); e.textContent = ok ? '🎉' : '✍️';
    var m = document.createElement('p'); m.textContent = msg;
    var x = document.createElement('button'); x.type = 'button'; x.setAttribute('aria-label', 'Mbyll'); x.textContent = '×';
    x.addEventListener('click', function () { t.remove(); });
    t.appendChild(e); t.appendChild(m); t.appendChild(x); box.appendChild(t);
    setTimeout(function () { t.remove(); }, ok ? 4000 : 5000);
  }
  // the reader's Submit button (blue while it says Submit, green once it says Next)
  function submitButton() { return document.querySelector('#nav-container button[class*="bg-blue-600"], #interface-container button[class*="bg-blue-600"]'); }

  function init() {
    document.querySelectorAll('[data-wordsearch]').forEach(function (root) {
      if (root.dataset.wsReady) return; root.dataset.wsReady = '1';
      var table = root.querySelector('table.ws-grid'), status = root.querySelector('.ws-status');
      var words = (root.dataset.words || '').split(',').map(function (w) { return w.trim(); }).filter(Boolean);
      var store = root.dataset.store || 'wordsearch';
      var rows = Array.from(table.rows), nRows = rows.length, nCols = rows[0].cells.length;
      var letters = [], cells = [], found = {}, start = -1, sel = [];
      var norm = function (s) { return s.toLocaleLowerCase('sq').replace(/\s/g, ''); };
      var rc = function (i) { return [Math.floor(i / nCols), i % nCols]; };
      var where = function (i) { var p = rc(i); return 'rreshti ' + (p[0] + 1) + ', kolona ' + (p[1] + 1); };
      var say = function (msg) { status.textContent = msg; };

      function load() {
        var v = window.adtResponses && window.adtResponses.load(store); found = {};
        if (v && typeof v === 'object') words.forEach(function (w) { if (Array.isArray(v[w])) found[w] = v[w]; });
      }
      function save() { if (window.adtResponses) window.adtResponses.save(store, Object.keys(found).length ? found : null); }

      function refresh() {
        var owner = {};
        words.forEach(function (w, k) { (found[w] || []).forEach(function (i) { (owner[i] = owner[i] || []).push(k); }); });
        cells.forEach(function (b, i) {
          var own = owner[i], picked = sel.indexOf(i) !== -1;
          b.className = 'ws-cell' + (own ? ' is-found' : '') + (picked ? ' is-current' : '') + (i === start ? ' is-start' : '');
          b.setAttribute('aria-pressed', picked ? 'true' : 'false');
          b.setAttribute('aria-label', letters[i] + ', ' + where(i) +
            (own ? ', pjesë e fjalës së gjetur: ' + own.map(function (k) { return words[k]; }).join(', ') : '') + (picked ? ', e zgjedhur' : ''));
        });
        root.querySelectorAll('.ws-words [data-word]').forEach(function (li) {
          var k = words.indexOf(li.dataset.word), ok = !!found[li.dataset.word], st = li.querySelector('.ws-state');
          li.className = ok ? 'is-found' : '';
          if (st) st.textContent = ok ? ' (u gjet)' : ' (ende pa u gjetur)';
        });
      }

      // cells from a to b when they lie on one row, column or diagonal; otherwise null
      function line(a, b) {
        var A = rc(a), B = rc(b), dr = B[0] - A[0], dc = B[1] - A[1];
        if (dr && dc && Math.abs(dr) !== Math.abs(dc)) return null;
        var n = Math.max(Math.abs(dr), Math.abs(dc)), out = [];
        for (var k = 0; k <= n; k++) out.push((A[0] + Math.sign(dr) * k) * nCols + A[1] + Math.sign(dc) * k);
        return out;
      }

      function choose(i) {
        if (start === -1 || sel.length > 1) { start = i; sel = [i]; say('Shkronja e parë: ' + letters[i] + '. Tani zgjidh shkronjën e fundit të fjalës.'); refresh(); return; }
        if (i === start) { start = -1; sel = []; say('Zgjedhja u pastrua.'); refresh(); return; }
        var path = line(start, i);
        if (!path) { play('error'); start = i; sel = [i]; say('Shkronjat duhet të jenë në një vijë të drejtë. Shkronja e parë tani është ' + letters[i] + '.'); refresh(); return; }
        var text = path.map(function (n) { return letters[n]; }).join(''), back = path.slice().reverse().map(function (n) { return letters[n]; }).join('');
        var match = words.find(function (w) { return norm(w) === norm(text) || norm(w) === norm(back); });
        if (match) {
          var again = !!found[match]; found[match] = path; save(); start = -1; sel = [];
          var n = Object.keys(found).length;
          if (n === words.length && !again) { refresh(); finish(); }
          else play('validate_success');
          say(n === words.length ? 'Urime! E gjete fjalën “' + match + '”. I gjete të gjitha fjalët!'
            : (again ? 'Fjalën “' + match + '” e ke gjetur tashmë. ' : 'Të lumtë! E gjete fjalën “' + match + '”. ') + n + ' nga ' + words.length + ' fjalë.');
        } else { play('error'); sel = path; say('Zgjedhja: ' + text + '. Kjo nuk është një nga fjalët. Provo përsëri.'); }
        refresh();
      }

      // All words found: let the reader run its own success (sound, confetti, Next button) through its Submit button;
      // validate() below shows the popup. Without the reader (page opened on its own) play the sound and show the popup here.
      function finish() {
        var btn = registered && submitButton();
        if (btn && !btn.disabled) btn.click(); else { play('success'); validate(); }
      }
      function validate() {
        var n = Object.keys(found).length, all = n === words.length;
        if (section) section.__adtItems = words.map(function (w) { return { itemId: w, response: found[w] ? w : '', result: found[w] ? 'correct' : 'empty' }; });   // read by tracking.js
        toast(all, all ? 'Urime! I gjete të gjitha fjalët.' : n + ' nga ' + words.length + ' fjalë të gjetura. Gjej edhe të tjerat.');
        return all;
      }
      // Register with the reader once it has set this section up (it gives the section a role).
      var registered = false, section = root.closest('section[data-section-type^="activity_custom"]'), tries = 0;
      (function register() {
        if (!section || !root.isConnected || registered) return;
        if (section.hasAttribute('role') && typeof window.adtRegisterCustomActivity === 'function') {
          registered = true; window.adtRegisterCustomActivity(section, { validate: validate }); return;
        }
        if (++tries < 40) setTimeout(register, 150);
      })();

      function focus(i) { cells.forEach(function (b, k) { b.tabIndex = k === i ? 0 : -1; }); cells[i].focus(); }

      rows.forEach(function (tr, r) {
        Array.from(tr.cells).forEach(function (td, c) {
          var i = r * nCols + c, b = document.createElement('button');
          letters.push(td.textContent.trim()); b.type = 'button'; b.textContent = letters[i]; b.tabIndex = i ? -1 : 0;
          td.textContent = ''; td.appendChild(b); cells.push(b);
          b.addEventListener('click', function () { cells.forEach(function (x, k) { x.tabIndex = k === i ? 0 : -1; }); choose(i); });
          b.addEventListener('keydown', function (e) {
            var to = { ArrowLeft: c > 0 ? i - 1 : i, ArrowRight: c < nCols - 1 ? i + 1 : i, ArrowUp: r > 0 ? i - nCols : i, ArrowDown: r < nRows - 1 ? i + nCols : i,
              Home: r * nCols, End: r * nCols + nCols - 1 }[e.key];
            if (to !== undefined) { e.preventDefault(); if (to !== i) focus(to); return; }
            if (e.key === 'Escape' && sel.length) { e.preventDefault(); start = -1; sel = []; say('Zgjedhja u pastrua.'); refresh(); }
          });
        });
      });
      root.classList.add('ws-live');
      root.querySelector('.ws-clear').addEventListener('click', function () { start = -1; sel = []; say('Zgjedhja u pastrua.'); refresh(); });
      root.querySelector('.ws-reset').addEventListener('click', function () { found = {}; start = -1; sel = []; save(); say('Fjalët e gjetura u fshinë. Mund të fillosh nga e para.'); refresh(); });
      load(); refresh();
    });
  }
  init();
  document.addEventListener('adt:page-changed', init);
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
})();
