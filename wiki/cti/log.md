# Compilation log

Append-only record of what was done to this wiki, by whom, and when.

---

## 2026-05-22 — Initial build

**By:** Claude (Opus 4.7, PyAutoLabs feature/pyautopaper-wiki-expansion
session).

**Scope of build:** `CTI/` (40 PDFs) + `Euclid/` (5) + root-level
`Euclid_TP_serial.pdf`, `CTI_Calibration_Henk.pdf`, and the
no-extension reference `Hall1952Theory`.

**What was created**

- `CLAUDE.md` — inherits schema from `lensing_wiki/CLAUDE.md`,
  scope-restricted to CTI / Euclid VIS detector physics.
- `index.md` — top-level navigation.
- `concepts/` — `charge-transfer-inefficiency`.
- `entities/` — `euclid-vis`, `arctic`.
- `sources/` — `cti-detector-physics`, `cti-correction-algorithms`,
  `trap-pumping`, `gaia-cti`, `euclid-vis-calibration`,
  `cti-shape-bias`, `cti-xray-and-cosmic-rays`, `hst-acs-cti`.

**Status of stubs**

All per-paper stubs are `status: stub`. Two CTI-folder files flagged
as non-papers for cleanup attention:
- `CTI/PastedGraphic-2.pdf` — likely a screenshot.
- `CTI/Contract change JN-signed.pdf` — administrative document.

**Provenance**

Same Karpathy "LLM Wiki" pattern as the lensing sub-wiki. Includes
the planned PyAutoCTI reference (`Nightingale 2024 PyAutoCTI`) as a
key sibling tool in the PyAuto stack.
