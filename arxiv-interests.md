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
last digest: 2026-10-07
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
2026-10-06 — [SMBHs] Gravitational-wave background from supermassive black holes without merger trees: Tidally regulated mergers and direct inference from the NANOGrav 15 yr data — 2610.06220
2026-10-06 — [SMBHs] Internal Radiative Feedback Triggers Global Collapse and Direct-Collapse Black Hole Formation in Metal-free Atomic-Cooling Haloes — 2610.03877
2026-10-06 — [Galaxy Formation / Evolution] The star-forming past and quenching of brightest cluster galaxies in TNG-Cluster — 2610.06634
2026-10-06 — [Stats] Not just a phase: detecting nanohertz gravitational waves from phase alone — 2610.06178
2026-10-06 — [Dark Matter] Baryonic Imprints on DM Halos: characterizing the full concentration-mass probability distribution with CAMELS — 2610.03946
2026-10-06 — [Stats] AI-assisted super-resolution cosmological simulations V: Cosmology-aware super-resolution — 2610.06710
2026-10-06 — [Dark Matter] Cusps, cores, and one acceleration: dark-matter haloes versus modified dynamics across the full SPARC sample — 2610.05871
2026-10-06 — [SMBHs] Jets with Streaks: the Global Dynamics and Structure of Striped Poynting flux dominated Jets — 2610.04796
2026-10-06 — [Galaxy Formation / Evolution] Unveiling the Origins of the Molecular Gas Reservoirs in Recently Quenched Massive Galaxies — 2610.06680
2026-10-06 — [Stats] Fast Bayesian Updating of the Neutron-Star Equation of State with Neural Posterior and Evidence Estimation — 2610.05121
2026-10-07 — [SMBHs] Radiation pressure powers quasar broad absorption line winds but fails to drive galaxy feedback — 2610.07624
2026-10-07 — [SMBHs] Chaotic accretion can (still) explain early supermassive black hole growth — 2610.07947
2026-10-07 — [SMBHs] Halo Mass Function Constraints on Early Galaxy and AGN Populations in the JWST Era — 2610.08731
2026-10-07 — [SMBHs] Hierarchical Black Hole Mergers at High Redshift: Predictions for LISA and LGWA from SEEDZ — 2610.07183
2026-10-07 — [Stats] Scalable and sequential inference of the neutron star equation of state with the Einstein Telescope — 2610.07975
2026-10-07 — [Stats] Spectra: Exact Component Transport for Test-Time Prior Adaptation in Simulation-Based Inference — 2610.08021
2026-10-07 — [Stats] Fast and accurate differentiable code of the galaxy power spectrum based on Eulerian and Lagrangian one-loop perturbation theories — 2610.08023
2026-10-07 — [Stats] When, Why, and How CMB Compression Fails — 2610.08728
2026-10-07 — [SMBHs] Galaxy merger-driven signatures in massive black hole pair hosts across cosmic time — 2610.08709
2026-10-07 — [Galaxy Formation / Evolution] The impact of feedback and cosmology on Cosmic Infrared Background cross-correlations — 2610.08436
