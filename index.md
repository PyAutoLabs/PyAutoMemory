# PyAutoPaper — top-level index

Multi-domain paper-management repo. Source PDFs (gitignored) sit
alongside several Karpathy-style LLM wikis. Each sub-wiki is
self-contained and uses the schema in
[`lensing_wiki/CLAUDE.md`](lensing_wiki/CLAUDE.md).

## Sub-wikis

- [`lensing_wiki/`](lensing_wiki/index.md) — **strong gravitational
  lensing.** The primary sub-wiki. Lens equation, mass models, source
  reconstruction, degeneracies, time-delay cosmography, dark-matter
  substructure, surveys (SLACS, BELLS, H0liCOW, TDCOSMO, Euclid Q1,
  HFF), software (PyAutoLens, lenstronomy).
- [`smbh_wiki/`](smbh_wiki/index.md) — **supermassive black holes.**
  Binaries, recoil, scouring, mass functions, GW background
  (NANOGrav), seeds and growth.
- [`cti_wiki/`](cti_wiki/index.md) — **Charge Transfer Inefficiency.**
  CCD trap physics, forward-model correction (`arctic`), trap pumping,
  Euclid VIS calibration, HST ACS, Gaia.
- [`methods_wiki/`](methods_wiki/index.md) — **statistical and
  computational methods.** Bayesian inference, samplers, deep learning,
  probabilistic programming, NUFFT, simulations, scientific software.
- [`galaxies_wiki/`](galaxies_wiki/index.md) — **galaxy formation and
  evolution.** Massive ellipticals (MASSIVE survey), bulge/disk
  decomposition, IFU spectroscopy, stellar halos, COSMOS,
  high-redshift, halo-galaxy connection, galaxy-scale DM geometry.

## Reading queue

- [`reading-queue.md`](reading-queue.md) — paper queue (moved from
  `admin_jammy/papers.md` on 2026-05-22). Section headers (Strong
  Lensing, SMBHs, Galaxy Formation, Dark Matter, Stats, SETI, Cancer)
  match topic folders. When a queued paper is acquired as a PDF, file
  it under the matching folder and stub it in the appropriate
  `<sub>_wiki/sources/*.md`.

## Schema

The schema is defined once in
[`lensing_wiki/CLAUDE.md`](lensing_wiki/CLAUDE.md) and inherited by
all sub-wikis. Each sub-wiki has its own `CLAUDE.md` that diverges
only on the `## Scope` section. Per-page frontmatter, naming
conventions, `[[wiki-links]]`, status flags (`stub | drafted |
reviewed`), and source-page layout are uniform across sub-wikis.

## Status (2026-05-22)

- Initial lensing-wiki build: 193 papers from Strong_Lens/,
  Substructure/, StrongLensCluster/, Dark_Matter_Detection/,
  DarkMatterModels/.
- Sibling sub-wiki build (this commit): ~422 additional papers from
  SMBHs/, CTI/, Euclid/, MassiveEllPaper/, Ellipticals/,
  Bulge_Disk_Decomp/, LightProFFits/, IFUs/, Manga/, COSMOS/,
  StellarHalos/, High_Redshift_galaxies/, Dark_Matter_Geometry/,
  Stats/, GaussianLinearModels/, PPLs/, Deep Learning/, Software/,
  Simulation/, PyAutoLens/, uvplane/, FRBLenses/, WeakLensing/,
  WeakLensingHaloShape/, Clusters/, LSS/, Lyman_Alpha_Forest/,
  SpiralsMorph/, AndrewSuggests/, UnRead/, Summarys/,
  Collaborations/, GWB/, Medical/, plus root-level singletons.
- PDFs deleted from the repo on the same day (backed up externally);
  `File:` lines in stubs are archival relative paths.

All per-paper entries remain `status: stub` (filename-inferred,
unread) — same convention as the initial lensing build. Upgrade to
`drafted` after reading the corresponding PDF; log the upgrade in the
relevant sub-wiki's `log.md`.
