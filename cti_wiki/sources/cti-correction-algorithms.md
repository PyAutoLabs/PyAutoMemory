---
title: Sources — CTI correction algorithms
type: sources
topics: [cti, correction-algorithms]
status: stub
---

# Sources: CTI correction algorithms

Papers on the forward-model algorithms that recover the pre-CTI image
from a CTI-distorted exposure: Bristow's first-pixel correction,
Massey's pixel-based forward model (the `arctic` algorithm),
Anderson's pix-by-pix iterative correction on HST ACS, and Israel's
Euclid-specific extension.

## Bristow 2002 — early CTI model

**File:** `CTI/Bristow2002_CTI_Model_Early.pdf`
**Concepts:** [[forward-model-cti]]
**Summary (stub):** One of the earliest physically motivated CTI
forward models, with HST FOC / STIS in mind.
(stub — verify against PDF)

## Bristow 2003 — first-pixel CTI correction

**File:** `CTI/Bristow2003_First_Pixel_CTI_Correction.pdf`
**Concepts:** [[forward-model-cti]]
**Summary (stub):** The "first pixel" correction scheme, a simpler
restoration alternative to full forward modelling.
(stub — verify against PDF)

## Massey 2009 — CTI correction I

**File:** `CTI/Massey2009_CTI_Correction_1.pdf`
**Concepts:** [[forward-model-cti]], [[arctic-algorithm]]
**Summary (stub):** The first Massey forward-model CTI correction
paper, kernel of what becomes the `arctic` algorithm used by Euclid VIS.
(stub — verify against PDF)

## Massey 2010 — CTI correction on HST

**File:** `CTI/Massey2010_CTI_Correction_On_HST.pdf`
**Concepts:** [[forward-model-cti]], [[hubble-acs-cti]]
**Summary (stub):** Application of the Massey forward-model correction
to HST ACS WFC data, validating reduction in residual CTI biases.
(stub — verify against PDF)

## Massey 2010 — pixel-based correction

**File:** `CTI/Massey2010PixelBased.pdf`
**Concepts:** [[forward-model-cti]]
**Summary (stub):** Pixel-based forward-model formulation, the
implementation that becomes `arctic`.
(stub — verify against PDF)

## Massey 2014 — CTI correction II

**File:** `CTI/Massey2014_CTI_Correction_2.pdf`
**Concepts:** [[forward-model-cti]], [[arctic-algorithm]]
**Summary (stub):** Second-generation Massey forward model with
multi-species traps and improved time-of-flight handling.
(stub — verify against PDF)

## Anderson 2010 — CTI correction on HST

**File:** `CTI/Anderson2010_CTI_Correction_HST.pdf`
**Concepts:** [[forward-model-cti]], [[hubble-acs-cti]]
**Summary (stub):** Anderson's pixel-by-pixel iterative CTI correction
on HST ACS WFC, the standard pipeline correction for ACS data.
(stub — verify against PDF)

## Anderson 2018 — ACS CTI

**File:** `CTI/Anderson2018ACS.pdf`
**Concepts:** [[hubble-acs-cti]]
**Summary (stub):** Updated Anderson-style ACS CTI correction, late-era
recalibration.
(stub — verify against PDF)

## Anderson 2021 — ACS CTI

**File:** `CTI/Anderson2021ACS.pdf`
**Concepts:** [[hubble-acs-cti]]
**Summary (stub):** Latest Anderson ACS CTI correction update; tracks
trap-density growth across the HST mission.
(stub — verify against PDF)

## Israel 2015 — CTI correction for Euclid

**File:** `CTI/Israel2015_CTI_Correct_Euclid.pdf`
**Concepts:** [[forward-model-cti]], [[euclid-vis-cti]]
**Summary (stub):** Adapts the Massey forward-model correction for
Euclid VIS, including trap-density and release-time-scale priors.
(stub — verify against PDF)

## Short 2013 — analytic CTI model

**File:** `CTI/Short2013_CTIanalyticModel.pdf`
**Concepts:** [[forward-model-cti]]
**Summary (stub):** Closed-form analytic CTI model as a fast
approximate alternative to full numerical forward modelling.
(stub — verify against PDF)

## Murray 2012 — mitigating CTI

**File:** `CTI/Murray2012_Mitigating_CTI.pdf`
**Concepts:** [[forward-model-cti]]
**Summary (stub):** Operational strategies for in-flight CTI
mitigation: pre-flashing, clocking schemes.
(stub — verify against PDF)

## Murray 2013 — multi-level clocking

**File:** `CTI/Murray2013_MultiLevel_CCD_Clocking.pdf`
**Concepts:** [[forward-model-cti]]
**Summary (stub):** Multi-level CCD clocking as a CTI-mitigation
scheme for Euclid VIS.
(stub — verify against PDF)

## Nightingale 2024 — PyAutoCTI

**File:** `CTI/Nightingale2024PyAutoCTI.pdf`
**Concepts:** [[forward-model-cti]], [[arctic-algorithm]],
[[pyautofit]] (cross-link)
**Summary (stub):** The PyAutoCTI package — a Bayesian forward-modelling
framework for CTI calibration, built on PyAutoFit. Used in Euclid VIS
trap-pumping calibration analysis.
(stub — verify against PDF; this is a co-authored / lead-authored work
relevant to PyAutoLens-adjacent infrastructure.)

## See also

- [[forward-model-cti]]
- [[arctic-algorithm]]
- [[sources-trap-pumping]]
- [[sources-euclid-vis-calibration]]
- [[sources-hst-acs-cti]]
