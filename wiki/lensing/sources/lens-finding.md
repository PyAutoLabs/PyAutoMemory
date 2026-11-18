---
title: Sources — lens finding
type: sources
topics: [surveys, methods]
status: drafted
---

# Sources: lens finding

## Metcalf 2018 — Lens Finding Challenge

**Canonical BibTeX key:** `Metcalf2018`
**Reference:** A&A 625, A119 (2019); arXiv:1802.03609; doi:10.1051/0004-6361/201832797
**Concepts:** [[lens-finding]], [[lens-finding-challenge]]

**Supports:**
- The open challenge compared visual, classical, and machine-learning methods on 100,000 simulated candidates.
- Finder efficiency and bias depend strongly on realistic simulations and control of false positives.

**Use when:**
- Motivating common benchmarks or calibrated selection functions for automated lens finding.

**Do not use for:**
- The completeness of a specific real-survey lens catalogue.

## Jacobs 2019 — DES lenses

**Canonical BibTeX key:** `Jacobs2019`
**Reference:** MNRAS 484, 5330–5349; arXiv:1811.03786; doi:10.1093/mnras/stz272
**Concepts:** [[lens-finding]], [[des-lenses]]

**Supports:**
- CNN ensembles trained with simulated lenses were applied to 1.1 million DES sources.
- Visual inspection of network-ranked candidates produced 84 new strong-lens candidates.

**Use when:**
- Citing CNN-based searches for high-redshift galaxy-galaxy lenses in DES.

**Do not use for:**
- Spectroscopic confirmation or purity of the candidate sample.

## Jaelani 2023 — HSC lens find

**Canonical BibTeX key:** `Jaelani2023`
**Reference:** arXiv:2312.07333
**Concepts:** [[lens-finding]], [[hsc-survey-lenses]]

**Supports:**
- CNNs searched 2.35 million galaxies over roughly 800 square degrees of HSC-SSP imaging.
- Human inspection produced 43 definite and 269 probable candidates, including 97 new systems.

**Use when:**
- Citing CNN lens finding and candidate yields in HSC-SSP.

**Do not use for:**
- A spectroscopically complete HSC lens sample.

## Rojas 2022 — DES lens modelling+finding

**Canonical BibTeX key:** `Rojas2022`
**Reference:** A&A 668, A73; arXiv:2109.00014; doi:10.1051/0004-6361/202142119
**Concepts:** [[lens-finding]], [[deep-learning-lensing]]

**Supports:**
- A CNN search of a colour-selected DES luminous-red-galaxy sample produced 405 candidates after visual inspection.
- An automated modelling pipeline successfully modelled 79% of a 52-system single-deflector subset.

**Use when:**
- Connecting DES candidate finding, visual grading, and automated follow-up modelling.

**Do not use for:**
- Spectroscopic confirmation of every reported candidate.

## Holloway 2024 — Bayesian lens finding

**Canonical BibTeX key:** `Holloway2024`
**Reference:** MNRAS 530, 1297–1310; arXiv:2311.07455; doi:10.1093/mnras/stae875
**Concepts:** [[lens-finding]], [[selection-effects]]

**Supports:**
- Calibrated probabilities can combine citizen-science and neural-network classifier scores.
- The ensemble improved completeness at a fixed low false-positive rate over the best individual classifier.

**Use when:**
- Discussing calibrated classifier ensembles, follow-up prioritisation, or population-level selection effects.

**Do not use for:**
- Claims that PyAutoLens evidence or lens-model evidence was the classification statistic.

## Gavazzi 2012 — SL2S I

**Canonical BibTeX key:** `Gavazzi2012`
**Reference:** ApJ 761, 170; arXiv:1202.3852; doi:10.1088/0004-637X/761/2/170
**Concepts:** [[sl2s]], [[lens-statistics]]

**Supports:**
- The SL2S-I analysis modelled mass and light alignment for 16 lensing early-type galaxies at redshift 0.2–0.9.
- The inferred external shear indicates a substantial environmental contribution around the sample lenses.

**Use when:**
- Citing SL2S mass-light alignment or environmental shear measurements.

**Do not use for:**
- Ringfinder completeness or purity.

## Gavazzi 2014 — Ringfinder

