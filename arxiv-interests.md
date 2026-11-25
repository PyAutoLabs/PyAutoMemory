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
last digest: 2026-11-25
2026-11-19 — [SMBHs] A Tight Broad-line Width-Luminosity Relation in Little Red Dots and Its Consequence for Virial Black Hole Masses — 2611.24217
2026-11-19 — [SMBHs] Radio emission from a local Little Red Dot: a challenge to the ionized cocoon scenario — 2611.24387
2026-11-19 — [SMBHs] A $10^5\,M_\odot$ Black Hole in the Bulgeless Spiral Galaxy IC 342: First Stellar-Dynamical $M_{\rm BH}$ Measurement with Keck/OSIRIS LGS-AO — 2611.24608
2026-11-19 — [SMBHs] Excess intergalactic heating around a dual quasar system 2.8 Gyr after the Big Bang — 2611.23487
2026-11-19 — [SMBHs] Reconstructing the mass-redshift distribution of supermassive black holes using multiband gravitational-wave observations — 2611.24281
2026-11-19 — [SMBHs] Powerful Radio Jets and Galaxy Assembly Align at Cosmic Noon — 2611.24490
2026-11-19 — [SMBHs] Deep Multiwavelength Constraints on the Host Galaxies and Black-Hole Growth of Dwarf AGNs — 2611.24698
2026-11-19 — [SMBHs] Seeing through the fog: astrophysical priors and the evidence for new physics in pulsar timing arrays — 2611.23371
2026-11-19 — [Stats] Interpretable attention-based neural posterior estimation for fast radio burst cosmology — 2611.24542
2026-11-19 — [Dark Matter] Leading Axion Sensitivity with Interstellar Medium Optical Line Emission — 2611.23385
2026-11-20 — [SMBHs] The Galaxy Activity, Torus, and Outflow Survey: N. Little Red Dots are not dust deficient: constraints from Seyfert 1 JWST spectra — 2611.26483
2026-11-20 — [Dark Matter] Dark Matter Model Implications of a Candidate Sub-halo Near the Sun, and the Data Needed to Discriminate Among Them — 2611.25359
2026-11-20 — [Galaxy Formation / Evolution] Top-heavy Initial Mass Functions are not enough at cosmic dawn — 2611.25027
2026-11-20 — [SMBHs] The Cosmic Infrared Background from Population III.1 Supermassive Stars and Black Holes — 2611.25355
2026-11-20 — [SMBHs] Little Red Dots from Primordial Vacuum Bubbles — 2611.26620
2026-11-20 — [Galaxy Formation / Evolution] Magnolia: a highly magnetized galaxy at redshift $z\simeq9$ — 2611.25937
2026-11-20 — [Galaxy Formation / Evolution] Every galaxy is a radio source: a stellar-mass dependent minimum 150 MHz luminosity identified in the LoTSS Deep Fields — 2611.26618
2026-11-20 — [Stats] Simulation-based inference for gravitational-wave cosmology: parameter reconstruction of a first-order electroweak phase transition — 2611.25036
2026-11-20 — [Stats] SlotFlow-GB: A Neural Framework for Trans-Dimensional Inference of Overlapping Galactic Binaries — 2611.26057
2026-11-20 — [Stats] Square Kilometre Array Science Data Challenge 3b: EoR inference — 2611.25823
2026-11-23 — [SMBHs] Hotter than Little Red Dots: Two Quasars with $T\sim10^4\,\mathrm{K}$ blackbody-like continua at $z\sim4$ — 2611.27856
2026-11-23 — [SMBHs] Little Red Dots at Cosmic Noon: Spectroscopic Identification and Broad-Line Properties — 2611.26710
2026-11-23 — [SMBHs] The role of gas on the collisional runaway path to supermassive black hole seeds — 2611.26885
2026-11-23 — [Stats] Diffusing the assumptions: towards realistic LISA stochastic component separation with physics-aware simulation-based inference — 2611.27848
2026-11-23 — [Galaxy Formation / Evolution] Nearly pristine gas and hard ionizing radiation one billion years after the Big Bang — 2611.27979
2026-11-23 — [SMBHs] Disrupted stars and captured compact objects: Combining observations from multiple messengers to infer the population of massive black holes — 2611.27742
2026-11-23 — [SMBHs] Little Red Dots at Cosmic Noon: Spectroscopy Reveals Declining Abundance but a Non-Evolving Luminosity Function Shape — 2611.26685
2026-11-23 — [Stats] Features investigated: A detailed study of axion monodromy inflation using CLiENT — 2611.27265
2026-11-23 — [SMBHs] Lost in the Signal Model: Confusion Between Deterministic and Stochastic Gravitational Wave Signals in Pulsar Timing Array Data — 2611.26681
2026-11-23 — [SMBHs] A TESS Search for Optical Variability in Intermediate-mass Black Hole Candidates — 2611.27890
2026-11-24 — [SMBHs] Velocity-Window Dependence of the Broad H$α$ Width-Luminosity Relation in Little Red Dots — 2611.29615
2026-11-24 — [SMBHs] Quasi-hostless LRDs with intrinsically red, faint UV continua — 2611.28209
2026-11-24 — [SMBHs] Modeling extraordinary relativistic jets on the scale of the cosmic web — 2611.28376
2026-11-24 — [Stats] Joint Flow-Matching Posteriors for Overlapping LISA Galactic Binaries — 2611.30872
2026-11-24 — [Galaxy Formation / Evolution] On the effect of a redshift- and metallicity-dependent top-heavy IMF on high-redshift UV luminosity functions — 2611.31148
2026-11-24 — [SMBHs] Dual Horizon-MAD: A New Mode of Binary Black Hole Magnetically Arrested Accretion with Saturated Horizon Magnetic Fluxes and Intermittent Minidisks — 2611.28237
2026-11-24 — [Galaxy Formation / Evolution] Discovery of Two Hyperluminous Infrared Galaxies at $z\sim6$ — 2611.29560
2026-11-24 — [Dark Matter] The Sensitivity of Gamma-Ray Searches for Dark Matter Annihilation in Milky Way Dwarf Galaxies: the LSST Era and Beyond — 2611.31130
2026-11-24 — [Stats] A Cross-Domain Simulator and Benchmark for Uncertainty Quantification in Global 21-cm Inference — 2611.30444
2026-11-24 — [Stats] Interpretable morphology-based marked statistics — 2611.31167
2026-11-25 — [SMBHs] Euclid: Discovery of a quasar at z = 8.13 hosting a 360-million-solar-mass black hole — 2611.31385
2026-11-25 — [Stats] Machine learning enables full Bayesian inference for spinning extreme-mass-ratio inspirals — 2611.31916
2026-11-25 — [Dark Matter] Enhanced spatial resolution and performance for N-body simulation of self-interacting dark matter — 2611.31364
2026-11-25 — [SMBHs] AGN feedback in the multiphase inner intracluster medium of a cosmological super-resolved galaxy cluster — 2611.31367
2026-11-25 — [SMBHs] The SDSS-V Black Hole Mapper Reverberation Mapping Project: Time-delayed Variability of a Quasar's C IV Broad Absorption Troughs — 2611.31415
2026-11-25 — [Galaxy Formation / Evolution] Resolving the Hubble Tension at $0.1σ$ with Early Dark Energy: Key Role of the Highest-redshift Galaxies from JWST Observations — 2611.32552
2026-11-25 — [Stats] Hesperos & Eosphoros: A Coupled Differentiable Forced-Photometry Operator and Forward Model for SPHEREx Spectrophotometry — 2611.33092
2026-11-25 — [Stats] Parallel and perpendicular: a two-population test with POSSUM radio galaxies confirms hint of CMB birefringence — 2611.31411
2026-11-25 — [Galaxy Formation / Evolution] The dust attenuation scaling relation in the TNG50 simulation — 2611.32592
2026-11-25 — [Stats] Symbolic Regression Diagnostics of 1D Lyman Alpha Forest Emulator — 2611.31450
