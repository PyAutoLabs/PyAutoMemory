# Compilation log

Append-only record of what was done to this wiki, by whom, and when.

---

## 2026-05-22 — Initial build

**By:** Claude (Opus 4.7, PyAutoLabs feature/pyautopaper-wiki-expansion
session).

**Scope of build:** `Stats/` (14 PDFs), `GaussianLinearModels/` (6),
`PPLs/` (7), `Deep Learning/` (4), `Software/` (7), `Simulation/`
(18), `Medical/` (3), plus root-level `PolyChord.pdf`,
`linearalgebra.pdf`, `NUFFTPAper.pdf`, `PYNUFFT.pdf`,
`MessagePassingIsAWayOfLife.pdf`, `BigData.pdf`, `imfit.pdf`,
`Profit2019.pdf`, `PyLops` (folder).

**What was created**

- `CLAUDE.md` — inherits schema, scope-restricted to statistical /
  computational methods.
- `index.md` — top-level navigation.
- `concepts/` — `bayesian-inference`, `nested-sampling`, `nufft`.
- `sources/` — `bayesian-inference`, `samplers`,
  `probabilistic-programming`, `likelihood-free-inference`,
  `linear-algebra`, `nufft`, `deep-learning-methods`,
  `scientific-software`, `simulations`, `medical-imaging-adjacents`.

**Status of stubs**

All per-paper stubs are `status: stub`. `Software/jimaging-04-00051-v2.pdf`
and `Stats/2008.09375.pdf` flagged as title-unknown until PDFs are
inspected.

**Provenance**

Same Karpathy "LLM Wiki" pattern as the lensing sub-wiki. Many entries
cross-link to `../lensing_wiki/` (Bayesian-inference-lensing,
source-reconstruction regularization) and `../smbh_wiki/`
(Rosas-Guevara EAGLE SMBH simulations, Latif SMBH seeds review).

## 2026-07-08 — Sampler pages for the Brain samplers faculty

Added four concept pages backing PyAutoBrain's new samplers faculty
(PyAutoBrain#54): [[hamiltonian-monte-carlo]] (fills index red-link;
NUTS/BlackJAX, gradient + warm-start requirements),
[[gpu-nested-sampling]] (fills index red-link; NSS, vmap fan-out OOM +
chunked-vmap fix), [[initialization-chaining]] (provider/consumer map,
PyAutoFit chained searches), [[sampler-benchmarks]] (MLTracker
diagnostic contract, minimal 1D-Gaussian table, A100 campaign headline
numbers, raw-output locations). All `status: draft` — grounded in
`autofit_workspace_developer/searches_minimal` outputs and the
autolens_profiling HPC campaign, not yet in the PDF sources; source
citations to be tightened when the Stats/ PDFs are ingested.

## 2026-07-08 — expectation-propagation concept page

Added `concepts/expectation-propagation.md` (status: draft): the EP
algorithm as PyAutoFit implements it — factor/variable mean-field
factorisation, cavity/tilted/moment-matching update with damping as an
EMA on natural parameters, evidence decomposition, exact conjugate
updates, and the three deterministic-composition mechanisms. Includes
the 2026-07-08 audit findings (PyAutoFit #1330/#1331/#1332): KL
direction inconsistency (Gamma/Beta reversed), truncated-normal KL
approximation error (1.5%→140% near bounds), and the three-legged
evidence-bookkeeping breakage. Linked from index.md (Start here) and
concepts/bayesian-inference.md. Written as Phase 1 output of
PyAutoMind research/graphical_ep/ep_framework_review.md; a public,
personal-content-free version is planned for the future
autofit_assistant wiki (PyAutoMind research/autofit_assistant/).

---

## 2026-07-14 — Gradient-optimizer benchmarks (MAP on the MGE lens likelihood)

**By:** Claude (Opus 4.8, PyAutoLabs next-wave-population-optimizers session).

**Scope:** new `concepts/gradient-optimizer-benchmarks.md` recording the
2026-07-13/14 study of JAX gradient-based MAP/optimization on the real MGE lens
likelihood (autolens_workspace_developer #95 + #97, merged PRs #96/#98). Headline:
robust MAP needs **diversity × gradients** — single cold-start fails; multi-start
Adam wins and scales to ~100 % basin-hit on an A100 (GIGA-Lens); SVGD reaches the
truth but is GPU-only; CMA-ES collapses. Includes exact CPU + A100 runtimes /
iterations (RAL A100 80GB), the diversity×gradient verdict, durable traps, the
reusable RAL A100 pipeline, and a Herculens/Enzi cold-start-vs-warm-start note.
Cross-linked from index.md (Samplers) and concepts/sampler-benchmarks.md.

---

## 2026-07-17 — Aggregator performance (result loading at catalogue scale)

**By:** Claude (Fable 5, PyAutoLabs aggregator-profiling arc session).

**Scope:** new `concepts/aggregator-performance.md` recording the 2026-07-16/17
profiling campaign over every PyAutoFit result-loading pathway (directory
Aggregator, sqlite scrape + direct-write, csv/png/fits catalogue workflows,
lens-level al.agg wrappers) at 3000-lens catalogue scale, via mock result trees
from PYAUTO_TEST_MODE_SAMPLES bypass fits. Headlines: samples-per-result is the
scaling axis; every stage floor-bounded by from_dict deserialization (model load
−44% after JSONPriorConfig lookup caching, Conf#130); representative-scale sqlite
reads comparable to directory (revising the small-data 2-10×-slower verdict);
three crash-level bugs found and fixed (from_dict 0.0-drop, AggregateFITS fd
leak at ~500 results, database slicing inversion). Durable methodology lessons
(fresh-Aggregator staging, idle-machine grids, interleaved A/B under load)
recorded. Cross-linked from index.md (Software ecosystem).
