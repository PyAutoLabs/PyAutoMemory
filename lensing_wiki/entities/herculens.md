---
title: Herculens
type: entity
topics: [software, differentiable-modelling, jax]
sources:
  - Galan et al. 2022 — Herculens code paper (arXiv:2207.05763)
  - Biggio et al. 2023 — continuous neural fields (arXiv:2210.09169)
status: drafted
---

# Herculens

## What it is

Open-source **differentiable** strong-lens modelling code (Galan et al.
2022), built entirely on JAX so the full forward model — analytic
profiles, pixelated source/potential, and machine-learning components —
is auto-differentiable and GPU-capable. It merges the analytical,
pixelated and deep-learning modelling paradigms into one modular
framework, with wavelet-regularised pixelated reconstructions optimised
by gradient-informed methods (SVI, HMC-within-Gibbs via NumPyro). It is
the closest external analogue to the differentiable-likelihood direction
PyAutoLens is pursuing under JAX ([[autodiff-implicit-diff]]).

## Key facts

- **Autodiff-native**: JAX end-to-end; thousands of free parameters
  optimised with gradients (source pixels, potential perturbations).
- **Wavelet regularisation**: sparse/wavelet priors capture deviations
  from smoothness — subhaloes, LOS haloes, multipoles ([[multipoles]],
  [[dark-matter-substructure]]). Predecessor: SLITronomy (`Galan2021`).
- **Lineage**: SLITronomy → Herculens code paper (`Galan2022`) →
  neural-field potentials (`Biggio2022`) → cluster/JWST applications.
- **Interoperability**: the Herculens group authored **COOLEST**
  (`Galan2023`), the code-independent lens-model exchange standard.

## Papers

- **`Galan2022`** — Herculens code paper: *Using wavelets to capture
  deviations from smoothness in galaxy-scale strong lenses*
  (arXiv:2207.05763). See [[sources-source-reconstruction#galan-2022-wavelet-lensing]].
- **`Galan2021`** — *SLITronomy*, the wavelet-inversion precursor
  (arXiv:2012.02802). See [[sources-source-reconstruction#galan-2021-slit]].
- **`Biggio2022`** — *Modeling lens potentials with continuous neural
  fields in galaxy-scale strong lenses* (arXiv:2210.09169): a
  physics-retaining neural field for the lens potential, implemented in
  Herculens, requiring no pre-training.
- **`Galan2023`** — *COOLEST: COde-independent Organized LEns STandard*
  (JOSS 8, 5567): JSON standard to store/share/compare lens models across
  codes; the Herculens group's interoperability effort.
- **`Galan2024`** — *El Gordo needs El Anzuelo* (arXiv:2402.18636):
  Herculens modelling of multi-band extended arcs in JWST data, measuring
  cluster-member density slopes steeper than isothermal.
- **`Galan2024a`** — *Exploiting the diversity of modeling methods to
  probe systematic biases in strong lensing analyses* (arXiv:2406.08484):
  cross-method comparison (via COOLEST) by the Herculens team; combining
  independent methods cuts maximal systematic biases by ~5.4×.

## See also

- [[gigalens]]
- [[pyautolens]]
- [[lenstronomy]]
- [[autodiff-implicit-diff]]
- [[source-reconstruction]]
- [[sources-lens-modeling-methods]]