**Canonical BibTeX key:** `Gavazzi2014`
**Reference:** ApJ 785, 144; arXiv:1403.1041; doi:10.1088/0004-637X/785/2/144
**Concepts:** [[lens-finding]], [[sl2s]]

**Supports:**
- Ringfinder detects blue residuals around smooth red foreground galaxies using two-band difference imaging.
- Simulations quantify its completeness and purity before and after visual inspection in CFHTLS-like data.

**Use when:**
- Citing colour-residual lens finding or its selection function.

**Do not use for:**
- CNN-based lens classification.

## Sonnenfeld 2018 — Yattalens

**Canonical BibTeX key:** `Sonnenfeld2018b`
**Reference:** PASJ 70, S29; arXiv:1704.01585; doi:10.1093/pasj/psx062
**Concepts:** [[lens-finding]], [[hsc-survey-lenses]]

**Supports:**
- YattaLens finds arc-like features and evaluates candidates with a lens-model fit.
- Comparison with CHITAH and spectroscopic selection showed complementary recovery across methods.

**Use when:**
- Citing the automated SuGOHI-I search or model-based YattaLens selection.

**Do not use for:**
- The later Space Warps crowdsourced HSC search.

## Sonnenfeld 2020 — HSC Space Warps

**Canonical BibTeX key:** `Sonnenfeld2020`
**Reference:** A&A 642, A148; arXiv:2004.00634; doi:10.1051/0004-6361/202038067
**Concepts:** [[lens-finding]], [[hsc-survey-lenses]]

**Supports:**
- Nearly 6,000 citizen volunteers searched a massive-galaxy sample drawn from 442 square degrees of HSC imaging.
- The study compared crowdsourced discoveries with YattaLens and found the methods complementary.

**Use when:**
- Citing Space Warps crowdsourcing or human-versus-automated HSC searches.

**Do not use for:**
- A joint lens-modelling-and-finding pipeline.

## Space Warps 2017 — Spaghetti

**Canonical BibTeX key:** `Kung2017`
**Reference:** Models of gravitational lens candidates from SpaceWarps CFHTLS; doi:10.1093/mnras/stx3012; arXiv:1711.07297; Monthly Notices of the Royal Astronomical Society
**Concepts:** [[lens-finding]], [[space-warps]]

**Supports TODO:**
- TODO — resolve the canonical key and verify the Space Warps claim context before using as evidence.

**Use when TODO:**
- TODO — use only after the paper identity and canonical key are resolved.

**Do not use for TODO:**
- Evidence until the paper identity and canonical key are verified.

## Tran 2022 — AGEL

**Canonical BibTeX key:** `Tran2022`
**Reference:** AJ 164, 148; arXiv:2205.05307; doi:10.3847/1538-3881/ac7da2
**Concepts:** [[des-lenses]], [[lens-finding]]

**Supports:**
- AGEL spectroscopy confirmed CNN-selected strong lenses in DES and DECaLS fields.
- The confirmed sample extends to higher lens redshift than many earlier surveys.

**Use when:**
- Citing spectroscopic confirmation and redshift measurement for automated-search candidates.

**Do not use for:**
- The completeness of the parent CNN search.

## d'Exivry 2009 — atlas of lenses

**Canonical BibTeX key:** `OrbandeXivry2008`
**Reference:** MNRAS 399, 2–20; arXiv:0904.1454; doi:10.1111/j.1365-2966.2009.14925.x
**Concepts:** [[lens-finding]]

**Supports:**
- Multi-component lens potentials predict unusual high-multiplicity and high-magnification image configurations.
- The paper estimates that several exotic galaxy-scale configurations should be rare in all-sky surveys.

**Use when:**
- Discussing recognition or expected abundance of exotic lens morphologies.

**Do not use for:**
- A catalogue of ordinary galaxy-scale lens candidates.

## Pearson 2021 — ML + parametric modelling

**Canonical BibTeX key:** `Pearson2021a`
**Reference:** MNRAS 505, 4362–4382; arXiv:2103.03257; doi:10.1093/mnras/stab1547
**Concepts:** [[deep-learning-lensing]], [[mass-models]]

**Supports:**
- A Bayesian CNN can estimate lens mass-profile parameters and uncertainties much faster than conventional fitting.
- CNN-informed priors can improve the speed and accuracy of subsequent parametric modelling.

**Use when:**
- Citing hybrid neural-network and parametric lens modelling.

