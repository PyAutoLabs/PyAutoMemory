# Compilation log

Append-only record of what was done to this wiki, by whom, and when.

---

## 2026-05-22 — Initial build

**By:** Claude (Opus 4.7, PyAutoLabs feature/pyautopaper-wiki-expansion
session).

**Scope of build:** `SMBHs/` (44 PDFs) + `GWB/` (1) + root-level
`Krist2011TinyTim.pdf`.

**What was created**

- `CLAUDE.md` — inherits schema from `lensing_wiki/CLAUDE.md`,
  scope-restricted to SMBH physics.
- `index.md` — top-level navigation.
- `concepts/` — `smbh-overview`, `smbh-binaries`, `smbh-scouring`,
  `gw-background`.
- `entities/` — `nanograv`, `rabbits`, `ketju`.
- `sources/` — `smbh-host-scaling`, `smbh-mass-measurement`,
  `smbh-recoil-scouring`, `smbh-binaries`, `smbh-seeds-growth`,
  `smbh-mass-functions`, `gw-background`.

**Status of stubs**

All per-paper stubs are `status: stub` — filename-inferred summaries,
not verified against PDFs. Liao 2024 RABBITS II appears in both
`sources-smbh-binaries.md` and `sources-smbh-recoil-scouring.md` as a
deliberate cross-listing.

**Provenance**

Same Karpathy "LLM Wiki" pattern as the lensing sub-wiki. The schema
contract lives at `../lensing_wiki/CLAUDE.md`.
