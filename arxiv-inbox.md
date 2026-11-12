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
last digest: 2026-11-12
2026-11-06 — Confirming HSC strong lens candidates with DESI Spectroscopy. II. Analysis of 80 galaxy-scale systems with lens redshifts above 0.8 — 2611.07524
2026-11-06 — Dust Survival in Lensed Quiescent Galaxies at $z>1$ Depends on How They Quench — 2611.07237
2026-11-09 — Lessons from double-plane lenses for galaxy profiles, the Hubble tension, and the mass-sheet degeneracy — 2611.09856
2026-11-09 — Through Ups and Downs: the Transient Lensing Behaviour of SIDM halos undergoing Core Collapse — 2611.09546
2026-11-09 — Short-term optical monitoring of quadruply imaged quasars — 2611.08633
2026-11-09 — VENUS: Strong Lens Mass Models and Einstein Radii of 60 Galaxy Clusters — 2611.08630
2026-11-10 — Revisiting the Einstein Cross with X-shooter spectra: New estimates of accretion disk parameters and broad emission line profiles from microlensing — 2611.12448
2026-11-11 — Leveraging Lensing-driven Early Warnings: Joint Detectability of lensed Gravitational Waves and their LSST Optical Counterparts — 2611.14343
2026-11-11 — The PAU Survey: Dissecting strong-lensing systems with narrow-band photometric redshifts — 2611.14229