**Do not use for:**
- Lens-candidate discovery or finder completeness.

## O'Riordan 2023 — Euclid

**Canonical BibTeX key:** `ORiordan2023`
**Reference:** MNRAS 521, 2342–2356; arXiv:2211.15679; doi:10.1093/mnras/stad650
**Concepts:** [[euclid-q1]], [[dark-matter-substructure]]

**Supports:**
- Machine-learning sensitivity maps can estimate subhalo detectability in Euclid VIS-like strong-lens images.
- Detectable subhalo yields vary sharply across lens configurations, motivating selection of the most sensitive lenses.

**Use when:**
- Forecasting dark-matter substructure sensitivity for Euclid-like imaging.

**Do not use for:**
- The observed contents or completeness of the Euclid Q1 lens catalogue.

## Wang 2025 — Euclid

**Canonical BibTeX key:** `Wang2025`
**Reference:** arXiv:2501.16139
**Concepts:** [[dark-matter-substructure]], [[bulge-halo-decomposition]]

**Supports:**
- Euclid-like lens imaging can probe the stellar-to-halo mass relation with detected line-of-sight haloes or subhaloes.
- Simultaneously modelling light from the main lens and perturber is required to avoid bias in the inferred halo mass.

**Use when:**
- Motivating strong-lens constraints on the low-mass stellar-to-halo mass relation.

**Do not use for:**
- Euclid Q1 lens-finding performance or catalogue statistics.

## Euclid Collaboration 2025 — Discovery Engine A

**Canonical BibTeX key:** `EuclidCollaboration2025`
**Reference:** arXiv:2503.15324
**Concepts:** [[euclid-q1]], [[lens-finding]], [[lens-statistics]]

**Supports:**
- Euclid Q1 yielded 497 galaxy-galaxy lens candidates over 63 square degrees, including 250 grade-A candidates.
- The discovery system combined deep learning, citizen-science inspection, expert vetting, and per-system modelling.

**Use when:**
- Citing the Q1 system overview, catalogue, or survey-scale yield forecast.

**Do not use for:**
- Detailed performance of any one machine-learning classifier.

## Euclid Collaboration 2025 — Discovery Engine B

**Canonical BibTeX key:** `EuclidCollaboration2025b`
**Reference:** arXiv:2503.15325
**Concepts:** [[euclid-q1]], [[lens-finding]]

**Supports:**
- Expert inspection of 11,660 high-velocity-dispersion galaxy images found 38 grade-A and 40 grade-B candidates.
- Expert-classified non-lenses and realistic simulated lenses provide training data for automated classifiers.

**Use when:**
- Discussing targeted visual searches or construction of Q1 lens-finder training data.

**Do not use for:**
- The full Q1 catalogue or blind machine-learning search performance.

## Euclid Collaboration 2025 — Discovery Engine C

**Canonical BibTeX key:** `EuclidCollaboration2025a`
**Reference:** arXiv:2503.15326
**Concepts:** [[euclid-q1]], [[lens-finding]], [[deep-learning-lensing]]

**Supports:**
- Five machine-learning models were evaluated on Euclid Q1 lens finding and validated by citizen scientists and experts.
- A fine-tuned Zoobot model ranked 122 grade-A and 41 grade-B lenses in its top 1,000 candidates.

**Use when:**
- Citing Q1 machine-learning ranking performance or human validation of classifier outputs.

**Do not use for:**
- The targeted high-velocity-dispersion visual search.

## Vincken 2026 — Euclid DR1 lens-finding network comparison

**Canonical BibTeX key:** `Vincken2026`
**Reference:** TODO — in preparation, not yet on arXiv. Refresh with the verified title, arXiv ID and DOI once the paper is public.
**Concepts:** [[euclid-q1]], [[lens-finding]], [[deep-learning-lensing]]

**Supports:**
- Placeholder only — a citable canonical key for the Euclid DR1 strong lens finding network comparison. No claim has been verified against a public record.

**Use when:**
- You need a stable key to cite the DR1 network-comparison paper before it is public. Nothing more.

**Do not use for:**
- Any quantitative result, method detail or interpretation. The paper is an unpublished Euclid Consortium draft; replace this entry with verified claims once it is on arXiv.

## Euclid Collaboration: Lines 2026 — ECLIPSE A, DR1 strong-lens catalogue

