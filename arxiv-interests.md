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
last digest: 2026-11-02
2026-10-27 — [Stats] FastPM: Fast Pretrained Model for Cosmological Simulation-Based Inference — 2610.33955
2026-10-27 — [SMBHs] Initial Conditions of Magnetized AGN Accretion Disks from Cloud Capture and Disruption — 2610.33297
2026-10-27 — [SMBHs] Multiphase Gas Structure in JWST Little Red Dots — 2610.34552
2026-10-27 — [SMBHs] The Hosts and Mass Distribution Function of the Most Massive Black Holes: Implications for the nHz Gravitational Wave Background — 2610.33162
2026-10-27 — [Stats] Cracking into RACS - I. Measuring the cosmic dipole in the RACS-low3 and RACS-mid1 radio surveys with simulation-based inference — 2610.35207
2026-10-27 — [Dark Matter] Dark Matter and MOND successes and degeneracies in reproducing SPARC rotation curves and weak lensing data — 2610.33157
2026-10-27 — [Galaxy Formation / Evolution] Recently launched AGN-driven outflow in a lensed quiescent galaxy at Cosmic Noon — 2610.33176
2026-10-27 — [Galaxy Formation / Evolution] How Quickly Did the Giants Form? Constraining the Formation Timescales of Massive Quiescent Galaxies at Cosmic Noon Using Chemical Evolution Modelling — 2610.34883
2026-10-27 — [SMBHs] Constraining Supermassive Black Hole Seeding and Accretion via Occupation Fractions and Mass-Weighted Distributions — 2610.35673
2026-10-27 — [Stats] Intrinsic Information Rates of Summaries in Simulation-Based Inference — 2610.34703
2026-10-30 — [SMBHs] The coupled evolution of nuclear star clusters and intermediate-mass black holes in a dwarf-galaxy merger — 2610.38767
2026-10-30 — [SMBHs] Black Hole Spin Evolution in Magnetized Accretion Flows — 2610.38673
2026-10-30 — [Stats] Celia: Catalog Embeddings Learned from cosmologIcal simulAtions — 2610.40218
2026-10-30 — [Stats] Field-level inference under pressure: the information content of the thermal Sunyaev-Zel'dovich field — 2610.40617
2026-10-30 — [Stats] Robust statistical significance for Gravitational Wave inference — 2610.39785
2026-10-30 — [SMBHs] The unresolved high-mass frontier of the black hole Fundamental Plane — 2610.40606
2026-10-30 — [SMBHs] Odds Estimation for Supermassive Black Hole Binaries in Local Core Galaxies — 2610.38886
2026-10-30 — [Galaxy Formation / Evolution] PRISMS GHZ8: Evidence for a Young Burst and Potential Merger Activity at z=10.23 — 2610.40633
2026-10-30 — [SMBHs] On The Scaling Relations Between Black Holes And The Galaxy/Bulge Mass And Their Connections With The Black Hole Occupation Fraction — 2610.38699
2026-10-30 — [Galaxy Formation / Evolution] Feeding or Fleeing: The Impact of Enhanced Early Black Hole Growth on Circumgalactic Clumps at $z > 6$ — 2610.39692
2026-11-02 — [SMBHs] Bridging Scales: Multi-Zone GRMHD-Informed Anisotropic AGN Feedback in Galaxies — 2610.40784
2026-11-02 — [Stats] When precise inference is wrong: Diagnosing model misspecification with applications to cosmic dawn and reionisation — 2610.40770
2026-11-02 — [Dark Matter] The multiple origins of spurs in stellar streams: a challenge for dark matter diagnostics — 2610.41842
2026-11-02 — [SMBHs] Cosmic merger rates and population evolution of binary black hole mergers in AGN disks — 2610.40787
2026-11-02 — [Galaxy Formation / Evolution] OASIS III: Bursty star formation drives observed galaxy sizes at $z\geq4$ — 2610.41491
2026-11-02 — [Stats] Learning Galaxy Kinematics from Spatially Unresolved Spectra — 2610.40789
2026-11-02 — [SMBHs] How to feed your dragon: the role of turbulence in AGN activity — 2610.40788
2026-11-02 — [Dark Matter] Dark Halos, Intermediate-Mass BH and Nuclear Stellar Clusters in Dwarf Spheroidals — 2610.41522
2026-11-02 — [SMBHs] The Broad-Line Region Size-Luminosity Relation in AGN Constrained by the Viewing Angle with the FRADO Model — 2610.41594
2026-11-02 — [Galaxy Formation / Evolution] The Size-Mass Relation and Inside-Out Quenching of Massive Quiescent Galaxies at $2<z<3$ with JWST PRIMER and MINERVA — 2610.40937
