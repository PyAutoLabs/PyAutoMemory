---
title: Sources — samplers
type: sources
topics: [samplers, mcmc, nested-sampling]
status: drafted
---

# Sources: samplers

Papers describing specific samplers: MCMC, nested sampling, basin
hopping, and the libraries that implement them.

## PolyChord 2015

**Canonical BibTeX key:** `Handley2015a`
**Reference:** POLYCHORD: Next-generation nested sampling; arXiv:1506.00171; doi:10.1093/mnras/stv1911; Monthly Notices of the Royal Astronomical Society
**Concepts:** [[nested-sampling]]

**Supports:**
- Introduces PolyChord as a next-generation nested-sampling algorithm.
- Uses slice-sampling ideas to handle high-dimensional nested-sampling problems.
- Provides the canonical PolyChord method citation.

**Use when:**
- Citing PolyChord or high-dimensional nested sampling.

**Do not use for:**
- Dynamic nested sampling in dynesty or MCMC ensemble sampling.


## PolyChord — root copy

**Canonical BibTeX key:** TODO — no unique match found in `bibliography/pyautomemory.bib`.
**Reference:** TODO — identify the public paper record and add or resolve the canonical BibTeX key.
**Concepts:** [[nested-sampling]]

**Supports TODO:**
- TODO — not migrated: paper identity or canonical bibliography entry is unresolved.

**Use when TODO:**
- TODO — use only after the paper is identified and claim support is verified.

**Do not use for TODO:**
- Evidence until the paper identity and canonical key are verified.


## Buchner — PyMultiNest

**Canonical BibTeX key:** TODO — ambiguous candidates: `Buchner2014`, `Johannesen2007`, `pymultinest`.
**Reference:** TODO — resolve the paper identity against `bibliography/pyautomemory.bib` and an authoritative public record.
**Concepts:** [[nested-sampling]]

**Supports TODO:**
- TODO — not migrated: canonical key is ambiguous, so claim support must be verified after key resolution.

**Use when TODO:**
- TODO — use only after the canonical key and paper identity are resolved.

**Do not use for TODO:**
- Evidence until the ambiguous canonical key is resolved.


## Nested basin sampling

**Canonical BibTeX key:** TODO — no unique match found in `bibliography/pyautomemory.bib`.
**Reference:** TODO — identify the public paper record and add or resolve the canonical BibTeX key.
**Concepts:** [[nested-sampling]]

**Supports TODO:**
- TODO — not migrated: paper identity or canonical bibliography entry is unresolved.

**Use when TODO:**
- TODO — use only after the paper is identified and claim support is verified.

**Do not use for TODO:**
- Evidence until the paper identity and canonical key are verified.


## Dynesty

**Canonical BibTeX key:** `Speagle2020`
**Reference:** [arXiv:1904.02180](https://arxiv.org/abs/1904.02180); doi:10.1093/mnras/staa278.
**Concepts:** [[nested-sampling]], [[sampler-candidate-curation]]

**Supports:**
- Static and dynamic nested sampling estimate posteriors and evidence.
- Dynamic allocation adjusts effort between posterior and evidence estimation.

**Use when:**
- Explaining dynesty's allocation strategy or choosing an evidence baseline.

**Do not use for:**
- Assuming a winner on an untested likelihood or current integration status.


## emcee

**Canonical BibTeX key:** TODO — ambiguous candidates: `Emcee`, `Foreman-Mackey2013`, `emcee`.
**Reference:** TODO — resolve the paper identity against `bibliography/pyautomemory.bib` and an authoritative public record.
**Concepts:** [[mcmc-samplers]]

**Supports TODO:**
- TODO — not migrated: canonical key is ambiguous, so claim support must be verified after key resolution.

**Use when TODO:**
- TODO — use only after the canonical key and paper identity are resolved.

**Do not use for TODO:**
- Evidence until the ambiguous canonical key is resolved.


## See also

- [[mcmc-samplers]]
- [[nested-sampling]]
- [[hamiltonian-monte-carlo]]
- [[sources-probabilistic-programming]]

## Nautilus — 2023

**Canonical BibTeX key:** `Lange2023Nautilus`
**Reference:** [arXiv:2306.16923](https://arxiv.org/abs/2306.16923); [official code](https://github.com/johannesulf/nautilus).
**Concepts:** [[sampler-candidate-curation]]

**Supports:**
- Combines importance nested sampling with neural-network regression for posterior and evidence estimation.

**Use when:**
- Evidence and posterior estimation for expensive gradient-free likelihoods.

**Do not use for:**
- A PyAutoFit performance ranking, evidence calibration claim or production acceptance.

## BlackJAX NUTS — 2024

**Canonical BibTeX key:** `Cabezas2024BlackJAX`
**Reference:** [arXiv:2402.10797](https://arxiv.org/abs/2402.10797); [official code](https://github.com/blackjax-devs/blackjax).
**Concepts:** [[sampler-candidate-curation]]

**Supports:**
- Provides composable JAX inference kernels operating on target log densities; the library includes NUTS.

**Use when:**
- Posterior refinement for differentiable JAX targets.

**Do not use for:**
- A PyAutoFit performance ranking, evidence calibration claim or production acceptance.

## UltraNest — 2021

**Canonical BibTeX key:** `Buchner2021UltraNest`
**Reference:** [arXiv:2101.09604](https://arxiv.org/abs/2101.09604); [official code](https://github.com/JohannesBuchner/UltraNest).
**Concepts:** [[sampler-candidate-curation]]

**Supports:**
- Provides parameter estimation and model comparison for non-Gaussian and multimodal spaces, with resumable parallel runs.

**Use when:**
- Independent evidence cross-check for non-Gaussian and multimodal targets.

**Do not use for:**
- A PyAutoFit performance ranking, evidence calibration claim or production acceptance.

## pocoMC — 2022

**Canonical BibTeX key:** `Karamanis2022PocoMC`
**Reference:** [arXiv:2207.05660](https://arxiv.org/abs/2207.05660); [official code](https://github.com/minaskar/pocomc).
**Concepts:** [[sampler-candidate-curation]]

**Supports:**
- Uses normalizing-flow preconditioning for nonlinear and multimodal posterior inference and model comparison.

**Use when:**
- Posterior and evidence investigation for strongly correlated nonlinear targets.

**Do not use for:**
- A PyAutoFit performance ranking, evidence calibration claim or production acceptance.

## Hoffman and Gelman 2011 — NUTS

**Canonical BibTeX key:** `Hoffman2011NUTS`
**Reference:** [arXiv:1111.4246](https://arxiv.org/abs/1111.4246).
**Concepts:** [[hamiltonian-monte-carlo]], [[sampler-candidate-curation]]

**Supports:**
- NUTS chooses HMC trajectory lengths using a U-turn stopping criterion.
- Dual averaging adapts the step size.

**Use when:**
- Explaining the gradient sampler's algorithm, distinct from its BlackJAX implementation.

**Do not use for:**
- An evidence estimator or proof of multimodal coverage.