**Canonical BibTeX key:** `EuclidDR1EclipseA`
**Reference:** Euclid Data Release 1 (DR1). Euclid Lens Identification Pipeline and Scientific Exploration (ECLIPSE) A: Strong lens catalogue overview; arXiv:2611.15883 (submitted to A&A, Euclid DR1 special issue)
**Concepts:** [[lens-finding]], [[lens-statistics]], [[euclid-q1]], [[deep-learning-lensing]]

**Supports:**
- 15 072 high-confidence strong-lens candidates over 2000 deg^2 of Euclid DR1 (6073 grade A, 8999 grade B), published with a further 9010 grade C candidates; more high-confidence candidates than all previous catalogues combined.
- 68 million of roughly 900 million DR1 sources passed the catalogue selection and were searched by a pipeline combining five machine-learning models, about 7000 citizen scientists and 67 strong-lensing experts.
- The catalogue includes 84 candidate double-source-plane lenses, over 1000 candidate disc lenses and several hundred candidate lensed AGN/quasars.
- Deflectors are mostly massive and quiescent (log M*/M_sun = 11.39 +0.29/-0.33, Salpeter IMF) at z = 0.68 +0.33/-0.29, with typical Einstein radius 0.85 +0.44/-0.24 arcsec; extrapolating by area gives over 100 000 high-confidence candidates in the Euclid Wide Survey.

**Use when:**
- Citing the Euclid DR1 lens sample, its size and composition, or the forecast Euclid Wide Survey yield.

**Do not use for:**
- Search-stage details or completeness (use `EuclidDR1EclipseB`), or lens-model methodology (use `EuclidDR1EclipseC`); Q1-era numbers (use the `EuclidCollaboration2025*` entries).

## Euclid Collaboration: Holloway 2026 — ECLIPSE B, DR1 discovery pipeline

**Canonical BibTeX key:** `EuclidDR1EclipseB`
**Reference:** Euclid Data Release 1 (DR1). Euclid Lens Identification Pipeline and Scientific Exploration (ECLIPSE) B: Discovery pipeline overview; arXiv:2611.15886 (submitted to A&A, Euclid DR1 special issue)
**Concepts:** [[lens-finding]], [[deep-learning-lensing]], [[selection-effects]], [[space-warps]]

**Supports:**
- The DR1 search runs in stages: a catalogue-level cut, a machine-learning and ensemble search, a two-stage citizen-science search, and expert grading of candidates.
- Neural networks classified over 68 million objects; volunteers made more than 4.5 million classifications of 300 000 objects; researchers inspected over 30 000 objects.
- Measured completeness is 0.73 +0.08/-0.15 for grade A ('definite') systems and 0.34 +0.05/-0.06 for grade A+B, so the search finds most definite lenses in the DR1 area.
- Expert grading is subjective; the paper calibrates individual inspector biases and shows that lens modelling (ECLIPSE C) helps decide the nature of a candidate.

**Use when:**
- Citing how Euclid DR1 lenses were found, the completeness of a multi-stage ML + citizen-science + expert search, or inspector-bias calibration.

**Do not use for:**
- Catalogue-level population statistics (use `EuclidDR1EclipseA`) or the performance of a single named network.

## Li, Shu & Nie 2026 — HSC lenses at z_lens > 0.8 confirmed with DESI

**Canonical BibTeX key:** `Li2026HSCDESI`
**Reference:** Confirming HSC strong lens candidates with DESI Spectroscopy. II. Analysis of 80 galaxy-scale systems with lens redshifts above 0.8; arXiv:2611.07524
**Concepts:** [[lens-finding]], [[hsc-survey-lenses]], [[mass-models]]

**Supports:**
- Lens modelling of 80 galaxy-scale candidates with z_lens > 0.8 (from paper I's 84) classifies 71 (about 90%) as secure, 8 as probable or possible, and 1 as a non-lens, nearly tripling the known galaxy-scale lenses at z_lens > 0.8.

**Use when:**
- Citing a high-redshift (z_lens > 0.8) galaxy-scale lens sample for total-mass-slope evolution tests.

**Do not use for:**
- A measured density-slope evolution; this paper confirms the sample, it does not yet report the slope result.

## See also

- [[lens-finding]]
- [[deep-learning-lensing]]
- [[euclid-q1]]
