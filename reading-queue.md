# Reading queue

Papers waiting to be read and filed. Format:

- `## <Section>` headers group papers by domain (matching `wiki/<domain>/`
  where one exists).
- One paper per line — a bare title, optionally followed by ` — <arXiv id or URL>`.
- **Add the ref whenever you know it.** It is what lets the Dashboard link the
  paper's arXiv abstract page and put a 📄 one-tap PDF button beside it; without
  one the board can only offer an arXiv title *search*, which costs a results
  page and a squint per paper. `scripts/backfill_arxiv_refs.py` (nightly, via
  `.github/workflows/arxiv_refs.yml`) fills in the ones nobody wrote by hand,
  and only when exactly one arXiv paper's title matches.
- A read/consumed paper is never deleted: prefix its line with
  `DONE <YYYY-MM-DD> — ` and leave it in place (the reading history).
- **Not every line is a paper.** Two kinds are not, and marking them keeps the
  Dashboard from offering a download button for a heading and stops the nightly
  ref backfill spending an arXiv lookup on one:
  - `__Bold Text__` on its own line is a **sub-heading** grouping the papers
    below it. Rendered as a heading, never counted, never looked up.
  - `NOTE <text>` is an **annotation** — a remark, a link that is not a paper,
    a stray line of pasted prose. Sibling of the `DONE ` prefix: same shape,
    same never-delete rule. A bare non-arXiv link counts as one automatically.
    `scripts/backfill_arxiv_refs.py --mark-unresolved` applies the prefix in
    bulk to lines it could not identify — run it after reading a dry run, since
    an unresolved title is more often a real paper whose line lost something
    (a LaTeX redshift, a wrapped subtitle) than a genuine non-paper.
  - A line that is *only* an arXiv link is still a paper — the title was just
    never written, so the board labels it `arXiv:<id>`.
- Filing a read paper: add its canonical entry to `bibliography/`, stub it in
  the matching `wiki/<domain>/sources/*.md` page per `wiki/CLAUDE.md`, then
  mark the line DONE and run `make validate`.

(Moved from `admin_jammy/papers.md` on 2026-05-22, when this repo — then
PyAutoPaper, now PyAutoMemory — became the unified knowledge repo.)

---

## Strong Lensing
DONE 2026-08-21 — The X-Ray Continuum Emission Region in the Lensed Quasar SDSS J133907.23+131038.6 is Much Smaller than the Accretion Disk
Confirmation of the Finch Flatter-Fainter Relation for the Quadruple Images of Lensed Point Sources — 2608.17116
The Koi Pond: A Strongly Lensed Protocluster Core hosting a Diverse Population of DSFGs — 2608.15997
Addressing position anomalies in the Strong Gravitational Lensing System HS~0810+2554 through Dark Matter Subhalos — 2608.15554
The Fornax Cluster VLT Spectroscopic Survey - V. Mass modelling of the BCG NGC 1399 out to 150 kpc — 2608.02730
Galaxy-LRD Strong Lenses: A Missing Population? — 2608.02739
Cosmic CORALS: Timing the Universe with high-z star clusters — 2607.19472
Polar coordinate transformations for machine learning based dark matter subhalo detection in strong gravitational lenses — 2607.02663
XShooter DESI Lens Program: Sample characterization — 2607.08562
Strong-lensing effects in high-redshift massive black-hole binary population inference — 2607.03345

LEGGOS III: Mapping Star Formation and Dust in Gravitationally Lensed Galaxies with SUMAC, a UMAP and Clustering Framework
LEGGOS II: A Strong Lens Model and Source-Plane Projection of the Clumpy Star-Forming Galaxy SGASJ111020.0+645950.8 at z=2.48

