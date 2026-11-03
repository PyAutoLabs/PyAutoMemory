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
last digest: 2026-11-03
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
2026-11-03 — [SMBHs] EMBER: A Little Red Dot Candidate at $z_{\rm spec}=10.36$ in the Seed Black Hole Era — 2611.00195
2026-11-03 — [SMBHs] Dynamically defined bulges reveal that early-type galaxies with compact bulges host more massive black holes — 2611.01469
2026-11-03 — [SMBHs] MARTA: A "little" black hole hidden in a clumpy, metal-poor galaxy at z~3.8 — 2611.00199
2026-11-03 — [Dark Matter] See you again: an $80^\circ$ NGC~5466 stellar stream and its constraints on the Galactic dark halo mass — 2611.02653
2026-11-03 — [Dark Matter] Baryonic feedback and intrinsic alignments in profile: a frequentist view of DES Y3 cosmic shear — 2611.03537
2026-11-03 — [SMBHs] Introducing Aurora: A New Black Hole Seeding Model With Explicit Environmental Coupling — 2611.01315
2026-11-03 — [Galaxy Formation / Evolution] Episodic Star Formation - II. The Origin of the Fundamental Metallicity Relation — 2611.03645
2026-11-03 — [SMBHs] Angular Momentum Transport across Accretion States around a rapidly spinning black hole — 2611.01827
2026-11-03 — [Galaxy Formation / Evolution] The Stellar-Mass Dependence of Feedback-Driven Outflows in DESI DR1 Star-Forming Galaxies — 2611.02580
2026-11-03 — [Stats] Accelerating posterior sampling in Bayesian inverse problems with diffusion models: an online-offline perspective — 2611.01300
