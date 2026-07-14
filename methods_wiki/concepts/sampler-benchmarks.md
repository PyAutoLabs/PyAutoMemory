---
title: Sampler benchmarks
type: concept
topics: [samplers, benchmarks, profiling, jax]
sources:
  - autofit_workspace_developer/searches_minimal/output/ (local, regenerable)
  - autolens_profiling (local repo, HPC campaign results)
status: draft
---

# Sampler benchmarks

## TL;DR

The record of the sampler benchmarking campaigns (April–June 2026):
what was measured, the headline numbers, and where the raw outputs
live. Two tiers of problem: the **minimal 1D Gaussian** (every sampler,
identical data, `searches_minimal`) and **real lensing likelihoods**
(NSS vs Nautilus on MGE / pixelization models, A100 HPC runs in
`autolens_profiling`).

## The diagnostic contract (MLTracker)

`autofit_workspace_developer/searches_minimal/_metrics.py` defines the
shared per-evaluation tracker every minimal script uses. Wrap the
likelihood with `MLTracker.wrap` (or reconstruct per-eval history from
dead/live points for fully-jitted samplers via
`MLTracker.from_log_l_history`) and report:

- **evals-to-ML / time-to-ML** — evaluation index and wall time at which
  the running max log L first comes within 1 nat of the final maximum
  (the headline "how fast does it find the answer" numbers).
- Wall time, sampling time, total evals, time/eval, ESS, log Z,
  max log L, posterior size, n_live.

Any new sampler prototype must honour this contract so its row is
comparable — that is the point of the minimal tier.

## Headline results — minimal 1D Gaussian (2026-06)

From `searches_minimal/output/comparison.txt` (100 data points,
noise 0.01, seed 1):

| Sampler | Wall (s) | Time/eval (ms) | log Z | Note |
|---|---:|---:|---:|---|
| nss_simple (callback) | 53.5 | 1.07 | −73.0 | n_live=50 bails early; evidence unreliable |
| nss_jit (pure JAX) | 12.7 | 0.022 | −57.6 | batched, no host↔device boundary |
| nss_grad (HMC+grad) | 5.2 | 0.002 | −58.1 | fastest wall time; gradient kernel |
| nautilus (NumPy) | 21.0 | 1.30 | −57.5 | CPU baseline; best ESS/eval |
| nautilus (JIT lik.) | 20.8 | 1.28 | −57.5 | JIT alone doesn't help a callback sampler |

Reference log Z ≈ −57.5; all converged samplers agree within ~0.5 nat.
Per-sampler summaries: `searches_minimal/output/*_summary.txt`.

The nautilus pair is the key negative result: **jitting the likelihood
does not speed up a Python-callback sampler** — the win only comes when
the sampler itself batches on-device ([[gpu-nested-sampling]]).

## Headline results — real likelihoods (A100 campaign)

From the `autolens_profiling` HPC runs ("searches first-class" series):

- NSS ≈ **7.5× faster per evaluation** than Nautilus on MGE lens
  models (vmap-batched likelihood).
- NSS **OOMs on pixelization/Delaunay** likelihoods via vmap fan-out;
  fixed by chunked vmap (see [[gpu-nested-sampling]] for the mechanism
  and the Mind prompts that shipped it).
- vmap batch sizing on A100: per-(cell, instrument) batches; MGE
  batches of 64 at AO=3; interferometer/MGE blocked at ALMA-scale and
  above.

Raw outputs, job scripts and result JSON/PNGs live in
`autolens_profiling` (per-run directories; see that repo's AGENTS.md).

## Benchmark hygiene

- Same seed, same data, same priors across samplers (the minimal tier
  fixes `np.random.seed(1)`).
- Beware `pure_callback` constant-folding under single-JIT — verify
  with `vmap` (honest tracing) before trusting a speedup.
- ESS and log Z agreement, not wall time alone, decide whether a fast
  sampler actually converged (nss_simple's 15-nat log Z error above).

## See also

- [[gradient-optimizer-benchmarks]] — the sibling study on gradient-based
  MAP/optimization (multi-start Adam, SVGD, CMA-ES) on the MGE lens likelihood,
  CPU + A100.
- [[gpu-nested-sampling]] — why the JAX tiers win and where they OOM.
- [[hamiltonian-monte-carlo]] — the gradient kernel behind nss_grad.
- [[initialization-chaining]] — how fast consumers get their start.
- [[nested-sampling]]
