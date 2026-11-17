# arXiv inbox

Papers the nightly arXiv digest suggested, waiting for a decision. Nothing here
is in the reading queue yet — the inbox is the tier *in front of* it.

Format:

- One paper per line: `<YYYY-MM-DD> — <title>`, optionally followed by
  ` — <arXiv id or URL>` (same title/ref convention as `reading-queue.md`).
- The date is the arXiv **announcement** date the digest ran against, and is
  the expiry anchor — not the day the paper was submitted.
- The Dashboard renders each line with a 📄 button straight to the paper's PDF
  (the ref above is what makes it possible) plus four one-tap actions: ➕ add to
  the reading queue, 📥 intake into memory, 📑 make citeable, ✖️ dismiss.
- Un-acted lines **lapse after 7 days** (`INBOX_WINDOW_DAYS` in
  `scripts/inbox_actions.py`) and are swept by the nightly job. A swept line is
  not lost: git history holds it. This is deliberate — the never-delete rule in
  `reading-queue.md` protects *reading history*, and an un-acted suggestion is
  not history.
- One `last digest: <YYYY-MM-DD>` line, directly below the `---`, records the
  last run of the nightly digest — **papers or none**. It is what lets an empty
  inbox say *which* kind of empty it is: dated today it is a genuinely quiet
  day, four days stale it means the filing is broken and papers were lost. The
  same job the `#papers` empty-day heartbeat does on the Slack side. It is
  replaced, never accumulated, so the sweep has nothing to age out.
- Written by PyAutoMind's `arxiv_papers.yml`. Hand edits are safe but will race
  a nightly run; prefer the Dashboard buttons.

---
last digest: 2026-11-17
2026-11-11 — Leveraging Lensing-driven Early Warnings: Joint Detectability of lensed Gravitational Waves and their LSST Optical Counterparts — 2611.14343
2026-11-11 — The PAU Survey: Dissecting strong-lensing systems with narrow-band photometric redshifts — 2611.14229
2026-11-13 — Euclid Data Release 1 (DR1). Euclid Lens Identification Pipeline and Scientific Exploration (ECLIPSE) A: Strong lens catalogue overview — 2611.15883
2026-11-13 — Euclid Data Release 1 (DR1). Euclid Lens Identification Pipeline and Scientific Exploration (ECLIPSE) C: Lens modelling pipeline overview — 2611.15888
2026-11-13 — Localization of gravitational-wave source behind galaxy clusters by gravitational-wave lensing — 2611.16916
2026-11-13 — Euclid Data Release 1 (DR1). Euclid Lens Identification Pipeline and Scientific Exploration (ECLIPSE) B: Discovery pipeline overview — 2611.15886
2026-11-13 — Euclid Data Release 1 (DR1). Euclid Lens Identification Pipeline and Scientific Exploration (ECLIPSE) D: Photometric redshifts and the first census of strong lenses in the galaxy evolution framework — 2611.15877
2026-11-13 — Euclid Data Release 1 (DR1). NISP spectroscopy of gravitational arcs and multiple images — 2611.15891
2026-11-16 — Multipoles in the IllustrisTNG simulation galaxies and implications for Strong Gravitational Lens modelling in Time-delay Cosmography — 2611.17538
2026-11-16 — Euclid Data Release 1 (DR1). AstroVink-TREX: Automated strong gravitational lens segmentation as input for mass modelling pipelines — 2611.17894
2026-11-16 — Euclid Data Release 1 (DR1). Enhancing deep-learning models: the impact of image processing and training data selection for strong-lens detection — 2611.17420
2026-11-16 — Probing the Activity History of Repeating Fast Radio Bursts with Cluster Lensing — 2611.17833
2026-11-17 — Euclid Data Release 1 (DR1). Double-source-plane lens candidates — 2611.20166
2026-11-17 — The mass density slope of early-type galaxies: newest results from the redshift distribution of strong gravitational lenses — 2611.20141
