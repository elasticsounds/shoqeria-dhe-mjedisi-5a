# SCORM activity tracking for ADT bundles — feature spec

Status: proposal, not implemented. Written 2026-11-15 from work on the bundle *Shoqëria dhe mjedisi 5A*
(226 reader pages, 42 activity pages, packaged as one SCORM 1.2 SCO).

## 1. Goal

A teacher looking at the LMS report for one pupil should be able to see:

1. **Current page** — where the pupil is in the book.
2. **Completion per activity** — which activities the pupil has submitted.
3. **Result per activity** — right or wrong, for activities that have an answer key.
4. **Number of attempts per activity** — activities with a key let the pupil self-correct and submit again, so the
   attempt count is part of the picture.
5. **An overall score and status** for the book.

Open-ended activities (no key) are tracked as *answered*, never as right or wrong.

## 2. What happens today

| Requirement | Today |
|---|---|
| Current page | Works. `scorm.js` writes `cmi.core.lesson_location` on load and on every `adt:page-changed`. |
| Completion per activity | Not reported. |
| Right / wrong per activity | Not reported. |
| Attempts | Not counted anywhere. |
| Overall score / status | Not working (see below). |

Details of the gap, from reading `assets/scorm.js` and `assets/base.bundle.local.js`:

- `scorm.js` embeds a fixed list of activity ids at generation time (`ALL_ACTIVITY_IDS`). In this bundle it holds only
  the 11 quiz ids (`qz001`…`qz011`); the 31 other activity pages are not in it.
- It derives the score from `localStorage['completedActivities']`. **Nothing in the runtime writes that key**, so the
  score stays 0 and the status stays `incomplete`. This was found by reading the code; it has not been confirmed in an
  LMS.
- The runtime has no outward signal when an activity is submitted. Each activity type keeps its result in internal
  state (it increments an internal success counter that fires the confetti), so `scorm.js` has nothing to listen to.
- Answers are kept in the browser's `localStorage` only. A pupil who changes device, or a shared classroom device,
  loses or mixes up answers; the LMS holds nothing.

## 3. Design

Three parts: the runtime announces submissions, a tracker records them, and the SCORM adapter reports them.

### 3.1 Runtime: one event per submit

Every activity type dispatches the same DOM event on `document` each time the pupil presses Submit (and when an
activity grades on selection, as quizzes do):

```js
document.dispatchEvent(new CustomEvent('adt:activity-submitted', { detail: {
  activityId: 'pg098_sec002',          // stable id: the section id (quiz pages: the quiz id)
  type: 'fill_in_the_blank',           // quiz | multiple_choice | multi_select | true_false | fill_in_the_blank |
                                       // open_ended_answer | matching | sorting | ordering | underline_text | custom
  graded: true,                        // false for open-ended and other activities without a key
  complete: true,                      // graded: all items correct; ungraded: every field accepted
  items: [                             // one entry per question / blank / option group
    { itemId: 'item-4', response: 'iliria', result: 'correct' },      // correct | wrong | neutral | empty
    { itemId: 'item-5', response: 'Kosova', result: 'wrong' }
  ],
  correct: 1, total: 3, empty: 1
} }));
```

Requirements:

- Fired on **every** submit, including unsuccessful ones, so attempts can be counted.
- Custom activities (`adtRegisterCustomActivity`) fire it too; `validate()` may return either a boolean (as now) or an
  object `{ complete, items }` so a custom activity can report its items.
- `activityId` must be stable across builds of the same book. Section ids are; generated `item-N` ids are stable only
  while the page's fields keep their order, so the build should not renumber them casually.

### 3.2 Tracker: per-activity record

A small module (part of the runtime, independent of SCORM) listens for the event and keeps one record per activity:

```json
{ "pg098_sec002": { "type": "fill_in_the_blank", "graded": true, "attempts": 3, "complete": true,
                    "firstCorrectAttempt": 3, "correct": 3, "total": 3, "lastSubmitted": "2026-11-15T10:42:00Z" } }
```

- `attempts` increases by one on every submit.
- `complete` latches: once true it stays true, even if the pupil later changes an answer.
- Stored in `localStorage` under a bundle-scoped key, and mirrored to the LMS (3.3) so it survives a device change.
- Exposes `window.adtProgress.get()` so a future in-book "my progress" view or teacher export can read it.

### 3.3 SCORM 1.2 mapping

| What the teacher sees | SCORM 1.2 element | Notes |
|---|---|---|
| Current page | `cmi.core.lesson_location` | As today. |
| Completion per activity | `cmi.objectives.n.id` = activity id, `cmi.objectives.n.status` = `not attempted` / `incomplete` / `completed` (ungraded) / `passed` (graded, all correct) | Objectives are readable, so they can be restored on resume. One objective per activity. |
| Score per activity | `cmi.objectives.n.score.raw` (0–100, share of items correct), `.min` 0, `.max` 100 | Graded activities only. |
| Each attempt, with right / wrong | `cmi.interactions.n.*`: `id`, `type`, `student_response`, `result`, `time`, `objectives.0.id` | Interactions are write-only and append-only in 1.2: write **one new interaction per item per attempt**. The LMS report then lists every attempt in order. |
| Attempt count | Number of interaction entries for an id; also stored in `cmi.suspend_data` | Most LMS reports do not total attempts themselves, so the count is also kept in suspend data for our own use. |
| Overall score | `cmi.core.score.raw` / `.min` / `.max` | See 3.4. |
| Overall status | `cmi.core.lesson_status` | See 3.4. |
| Time spent | `cmi.core.session_time` | Not written today; cheap to add. |
| Resume state | `cmi.suspend_data` | 4,096-character limit: store a compact map `id → attempts, complete, correct/total`, not answer text. |