Dynamical models of cluster members to probe the total mass properties of cluster subhalos. I. A comparison with parametric strong lensing models — 2606.05298
COOL-LAMPS IX: A Rare Duo of Quasars Each Lensed by a Single Massive Galaxy Cluster — 2605.13514
Beyond collective fluctuations: probing micro-image swarms in lensed quasars with intensity interferometry — 2605.02181
Constraining Axion-like Particles through Multi-epoch Monitoring of Strong Gravitational Lenses — 2602.12863
Mapping dark matter in the Bullet Cluster using JWST imaging and spectroscopy — 2601.22245
Detecting Strongly-Lensed Supernovae in Wide-field Space Telescope Imaging via Deep Learning — 2512.19886
Microlensing Black Hole Shadows-II: Constraining Primordial Black Hole Dark Matter using the photon rings of M87 and Sgr A* — 2512.20037
SLICE -- Combining Strong Lensing and X-ray in AC\,114. Insights into the Merger Scenario
Tracing Structure: Shape and Centroid Deviations in 39 Strong Lensing Clusters as a Test of Cluster Formation Predictions — 2511.22661
A Super-Eddington, Lensing-Magnified Quasar at  observed with JWST
Caustic crossings in giant arcs with extended dark matter objects — 2511.20761
Kinematic Mapping of Giant Arcs: A New Method to Locate Lensing Critical Curves — 2511.18479
VENUS: A Strongly Lensed Clumpy Galaxy at  behind the Galaxy Cluster MACS J0257.1-2325
Investigating the Dark Energy Constraint from Strongly Lensed AGN at LSST-Scale — 2511.13669
The Chandra Strong Lens Sample: Measuring the Dynamical States and Relaxation Fraction of a Sample of 28 Strong Lensing Selected Galaxy Clusters — 2511.12707
The Impact of Orbital Anisotropy Assumptions in Lensing-Dynamics Modeling — 2511.12013
SourceREACH (Source REconstruction of Arcs behind Cluster Halos): A New Source Reconstruction Algorithm Optimized for Giant Arcs and Galaxy Cluster Lenses
JWST Lensed Quasar Dark Matter Survey III: Dark Matter Sensitive Flux Ratios and Warm Dark Matter Constraint from the Full Sample. — 2511.07765
A Strong Gravitational Lensing Model of PSZ2 G118.46+39.32
CSST Strong Lensing Preparation: Cosmological Constraints Forecast from CSST Galaxy-Scale Strong Lensing — 2511.08030
The complicated nature of the X-ray emission from the field of the strongly lensed hyperluminous infrared galaxy PJ1053+60 at z=3.54
A cosmographic analysis using DESI-DR2 and strong lensing: I. Time-Delay measurements — 2511.00788
A cosmographic analysis using DESI-DR2 and strong lensing: II. Distance Ratio measurements — 2511.00789
Detecting dark matter substructure with lensed quasars in optical bands — 2510.09148
CURLING -- II. Improvement on the  Inference from Pixelized Cluster Strong Lens Modeling
iPTF16geu through the lens of thermonuclear explosion models — 2510.01160
Forecasting the Observable Rates of Gravitationally Lensed Supernovae for the PASSAGES Dusty Starbursts — 2510.00923
The Case for Space: Estimating Precise Time Delays from Ground- and Space-Based Observations of Lensed Supernovae with Glimpse — 2509.25350
JWST Discovery of Strong Lensing from a Galaxy Cluster at Cosmic Noon: Giant Arcs and a Highly Concentrated Core of XLSSC 122 — 2508.08356
HOLISMOKES XVIII: Detecting strongly lensed SNe Ia from time series of multi-band LSST-like imaging data
The  collar of early-type galaxies -- probing evolution by focusing on the inner stellar density profile
High-Dimensional Bayesian Model Comparison in Cosmology with GPU-accelerated Nested Sampling and Neural Emulators — 2509.13307
THE STELLAR AND DARK MATTER DISTRIBUTIONS IN ELLIPTICAL GALAXIES MEASURED BY  STACKED WEAK GRAVITATIONAL LENSING
Model independent lensing sub-structure detection with multiply-imaged star clusters constellations — 2608.21253
On what scales does strong lensing robustly constrain the mass profile of low-mass perturbers? — 2608.20454


