# Changes and validation

Complete repaired Part 1: 50 physical PDF pages inventoried, 107 ADT sections mapped, 20 fixed page families applied. Original ZIP and untouched baseline preserved.

## What changed

- Source Poppins/Amiri typography, purple lesson bands, cyan/green/yellow panels, orange practice rules, responsive figures and tables.
- Real cover layout and logos; page 6 vector scene; source rubric icons; exact crossword diagram; corrected image descriptions and section headings.
- Fixed Tailwind source, compiled CSS, licensed fonts, brand guide and 20 actual-content examples under book-design/. No added global preflight.
- Activity reset adapter clears answers and selections on every page visit; no response persistence remains. Quiz grading logic and runtime scripts are preserved. Page 14 has a direct link to page 15 if the reader navigation control is unavailable.

## Current repair check · 2026-11-08

- Static audit of the current 81-entry navigation manifest: every target file exists, page IDs and order match, and no local HTML asset references are broken.
- The embedded offline cache is synchronized with the page files and checked by `npm run check:cache`.
- Verified by code inspection that the page 14 next-link target exists and that answer restoration/storage hooks have been removed.
- A live browser walkthrough was unavailable in this repair run because the browser security policy blocked opening the local `file:` URL. The current repair has not been re-certified at desktop and phone widths.

## Earlier browser evidence

- The prior evidence file records 428 layout checks, 107-section Next/Back walks, contents jumps, quiz retry, and saved-response checks. It predates this reset change; its saved-response results do not describe the current behavior.
- All 362 original control identities, binding IDs, section identities, reading order, grading payloads and original non-cache scripts preserved; local references and embedded caches checked.
- Exported ZIP reopening results are recorded separately in export-verification.json.

## Remaining flags

- **E-01 · Teacher review:** The original generated letter-entry grid has different cell counts/offsets from the source diagram, including Albanian digraph treatment. The exact source grid is restored and the six full-word response fields are primary. Legacy letter controls remain in a separate expandable area with IDs/names/values preserved and support up to two characters. No answer key or letter-to-cell grading was invented.
- **E-02 · Teacher review:** The original source asks for official languages and provides three response lines without specifying the intended scope. The original prompt and open response controls are preserved. A teacher should confirm the expected response count/scope; no new answer was supplied.
- **H-01 · Human validation remaining:** Live screen-reader/assistive-technology use, classroom pedagogical review, and SCORM 1.2 operation in the target LMS were not certified by these browser checks.
- **P-01 · Provenance limitation:** For retained original raster crops of vector artwork, exact historical extraction coordinates are unavailable where explicitly null in the ledger. Their physical source pages and appearance were visually checked. Every newly extracted figure has recorded crop coordinates or source vector bounds.
- **S-01 · Source scope, intentional:** Physical page 4 is lined notes stationery. Contents references to pages 53–101 are outside the supplied 1–50 PDF/Part 1 ADT. No missing later lessons or publication details were fabricated.

This is an evidence-backed repair and browser verification, not a complete accessibility, pedagogical or LMS certification.
