---
title: Charge Transfer Inefficiency (CTI)
type: concept
topics: [cti, detector-systematics]
sources:
  - CTI/ShockleyRead1952.pdf
  - CTI/Massey2010PixelBased.pdf
  - CTI/Israel2015_CTI_Correct_Euclid.pdf
status: stub
---

# Charge Transfer Inefficiency (CTI)

## TL;DR

CTI is the small fraction of charge that fails to transfer perfectly
between CCD pixels during readout. In an irradiated CCD (Hubble ACS,
Gaia, Euclid VIS, Roman WFI), high-energy protons displace silicon
atoms and create deep-level "traps" in the buried channel; as a charge
packet clocks past, traps capture electrons and release them
stochastically into trailing pixels. The visible effect is asymmetric
charge trails behind every bright source, ~10⁻⁵ shape biases that
matter at the 0.1 % level required for weak-lensing cosmology, and
biased point-source astrometry / photometry. Forward-model corrections
(`arctic`, Anderson) recover the pre-CTI image given a calibrated trap
model.

## What it is

A CTI trap is characterised by:

- A capture cross-section (σ_e × volume).
- A release time-scale τ (in pixel transfers), set by Shockley–Read–Hall
  thermal-emission kinetics at the device temperature.
- A density per pixel, growing roughly linearly with cumulative
  radiation dose.

Multiple trap species (one per energy level of the dominant defects)
coexist; flight detectors typically need 3–5 species to fit the
charge-trail residuals.

CTI grows over a mission: HST ACS WFC's CTI today is ~1000× worse than
at launch. Euclid VIS launched (2023) with a budget that survives the
end-of-mission CTI growth provided the forward-model correction stays
calibrated.

## Why it matters for PyAutoLens

Indirect but real. Euclid will produce ~10⁵ strong lenses (the largest
lens-modeling sample ever, by far); residual CTI biases the lens-light
and source-light morphology that PyAutoLens fits. Trap-pumping
calibration data, processed via PyAutoCTI (built on PyAutoFit), feeds
the Euclid VIS CTI correction.

## Key references

- Foundational: [[sources-cti-detector-physics#shockley-read-1952-recombination-theory]].
- Forward-model correction: [[sources-cti-correction-algorithms#massey-2010-pixel-based-correction]],
  [[sources-cti-correction-algorithms#israel-2015-cti-correction-for-euclid]].
- Calibration via trap pumping: [[sources-trap-pumping]].
- Weak-lensing impact: [[sources-cti-shape-bias]].
- PyAutoCTI: [[sources-cti-correction-algorithms#nightingale-2024-pyautocti]].

## See also

- [[forward-model-cti]]
- [[trap-pumping]]
- [[arctic-algorithm]]
- [[euclid-vis-cti]]
- `../lensing/entities/pyautofit.md`
