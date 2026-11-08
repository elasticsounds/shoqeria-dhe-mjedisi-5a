# Local book and design files

Extract the entire ZIP into one folder, then open `index.html` in that folder. Keep its subfolders together. The original ADT reader is retained. Nothing needs to be uploaded. The brand guide is `book-design/brand-guide.html`; the changes, evidence and remaining flags are linked there.

The supplied source PDF contains 50 physical pages. This book has all 107 sections of the supplied ADT, including its supplementary quizzes. Page 4 is a lined notes page; later chapters listed in the printed contents are outside the supplied sources.

## Rebuilding the fixed component library

With Node.js installed, open a terminal in `book-design`, run `npm install`, then `npm run build`. The build compiles the scoped Tailwind source and synchronizes the existing reader's offline HTML, dictionary and CSS cache with a new dependency version. It does not change grading or the original runtime scripts. Work on a backup before making future edits, and repeat browser/export checks after a rebuild.

Run `node rebuild-cache.cjs --check` to check the embedded page/dictionary/style copies without writing anything. For HTML or dictionary changes without recompiling CSS, run `node rebuild-cache.cjs` to synchronize them.

Non-quiz activity responses are saved locally in this browser on this device. Quiz selections are cleared whenever a quiz is opened. Browser storage settings, different browsers, and different hosting origins can affect saved responses. The source package had no cross-device response synchronization. The supplied narration mapping is empty and read-aloud is disabled.

The report records two exercise ambiguities for teacher review and the limits of automated accessibility and LMS checks. Original inputs remain preserved outside this repaired copy.
