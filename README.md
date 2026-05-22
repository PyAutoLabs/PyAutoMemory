# PyAutoPaper

The unified paper-management repo for [PyAutoLens](https://github.com/Jammy2211/PyAutoLens)
and related science. Holds a paper reading queue, several
Karpathy-style LLM wikis, and bibliography files. Source PDFs are kept
externally (backed up off-repo as of 2026-05-22) — only their
filename references survive in stubs as historic anchors.

Start at [`index.md`](index.md).

## What's in here

- **[`index.md`](index.md)** — top-level navigation across all sub-wikis.
- **[`reading-queue.md`](reading-queue.md)** — paper reading queue
  (moved from `admin_jammy/papers.md` on 2026-05-22). Section headers
  match topic folders so queued papers can be filed and stubbed when
  acquired.
- **Sub-wikis** (each self-contained, same schema):
  - [`lensing_wiki/`](lensing_wiki/index.md) — strong gravitational
    lensing (the primary sub-wiki).
  - [`smbh_wiki/`](smbh_wiki/index.md) — supermassive black holes,
    binaries, recoil, scouring, GW background.
  - [`cti_wiki/`](cti_wiki/index.md) — Charge Transfer Inefficiency,
    Euclid VIS detector calibration, `arctic`, PyAutoCTI.
  - [`methods_wiki/`](methods_wiki/index.md) — Bayesian inference,
    samplers, deep learning, scientific software, NUFFT, simulations.
  - [`galaxies_wiki/`](galaxies_wiki/index.md) — galaxy formation /
    evolution, ellipticals, bulge/disk decomposition, IFU surveys,
    stellar halos, COSMOS, high-z, halo-galaxy connection.
- **Bibliographies** (`.bib`) at the repo root — kept in git; used by
  LaTeX writing.
- (Gitignored / no longer in repo:) `Strong_Lens/`, `SMBHs/`, `CTI/`,
  …  — the historic PDF folders. Their content was backed up off-repo
  on 2026-05-22 and removed. The `File:` lines in stubs are the
  recovery key if a PDF ever needs to be restored.

## Schema

The schema is defined in
[`lensing_wiki/CLAUDE.md`](lensing_wiki/CLAUDE.md) and inherited by
all sub-wikis. Each sub-wiki has its own `CLAUDE.md` that diverges
only on `## Scope`. Concept-page structure, source-page format,
`[[wiki-links]]`, and frontmatter (`status: stub | drafted |
reviewed`) are uniform across sub-wikis.

## For collaborators

Clone the repo and you have the wikis. You won't see the PDFs — fetch
the ones you need from arXiv / journal sites; the filename in each
stub is usually enough to find the original.

Anything contributed should upgrade a stub to `drafted` after reading
the underlying PDF, and add a line to the relevant sub-wiki's `log.md`.

## Roadmap

- Verify and upgrade per-paper stubs from `stub` → `drafted` as PDFs
  are re-read.
- Distribute `Cancer:` / SETI entries in `reading-queue.md` to a
  dedicated misc sub-wiki if they accumulate enough volume.
- Add new sibling sub-wikis as the library grows (e.g.
  `cosmology_wiki/`, `pipeline_wiki/`) following the same schema.
