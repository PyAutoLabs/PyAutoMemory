# Compilation log

Append-only record of what was done to this wiki, by whom, and when.

---

## 2026-05-22 — Scope expansion + sibling sub-wikis

**By:** Claude (Opus 4.7, PyAutoLabs feature/pyautopaper-wiki-expansion
session).

**What changed in `lensing_wiki/` itself**

- Added new source-collection pages:
  - `sources/pyautolens-papers.md` — PyAutoLens-self / lead-author
    works pulled from `PyAutoLens/` folder and root-level singletons
    (1807.05566, AutoLens.pdf, autolens_paper1_resubmit*, MN-* proofs,
    RusuMNRASProof).
  - `sources/frb-lenses.md` — `FRBLenses/` (3 papers).
  - `sources/weak-lensing.md` — `WeakLensing/`, `WeakLensingHaloShape/`,
    root `Mandelbaum2018*`.
  - `sources/wdm-and-lya.md` — `Lyman_Alpha_Forest/` papers and stream
    gaps.
  - `sources/reviews-and-summaries.md` — `Summarys/` folder.
- Extended existing source pages:
  - `sources/interferometric-lensing.md` — added `uvplane/` papers.
  - `sources/cluster-lensing.md` — added `Clusters/`, root cluster
    PDFs (Postman2012Abell, Abell1201XRay, Harvey2015*).
  - `sources/dark-matter-substructure.md` — added 11 `Substructure/`
    papers.
  - `sources/gr-cosmology.md` — added root `Planck2015.pdf` and
    `LSS/Lee2016_DM_Evinronments_Bolshoi_Planck.pdf`.

**Sibling sub-wikis created at repo root**

- `smbh_wiki/` — supermassive black holes (44 SMBHs/ PDFs + GWB/).
- `cti_wiki/` — Charge Transfer Inefficiency (40 CTI/, 5 Euclid/,
  root Euclid TP + Henk).
- `methods_wiki/` — statistical and computational methods (Stats,
  GaussianLinearModels, PPLs, Deep Learning, Software, Simulation,
  root NUFFT / PolyChord / MessagePassing / BigData / imfit / Profit
  / PyLops + Medical).
- `galaxies_wiki/` — galaxy formation and evolution (MassiveEllPaper,
  Ellipticals, Bulge_Disk_Decomp, LightProFFits, IFUs, Manga, COSMOS,
  StellarHalos, High_Redshift_galaxies, Dark_Matter_Geometry,
  AndrewSuggests, UnRead, SpiralsMorph, Collaborations, plus most
  root-level singletons).

Each sibling sub-wiki has its own `CLAUDE.md` (inherits schema from
`lensing_wiki/CLAUDE.md`, diverges on `## Scope`), `index.md`,
`log.md`, plus initial concept / entity / sources content.

**Top-level repo restructure**

- New `PyAutoPaper/index.md` — top-level map of all sub-wikis +
  reading queue.
- `PyAutoPaper/README.md` rewritten to describe the multi-wiki layout.
- `admin_jammy/papers.md` moved to `PyAutoPaper/reading-queue.md`
  with a header explaining the move. References fixed in
  `PyAutoPrompt/README.md`, `admin_jammy/README.md`,
  `admin_jammy/claude.md`, and (un-versioned local file)
  `PyAutoLabs/CLAUDE.md`.

**PDF removal (separate commit, same day)**

After backup-location confirmation, all in-repo PDFs were removed
(~615 files across the historic folders). The `File:` line in every
stub is the archival anchor for restoration. Preserved: all `.bib`,
`.sty`, README.md, the no-extension reference files (`Hubble1926.321H`,
`devaucoleurs1948.247D`, `CTI/Hall1952Theory`, etc.), and
`Medical/Liu2024CUPRCT.htm`.

**Status of new stubs**

All entries created in this build are `status: stub` — filename-inferred
summaries, not yet verified against PDFs. Same convention as the
initial 193-paper build.

**Provenance**

Total wiki coverage after this build: ~615 papers across 5 sub-wikis.

---

## 2026-05-22 — Initial build

**By:** Claude (Opus 4.7, PyAutoLens AI-assistant wiki bootstrap session).

**Scope of build:** Strong_Lens (~170 PDFs), Substructure (11), StrongLensCluster (3),
Dark_Matter_Detection (2), DarkMatterModels (5).

**What was created**

- `CLAUDE.md` — schema, page types, naming, cross-reference conventions.
- `index.md` — top-level navigation.
- `concepts/*` — topical concept hubs synthesising the field (lens equation,
  mass models, substructure, time-delay cosmography, degeneracies, source
  reconstruction, lens finding, deep learning, cluster lensing, etc.).
- `entities/*` — SLACS, BELLS, H0liCOW, TDCOSMO, Euclid Q1, HFF, Abell 1201,
  Cosmic Horseshoe, PyAutoLens, lenstronomy, SLaM pipeline, Space Warps.
- `sources/*` — per-topic bibliography stubs. One section per paper. All
  per-paper summaries in this initial build are inferred from filenames
  plus general field knowledge and are marked `status: stub`. They are
  **not yet verified against the PDF**.

**Known gaps / explicit TODOs**

- Every source-stub is unread. The PyAutoLens assistant should treat the
  summary lines as priors, not facts, until the corresponding PDF has been
  read and the stub upgraded to `status: drafted`.
- A handful of filenames are ambiguous (typos, generic dates, working
  drafts like `1901.07801.pdf`, `detections_stochastic_no_zeros.pdf`,
  `MN-24-0938-MJ_Proof_hi.pdf`); these are listed under
  `sources/unclassified.md` for manual triage.
- Adjacent folders (`WeakLensing/`, `Ellipticals/`, `Bulge_Disk_Decomp/`,
  `Deep Learning/`, `Stats/`, `IFUs/`, `SMBHs/`, root-level `AutoLens.pdf` &
  `autolens_paper1_resubmit_*.pdf`) contain material a PyAutoLens
  assistant would benefit from. User chose to defer ingesting these in
  this build. To extend later, follow the procedure in `CLAUDE.md`.

**Provenance note**

The format follows Karpathy's LLM Wiki pattern (April 2026 gist): raw PDFs
are immutable, the wiki layer is compiled and cross-linked, and the
schema lives in `CLAUDE.md` so the maintaining LLM has a stable contract.

---

## 2026-06-22 — Added canonical citation metadata

**By:** Codex (maintainer session).

Added the repository-wide canonical BibTeX and alias layer, validation tooling, and compact
claim-support schema inherited by every sub-wiki. Migrated the verified lens-finding and
Euclid Q1 entries without retaining local PDF paths or abstract summaries.

---

## 2026-06-22 — Migrated lensing transient citations

Verified and migrated the two lensed-supernova and three plasma-lensing entries to compact
claim support. Corrected the legacy Rydberg and Rogers labels and updated the lensed-supernova
concept references without retaining local PDF paths.

---

## 2026-06-22 — Migrated microlensing IMF citation

Verified the Jiménez-Vicente & Mediavilla lens-galaxy IMF paper and replaced its misspelt,
filename-derived stub with compact claim support and canonical citation metadata.
