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
last digest: 2026-11-25
2026-11-19 — A twist in the tail: GWLENS, a fast and accurate tool for wave-optics lensing of gravitational waves — 2611.24621
2026-11-23 — Baryon-Enhanced Strong Lensing Signatures of Self-Interacting Dark Matter Subhalos — 2611.27249
2026-11-24 — Euclid Data Release 1 (DR1). Learning machine learning: Investigating the complementarity and biases of strong gravitational lens finding networks on Euclid data — 2611.31231
2026-11-25 — VENUS: A Census of Strong Lensing in a 60-Cluster JWST Survey — 2611.33142
2026-11-25 — Probing the X-Ray Structure of the $z = 2.38$ Strongly Lensed Quasar J1721+8842, the First Einstein Zig-Zag Lens, Down to $140\ \mathrm{pc}$ — 2611.31386
