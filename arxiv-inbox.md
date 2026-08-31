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
last digest: 2026-08-31
2026-08-25 — Strong Lensing Cosmology with Population-level Calibrated Neural Ratio Estimation — 2608.23534
2026-08-25 — Mapping the Information Geometry of an Unresolved Dark Matter Population using a Differentiable Strong Lensing Simulator — 2608.18224
2026-08-27 — Accretion Disk Sizes and Temperature Profiles in Lensed Quasars: NIR Microlensing Challenges Thin Disk Theory — 2608.26039
2026-08-28 — HOLISMOKES -- XVIII. Cosmology with strongly lensed type II supernovae: Effects of instrumental setups on $H_0$ — 2608.26331
2026-08-31 — Follow-up of SN 2025wny I: Space-based Observations of the First Multiply-imaged Superluminous Supernova — 2608.28413
2026-08-31 — Follow-up of SN 2025wny V: Lens Modelling and Cosmography of a Strongly Lensed Superluminous Supernova at $z = 2.015$ using Space Data — 2608.28430
2026-08-31 — TDCOSMO. XXVII. JWST-based Lens Models and H$_0$ Measurement of WFI2033, HE0435, and PG1115 — 2608.27566
2026-08-31 — Follow-up of SN 2025wny II: Superluminous Supernova Physics at Cosmic Noon — 2608.28415
2026-08-31 — Follow-up of SN 2025wny III: Spectroscopic Time-delay Measurements of a Strongly Gravitationally Lensed Superluminous Supernova — 2608.28416
2026-08-31 — Follow-up of SN 2025wny IV: Photometric Time-delay Measurements of a Strongly Lensed Superluminous Supernova — 2608.28427
2026-08-31 — Measuring Extragalactic Microlens Masses and Motions in Strongly Lensed Quasar Systems with Intensity Interferometry — 2608.27577