Interaction details:

- `type`: `choice` (quiz, multiple choice, multi-select), `true-false`, `fill-in` (blanks and open-ended), `matching`,
  `sequencing` (ordering), `performance` (custom).
- `result`: `correct`, `wrong`, or `neutral` for open-ended answers. Never mark an open-ended answer correct or wrong.
- `student_response` is limited to 255 characters; long open-ended answers must be truncated. Decide in 5.2 whether
  open-ended text is sent at all.
- Call `LMSCommit` after each submit, not only on page change, so a closed tab does not lose the attempt.

### 3.4 Overall score and status

Proposed default, to be confirmed (5.1):

- **Score** = share of *graded* items answered correctly at the pupil's latest attempt, across the whole book (0–100).
  Open-ended activities do not affect it.
- **Status** = `completed` when every activity (graded and open-ended) has been submitted at least once and the last
  page has been reached; otherwise `incomplete`. Use `passed` / `failed` only if a mastery score is set in the
  manifest.
- The list of activities and their item counts is generated at build time from the pages (replacing the hand-kept
  `ALL_ACTIVITY_IDS`), so new activity pages are counted automatically.

### 3.5 Pupil-facing behaviour

- Every page with answer fields has the Submit button, including open-ended ones.
- Open-ended feedback is neutral: a "your answers have been saved" message, no green tick, no "correct" wording, no
  right/wrong sound. Empty fields get a gentle reminder only.
- Graded feedback stays as it is (tick or cross per item, popup with counts, sounds), and the pupil may retry without
  limit. Each retry is one attempt.
- The existing interface string `answers-submitted` says the answers were sent to the teacher. It should only be
  shown when that is true (inside an LMS, after a successful commit).

## 4. Work items

| # | Item | Where |
|---|---|---|
| 1 | Dispatch `adt:activity-submitted` from every activity type and from custom activities | Runtime (`base.bundle`) |
| 2 | Tracker module with attempts, latching completion, `window.adtProgress` | Runtime |
| 3 | Generate the activity manifest (ids, types, graded, item counts) at build time | ADT Studio packaging |
| 4 | Rewrite the SCORM adapter: objectives, interactions, suspend data, session time, commit on submit | `scorm.js` generator |
| 5 | Restore from `cmi.suspend_data` / objectives on launch, so progress follows the pupil across devices | `scorm.js` generator |
| 6 | Neutral feedback mode for open-ended activities | Runtime |
| 7 | Test matrix: Moodle and at least one other LMS; resume; two pupils on one device; offline use | QA |

For this book only, items 1–2 can be approximated before the runtime changes: the bundle's own
`book-design/responses.js` can observe the Submit button and the activity's state. That is a stop-gap, not the design.

## 5. Open questions

1. **Score definition.** Is the proposal in 3.4 right, or should the score be "share of activities completed"?
   Should first-attempt correctness be reported separately from eventual correctness?
2. **Open-ended answer text.** Should the pupil's written answers be sent to the LMS (truncated to 255 characters),
   or only the fact that they answered? This is pupil-written personal data and LMS reports display it poorly.
3. **SCORM version.** 1.2 has the widest support but small limits (4,096-character suspend data, 255-character
   responses, write-only interactions). SCORM 2004 or xAPI/cmi5 would lift these; which LMSs must be supported?
4. **Objectives support.** Some LMSs ignore `cmi.objectives` in reports. If the target LMS does, per-activity
   completion has to be read from interactions instead.
5. **Scale.** A book with about 40 activities and unlimited retries can produce several hundred interaction entries
   per pupil. Check the target LMS's limits and report readability.
6. **Shared devices.** `localStorage` is per browser, not per pupil. Inside an LMS, should local answers be cleared or
   namespaced by `cmi.core.student_id` at launch?
7. **Quizzes.** Quizzes grade on selection and have no Submit. Does each selection count as an attempt?

## 6. Reference: activity pages in this bundle

| Type | Pages | Graded |
|---|---|---|
| `activity_quiz` | 11 | yes |
| `activity_open_ended_answer` | 20 | no |
| `activity_fill_in_the_blank` | 6 | yes (blanks without a key count as answered) |
| `activity_multiple_choice` | 2 | yes |
| `activity_multi_select` | 1 | yes |
| `activity_true_false` | 1 | yes |
| `activity_custom` (word search) | 1 | yes |
| Pages with answer fields but no activity type or Submit yet | about 90 | no |
