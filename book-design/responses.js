/* Saves activity answers in this browser (localStorage) and restores them when a page is opened again.
 *
 * Storage: one JSON object per page under "adt5a.responses.v1.<bucket>", where <bucket> is
 *   - the nearest [data-response-page] value (answers shared between pages, e.g. the page 9 diary), else
 *   - the control's data-response-section (sub-activities that reuse keys, e.g. page 24), else
 *   - the page's <meta name="title-id">.
 * Field key: data-response-key || data-activity-item || id || name. Radios are stored per group name.
 * Not saved: quiz options (the runtime grades on selection, so a restored choice would show without feedback),
 * file inputs (browsers do not allow restoring them), hidden/disabled controls.
 * If storage is unavailable (private mode, quota), pages keep working; answers just are not kept.
 */
/* Password gate for the web version (first block below).
 * This is a courtesy lock, not security: the site is static, so anyone who knows a file's address or reads the page
 * source can still fetch the content. It keeps casual visitors out. The password is not stored here, only a salted
 * SHA-256 hash; to change it, replace HASH with:  printf 'shoqeria-dhe-mjedisi-5a:<new password>' | shasum -a 256
 * Not shown inside an LMS (SCORM), where the LMS signs pupils in, nor on a local preview (localhost, file://).
 */
(function () {
  var HASH = '1420a08137de43e86e3f6e44cf84fe3c88be021ed95804b05d47ca83b44ab994', SALT = 'shoqeria-dhe-mjedisi-5a:', KEY = 'adt5a.gate.v1';
  if (window.__adt5aGate) return; window.__adt5aGate = true;
  if (!/^https?:$/.test(location.protocol) || /^(localhost|127\.0\.0\.1|\[::1\])$/.test(location.hostname) || /\.(localhost|test)$/.test(location.hostname)) return;
  try { for (var w = window, i = 0; i < 7; i++) { if (w.API) return; if (!w.parent || w.parent === w) break; w = w.parent; } } catch (_) {}
  try { if (localStorage.getItem(KEY) === HASH) return; } catch (_) {}

  var style = document.createElement('style');
  style.textContent = 'html.adt-locked body{overflow:hidden!important}html.adt-locked body>*:not(.adt-gate){display:none!important}' +
    '.adt-gate{position:fixed;inset:0;z-index:2147483000;display:flex;align-items:center;justify-content:center;padding:16px;background:#f3ecf8;font-family:BookPoppins,Poppins,Arial,sans-serif;color:#231f20}' +
    '.adt-gate form{width:min(100%,460px);padding:28px;border:2px solid #794282;border-radius:20px;background:#fff;box-shadow:0 10px 30px rgba(0,0,0,.12)}' +
    '.adt-gate h1{margin:0 0 8px;font:700 26px/1.3 BookPoppins,Poppins,Arial,sans-serif;color:#794282}' +
    '.adt-gate p{margin:0 0 16px;font:400 20px/1.5 BookPoppins,Poppins,Arial,sans-serif}' +
    '.adt-gate label{display:block;margin:0 0 6px;font:600 20px/1.4 BookPoppins,Poppins,Arial,sans-serif}' +
    '.adt-gate input{display:block;width:100%;box-sizing:border-box;min-height:52px;padding:8px 14px;border:2px solid #5b5b5b;border-radius:12px;background:#fff;color:#231f20;font:400 20px/1.4 BookPoppins,Poppins,Arial,sans-serif}' +
    '.adt-gate input:focus-visible,.adt-gate button:focus-visible{outline:3px solid #075a70;outline-offset:2px}' +
    '.adt-gate button{margin:16px 0 0;min-height:52px;padding:10px 28px;border:0;border-radius:999px;background:#794282;color:#fff;font:600 20px/1.3 BookPoppins,Poppins,Arial,sans-serif;cursor:pointer}' +
    '.adt-gate .adt-gate-error{min-height:30px;margin:10px 0 0;font-weight:600;color:#a3231c}';
  document.head.appendChild(style);
  document.documentElement.classList.add('adt-locked');

  var gate = document.createElement('div'); gate.className = 'adt-gate';
  gate.innerHTML = '<form role="dialog" aria-modal="true" aria-labelledby="adt-gate-title" novalidate>' +
    '<h1 id="adt-gate-title">Shoqëria dhe mjedisi</h1><p>Ky libër është i mbrojtur me fjalëkalim.</p>' +
    '<label for="adt-gate-pw">Fjalëkalimi</label><input id="adt-gate-pw" type="password" autocomplete="current-password" aria-describedby="adt-gate-error" required>' +
    '<button type="submit">Hyr</button><p class="adt-gate-error" id="adt-gate-error" role="alert"></p></form>';
  document.body.appendChild(gate);
  var input = gate.querySelector('input'), error = gate.querySelector('.adt-gate-error');
  setTimeout(function () { input.focus(); }, 50);

  function digest(text) {
    return crypto.subtle.digest('SHA-256', new TextEncoder().encode(text)).then(function (buf) {
      return Array.prototype.map.call(new Uint8Array(buf), function (b) { return (b < 16 ? '0' : '') + b.toString(16); }).join('');
    });
  }
  gate.querySelector('form').addEventListener('submit', function (e) {
    e.preventDefault(); error.textContent = '';
    if (!window.crypto || !crypto.subtle) { error.textContent = 'Ky shfletues nuk e hap dot librin. Provo një shfletues tjetër.'; return; }
    digest(SALT + input.value).then(function (h) {
      if (h !== HASH) { error.textContent = 'Fjalëkalimi nuk është i saktë. Provo përsëri.'; input.select(); return; }
      try { localStorage.setItem(KEY, HASH); } catch (_) {}
      document.documentElement.classList.remove('adt-locked'); gate.remove();
    });
  });
  // keep keyboard focus inside the gate while it is shown
  document.addEventListener('focusin', function (e) { if (gate.isConnected && !gate.contains(e.target)) input.focus(); });
})();

