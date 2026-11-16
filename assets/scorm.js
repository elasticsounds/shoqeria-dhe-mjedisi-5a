// scorm.js — SCORM 1.2 adapter for this book (hand-maintained; implements SCORM-TRACKING-SPEC.md section 3.3).
// The ACTIVITIES list below is rewritten by book-design/build-scorm.py from the pages; do not edit it by hand.
//
// Reported to the LMS:
//   cmi.core.lesson_location        current page
//   cmi.objectives.n.*              one objective per activity: status (not attempted / incomplete / completed / passed) and score
//   cmi.interactions.n.*            one entry per answered item per attempt (correct / wrong), or one neutral entry per
//                                   open-ended submission; the text of open-ended answers is not sent
//   cmi.core.score.raw              share of checked items that are right at the latest attempt, over the whole book
//   cmi.core.lesson_status          completed once every activity was submitted and the last page was reached
//   cmi.suspend_data                compact progress (attempts, completion, score per activity) so it follows the pupil
//   cmi.core.session_time           time spent this session
// Progress comes from book-design/tracking.js ('adt:progress-updated').
(function () {
  'use strict';

  function findAPI(win) {
    var depth = 0;
    while (depth < 7) {
      if (win.API) return win.API;
      if (!win.parent || win.parent === win) break;
      win = win.parent; depth++;
    }
    return null;
  }
  var API = findAPI(window);
  if (!API) return; // not in a SCORM LMS

  // {id, t: type, g: graded (1/0), n: checked items}
  var ACTIVITIES = /*ADT-ACTIVITIES*/[{"id":"qz001","t":"quiz","g":1,"n":1},{"id":"pg009_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg010_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg013_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"qz002","t":"quiz","g":1,"n":1},{"id":"pg014_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg015_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg017_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"qz003","t":"quiz","g":1,"n":1},{"id":"pg018_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg018_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg018_sec003","t":"open_ended_answer","g":0,"n":0},{"id":"pg018_sec004","t":"open_ended_answer","g":0,"n":0},{"id":"pg019_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg022_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"qz004","t":"quiz","g":1,"n":1},{"id":"pg023_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg023_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg024_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg025_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"qz005","t":"quiz","g":1,"n":1},{"id":"pg027_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg027_sec003","t":"open_ended_answer","g":0,"n":0},{"id":"pg028_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg029_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg030_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg030_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg030_sec003","t":"open_ended_answer","g":0,"n":0},{"id":"qz006","t":"quiz","g":1,"n":1},{"id":"pg031_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg031_sec003","t":"open_ended_answer","g":0,"n":0},{"id":"pg031_sec004","t":"open_ended_answer","g":0,"n":0},{"id":"pg032_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg033_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg033_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg034_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg035_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"qz007","t":"quiz","g":1,"n":1},{"id":"pg036_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg037_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg037_sec003","t":"open_ended_answer","g":0,"n":0},{"id":"pg038_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg039_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"qz008","t":"quiz","g":1,"n":1},{"id":"pg040_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg041_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg042_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"qz009","t":"quiz","g":1,"n":1},{"id":"pg043_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg044_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg045_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg046_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg047_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg048_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg048_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"qz010","t":"quiz","g":1,"n":1},{"id":"pg049_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg049_sec003","t":"open_ended_answer","g":0,"n":0},{"id":"pg049_sec004","t":"open_ended_answer","g":0,"n":0},{"id":"pg050_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"qz011","t":"quiz","g":1,"n":1},{"id":"pg051_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg052_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg052_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg052_sec003","t":"open_ended_answer","g":0,"n":0},{"id":"pg054_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg055_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg055_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg057_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg058_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg060_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg060_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg062_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg063_sec001","t":"true_false","g":1,"n":6},{"id":"pg063_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg064_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg065_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg065_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg066_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg066_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg067_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg068_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg069_sec001","t":"custom","g":1,"n":4},{"id":"pg070_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg071_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg072_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg072_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg074_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg074_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg075_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg075_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg075_sec003","t":"open_ended_answer","g":0,"n":0},{"id":"pg077_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg077_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg078_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg078_sec002","t":"fill_in_the_blank","g":1,"n":5},{"id":"pg081_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg081_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg081_sec003","t":"open_ended_answer","g":0,"n":0},{"id":"pg082_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg083_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg083_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg083_sec003","t":"open_ended_answer","g":0,"n":0},{"id":"pg085_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg086_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg086_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg087_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg087_sec003","t":"open_ended_answer","g":0,"n":0},{"id":"pg088_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg089_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg089_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg089_sec003","t":"open_ended_answer","g":0,"n":0},{"id":"pg090_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg091_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg092_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg092_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg092_sec003","t":"open_ended_answer","g":0,"n":0},{"id":"pg093_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg094_sec002","t":"multiple_choice","g":1,"n":3},{"id":"pg096_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg096_sec002","t":"open_ended_answer","g":0,"n":0},{"id":"pg097_sec001","t":"open_ended_answer","g":0,"n":0},{"id":"pg097_sec002","t":"multi_select","g":1,"n":4},{"id":"pg097_sec003","t":"open_ended_answer","g":0,"n":0},{"id":"pg098_sec001","t":"multiple_choice","g":1,"n":1},{"id":"pg098_sec002","t":"fill_in_the_blank","g":1,"n":3},{"id":"pg098_sec003","t":"fill_in_the_blank","g":1,"n":8},{"id":"pg098_sec004","t":"fill_in_the_blank","g":1,"n":1},{"id":"pg099_sec001","t":"fill_in_the_blank","g":1,"n":3},{"id":"pg099_sec002","t":"fill_in_the_blank","g":1,"n":6},{"id":"pg099_sec003","t":"open_ended_answer","g":0,"n":0}]/*END-ADT-ACTIVITIES*/;
  var LAST_PAGE = /*ADT-LAST-PAGE*/"pg101_sec002"/*END-ADT-LAST-PAGE*/;
  var PROGRESS_KEY = 'adt5a.progress.v1', STUDENT_KEY = 'adt5a.progress.student';
  var index = {}; ACTIVITIES.forEach(function (a, i) { index[a.id] = i; });
  var started = Date.now();
  var set = function (k, v) { return API.LMSSetValue(k, String(v)); };
  var get = function (k) { try { return API.LMSGetValue(k) || ''; } catch (_) { return ''; } };

  API.LMSInitialize('');

  var meta = document.querySelector('meta[name="title-id"]');
  var pageId = meta ? meta.getAttribute('content') : '';

  // ---------- state: idx -> {a: attempts, c: complete, k: correct, t: total} ----------
  var state = {}, reachedEnd = false;
  (function restore() {
    var parts = get('cmi.suspend_data').split('|');
    if (parts[0] !== 'v1') return;
    reachedEnd = parts[1] === '1';
    (parts[2] || '').split(',').forEach(function (e) {
      var f = e.split('.'); if (f.length < 5) return;
      state[parseInt(f[0], 36)] = { a: parseInt(f[1], 36) || 0, c: f[2] === '1', k: parseInt(f[3], 36) || 0, t: parseInt(f[4], 36) || 0 };
    });
  })();

  // Keep this browser's record in step with the LMS, so attempt counts continue on another device. The local record is
  // only trusted when it belongs to the same LMS user; otherwise it is replaced (answers typed on the page are not touched).
  (function syncLocal() {
    var local = {}, student = get('cmi.core.student_id');
    try {
      if (localStorage.getItem(STUDENT_KEY) === student) local = JSON.parse(localStorage.getItem(PROGRESS_KEY) || '{}') || {};
      ACTIVITIES.forEach(function (act, i) {
        var s = state[i], l = local[act.id];
        if (l && (!s || l.attempts > s.a)) state[i] = { a: l.attempts || 0, c: !!l.complete || !!(s && s.c), k: l.correct || 0, t: l.total || 0 };
        s = state[i];
        if (s) local[act.id] = { type: act.t, graded: !!act.g, attempts: s.a, complete: s.c, correct: s.k, total: s.t,
          firstCorrectAttempt: l && l.firstCorrectAttempt, lastSubmitted: l && l.lastSubmitted };
        else delete local[act.id];
      });
      localStorage.setItem(PROGRESS_KEY, JSON.stringify(local)); localStorage.setItem(STUDENT_KEY, student);
    } catch (_) { /* storage unavailable: the LMS copy is still used */ }
  })();

  // ---------- objectives: SCORM 1.2 needs them created in order, so create any that are missing ----------
  var objectives = parseInt(get('cmi.objectives._count'), 10) || 0;
  for (var i = objectives; i < ACTIVITIES.length; i++) {
    set('cmi.objectives.' + i + '.id', ACTIVITIES[i].id);
    set('cmi.objectives.' + i + '.status', 'not attempted');
  }
  var interactions = parseInt(get('cmi.interactions._count'), 10) || 0;

  function writeObjective(i) {
    var act = ACTIVITIES[i], s = state[i]; if (!s) return;
    set('cmi.objectives.' + i + '.status', !s.a ? 'not attempted' : act.g ? (s.c ? 'passed' : 'incomplete') : 'completed');
    if (act.g) {
      var n = act.n || s.t || 1;
      set('cmi.objectives.' + i + '.score.raw', Math.round(100 * Math.min(s.k, n) / n));
      set('cmi.objectives.' + i + '.score.min', 0); set('cmi.objectives.' + i + '.score.max', 100);
    }
  }

  function writeOverall() {
    var right = 0, items = 0, submitted = 0;
    ACTIVITIES.forEach(function (act, i) {
      var s = state[i]; if (s && s.a) submitted++;
      if (!act.g) return;
      var n = act.n || (s && s.t) || 1; items += n; if (s) right += Math.min(s.k, n);
    });
    set('cmi.core.score.raw', items ? Math.round(100 * right / items) : 0);
    set('cmi.core.score.min', 0); set('cmi.core.score.max', 100);
    var done = submitted === ACTIVITIES.length && reachedEnd, was = get('cmi.core.lesson_status');
    if (done) set('cmi.core.lesson_status', 'completed');
    else if (was !== 'completed' && was !== 'passed') set('cmi.core.lesson_status', 'incomplete');
    var entries = [];
    ACTIVITIES.forEach(function (act, i) {
      var s = state[i]; if (s && s.a) entries.push([i.toString(36), s.a.toString(36), s.c ? 1 : 0, s.k.toString(36), s.t.toString(36)].join('.'));
    });
    set('cmi.suspend_data', 'v1|' + (reachedEnd ? 1 : 0) + '|' + entries.join(','));
  }

  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function clock() { var d = new Date(); return pad(d.getHours()) + ':' + pad(d.getMinutes()) + ':' + pad(d.getSeconds()); }
  var KIND = { quiz: 'choice', multiple_choice: 'choice', multi_select: 'choice', true_false: 'true-false', fill_in_the_blank: 'fill-in',
    open_ended_answer: 'fill-in', matching: 'matching', ordering: 'sequencing', sorting: 'matching', custom: 'performance' };

  function writeInteraction(id, type, response, result, objectiveIndex) {
    var p = 'cmi.interactions.' + interactions++ + '.';
    set(p + 'id', id.replace(/[^A-Za-z0-9_\-.:]/g, '_').slice(0, 255));
    set(p + 'objectives.0.id', ACTIVITIES[objectiveIndex].id);
    set(p + 'time', clock());
    set(p + 'type', KIND[type] || 'performance');
    if (response) set(p + 'student_response', response);
    set(p + 'result', result);
  }
  function responseFor(type, item) {
    var r = String(item.response || '');
    if (type === 'true_false') return /^(v|t|true|1)$/i.test(r) ? 't' : 'f';
    if (type === 'quiz') return (r.match(/o(\d+)$/) || [0, '0'])[1];                         // option number
    if (type === 'multiple_choice') return r.toLowerCase().replace(/[^a-z0-9]/g, '').slice(0, 1) || '0';
    if (type === 'multi_select') return '1';
    return r.replace(/\s+/g, ' ').slice(0, 255);
  }

  document.addEventListener('adt:progress-updated', function (e) {
    var d = e.detail || {}, i = index[d.activityId]; if (i === undefined) return;
    var r = d.record || {}, sub = d.submission || {};
    state[i] = { a: r.attempts || 0, c: !!r.complete, k: r.correct || 0, t: r.total || 0 };
    if (sub.graded) {
      (sub.items || []).forEach(function (item) {
        if (!item.graded || item.result === 'empty') return;
        writeInteraction(d.activityId + '--' + item.itemId, sub.type, responseFor(sub.type, item), item.result === 'correct' ? 'correct' : 'wrong', i);
      });
    } else writeInteraction(d.activityId, sub.type, '', 'neutral', i);
    writeObjective(i); writeOverall(); API.LMSCommit('');
  });

  function visit(id) {
    if (id) { pageId = id; set('cmi.core.lesson_location', pageId); }
    if (pageId === LAST_PAGE) reachedEnd = true;
    writeOverall(); API.LMSCommit('');
  }
  visit(pageId);
  document.addEventListener('adt:page-changed', function (event) { visit(event && event.detail ? event.detail.sectionId : null); });

  window.addEventListener('beforeunload', function () {
    var s = Math.round((Date.now() - started) / 1000), h = Math.floor(s / 3600);
    set('cmi.core.session_time', (h < 10 ? '000' : h < 100 ? '00' : h < 1000 ? '0' : '') + h + ':' + pad(Math.floor(s / 60) % 60) + ':' + pad(s % 60));
    writeOverall(); API.LMSCommit(''); API.LMSFinish('');
  });
})();
