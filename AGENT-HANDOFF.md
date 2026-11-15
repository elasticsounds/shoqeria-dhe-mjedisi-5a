# Agent hand-off: Shoqëria dhe mjedisi 5A

A record of everything the book owner asked for in the restyle session (November 2026), the standards that came out of it, and what is still open. Read this together with `AGENTS.md`, which describes the bundle structure, and `book-design/CHANGES-AND-VALIDATION.md`, which is the change log.

---

## 1. Requests, in order

The owner's requests, close to their own words, with what was done.

1. **Book-wide typography.** "The PDF has a lot of different font types, is a bit messy, and the minimum font size is a bit too small. Set a minimum font size, clean up messy design and make the entire book look more consistent."
   → Two families only, 16px floor book-wide, canvas pages switch to flow layout below 900px, no justified text, unified ink colour (`book-design/normalize-typography.py`).
2. **Contents pages 2–3.** "Make this page and the next page consistent in style and font size. Add clickable links to each item for the page it links to."
   → Shared `.b-toc` list. Entries whose page is in this bundle link to it; later entries (53+, page 3 79–101) are outside the bundle and stay plain.
3. **Page 8 redesign.** "More inclusive, clean, friendly and better designed. There are too many fonts and font sizes. Let's standardise. The serif fonts should be sans serif and they are too small. I would target minimum font 20. The notebook is text on an image: transcribe the text in a font that is more accessible and readable and put it on the notebook again."
   → Poppins only; 32/22/20; the diary is real text on a CSS notebook (`.b-notebook`, ruled lines locked to the text, spiral rings from the source art).
4. **Keyword spaces and italic.** "Check the listed words (premtim, besim, etc.) don't have spaces between the words [missing]. For the handwritten you can use italic if this is ok for accessibility."
   → Glossary-highlight spacing bug fixed (no flex on text containers). Italic was *not* applied: a long italic passage is harder to read and Poppins has no bundled italic.
5. **Page 7.** "Change this page so the design is more similar to the sans-serif larger font look of pg008."
6. **Page 9 (sec001, sec002).** "Make these clean and follow a similar font style to pg008; keep the sections, just make it look better. The text input field and lines on the notepad don't line up: when you type it is small serif font, but it should be the same sans serif and fit on the lines."
   → The textarea itself carries the ruled lines (`background-attachment: local`), 22px Poppins on 44px lines.
