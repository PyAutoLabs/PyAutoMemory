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
last digest: 2026-09-09
2026-09-07 — Probing Dark Matter with Strongly Lensed Binary Black Hole Mergers: Prospects in the Near Future — 2609.05020
2026-09-07 — ALPACA I: Controlling source and PSF systematics in JWST time-delay cosmography with differentiable lens modeling — 2609.04312
2026-09-09 — Harnessing stellar kinematics to constrain dark energy with the double-source-plane gravitational lens SDSS J0946+1006 — 2609.08573
2026-09-09 — $\texttt{LensFactory.jl}$: A general-purpose strong lens modeling package — 2609.08649
2026-09-09 — Observation-driven simulations of strong lensing galaxy clusters — 2609.07840
2026-09-09 — LEGGOS: Direct abundances of N, O, Ne, S, and Ar in five lensed galaxies at Cosmic Noon — 2609.07851
2026-09-09 — LEGGOS: A Shocking Lack of Evidence for Shocks at sub-kiloparsec Scales at 2 < z < 4 — 2609.07850
