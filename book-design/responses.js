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

  restoreAll();
  document.addEventListener('DOMContentLoaded', function () { restoreAll(); });
  window.addEventListener('load', function () { restoreAll(); });
  // After an in-place page turn, re-apply stored answers to every field (the reader may re-insert or rewrite fields), then load page scripts.
  document.addEventListener('adt:page-changed', function () {
    restoreAll(true); loadPageScripts();
    setTimeout(function () { restoreAll(true); }, 60);
    setTimeout(function () { restoreAll(true); }, 400);
  });
  loadPageScripts();

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
