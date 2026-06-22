# PyAutoPaper

The unified paper-management repo for [PyAutoLens](https://github.com/Jammy2211/PyAutoLens)
and related science. Holds a paper reading queue, several
Karpathy-style LLM wikis, and a paired canonical bibliography. Source PDFs
are kept externally (backed up off-repo as of 2026-05-22).

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
- **[`bibliography/`](bibliography/README.md)** — canonical BibTeX metadata,
  aliases, and citation validation shared by every sub-wiki.
- **Legacy/project bibliographies** (`.bib`) at the repo root — retained for
  existing LaTeX projects; not the canonical metadata layer.
- (Gitignored / no longer in repo:) historic PDF folders such as
  `Strong_Lens/` and `SMBHs/`; their content was backed up off-repo.

## Schema

The schema is defined in [`lensing_wiki/CLAUDE.md`](lensing_wiki/CLAUDE.md)
and inherited by all sub-wikis. Wiki source entries provide semantic claim
support; `bibliography/pyautopaper.bib` provides canonical citation metadata.

## For collaborators

Clone the repo and you have the wikis and canonical citation metadata. Fetch
papers from public DOI/arXiv/journal references when claim verification is needed.

New papers must update canonical metadata and compact claim support together,
then pass `make validate-literature-citations`.

## Roadmap

- Verify and upgrade per-paper stubs from `stub` → `drafted` as PDFs
  are re-read.
- Distribute `Cancer:` / SETI entries in `reading-queue.md` to a
  dedicated misc sub-wiki if they accumulate enough volume.
- Add new sibling sub-wikis as the library grows (e.g.
  `cosmology_wiki/`, `pipeline_wiki/`) following the same schema.
