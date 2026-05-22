---
title: Nanohertz gravitational-wave background
type: concept
topics: [smbh, gw-background, pta]
sources:
  - GWB/NANOGrav152024SMBHB.pdf
  - SMBHs/MarconiLocalAndRelicBHMassFunctions.pdf
status: stub
---

# Nanohertz gravitational-wave background

## TL;DR

Pulsar-timing arrays (PTAs) detect a low-frequency stochastic
gravitational-wave background (SGWB) consistent with the incoherent
superposition of many SMBHB inspirals across the universe. NANOGrav's
15-year dataset (2023) was the first to claim Hellings–Downs evidence
for the SGWB. The amplitude pins down the high-mass end of the SMBH
mass function and the binary coalescence efficiency.

## What it is

PTAs monitor an ensemble of millisecond pulsars; the angular
correlation function of timing residuals (Hellings–Downs) is the
signature of a GW background. The expected SGWB from SMBHB is
characterised by a power-law strain spectrum h_c(f) ∝ f^{-2/3} in the
GW-only limit, with f ~ nHz–μHz.

## Why it matters for PyAutoLens

Indirect: the SGWB amplitude is set by the same SMBH mass function
that drives the lensing-galaxy population's central-image phenomenology.
A high SGWB normalisation implies more / heavier SMBHBs, which has
follow-on effects on the cored ETG population (see [[smbh-scouring]])
and on the population of compact AGN that act as lensed sources.

## Key references

- NANOGrav 15-year: [[sources-gw-background#nanograv-15-year-smbhb-constraints]].
- Local + relic mass function (Soltan + GW): [[sources-smbh-mass-functions#marconi-local-and-relic-bh-mass-functions]].
- RABBITS resolution of the final-parsec problem (high-mass end):
  [[sources-smbh-binaries#liao-2024-rabbits-ii]].

## See also

- [[smbh-binaries]]
- [[pulsar-timing-arrays]]
- [[smbh-mass-functions]]
