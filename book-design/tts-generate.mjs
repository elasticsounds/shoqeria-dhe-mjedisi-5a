#!/usr/bin/env node
/* Fast local TTS for this ADT bundle — same Gemini 3.8 request as ADT Speech Studio
 * (packages/tts/src/provider.ts, branch tts-cost-confirmation), run with real concurrency.
 *
 *   node book-design/tts-generate.mjs --dry-run              counts + cost estimate, no API calls
 *   GEMINI_API_KEY=… node book-design/tts-generate.mjs       generate missing/changed clips
 *
 * Options
 *   --lang sq              language folder (default: config default)
 *   --model gemini-3.8-flash-tts | gemini-3.8-flash-lite-tts
 *   --voice Kore           Gemini voice (studio default)
 *   --instructions "…"     delivery/style instructions (studio "speech_metadata" style)
 *   --temperature 1        optional, as in the studio
 *   --concurrency 8        parallel requests (auto-reduced on rate limits)
 *   --only pg012,gl001     only ids starting with these prefixes
 *   --skip-easy-read       leave *_easy_read entries out
 *   --limit 10             stop after N clips (try a sample first)
 *   --force                regenerate even if a matching clip exists
 *   --bitrate 64k          MP3 bitrate (mono)
 *   --cache <dir>          WAV cache (default ~/.cache/adt-tts/<bundle folder name>)
 *   --key-file <path>      key file outside the bundle (default ~/.config/adt-tts/gemini-key)
 *   --out <dir>            sample mode: write MP3s to this folder only (book audio and audios.json untouched)
 * Output: content/i18n/<lang>/audio/<id>.mp3 and audios.json (<id> → <id>.mp3).
 * Cache: ~/.cache/adt-tts/<bundle>/<signature>.wav (signature = text + model + voice + instructions + temperature),
 * so re-runs only call the API for new or changed text. Afterwards: node book-design/rebuild-cache.cjs
 */
import fs from 'node:fs/promises'
import { existsSync } from 'node:fs'
import path from 'node:path'
import os from 'node:os'
import crypto from 'node:crypto'
import { execFile } from 'node:child_process'
import { promisify } from 'node:util'
import { fileURLToPath } from 'node:url'

const run = promisify(execFile)
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const API = process.env.GEMINI_API_BASE || 'https://generativelanguage.googleapis.com/v1beta'

// ---------- options ----------
const argv = process.argv.slice(2)
const flag = (n) => argv.includes(`--${n}`)
const opt = (n, d) => { const i = argv.indexOf(`--${n}`); return i >= 0 && argv[i + 1] !== undefined ? argv[i + 1] : d }
const config = JSON.parse(await fs.readFile(path.join(ROOT, 'assets/config.json'), 'utf8'))
const O = {
  lang: opt('lang', config.languages?.default || 'sq'),
  model: opt('model', 'gemini-3.8-flash-tts'),
  voice: opt('voice', 'Kore'),
  instructions: opt('instructions', ''),
  temperature: opt('temperature') !== undefined ? Number(opt('temperature')) : undefined,
  concurrency: Math.max(1, Math.min(32, Number(opt('concurrency', 8)))),
  only: (opt('only', '') || '').split(',').map((s) => s.trim()).filter(Boolean),
  skipEasy: flag('skip-easy-read'),
  limit: Number(opt('limit', 0)) || Infinity,
  force: flag('force'),
  dry: flag('dry-run'),
  bitrate: opt('bitrate', '64k'),
  cache: opt('cache', ''),
  out: opt('out', ''),
}
if (!/^gemini-3\.8-/.test(O.model)) { console.error('This script implements the Gemini 3.8 request; use --model gemini-3.8-flash-tts or gemini-3.8-flash-lite-tts.'); process.exit(2) }
if (!/^[a-zA-Z0-9._:-]+$/.test(O.voice)) { console.error('Invalid voice name.'); process.exit(2) }
// Google lists Albanian for gemini-3.8-flash-tts but not for the Flash-Lite model.
if (O.model === 'gemini-3.8-flash-lite-tts' && /^sq/i.test(O.lang)) { console.error('gemini-3.8-flash-lite-tts does not list Albanian as a supported language; use gemini-3.8-flash-tts.'); process.exit(2) }