7. **Title accessibility.** "The top purple section is not high-contrast enough. Make it a full-width purple heading bar with the darker high-contrast purple, or, if it looks better, a purple line across the top and the heading in purple text."
   → Chosen: a full-width purple line plus a purple heading (`.b-page-title`, #794282, 7.2:1 on white).
8. **Page 10 (butterfly).** "A similar thing with a yellow line across the top and remove the left bar. Restyle the header. Make sure the activity is accessible: text inputs with white backgrounds. The titles and inputs are too high and don't align with the image on desktop."
   → `.b-page-title.is-practice` (yellow); fields positioned as a % of the artwork, measured from the art; stacks below 900px.
9. **Page 11 table.** "Remove the yellow bar, restyle the table in the same friendly font. The table is so boring: add emojis to each line and make it more child-friendly."
10. **Page 11 star rating.** "Make pg011 [sec002] more appealing."
11. **Pages 12 and 15.** "Restyle these like pg008."
    → Shared lesson components (`.b-lesson*`) created.
12. **Quizzes qz001–qz011.** "Same nice styling, with a header that is obvious so you know it's always a quiz. Use the purple styling from pg011_sec002 and a light purple full-page background."
13. **Page 13 (then `qz002_new2`).** "Restyle this page in the same style." → Rebuilt as a real reader page from the dictionary.
14. **Pages from 14 on.** "Go through the book and update the pages with similar style changes: purple lines for chapters, yellow lines at the top for the activities with the yellow bars, font sizes etc. Only do the next 10 or 20 pages so I can check."
15. **Rename.** "This page should be pg013_sec001: rename the HTML and ensure it is in the nav order."
16. **Rename.** "Also rename qz003_new2.html to pg017 and ensure the nav is updated."
17. "Commit all our current changes."
18. **Saving answers.** "Entering text in text boxes doesn't save between pages. It should save to local storage, so going from page to page it loads your answers."
19. **SCORM question.** "We want to eventually integrate SCORM: will the quizzes be saved and uploaded into the system?" → Answered: not yet; see open items.
20. **Page 9.** "Remove the journal from this page; it should only be on the next page."
21. **Page 14.** "There are two text areas per question; they started as ruled lines but the system incorrectly made two text areas instead of one."
22. **Page 18.** "pg018_sec001 has the same multi-line issue."
23. **Pages 27–50.** "From pg027 clean up the remaining pages the way we have: design, fixing multi-line issues, ensuring the interactivity works."
24. "Remove the page numbers at the bottom of each page."
25. **Page 37 crossword.** "Question two is a crossword where you enter letters. Break this page into three sections by question. I have no idea how it validates; shouldn't this be a fill-in-the-blank or another way that validates?"
26. **Page 23.** "Split this page up; there are too many boxes on one page."
27. **Page 16.** "Split this page and put the archaeological sites onto a new section."
28. "Push the latest."
29. **Page 28.** "Split pg028_sec001 question three and put it on its own section."
30. **TTS.** "Regenerate the TTS to use the Gemini 3.8 TTS key. I set up https://github.com/elasticsounds/adt-speech-studio/ which lets you upload an ADT and regenerate it, but it's slow on the web. Use the same process but have it go faster."
31. **Accent.** "It's Albanian (Kosovo): will it direct Gemini 3.8 TTS to do it in that accent?"
32. "I don't speak with the Kosovo accent, so just test that it actually receives the instruction, then let's generate. Before we start, commit and push everything. Where is this repo?"
33. **New repo.** "Let's generate a new repository, write to that and push to GitHub Pages."
34. **Generate.** "Generate the TTS. Once it's finished, commit and push this online." The key was provided as a file (option B, `~/.config/adt-tts/gemini-key`).
35. **Read-aloud highlight.** "When the speech highlight plays on pg008 the words are separated or squashed together. It needs to just highlight and not modify the word positions."
36. "Upload this to GitHub."
37. "Generate a SCORM.zip file from this book."
38. "Push this to GitHub." → Code pushed; the zip attached to a GitHub Release (it is over the 100 MB git limit).
39. "Collect the entire chat, everything I asked, into a .md I can use for future updates to the agent." → This file.

---

## 2. Standards to keep

### Typography and colour
- **Font:** Poppins only (`var(--book-heading)`) on every restyled page. Amiri (serif) is retired from the restyled pages.
- **Sizes:**

  | Element | Desktop | Phone (≤700px) |
  |---|---|---|
  | Page title | 32px | 26px |
  | Rubric heading (Pyetje për ty, Diskuto, Thello dijet, …) | 28px | 24px |
  | Reading text, instructions | 22px | 20px |
  | Labels, captions, inputs, buttons | 20px | 20px |

  **Nothing below 20px**, apart from the cover credits (16px, kept on purpose; ask the owner before changing).
- **Colours:**

  | Use | Value |
  |---|---|
  | Purple ink (titles, borders, quiz header) | `#794282` |
  | Lesson purple (decorative only) | `#9b73b7` |
  | Practice yellow line | `#ffb149` |
  | Thought panel | cyan `#91cfdb` |
  | Discussion panel | green `#a1cf75` |
  | Research note | yellow `#fff4ce`, border `#c99a1e` |
  | Glossary panel | lavender `#ece2f3`, border `#c8b4d9` |
  | Quiz page background | `#f3ecf8` |
  | Ink | `--book-ink`, #231f20 |
  | Focus ring | `#075a70` |

  White text only on `#794282` or darker.
- **Lines:**
  - Lessons: a full-width purple top line (`.b-page-title`).
  - "Provoje veten" activities: a yellow line (`.b-page-title.is-practice`, dark heading plus the blocks icon `studio/assets/pg010_heading_tab.png`).
  - Continuation sections: the same line without a title (`.b-page-rule` / `.b-page-rule.is-practice`).
  - No side bars.
- **Never** use justified text, letter-spacing tricks, viewport-scaled type below the floor, or italic for long passages.

### Shared components (book-design/components.tailwind.css)
- **Page structure:**
  - `.b-page-title` (+ `-kicker` for a chapter line), `.b-page-rule`;
  - lesson root `#content.book.b-lesson`, practice root `+ .prx`.
- **Lesson parts:**
  - `.b-lesson-keywords`, `.b-lesson-text`, `.b-lesson-media` (`.is-reversed`), `.b-lesson-figure` (`.is-wide`);
  - `.b-lesson-gallery` (`--cols`, `.is-contain`, `.is-natural`), `.b-lesson-prompt`, `.b-lesson-list`.
- **Panels:** `.b-lesson-thought` (variants `.is-outlined`, `.is-research`, `.is-discussion`, `.is-glossary`).
- **Answers:**
  - `.b-lesson-answers` (fold-out answer fields);
  - practice tasks: `.prx-step`, `.prx-instruction`, `.prx-fields`, `.prx-field`;
  - one ruled answer box per question: `textarea.prx-lined` / `.b-lined`, `rows="4"`.
- **Other:** `.b-notebook` (diary), `.b-toc` (contents), quiz styles under `#content.book[data-family=quiz]`.
- After editing `components.tailwind.css`, build with `npx tailwindcss -i components.tailwind.css -o components.css --minify` in `book-design/` (needs `npm install`; remove `node_modules` afterwards).

### Rules learned the hard way
- **No flex or grid on any element that holds text with a `data-id`.** Glossary highlighting and read-aloud split that text into spans; in a flex or grid box the words lose their spaces or spread apart. Centre with `display:block; align-content:center` instead.
- **Form fields:** the global input rule has specificity (1,2,1), so page or component field rules need at least that, or fonts fall back to 17px. Measure the fields themselves; a text audit does not see empty inputs.
- **One answer box per question.** Where the PDF printed several ruled lines, merge them into one ruled textarea. Keep the first box's id and keys, and keep placeholder `data-id`s as sr-only. Don't merge genuinely separate fields (numbered sub-items, table cells, diagram regions).
- **Preserve the wiring:** every `data-id` that exists in `texts.json`, and every control's id, name, value, `data-activity-item`, `data-response-key` and `data-response-section`. Check before and after with a script.
- **Missing content:** if a PDF page's content exists in `texts.json` but no page shows it, restore it (as on pages 23, 39, 44, 49) and tell the owner.
- **Links:** in-book links must not do full page loads in an LMS; `responses.js` turns them into in-place page turns. Don't add plain cross-page links outside `<main>`.
- **Page scripts:** the reader re-runs only *inline* scripts on an in-place page turn. An external page script must be declared with `data-page-script="./path.js"` (loaded by `responses.js`) and must re-init on `adt:page-changed`.
- **Offline cache:** the cache (`assets/offline-preloader.js`) serves embedded copies of pages during in-place page turns, **even over HTTP**. After any page, JSON or CSS change, run `node book-design/rebuild-cache.cjs`, and check with `--check`.
- **Saving:**
  - Answers save to localStorage via `responses.js`, under `adt5a.responses.v1.<page id>`.
  - Use `data-response-page` for answers shared across pages (the page 9 diary) and `data-response-section` for sub-activities that reuse keys (page 24).
  - Quizzes are deliberately not saved. Every field needs a key that is unique on its page.
- **No "answers are saved on this device" notices** on individual pages. A single book-wide notice may come later.

### Workflows and tools
- **Rename a page:** do the steps by hand.
  1. `git mv` the file, then update its `title-id` meta and `data-section-id`;
  2. update `content/pages.json`, `content/toc.json` and `imsmanifest.xml`;
  3. rename the page's key in the offline cache, then rebuild the cache.
- **Split a page into sections:** `python3 book-design/split-section.py <page>.html --list` shows the top-level blocks; `… <page>.html <cut> [<cut>…]` splits. It updates the reading order, renumbers every `page-section-id` (1-based position in `pages.json`), and updates the manifest and cache keys. Then run `rebuild-cache.cjs`. If a moved heading has a contents entry, move that `toc.json` entry to the new section.
- **Typography normaliser:** `python3 book-design/normalize-typography.py`. It is idempotent; `--dry-run` previews.
- **TTS:** `node book-design/tts-generate.mjs`.
  - It uses the same Gemini 3.8 `interactions` request as ADT Speech Studio, with model `gemini-3.8-flash-tts` and voice `Kore`.
  - Options: `--dry-run` (cost), `--limit`, `--only`, `--out <dir>` (samples), `--skip-easy-read`, `--concurrency`.
  - Key: the `GEMINI_API_KEY` environment variable, or `~/.config/adt-tts/gemini-key`, which stays outside the repo and is never printed.
  - Cache: `~/.cache/adt-tts/<bundle>/`.
  - **Accent instruction used:**
    ```
    --instructions "Speak in standard Albanian as used in Kosovo schools, with a natural Kosovo Albanian pronunciation. Warm, clear and calm, at a steady pace for 10-year-old students."
    ```
  - Re-runs only record new or changed text. Flash-Lite does not list Albanian, so the script refuses it. Afterwards, rebuild the cache.
- **SCORM package:** `python3 book-design/build-scorm.py` writes `dist/Shoqeria-dhe-mjedisi-5A-SCORM.zip` (runtime files only; `dist/` is git-ignored) and regenerates the `imsmanifest.xml` file list. Publish the zip as a GitHub Release asset, not a git file.
- **Verify before reporting.** Use a headless browser (Playwright) with a local `python3 -m http.server`:
  - fonts and sizes at 1280, 820 and 390px;
  - no horizontal scroll;
  - field fonts;
  - glossary spacing (simulate the highlight wrapping);
  - a dock walk of every page in order;
  - save and restore every field after a dock round trip;
  - custom activities after a dock arrival;
  - read-aloud letter positions;
  - for SCORM: the unzipped package inside a fake SCORM 1.2 API frame, with no missing files, one session, and `lesson_location` updates.

### Repository and publishing
- **Local folder:** `/Users/eliasc/Dev/shoqeria-dhe-mjedisi-5a`. Work happens on branch **`book-restyle`**; `main` is the original.
- **Remotes:**
  - `elasticsounds` → https://github.com/elasticsounds/shoqeria-dhe-mjedisi-5a (private). This is where to push; `book-restyle` tracks it.
  - `origin` → `flamurbeqiraj/shoqeria-dhe-mjedisi-5a`. The `elasticsounds` account has no write access there.
- **Live site:** https://elasticsounds.github.io/shoqeria-dhe-mjedisi-5a/ (GitHub Pages from `book-restyle`, root, `.nojekyll`). It rebuilds on every push.
- **SCORM releases:** https://github.com/elasticsounds/shoqeria-dhe-mjedisi-5a/releases
- **Commits:** the owner asks for commits and pushes explicitly. Don't commit or push unprompted.

---

## 3. Open items and decisions waiting on the owner

- **SCORM reporting:**
  - score and status are always 0% / incomplete, because nothing writes `completedActivities`;
  - quiz answers are not sent as `cmi.interactions`;
  - written answers are not stored in `cmi.suspend_data` (SCORM 1.2 allows only ~4 KB);
  - local answers are not separated per learner on shared devices.

  Needs: the LMS and SCORM version, a quiz scoring rule, and whether teachers need to see written answers.
- **Shared devices:** saved answers stay in the browser, including page 10's name and birthday. Consider a "Fshi përgjigjet e mia" (clear my answers) button.
- **Accent review:** a Kosovo-Albanian speaker should listen to the narration. To change the voice, rerun `tts-generate.mjs` with new instructions (about $1.40–$2.40 for the whole book).
- **Answer-box consistency:** some pages show answer boxes inline, others behind a "Shkruaj përgjigjet" fold-out. The owner may want one rule.
- **Decisions to confirm with the owner:**
  - restored content (pages 23, 31, 39 with a new field `item-4`, 44, 49);
  - removed items: page 42's "Shiko fotografitë" link and page 27 sec002's duplicate Diskuto list;
  - page 43: three-bullet groups merged into one box each;
  - page 30: an extra box labelled "Vazhdim i përgjigjes";
  - page 37 crossword answer key: BUKA/BUKË, TURSHI, QUMËSHTI, FLIJA, MISHI, KUZHINA/KUZHINË, coloured column USHQIMI.
- **Source-text issues (unchanged):**
  - page 8 title "“Jam në klasën e pestë “" and the doubled comma "rritur, , si dhe";
  - page 25 stray comma;
  - page 39 "prefesion";
  - page 47 missing opening quotation mark;
  - page 35 food lists only inside images;
  - teacher flags E-01 (crossword source grid) and E-02 (page 46 official-languages scope).
- **Size:** the `studio/` editor history (~357 MB) is published on Pages; it could be removed from the published branch. `images/` (49 MB; `pg001_im001.png` alone is 8.7 MB) could be compressed if an LMS rejects the 150 MB package.
- **Speech Studio:** the hosted tool could be sped up by raising `MAX_CONCURRENT_JOBS` and the cap of 3, and lowering `PROVIDER_INTERVAL_MS`. A PR was offered, not made.
- **API key:** the Gemini key file is at `~/.config/adt-tts/gemini-key`. The owner may delete it when it's no longer needed.

---

## 4. Part 2 (PDF pages 51–102): how pages are built

The source PDF (`Shoqeria dhe mjedisi 5A.pdf`, 102 pages, git-ignored: 144 MB) is in the bundle root. Pages 51+ are built directly in the finished style from **page specs**, not converted from PDF layout.

- **Spec per PDF page:** `book-design/part2/specs/pgNNN.py`. Each spec calls the helpers in `book-design/part2/build.py` (`section`, `title`, `rule`, `keywords`, `panel`, `heading`, `items`, `text`/`para`, `figure`, `media`, `gallery`, `task`, `field`, `t`). See `pg051.py`–`pg055.py` for the pattern.
- **Build:** `python3 book-design/part2/build.py [page numbers]`, then `node book-design/rebuild-cache.cjs`. The build writes the section HTML files, allocates text ids (`pgNNN_n0001…`, image descriptions `pgNNN_im001…`), merges `texts.json` / `speech_texts.json` (including `_easy_read` versions), `pages.json`, `toc.json` and the cache keys, and renumbers `page-section-id`. Generated HTML must not be edited by hand; edit the spec.
- **Rules for specs:**
  - one section per question or topic (lesson start; Pyetje për ty; Diskuto; Thello dijet; each numbered Provoje veten task);
  - one `data-id` per sentence; easy-read text for every body sentence and question (not for headings);
  - an image description (alt) for every illustration or photo;
  - answer fields only where the PDF prints writing lines or boxes, one box per question (`field('lined')`), separate fields only for genuinely separate items;
  - fix PDF line-break hyphenation in the text ("Dri-tanit" → "Dritanit").
- **Images:** `python3.13 book-design/part2/crop.py <page> x0 y0 x1 y1 <out.png> [--erase box] [--flatten box]` cuts illustrations out of the PDF (coordinates in the 150-dpi page render, 1332×1805). Text printed over artwork is removed from the image and rendered as real text.
- **Checks:** `node book-design/check-pages.mjs <page prefixes…> [--shots dir] [--walk]` (needs Playwright via `NODE_PATH` and a local server on 8765).
- **Not done for part 2 yet:** quizzes (owner: not yet), narration for the new text (run `tts-generate.mjs` with the same instructions at the end), contents-page links for pages 53+, SCORM rebuild. The owner will confirm crossword / word-search answer keys.
- **Glossary:** the PDF's Fjalorthi (page 100) is merged; added gl132–gl136 (Dardani, NATO, shoqëri demokratike, UÇK, universale); the other entries already existed.

## 5. Reader activities in part 2 (added 2026-11-15)

Checked activities on pages 51–101 use the reader's own activity system (Submit button "Dërgo" above the bottom bar,
sounds, result popup, confetti), not page-local buttons. The reader handles **one activity type per page**, so a section
holds one kind only. Helpers in `book-design/part2/build.py`:

