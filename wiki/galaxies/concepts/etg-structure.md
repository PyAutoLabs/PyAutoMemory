---
title: ETG structure
type: concept
topics: [etg-structure, ellipticals]
sources:
  - MassiveEllPaper/Ma2014MassiveIOverview.pdf
  - LightProFFits/Peng_2010_AJ_139_2097.pdf
status: stub
---

# ETG structure

## TL;DR

Early-type galaxies (ETGs) are the typical hosts of strong-lens
galaxies and the largest population modelled by PyAutoLens. Their
surface-brightness profiles are well-fit by Sérsic (or Sérsic + extra
component) profiles; the most massive ETGs show a "core" inside ~kpc
from SMBH-binary scouring (cross-link `../smbh/concepts/smbh-scouring.md`);
they often contain a smaller inner extra-light disk or pseudo-bulge.

## What it is

Standard PyAutoLens lens-light model:

- **Outer Sérsic** with n ~ 4 (de Vaucouleurs) for massive ETGs, n ~ 1
  (exponential) for disks.
- **Inner component** — extra-light bulge (compact, dense),
  pseudo-bulge (disk-like, lower-n), or core (carved out by SMBH
  binaries).
- **Halo** — diffuse outer envelope; usually faint enough to be
  absorbed into the outer Sérsic in galaxy-galaxy lens fits.

ETGs split kinematically into slow rotators (~triaxial, V/σ < 0.2,
dispersion-dominated) and fast rotators (axisymmetric oblate
rotators, V/σ > 0.2) — the ATLAS3D / SLUGGS / SAMI / MaNGA
classification.

## Why it matters for PyAutoLens

The lens-light model directly affects the lens-mass fit because (a)
joint light + mass fits propagate light-model errors into mass-model
errors, and (b) the lens-light subtraction is what reveals the source.
Mis-modelled cores or compact inner bulges leave residuals that the
source pixelisation then has to absorb, biasing source reconstruction
and inferred mass slopes.

## Key references

- MASSIVE survey overview: [[sources-massive-ellipticals#ma-2014-massive-i-overview]].
- ETG kinematic classification: [[sources-ifu-spectroscopy#emsellem-2011-atlas3d-kinematic-misalignments]].
- Core / extra-light dichotomy: [[sources-massive-ellipticals#kormendy-bender-2013-cores-in-ellipticals]]
  (cross-link `../smbh/`).
- Three-component decompositions: [[sources-massive-ellipticals#huang-2012-three-component-etg-models]].

## See also

- [[etg-kinematics]]
- [[massive-ellipticals]]
- [[bulge-disk-decomposition-galaxies]]
- `../lensing/concepts/bulge-halo-decomposition.md`
- `../smbh/concepts/smbh-scouring.md`