// ---------- entries (same selection as the studio catalog) ----------
const dir = path.join(ROOT, 'content/i18n', O.lang)
const readJson = async (f, d = {}) => (existsSync(f) ? JSON.parse(await fs.readFile(f, 'utf8')) : d)
const texts = await readJson(path.join(dir, 'texts.json'))
const speech = await readJson(path.join(dir, 'speech_texts.json'))
const audios = await readJson(path.join(dir, 'audios.json'))
const decode = (s) => s.replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#39;/g, "'")
const plain = (s) => decode(s.replace(/<[^>]+>/g, ' ')).replace(/\s+/g, ' ').trim()
const sig = (text) => crypto.createHash('sha256').update(JSON.stringify(['speech-v2', O.lang, text.trim(), 'gemini', O.model, O.voice, O.instructions, O.temperature ?? null, 1, 'wav'])).digest('hex').slice(0, 32)
// The WAV cache lives outside the bundle so it is never zipped, shipped or committed with the book.
const audioDir = O.out ? path.resolve(O.out) : path.join(dir, 'audio'), cacheDir = O.cache ? path.resolve(O.cache) : path.join(os.homedir(), '.cache', 'adt-tts', path.basename(ROOT))
const manifestPath = path.join(cacheDir, `manifest-${O.lang}.json`)
const manifest = await readJson(manifestPath)          // id -> signature of the mp3 currently in audio/

let entries = Object.entries(texts).map(([id, t]) => {
  const s = Object.hasOwn(speech, id) ? speech[id] : (/<math[\s>]/i.test(t) ? '' : plain(t))
  return { id, text: (s || '').trim() }
}).filter((e) => e.text)
if (O.only.length) entries = entries.filter((e) => O.only.some((p) => e.id.startsWith(p)))
if (O.skipEasy) entries = entries.filter((e) => !e.id.endsWith('_easy_read'))
for (const e of entries) { e.sig = sig(e.text); e.mp3 = `${e.id}.mp3` }
const todo = entries.filter((e) => O.out || O.force || manifest[e.id] !== e.sig || !existsSync(path.join(audioDir, e.mp3))).slice(0, O.limit)

// ---------- cost estimate (studio formula, standard paid rates; promotional until 2027-01-01) ----------
function estimate(list) {
  const L = list.map((e) => e.text.length), C = L.reduce((a, b) => a + b, 0)
  const promo = Date.now() < Date.parse('2027-01-01T00:00:00Z')
  const textRate = promo ? 0.5 : 1, audioRate = (O.model === 'gemini-3.8-flash-lite-tts' ? 12 : 18) * (promo ? 0.5 : 1)
  const lo = L.reduce((s, n) => s + Math.max(0.5, (n * 60) / 1000), 0), hi = L.reduce((s, n) => s + Math.max(2, (n * 60) / 600), 0)
  const pc = C + list.length * (O.instructions.length + 40)
  return { clips: list.length, characters: C, hoursLow: lo / 3600, hoursHigh: hi / 3600, usdLow: ((pc / 4) * textRate + lo * 25 * audioRate) / 1e6, usdHigh: ((pc / 2) * textRate + hi * 25 * audioRate) / 1e6 }
}
// Identical texts are recorded once, so cost follows the unique texts still to record.
const uniqueTodo = [...new Map(todo.map((e) => [e.sig, e])).values()].filter((e) => !existsSync(path.join(cacheDir, `${e.sig}.wav`)))
const est = estimate(uniqueTodo)
console.log(`Book: ${entries.length} voiced entries (${O.lang}). To write now: ${todo.length} clips; ${est.clips} unique recordings to generate (${est.characters} characters, ~${est.hoursLow.toFixed(1)}–${est.hoursHigh.toFixed(1)} h audio).`)
console.log(`Model ${O.model}, voice ${O.voice}${O.instructions ? ', with instructions' : ''}${O.temperature !== undefined ? `, temperature ${O.temperature}` : ''}. Estimated cost $${est.usdLow.toFixed(2)}–$${est.usdHigh.toFixed(2)} (studio formula; cached clips cost nothing).`)
if (O.dry || !todo.length) { if (!todo.length) console.log('Nothing to do: every clip matches its text and settings.'); process.exit(0) }

