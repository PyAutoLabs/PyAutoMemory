---
title: arctic
type: entity
topics: [cti, software]
sources:
  - CTI/Massey2010PixelBased.pdf
  - CTI/Massey2014_CTI_Correction_2.pdf
status: stub
---

# arctic

## What it is

`arctic` (Algorithm for the Reverse Correction of Trails from
Imperfect CCDs) — the open-source C++ / Python implementation of the
Massey forward-model CTI correction, adopted by the Euclid VIS pipeline
and used in HST ACS reductions.

## Key facts

- Models each trap species with capture cross-section, release time
  scale, and density-per-pixel.
- Supports both express (fast) and full (slow, exact) modes.
- Calibrated via trap-pumping data (`arctic_calib` / PyAutoCTI).
- Authors: Massey, Israel, Hoekstra, and collaborators.

## Papers

- [[sources-cti-correction-algorithms#massey-2010-pixel-based-correction]]
- [[sources-cti-correction-algorithms#massey-2014-cti-correction-ii]]
- [[sources-cti-correction-algorithms#israel-2015-cti-correction-for-euclid]]

## See also

- [[forward-model-cti]]
- [[arctic-algorithm]]
- [[euclid-vis]]
