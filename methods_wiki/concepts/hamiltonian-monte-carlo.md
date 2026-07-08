---
title: Hamiltonian Monte Carlo
type: concept
topics: [hmc, nuts, gradients, jax, samplers]
sources:
  - PPLs/Dynesty.pdf
  - Software (BlackJAX docs, https://blackjax-devs.github.io/blackjax/)
status: draft
---

# Hamiltonian Monte Carlo

## TL;DR

HMC proposes MCMC moves by simulating Hamiltonian dynamics on the
log-posterior surface, using its **gradient** to travel far in one step
while keeping acceptance high. NUTS (the No-U-Turn Sampler) removes the
hand-tuned trajectory length. The price of the speed: the likelihood
must be differentiable end-to-end (in the PyAuto stack that means
written in `jax.numpy` so `jax.grad` works), it samples the posterior
only (**no Bayesian evidence**), and it wants a **good starting point
plus warmup** — it refines a mode, it does not find one.

## What it is

- Augment parameters θ with momenta p; simulate the Hamiltonian
  H(θ, p) = −log π(θ) + ½pᵀM⁻¹p with leapfrog integration; accept via
  Metropolis. Gradient ∇ log π steers each leapfrog step.
- **NUTS** grows the trajectory until it starts doubling back ("no
  U-turn"), removing the trajectory-length knob.
- **Warmup / adaptation**: a Stan-style windowed phase tunes the step
  size (dual averaging) and the (inverse) mass matrix M. In BlackJAX
  this is `blackjax.window_adaptation(blackjax.nuts, logdensity)` —
  exactly what `autofit_workspace_developer/searches_minimal/nuts_jax.py`
  runs before production sampling.
- Constrained/uniform priors are handled by transforming to an
  unconstrained space (or, in the minimal scripts, by clipping to the
  prior box inside a `jnp.where` penalty) so gradients stay finite.

## Requirements and failure modes

- **Differentiability** — every operation from parameters to log L must
  be JAX-traceable. Python callbacks, `pure_callback` hops, or numpy
  branches break `jax.grad` (or silently give zero gradients).
- **Initialization** — HMC/NUTS started in a low-density region wastes
  warmup or diverges; multi-modal posteriors are explored only within
  the mode the chain starts in. Standard remedy in this stack: seed
  from a cheap global pass — see [[initialization-chaining]].
- **No evidence** — model comparison still needs nested sampling
  ([[nested-sampling]], [[gpu-nested-sampling]]); HMC complements, not
  replaces, it.
- Divergences flag too-large step sizes or pathological curvature
  (Neal's funnel); reparameterise or lower the target acceptance.

## Why it matters for the PyAuto stack

The JAX migration makes gradients of real lensing likelihoods available
for free — the same `jax.numpy` likelihood that `vmap` batches for GPU
nested sampling also yields `jax.grad` for HMC. The minimal benchmarks
(see [[sampler-benchmarks]]) show the payoff: NSS's HMC-kernel variant
(`nss_grad`) reached the 1D-Gaussian posterior in 5.2 s wall time vs
53.5 s for the callback-based nested sampler, at ~0.002 ms per
likelihood evaluation. BlackJAX NUTS is prototyped in
`searches_minimal/nuts_jax.py` and integrated in PyAutoFit as
`BlackJAXNUTS` (exercised by
`autofit_workspace_test/scripts/searches/BlackJAXNUTS.py`).

## Key references

- Neal (2011), "MCMC using Hamiltonian dynamics" — the canonical HMC
  chapter.
- Hoffman & Gelman (2014), arXiv:1111.4246 — NUTS.
- Betancourt (2017), arXiv:1701.02434 — conceptual introduction,
  divergences and geometry.
- Implementations: BlackJAX (JAX), NumPyro, Stan — see
  [[probabilistic-programming]] and [[sources-samplers]].

## See also

- [[initialization-chaining]] — where the starting point comes from.
- [[gpu-nested-sampling]] — the evidence-bearing JAX sibling; `nss_grad`
  puts an HMC kernel *inside* nested sampling.
- [[mcmc-samplers]] — gradient-free ensemble MCMC (emcee, Zeus).
- [[jax-ecosystem]] — BlackJAX, the handley-lab fork used by NSS.
