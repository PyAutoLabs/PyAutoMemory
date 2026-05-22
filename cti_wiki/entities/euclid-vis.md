---
title: Euclid VIS
type: entity
topics: [euclid, cti]
sources:
  - CTI/Cropper2013DefiningWL.pdf
  - Euclid/Azzollini2021CIReport.pdf
  - CTI/Israel2015_CTI_Correct_Euclid.pdf
status: stub
---

# Euclid VIS

## What it is

The Visible Imager (VIS) on ESA's Euclid mission — a 36-CCD mosaic
covering ~0.5 deg² per pointing, optimised for cosmic-shear shape
measurement at 0.16″ resolution in a broad I_E band.

## Key facts

- Detectors: e2v CCD273-84, n-channel, p-channel format.
- Launched: July 2023. Wide and Deep surveys ongoing.
- Shape-measurement budget for weak-lensing cosmology drives a strict
  residual-CTI requirement (Cropper 2013), enforced by:
  - Forward-model correction using `arctic` (Massey / Israel algorithm).
  - Charge-injection lines for monitoring (Azzollini 2021).
  - In-flight trap pumping for trap-parameter refresh.
- Strong-lensing science: VIS is expected to find ~10⁵ galaxy-scale
  lenses across the Euclid Wide Survey, the largest sample ever for
  PyAutoLens-class modelling.

## Papers

- Weak-lensing requirements: [[sources-euclid-vis-calibration#cropper-2013-defining-weak-lensing-requirements]].
- CTI correction algorithm: [[sources-cti-correction-algorithms#israel-2015-cti-correction-for-euclid]].
- Charge-injection: [[sources-euclid-vis-calibration#azzollini-2021-charge-injection-report]].

## See also

- [[euclid-vis-cti]]
- [[arctic]]
- [[charge-injection]]
- `../lensing_wiki/entities/euclid-q1.md`
