---
title: Initialization chaining
type: concept
topics: [samplers, initialization, search-chaining, hmc]
sources:
  - Stats/PolyChod2015.pdf
status: draft
---

# Initialization chaining

## TL;DR

Samplers divide into **providers** and **consumers** of starting
points. Global, gradient-free searches (nested sampling, particle
swarm) find modes from a cold prior; local, efficient samplers
(HMC/NUTS, ensemble MCMC, L-BFGS refinement) need to start *at* a mode
to be worth running. Chaining — one search's posterior seeding the
next search's start (or priors) — is how the two are combined, and it
is a first-class pattern in PyAutoFit (chained searches / SLaM
pipelines).

## The provider/consumer map

| Role | Samplers | Notes |
|---|---|---|
| Cold-start providers | Nautilus, dynesty, NSS, UltraNest | Explore the full prior; multi-modal-safe; return posterior + evidence |
| Cheap mode-finders | PySwarms, BFGS/L-BFGS, Drawer (sanity) | MLE only, no posterior; fast way to a basin |
| Warm-start consumers | HMC/NUTS (BlackJAX), Emcee, Zeus | Refine a known mode; HMC also needs warmup to adapt step size/mass matrix |

Consumer requirements differ in strength:

- **Ensemble MCMC** (emcee/Zeus): initialise the walker cloud in a ball
  around a mode; a bad start means long burn-in, not failure.
- **HMC/NUTS**: needs a start in a region of reasonable density *and* a
  warmup phase ([[hamiltonian-monte-carlo]]); starting in the tails
  wastes the entire adaptation window or diverges. The natural provider
  is a nested-sampling posterior: seed chains from posterior draws, and
  optionally use the posterior covariance as the initial mass matrix.
- **Optimisers** consume anything and provide only a point estimate —
  useful as the middle link (NS → MLE polish → HMC).

## How PyAutoFit expresses it

- **Chained searches**: `result.model` / prior passing carries one
  search's posterior into the next search's priors — the mechanism
  under SLaM pipelines (autolens_assistant skill `al_chain_searches`).
- **Initializer classes**: `autofit/non_linear/initializer.py`
  (`InitializerPrior`, `InitializerBall`, `InitializerParamBounds`)
  control where a search's first samples are drawn — the API surface a
  warm-start (e.g. "start NUTS from these posterior draws") plugs into.
- The minimal-tier prototype of the full pattern is `nss_grad` — an HMC
  kernel *inside* sequential nested sampling, where the NS live points
  are, in effect, a continuously-maintained initialization set.

## Why it matters for the PyAuto stack

The JAX migration makes the fast consumers (HMC/NUTS) available on real
lensing likelihoods, but they will only be competitive as the *second*
stage of a chain — lens posteriors are multi-modal and a cold NUTS run
is unsafe. The practical architecture is: nested sampling (evidence +
global map, possibly GPU-native — [[gpu-nested-sampling]]) → HMC/NUTS
(cheap extra posterior precision at ~0.002 ms/eval —
[[sampler-benchmarks]]). Any promoted PyAutoFit search that *requires*
initialization must declare its provider in the pipeline, not assume
one.

## See also

- [[hamiltonian-monte-carlo]]
- [[gpu-nested-sampling]]
- [[nested-sampling]]
- [[sampler-benchmarks]]
