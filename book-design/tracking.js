/* Activity tracking for this book — the stop-gap described in SCORM-TRACKING-SPEC.md (section 4).
 *
 * The reader does not announce submissions yet, so this file watches the reader's Submit button (and quiz selections),
 * reads the result the reader has drawn on the page, and dispatches the event the spec asks the reader to send:
 *
 *   document  'adt:activity-submitted'  detail = { activityId, type, graded, complete, items[], correct, total, empty }
 *
 * It then keeps one record per activity (attempts, completion, score) in this browser and announces
 *   document  'adt:progress-updated'    detail = { activityId, record, submission }
 * which assets/scorm.js reports to the LMS. window.adtProgress.get() returns all records.
 * When the reader sends 'adt:activity-submitted' itself, delete the "observe" half of this file and keep the tracker.
 *
 * Loaded on every page by responses.js. Open-ended answers are never marked right or wrong, and their text is not
 * put in the event (only that the pupil answered).
 */
(function () {
  if (window.__adt5aTracking) return;
  window.__adt5aTracking = true;

  // ---------- tracker ----------
  var KEY = 'adt5a.progress.v1';
  function load() { try { return JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (_) { return {}; } }
  function store(all) { try { localStorage.setItem(KEY, JSON.stringify(all)); } catch (_) {} }
  window.adtProgress = { get: load, key: KEY };

  document.addEventListener('adt:activity-submitted', function (e) {
    var d = e.detail; if (!d || !d.activityId) return;
    var all = load(), r = all[d.activityId] || { attempts: 0, complete: false };
    r.type = d.type; r.graded = !!d.graded; r.attempts += 1;
    if (d.complete && !r.complete) { r.complete = true; r.firstCorrectAttempt = r.attempts; }   // completion latches
    r.correct = d.correct || 0; r.total = d.total || 0; r.lastSubmitted = new Date().toISOString();
    all[d.activityId] = r; store(all);
    document.dispatchEvent(new CustomEvent('adt:progress-updated', { detail: { activityId: d.activityId, record: r, submission: d } }));
  });

  // ---------- observe the reader ----------
  function pageId() {
    var meta = document.querySelector('meta[name="title-id"]');
    return (meta && meta.content) || location.pathname.split('/').pop().replace(/\.html?$/, '');
  }
  function activity() { return document.querySelector('#content section[data-section-type^="activity_"]'); }
  function typeOf(sec) { return sec.getAttribute('data-section-type').replace(/^activity_/, ''); }
  var CHROME = '#nav-container button, #interface-container button';
  function isSubmit(btn) { return /bg-blue-600/.test(btn.className); }                 // blue = Submit, green = Next
  function nowNext() { return Array.prototype.some.call(document.querySelectorAll(CHROME), function (b) { return /bg-emerald-600/.test(b.className); }); }
  function fields(sec) { return Array.prototype.slice.call(sec.querySelectorAll('input[type="text"], textarea')); }
  function itemId(el) { return el.getAttribute('data-activity-item') || el.id || el.name || ''; }

  function collect(sec, type) {
    var items = [], graded = true;
    if (type === 'fill_in_the_blank') {
      var keys = window.correctAnswers || {};
      fields(sec).forEach(function (el) {
        var id = itemId(el), keyed = keys[id] != null && String(keys[id]).replace(/\|/g, '') !== '', v = el.value.trim();
        if (!keyed) { items.push({ itemId: id, response: '', result: v ? 'neutral' : 'empty', graded: false }); return; }
        items.push({ itemId: id, response: v, graded: true,
          result: !v ? 'empty' : el.classList.contains('border-green-500') ? 'correct' : 'wrong' });
      });
    } else if (type === 'open_ended_answer') {
      graded = false;
      fields(sec).forEach(function (el) { items.push({ itemId: itemId(el), response: '', result: el.value.trim() ? 'neutral' : 'empty', graded: false }); });
    } else if (type === 'multiple_choice') {
      var names = [];
      sec.querySelectorAll('input[type="radio"]').forEach(function (r) { if (names.indexOf(r.name) === -1) names.push(r.name); });
      names.forEach(function (name) {
        var picked = null;
        sec.querySelectorAll('input[type="radio"]').forEach(function (r) { var l = r.closest('label'); if (r.name === name && l && l.getAttribute('aria-checked') === 'true') picked = l; });
        var state = picked && picked.getAttribute('data-mc-style-state');
        items.push({ itemId: name, response: picked ? picked.querySelector('input').value : '', graded: true,
          result: !picked ? 'empty' : state === 'correct' ? 'correct' : 'wrong' });
      });
    } else if (type === 'multi_select') {
      var key = {}; try { key = JSON.parse(sec.getAttribute('data-correct-answers') || '{}'); } catch (_) {}
      sec.querySelectorAll('input[type="checkbox"][data-activity-item]').forEach(function (c) {
        var id = itemId(c), l = c.closest('label'), on = l && l.getAttribute('aria-checked') === 'true';
        if (on) items.push({ itemId: id, response: 'selected', graded: true, result: key[id] ? 'correct' : 'wrong' });
        else if (key[id]) items.push({ itemId: id, response: '', graded: true, result: 'empty' });
      });
    } else if (type === 'true_false') {
      var rows = [];
      sec.querySelectorAll('input[type="radio"][data-activity-item]').forEach(function (r) { var id = itemId(r); if (rows.indexOf(id) === -1) rows.push(id); });
      rows.forEach(function (id) {
        var picked = sec.querySelector('input[type="radio"][data-activity-item="' + id + '"]:checked');
        var mark = picked && picked.closest('label') && picked.closest('label').querySelector('.validation-mark i');
        items.push({ itemId: id, response: picked ? picked.value : '', graded: true,
          result: !picked ? 'empty' : mark && /fa-check/.test(mark.className) ? 'correct' : 'wrong' });
      });
    } else if (type === 'quiz') {
      var opt = sec.querySelector('.activity-option[aria-checked="true"]');
      if (!opt) return null;
      items.push({ itemId: sec.getAttribute('data-id') || pageId(), response: opt.getAttribute('data-activity-item') || '', graded: true,
        result: opt.getAttribute('aria-invalid') === 'false' ? 'correct' : 'wrong' });
    } else {
      // custom activities describe their own items (see wordsearch.js): section.__adtItems = [{ itemId, response, result }]
      (sec.__adtItems || []).forEach(function (i) { items.push({ itemId: i.itemId, response: i.response || '', result: i.result, graded: true }); });
    }
    var scored = items.filter(function (i) { return i.graded; });
    var correct = scored.filter(function (i) { return i.result === 'correct'; }).length;
    var empty = items.filter(function (i) { return i.result === 'empty'; }).length;
    return { type: type, graded: graded, items: items, correct: correct, total: scored.length, empty: empty };
  }

  function announce(sec, type, complete) {
    var d = collect(sec, type); if (!d) return;
    d.activityId = pageId();
    d.complete = type === 'quiz' ? d.correct === d.total : complete;
    document.dispatchEvent(new CustomEvent('adt:activity-submitted', { detail: d }));
  }

  // Submit: read the page once the reader has drawn its verdict (open-ended answers are checked asynchronously).
  document.addEventListener('click', function (e) {
    var btn = e.target.closest && e.target.closest(CHROME);
    if (!btn || btn.disabled || !isSubmit(btn)) return;
    var sec = activity(); if (!sec) return;
    var type = typeOf(sec); if (type === 'quiz') return;
    setTimeout(function () { if (sec.isConnected) announce(sec, type, nowNext()); }, 350);
  }, true);

  // Quizzes grade when an option is chosen; each choice is one attempt.
  var quizTimer = null, lastQuiz = '';
  function quizPick(e) {
    var sec = e.target.closest && e.target.closest('section[data-section-type="activity_quiz"]'); if (!sec) return;
    clearTimeout(quizTimer);
    quizTimer = setTimeout(function () {
      var opt = sec.querySelector('.activity-option[aria-checked="true"]'); if (!opt || !sec.isConnected) return;
      var sig = pageId() + '|' + opt.getAttribute('data-activity-item'); if (sig === lastQuiz) return;   // same option again is not a new attempt
      lastQuiz = sig; announce(sec, 'quiz', false);
    }, 300);
  }
  document.addEventListener('click', quizPick, true);
  document.addEventListener('keyup', quizPick, true);
  document.addEventListener('adt:page-changed', function () { lastQuiz = ''; });
})();
