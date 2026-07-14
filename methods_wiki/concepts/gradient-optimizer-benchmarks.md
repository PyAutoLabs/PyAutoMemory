---
title: Gradient-optimizer benchmarks (MAP on the MGE lens likelihood)
type: concept
topics: [samplers, optimizers, benchmarks, jax, gpu, map, giga-lens, svgd]
sources:
  - autolens_workspace_developer/searches_minimal/ (merged PRs #96 + #98, 2026-07-14)
  - autolens_workspace_developer/searches_minimal/next_wave_findings.md
  - autolens_workspace_developer/searches_minimal/gradient_optimizer_findings.md
  - GitHub issues autolens_workspace_developer #95, #97
  - A100 runs: RAL /mnt/ral/jnightin/nextwave_logs/ (SLURM 330165/170/171/172)
status: draft
last_updated: 2026-07-14
---

# Gradient-optimizer benchmarks (MAP on the MGE lens likelihood)

## TL;DR

A two-part study (2026-07-13/14) of JAX gradient-based **MAP/optimization**
methods on the real HST **MGE lens likelihood** (`AnalysisImaging(use_jax=True)`,
15 free nonlinear params — MGE light amplitudes solved by the linear inversion;
einstein_radius truth ≈ 1.6). The central result:

> **Robust MAP-finding needs BOTH maintained diversity AND gradients.**
> Single cold-start from a broad prior fails (any optimizer → wrong basin).
> *Independent multi-start* gradient descent is the practical winner and
> **scales to ~100 % basin-hit on a GPU** (GIGA-Lens recipe). *Interacting*
> populations only help if they preserve diversity: CMA-ES collapses, SVGD
> (repulsion + gradient) reaches the truth but needs a GPU even to compile.

Objective throughout: minimise `-(log_likelihood + Σ log_prior)` in the physical
parameter vector (a true MAP; `model.log_prior_list_from_vector(…, xp=jnp)` is
the jax-traceable prior — same term `af.Fitness(fom_is_log_likelihood=False)`
adds). "Works" = recovers the truth basin (positive log L; the noise
normalisation dominates when χ² ≪ N_pixels).

## A100 results (RAL, NVIDIA A100 80GB, float32) — the headline

| Method | Iters | Evals | Compile | Sampling | Wall | ms/eval | Max log L | r_E | Works? |
|---|--:|--:|--:|--:|--:|--:|--:|--:|:--:|
| **multi-start Adam 128×** | 300 | 38 400 | 152.8 s | 17.5 s | 170.2 s | 0.5 | +31 787.9 | 1.600 | ✅ 23/128 (p_hit 0.18) |
| multi-start ADABelief 128× | 300 | 38 400 | 148.8 s | 18.1 s | 166.8 s | 0.5 | +31 787.8 | 1.600 | ✅ 19/128 (0.15) |
| multi-start Lion 128× | 300 | 38 400 | 137.7 s | 16.3 s | 154.0 s | 0.4 | +29 559.3 | 1.604 | ✅ 20/128 (0.16) |
| **SVGD (16 particles)** | 300 | 4 800 | 90.1 s | 105.0 s | 195.2 s | 22.0 | +17 999.4 | 1.595 | ✅ best particle = truth |

**The 128-start optimization is compile-dominated and essentially free.** On the
A100 each fwd+grad eval is **~0.5 ms** (batched over 128 starts), so 300 steps ×
128 starts = 38 400 evals run in **~17 s**; the ~150 s wall is almost entirely
one-shot JIT compilation. Same eval on CPU ≈ 192 ms (~400× slower). ⇒ on a GPU
the *wide parallel start-batch that buys robustness is nearly free*.

- **Local rule barely matters within multi-start.** Adam/ADABelief/Lion all give
  ~15–18 %/start hit rate and recover r_E ≈ 1.60. Adam/ADABelief reach the
  deepest optimum (+31.8k); Lion (sign-based) lands slightly shallower (+29.6k).
- **SVGD** reaches the truth as a *mode-finder* (best particle r_E 1.595); its
  "0/16 final in basin" is because it is a **posterior** method — repulsion
  spreads the cloud rather than collapsing to the MAP (hence +18k < point
  optimum +31.8k). 22 ms/eval (pairwise kernel + per-particle grads, not a flat
  batch). **Compile-prohibitive on CPU (>26 min, 10 GB); A100 compiles in 90 s.**

## CPU results (baseline)

**Single-optimizer benchmark (#95, ~192 ms/eval):**

| Method | Iters | Evals | Compile | Wall | Max log L | r_E | Works? |
|---|--:|--:|--:|--:|--:|--:|:--:|
| optax Adam (single) | 187 | 247 | 311 s | 374 s | −158 002 | 4.89 | ❌ |
| optax ADABelief (single) | 196 | 256 | 277 s | 329 s | −157 999 | 5.01 | ❌ (+NaN) |
| jaxopt L-BFGS (single) | 200 | ×line-search | 298 s | 1037 s | −158 005 | 4.42 | ❌ |
| numpyro SVI + ADABelief | 800 | 800 | folded | 107 s | −158 022 | 3.54 ± 0.07 | ❌ overconfident |
| **multi-start Adam 12×** | 300 | 3 600 | ~561 s | ~1254 s | +31 788 | 1.600 | ✅ 2/12 |

**Interacting population (#97, CPU):**

| Method | Gens | Evals | Compile | Wall | Max log L | r_E | Works? |
|---|--:|--:|--:|--:|--:|--:|:--:|
| CMA-ES (evosax) | 200 | 3 200 | 20 s | 232 s | −158 018 | 7.999 | ❌ collapsed 0/16 |
| SV-CMA-ES (evosax) | 120 | 7 680 | 28 s | 232 s | −149 670 | 2.605 | ⚠️ near, 0/8, still improving |
| SVGD (blackjax) | — | — | prohibitive (>26 min/10 GB) | — | — | — | ❌ → A100 |

## The verdict — diversity × gradients

| method | diversity | gradient | reaches truth? |
|---|:--:|:--:|:--:|
| single cold-start (Adam/L-BFGS/SVI) | ✗ | ✓ | ✗ |
| CMA-ES | ✗ (collapses) | ✗ | ✗ (worst, r_E 8.0) |
| SV-CMA-ES | ✓ (repulsion) | ✗ | ✗ (near, too slow) |
| **multi-start Adam/ADABelief/Lion** | ✓ (independence) | ✓ | ✓ **GPU-scalable point est.** |
| **SVGD** | ✓ (repulsion) | ✓ | ✓ (mode-finder; posterior spread) |

- **Diversity alone** (SV-CMA-ES) stays near the truth but descends the narrow
  basin too slowly. **Gradient alone** (single start) descends fast into whatever
  basin the cold start fell in — usually the wrong one. **Both** wins.
- A "population" is not enough — it must *stay diverse*. CMA-ES's single adapting
  covariance collapses onto one (wrong) mode; the many-live-point population is
  exactly why nested sampling (Nautilus) is robust for lensing.
- **Recommendation:** multi-start Adam for a robust fast *point* estimate (scales
  to ~100 % basin-hit on GPU, GIGA-Lens); SVGD when a *posterior* is also wanted.

## Traps / lessons (durable)

- **Prior median is a NaN-gradient degenerate point** on this MGE model
  (ell_comps/shear median = 0 → singular arctan2/sqrt). Cold-start must perturb
  (unit-space, stays in-bounds). NOT NNLS poisoning.
- **einstein_radius `UniformPrior(0,8)` median = 4.0 ≠ truth 1.6** → single-start
  gradient descends *away* from truth to the r_E~5 wall.
- **numpyro SVI compile HANGS (>25 min)** if handed the pre-jitted likelihood
  (jit-in-jit); pass a RAW closure. `init_to_uniform` drives the tight ell_comps
  to unphysical |x|>1 → NaN; use `init_to_value` + gradient clip.
- **SVGD step MUST be `jax.jit`'d** — an un-jitted Python loop retraces the
  median-heuristic kernel update every step (~compile cost per step → never
  finishes).
- **RAL GPU is float32** (x64 off), tolerated here.

## RAL A100 pipeline (reusable)

Established this study; see [[gpu-nested-sampling]] and the personal RAL notes.
SSH `euclid_jump` (key-auth, A100 80GB `gpu` partition); clone workspace to
`/mnt/ral/jnightin/`; base venv has CUDA jax 0.4.38 + optax + dill (blackjax only
0.1.0b1); add modern deps via an **overlay** — but `venv --system-site-packages`
from a *venv* python inherits the SYSTEM not the base venv, so use the **base
python + PYTHONPATH** an extra site-packages dir, and NEVER `pip jaxlib` into the
overlay (CPU wheel shadows the CUDA build → backend cpu). Login-node `import jax`
hangs (CUDA init, no GPU) → `JAX_PLATFORMS=cpu` or metadata-only. Drive with
`hpc/sync push-submit gpu` or direct `sbatch --partition=gpu --gres=gpu:1`.

## Herculens / Enzi note

Herculens's own optimizer is **Adam (optax)**; Enzi et al. 2026's recipe is
**NumPyro SVI + ADABelief + `init_to_median`** — both *tested here* (single-start
Adam; `svi_adabelief.py`) and both fail as **cold starts**, which is exactly why
Herculens/Enzi rely on **warm-start chaining** and careful init. We deliberately
tested the hard cold-start regime; multi-start is the alternative that buys
robustness without a hand-crafted warm start. NOT tested: warm-start chaining,
staged complexity, Herculens's GP/wavelet source (we used the MGE inversion), or
the Herculens code itself.

## See also

- [[sampler-benchmarks]] — the nested-sampling / NSS campaign record.
- [[gpu-nested-sampling]] — JAX GPU sampling, vmap batching, A100.
- [[hamiltonian-monte-carlo]] — the gradient kernel family.
- [[initialization-chaining]] — warm-start providers vs consumers (the
  Herculens/Enzi strategy).
