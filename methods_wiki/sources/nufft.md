---
title: Sources — non-uniform FFT
type: sources
topics: [nufft, interferometry, methods]
status: stub
---

# Sources: non-uniform FFT

Papers on the non-uniform fast Fourier transform — the workhorse
operator for interferometric lensing forward models (ALMA, VLBI, SKA)
and for the PyLops sparse-linear-operator framework.

## NUFFT paper

**Canonical BibTeX key:** `Jacob2009`
**Reference:** Optimized least-square nonuniform fast Fourier transform; doi:10.1109/tsp.2009.2014809; IEEE Transactions on Signal Processing
**Concepts:** [[nufft]]

**Supports:**
- Presents an optimized least-squares formulation for nonuniform fast Fourier transforms.
- Supports NUFFT use where samples are not on a regular Fourier grid.
- Provides a signal-processing reference for accurate nonuniform Fourier operators.

**Use when:**
- Citing optimized least-squares NUFFT methodology.

**Do not use for:**
- GPU-specific NUFFT auto-tuning or PyNUFFT package citation.


## PyNUFFT

**Canonical BibTeX key:** `Lin2017`
**Reference:** Python Non-Uniform Fast Fourier Transform (PyNUFFT): multi-dimensional non-Cartesian image reconstruction package for heterogeneous platforms and applications to MRI; arXiv:1710.03197; arXiv
**Concepts:** [[nufft]]

**Supports:**
- Presents PyNUFFT as a Python package for multidimensional non-Cartesian image reconstruction.
- Targets heterogeneous platforms and MRI-style non-Cartesian Fourier applications.
- Provides the package-level citation for PyNUFFT.

**Use when:**
- Citing PyNUFFT software or Python nonuniform FFT reconstruction tooling.

**Do not use for:**
- General NUFFT theory independent of the package.


## NUFFT GPU

**Canonical BibTeX key:** TODO — previous automated match was not sufficiently verified for claim use; resolve against `bibliography/pyautopaper.bib` before citing.
**Reference:** TODO — verify the public paper record and canonical BibTeX key.
**Concepts:** [[nufft]]

**Supports TODO:**
- TODO — not migrated: canonical-key identity needs manual verification.

**Use when TODO:**
- TODO — use only after the paper identity and canonical key are resolved.

**Do not use for TODO:**
- Evidence until the paper identity and canonical key are verified.

## PyLops — root

**Canonical BibTeX key:** TODO — no unique match found in `bibliography/pyautopaper.bib`.
**Reference:** TODO — identify the public paper record and add or resolve the canonical BibTeX key.
**Concepts:** [[linear-inversion]], [[nufft]]

**Supports TODO:**
- TODO — not migrated: paper identity or canonical bibliography entry is unresolved.

**Use when TODO:**
- TODO — use only after the paper is identified and claim support is verified.

**Do not use for TODO:**
- Evidence until the paper identity and canonical key are verified.


## PyLops — Software/

**Canonical BibTeX key:** `PyLops`
**Reference:** PyLops -- A Linear-Operator Python Library for large scale optimization; arXiv:1907.12349
**Concepts:** [[linear-inversion]]

**Supports:**
- Presents PyLops as a Python library built around linear-operator abstractions.
- Targets large-scale optimization problems where matrix-free operators are useful.
- Provides the package citation for PyLops in inverse-problem workflows.

**Use when:**
- Citing PyLops software or linear-operator abstractions in Python.

**Do not use for:**
- A NUFFT-specific algorithm unless PyLops is the implementation being cited.


## See also

- [[nufft]]
- [[jax-finufft]]
- [[../lensing_wiki/concepts/interferometric-lensing.md]]