## SMBHs
Overmassive and Undermassive Massive Black Holes: The Role of Environment and Gravitational-Wave Recoils — 2603.02811
Core Scouring Dynamics and Gravitational Wave Consequences: Constraints on Supermassive Black Hole Binary Hardening — 2601.07762
Stellar cores live long and prosper in cuspy dark matter halos — 2512.05719
Recoiling Black Hole Candidates from Spatially Offset Broad Emission Lines in MaNGA — 2512.00174
Accretion, Jets, and Recoil in Merging Supermassive Binary Black Holes — 2510.05883
Off-center black hole seed formation? Implications for high and low redshift massive black holes — 2509.12306
Understanding the Evolution of Black Hole Accretion and Dust out to z=4 with a Deep Imaging Extragalactic Survey with PRIMA — 2509.01674
Identifying massive black hole binaries via light curve variability in optical time-domain surveys — 2508.21510
A Large Systematic Search for Close Supermassive Binary and Rapidly Recoiling Black Holes -- IV. Ultraviolet spectroscopy — 2501.10574
Elliptical (E) and ellicular (ES) galaxies in the M_bh-M_*,sph diagram, and a merger-driven explanation for the origin of ES galaxies, anti-truncated stellar discs in lenticular galaxies, and the Sersicification of E galaxy light profiles — 2501.09953
HST Observations within the Sphere of Influence of the Powerful Supermassive Black Hole in PKS0745-191 — 2501.03339
Primordial Black Hole stellar microlensing constraints: understanding their dependence on the density and velocity distributions — 2501.02610
Probing the Merger Rates of Supermassive Black Holes and Galaxies with Gravitational Waves — 2501.02748
Two radio cores in GPS J1543-0757: a new dual supermassive black hole system? — 2408.06187
Can quasars, triggered by mergers, account for NANOGrav's stochastic gravitational wave background?
Is your stochastic signal really detectable? — 2412.10468
Beyond the Goldilocks Zone: Identifying Critical Features in Massive Black Hole Formation — 2412.08829
Massive black holes or stars first: the key is the residual cosmic electron fraction — 2412.02763
Wandering and escaping: recoiling massive black holes in cosmological simulations — 2412.02374
Large-scale dual AGN in large-scale cosmological hydrodynamical simulations — 2411.15297
Super-Size Me: The Big Multi-AGN Catalog (The Big MAC), Data Release 1: The Source Catalog — 2411.12799
A Recent Supermassive Black Hole Binary in the Galactic Center Unveiled by the Hypervelocity Stars — 2411.09278
Primordial black holes as supermassive black holes seeds — 2411.03448
Connecting Inflation to the NANOGrav 15-year Data Set via Massive Gravity — 2410.09658
Active Galactic Nuclei and Host Galaxies in COSMOS-Web. II. First Look at the Kpc-scale Dual and Offset AGN Population — 2405.14980
Signatures of Massive Black Hole Merger Host Galaxies from Cosmological Simulations II: Unique Stellar Kinematics in Integral Field Unit Spectroscopy — 2407.14061
The formation of supermassive black holes from Population III.1 seeds. III. Galaxy evolution and black hole growth from semi-analytic modelling — 2407.09949
PKS 2131-021 -- Discovery of Strong Coherent Sinusoidal Variations from Radio to Optical Frequencies: Compelling Evidence for a Blazar Supermassive Black Hole Binary — 2407.09647
Dynamics around supermassive black holes: Extreme mass-ratio inspirals as gravitational-wave sources — 2406.19443
Supermassive black hole mass measurement in the spiral galaxy NGC 4736 Using JWST/NIRSpec stellar kinematics — 2505.09941

