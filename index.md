# PyAutoMemory — top-level index

The PyAuto organism's long-term knowledge: a multi-domain knowledge base of
accumulated scientific and project knowledge, organised as several
Karpathy-style LLM wikis over a shared canonical bibliography. Each sub-wiki uses
the schema in [`wiki/CLAUDE.md`](wiki/CLAUDE.md).

## Sub-wikis

- [`wiki/lensing/`](wiki/lensing/index.md) — **strong gravitational
  lensing.** The primary sub-wiki. Lens equation, mass models, source
  reconstruction, degeneracies, time-delay cosmography, dark-matter
  substructure, surveys (SLACS, BELLS, H0liCOW, TDCOSMO, Euclid Q1,
  HFF), software (PyAutoLens, lenstronomy).
- [`wiki/smbh/`](wiki/smbh/index.md) — **supermassive black holes.**
  Binaries, recoil, scouring, mass functions, GW background
  (NANOGrav), seeds and growth.
- [`wiki/cti/`](wiki/cti/index.md) — **Charge Transfer Inefficiency.**
  CCD trap physics, forward-model correction (`arctic`), trap pumping,
  Euclid VIS calibration, HST ACS, Gaia.
- [`wiki/methods/`](wiki/methods/index.md) — **statistical and
  computational methods.** Bayesian inference, samplers, deep learning,
  probabilistic programming, NUFFT, simulations, scientific software.
- [`wiki/galaxies/`](wiki/galaxies/index.md) — **galaxy formation and
  evolution.** Massive ellipticals (MASSIVE survey), bulge/disk
  decomposition, IFU spectroscopy, stellar halos, COSMOS,
  high-redshift, halo-galaxy connection, galaxy-scale DM geometry.

## Reading queue

- [`reading-queue.md`](reading-queue.md) — paper queue (moved from
  `admin_jammy/papers.md` on 2026-05-22). Section headers (Strong
  Lensing, SMBHs, Galaxy Formation, Dark Matter, Stats, SETI, Cancer)
  match the sub-wiki domains. When a queued paper is read, stub it in
  the appropriate sub-wiki `sources/*.md` and add its canonical entry
  to `bibliography/` — the PDF itself stays off-repo, never committed.

## Schema

The schema is defined once in
[`wiki/CLAUDE.md`](wiki/CLAUDE.md) and inherited by
all sub-wikis. Each sub-wiki has its own `CLAUDE.md` that diverges
only on the `## Scope` section. Per-page frontmatter, naming
conventions, `[[wiki-links]]`, status flags (`stub | drafted |
reviewed`), and source-page layout are uniform across sub-wikis.

## Citation metadata

The sub-wikis explain which claims papers support. Canonical BibTeX metadata,
key aliases, downstream-project resolution rules, and validation live in
[`bibliography/`](bibliography/README.md).

## Provenance

The wikis were seeded in 2026-05 from a ~615-paper personal PDF library
(the PDFs themselves were deleted from the repo the same day, backed up
externally). Most legacy per-paper entries remain filename-inferred stubs:
upgrade them to compact, claim-oriented `drafted` entries only after
verifying the paper, and log the change in the relevant sub-wiki. The live
counts — pages, maturity, unresolved citation keys, reading queue — are on
the [knowledge board](https://pyautolabs.github.io/PyAutoMemory/).
