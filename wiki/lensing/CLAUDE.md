# PyAutoLens AI Assistant — Strong Lensing Wiki

This sub-wiki gives a PyAutoLens AI assistant broad scientific context for
strong gravitational lensing: the lens equation, mass models, source
reconstruction, degeneracies, time-delay cosmography, dark-matter
substructure, the major surveys and the software landscape. It is the
primary sub-wiki; the shared schema is defined in
[`../CLAUDE.md`](../CLAUDE.md).

## Schema

Inherits verbatim from [`../CLAUDE.md`](../CLAUDE.md) — page types, naming,
`[[wiki-links]]`, frontmatter, concept-page structure, source-collection
structure, `status: stub|drafted|reviewed`. This file only diverges on
scope. In concept pages, "Why it matters" is written for PyAutoLens users
("Why it matters for PyAutoLens").

## Scope

Strong gravitational lensing end to end: galaxy- and cluster-scale lenses,
substructure and dark-matter detection, lens searches and samples, source
reconstruction, cosmography. Source PDFs live off-repo (the wiki was
compiled from an off-repo corpus: Strong_Lens, Substructure,
StrongLensCluster, Dark_Matter_Detection, DarkMatterModels); what's here is
the durable knowledge plus canonical citation metadata in
`../../bibliography/`.

Adjacent topics that link out:
- Weak lensing, LSS, clusters as cosmology probes — out of scope until
  explicitly added; see `log.md` for the decision.
- Bayesian inference and samplers — `../methods/`.
- Galaxy structure and evolution of the deflector population —
  `../galaxies/`.

## How the assistant should use this wiki

Same protocol as [`../CLAUDE.md`](../CLAUDE.md): follow concepts/entities to
compact source claims, use canonical metadata from `../../bibliography/`,
resolve downstream keys before editing LaTeX, and never fabricate.
