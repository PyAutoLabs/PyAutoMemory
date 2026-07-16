# Galaxies AI Assistant — Galaxy Formation & Evolution Wiki

This sub-wiki gives an AI assistant the scientific context of galaxy
formation and evolution as it bears on PyAutoLens / PyAutoGalaxy work:
elliptical-galaxy structure, bulge/disk/halo decompositions, light-
profile fitting, stellar halos, IFU kinematics, high-redshift galaxies,
COSMOS / COSMOS-Web morphology, dark-matter halo geometry from
galaxy-scale dynamics, and halo-galaxy connection statistics. Sibling
of `../lensing/` under `PyAutoMemory/`, same Karpathy "LLM Wiki"
pattern.

## Layout

```
galaxies/
├── CLAUDE.md           # this file — schema + scope
├── index.md            # top-level navigation
├── log.md              # append-only compilation log
├── concepts/           # galaxy-formation & morphology topics
├── entities/           # surveys (MaNGA, SAMI, COSMOS-Web), notable galaxies
└── sources/            # per-topic claim support
```

## Schema

Inherits verbatim from [`../CLAUDE.md`](../CLAUDE.md).

## Scope

In-scope folders:

- `MassiveEllPaper/` — massive elliptical galaxy paper drafts and refs.
- `Ellipticals/` — elliptical-galaxy structure and kinematics.
- `Bulge_Disk_Decomp/` — bulge+disk image decomposition methodology.
- `LightProFFits/` — light-profile fitting (Sérsic, MGE, free-form).
- `IFUs/` — integral-field unit spectroscopy methodology and results.
- `Manga/` — MaNGA survey-specific results.
- `COSMOS/` — COSMOS / COSMOS-Web survey papers.
- `StellarHalos/` — stellar-halo science, halo-mass proxies.
- `High_Redshift_galaxies/` — z > 4 galaxy structure, JWST results.
- `Dark_Matter_Geometry/` — galaxy-scale dark-matter halo shapes,
  rotation-curve inference, dwarf-galaxy dynamics (this is *not* the
  cluster/lensing dark-matter geometry — those live in
  `../lensing/`).
- Several root-level singletons: `ETGKine1.pdf`, `ETGKine2.pdf`,
  `Tinker2017*.pdf`, `Tinker2018*.pdf`, `Charlton2017*.pdf`,
  `Leathuad2018LensingisLow.pdf`, `Saito2018*.pdf`, `Oh2016*.pdf`,
  `Cohen2018DragonflyV.pdf`, `Greco2017*.pdf`, `Ferraras2019*.pdf`,
  `COSMOSWeb.pdf`, `Hubble1926.321H`, `RimondiniGaia2018.pdf`,
  `DuttonDarkMatterCore2018.pdf`.

Adjacent topics that link out:
- Stellar mass / lensing constraints —
  `../lensing/concepts/bulge-halo-decomposition.md`.
- Dark-matter substructure as seen in *lensed* systems —
  `../lensing/concepts/dark-matter-substructure.md`.
- SMBH-host galaxy scaling relations — `../smbh/`.

## How the assistant should use this wiki

Same protocol as `../CLAUDE.md`.