The Host Galaxies of PTA Sources: Converting Supermassive BH Binary Parameters into EM Observables — 2505.11598
First Light And Reionization Epoch Simulations (FLARES) -- XIX: Supermassive black hole mergers in the early Universe and their environmental dependence — 2505.12591
Accretion onto supermassive black hole binaries — 2405.14843
Astrometric Jitter as a Detection Diagnostic for Recoiling and Slingshot Supermassive Black Hole Candidates — 2405.11026
Detection and Prediction of Future Massive Black Hole Mergers with Machine Learning and Truncated Waveforms — 2405.11340
How do Primordial Black Holes change the Halo Mass Function and Structure? — 2405.11381
Tip of the iceberg: overmassive black holes at 4<z<7 found by JWST are not inconsistent with the local MBH-M⋆ relation


https://arxiv.org/pdf/2103.16254.pdf
https://arxiv.org/pdf/2112.03576.pdf

NOTE as several triplet SMBHs have
NOTE been observed in the local Universe (Deane et al. 2014;
NOTE Pfeifle et al. 2019; Liu et al. 2019; Kollatschny et al.
NOTE 2020).

NOTE , shrink the orbits further (see
NOTE e.g. Amaro-Seoane et al. 2022, for a review).

The Redshift Difference in Gravitational Lensed Systems: A Novel Probe of Cosmology — 2308.07529
Evidence for a milli-parsec separation Supermassive Black Hole Binary with quasar microlensing
The Black Hole Mass Function Across Cosmic Times II. Heavy Seeds and (Super)Massive Black Holes — 2206.07357
Black Hole Mass Measurements of Early-Type Galaxies NGC 1380 and NGC 6861 Through ALMA and HST Observations and Gas-Dynamical Modeling — 2206.09043
A Bayesian Approach To The Halo-Galaxy-SMBH Connection Through Cosmic Time
Detection of an X-ray quasar in a gravitationally-lensed z=10.3 galaxy suggests that early supermassive black holes originate from heavy seeds
Mass-redshift dependency of Supermassive Black Hole Binaries for the Gravitational Wave Background — 2305.18293
SLICK: Strong Lensing Identification of Candidates Kindred in gravitational wave data — 2403.02994


## Galaxy Formation / Evolution
The heartbeat of stellar halos: Insights from the stellar halo mass-metallicity relation — 2512.07780
Mock Observations: Morphological Analysis of Galaxies in TNG100 Simulations — 2504.18042
The Outskirt Stellar Mass of Low-Redshift Massive Galaxies is an Excellent Halo Mass Proxy in Illustris/IllustrisTNG Simulations — 2412.03406
Tracing the origins of galaxy lopsidedness across cosmic time — 2411.19426
Photometric properties of classical bulge and pseudo-bulge galaxies at 0.5≤z<1.0
ALESS-JWST: Joint (sub-)kiloparsec JWST and ALMA imaging of z∼3 submillimeter galaxies reveals heavily obscured bulge formation events
Little Red Dots: Rapidly Growing Black Holes Reddened by Extended Dusty Flows — 2407.10760
Characterising Tidal Features Around Galaxies in Cosmological Simulations — 2404.12436
A forward-modelling approach to overcome PSF smearing and fit flexible models to the chemical structure of galaxies — 2403.08175
A two-phase model of galaxy formation: I. The growth of galaxies and supermassive black holes — 2311.05030
Galaxy quenching at the high redshift frontier: A fundamental test of cosmological models in the early universe with JWST-CEERS — 2311.02526
Field-level simulation-based inference with galaxy catalogs: the impact of systematic effects — 2310.15234
A JWST investigation into the bar fraction at redshifts 1 < z < 3 — 2309.10038
Identifying the disc, bulge, and intra-halo light of simulated galaxies through structural decomposition
Exploring the Angular Momentum - Atomic Gas Content Connection with EAGLE and IllustrisTNG — 2307.02722
Bulgeless disks, dark galaxies, inverted color gradients, and other expected phenomena at higher z. The chromatic surface brightness modulation (CMOD) effect — 2303.12845
Has JWST already falsified dark-matter-driven galaxy formation? — 2210.14915
A shot in the Dark (Ages): a faint galaxy at z=9.76 confirmed with JWST
CEERS Key Paper IV: The Diversity of Galaxy Structure and Morphology at z=3-9 with JWST
The MillenniumTNG Project: Many papers 2022
The MASSIVE Survey. XVIII. Deep Wide-Field K-band Photometry and Local Scaling Relations for Massive Early-Type Galaxies — 2210.08043
Sizes and mass profiles of candidate massive galaxies discovered by JWST at 7<z<9: evidence for very early formation of the central ∼100 pc of present-day ellipticals — 2305.17162

