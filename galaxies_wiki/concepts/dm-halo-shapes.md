---
title: Dark-matter halo shapes
type: concept
topics: [dm-halo-shapes, galaxy-scale]
sources:
  - Dark_Matter_Geometry/BailinShapesAngMom2005.pdf
  - Dark_Matter_Geometry/TennitiIntrSlignDiskEll2015.pdf
status: stub
---

# Dark-matter halo shapes (galaxy-scale)

## TL;DR

LCDM predicts triaxial dark-matter halos at galaxy scales; baryonic
processes (gas dissipation, AGN feedback) round the inner halo
relative to the dark-matter-only prediction. Observational probes at
galaxy scale include satellite-galaxy alignments, intrinsic-shape
inference from photometry + kinematics, and weak / strong lensing.
The geometric satellite-alignment work in this sub-wiki is the
companion probe to strong-lensing halo-shape constraints in
`../lensing_wiki/`.

## What it is

Three families of galaxy-scale halo-shape probe in this collection:

- **Satellite anisotropic distributions** — central galaxies'
  satellites preferentially lie along the major axis of their host
  (e.g. Brainerd 2005, Wang 2005, Wang 2014).
- **Plane-of-satellites** — coplanar satellite arrangements as
  potential LCDM challenges (Cautun 2015).
- **Intrinsic 3D shape inference** — joint photometric / kinematic
  inversion gives a posterior on intrinsic axis ratios (Weijmans 2014
  — see `sources-ifu-spectroscopy.md`).

## Why it matters for PyAutoLens

Lensing measures the projected potential. Joint use of satellite-
alignment statistics + strong-lensing fits can in principle reveal
halo triaxiality on galaxy scales. Most direct relevance: a triaxial
halo viewed along an off-axis line of sight contributes external-shear-
like structure that the lens model would absorb into nuisance shear
parameters — a possible systematic on inferred shear / convergence.

## Key references

- Satellite alignment statistics: [[sources-dark-matter-geometry-galaxies]].
- Intrinsic ETG shapes: [[sources-ifu-spectroscopy#weijmans-2014-intrinsic-shape-etg-kinematic-misalignments]].
- Hydrodynamic comparison: [[sources-dark-matter-geometry-galaxies#tenneti-2015-intrinsic-alignment-disk-etg]].

## See also

- [[stellar-mass-halo-mass-relation]]
- [[../lensing_wiki/concepts/external-convergence-shear.md]]
- [[../lensing_wiki/sources-dark-matter-physics]]
