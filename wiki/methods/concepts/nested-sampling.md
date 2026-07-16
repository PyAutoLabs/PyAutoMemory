---
title: Nested sampling
type: concept
topics: [nested-sampling, samplers]
sources:
  - Stats/PolyChod2015.pdf
  - PolyChord.pdf
  - Stats/ButchnerPyMultiNest.pdf
  - PPLs/Dynesty.pdf
status: stub
---

# Nested sampling

## TL;DR

Nested sampling is a Bayesian-evidence-first sampler: it samples in
nested likelihood contours from prior, accumulating live points and
computing the marginal likelihood Z directly. PolyChord (slice
sampling), MultiNest (rejection sampling in ellipsoidal regions), and
dynesty (Python re-implementation with dynamic & static modes) are the
implementations PyAutoFit interfaces with most often. PolyChord scales
to ~30+ dimensions, which is what lens models typically demand.

## What it is

Algorithmic flavours:

- **MultiNest** — fast for low/moderate dims, can fail in high-dim
  banana-shaped posteriors.
- **PolyChord** — slice sampling inside the likelihood contour; robust
  in high dim, the default for lens modelling.
- **dynesty** — pure-Python, dynamic mode trades posterior vs evidence
  precision adaptively.
- **JAX-based nested sampling** (jaxns, etc.) — GPU acceleration via
  vectorised likelihoods.

## Why it matters for PyAutoLens

PyAutoFit returns a Bayesian evidence by default; this is what enables
model comparison (e.g. with or without a multipole, broken vs unbroken
power-law). Without nested sampling, evaluating evidence would require
post-hoc thermodynamic-integration of MCMC samples, which is brittle.

## Key references

- PolyChord paper: [[sources-samplers#polychord-2015]].
- MultiNest / PyMultiNest: [[sources-samplers#buchner-pymultinest]].
- dynesty: [[sources-samplers#dynesty]].

## See also

- [[bayesian-inference]]
- [[mcmc-samplers]]
- [[gpu-nested-sampling]]
- `../lensing/entities/pyautofit.md`
