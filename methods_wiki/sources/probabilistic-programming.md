---
title: Sources — probabilistic programming languages
type: sources
topics: [ppl, methods]
status: stub
---

# Sources: probabilistic programming languages

Papers / reference manuals for PPLs that PyAutoFit and PyAutoLens
adjacent work either uses or competes with.

## STAN

**Canonical BibTeX key:** `Carpenter2017`
**Reference:** Stan: A probabilistic programming language; doi:10.18637/jss.v076.i01; Journal of Statistical Software
**Concepts:** [[probabilistic-programming]], [[hamiltonian-monte-carlo]]

**Supports:**
- Presents Stan as a probabilistic programming language.
- Supports Bayesian model specification with automatic inference machinery.
- Provides the canonical software/method citation for Stan.

**Use when:**
- Citing Stan or probabilistic programming for Bayesian models.

**Do not use for:**
- PyMC, Pyro, or PyAutoFit-specific API claims.


## PyMC3

**Canonical BibTeX key:** `Salvatier2016`
**Reference:** Probabilistic programming in Python using PyMC3; arXiv:1507.08050; doi:10.7717/peerj-cs.55; PeerJ Computer Science
**Concepts:** [[probabilistic-programming]]

**Supports:**
- Presents PyMC3 as a Python probabilistic-programming system.
- Supports Bayesian statistical modelling with MCMC and related inference tools.
- Provides the canonical citation for PyMC3 software.

**Use when:**
- Citing PyMC3 or Python probabilistic programming.

**Do not use for:**
- Stan, Pyro, or PyAutoFit-specific implementation details.


## Pyro

**Canonical BibTeX key:** `Bingham2019`
**Reference:** Pyro: Deep universal probabilistic programming; arXiv:1810.09538; Journal of Machine Learning Research
**Concepts:** [[probabilistic-programming]], [[deep-learning-astro]]

**Supports:**
- Presents Pyro as a deep universal probabilistic-programming system.
- Connects probabilistic modelling with deep-learning frameworks.
- Provides the software citation for Pyro.

**Use when:**
- Citing Pyro or deep probabilistic programming.

**Do not use for:**
- General Bayesian inference without Pyro-specific relevance.


## GetDist

**Canonical BibTeX key:** `Lewis2019`
**Reference:** GetDist: a Python package for analysing Monte Carlo samples; arXiv:1910.13970; preprint (arXiv:1910.13970)
**Concepts:** [[probabilistic-programming]]

**Supports:**
- Presents GetDist as a Python package for analysing Monte Carlo samples.
- Supports posterior-sample analysis and visualization workflows.
- Provides the package citation for GetDist.

**Use when:**
- Citing GetDist for Monte Carlo sample analysis.

**Do not use for:**
- Running samplers or defining probabilistic models.


## corner

**Canonical BibTeX key:** `Foreman-Mackey2016`
**Reference:** corner.py: Scatterplot matrices in Python; doi:10.21105/joss.00024; J. Open Source Softw.
**Concepts:** [[probabilistic-programming]]

**Supports:**
- Presents corner.py for scatterplot-matrix visualizations in Python.
- Supports visualizing multidimensional posterior samples and parameter covariances.
- Provides the JOSS software citation for corner.py.

**Use when:**
- Citing corner plots or corner.py visualisation.

**Do not use for:**
- Sampler algorithms or posterior-estimation methodology.


## See also

- [[probabilistic-programming]]
- [[sources-samplers]]
- [[sources-bayesian-inference]]
