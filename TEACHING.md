# Session 2 — Teaching Guide: Static Todo List (HTML + CSS)

A complete, patch-by-patch project for a **3-hour workshop session**.
Target: newcomers + 2nd-year CS students. Pure HTML & CSS — no JavaScript
(today's build becomes the interactive Todo app in the next session).

---

## 1. The files

| File | Who uses it | Purpose |
|---|---|---|
| `index.html` + `style.css` | Instructor (+ reference) | **Version 2 — the demo file**: complete build cut into `▼ PATCH … ▲` blocks (non-accumulative: each block holds only its own patch) |
| `final/index.html` + `final/style.css` | Students | **Version 1 — the full website**: same code, all instructor banners stripped (the clean answer key) |
| `stages/patch1 … stages/patch4/` | Both | **Version 3 — accumulative checkpoints**: stage N = patches 1…N combined |
| `make-stages.py` | Instructor | Regenerates `final/` and `stages/` after you edit the demo file (`python3 make-stages.py`) |
| `starter/index.html` + `starter/style.css` | Students | Same frame, every patch section is a `TODO` with hints |
| `assets/logo.svg` | Both | The `<img>` example for HTML ch4 — the check-mark logo in the list card's header |
| `TEACHING.md` | Instructor & teammates | This script |

**The three versions at a glance**

1. **Full website** (`final/`) — the finished site, no scaffolding. Show it
   at the start ("this is what we're building") or hand it out as the key.
2. **Non-accumulative demo** (`index.html` + `style.css`) — one block per
   patch, each block contains *only* that patch's changes → delete one block,
   explain, Ctrl+Z, next patch.
3. **Accumulative stages** (`stages/patchN/`) — open `stages/patch2/` to show
   "the site exactly as it looks after Patch 2"; stage N always contains
   everything from the previous stages plus the new patch.

Open `index.html` in a browser (double-click works — no server needed) and keep
DevTools open (F12 → elements panel) so students can see the DOM while you edit.

## 2. The delete → explain → undo mechanic

Every concept lives in **one contiguous block**, marked by banners:

```html
<!-- ▼ PATCH 3 · HTML ch4 + ch5 (+ CSS ch4) -->
  …everything this patch adds…
<!-- ▲ END PATCH 3 -->
```

Demo loop (repeat per patch):

1. **Select** the block — from its `▼` banner line to its `▲` banner line
   (the banners are deleted with the block on purpose).
2. **Delete** → look at the browser → ask students: *what disappeared and why?*
3. **Explain** line by line what each deleted line was doing.
4. **Ctrl+Z** to restore (undo), refresh, confirm it's back.

Rules that keep the demo safe:

- Patches are **siblings inside `<body>`** — deleting any one leaves valid
  HTML and the rest of the page still renders.
- CSS blocks only style elements from the **same or an earlier** patch, so a
  deleted CSS block never "breaks" future blocks.
- The one exception: **Patch 1 part A is the whole frame** (`<head>`, `<body>`).
  Deleting it removes *everything* — that is the lesson of HTML ch1
  ("structure holds all content"). Do it once, explain, undo.
  For finer demos, delete single lines instead: the `<title>` line (tab name
  changes), the `<link>` line (all styling vanishes), the `<meta charset>` line.

## 3. Suggested timing (180 min)

| Block | Time | Content |
|---|---|---|
| Pre-Patch | 15 min | What is HTML, its role, basic syntax (slides → open the file) |
| Patch 1 | 25 min | HTML ch1 + ch2, CSS ch1 (Typography) |
| Break | 10 min | |
| Patch 2 | 40 min | HTML ch3, CSS ch2 + ch5 + ch3 + ch4 (the big visual jump) |
| Patch 3 | 40 min | HTML ch4 + ch5, CSS ch4 again (lists, links, media) |
| Patch 4 | 30 min | HTML ch6, CSS ch6 (form + motion) |
| Wrap-up | 15 min | Recap + hook for next session |
| Buffer | 10 min | Slowdowns, questions |

After **each patch**: give students 3–5 minutes to reproduce it in
`starter/` before moving on (workshop style). The final stretch (Patch 4 +
wrap-up) lets fast students do the `BONUS` media query.

---

## 4. The script

### Pre-Patch — "What is HTML?" *(slides first, then code)*

- **Slides:** HTML = the *structure* of a page; its role vs CSS (content vs
  looks); basic syntax: `<tag>attributes</tag>`, nesting, `name="value"`.
- **Code:** open `index.html`, walk the frame line by line (this frame also
  covers **HTML ch1 · Document Structure**):
  - `<!DOCTYPE html>` → tells the browser "this is modern HTML"
  - `<html lang="en">` → the root that encapsulates everything
  - `<head>` → invisible meta-information: `charset`, `viewport`, `title`, `link`
  - `<title>` → **micro-demo:** delete this line → tab name changes → undo
  - `<link rel="stylesheet">` → **micro-demo:** delete it → the whole page
    turns plain → undo (best "why do we need CSS" moment of the day)
  - `<body>` → everything visible lives inside it
- **Basic syntax drill:** point at `<h1 class="hero-title">` in the file —
  tag, closing tag, attribute, value. Show that CSS reaches it via the class.
- Note for the team: the guide assigns HTML ch1 to Patch 1; we walk the frame
  here because "basic syntax" needs a real file. Recap ch1 in 60 seconds when
  you reach the Patch 1 banner.

### Patch 1 — HTML ch1 (recap) + ch2 · CSS ch1 (Typography)

- **Slides:** `<h1>…<h6>`, `<p>`, `<span>` (inline container for styling part
  of a text); CSS properties: `color, font-size, font-family, font-weight,
  text-align, line-height, text-decoration`.
- **Delete demo:** HTML part B block (the `<h1>` + `<p>`) → hero text vanishes.
  Then CSS Patch 1 block → text jumps back to browser defaults.
- **Line-by-line:**
  - `<h1 class="hero-title">My <span class="accent">Todo</span> List</h1>` —
    the `<span>` is exactly the slide's definition: style *one part* of a text.
  - `.hero-title { font-size: 40px; font-weight: 800; line-height: 1.15;
    text-align: center; }` — connect each line to its slide row.
  - `.accent { text-decoration: underline; … }` — first appearance of
    `text-decoration`; it comes back as `line-through` in Patch 3.
- **Student checkpoint:** centered hero + underlined accent word.

### Patch 2 — HTML ch3 · CSS ch2 + ch5 + ch3 + ch4 *(the wow moment)*

- **Slides:** `<div> <main> <section> <header> <footer>`;
  box model (`width height margin padding border border-radius`),
  backgrounds (`background-color background-image background-size box-shadow
  opacity`), flexbox (`display justify-content align-items gap`),
  positioning (`position top/right z-index`).
- **Delete demo:** the whole Patch 2 block → gradient, glow, glass card and
  stats all disappear → raw hero text on white. Restore → students *feel* what
  this patch was worth. (The block includes the nested-free siblings only, so
  the list and form below are untouched.)
- **Line-by-line:**
  - `body` rule → this one rule is the whole page: flex column + `gap` stacks
    the sections, `background-image: linear-gradient(...)` paints the theme.
  - `.glow` → `position: fixed; top/right: -120px/-80px` parks a decorative
    ball off-corner; `opacity: 0.7` + `z-index: -1` send it behind content.
  - `.card` → walk the box model out loud: content → padding → border →
    radius → shadow. `position: relative` = "anchor" for the next rule.
  - `.badge` → `position: absolute; top: 24px; right: 24px` — first
    *relative + absolute* pair; the card is the anchor, the badge pins to it
    (24px = the card's own padding, so it lines up with the content below).
  - `.stats` → `display: flex; justify-content: space-between; gap: 12px` =
    the three columns.
  - `.num` / `.label` → typography recall on new elements.
- **Student checkpoint:** gradient page + glass stats card with corner badge.

### Patch 3 — HTML ch4 + ch5 · CSS: recalls only (no new chapter)

- **Slides:** `<a href>`, `<img src alt>`; `<ul> <ol> <li>`.
  (Positioning was covered in Patch 2 — nothing new on the CSS board today.)
- **Live ch4 elements:** the footer row is gone, but both ch4 tags live *inside*
  the list card now — the logo `<img>` is the card-header icon, and one task
  contains a real `<a href>` (a link is inline: it sits inside your text).
- **Delete demo:** the Patch 3 block → icon, list, clocks and link all disappear
  (the whole card); stats card and form stay (they're siblings). Also delete
  just the CSS Patch 3 block → the list falls back to default bullets and the
  logo jumps back to its raw 64px.
- **Line-by-line:**
  - `<ul class="tasks">` + `<li class="task">` → bullets on, then
    `list-style: none` removes them (supporting property, not in the 30).
  - `.time { margin-left: auto }` → a **flex/box-model recall**: the free
    space piles up before the clock, so it slides to the right edge of the
    row — no positioning needed (ch4 stays in Patch 2).
  - `.check` → box-model recall (`width height border border-radius`) + flex
    recall to center the ✓.
  - `.task.done .name { text-decoration: line-through }` → callback to
    Patch 1: same property, new value, now on a real use case.
  - `<img class="head-icon" src="assets/logo.svg" alt="Web Dev Team logo">` →
    `src` + `alt` from the slide; `width/height/border-radius` make it a
    circle (recall ch2) — ch4's media example, wearing the app's check-mark.
  - `… <a href="…" target="_blank" rel="noopener">flexbox</a>` → `href` is the
    address (a real URL is long — that's normal); the link sits *inside* the
    task text; `target="_blank"` opens a new tab so we never navigate away
    from our own page; `text-decoration: none` strips the underline (recall ch1).
- **Student checkpoint:** logo icon + title in the card head, 4 rows with
  circles, one struck-through, one task linking out, clock tags at the right
  edge.

### Patch 4 — HTML ch6 · CSS ch6

- **Slides:** `<form> <label for> <input type> <button>`;
  interactivity: `cursor transition :hover transform`.
- **Delete demo:** HTML Patch 4 block → the form vanishes. Then CSS Patch 4
  block → button still there but *dead*: no cursor change, no lift, rows and
  the link stop reacting. Hover everything before/after the restore.
- **Line-by-line:**
  - `<form class="card add-card">` → reuses `.card` from Patch 2 (that's why
    we use classes); `label for="new-task"` matches `input id="new-task"` —
    clicking the label focuses the input (try it).
  - `<button type="button">` → `type="button"` so nothing submits/reloads
    today; next session we replace it with real logic.
  - `cursor: pointer` → the hand icon.
  - `transition: transform .18s ease, box-shadow .18s ease` → *how long* a
    change takes; `:hover { transform: translateY(-3px) }` → *what* changes.
  - `.task:hover { background-color…; padding-left: 10px }` → rows slide
    right on hover — same transition pattern, second use.
  - `.name a:hover { text-decoration: underline }` → third `:hover` target:
    the link only reveals its underline when the mouse is over it.
  - `input:focus` → bonus pseudo; nice glow, mention only if asked.
- **Student checkpoint:** the full app, everything reacts to the mouse.

### Wrap-up

- Recap the map: structure (ch1) → text (ch2) → containers (ch3) →
  boxes/colors/flex/position (CSS) → lists/links/media → forms/motion.
- **Hook for next session:** the form does nothing yet and there are no
  delete buttons — next time we add JavaScript: add a task for real, delete a
  task, and **undo** the deletion. Today's HTML gives us every element we need.

---

## 5. Guide mapping (from `material_references/guide.txt`)

| Patch | HTML chapters | CSS chapters | Where in the code |
|---|---|---|---|
| Pre-Patch | (what is HTML, role, basic syntax) | (basic CSS syntax) | `index.html` frame lines · `style.css` `BASE` block |
| 1st | 1 · Document Structure, 2 · Text & Headings | 1 · Typography & Text | `PATCH 1` parts A+B · `style.css` `PATCH 1` |
| 2nd | 3 · Containers & Layout | 2 · Box Model, 5 · Backgrounds, 3 · Flexbox, 4 · Positioning | `PATCH 2` · `style.css` `PATCH 2` |
| 3rd | 4 · Links & Media, 5 · Lists | — (recalls only, no new chapter) | `PATCH 3` · `style.css` `PATCH 3` |
| 4th | 6 · Forms & Interaction | 6 · Interactivity & Motion *(see note)* | `PATCH 4` · `style.css` `PATCH 4` |

**Notes for the team**

1. The guide lists **CSS ch4 in both the 2nd and 3rd patches**; per session
   decision **positioning stays only in Patch 2** (the badge) — Patch 3's CSS
   is recall-only (the clock uses `margin-left: auto`). The guide never lists
   **CSS ch6**, which we place in the 4th patch next to HTML ch6, where
   `cursor/transition/:hover` naturally belong (buttons + hover states).
2. HTML ch1's frame is walked in the Pre-Patch (basic syntax needs a file);
   it is recapped at the Patch 1 banner.
3. Properties outside the "30 essential" list are marked with comments
   (`supporting`, `bonus`, `recall`) — they are one-liners, never a new topic.

## 6. Student build order (for `starter/`)

1. `BASE` is pre-given — explain `:root` as "our palette".
2. After each demo: fill that patch's `TODO` in **both** files, refresh,
   then compare with `stages/patchN/` — that folder is your page's exact
   expected state after patch N.
3. Stuck? The instructor's `index.html` / `style.css` is the reference —
   read it, don't copy it.
4. Fast finishers: `BONUS` media query (small screens), then restyle with a
   different `:root` palette.
