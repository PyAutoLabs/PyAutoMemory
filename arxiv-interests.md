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
last digest: 2026-11-10
2026-11-04 — [SMBHs] UV spectra of little red dots: Broad-line N/C, gas recycling and black hole masses — 2611.05349
2026-11-04 — [Dark Matter] 3D dark matter map of the JWST COSMOS-Web field using diffusion-based generative priors — 2611.03786
2026-11-04 — [Stats] SBi3PCF: cosmology with Dark Energy Survey Year 3 cosmic shear — 2611.05367
2026-11-04 — [Dark Matter] Gaia's dark partners: A new signature of dissipative dark matter — 2611.03793
2026-11-04 — [SMBHs] How Fast do Black Holes Spin? — 2611.04361
2026-11-04 — [SMBHs] A full chemical network treatment of supermassive black hole seed formation from dark matter annihilation or decay — 2611.03802
2026-11-04 — [SMBHs] Towards Self-consistent Modeling of Quasi-Stars and their NLTE Spectra: Implications for Little Red Dots — 2611.03819
2026-11-04 — [Galaxy Formation / Evolution] How bursty star formation shapes spectral diversity at high redshifts: breaking degeneracies in early galaxy formation — 2611.03790
2026-11-04 — [SMBHs] The STARfall pathway: forging intermediate-mass black holes through stellar collisions in dense star clusters — 2611.03812
2026-11-04 — [Stats] Stress-Testing Small-Scale Cosmological Inference With Empirical Galaxy--Halo Connection Models — 2611.04419
2026-11-05 — [SMBHs] The M87 Black Hole Mass from JWST and Keck Stellar Kinematics Spanning 10 pc to 10 kpc — 2611.05486
2026-11-05 — [SMBHs] Spectroscopy-informed Deep Learning Searches for Photometric Little Red Dots in JWST Surveys — 2611.06026
2026-11-05 — [Dark Matter] DESI DR2 Results III: The Mass of the Milky Way — 2611.05518
2026-11-05 — [Galaxy Formation / Evolution] The impact of Population III stars on the elemental enrichment of ultra-faint galaxies in the FIRE-3 zoom-in simulations — 2611.05589
2026-11-05 — [SMBHs] Revisiting the Stellar-Dynamical Mass of the Central Black Hole in NGC 3227 — 2611.05547
2026-11-05 — [Dark Matter] Dynamics of self-gravitating halos with decaying dark matter — 2611.05474
2026-11-05 — [Galaxy Formation / Evolution] AGN Host Galaxies in COSMOS-Web: Linking Structural Evolution and Star Formation Quenching up to $z=5$ — 2611.06443
2026-11-05 — [Dark Matter] Gravitational-Wave Microlensing as a Probe of Compact Object Population — 2611.05947
2026-11-05 — [Stats] Evolutionary Map of the Universe (EMU): Selection of active galactic nuclei and star-formation emission with machine-learning techniques — 2611.06190
2026-11-05 — [SMBHs] ReveaLLAGN 2: Exploring the Nuclear Gas and Stellar Kinematics of Nearby LLAGNs with JWST/NIRSpec IFU — 2611.05496
2026-11-06 — [Dark Matter] Probing the Seed Effect of Supermassive Primordial Black Holes with Weak Gravitational Lensing — 2611.07574
2026-11-06 — [SMBHs] Black Hole Seeds and Little Red Dots: Connecting Formation and Growth with a JWST Multi-Cycle Treasury Program — 2611.07006
2026-11-06 — [Stats] Is Morphology All You Need? Quantifying Imprints of Past Star Formation in the Present-Day Morphologies of Galaxies — 2611.07373
2026-11-06 — [SMBHs] Violent relaxation in hierarchical stellar systems: pathways toward massive black hole formation in the early Universe — 2611.07546
2026-11-06 — [SMBHs] AGN Archaeology: A Systematic Search for Fading AGN in MaNGA — 2611.07028
2026-11-06 — [SMBHs] The complex periodic variability of PKS 0301-243: hints of a supermassive black hole binary candidate — 2611.08332
2026-11-06 — [Dark Matter] Latest $ν$s from the Earliest Galaxies: Probing neutrino self-interactions with JWST — 2611.07013
2026-11-06 — [Galaxy Formation / Evolution] The ALPINE-CRISTAL-JWST Survey: The Tully-Fisher Relation at $z = 4-6$ — 2611.07064
2026-11-06 — [SMBHs] The HST-Hyperion Survey: X-ray AGN Enhancement in the Hyperion Proto-supercluster — 2611.07047
2026-11-06 — [Stats] A Machine Learning Approach to Coupling Photoionization & Multi-Frequency Radiation Hydrodynamics — 2611.07162
2026-11-09 — [SMBHs] Where the red rise stops: JWST/MIRI reveals a near-infrared turnover in the Little Red Dot Abell2744-QSO1 — 2611.09397
2026-11-09 — [SMBHs] Magnetically Arrested Accretion and Black Hole Spin in a Semi-Analytic Model of Galaxy Formation — 2611.08599
2026-11-09 — [Dark Matter] The AIDA-TNG project: Galactic bar pattern speeds in self-interacting dark matter — 2611.09852
2026-11-09 — [Stats] New optimisations for exact, scalable 2D Gaussian process inference, with applications to astronomical time-series — 2611.09198
2026-11-09 — [Galaxy Formation / Evolution] Jeans Dynamical Constraints on the IMF in Massive Quiescent Galaxies at $z\sim0.7$ from JWST/NIRSpec — 2611.08612
2026-11-09 — [SMBHs] GW230729\_082317 and GW231118\_005626: A Candidate of Hierarchical Triple Mergers — 2611.09338
2026-11-09 — [Stats] Phentax: A JAX implementation of the IMRPhenomTHM waveform model — 2611.08596
2026-11-09 — [Dark Matter] Axion cloud survival in nuclear star clusters — 2611.09236
2026-11-09 — [SMBHs] KCWI Observations of Type 2 Quasar-driven Ionized Outflows at z~0.1 — 2611.08828
2026-11-09 — [Dark Matter] Nonstandard Dark Matter at Nonlinear Scales — 2611.08636
2026-11-10 — [SMBHs] Little Red Dots from Primordial Black Holes: Non-Gaussianity and Accretion Evade $μ$-Distortion Constraints — 2611.12861
2026-11-10 — [SMBHs] AGN Feedback Turbulence in Cool-core Clusters: Evidence from XRISM — 2611.12845
2026-11-10 — [Galaxy Formation / Evolution] The Cool Circumgalactic Echo of the Stellar-to-Halo Mass Relatio — 2611.12734
2026-11-10 — [Stats] Two-Phase Rapid Simulation-Based Inference with Differentiable Simulators — 2611.12422
2026-11-10 — [SMBHs] A Self-Interacting Dark-Matter Route to Supermassive Kerr Black Holes via Super-Eddington Bondi Accretion: Mass-Spin Evolution — 2611.12282
2026-11-10 — [Dark Matter] Dust in cold and warm dark matter in a suite of zoom-in simulations of Milky Way analogues — 2611.12047
2026-11-10 — [Stats] FAIR Universe Weak Lensing ML Uncertainty Challenge: Dataset and Cosmological Inference Competition — 2611.10228
2026-11-10 — [SMBHs] The Edge of the Warm Corona in Active Galactic Nuclei — 2611.12595
2026-11-10 — [SMBHs] The shape and velocity of black hole coronas — 2611.11884
2026-11-10 — [Dark Matter] Negative Dynamical Friction in Dark Matter Spikes around Rotating Black Holes — 2611.11380
