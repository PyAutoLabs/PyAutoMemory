# PyAutoPaper

A personal paper library and writing context repo for
[PyAutoLens](https://github.com/Jammy2211/PyAutoLens) and related
science. Holds source PDFs locally (gitignored) and compiled
LLM-readable wikis in git.

## What's in here

- **`lensing_wiki/`** — the strong-gravitational-lensing sub-wiki.
  Topical concept pages, named-entity pages (surveys, lenses, software),
  and per-topic bibliographies covering ~190 papers across
  `Strong_Lens/`, `Substructure/`, `StrongLensCluster/`,
  `Dark_Matter_Detection/`, `DarkMatterModels/`. Built on Karpathy's
  "LLM Wiki" pattern: the PDFs are the raw layer, the wiki is the
  compiled layer an AI assistant reads at query time. Start at
  [`lensing_wiki/index.md`](lensing_wiki/index.md). See
  [`lensing_wiki/CLAUDE.md`](lensing_wiki/CLAUDE.md) for the schema.
- **`Strong_Lens/`, `Substructure/`, …** (gitignored) — the PDF folders.
  Kept locally so the wiki can reference them; not pushed because the
  PDFs are available from arXiv / journal sites.

## For collaborators

Clone the repo and you have the wikis. You won't see the PDFs — fetch
them from the URLs cited in each source page if you need them. The
wikis are self-contained scientific context: every concept page is a
synthesis, every source page lists the file path and a one-paragraph
stub keyed to the cited PDF.

The wiki status of each source page is tracked in its frontmatter
(`status: stub | drafted | reviewed`). In the initial build all
per-paper stubs are `stub` — inferred from filenames and field
knowledge, not yet verified against the PDFs. Anything contributed
should upgrade stubs to `drafted` after the corresponding PDF has been
read, and add an entry to `lensing_wiki/log.md`.

## Roadmap

- Verify and upgrade per-paper stubs from `stub` → `drafted`.
- Add tangential folders (`WeakLensing/`, `Ellipticals/`,
  `Deep Learning/`, `Stats/`, …) to scope.
- Add sibling sub-wikis as the library grows (e.g. `imaging_wiki/`,
  `cosmology_wiki/`) following the same schema.
