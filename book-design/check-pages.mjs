#!/usr/bin/env node
/* Browser checks for reader pages. Needs Playwright (npm i playwright in any folder, then run with
 * NODE_PATH=<that folder>/node_modules) and a local server: python3 -m http.server 8765 (from the bundle root).
 *
 *   node book-design/check-pages.mjs pg051 pg052            page checks for ids starting with these prefixes
 *   node book-design/check-pages.mjs all                    every page
 *   … --shots <dir>                                         also save full-page screenshots (1280 and 390)
 *   … --walk                                                dock walk of the whole book + save/restore of every field
 *
 * Page checks (1280, 820, 390 wide): only Poppins; nothing under 20px (cover excepted); no horizontal scroll;
 * visible form fields are Poppins >= 20px; glossary highlighting keeps word spacing; no text element with a
 * data-id is flex/grid (read-aloud would move its words); no page errors. Exit code 1 if anything fails.
 */
import { createRequire } from 'node:module'
import fs from 'node:fs'
const require = createRequire(import.meta.url)
let pw
try { pw = require('playwright') } catch (_) {
  const dir = (process.env.NODE_PATH || '').split(':').find((d) => d && fs.existsSync(d + '/playwright'))
  if (!dir) { console.error('Playwright not found: npm i playwright somewhere and set NODE_PATH=<folder>/node_modules'); process.exit(2) }
  pw = require(dir + '/playwright')
}
const { chromium } = pw
const BASE = process.env.BASE || 'http://localhost:8765/'
const args = process.argv.slice(2)
const shots = args.includes('--shots') ? args[args.indexOf('--shots') + 1] : null
const walk = args.includes('--walk')
const prefixes = args.filter((a, i) => !a.startsWith('--') && args[i - 1] !== '--shots')
const spine = (await (await fetch(BASE + 'content/pages.json')).json()).map((p) => p.href)
// prefixes match pages in the reading order; for preview pages not merged yet, matching files on disk are used
const onDisk = fs.readdirSync(new URL('..', import.meta.url)).filter((f) => /^(pg|qz)\d+.*\.html$/.test(f)).sort()
const pages = prefixes.includes('all') ? spine : [...new Set([...spine, ...onDisk])].filter((h) => prefixes.some((p) => h.startsWith(p)))
const glossary = await (await fetch(BASE + 'content/i18n/sq/glossary.json')).json()
if (shots) fs.mkdirSync(shots, { recursive: true })
const browser = await chromium.launch()
const problems = []
const note = (page, w, msg) => problems.push(`${page} @${w}: ${msg}`)

