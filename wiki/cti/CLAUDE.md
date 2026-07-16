# CTI AI Assistant — Charge Transfer Inefficiency Wiki

This sub-wiki gives an AI assistant the scientific context of Charge
Transfer Inefficiency (CTI) in CCDs — the physics of charge trapping
and release in silicon, its impact on astronomical imaging, the
forward-model correction algorithms (`arctic`), and the Euclid VIS
detector calibration programme. Sibling of `../lensing/` under
`PyAutoMemory/`, same Karpathy "LLM Wiki" pattern.

## Layout

```
cti/
├── CLAUDE.md           # this file — schema + scope
├── index.md            # top-level navigation
├── log.md              # append-only compilation log
├── concepts/           # CTI physics + algorithmic topics
├── entities/           # Euclid VIS, Hubble ACS, arctic, etc.
└── sources/            # per-topic claim support
```

## Schema

Inherits verbatim from [`../CLAUDE.md`](../CLAUDE.md)
— page types, naming, `[[wiki-links]]`, frontmatter, concept-page
structure, source-collection structure, `status: stub|drafted|reviewed`.
This file only diverges on scope.

## Scope

CTI physics, correction algorithms, trap-pumping calibration, charge
injection, the Euclid VIS detector and calibration pipeline, and the
Hall-Shockley-Read trap-emission theory underlying CTI. Source PDFs live
off-repo (the wiki was compiled from an off-repo CTI/Euclid paper corpus);
what's here is the durable knowledge plus canonical citation metadata in
`../../bibliography/`.

Adjacent topics that link out:
- Sampling / Bayesian inference of trap-density posteriors —
  `../methods/`.
- Cosmological weak-lensing shape biases from residual CTI —
  `../lensing/` ([[weak-lensing]] when written).

## How the assistant should use this wiki

Same protocol as `../CLAUDE.md`: follow concepts/entities to
compact source claims, use canonical metadata from `../../bibliography/`, resolve
downstream keys before editing LaTeX, and never fabricate.