## Dark Matter
The AIDA-TNG project: 3D halo shapes — 2512.15856
The AIDA-TNG project: dark matter profiles and concentrations in alternative dark matter models — 2512.15869
Connection between galaxy morphology and dark-matter halo structure II: predicting disk structure from dark-matter halo properties — 2512.13822
Buried but not destroyed: the evolution from prompt cusps to NFW haloes — 2512.13804
Forecasting Dark Matter Subhalo Constraints from Stellar Streams using Implicit Likelihood Inference — 2512.07960
Probing the Nature of Dark Matter Self-Interactions Through Observations of Massive Black Hole Mergers — 2511.13220
Reaching for the Edge II: Stellar Halos out to Large Radii as a Tracer of Dark Matter Halo Mass — 2511.10723
Detecting dark matter sub-halos in the Galactic plane with the Cherenkov Telescope Array Observatory — 2501.09789
Implications of the intriguing constant inner mass surface density observed in dark matter halos — 2501.03761
Dwarf galaxies imply dark matter is heavier than 2.2×10−21eV
Effectiveness of halo and galaxy properties in reducing the scatter in the stellar-to-halo mass relation — 2405.15191
Hydrodynamical simulations of merging galaxy clusters: giant dark matter particle colliders, powered by gravity — 2405.00140
The Influence of Baryons on Low-mass Haloes — 2403.17044
Predicting the Scaling Relations between the Dark Matter Halo Mass and Observables from Generalised Profiles I: Kinematic Tracers — 2403.07352
Brightest Cluster Galaxy Offsets in Cold Dark Matter — 2402.00928
Micro galaxies as a falsifiable prediction of LCDM cosmology
No Catch-22 for Fuzzy Dark Matter: testing substructure counts and core sizes via high-resolution cosmological simulations — 2311.03591
Baryonic Imprints on DM Halos: the concentration-mass relation and its dependence on halo and galaxy properties — 2311.03491
Beyond Best-Fits and Model Selection -- Introducing "Reliability" of cusp-core inference of dark matter halos — 2310.20272
Can prompt cusps of WIMP dark matter be detected as individual gamma-ray sources? — 2310.15214
The formation of cores in galaxies across cosmic time -- the existence of cores is not in tension with the LCDM paradigm — 2310.13055
Till the core collapses: the evolution and properties of self-interacting dark matter subhalos — 2310.09910
The abundance of core--collapsed subhalos in SIDM: insights from structure formation in ΛCDM
Tracking the evolution of satellite galaxies: mass stripping and dark-matter deficient galaxies — 2212.12090
New Constraints on Warm Dark Matter from the Lyman-α Forest Power Spectrum — 2209.14220
Review of solutions to the Cusp-core problem of the ΛCDM Model
Matching the mass function of Milky Way satellites in competing dark matter model
The shape of dark matter haloes: results from weak lensing in the Ultraviolet Near-Infrared Optical Northern Survey (UNIONS) — 2209.09088
A lensing multi-messenger channel: Combining LIGO-Virgo-Kagra lensed gravitational-wave measurements with Euclid observations
Chandra Observations of Spikey: A Possible Self-lensing Supermassive Black Hole Binary System
The massive relic galaxy NGC 1277 is dark matter deficient. From dynamical models of integral-field stellar kinematics out to five effective radii — 2303.11360
The impact of baryonic potentials on the gravothermal evolution of self-interacting dark matter haloes — 2306.08028

