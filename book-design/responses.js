/* Book-scoped persistence only. The original runtime remains responsible for grading. */
(function () {
  if (window.__adt5aResponses) return;
  window.__adt5aResponses = true;
  var prefix = 'adt5a.responses.f7bf719411a7c7cf.';
  var restored = new WeakMap();
  var restoring = false;
  var pending = false;
  function current() {
    var root = document.querySelector('#content.book');
    var meta = document.querySelector('meta[name="title-id"]');
    if (!root || !meta) return null;
    var section = root.querySelector('[data-section-id],[data-correct-answers]');
    var id = section && (section.getAttribute('data-section-id') || section.getAttribute('data-id'));
    if (id !== meta.content) return null;
    return {root: root, id: id};
  }
  function controls(root) { return Array.from(root.querySelectorAll('input:not([type=hidden]),textarea,select')); }
  function key(el, index) { return el.id || el.getAttribute('data-activity-item') || el.name + ':' + index; }
  function clearQuiz(quiz) {
    quiz.querySelectorAll('[role="radio"], label.activity-option').forEach(function (option) {
      option.classList.remove('selected-option', 'ring-2', 'ring-blue-400', 'bg-blue-50', 'bg-green-50', 'bg-red-50', 'border-green-500', 'border-red-500');
      option.removeAttribute('aria-invalid');
      option.setAttribute('aria-checked', 'false');
      option.style.borderColor = '';
      option.style.outline = '';
      option.style.outlineOffset = '';
      option.style.backgroundColor = '';
      option.querySelectorAll('input[type="radio"]').forEach(function (input) { input.checked = false; });
      var feedback = option.querySelector('.feedback-container');
      if (feedback) {
        feedback.classList.add('hidden');
        var text = feedback.querySelector('.feedback-text');
        if (text) {
          text.textContent = '';
          text.className = 'feedback-text';
        }
      }
      option.querySelectorAll('[data-mc-status-badge]').forEach(function (badge) { badge.remove(); });
      option.querySelectorAll('.validation-mark').forEach(function (mark) { mark.classList.add('hidden'); });
    });
  }
  function clearSavedQuizResponse(id) {
    try { localStorage.removeItem(prefix + id); } catch (_) {}
  }
  function save() {
    if (restoring) return;
    var page = current();
    if (!page) return;
    if (page.root.querySelector('[data-correct-answers]')) return;
    var values = {};
    controls(page.root).forEach(function (el, index) {
      if (['password', 'file'].includes(el.type)) return;
      var quizLabel = el.closest('label[role=radio]');
      values[key(el, index)] = el.type === 'radio' || el.type === 'checkbox' ? {checked: quizLabel ? quizLabel.getAttribute('aria-checked') === 'true' : el.checked} : {value: el.value};
    });
    try { localStorage.setItem(prefix + page.id, JSON.stringify(values)); } catch (_) {}
  }
  function restore() {
    pending = false;
    var page = current();
    if (!page || getComputedStyle(page.root).opacity !== '1') return;
    var quiz = page.root.querySelector('[data-correct-answers]');
    if (quiz) {
      clearSavedQuizResponse(page.id);
      clearQuiz(quiz);
      restored.set(page.root, page.id);
      page.root.dataset.responsesReady = page.id;
      return;
    }
    if (restored.get(page.root) === page.id) return;
    var values;
    try { values = JSON.parse(localStorage.getItem(prefix + page.id) || '{}'); } catch (_) { values = {}; }
    restored.set(page.root, page.id);
    restoring = true;
    controls(page.root).forEach(function (el, index) {
      var entry = values[key(el, index)];
      if (!entry) return;
      if ('checked' in entry) {
        el.checked = entry.checked;
      } else if (typeof entry.value === 'string') el.value = entry.value;
    });
    restoring = false;
    page.root.dataset.responsesReady = page.id;
  }
  function schedule() {
    if (pending) return;
    pending = true;
    setTimeout(restore, 80);
  }
  document.addEventListener('input', function (event) { if (event.target.closest('#content.book')) save(); }, true);
  document.addEventListener('change', function (event) { if (event.target.closest('#content.book')) save(); }, true);
  document.addEventListener('click', function (event) {
    if (event.target.closest('#content.book label[role=radio]')) setTimeout(save, 0);
  }, true);
  document.addEventListener('keydown', function (event) { if (event.target.closest('#content.book label[role=radio]')) setTimeout(save, 0); }, true);
  document.addEventListener('adt:page-changed', function () {
    setTimeout(function () {
      var page = current();
      var quiz = page && page.root.querySelector('[data-correct-answers]');
      if (!page || !quiz) return;
      clearSavedQuizResponse(page.id);
      clearQuiz(quiz);
      restored.set(page.root, page.id);
      page.root.dataset.responsesReady = page.id;
    }, 0);
  });
  window.addEventListener('pagehide', save);
  new MutationObserver(schedule).observe(document.documentElement, {subtree:true,childList:true,attributes:true,attributeFilter:['class','content','data-section-id']});
  schedule();
})();
