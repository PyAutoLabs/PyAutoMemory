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
last digest: 2026-10-19
2026-10-14 — [SMBHs] Massive black holes in the first billion years with JWST — 2610.18263
2026-10-14 — [Galaxy Formation / Evolution] Mergers may not be the main channel for galaxy stellar mass growth at redshift $z\gtrsim5$: Predictions from cosmological hierarchical models and simulations — 2610.17575
2026-10-14 — [Dark Matter] MUSE-DARK IV. Comparing Dark Matter Densities to Star Formation Histories in 375 intermediate-z galaxies — 2610.18282
2026-10-14 — [SMBHs] The Connection Between the Growth of Massive Black Holes and Their Dynamical Histories — 2610.18659
2026-10-14 — [Galaxy Formation / Evolution] Untangling Similarities and Differences in Star Formation Histories Across Cosmological Simulations — 2610.17359
2026-10-14 — [SMBHs] A radio counterpart of the local little-red-dot J092359+415736 — 2610.17559
2026-10-14 — [SMBHs] Scaling Up: A Global Optical/X-ray Correlation For Reprocessing Across Black Hole Masses — 2610.17248
2026-10-14 — [Dark Matter] MeV dark matter decay forecasts for the COSI mission — 2610.17217
2026-10-14 — [SMBHs] Delving into the depths of NGC 3783 with XRISM VI. Evidence for a failed wind based on Fe xxv absorption line variability — 2610.18429
2026-10-14 — [SMBHs] The ePESSTO+ census of ZTF nuclear transients. I. What flares in galactic nuclei? — 2610.18633
2026-10-15 — [SMBHs] The Dance of the Little Red Dots: Spectroscopy of Two Blue Companions at z = 3.9 and 5.5 Reveals Young, Metal-Poor Starbursts Merging with Their LRDs within a Few Hundred Myr — 2610.18968
2026-10-15 — [Stats] Low-cost neural summaries for cosmological inference: an ensemble of convolutional neural networks trained on approximate simulations — 2610.19891
2026-10-15 — [Galaxy Formation / Evolution] Galactic Outflows and Star-Formation Quenching: A JWST Perspective — 2610.19182
2026-10-15 — [SMBHs] Are Broad Mg II Galaxies Fading AGN? — 2610.19126
2026-10-15 — [Dark Matter] The Atacama Cosmology Telescope: DR6 Constraints on Isotropic Time-Dependent Cosmic Birefringence from Axion-like Particles — 2610.19049
2026-10-15 — [Dark Matter] Wave Cold Dark Matter Can Reproduce the Radial Acceleration Relation in X-ray Elliptical Galaxies — 2610.18969
2026-10-15 — [SMBHs] SQuIGGLE: Radio AGN Found Predominantly in Young, Gas-rich Post-starburst Galaxies at z ~ 0.7 — 2610.19146
2026-10-15 — [Stats] jax-SNANA: A GPU-accelerated Supernova Framework for the SBI Era — 2610.19000
2026-10-15 — [Galaxy Formation / Evolution] Sleeping or Dead? Probing the Quenching Mechanism of JWST Dormant Galaxies at z > 3 with ALMA — 2610.19926
2026-10-15 — [SMBHs] Scalar-Assisted Growth of Supermassive Black Holes: Boson-Mass Windows and Observational Constraints — 2610.18986
2026-10-16 — [SMBHs] The Radius-Luminosity Relationship for Active Galactic Nuclei with Hierarchical Bayesian Reverberation Mapping — 2610.22096
2026-10-16 — [SMBHs] How Little Red Dots Turn Blue: Evolution of Kelvin-Helmholtz Contracting Black Hole Envelopes and Observational Diagnostics — 2610.20709
2026-10-16 — [Stats] Conditional Mean Flows: Few-Step Densities for Simulation-Based Inference — 2610.21657
2026-10-16 — [SMBHs] Wandering intermediate-mass black holes and off-nuclear tidal disruption events from early star clusters — 2610.20719
2026-10-16 — [Dark Matter] Hydrostatic Equilibrium Constraints on the Fuzzy Dark Matter Mass from Dwarf Spheroidals: Method, Systematics, and Robustness — 2610.21722
2026-10-16 — [SMBHs] A Comprehensive AGN Inventory for the Dwarf-Dominated RESOLVE and ECO Surveys: Mass-Dependent AGN Types and Occupation Fractions — 2610.22115
2026-10-16 — [SMBHs] Neutrino production at the extreme vicinity of supermassive black hole in NGC 1068 — 2610.21110
2026-10-16 — [Dark Matter] Compact Dark Matter with Globular Cluster Pulsars — 2610.20732
2026-10-16 — [SMBHs] A model for the image structure and spectral energy distribution of relativistic jets — 2610.20961
2026-10-16 — [Galaxy Formation / Evolution] An Attenuation Bump at z=9.3: Probing Dust Diversity at Cosmic Dawn — 2610.20722
2026-10-19 — [SMBHs] Clustering of JWST LRDs. Implications for PBHs and other early-forming seeds — 2610.23806
2026-10-19 — [Stats] ENFR: Evidence Networks with Flow-Matched References for Amortized Simulation-Based Model Inference — 2610.23825
2026-10-19 — [Galaxy Formation / Evolution] How bright can a galaxy be? Extreme value predictions for high-redshift survey observables — 2610.23016
2026-10-19 — [SMBHs] What can a uniform reflection pipeline establish about supermassive black hole spin? An audit and a corrected analysis of 57 AGN with XMM and NuSTAR — 2610.23081
2026-10-19 — [SMBHs] $\texttt{GASTRO-BH}$: Effects of a Central Black Hole in GSE-like Dwarf-galaxy Mergers Around Milky Way-like Hosts — 2610.22860
2026-10-19 — [SMBHs] Exploring Cosmic Rays from Gravity-Limited Acceleration at Supermassive Black Holes — 2610.23393
2026-10-19 — [SMBHs] A precessing AGN with S-shaped morphology discovered in MALS — 2610.23738
2026-10-19 — [Dark Matter] Foreground dependence of the 20 GeV Galactic halo gamma-ray excess and its proposed connection to the LUX-ZEPLIN event — 2610.23713
2026-10-19 — [Dark Matter] Hidden Disruption in Milky Way-like Satellite Galaxy Populations — 2610.22481
2026-10-19 — [Dark Matter] Analytic and numerical study of dark matter halos in the Horndeski theory — 2610.22819
