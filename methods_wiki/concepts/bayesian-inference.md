---
title: Bayesian inference
type: concept
topics: [bayesian-inference, methods]
sources:
  - Stats/Variation Inference - A Review for Statisticians.pdf
  - Stats/Expectation propagation as a way of life.pdf
status: stub
---

# Bayesian inference

## TL;DR

PyAutoFit (and therefore PyAutoLens / PyAutoGalaxy / PyAutoCTI) is a
Bayesian framework: every fit returns a posterior over a parametric
model, and model comparison uses the marginal likelihood (Bayesian
evidence) computed by nested sampling. Approximate-inference
alternatives — variational inference, expectation propagation, neural
posterior estimation — appear in adjacent tooling.

## What it is

Three sampler / inference families are in play across the PyAuto
ecosystem and the wider literature:

- **MCMC** (emcee, dynesty's MCMC mode): correct in the limit, but
  poorly tested for high-dim multi-modal lens models.
- **Nested sampling** (PolyChord, MultiNest, dynesty): default
  high-dim sampler for PyAutoFit; gives evidence for free.
- **Likelihood-free** (NPE, ABC): pivots to a learned posterior when
  the likelihood is intractable.

Variational inference and EP are deterministic alternatives that scale
to very large catalogs (Celeste, Cannon) but trade away exactness.
PyAutoFit implements EP over factor graphs for multi-dataset /
hierarchical fits — see [[expectation-propagation]] for the algorithm
as implemented and the 2026 audit findings.

## Why it matters for PyAutoLens

Lens-modelling is a Bayesian high-dim non-linear fit. Choices of
sampler, prior, and convergence criterion materially change the
science output. Reading the methodology papers (variational inference,
EP, message passing) keeps the cost-benefit framing of "why nested
sampling" defensible.

## Key references

- VI review: [[sources-bayesian-inference#variational-inference-review-for-statisticians]].
- EP modern review: [[sources-bayesian-inference#expectation-propagation-as-a-way-of-life]],
  [[sources-bayesian-inference#vehtari-2020-ep]].
- Factor graphs / message passing:
  [[sources-bayesian-inference#factor-graphs]].
- Sampler papers: [[sources-samplers]].

## See also

- [[mcmc-samplers]]
- [[nested-sampling]]
- [[simulation-based-inference]]
- [[probabilistic-programming]]
- `../lensing_wiki/concepts/bayesian-inference-lensing.md`