// Key: GEMINI_API_KEY (or GOOGLE_API_KEY), else a key file outside the bundle (--key-file, default ~/.config/adt-tts/gemini-key).
// The key is only sent as the x-goog-api-key header; it is never printed or written anywhere.
const keyFile = opt('key-file', path.join(os.homedir(), '.config', 'adt-tts', 'gemini-key'))
if (path.resolve(keyFile).startsWith(ROOT + path.sep)) { console.error('Keep the key file outside the book folder so it is never committed or published.'); process.exit(2) }
const KEY = (process.env.GEMINI_API_KEY || process.env.GOOGLE_API_KEY || (existsSync(keyFile) ? (await fs.readFile(keyFile, 'utf8')).trim() : '')).trim()
if (!KEY) { console.error(`No key: set GEMINI_API_KEY in this terminal or create ${keyFile} (chmod 600). It is never printed or saved.`); process.exit(2) }
const redact = (m) => String(m).replaceAll(KEY, '[redacted]').replace(/AIza[A-Za-z0-9_-]{10,}/g, '[redacted]').slice(0, 300)

// ---------- audio helpers (from the studio provider) ----------
function pcmToWav(pcm, rate = 24000) {
  const h = Buffer.alloc(44); h.write('RIFF'); h.writeUInt32LE(36 + pcm.length, 4); h.write('WAVE', 8); h.write('fmt ', 12)
  h.writeUInt32LE(16, 16); h.writeUInt16LE(1, 20); h.writeUInt16LE(1, 22); h.writeUInt32LE(rate, 24); h.writeUInt32LE(rate * 2, 28)
  h.writeUInt16LE(2, 32); h.writeUInt16LE(16, 34); h.write('data', 36); h.writeUInt32LE(pcm.length, 40); return Buffer.concat([h, pcm])
}
function decodeAudio(data, mime) {
  const bytes = Buffer.from(data, 'base64')
  if (bytes.toString('ascii', 0, 4) === 'RIFF') return bytes
  if (!/^audio\/(?:L16|pcm|x-pcm|raw)/i.test(mime || '')) throw new Error(`unsupported audio format ${mime}`)
  if (!bytes.length || bytes.length % 2) throw new Error('invalid PCM audio')
  return pcmToWav(bytes, Number((mime.match(/rate=(\d+)/i) || [])[1] || 24000))
}

// ---------- adaptive concurrency ----------
let limit = O.concurrency, active = 0, pausedUntil = 0, okStreak = 0
const waiters = []
const sleep = (ms) => new Promise((r) => setTimeout(r, ms))
async function slot() {
  for (;;) {
    const wait = pausedUntil - Date.now()
    if (wait > 0) { await sleep(wait); continue }
    if (active < limit) { active++; return }
    await new Promise((r) => waiters.push(r))
  }
}
function release() { active--; const w = waiters.shift(); if (w) w() }
// One slowdown per burst of rate-limit responses (ease off by ~1/3), then recover step by step:
// +1 after 8 successes or 5 s without a rate limit, up to --concurrency.
let lastCut = 0, lastLimited = 0
function rateLimited(ms) {
  const now = Date.now(); lastLimited = now; okStreak = 0
  if (now - lastCut > 3000) { limit = Math.max(1, Math.ceil(limit * 0.67)); lastCut = now }
  pausedUntil = Math.max(pausedUntil, now + ms)
}
function grow() { if (limit < O.concurrency) { limit++; okStreak = 0; const w = waiters.shift(); if (w) w() } }
function succeeded() { if (++okStreak >= 8 || Date.now() - lastLimited > 5000) grow() }

async function synthesize(text) {
  const body = {
    model: O.model,
    input: [{ type: 'user_input', content: [{ type: 'text', text, ...(O.instructions ? { annotations: [{ type: 'speech_metadata', style: O.instructions }] } : {}) }] }],
    response_format: { type: 'audio' },
    generation_config: { speech_config: [{ voice: O.voice }], ...(O.temperature !== undefined ? { temperature: O.temperature } : {}) },
  }
  for (let attempt = 1; attempt <= 6; attempt++) {
    await slot()
    let res
    try {
      res = await fetch(`${API}/interactions`, { method: 'POST', headers: { 'Content-Type': 'application/json', 'x-goog-api-key': KEY }, body: JSON.stringify(body), signal: AbortSignal.timeout(120000) })
    } catch (e) {
      release(); if (attempt === 6) throw new Error('connection failed or timed out'); await sleep(1500 * attempt); continue
    }
    if (res.ok) {
      const payload = await res.json().finally(release)
      const audio = (payload.steps || []).filter((s) => s.type === 'model_output').flatMap((s) => s.content || []).filter((c) => c.type === 'audio' && typeof c.data === 'string').at(-1)
      if (!audio) throw new Error('Gemini returned no audio')
      succeeded()
      return decodeAudio(audio.data, audio.mime_type || audio.mimeType || 'audio/wav')
    }
    release(); await res.body?.cancel()
    if (res.status === 429 || res.status >= 500) {
      const ra = Number(res.headers.get('retry-after'))
      rateLimited(Number.isFinite(ra) && ra > 0 ? Math.min(ra * 1000, 60000) : 2500 * attempt)
      if (attempt < 6) continue
      throw new Error(res.status === 429 ? 'rate limit / quota reached' : `server error ${res.status}`)
    }
    if (res.status === 401 || res.status === 403) { const e = new Error('API key rejected or no access to this model'); e.fatal = true; throw e }
    throw new Error(`request rejected (HTTP ${res.status})`)
  }
}

