# CTI AI Assistant — Charge Transfer Inefficiency Wiki

This sub-wiki gives an AI assistant the scientific context of Charge
Transfer Inefficiency (CTI) in CCDs — the physics of charge trapping
and release in silicon, its impact on astronomical imaging, the
forward-model correction algorithms (`arctic`), and the Euclid VIS
detector calibration programme. Sibling of `lensing_wiki/` under
`PyAutoPaper/`, same Karpathy "LLM Wiki" pattern.

## Layout

```
cti_wiki/
├── CLAUDE.md           # this file — schema + scope
├── index.md            # top-level navigation
├── log.md              # append-only compilation log
├── concepts/           # CTI physics + algorithmic topics
├── entities/           # Euclid VIS, Hubble ACS, arctic, etc.
└── sources/            # per-topic bibliography pages
```

## Schema

Inherits verbatim from [`../lensing_wiki/CLAUDE.md`](../lensing_wiki/CLAUDE.md)
— page types, naming, `[[wiki-links]]`, frontmatter, concept-page
structure, source-collection structure, `status: stub|drafted|reviewed`.
This file only diverges on scope.

## Scope

In-scope folders:

- `CTI/` — primary; ~40 PDFs on CTI physics, correction algorithms,
  trap-pumping calibration, charge injection lines.
- `Euclid/` — 5 PDFs on Euclid VIS detector and calibration pipeline.
- Root-level `Euclid_TP_serial.pdf` (trap-pumping serial-direction
  measurements) and `CTI_Calibration_Henk.pdf`.
- Root-level `Hall1952Theory` (no-extension reference file) on the
  Hall-Shockley-Read trap-emission theory underlying CTI.

Adjacent topics that link out:
- Sampling / Bayesian inference of trap-density posteriors —
  `../methods_wiki/`.
- Cosmological weak-lensing shape biases from residual CTI —
  `../lensing_wiki/` ([[weak-lensing]] when written).

## How the assistant should use this wiki

Same protocol as `../lensing_wiki/CLAUDE.md`: open `index.md`, follow
`concepts/` or `entities/`, cite via `[[sources-topic#author-year]]`,
upgrade stubs after reading the PDF, never fabricate.
