---
title: SMBH overview
type: concept
topics: [smbh, host-galaxies]
sources:
  - SMBHs/Kormendy1995SearchInward.pdf
  - SMBHs/Ferrarese2000VeloDisp.pdf
  - SMBHs/Gebhardt2000SMBHVelDisp.pdf
status: stub
---

# SMBH overview

## TL;DR

Supermassive black holes (SMBHs) sit at the centres of essentially all
massive galaxies. Their masses (10^6–10^10 M☉) correlate tightly with
host-bulge properties (M–σ, M–M_bulge), and their merger history
sources the nanohertz gravitational-wave background. For PyAutoLens
work, SMBHs matter because (a) they can sit inside the lensing
galaxy and perturb central images, (b) cored ellipticals carry their
SMBH-binary scouring fingerprint, and (c) lensed quasars are
SMBH-powered.

## What they are

SMBHs grow over cosmic time through gas accretion (quasar phases) and
SMBH-SMBH mergers (driven by host-galaxy mergers). Their cosmological
mass function is set by both channels and inferred from the local
demographics + the AGN luminosity function (Soltan argument).

## Why they matter for PyAutoLens

- **Lensed quasars** are powered by SMBHs; quasar microlensing
  constrains accretion-disk sizes and SMBH masses.
- **Central images** of lensed sources test the central mass slope and,
  in principle, the existence of the lensing-galaxy SMBH.
- **Cored ETGs** (the typical lens-galaxy hosts) bear the dynamical
  scouring footprint of past SMBH-binary mergers — a real concern when
  modelling the innermost light and mass profile.

## Key references

- M–σ discovery: [[sources-smbh-host-scaling#ferrarese-merritt-2000]],
  [[sources-smbh-host-scaling#gebhardt-2000]].
- Coevolution review: [[sources-smbh-host-scaling#kormendy-ho-2013]].
- Mass-measurement techniques: [[sources-smbh-mass-measurement]].
- Nanohertz SGWB: [[sources-gw-background]].

## See also

- [[smbh-binaries]]
- [[smbh-scouring]]
- [[smbh-host-scaling]]
- [[gw-background]]
- `../lensing/concepts/smbh-from-lensing.md`
