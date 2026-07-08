---
title: GPU / JAX nested sampling
type: concept
topics: [nested-sampling, jax, gpu, vmap, samplers]
sources:
  - Stats/PolyChod2015.pdf
  - Software (NSS, https://github.com/yallup/nss)
status: draft
---

# GPU / JAX nested sampling

## TL;DR

JAX-native nested samplers (NSS, jaxns) keep the whole sampling loop —
live points, proposals, likelihood — on the accelerator, evaluating
**batches** of likelihoods via `jax.vmap` instead of one Python call at
a time. On the minimal 1D-Gaussian benchmark this cuts per-evaluation
cost from ~1 ms (Python callback) to ~0.02 ms; on real lensing
likelihoods the A100 campaign measured NSS ~7.5× faster per evaluation
than Nautilus on MGE models. The catch: `vmap` fan-out multiplies
memory, which OOMs inversion-heavy (pixelization/Delaunay) likelihoods
— fixed by **chunked vmap** (split the batch, `lax.map` over chunks).

## What it is

- Classical nested sampling ([[nested-sampling]]) calls the likelihood
  through a Python callback — dynesty, Nautilus, MultiNest. Each call
  crosses the host↔device boundary; the sampler logic runs on CPU.
- JAX nested sampling compiles sampler + likelihood into one XLA
  program. Live-point updates become batched `vmap` evaluations; the
  GPU is kept saturated. NSS (yallup/nss, on the handley-lab BlackJAX
  fork) is the implementation prototyped in this stack; its variants in
  `autofit_workspace_developer/searches_minimal/`:
  - `nss_simple.py` — callback likelihood (baseline; slowest).
  - `nss_jit.py` — pure-JAX likelihood, fully jitted (~0.02 ms/eval).
  - `nss_grad.py` — HMC-kernel sequential Monte Carlo
    (`nss.smc.run_hmc_sequential_mc`), adding `jax.grad` to the batch
    ([[hamiltonian-monte-carlo]]).

## Memory: the vmap fan-out problem

`vmap(likelihood)(batch)` materialises every intermediate for the whole
batch. For MGE/light-profile likelihoods that is fine (A100 batches of
64 at AO=3 in the vmap-batch investigation); for inversion-heavy
likelihoods (pixelization / Delaunay source reconstructions, large
interferometer NUFFTs) the per-sample intermediates are already large,
and the fan-out OOMs even an 80 GB A100. The working fix is **chunked
vmap**: split the live-point batch into fixed-size chunks and loop
(`lax.map` / scan) over them — trading a little parallelism for bounded
memory. This shipped for NSS as the chunked-vmap work (PyAutoMind:
`issued/nss_chunked_vmap_for_inversion_heavy_likelihoods.md`, follow-up
`issued/nss_chunked_init_followup.md`).

## Benchmarking honesty (JAX gotchas)

- `pure_callback` inside a single-JIT likelihood can be **constant-
  folded** by XLA — the "likelihood" is baked in as a constant and looks
  20–30× faster than it is. Benchmark through `vmap` with real traced
  inputs, never a jitted call on concrete values.
- A likelihood closure rebuilt per call busts the JIT cache and re-pays
  compile every evaluation; cache the compiled function on the instance.

## Why it matters for the PyAuto stack

Nested sampling is the stack's default (evidence for model comparison,
robust multi-modal exploration), so making *it* GPU-native — rather than
only the likelihood — is the highest-leverage sampler work. The measured
A100 results and the OOM boundary define where NSS is deployable today:
parametric/MGE models yes; pixelized-source and ALMA-scale
interferometer likelihoods only via chunking. Raw numbers and where they
live: [[sampler-benchmarks]].

## Key references

- Skilling (2006) — nested sampling; see [[sources-samplers]].
- Handley et al. (2015), arXiv:1506.00171 — PolyChord (slice NS).
- Albert (2020), arXiv:2012.15286 — jaxns.
- Lange (2023), arXiv:2306.16923 — Nautilus (the CPU baseline the
  benchmarks compare against).

## See also

- [[nested-sampling]] — the algorithm family.
- [[hamiltonian-monte-carlo]] — the gradient kernel `nss_grad` embeds.
- [[sampler-benchmarks]] — the campaign record.
- [[jax-ecosystem]] — BlackJAX fork, Equinox, Optimistix.