for (const w of pages.length ? [1280, 820, 390] : []) {
  const p = await browser.newPage({ viewport: { width: w, height: 900 } })
  let errs = []; p.on('pageerror', (e) => errs.push(e.message.slice(0, 120)))
  for (const href of pages) {
    errs = []
    await p.goto(BASE + href, { waitUntil: 'networkidle' }).catch(() => {})
    await p.waitForTimeout(350)
    const r = await p.evaluate((gl) => {
      const c = document.querySelector('#content'); if (!c) return { missing: true }
      c.querySelectorAll('details').forEach((d) => (d.open = true))
      const out = { small: [], fonts: new Set(), fields: [], flex: [], spacing: [] }
      const hidden = (el) => el.closest('.sr-only,[hidden]') || getComputedStyle(el).visibility === 'hidden'
      const tw = document.createTreeWalker(c, NodeFilter.SHOW_TEXT)
      while (tw.nextNode()) {
        const t = tw.currentNode, el = t.parentElement
        if (!t.textContent.trim() || hidden(el)) continue
        const r = el.getBoundingClientRect(); if (!r.width && !r.height) continue
        const cs = getComputedStyle(el); out.fonts.add(cs.fontFamily.split(',')[0].replace(/["']/g, '').trim())
        if (parseFloat(cs.fontSize) < 20) out.small.push(`${Math.round(parseFloat(cs.fontSize))}px "${t.textContent.trim().slice(0, 24)}"`)
      }
      for (const f of c.querySelectorAll('input:not([type=radio]):not([type=checkbox]):not([type=file]),textarea')) {
        if (!f.offsetParent) continue
        const cs = getComputedStyle(f)
        if (parseFloat(cs.fontSize) < 20 || !/Poppins/.test(cs.fontFamily)) out.fields.push(`${f.id || f.name} ${cs.fontSize} ${cs.fontFamily.split(',')[0]}`)
      }
      for (const el of c.querySelectorAll('[data-id]')) {
        if (el.tagName === 'IMG' || !el.textContent.trim()) continue
        if (/flex|grid/.test(getComputedStyle(el).display)) out.flex.push(el.getAttribute('data-id'))
      }
      // simulate glossary highlighting (one span per term) and compare rendered text with DOM text
      const vars = Object.values(gl).flatMap((v) => v.variations || [v.word]).sort((a, b) => b.length - a.length)
      const re = new RegExp('(?<![\\p{L}])(' + vars.map((v) => v.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|') + ')(?![\\p{L}])', 'giu')
      const nodes = []; const tw2 = document.createTreeWalker(c, NodeFilter.SHOW_TEXT)
      while (tw2.nextNode()) { const t = tw2.currentNode; if (t.parentElement.closest('h1,h2,h3,h4,script,style')) continue; if (re.test(t.textContent)) nodes.push(t); re.lastIndex = 0 }
      for (const t of nodes) {
        const f = document.createDocumentFragment(); let last = 0; const s = t.textContent
        s.replace(re, (m, _, i) => { f.appendChild(document.createTextNode(s.slice(last, i))); const sp = document.createElement('span'); sp.className = 'glossary-term'; sp.style.font = 'inherit'; sp.textContent = m; f.appendChild(sp); last = i + m.length })
        f.appendChild(document.createTextNode(s.slice(last))); t.parentNode.replaceChild(f, t)
      }
      for (const el of c.querySelectorAll('*')) {
        if (!el.querySelector(':scope > .glossary-term') || hidden(el)) continue
        const dom = el.textContent.replace(/\s+/g, ' ').trim(), vis = el.innerText.replace(/\s+/g, ' ').trim()
        if (vis && dom !== vis) out.spacing.push(vis.slice(0, 40))
      }
      out.fonts = [...out.fonts]; out.hscroll = document.documentElement.scrollWidth > innerWidth + 1
      return out
    }, glossary)
    if (r.missing) { note(href, w, 'no #content'); continue }
    const cover = href.startsWith('pg001')
    if (r.small.length && !cover) note(href, w, `text under 20px: ${[...new Set(r.small)].slice(0, 4).join(', ')}`)
    const odd = r.fonts.filter((f) => f !== 'BookPoppins'); if (odd.length) note(href, w, `fonts: ${odd.join(', ')}`)
    if (r.hscroll) note(href, w, 'horizontal scroll')
    if (r.fields.length) note(href, w, `fields: ${r.fields.slice(0, 3).join('; ')}`)
    if (r.flex.length) note(href, w, `flex/grid text elements: ${r.flex.slice(0, 4).join(', ')}`)
    if (r.spacing.length) note(href, w, `glossary spacing: ${r.spacing.slice(0, 2).join(' | ')}`)
    if (errs.length) note(href, w, `page errors: ${[...new Set(errs)].slice(0, 2).join(' | ')}`)
    if (shots && w !== 820) { await p.goto(BASE + href, { waitUntil: 'networkidle' }); await p.waitForTimeout(300); await p.screenshot({ path: `${shots}/${w}_${href.replace('.html', '')}.png`, fullPage: true }) }
  }
  await p.close()
}
if (pages.length) console.log(`page checks: ${pages.length} pages x 3 widths, ${problems.length} problems`)

if (walk) {
  const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } }); const p = await ctx.newPage()
  let errs = []; p.on('pageerror', (e) => errs.push(e.message.slice(0, 100)))
  const here = () => p.url().split('/').pop().split('?')[0].split('#')[0]
  const dock = async (label) => { await p.locator(`button[aria-label="${label}"]:visible`).first().click(); await p.waitForTimeout(1200) }
  await p.goto(BASE + spine[0], { waitUntil: 'networkidle' }); await p.waitForTimeout(1500)
  const seen = [here()]; for (let i = 1; i < spine.length; i++) { await dock('Faqja e ardhshme'); seen.push(here()) }
  const wrong = seen.filter((u, i) => u !== spine[i]).length
  console.log(`dock walk: ${seen.length}/${spine.length} pages, out of order: ${wrong}, errors: ${errs.length}`)
  if (wrong) problems.push(`dock walk: ${wrong} pages out of order`); if (errs.length) problems.push(`dock walk errors: ${[...new Set(errs)].slice(0, 3).join(' | ')}`)
  let total = 0, ok = 0
  for (let i = 0; i < spine.length - 1; i++) {
    const f = spine[i]; if (f.startsWith('qz')) continue
    await p.goto(BASE + f, { waitUntil: 'networkidle' }); await p.waitForTimeout(900)
    const filled = await p.evaluate(() => {
      document.querySelectorAll('#content details').forEach((d) => (d.open = true)); const out = [], seen = new Set()
      document.querySelectorAll('#content input, #content textarea').forEach((el, k) => {
        if (el.closest('#simple-main') || ['file', 'hidden', 'button', 'submit'].includes(el.type) || el.disabled) return
        if (el.type === 'radio') { if (seen.has(el.name)) return; seen.add(el.name); el.click(); out.push({ id: el.id, name: el.name, kind: 'radio', v: el.value }); return }
        if (el.type === 'checkbox') { el.click(); out.push({ id: el.id, kind: 'checkbox', v: true }); return }
        const v = el.maxLength > 0 && el.maxLength < 3 ? 'A' : el.tagName === 'TEXTAREA' ? 'test ' + k + '\nrreshti 2' : 'test ' + k
        el.focus(); el.value = v; el.dispatchEvent(new Event('input', { bubbles: true })); out.push({ id: el.id, kind: 'text', v })
      }); return out
    })
    if (!filled.length) continue
    await dock('Faqja e ardhshme'); await dock('Faqja e mëparshme'); await p.waitForTimeout(400)
    const res = await p.evaluate((fs) => fs.map((x) => {
      const el = x.id ? document.getElementById(x.id) : null; if (!el) return false
      if (x.kind === 'radio') { const c = document.querySelector(`input[name="${x.name}"]:checked`); return !!c && c.value === x.v }
      return x.kind === 'checkbox' ? el.checked === true : el.value === x.v
    }), filled)
    total += res.length; ok += res.filter(Boolean).length
    if (res.some((x) => !x)) problems.push(`${f}: ${res.filter((x) => !x).length} fields not restored`)
  }
  console.log(`save/restore after dock round trip: ${ok}/${total} fields`)
}
await browser.close()
if (problems.length) { console.log(problems.join('\n')); process.exit(1) }
console.log('all checks passed')
