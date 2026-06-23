# SMBH AI Assistant — Supermassive Black Holes Wiki

This sub-wiki gives an AI assistant the scientific context of supermassive
black holes (SMBHs): their binaries, recoil, scouring of galactic nuclei,
mass functions, and the nanohertz gravitational-wave background. It is a
sibling of `lensing_wiki/` under the same `PyAutoPaper/` repo and follows
the same Karpathy "LLM Wiki" pattern: the PDFs in surrounding folders are
the immutable raw layer (gitignored), and this `smbh_wiki/` folder is the
compiled, cross-linked knowledge layer that lives in git.

## Layout

```
smbh_wiki/
├── CLAUDE.md           # this file — schema + scope
├── index.md            # top-level navigation
├── log.md              # append-only compilation log
├── concepts/           # one topic per page — the physics
├── entities/           # named surveys, collaborations, codes
└── sources/            # per-topic claim support (one paper = one section)
```

## Schema

All schema rules — page types, naming, `[[wiki-links]]`, frontmatter,
concept page structure, source-collection structure, status flags
(`stub | drafted | reviewed`) — are inherited verbatim from
[`../lensing_wiki/CLAUDE.md`](../lensing_wiki/CLAUDE.md). Read that file
first; this one only diverges on scope.

Cross-wiki links work: `[[../lensing_wiki/concepts/smbh-from-lensing]]`
or just `[[smbh-from-lensing]]` if the resolver is sub-wiki-aware.

## Scope

In-scope folders (PDFs live alongside this wiki, gitignored):

- `SMBHs/` — primary; ~44 PDFs on SMBH formation, binaries, recoil,
  scouring, dual AGN, mass functions.
- `GWB/` — gravitational-wave background (pulsar-timing array
  detections, theoretical predictions).
- Selected root-level PDFs assigned by topic (e.g. `Krist2011TinyTim.pdf`
  for HST/JWST PSF modelling of AGN host decompositions).

Adjacent topics that link out:
- Galaxy-scale dynamics, host-galaxy properties — `../galaxies_wiki/`.
- Bayesian inference on hierarchical population models — `../methods_wiki/`.
- SMBHs detected/constrained via strong lensing — `../lensing_wiki/`
  ([[smbh-from-lensing]]).

## How the assistant should use this wiki

Follow the protocol in `../lensing_wiki/CLAUDE.md`: trace claims through compact
source entries, use canonical metadata from `../bibliography/`, resolve keys
against downstream projects before changing LaTeX, and never fabricate.
