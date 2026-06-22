# Methods AI Assistant — Statistical & Computational Methods Wiki

This sub-wiki gives an AI assistant the scientific context of the
**methodological** tooling that underpins PyAutoLens, PyAutoFit, and
related codes: Bayesian inference, nested and Hamiltonian sampling,
deep learning for astrophysics, probabilistic programming languages,
linear-algebra primitives (NUFFT, message passing), and the wider
scientific-software ecosystem. Sibling of `lensing_wiki/` under
`PyAutoPaper/`, same Karpathy "LLM Wiki" pattern.

## Layout

```
methods_wiki/
├── CLAUDE.md           # this file — schema + scope
├── index.md            # top-level navigation
├── log.md              # append-only compilation log
├── concepts/           # Bayes basics, samplers, deep learning, etc.
├── entities/           # PyAutoFit, PolyChord, BlackJAX, jax-finufft, …
└── sources/            # per-topic claim support
```

## Schema

Inherits verbatim from [`../lensing_wiki/CLAUDE.md`](../lensing_wiki/CLAUDE.md).

## Scope

In-scope folders:

- `Stats/` — Bayesian methods, likelihood-free inference, MCMC,
  sampler comparisons.
- `GaussianLinearModels/` — Gaussian linear models, conjugate priors,
  closed-form posteriors used in linear inversion.
- `PPLs/` — probabilistic programming languages (Stan, PyMC, NumPyro,
  Pyro, etc.).
- `Deep Learning/` — CNNs, BNNs, simulation-based inference applied
  to astrophysics (cross-references `../lensing_wiki/sources-deep-learning-lensing.md`).
- `Software/` — general-purpose scientific software references (samplers,
  optimisers, JAX ecosystem).
- `Simulation/` — Monte Carlo simulation methodology, hierarchical
  forward modelling.
- Root-level `PolyChord.pdf`, `linearalgebra.pdf`, `NUFFTPAper.pdf`,
  `PYNUFFT.pdf`, `MessagePassingIsAWayOfLife.pdf`, `BigData.pdf`,
  `PyLops` (folder), `imfit.pdf`, `Profit2019.pdf`.

Adjacent topics that link out:
- Lens-modelling-specific Bayesian / regularisation methods —
  `../lensing_wiki/concepts/bayesian-inference-lensing.md` and
  `../lensing_wiki/concepts/regularization.md`.
- Mass-model / source-reconstruction software entities —
  `../lensing_wiki/entities/{pyautolens,pyautofit,lenstronomy}.md`.

## How the assistant should use this wiki

Same protocol as `../lensing_wiki/CLAUDE.md`.
