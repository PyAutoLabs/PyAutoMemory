---
title: Non-uniform FFT (NUFFT)
type: concept
topics: [nufft, interferometry]
sources:
  - NUFFTPAper.pdf
  - PYNUFFT.pdf
  - Software/NUFFTGPU.pdf
status: stub
---

# Non-uniform FFT (NUFFT)

## TL;DR

The Fourier transform between an image plane and a non-regular set of
visibility samples (e.g. interferometer uv-coverage) is implemented in
PyAutoLens via the NUFFT. Plain FFTs require regular grids; the NUFFT
extends them to arbitrary sample points by spreading visibilities onto
an oversampled regular grid with a Kaiser–Bessel or Gauss kernel, then
FFT-ing. GPU NUFFTs (jax-finufft, cufinufft) enable VLBI / SKA-scale
lens modelling at JAX speeds.

## What it is

For PyAutoLens interferometric models:
1. Apply the lensing operator to a source-plane model image.
2. NUFFT the lensed image plane onto the observed uv samples.
3. Compare in visibility space.

Critical knobs are the spreading-kernel width and the oversampling
factor; tradeoffs determine accuracy vs speed.

## Why it matters for PyAutoLens

ALMA, VLBI, SKA, and MERLIN lens modelling all live in visibility
space. The NUFFT is the per-iteration cost driver. The PyLops /
jax-finufft ecosystems give a path to GPU-accelerated forward models.

## Key references

- NUFFT: [[sources-nufft#nufft-paper]].
- PyNUFFT: [[sources-nufft#pynufft]].
- GPU NUFFT: [[sources-nufft#nufft-gpu]].
- PyLops: [[sources-scientific-software#pylops]].

## See also

- [[nufft]]
- [[jax-finufft]]
- `../lensing_wiki/concepts/interferometric-lensing.md`