| Helper | Section type | Used on |
|---|---|---|
| `questions(...)` | `activity_open_ended_answer` (any real text accepted) | every "Pyetje për ty" panel, pp. 51–96 |
| `keyed(field, *answers)` / `open_answer(field)` | `activity_fill_in_the_blank` (key in an inline `window.correctAnswers` script) | pp. 78, 98, 99 |
| `choice(name, value, label, correct)` | `activity_multiple_choice` | pp. 94, 98 q1 |
| `tick(label, correct)` | `activity_multi_select` | p. 97 q2 |
| `section(..., stype='activity_true_false', answers={...})` | `activity_true_false` | p. 63 |
| `stype='activity_custom'` + `book-design/wordsearch.js` | custom activity registered with `window.adtRegisterCustomActivity` | p. 69 word search |

- `book-design/responses.js` still saves the answers; it also tells the reader about restored answers so "Dërgo" is enabled
  again after a page turn (see `syncChoices`).
- Albanian wording for the popups was added to `assets/interface_translations/sq/interface_translations.json`.
- Answer keys were derived from the lesson text and are **waiting for the owner's confirmation**: pp. 63, 67 (not built),
  69, 78, 97, 98, 99. Owner decisions already taken: p. 94 q3 option c reads "78 vjet" and is correct; underlining tasks
  (pp. 87, 89) became "write the words" boxes.
- Not done: narration (TTS) for pages 51–101 and for the new activity wording; quizzes for part 2; boxes for
  "Shpreh mendimin tënd" prompts; p. 67 logo-naming task has no checking.
