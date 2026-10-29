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
last digest: 2026-10-29
2026-10-23 — [Stats] 2Flow2SN: Dusty Supernova Cosmology with Photometric Redshifts and Contamination using Neural Simulation-Based Inference — 2610.30244
2026-10-23 — [Stats] Simulation-based inference of profile evolution for high-precision pulsar timing — 2610.31450
2026-10-23 — [Dark Matter] Same Events, Weaker Bound: Model Dependence in Magellanic Microlensing Limits on Primordial Black Holes — 2610.30510
2026-10-23 — [SMBHs] The black hole-galaxy correlations of the 12 micron local AGN sample: a NuSTAR perspective — 2610.30285
2026-10-23 — [SMBHs] A Catalog of Spectral Properties for DESI DR1 Quasars — 2610.31416
2026-10-23 — [Stats] Assessing the consistency of the CPL dark-energy model with cosmological data: Simulation-calibrated neural posterior disagreement — 2610.31044
2026-10-23 — [SMBHs] A recurring changing state AGN discovered in the SAMI Galaxy Survey and SDSS — 2610.30816
2026-10-23 — [Stats] Self-Supervised Representation Learning for JWST Galaxy Images and Low Resolution Spectra — 2610.31078
2026-10-23 — [SMBHs] Lomb-Scargle Recovery of Periodic Binary Signals across Black Hole Mass and Cadence — 2610.30772
2026-10-23 — [Galaxy Formation / Evolution] The Milky Way's Early Disk Was Built in Bursts. II. The Multi-component Age-Metallicity Structure of the High-$α$ Disk — 2610.30659
2026-10-26 — [SMBHs] Local Analogs of Little Red Dots: Clues to the X-ray Weakness — 2610.32430
2026-10-26 — [Dark Matter] The Galactic Center Gamma-Ray Excess and the Look-Elsewhere Effect — 2610.32845
2026-10-26 — [Stats] Complete Multi-Band Structural Characterization for 10 Million Galaxies in the Hyper Suprime-Cam Wide Survey using Deep Learning — 2610.32913
2026-10-26 — [Stats] Forward model of the Gaia DR3 selection function — 2610.32551
2026-10-26 — [SMBHs] An Extra-nuclear Water Maser in NGC 1106 Likely Driven By An AGN Shock: Implications for Maser-based Black Hole Mass Measurements — 2610.31753
2026-10-26 — [Galaxy Formation / Evolution] Galaxy Luminosity Functions at z~7-10 from Four Years of JWST Observations — 2610.32307
2026-10-26 — [SMBHs] Tracking the Evolution of Supermassive Black Hole Binaries with Pulsar Terms — 2610.32736
2026-10-26 — [Stats] Prospects of Detecting Cosmological Domain Walls in the Cosmic Microwave Background — 2610.31761
2026-10-26 — [Stats] Sparse Bayesian Neural Networks via Sticky Piecewise Deterministic Markov Processes — 2610.32753
2026-10-26 — [Galaxy Formation / Evolution] Star clusters at cosmic dawn I: the emergence of the initial cluster mass function — 2610.32497
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
