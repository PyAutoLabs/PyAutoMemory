---
title: Automatic differentiation of PyAuto likelihoods
type: concept
topics: [autodiff, jax, gradients, finite-differences, inversions, hmc]
sources:
  - autolens_workspace_developer/jax_profiling/gradient/ (probes + README)
  - autolens_workspace_test/scripts/jax_grad/ (FD correctness tests)
  - arXiv:2606.30620 (Enzi et al., RTU grids)
  - PyAutoArray PR #281 (closed unmerged)
status: draft
---

# Automatic differentiation of PyAuto likelihoods

## TL;DR

As of the 2026-07 gradient audit (autolens_workspace_developer#87): every
**smooth** PyAutoLens likelihood is not just traceable but **finite-difference
validated** under `jax.grad` — parametric light profiles (Sérsic, linear
Sérsic, MGE through the positive-only NNLS solve), the point-source
source-plane χ² (including magnification-via-Hessian, i.e. third derivatives
of the deflection potential), and the weak-lensing `FitWeak` likelihood.
The two structural holes are **mesh discreteness** (Delaunay: `pure_callback`
with no JVP rule → hard error; rectangular adaptive: piecewise-smooth bin
assignment) and the **image-plane point-source solver** (triangle-tiling
forward solve, not differentiable by construction).

## What "validated" means

Finiteness of `jax.grad` output catches nothing interesting — silently zeroed
cotangents, dropped `stop_gradient` terms and wrong custom VJPs all produce
finite numbers. The audit's bar is agreement with central finite differences
parameter-by-parameter (`jax_grad/util.py`): autodiff on the eager likelihood,
FD sweep on a jitted one, guarded by an eager-vs-jit base-point check so
`pure_callback` constant-folding cannot fake the comparison (float64
throughout; per-parameter step `1e-5 * max(|x|, 0.1)`).

## Traps discovered (worth remembering)

- **NNLS dead zones**: the positive-only linear solve zeroes components whose
  amplitude would be negative — at a bad evaluation point (e.g. prior-median
  lens bulge with r_eff ≈ 15" flooding a 3" mask) the source amplitude is 0
  and every source *and mass* gradient is legitimately, correctly zero.
  Gradient tests must anchor near a live configuration and assert liveness;
  HMC/NUTS on linear-profile models will encounter genuine plateaus.
- **Zero gradients can be correct**: distinguish "gradient is zero because the
  parameter has no positional information" (flux, H0 in a positions-only fit)
  from "gradient is zero because a frozen structure ate it". FD agrees with
  the former and exposes the latter.
- **The adaptive-mesh staircase (headline finding)**: `RectangularAdaptDensity`
  with pixelization over-sampling 1 makes the likelihood **exactly
  piecewise-constant in every mass/shear parameter** — LL is bit-identical
  under ≤1e-6 shifts, because the empirical rank-space CDF transform
  (`create_transforms`) is invariant under order-preserving deformations of
  the traced grid when queries coincide with knots. Autodiff's zero is the
  *correct* a.e. derivative; naive FD "gradients" there are discontinuity
  artifacts. Controls: `RectangularUniform` is exactly smooth (AD = FD to
  7 s.f.); over-sampling > 1 restores a smooth mass signal via sub-pixel
  strain — full 14-param FD sweeps at os_pix=4 validate both adaptive meshes,
  including `RectangularAdaptImage` in the full production shape
  (`reg.Adapt` + `AdaptImages` + border relocator, ≤ ~1% on mass;
  `AdaptDensity` ≤ ~3%; FD drifts toward AD as h→0, so the residue is FD
  staircase contamination). Imaging production-config gradient mass inference
  is therefore certified; only the os_pix=1 adaptive corner is unusable —
  **and interferometer is that corner by construction** (its pixelization has
  no over-sampling): on the production sparse-operator path
  (`TransformerDFT` + `apply_sparse_operator(use_jax=True)` +
  `RectangularAdaptDensity` + `reg.Adapt`) every mass/shear gradient is
  correctly zero and, with no lens light in interferometer models, there are
  no usable gradients at all. Interferometer gradient work needs
  `RectangularUniform` (FD-validated on the same sparse path) until a
  smooth-density transform exists. Interferometer parametric light profiles
  (standard + linear Sérsic through the DFT) are FD-certified ≤ ~1e-6. Key distinction vs the paper
  (arXiv:2606.30620): Enzi et al. build the CDF from a *smooth* density, not
  empirical point ranks — that is what makes their RTU formulation fully
  differentiable. The old `jnp.interp` vjp explosion (PyAutoArray PR #281,
  closed unmerged) is moot on the refactored code — do not re-land it.
- **The spline meshes are the prior attempt at exactly this**:
  `RectangularSplineAdapt{Density,Image}` (PyAutoArray PR #289, 2026-04-22,
  opt-in, built "for gradient-based samplers": deg-11 polynomial fit to the
  inverse empirical CDF at Chebyshev nodes + Hermite inversion). Measured
  2026-07-09: they DO break the rank invariance (AD live on all params even
  at os_pix=1) but the likelihood surface is noisy — eager-vs-JIT LL gap
  ~15, FD erratic across h=1e-7..1e-5 — matching #289's shipped
  "oscillations" limitation; noise suspects are the
  `_enforce_strict_monotone` eps-jitter, polyfit conditioning, and the
  inversion table. A 727-line jax-friendly spline-interpolator refactor is
  parked in PyAutoArray stash@{0} (Mind parked.md `rectangular-spline-cdf`,
  2026-05-08). Fix path: de-noise the spline chain or leapfrog to a
  kernel-density CDF; then FD-certify incl. the interferometer sparse path.
- **Frozen Delaunay connectivity** would give exact gradients almost
  everywhere (connectivity is piecewise-constant), but today the path
  hard-errors: `pure_callback` has no JVP rule — a `custom_jvp` zero-rule
  wrapper is the unblocking step.

## Where things live

- Status table + per-likelihood write-ups:
  `autolens_workspace_developer/jax_profiling/gradient/README.md`.
- FD correctness tests (repeatable): `autolens_workspace_test/scripts/jax_grad/`.
- Related: [[hamiltonian-monte-carlo]] (why gradients matter),
  [[gpu-nested-sampling]], [[jax-ecosystem]].
