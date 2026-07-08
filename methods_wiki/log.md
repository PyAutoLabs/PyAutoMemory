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
