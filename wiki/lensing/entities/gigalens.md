---
title: GIGA-Lens
type: entity
topics: [software, gpu, differentiable-modelling]
sources:
  - Gu et al. 2022 — GIGA-Lens code paper (arXiv:2202.07663)
  - Huang et al. 2026 — GIGA-Lens 2.0 (arXiv:2606.30633)
status: drafted
---

# GIGA-Lens

## What it is

GPU-accelerated, **fully forward-modelling Bayesian** strong-lens code
(Gu et al. 2022) built on TensorFlow/JAX-style autodiff. Optimisation,
posterior-covariance estimation and sampling all exploit gradients plus
massive GPU parallelisation, modelling a single galaxy-scale lens in
~minutes — designed for the ~10^5 lenses expected from surveys such as
DESI, Rubin/LSST and Euclid. Same differentiable, GPU-first philosophy as
[[herculens|Herculens]] and the JAX direction of PyAutoLens
([[autodiff-implicit-diff]]), oriented toward high-throughput survey
modelling.

## Key facts

- **Speed**: ~2 min per galaxy-scale lens on a single GPU; scales across
  many GPUs (v2.0: run on 128 nodes / 512 A100 GPUs).
- **Method**: gradient-based optimisation → posterior covariance →
  sampling, all auto-differentiated on GPU ([[bayesian-inference-lensing]]).
- **Survey driver**: the DESI Strong Lens Foundry — thousands of ML/AI
  candidates from DESI Legacy Imaging, HST-confirmed and modelled at scale.

## Papers

- **`Gu2022`** — GIGA-Lens code paper: *Fast Bayesian Inference for
  Strong Gravitational Lens Modeling* (ApJ 935, 49; arXiv:2202.07663).
  See [[sources-lens-modeling-methods#gu-2022-giga-lens]].
- **`Huang2026`** — *GIGA-Lens 2.0: Strong-Lens Modeling on Multiple GPU
  Nodes* (arXiv:2606.30633): multi-node scaling (up to 512 A100 GPUs);
  demonstrated on 100 simulated systems and DESI J238.5690+04.7276. See
  [[sources-lens-modeling-methods#huang-2026-giga-lens-2-0]].
- **`Huang2025`** — *DESI Strong Lens Foundry I: HST Observations and
  Modeling with GIGA-Lens* (arXiv:2502.03455): ~3500 ML-found candidates,
  51 HST-confirmed, modelled with GIGA-Lens on multiple GPUs.
- **`Urcelay2025`** — *A compact group lens modeled with GIGA-Lens*
  (A&A 694, A35; arXiv:2412.04567): extends GIGA-Lens to multi-galaxy
  group-scale systems with many free parameters (DES J0248-3955).

## See also

- [[herculens]]
- [[pyautolens]]
- [[autodiff-implicit-diff]]
- [[bayesian-inference-lensing]]
- [[sources-lens-modeling-methods]]