(function () {
  if (window.__adt5aResponses) return;
  window.__adt5aResponses = true;

  var PREFIX = 'adt5a.responses.v1.';
  var SKIP = '[data-section-type="activity_quiz"], #simple-main';
  var restored = new WeakSet();

  function pageId() {
    var meta = document.querySelector('meta[name="title-id"]');
    return (meta && meta.content) || location.pathname.split('/').pop().replace(/\.html?$/, '');
  }

  function bucketOf(el) {
    var shared = el.closest('[data-response-page]');
    if (shared) return shared.getAttribute('data-response-page');
    if (el.getAttribute('data-response-section')) return el.getAttribute('data-response-section');
    return pageId();
  }

  function keyOf(el) {
    if (el.type === 'radio') return el.name ? 'radio:' + el.name : null;
    return el.getAttribute('data-response-key') || el.getAttribute('data-activity-item') || el.id || el.name || null;
  }

  function eligible(el) {
    if (!el || !el.matches || !el.matches('input, textarea, select')) return false;
    if (el.type === 'file' || el.type === 'hidden' || el.type === 'submit' || el.type === 'button' || el.disabled) return false;
    if (el.closest(SKIP)) return false;
    return !!el.closest('#content') && !!keyOf(el);
  }

  function read(bucket) {
    try { return JSON.parse(localStorage.getItem(PREFIX + bucket) || '{}') || {}; } catch (_) { return {}; }
  }

  function write(bucket, data) {
    try {
      var empty = Object.keys(data).every(function (k) { return data[k] === '' || data[k] === false || data[k] == null; });
      if (empty) localStorage.removeItem(PREFIX + bucket);
      else localStorage.setItem(PREFIX + bucket, JSON.stringify(data));
    } catch (_) { /* storage unavailable: keep working without saving */ }
  }

  function save(el) {
    if (!eligible(el)) return;
    var bucket = bucketOf(el), data = read(bucket), key = keyOf(el);
    if (el.type === 'radio') { if (el.checked) data[key] = el.value; }
    else if (el.type === 'checkbox') data[key] = el.checked;
    else data[key] = el.value;
    write(bucket, data);
  }

  function restore(el, force) {
    if ((!force && restored.has(el)) || !eligible(el)) return;
    restored.add(el);
    var data = read(bucketOf(el)), key = keyOf(el);
    if (!(key in data)) return;
    var v = data[key];
    if (el.type === 'radio') el.checked = (el.value === v);
    else if (el.type === 'checkbox') el.checked = !!v;
    else if (el.value !== v) el.value = v;
    // let page scripts react to a restored answer (e.g. the page 37 crossword grid)
    try { el.dispatchEvent(new CustomEvent('adt:response-restored', { bubbles: true })); } catch (_) {}
  }

  function restoreAll(force) {
    document.querySelectorAll('#content input, #content textarea, #content select').forEach(function (el) { restore(el, force); });
  }

  // Reader activities (multiple choice, multi-select, fill-in-the-blank, open-ended; pages 87–99). The reader only enables its Submit button for answers it has seen being given, and it
  // unticks checkboxes when it sets a multi-select up. So once the reader has set the activity up (it puts a role on the
  // options or the section), put the stored answers back and tell it about them.
  var CHOICE = '#content section[data-section-type="activity_multiple_choice"], #content section[data-section-type="activity_multi_select"]';
  var BLANKS = '#content section[data-section-type="activity_fill_in_the_blank"][role], #content section[data-section-type="activity_open_ended_answer"][role]';
  function syncChoices() {
    document.querySelectorAll(CHOICE).forEach(function (sec) {
      sec.querySelectorAll('input[type="radio"], input[type="checkbox"]').forEach(function (el) {
        var label = el.closest('label'); if (!label || !/^(radio|checkbox)$/.test(label.getAttribute('role') || '')) return;
        if (!sec.__adtSynced) restore(el, true);
        if (el.checked && label.getAttribute('aria-checked') !== 'true') el.dispatchEvent(new Event('change', { bubbles: true }));
        el.__adtReady = true;
      });
      if (sec.querySelector('label[role]')) sec.__adtSynced = true;
    });
    // true/false tables: the reader listens for the radios' change event
    document.querySelectorAll('#content section[data-section-type="activity_true_false"][role]').forEach(function (sec) {
      if (sec.__adtSynced) return; sec.__adtSynced = true;
      sec.querySelectorAll('input[type="radio"]').forEach(function (el) {
        restore(el, true); if (el.checked) el.dispatchEvent(new Event('change', { bubbles: true }));
      });
    });
    // typed answers: an input event makes the reader notice the restored text. Its "became right/wrong" sound is avoided by
    // telling it the answer already had that state.
    document.querySelectorAll(BLANKS).forEach(function (sec) {
      if (sec.__adtSynced) return; sec.__adtSynced = true;
      sec.querySelectorAll('input[type="text"], textarea').forEach(function (el) {
        if (!el.value.trim()) return;
        var key = (window.correctAnswers || {})[el.getAttribute('data-activity-item')], v = el.value.trim().toLowerCase();
        var ok = key == null || key === '' || String(key).split('|').some(function (k) { return k.trim().toLowerCase() === v; });
        el.dataset.wasValid = ok ? 'true' : 'false';
        el.dispatchEvent(new Event('input', { bubbles: true }));
      });
    });
  }
  function syncChoicesSoon() { [200, 700, 1500, 3000].forEach(function (ms) { setTimeout(syncChoices, ms); }); }

  // Page scripts: the reader's in-place page turn re-runs inline scripts but does not load external ones.
  // A page can declare one with data-page-script="./path.js"; it is loaded once and then handles later page turns itself.
  function loadPageScripts() {
    document.querySelectorAll('main [data-page-script]').forEach(function (el) {
      var src = el.getAttribute('data-page-script'); if (!src) return;
      var abs = new URL(src, location.href).href.split('?')[0];
      var loaded = Array.prototype.some.call(document.scripts, function (s) { return s.src && s.src.split('?')[0] === abs; });
      if (loaded) return;
      var tag = document.createElement('script'); tag.src = src; tag.setAttribute('data-book-page-script', ''); document.body.appendChild(tag);
    });
  }

  document.addEventListener('input', function (e) { save(e.target); }, true);
  document.addEventListener('change', function (e) { save(e.target); }, true);
  // In the reader's choice activities the reader ticks the option itself, so the browser often fires no change event
  // (always for a multi-select, and for a radio when its label is clicked). Save the choices after each click or key press.
  ['click', 'keyup'].forEach(function (type) {
    document.addEventListener(type, function (e) {
      var sec = e.target.closest && e.target.closest('section[data-section-type="activity_multi_select"], section[data-section-type="activity_multiple_choice"]'); if (!sec) return;
      setTimeout(function () { sec.querySelectorAll('input[type="checkbox"], input[type="radio"]').forEach(save); }, 0);
    }, true);
  });

  restoreAll();
  document.addEventListener('DOMContentLoaded', function () { restoreAll(); });
  window.addEventListener('load', function () { restoreAll(); syncChoicesSoon(); });
  // After an in-place page turn, re-apply stored answers to every field (the reader may re-insert or rewrite fields), then load page scripts.
  document.addEventListener('adt:page-changed', function () {
    restoreAll(true); loadPageScripts();
    setTimeout(function () { restoreAll(true); }, 60);
    setTimeout(function () { restoreAll(true); }, 400);
    syncChoicesSoon();
  });
  loadPageScripts();

  // Activity tracking (attempts, completion, score per activity; reported to the LMS by assets/scorm.js).
  (function () {
    var me = document.querySelector('script[data-book-responses]'), tag = document.createElement('script');
    tag.src = (me && me.src ? me.src.split('?')[0].replace(/responses\.js$/, '') : './book-design/') + 'tracking.js';
    document.body.appendChild(tag);
  })();

  // The reader runtime builds or re-renders parts of the page after load; restore any controls it adds.
  new MutationObserver(function (mutations) {
    mutations.forEach(function (m) {
      m.addedNodes.forEach(function (n) {
        if (n.nodeType !== 1) return;
        if (n.matches('input, textarea, select')) restore(n);
        else if (n.querySelectorAll) n.querySelectorAll('input, textarea, select').forEach(restore);
      });
    });
  }).observe(document.documentElement, { childList: true, subtree: true });

  // In-book links turn the page in place, like the dock. A plain link would reload the document, which inside an LMS
  // ends the SCORM session (LMSFinish) and starts a new one; SCORM 1.2 does not allow that. The reader soft-navigates
  // on popstate to the current URL, so: update the URL, then fire popstate. Only where the reader soft-navigates
  // (http/https, not ?embed=1); modifier clicks, new-tab links and other sites keep their normal behaviour.
  document.addEventListener('click', function (e) {
    if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var a = e.target.closest && e.target.closest('main a[href]');
    if (!a || (a.target && a.target !== '_self') || a.hasAttribute('download')) return;
    if (!/^https?:$/.test(location.protocol) || new URLSearchParams(location.search).get('embed') === '1') return;
    var url = new URL(a.getAttribute('href'), location.href), here = new URL(location.href);
    var dir = function (u) { return u.pathname.slice(0, u.pathname.lastIndexOf('/') + 1); };
    if (url.origin !== here.origin || dir(url) !== dir(here) || !/\.html?$/i.test(url.pathname)) return;
    if (url.pathname === here.pathname && url.hash) return;           // same-page anchors behave normally
    e.preventDefault();
    try {
      history.pushState({ adtSoftNav: true }, '', url.href);
      window.dispatchEvent(new PopStateEvent('popstate', { state: { adtSoftNav: true } }));
    } catch (_) { location.href = url.href; }
  });

  // Small API for pages with custom activities (e.g. the page 14 drawing).
  window.adtResponses = {
    load: function (name) { try { return JSON.parse(localStorage.getItem(PREFIX + 'custom.' + name) || 'null'); } catch (_) { return null; } },
    save: function (name, value) {
      try {
        if (value == null) localStorage.removeItem(PREFIX + 'custom.' + name);
        else localStorage.setItem(PREFIX + 'custom.' + name, JSON.stringify(value));
        return true;
      } catch (_) { return false; }
    }
  };
})();
