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
- **A backlog, not a timer.** Nothing here lapses. The Dashboard shows the
  **oldest un-cleared batch only**, and its 🧹 *clear* button drops that whole
  day and reveals the next — so a fortnight away is a fortnight of batches to
  cycle through, one tap each, not a fortnight of lost recommendations. This is
  the one way this list differs from `arxiv-inbox.md`, which lapses after seven
  days.
- Each paper carries the same one-tap actions as the inbox: 📄 straight to the
  PDF, ➕ add to the reading queue, 📥 intake into memory, 📑 make citeable,
  ✖️ dismiss.
- A cleared batch is not lost: git history holds it. Same reasoning as the
  inbox sweep — the never-delete rule in `reading-queue.md` protects *reading
  history*, and an un-acted suggestion is not history.
- One `last digest: <YYYY-MM-DD>` line, directly below the `---`, records the
  last run of the nightly digest — **papers or none** — so an empty list says
  *which* kind of empty it is: dated today it is a genuinely quiet day, four
  days stale it means the filing is broken and papers were lost. Replaced,
  never accumulated.
- Written by PyAutoMind's `arxiv_interests.yml`. Hand edits are safe but will
  race a nightly run; prefer the Dashboard buttons.

---
last digest: 2026-09-02
2026-08-28 — [Stats] Cross-simulator transfer with foundation model summaries: Towards robust SKA-era reionization inference — 2608.26354
2026-08-28 — [SMBHs] Optimal transport regularized dynamic radio interferometric reconstruction — 2608.27192
2026-08-28 — [Dark Matter] The solitary star cluster of the Andromeda XXV dwarf spheroidal — 2608.26959
2026-08-28 — [Dark Matter] Scatter, bias, and chaos of satellite orbits in triaxial dark matter haloes — 2608.26249
2026-08-28 — [Dark Matter] ELUCID-DESI II. Revealing dark matter mass, tidal, and velocity (MTV) fields using galaxy group phase information — 2608.26668
2026-08-28 — [Dark Matter] Paleo-Detectors as a Novel Probe of Dark Matter-Nucleus Effective Interactions — 2608.26289
2026-08-28 — [Dark Matter] Effects of the interaction of dark matter and neutron-star matter on extreme and intermediate mass-ratio inspirals — 2608.26274
2026-08-28 — [Galaxy Formation / Evolution] SERENADE III: Insight into the Origin of the High Dust Temperature and High [O III]/[C II] Ratio at $z\gtrsim6$ — 2608.26708
2026-08-28 — [Galaxy Formation / Evolution] COSMOS-Web: From early star-formation enhancement to late suppression in galaxy groups — 2608.26348
2026-08-28 — [Dark Matter] Barren but not Empty: The Impact of Void Environments on Galaxy and Halo Populations — 2608.26256
2026-08-28 — [Stats] Derivative hierarchy as the origin of kernel-dependent trends in Gaussian process reconstructions of the hubble parameter — 2608.26774
2026-08-28 — [Galaxy Formation / Evolution] The origin of the stellar mass-size relation of satellite galaxies in the COLIBRE simulations — 2608.26275
2026-08-28 — [Stats] $\texttt{SPINE}$: Symbolic Models to Predict the Evolution of the $Λ$CDM Nonlinear Power Spectrum — 2608.26276
2026-08-28 — [Dark Matter] Revisiting the enigmatic sixth star cluster in the Fornax dwarf spheroidal galaxy — 2608.27270
2026-08-31 — [SMBHs] Overmassive supermassive black holes in SDSS close galaxy pairs — 2608.27730
2026-08-31 — [SMBHs] Formation of black hole stars via star--black hole collisions — 2608.27596
2026-08-31 — [Galaxy Formation / Evolution] Dust and PAHs in late-stage galaxy evolution: Imprints of TP-AGB dust injection, grain growth and AGN feedback in high-z quiescent galaxies with JWST and ALMA — 2608.27571
2026-08-31 — [Stats] Fast and efficient nested sampling with BEST — 2608.28514
2026-08-31 — [SMBHs] Relativistic outflows power a quasi-periodic eruption: constraints on energetics, mass loss, and emission mechanisms — 2608.28507
2026-08-31 — [SMBHs] From Inspiral to Expansion: The Wake-Driven Torque on Binary Black Holes in Gaseous Medium — 2608.27970
2026-08-31 — [SMBHs] A Similarity Theorem and Its Breakdown in Atomic Black Hole Accretion — 2608.28587
2026-08-31 — [Stats] Learning the averaged history of an inhomogeneous universe from its present day density field — 2608.27962
2026-08-31 — [Dark Matter] Low-energy antinuclei measurements for background-free indirect dark matter searches and PBH signatures — 2608.27787
2026-08-31 — [Dark Matter] A Unified Tracer Analysis of DESI DR2 Baryon Acoustic Oscillations — 2608.27830
2026-09-01 — [SMBHs] ALMA CO(2-1) Gas Dynamics in NGC 315: A Multi-Method Benchmark for Supermassive Black Hole Mass Measurement — 2608.31015
2026-09-01 — [SMBHs] A Self-Sustaining Black Hole Engine Powered by the Tidal Disruptions of Stars — 2608.28947
2026-09-01 — [Galaxy Formation / Evolution] The Structural Abundance Crisis of Massive Galaxies in Current Cosmological Simulations — 2608.29893
2026-09-01 — [Dark Matter] Stellar streams around dwarf galaxies are observationally rare in the local Universe — 2608.30806
2026-09-01 — [Dark Matter] Photon--Dark Matter Elastic Scattering: An Effective-Operator Scan and First Operator-Resolved Sensitivity Estimates from the Galactic Halo — 2608.29546
2026-09-01 — [SMBHs] The multi-frequency radio light curve of the sub-pc SMBH binary candidate PG 1302-102 — 2608.29682
2026-09-01 — [Galaxy Formation / Evolution] Radio-dust connection in quasars driven by powerful ionised outflows — 2608.28775
2026-09-01 — [Galaxy Formation / Evolution] Caught Napping by JWST UNCOVER+MegaScience: Constraining bursty star formation histories and number densities of mini-quenched galaxies at redshifts 4-7 — 2608.30011
2026-09-01 — [Galaxy Formation / Evolution] Constraining Baryonic Feedback at $z\sim 1$ with the H$α$ Luminosity Function — 2608.30698
2026-09-01 — [SMBHs] Evidence for an accretion-driven subpopulation of black holes in GWTC-5.0 — 2608.29072
2026-09-02 — [SMBHs] Nanohertz Gravitational-Wave Constraints on Supermassive Binary Black Holes at Cosmic Dawn — 2609.00613
2026-09-02 — [Galaxy Formation / Evolution] Slow stellar halo rotation as a signature of disc flips and GES-like mergers — 2609.01208
2026-09-02 — [Stats] Connecting radio pulsars, magnetars, and XDINSs in a unified evolutionary framework using simulation-based inference — 2609.00962
2026-09-02 — [SMBHs] Accretion-disk sizes in two quasars with interferometrically resolved broad-line regions at $z=2.3$ and $z=4.0$ — 2609.00278
2026-09-02 — [Dark Matter] Extragalactic Stellar Streams in Time-Dependent Cosmological Halos — 2609.00526
2026-09-02 — [Galaxy Formation / Evolution] ELVES-Dwarf. II. A Systematic Search for Satellite Systems of Dwarf Galaxies in the Local Volume — 2609.00283
2026-09-02 — [Dark Matter] Scalar wave scattering by black holes embedded in dark matter halos — 2609.01391
2026-09-02 — [Dark Matter] Baryonic feedback suppression of the matter power spectrum: a three-parameter fitting formula and its single-parameter reduction — 2609.00807
2026-09-02 — [Stats] $\texttt{BilbyFlow}$: user-friendly neural posterior estimation for gravitational-wave astronomy — 2609.00766
2026-09-02 — [SMBHs] Extreme AGN Variability in WISE: Powerful Flares and Candidate Tidal Disruption Events in AGN — 2609.01421