## Stats
AstroAlertBench: Evaluating the Accuracy, Reasoning, and Honesty of Multimodal LLMs in Astronomical Classification — 2605.05573
ALABI: Active Learning for Accelerated Bayesian Inference — 2603.18259
Probabilistic Graphical Models in Astronomy — 2601.16959
How to embed any likelihood into SBI: Application to Planck + Stage IV galaxy surveys and Dynamical Dark Energy — 2507.22990
IRIS: A Bayesian Approach for Image Reconstruction in Radio Interferometry with expressive Score-Based priors — 2501.02473
SIDE-real: Truncated marginal neural ratio estimation for Supernova Ia Dust Extinction with real data
LtU-ILI: An All-in-One Framework for Implicit Inference in Astrophysics and Cosmology — 2402.05137
nbi: the Astronomer's Package for Neural Posterior Estimation
Bayesian Computation in Astronomy: Novel methods for parallel and gradient-free inference
Finding reproducible cluster partitions for the k-means algorithm
Scalable hierarchical BayeSN inference: Investigating dependence of SN Ia host galaxy dust properties on stellar mass and redshift

## SETI
Imagining the Alien: Human Projections and Cognitive Limitations
Results of ten years of UCLA SETI searches with the Green Bank Telescope
OmniCosmos: Transferring Particle Physics Knowledge Across the Cosmos
From Extraterrestrial Microbes to Alien Intelligence: Rebalancing Astronomical Research Priorities
Microlensing Signatures of Dyson Sphere-like Structures around Primordial Black Holes as Technosignatures of Extraterrestrial Advanced Civilizations

## Cancer
https://eur03.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.linkedin.com%2Fposts%2Fturbine-ai_network-driven-cancer-cell-avatars-for-combination-activity-7211408647778668547-nd7n%3Futm_source%3Dshare%26utm_medium%3Dmember_desktop&data=05%7C02%7CJames.Nightingale%40newcastle.ac.uk%7Cb88055fe74cc48f5d2e708dc9a85e8e8%7C9c5012c9b61644c2a91766814fbe3e87%7C1%7C0%7C638555147133736023%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=WefLDikVOdmU5gFIaZTXyRjF5fyvksFjdZ6hpJl9lHc%3D&reserved=0

https://eur03.safelinks.protection.outlook.com/?url=https%3A%2F%2Fjournals.plos.org%2Fploscompbiol%2Farticle%3Fid%3D10.1371%2Fjournal.pcbi.1005268&data=05%7C02%7CJames.Nightingale%40newcastle.ac.uk%7Cb88055fe74cc48f5d2e708dc9a85e8e8%7C9c5012c9b61644c2a91766814fbe3e87%7C1%7C0%7C638555147133749366%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=RaOdWGBY8mRAssK2Haar9r6dK8lGQfp3ZWU%2Fz1uzFpI%3D&reserved=0








NOTE postprocessing (Kelley et al. 2017a;
NOTE Katz et al. 2020; Volonteri et al. 2020) find that many
NOTE binaries stall and fail to merge within a Hubble time.
NOTE For example, the fiducial model in Kelley et al. (2017a)
NOTE sees a peak of MBHB lifetimes at a median value is 29
NOTE Gyr, with only ∼ 7 % binaries have lifetime less than 1
NOTE Gyr.

__SMBH__

Massive black holes in galactic nuclei: Theory and Simulations
 
    Cant remember

Massive Black Holes summary — https://arxiv.org/pdf/2304.10233.pdf

    Thorough summary of black hole binarys

