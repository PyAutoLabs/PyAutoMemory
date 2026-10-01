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
last digest: 2026-10-01
2026-09-29 — Improving Lens Modelling from Ground-Based Imaging with Deconvolution — 2609.34305
2026-09-29 — Constraining the Light Curves of Magnified Stellar Events at z ~ 0.725 — 2609.33925
2026-09-29 — SLICE: Unveiling the Multi-Component Merging Core of SPT-CLJ1150-2805 Through Strong-Lensing Mass Modelling — 2609.31944
2026-09-30 — Detecting Extragalactic Exoplanets With Fast Radio Burst Nanolensing — 2609.36988
2026-09-30 — LUMA: A CNN for Strong Gravitational Lens Searches in Astronomical Imaging — 2609.36857
2026-09-30 — JWST lensed quasar dark matter survey V: Hints of self-interacting dark matter from 29 quadruply imaged quasars — 2609.35974
2026-10-01 — Sub-kiloparsec Test of the Kennicutt-Schmidt Relation in a Strongly Lensed Dusty Star-Forming Galaxy at z~2.78 — 2609.40233
2026-10-01 — Effects of a central dark matter core on time-delay cosmography with galaxy clusters — 2609.39796
2026-10-01 — Stacked strong and weak lensing united: Improved measurement of the stellar and dark matter distributions in massive early-type galaxies at $z\sim 0.5$ — 2609.39040
2026-10-01 — Toward Detecting the Moving Lens Effect with Optical Spectroscopy — 2609.38457
2026-10-01 — Testing Offsets Between Cluster-Scale Halos and BCGs in Strong Lensing Models Using the Jackknife Method — 2609.38310
