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
last digest: 2026-08-28
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