__SMBH Binaries__

Hierarchical Bayesian inference on an analytical model of the LISA massive black hole binary population

    Incredible Bayes Model of SMBH mergers for GW astronomy, INCLUING MERGER TIME DELAYS

Dual AGNs: Precursors of Binary Supermassive Black Hole Formation and Mergers:

    Shows rates of SMBHs around AGNs, implies that galaxies should have many 10^8MSun SMBHs wandering around.

Active Galactic Nuclei and Host Galaxies in COSMOS-Web. II. First Look at the Kpc-scale Dual and  Offset AGN Population — 2405.14980

    High rate of dual AGN in redshift 1-3 galaxies, now possible due to JWST.

Einstein vs Hawking: Black hole binaries and cosmological expansion:

    Cant remember

Observational Signatures of Supermassive Black Hole Binaries

    CONTAINS SMBHB EVOLUTION EQUATIONS

    https://arxiv.org/pdf/2310.16896.pdf

RABBITS Simulations which show that SMBH binaries are driven to coalescence by central nuclear star formation

    https://arxiv.org/abs/2311.01499
    https://arxiv.org/abs/2311.01493

Compact object mergers: Observations of supermassive binary black holes and stellar tidal disruption events

    Run through of observational signatures of SMBHBs, most of which are x-ray or AGN based.

The NANOGrav 15-year Data Set: Constraints on Supermassive Black Hole Binaries from the Gravitational Wave Background

    The link between gravitational wave background and > 10^7MSun SMBHB's.

Premature supermassive black hole mergers in cosmological simulations of structure formation

    Brilliant example of how numerical effects in simulations can lead to delays on SMBH mergers which impact SWGB PTA results.

## KetJU
https://arxiv.org/pdf/2211.11788.pdf

Big Galaxies and Big Black Holes: The Massive Ends of the Local Stellar and Black Hole Mass Functions and the Implications for Nanohertz Gravitational Waves

    Examples of how to make and plot SMBH mass functions and relating them to GWB.


Varstrometry for Off-nucleus and Dual sub-Kpc AGN (VODKA): A Mix of Singles, Lenses, and True Duals at Cosmic Noon

    Good overview of dual AGN and looking for them

Identifying supermassive black hole recoil in elliptical galaxies

    All the stuff SMBH binary recoils do to the Sersic core and galaxy around them.


__SMBH Scouring__

The supermassive black hole merger driven evolution of high-redshift red nuggets into present-day cored early-type galaxies

    Great KetJU simulation study of how scouring SMBHs can create cored galaxies and impact the galaxies around them.

__Analysis__

Characterization of JWST NIRCam PSFs and Implications for AGN+Host Image Decomposition: — 2304.13776

    Detailed discussion of the JWST PSF and how to model it, reference for PyAutoGalaxy.


__Dark Matter__

THESAN-HR: Galaxies in the Epoch of Reionization in warm dark matter, fuzzy dark matter and interacting dark matter: — 2304.06742

    Good description of how alternative DM models (Warm, Fuzzy, Interacting) impact high-z galaxy formation / reionization.


The shape of dark matter halos: a new fundamental cosmological invariance — 2406.15947

    Could be a Cosmology motivation for COMSOSO SL+WL study


__Galaxies__

Stellar feedback-regulated black hole growth: driving factors from nuclear to halo scales — 2210.09320

    Description of how a mass threshold surpresses stellar feedback to make BH's efficient and quency galaxie,s similar to Bower 2017



__Software__

Setting SAIL: Leveraging Scientist-AI-Loops for Rigorous Visualization Tools — 2603.18145

https://github.com/patrick-kidger/optimistix?tab=readme-ov-file: 
    
    LOADS of JAX githubs including lineaer solvers, BlackJAX
   
Eryn: A multi-purpose sampler for Bayesian inference: https://arxiv.org/list/astro-ph/new

    Another cool sampler for autofit.





