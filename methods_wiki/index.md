# Methods Wiki — Index

Top-level navigation. See `CLAUDE.md` for the schema and how the assistant
should use this wiki.

## Start here

- [[bayesian-inference]] — likelihoods, priors, posteriors, evidence.
- [[model-comparison]] — Bayes factors, AIC/BIC, posterior predictive
  checks.

## Samplers

- [[mcmc-samplers]] — Metropolis-Hastings, ensemble samplers, Eryn.
- [[hamiltonian-monte-carlo]] — NUTS, NumPyro, Stan.
- [[nested-sampling]] — MultiNest, PolyChord, dynesty, UltraNest.
- [[gpu-nested-sampling]] — JAX-accelerated nested sampling.

## Likelihood-free inference

- [[simulation-based-inference]] — SBI, ABC, neural ratio estimators.
- [[neural-posterior-estimation]] — nbi, sbi, lampe, LtU-ILI.
- [[likelihood-emulation]] — neural likelihood surrogates.

## Probabilistic programming

- [[probabilistic-programming]] — PPL philosophy, conjugate vs MCMC vs
  NPE.
- [[message-passing]] — graphical models, belief propagation.

## Deep learning

- [[deep-learning-astro]] — CNNs, BNNs, transformers in astrophysics.
- [[active-learning]] — accelerated Bayesian inference via surrogates.
- [[neural-emulators]] — emulating cosmology / N-body / lensing.

## Linear algebra & numerics

- [[linear-inversion]] — least-squares with regularisation.
- [[gaussian-linear-models]] — closed-form Bayesian linear inference.
- [[nufft]] — non-uniform fast Fourier transform.
- [[jax-finufft]] — GPU-accelerated NUFFT.
- [[autodiff-implicit-diff]] — automatic / implicit differentiation
  through solvers.

## Software ecosystem

- [[jax-ecosystem]] — Equinox, Optimistix, BlackJAX, NumPyro, …
- [[pyautofit]] (cross-link to `../lensing_wiki/`) — model-fitting
  framework underlying PyAutoLens.
- [[scientific-software]] — general-purpose tooling.

## Simulation

- [[forward-modelling]] — full forward-model pipelines.
- [[hierarchical-population-models]] — multi-level Bayesian inference.

## Named entities

- Samplers / codes: [[polychord]], [[multinest]], [[dynesty]],
  [[ultranest]], [[nautilus]], [[emcee]], [[blackjax]], [[numpyro]],
  [[stan]], [[pymc]], [[eryn]], [[nbi]], [[lampe]], [[ltu-ili]].
- JAX tooling: [[optimistix]], [[equinox]], [[jaxopt]], [[jaxns]].
- Astro-method codes: [[pyautofit]], [[pylops]], [[finufft]],
  [[pynufft]].

## Sources (bibliography by topic)

These pages describe claim support. Canonical citation metadata and key-management rules
live in [`../bibliography/`](../bibliography/README.md).

- [[sources-bayesian-inference]]
- [[sources-samplers]]
- [[sources-likelihood-free-inference]]
- [[sources-probabilistic-programming]]
- [[sources-deep-learning-methods]]
- [[sources-linear-algebra]]
- [[sources-nufft]]
- [[sources-scientific-software]]
- [[sources-simulations]]

## Meta

- [[CLAUDE]] — schema and usage rules.
- [[log]] — compilation history.
