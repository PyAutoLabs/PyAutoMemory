---
title: SMBH binaries
type: concept
topics: [smbh, binaries]
sources:
  - SMBHs/Liao2024RABBITS2.pdf
  - SMBHs/Shen2013BBHsViaTimeChangeOfBLRs.pdf
status: stub
---

# SMBH binaries

## TL;DR

When two massive galaxies merge, their SMBHs sink to the centre via
dynamical friction, form a bound binary, and (if anything unsticks
them at sub-parsec separations) eventually coalesce via gravitational
radiation. The bottleneck — the "final-parsec problem" — is whether
enough stars or gas scatter into the binary's loss cone to hand
energy from the binary into the surrounding nuclear material. SMBHBs
are the dominant source of the nanohertz stochastic GW background
detected by pulsar-timing arrays.

## What they are

Three-phase evolution:

1. **Dynamical friction** drags each SMBH towards the new merged
   centre (kpc → pc separations).
2. **Hardening** by three-body interactions with the surrounding
   stellar / gas distribution (pc → mpc).
3. **GW inspiral and coalescence** (mpc → ISCO).

The hardening phase is where the binary can stall — see
[[final-parsec-problem]]. RABBITS-style simulations
([[sources-smbh-binaries#liao-2024-rabbits-ii]]) argue that nuclear
star formation refills the loss cone enough to drive most binaries to
coalescence within a Hubble time, but other works show many binaries
stall (Kelley 2017a, Volonteri 2020).

## Why they matter for PyAutoLens

- SMBH-binary scouring leaves cored stellar profiles in the lensing
  galaxy — fits should allow shallow inner cusps in the light model.
- The nanohertz SGWB normalisation constrains the high-mass end of
  the SMBH mass function — relevant for the lensing-galaxy
  population.
- Recoiling SMBH remnants leave kinematic offsets in the lens galaxy
  that can perturb central images.

## Key references

- Final-parsec problem and resolution: [[sources-smbh-binaries#liao-2024-rabbits-ii]].
- BLR-variability detection channel: [[sources-smbh-binaries#shen-2013-bbhs-via-blr-time-variations]].
- Population modelling for GWB: [[sources-gw-background]].

## See also

- [[final-parsec-problem]]
- [[smbh-recoil]]
- [[smbh-scouring]]
- [[gw-background]]
- [[dual-agn]]
