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
last digest: 2026-10-22
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
2026-10-20 — [SMBHs] Modeling Multi-band Active Galactic Nuclei Lightcurves Using an Self-supervised Attentive Neural Process Network — 2610.24195
2026-10-20 — [Stats] ERGO-ML and how to directly infer the multi-temperature nature of intra-cluster gas: simulation-based inference with TNG-Cluster — 2610.26627
2026-10-20 — [Stats] Exploring the Evidence for Evolving Dark Energy with the Jeffreys prior — 2610.26493
2026-10-20 — [SMBHs] Tidal Disruption Events in Active Galactic Nuclei: Thermal Radiation and Jets — 2610.24849
2026-10-20 — [Galaxy Formation / Evolution] The DARWIN Project: Cosmological Simulations of Galaxy Formation down to Dwarf Scales in Diverse Environments — 2610.25786
2026-10-20 — [SMBHs] Clumpy Outflows from Super-Eddington Accreting Black Holes. II. Conditions for Clump Formation — 2610.24660
2026-10-20 — [SMBHs] The accretion flow and jet of M87: broadband modelling across spatial scales — 2610.26434
2026-10-20 — [Galaxy Formation / Evolution] PRISMS/U13151. A Glimpse into the Earliest Phases of Galaxy Formation through an Ultra-Faint System $\approx$ 500 Myr after the Big Bang — 2610.26560
2026-10-20 — [Galaxy Formation / Evolution] Star formation history of Draco revealed by DESI DR1: suppressed early star formation efficiency for Milky Way dwarf galaxies — 2610.26375
2026-10-20 — [Dark Matter] Multimessenger Probes of Primordial Black Holes with Gravitational Wave and 21 cm Observations — 2610.24067
2026-10-21 — [Dark Matter] Searching for Dense Perturbers in Cold Dark Matter Simulations — 2610.27236
2026-10-21 — [Dark Matter] ASTROLABE: A 3D Particle-Level Surrogate for Cosmology Simulation with Physical Flow Matching — 2610.27068
2026-10-21 — [SMBHs] Balmer breaks in accreting super-massive black hole binaries — 2610.27076
2026-10-21 — [Galaxy Formation / Evolution] Leviathan: a very massive, extended sub-millimetre galaxy spectroscopically confirmed at $\rm z = 4.05$ — 2610.27101
2026-10-21 — [Stats] Modular Bayesian Inference for Partially Misspecified Mixtures with Uncertain Class Labels — 2610.27085
2026-10-21 — [Dark Matter] Kinematically isolating intracluster light in AS1063: a distinct stellar population tracing the dark matter core — 2610.28013
2026-10-21 — [Stats] Gaussian process-based Bayesian imaging of bolometric (sub-)millimetre data — 2610.27733
2026-10-21 — [SMBHs] Probing the Optical/UV Continuum Variability of Active Galactic Nuclei with the Damped Random Walk Model — 2610.27806
2026-10-21 — [Galaxy Formation / Evolution] The clumpy fraction of galaxies at $z=1-9$ with JADES: evidence for a mass-dependent transition in clump origin — 2610.28515
2026-10-21 — [Stats] Are Dynamical Dark-Energy Cosmologies Old Enough? — 2610.27209
2026-10-22 — [SMBHs] Discovery of a Broad-Line Active Galactic Nucleus at $z = 9.98$ — 2610.28735
2026-10-22 — [SMBHs] Prior volume effect inflates the gravitational-wave background in pulsar timing arrays — 2610.28739
2026-10-22 — [Dark Matter] Not so Fast: Revised Calibration of SIDM Core Collapse — 2610.28890
2026-10-22 — [SMBHs] A Little Red Dot emerging from a nitrogen-rich UV-luminous galaxy with Very Massive Stars — 2610.29887
2026-10-22 — [Dark Matter] Gravothermal Evolution of Self-Interacting Dark Matter Halos across Knudsen Numbers — 2610.28745
2026-10-22 — [Dark Matter] Poisson Clustering and Seed Effect of PBHs: Implications for Microlensing, Gravitational Waves, Little Red Dots and Ultra-Faint Dwarf Galaxies — 2610.28723
2026-10-22 — [Stats] PIANISTpy: A JAX-based Python package for velocity-anisotropic astrophysical equilibrium models — 2610.28758
2026-10-22 — [SMBHs] Lasting mEMRIs: Signatures of Multiple Black Hole Extreme Mass Ratio Inspirals from AGN discs — 2610.29376
2026-10-22 — [Galaxy Formation / Evolution] Unveiling the correlation between the UV 2175 Å dust attenuation bump, PAH emission, and gas-phase metallicity at cosmic noon — 2610.28743
2026-10-22 — [Stats] Noisy Pipelines I: An end-to-end pipeline to perform multivariate noise inference for LISA — 2610.28726
