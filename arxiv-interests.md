# arXiv interests

The day's ten most relevant arXiv papers that are **not** strong lensing —
black holes, dark matter, galaxy formation, statistics and inference, and
whatever else the digest judges worth a look. Strong lensing has its own tier
(`arxiv-inbox.md`); nothing appears on both.

Format:

- One paper per line: `<YYYY-MM-DD> — [<Topic>] <title>`, optionally followed
  by ` — <arXiv id or URL>` (the same title/ref convention as
  `reading-queue.md`, plus the topic).
- The date is the arXiv **announcement** date the digest ran against, and it is
  what groups the file into **day batches**.
- `[<Topic>]` names the `reading-queue.md` section the ➕ button files the paper
  into — these papers span domains, so unlike the strong-lensing inbox there is
  no single destination. A topic naming no real section falls back to
  `## Interests` (`FALLBACK_SECTION` in `scripts/interests_actions.py`).
- **A backlog on the inbox's timer.** The Dashboard shows the **oldest
  un-cleared batch only**, and its 🧹 *clear* button drops that whole day and
  reveals the next — but a batch nobody clears **lapses after 7 days**
  (`INBOX_WINDOW_DAYS` in `scripts/inbox_actions.py`, reused by
  `interests_actions.py sweep`) and is swept by the nightly job. The batch is
  the unit: the whole day goes, never part of one.

  This list was built the other way — "a backlog, not a timer; nothing here
  lapses" — so that a fortnight away would be a fortnight of batches to cycle
  through rather than a fortnight of lost recommendations. The measurement
  said otherwise: of 123 papers appended, **2 reached the reading queue and 1
  batch was cleared** — a 1.6 % clearance rate, leaving 114 entries in 11
  day-batches unread. A backlog nobody walks forward through is not a backlog,
  and it makes the oldest batch — the one the Dashboard shows — the least
  relevant thing on the board. Seven days is how long a suggestion is worth
  looking at; the same rule as `arxiv-inbox.md`, applied a day at a time.
- Each paper carries the same one-tap actions as the inbox: 📄 straight to the
  PDF, ➕ add to the reading queue, 📥 intake into memory, 📑 make citeable,
  ✖️ dismiss.
- A cleared or swept batch is not lost: git history holds it. Same reasoning as
  the inbox sweep — the never-delete rule in `reading-queue.md` protects
  *reading history*, and an un-acted suggestion is not history.
- One `last digest: <YYYY-MM-DD>` line, directly below the `---`, records the
  last run of the nightly digest — **papers or none** — so an empty list says
  *which* kind of empty it is: dated today it is a genuinely quiet day, four
  days stale it means the filing is broken and papers were lost. Replaced,
  never accumulated.
- Written by PyAutoMind's `arxiv_interests.yml`. Hand edits are safe but will
  race a nightly run; prefer the Dashboard buttons.

---
last digest: 2026-10-05
2026-10-05 — [SMBHs] The Structure in the Structure Function of Black Hole Light Curves — 2610.02729
2026-10-05 — [Dark Matter] Baryonic Imprints on DM Halos: the concentration-mass relation and its dependence on 28 model parameters in the CAMELS suite — 2610.03544
2026-10-05 — [SMBHs] Separating the Optical to Near-Infrared Light of AGN and Their Host Galaxies — 2610.02465
2026-10-05 — [Galaxy Formation / Evolution] A two-stage settling of the Milky Way disk revealed by precise ChronoGal ages — 2610.03164
2026-10-05 — [Stats] Dark Energy Survey Year 6 Results: fast and interpretable posterior predictive checks for correlated cosmic probes — 2610.03447
2026-10-05 — [SMBHs] Suppression of spiral density waves in collisionless accretion flows — 2610.02475
2026-10-05 — [Dark Matter] The Largest Catalog of Dwarf Galaxy Groups: Transient Structures or Building Blocks of the Universe? — 2610.02587
2026-10-05 — [Stats] A novel, fast, and accurate code for cosmological loop calculations — 2610.03466
2026-10-05 — [Dark Matter] Higgsino dark matter compatible with the LUX-ZEPLIN high-energy nuclear-recoil event and IceCube constraints — 2610.03692
2026-10-05 — [Galaxy Formation / Evolution] Star Cluster Populations in 38 Spiral Galaxies: Evidence for Near-Universal Mass and Age Distributions from PHANGS — 2610.02606
