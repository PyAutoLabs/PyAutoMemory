---
title: Expectation propagation
type: concept
topics: [expectation-propagation, graphical-models, bayesian-inference, message-passing]
sources:
  - MessagePassingIsAWayOfLife.pdf
  - sources/bayesian-inference.md
status: draft
---

# Expectation propagation (as PyAutoFit implements it)

## TL;DR

EP approximates a factor-graph posterior by giving every factor its own
exponential-family "message" per variable and iterating: pull one factor
out (cavity), fit that factor against the cavity (the tilted
distribution), project the result back onto the family by moment
matching, and divide out the cavity to get the factor's new message.
PyAutoFit's twist is that the per-factor fit is a full non-linear search
(Dynesty/Nautilus/Laplace), so each dataset's factor is fit at low
dimension instead of sampling the joint. Source: `autofit/graphical/`;
messages in `autofit/messages/`. Audited 2026-07-08 (PyAutoFit #1330,
#1331, #1332) — the core update algebra is correct; evidence bookkeeping
and KL-direction consistency are not (see Pitfalls).

## The model and the approximation

The joint model is a factor graph over variables x = (x₁, …, x_n):

    p(x) ∝ ∏ₐ fₐ(xₐ)        (factors a; xₐ the variables factor a touches)

The approximation is fully factorised ("mean field") both over factors
and over variables:

    q(x) = ∏ₐ qₐ(x),    qₐ(x) = ∏ᵢ qₐᵢ(xᵢ)

Each qₐᵢ is an exponential-family message

    q(x) = h(x) exp(η·T(x) − A(η))

so products/quotients of messages are natural-parameter sums/differences
(`sum_natural_parameters`, message `__mul__`/`__truediv__`), and the
global posterior approximation is q(xᵢ) ∝ ∏ₐ qₐᵢ(xᵢ).

Code map: `EPMeanField` holds {factor → MeanField}; `MeanField` is
{Variable → AbstractMessage}; priors are themselves messages
(`MeanField.from_priors`), so a prior is just one more factor.

## One EP step (as coded)

For each factor a (`EPOptimiser.run` loops; `factor_approximation`
builds the pieces):

1. **Cavity** — everything except factor a:

       q^{\a}(x) = ∏_{b≠a} q_b(x)        (natural params: η_cav = Σ_{b≠a} η_b)

2. **Tilted distribution** — the exact factor times the cavity:

       p̂ₐ(x) = fₐ(x) q^{\a}(x) / Ẑₐ

   In `AbstractSearch.optimise` the cavity messages are installed as the
   model's priors (`prior.with_message`), and the search samples p̂ₐ.

3. **Projection (moment matching)** — find the exponential-family q*
   closest in KL(p̂ₐ ‖ q*), which for exponential families means matching
   expected sufficient statistics:

       E_{q*}[T(x)] = E_{p̂ₐ}[T(x)]

   Implemented as importance-weighted sample moments
   (`AbstractMessage.project`, with max-log-weight stabilisation), or as
   a Gaussian at the mode with covariance from the Hessian when the
   factor optimiser is the Laplace path (`MeanField.from_mode_covariance`
   after `laplace/newton.py` quasi-Newton iterations with Wolfe line
   search).

4. **Factor update (divide out the cavity)** with damping δ ∈ (0, 1]
   (`MeanField.update_factor_mean_field`):

       qₐ^new = (q*)^δ (qₐ^old)^{1−δ} / (q^{\a})^δ

   i.e. an exponential moving average on natural parameters:

       ηₐ ← (1−δ) ηₐ + δ (η_{q*} − η_cav)

   δ comes from `SimplerUpdater` (fixed), `FactorUpdater` (per-factor)
   or `DynamicUpdater` (per-variable, slower for variables shared by
   more factors). Invalid projections (negative variance etc.) fall back
   per-parameter to the previous message (`update_invalid`, flag
   `BAD_PROJECTION`).

## Convergence

`EPHistory` terminates when the summed per-variable KL between
successive global mean fields drops below `kl_tol` (default 1e-1), or on
an `evidence_tol`, or a callback. Contract to enforce: `m.kl(other)`
should mean KL(m ‖ other) for every family — see Pitfalls.

## Evidence

The intended decomposition (docstring of `EPMeanField.log_evidence`):

    Zᵢ = ∫ ∏ₐ qₐᵢ(xᵢ) dxᵢ                       (per-variable)
    Zₐ = ∫ p̂ₐ / ∏ᵢ Zᵢ                            (per-factor)
    Z  = ∏ᵢ Zᵢ ∏ₐ Zₐ

with ∫∏ messages computed in closed form from log-partitions
(`log_normalisation`: Σ(log h − A) − (log h − A)_prod). The structure is
right; the bookkeeping feeding it is currently broken (Pitfalls, F7).

## Exact (analytic) updates

If the factor callable itself is a message (`AbstractMessage.as_factor`)
and the cavity is same-family (`has_exact_projection`), the tilted
distribution is conjugate and `ExactFactorFit` multiplies the factor in
analytically — no sampler. `EPOptimiser.from_meanfield` auto-selects
this. This is the extension point for analytic likelihood updates
(linear-Gaussian factors, conjugate hierarchical updates) rather than a
green-field build.

## Deterministic variables & composition (three mechanisms)

1. **Low-level graph API**: `Factor(..., factor_out=v)` declares
   deterministic outputs propagated via `FactorValue.deterministic_values`
   (with quasi-Newton curvature transfer `quasi_deterministic_update`).
2. **Compound prior arithmetic** (`mapper/prior/arithmetic/`): model-space
   composition (rhayes777's compound-prior work) — deterministic
   relations expressed on priors before the graph exists.
3. **Free shared variables**: just share the prior across factors and
   express the relation inside the likelihood.

The IC50 cancer use case uses (2)/(3), not (1) — the low-level
deterministic API is exercised mainly by unit tests. Reconciling these
is an open design question (EP review Phase 5).

## Pitfalls (audit findings, 2026-07-08, PyAutoFit main @ 0f26ff2d8)

- **KL direction is inconsistent across families**: Normal and
  TruncatedNormal implement `self.kl(dist)` = KL(self‖dist); Gamma and
  Beta implement the reverse (verified numerically). Mixed-family
  convergence sums are therefore incoherent. (#1332 F2)
- **TruncatedNormal KL uses the untruncated formula** — error 1.5%
  (mass central) → 72% (near bound) → 140% (at bound); biases `kl_tol`
  termination for truncated priors. (#1332 F6)
- **Evidence bookkeeping broken in three legs**: `MeanField.__truediv__`
  and `__pow__` pass `log_norm` into the `plates` ctor slot (dropped +
  plates corrupted); `MeanField.from_priors` never sets `log_norm` so
  sampler evidence never enters; `TruncatedNormalMessage.log_partition`
  omits the Gaussian term (pdf integrates to σ·e^{μ²/2σ²}, not 1). Do
  not use `EPMeanField.log_evidence` for model comparison until fixed.
  (#1331, #1332 F1/F7)
- **Priors/messages layer**: 9 confirmed bugs from the 2026 audit —
  LogGaussian `with_limits` crash, Gamma `from_mode` variance inversely
  wrong, negative-sigma unchecked, Beta clamp no-op, etc. Decisions hub:
  PyAutoFit #1331.
- `ParallelEPOptimiser` recomputes all cavities from the same stale mean
  field per sweep (standard parallel-EP semantics, but different results
  from serial) and crashes at completion when `paths=None`. (#1332 F3)

## Reading

- Minka (2001), *Expectation Propagation for Approximate Bayesian
  Inference* — the original algorithm.
- Vehtari et al. (2020), *Expectation propagation as a way of life* —
  the data-partitioned EP framing PyAutoFit's per-dataset factors follow
  (notes in [sources/bayesian-inference.md](../sources/bayesian-inference.md)).

## Links

- [[bayesian-inference]] — where EP sits among inference methods.
- [[nested-sampling]] — the per-factor tilted-distribution sampler.
- [[hamiltonian-monte-carlo]], [[gpu-nested-sampling]] — alternative
  factor optimisers under consideration.
