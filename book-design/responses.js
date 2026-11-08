/* Activities start blank on every visit. Quiz grading remains in the reader runtime. */
(function () {
  if (window.__adt5aResetResponses) return;
  window.__adt5aResetResponses = true;

  var previousPage = null;

  function clearOldAnswers() {
    var prefixes = ['adt5a.responses.', 'adt5a.drawing.', 'qz002_new2:'];
    try {
      for (var i = localStorage.length - 1; i >= 0; i--) {
        var key = localStorage.key(i);
        if (key && prefixes.some(function (prefix) { return key.indexOf(prefix) === 0; })) {
          localStorage.removeItem(key);
        }
      }
    } catch (_) {}
  }

  function pageIdentity(root) {
    var meta = document.querySelector('meta[name="title-id"]');
    var section = root.querySelector('[data-section-id],[data-id],[data-correct-answers]');
    var sectionId = section && (
      section.getAttribute('data-section-id') ||
      section.getAttribute('data-id') ||
      section.getAttribute('data-correct-answers')
    );
    return (meta && meta.content ? meta.content : '') + '|' + (sectionId || '');
  }

  function clearActivity(root) {
    root.querySelectorAll('input:not([type="hidden"]), textarea, select').forEach(function (control) {
      control.setAttribute('autocomplete', 'off');
      if (control.type === 'radio' || control.type === 'checkbox') {
        control.checked = false;
        control.removeAttribute('checked');
      } else if (control.tagName === 'SELECT') {
        control.selectedIndex = -1;
      } else {
        try { control.value = ''; } catch (_) {}
      }
    });

    root.querySelectorAll('[role="radio"], [role="checkbox"], .activity-option').forEach(function (option) {
      if (option.matches('[role="radio"], [role="checkbox"]') || option.hasAttribute('aria-checked')) {
        option.setAttribute('aria-checked', 'false');
      }
      option.removeAttribute('aria-invalid');
      option.classList.remove(
        'selected-option', 'correct-option', 'incorrect-option', 'ring-2', 'ring-blue-400',
        'bg-blue-50', 'bg-green-50', 'bg-red-50', 'border-green-500', 'border-red-500'
      );
      if (option.hasAttribute('data-mc-style-state')) {
        option.style.borderColor = '';
        option.style.outline = '';
        option.style.outlineOffset = '';
        option.style.backgroundColor = '';
        option.removeAttribute('data-mc-style-state');
      }
      option.querySelectorAll('[data-mc-status-badge]').forEach(function (badge) { badge.remove(); });
      var feedback = option.querySelector('.feedback-container');
      if (feedback) {
        feedback.classList.add('hidden');
        var text = feedback.querySelector('.feedback-text');
        if (text) {
          text.textContent = '';
          text.className = 'feedback-text';
        }
      }
    });
    root.querySelectorAll('[aria-pressed="true"]').forEach(function (button) {
      button.setAttribute('aria-pressed', 'false');
    });
  }

  function resetIfVisited(force) {
    var root = document.querySelector('#content.book');
    if (!root) return;
    var id = pageIdentity(root);
    if (force || id !== previousPage) {
      clearActivity(root);
      previousPage = id;
    }
  }

  clearOldAnswers();
  resetIfVisited(true);
  document.addEventListener('adt:page-changed', function () { resetIfVisited(true); });
  window.addEventListener('pageshow', function () { resetIfVisited(true); });

  new MutationObserver(function () { resetIfVisited(false); }).observe(document.documentElement, {
    subtree: true,
    childList: true,
    attributes: true,
    attributeFilter: ['content', 'data-section-id', 'data-id']
  });
})();
