# PyAutoMemory

The **long-term knowledge** of the PyAuto ecosystem as it grows into a software
organism. PyAutoMemory is where the organism stores and organises what it has
learned — literature summaries, LLM-generated wikis, reading queues, accumulated
scientific knowledge, and project knowledge — for [PyAutoLens](https://github.com/Jammy2211/PyAutoLens)
and related science.

Start at [`index.md`](index.md).

## What PyAutoMemory stores

PyAutoMemory holds what the organism has learned, not just a pile of papers:

- **Literature summaries** — Karpathy-style LLM wikis distilling what each source
  actually says and which claims it supports.
- **Scientific knowledge** — concepts, entities, and cross-linked explanations
  spanning strong lensing, supermassive black holes, charge-transfer
  inefficiency, statistical/computational methods, and galaxy formation.
- **Project knowledge** — reading queues, canonical citation metadata, and the
  conventions that keep the knowledge base consistent and verifiable.
- **Accumulated / learned information** — knowledge the organism acquires over
  time, filed and stubbed so it can be revisited, upgraded, and cited.

Source PDFs are kept externally (backed up off-repo as of 2026-05-22); what lives
here is the distilled, durable knowledge.

## The organism

PyAutoMemory is the Memory organ of the PyAuto organism — it stores what the
organism has learned. The organs and their boundaries are defined once in
`PyAutoBrain/ORGANISM.md`; how agents should read this repo is defined in
[`AGENTS.md`](AGENTS.md).

## What's in here

- **[`index.md`](index.md)** — top-level navigation across all sub-wikis.
- **[`reading-queue.md`](reading-queue.md)** — reading queue
  (moved from `admin_jammy/papers.md` on 2026-05-22). Section headers
  match topic folders so queued sources can be filed and stubbed when
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
support; `bibliography/pyautomemory.bib` provides canonical citation metadata.

## For collaborators

Clone the repo and you have the wikis and canonical citation metadata. Fetch
sources from public DOI/arXiv/journal references when claim verification is needed.

New knowledge must update canonical metadata and compact claim support together,
then pass `make validate-literature-citations`.

## Roadmap

- Verify and upgrade per-source stubs from `stub` → `drafted` as material
  is re-read.
- Distribute `Cancer:` / SETI entries in `reading-queue.md` to a
  dedicated misc sub-wiki if they accumulate enough volume.
- Add new sibling sub-wikis as the knowledge base grows (e.g.
  `cosmology_wiki/`, `pipeline_wiki/`) following the same schema.