async function toMp3(wavFile, mp3File) {
  const tmp = `${mp3File}.part.mp3`
  await run('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', '-i', wavFile, '-ac', '1', '-codec:a', 'libmp3lame', '-b:a', O.bitrate, tmp])
  await fs.rename(tmp, mp3File)
}

// ---------- run ----------
await fs.mkdir(audioDir, { recursive: true }); await fs.mkdir(cacheDir, { recursive: true })
let done = 0, cached = 0, failed = [], fatal = null
const t0 = Date.now()
const saveMaps = async () => {
  const sorted = Object.fromEntries(Object.entries(audios).sort(([a], [b]) => a.localeCompare(b)))
  await fs.writeFile(path.join(dir, 'audios.json'), JSON.stringify(sorted, null, 2) + '\n')
  await fs.writeFile(manifestPath, JSON.stringify(manifest, null, 2) + '\n')
}
let saveTimer = null
const queue = [...todo]
const inflight = new Map()   // signature -> promise of the recording being generated
async function worker() {
  while (queue.length && !fatal) {
    const e = queue.shift()
    const wav = path.join(cacheDir, `${e.sig}.wav`), mp3 = path.join(audioDir, e.mp3)
    try {
      // Identical texts share one recording: generate each signature once, others wait for it.
      if (existsSync(wav)) cached++
      else if (inflight.has(e.sig)) { await inflight.get(e.sig); cached++ }
      else {
        const job = (async () => { const audio = await synthesize(e.text); const part = `${wav}.${process.pid}.${Math.random().toString(36).slice(2)}.part`; await fs.writeFile(part, audio); await fs.rename(part, wav) })()
        inflight.set(e.sig, job)
        try { await job } finally { inflight.delete(e.sig) }
      }
      await toMp3(wav, mp3)
      if (!O.out) { audios[e.id] = e.mp3; manifest[e.id] = e.sig } done++
      if (!O.out && !saveTimer) saveTimer = setTimeout(async () => { saveTimer = null; await saveMaps() }, 2000)
    } catch (err) {
      if (err.fatal) fatal = err
      failed.push({ id: e.id, error: redact(err.message) })
    }
    const n = done + failed.length
    if (n % 25 === 0 || n === todo.length) {
      const s = (Date.now() - t0) / 1000
      console.log(`${n}/${todo.length}  ok ${done} (cached ${cached})  failed ${failed.length}  ${(done / Math.max(s, 1) * 60).toFixed(0)} clips/min  concurrency ${limit}`)
    }
  }
}
await Promise.all(Array.from({ length: O.concurrency }, worker))
clearTimeout(saveTimer); if (!O.out) await saveMaps()
const secs = ((Date.now() - t0) / 1000).toFixed(0)
console.log(`Finished in ${secs}s: ${done} clips written (${cached} from cache), ${failed.length} failed.`)
if (fatal) console.error(`Stopped: ${redact(fatal.message)}`)
if (failed.length) {
  await fs.writeFile(path.join(cacheDir, `failed-${O.lang}.json`), JSON.stringify(failed, null, 2))
  console.log(`Failed ids saved to ${path.join(cacheDir, `failed-${O.lang}.json`)}; run the same command again to retry only those.`)
}
console.log('Next: node book-design/rebuild-cache.cjs  (and enable "readAloud" in assets/config.json to show the read-aloud controls)')
process.exit(fatal ? 1 : 0)
