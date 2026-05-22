---
title: SMBH core scouring
type: concept
topics: [smbh, scouring, etg-structure]
sources:
  - SMBHs/Thomas2013DynamicalFootprintCoreScouring.pdf
  - SMBHs/Kormendy2013CoresEll.pdf
status: stub
---

# SMBH core scouring

## TL;DR

When an SMBH binary hardens in a galactic nucleus, three-body
encounters with central stars eject those stars on radial orbits.
This carves a "cored" stellar surface-brightness profile — the inner
light deviates below a Sérsic extrapolation, in a region of size
comparable to the binary's hardening radius. The cores observed in
the most massive ETGs (and especially BCGs) are taken as fossil
evidence of past binary inspirals.

## What it is

Observationally, "core" ETGs show:

- An inner break radius (~10–500 pc) below which the surface
  brightness is shallower than an extrapolated outer Sérsic profile.
- A central tangential velocity-anisotropy bias from radial-orbit
  ejection.
- A correlation between core mass deficit and SMBH mass.

In simulations (KETJU, RABBITS), the deficit grows as ~0.5–1 × M_BH
per major merger, accumulating across the merger history.

## Why it matters for PyAutoLens

When fitting the lensing-galaxy light, a cored ETG can violate the
implicit assumption of a single Sérsic or composite Sérsic + exp profile.
Forcing a cuspy fit to a real core mis-attributes flux to a fictitious
central bulge component, biasing bulge–halo decompositions and (because
light traces mass weakly in the centre) the inferred inner mass slope.

## Key references

- Dynamical footprint of scouring: [[sources-smbh-recoil-scouring#thomas-2013-dynamical-footprint-of-core-scouring]].
- Catalogue of cores vs extra-light ETGs: [[sources-smbh-recoil-scouring#kormendy-bender-2013-cores-in-ellipticals]].
- KETJU-style high-z scouring: see [[ketju]].

## See also

- [[smbh-binaries]]
- [[smbh-recoil]]
- `../galaxies_wiki/concepts/etg-structure.md`
- `../lensing_wiki/concepts/bulge-halo-decomposition.md`
