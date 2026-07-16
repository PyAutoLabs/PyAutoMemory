---
title: Sources — X-ray CTI and cosmic rays
type: sources
topics: [cti, xray, cosmic-rays]
status: stub
---

# Sources: X-ray CTI and cosmic rays

Papers on CTI in Chandra ACIS and on cosmic-ray rejection — adjacent
detector-systematics concerns that overlap with the CTI literature.

## Townsley 2001 — X-ray Chandra CTI

**Canonical BibTeX key:** `Townsley2002`
**Reference:** Modeling charge transfer inefficiency in the Chandra Advanced CCD Imaging Spectrometer; doi:10.1016/s0168-9002(01)02156-8; Nuclear Instruments and Methods in Physics Research, Section A: Accelerators, Spectrometers, Detectors and Associated Equipment
**Concepts:** [[ccd-trap-physics]]

**Supports:**
- Models CTI in the Chandra ACIS CCDs after radiation damage.
- Connects charge traps and parallel readout to degraded detector performance in the ACIS instrument.
- Provides a Chandra X-ray detector example of CTI modelling outside optical weak-lensing CCDs.

**Use when:**
- Citing Chandra/ACIS CTI modelling or X-ray CCD examples of radiation-induced CTI.

**Do not use for:**
- HST ACS pixel-based correction performance or Euclid VIS trap-pumping calibration.


## Grant — X-ray Chandra

**Canonical BibTeX key:** `Grant2006`
**Reference:** Temperature dependence of charge transfer inefficiency in Chandra X-ray CCDs; doi:10.1117/12.672019; High Energy, Optical, and Infrared Detectors for Astronomy II
**Concepts:** [[ccd-trap-physics]]

**Supports:**
- Studies temperature dependence of CTI in Chandra X-ray CCDs.
- Uses Chandra detector data as an example of how operating conditions affect CTI behaviour.

**Use when:**
- Citing temperature-dependent CTI behaviour in Chandra X-ray CCDs.

**Do not use for:**
- General-purpose optical cosmic-ray rejection or HST ACS CTI correction algorithms.


## van Dokkum 2001 — L.A.Cosmic

**Canonical BibTeX key:** `VanDokkum2002`
**Reference:** Cosmic‐Ray Rejection by Laplacian Edge Detection; doi:10.1086/323894; Publ. Astron. Soc. Pac.
**Concepts:** [[ccd-trap-physics]]

**Supports:**
- Introduces L.A.Cosmic, a cosmic-ray rejection algorithm based on Laplacian edge detection.
- Targets single-exposure CCD data where conventional contrast-based rejection can fail.
- Distinguishes sharp cosmic-ray edges from undersampled point sources in imaging and spectroscopic data.

**Use when:**
- Citing Laplacian-edge cosmic-ray rejection in CCD image preprocessing.

**Do not use for:**
- CTI trap modelling, charge-transfer correction, or radiation-damage calibration.


## See also

- [[ccd-trap-physics]]
- [[sources-cti-detector-physics]]
