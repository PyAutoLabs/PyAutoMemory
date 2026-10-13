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
last digest: 2026-10-13
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
2026-10-08 — [SMBHs] Can LISA See Inside the Little Red Dots? — 2610.08964
2026-10-08 — [Galaxy Formation / Evolution] Early onset of the hot circumgalactic medium around Milky Way galaxies — 2610.08931
2026-10-08 — [SMBHs] Widespread steep X-ray spectra of luminous $z\simeq5.85-7.5$ quasars and their implications for future X-ray surveys — 2610.10522
2026-10-08 — [SMBHs] A relativistic inflow candidate in a quasar at cosmic noon — 2610.10267
2026-10-08 — [SMBHs] A Decade-Scale Ionization Echo of Black-Hole Accretion in Galactic Nuclei — 2610.10373
2026-10-08 — [SMBHs] Changing-look Active Galactic Nuclei from the Dark Energy Spectroscopic Instrument. VII. Testing Disk-Corona Diagnostics with eROSITA — 2610.10331
2026-10-08 — [Galaxy Formation / Evolution] SAGE26 Paper I: Modelling the baryon cycle from cosmic dawn to the present day — 2610.09564
2026-10-08 — [SMBHs] Quasi-periodic eruption spectral-timing: EMRIs crossing warped accretion disks — 2610.10110
2026-10-08 — [Galaxy Formation / Evolution] Euclid Quick Data Release (Q1). Exploring the complexity of quenching processes across time, environment, and mass through recently quenched galaxies — 2610.08999
2026-10-08 — [Dark Matter] Measuring the Clustering of tSZ-Selected Galaxy Clusters with SPT-3G — 2610.08947
2026-10-09 — [SMBHs] ACORN I. Massive Black Hole Seeding and Tidal Disruption Events from Star Clusters in Cosmological Simulations — 2610.12398
2026-10-09 — [Stats] Feedback-Conditional 3D Reconstruction of Cosmic Baryons with Flow Matching — 2610.10741
2026-10-09 — [SMBHs] Disk Structure May Determine AGN Variability and Explain the Accretion Disk Size Problem: No Broad Line Region Required — 2610.12462
2026-10-09 — [SMBHs] Cosmic Duets II. Growth and accretion in Gaia Multi-Peak dual AGN at Cosmic Noon — 2610.10687
2026-10-09 — [Galaxy Formation / Evolution] JWST CAPERS: Spectroscopic evaluation of very high redshift galaxy candidates — 2610.12322
2026-10-09 — [SMBHs] Prevalence of radio Active Galactic Nuclei in galaxy groups since z=3.5 in the COSMOS-Web field — 2610.10719
2026-10-09 — [Stats] Evidence for orbital eccentricity supports a hierarchical origin for GW231123 — 2610.12205
2026-10-09 — [Stats] Opening the Black Box: What Neural Networks Learn from Pulsar Timing Array Data — 2610.12308
2026-10-09 — [Galaxy Formation / Evolution] Inflow-driven galaxy evolution - II: A hierarchy in the scaling relations of star-forming galaxies — 2610.12394
2026-10-09 — [SMBHs] Pushing Variability Searches to Extreme Dwarf Galaxies with the Vera C. Rubin Observatory Data Preview 2 — 2610.10755
2026-10-12 — [Galaxy Formation / Evolution] A Burst of Reionization in the Dark Ages — 2610.12552
2026-10-12 — [SMBHs] A dust-reddened quasar in a [C II]-luminous host at z=6.55 — 2610.13758
2026-10-12 — [Stats] Neural Estimation of Summary Statistics for Simulation-Based Inference with Non-Asymptotic Guarantees — 2610.13031
2026-10-12 — [Stats] SLICE: Sequential Likelihood-Free Inference via Conformal E-Values — 2610.13855
2026-10-12 — [SMBHs] The Population of Type~1 Active Galactic Nuclei in Dark Energy Spectroscopic Instrument. I. Profile-dependent Measurements of the Low-redshift Sample — 2610.13218
2026-10-12 — [Galaxy Formation / Evolution] When dust growth takes over: the origin of dust in post-reionization galaxies — 2610.12591
2026-10-12 — [Galaxy Formation / Evolution] A Single Line-Emitter Identified in an Unbiased Search with JWST/NIRSpec: Multi-Object Coronagraphy for Slitless Spectroscopy — 2610.12553
2026-10-12 — [SMBHs] Extreme mass ratio inspirals from the Hills mechanism, The eccentricity distribution of Hills EMRIs in LISA — 2610.13294
2026-10-12 — [SMBHs] Resistive alignment of a black-hole magnetosphere — 2610.13288
2026-10-12 — [Stats] Amortised Inference through One-Step Implicit Sampling — 2610.12679
