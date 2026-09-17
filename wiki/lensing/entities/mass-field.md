---
title: MassField
type: entity
topics: [software, environment, systematics]
sources:
  - Galan et al. 2023 — COOLEST standard
status: drafted
---

# MassField

## What it is

A **mass field** is a redshift plus a bag of mass profiles that describe the
tidal field of everything *outside* the modelled system — an external shear
γ_ext, a mass sheet κ_ext, an external potential — as a model object that is
a **peer of a galaxy, not a property of one**. It exists because the physics
of [[external-convergence-shear]] says nothing about any deflector: the
constant shear and convergence come from the line-of-sight environment, so
attaching them to `lens_0` misdescribes the model the moment there is more
than one deflector.

Two implementations share the name:

- **COOLEST** (`Galan2023`, the code-independent lens-model exchange
  standard written by the [[herculens]] group) has a `MassField` entity
  alongside its `Galaxy` entity; both carry a redshift, and external shear
  and convergence sheets live only on the former. lenstronomy goes further
  and has no galaxy concept at all — a flat list of mass components, each
  with its own redshift ([[lenstronomy]]).
- **PyAutoLens / PyAutoGalaxy** adopt COOLEST's middle ground:
  `MassField(redshift, **mass_profiles)` is a standalone class (not a
  `Galaxy` subclass) holding any mass profile — `ExternalShear`, `MassSheet`
  and `ExternalPotential` are the intended ones. It has its own slot in the
  model, `fields=`, and its own argument on the tracer,
  `Tracer(galaxies=..., fields=...)`. Only the tracer's *planes* merge
  galaxies and fields at each redshift; `tracer.galaxies` never contains a
  field, so per-galaxy surfaces (image dictionaries, plotters, result
  tables) never see one. The COOLEST interop is 1:1 in both directions.

## Key facts

- **One field per redshift, several fields for several planes.** Shear +
  sheet + potential at one redshift is one `MassField`, as bulge + disk is
  one `Galaxy`. Several fields means several planes — the per-plane mass
  sheets of a line-of-sight halo sampler, or foreground and background
  tidal planes in a [[line-of-sight-effects|LOS shear]] formalism — which is
  why the model slot is a collection and not a single `field=`.
- **The galaxy-attached form stays supported.** A `Galaxy` carrying a shear
  or sheet keeps working, unwarned, and keeps the same PyAutoFit result
  identifier; single-deflector `imaging/` scripts keep it, because there
  nothing is misrepresented. A model that adopts `fields=` is a different
  model and gets a new identifier.
- **External potential centre.** `ExternalPotential` has a `centre` (its
  τ/δ terms have radial dependence about it); composed in a `MassField` its
  centre prior is tied to the primary galaxy's mass centre by a
  `model_util` helper, which is the convention for where an external
  potential is centred.
- **Where it matters.** Multi-deflector fits (`multi_galaxy/`, `group/`),
  where the older idiom was a shear-only `Galaxy` named `shear_galaxy`;
  [[cluster-lensing|cluster]] models; multi-plane LOS sheets. A
  [[mass-sheet-degeneracy|mass sheet]] is a field for the same reason κ_ext
  is not a galaxy parameter.
- **Rejected designs**, so nobody re-derives them: a `Galaxy` subclass in
  the `galaxies` collection (keeps the false is-a relation and the
  positional-index hazard); a bare profile at the model root (no redshift
  for multi-plane tracing); a single `field=` slot (a second spelling would
  be needed for two-plane LOS shear).

The delivery status of the PyAutoLens integration is operational history and
lives in PyAutoMind (epic `mass-field`, ledger
`draft/feature/autogalaxy/mass_field_epic.md`), not here.

## Papers

- **`Galan2023`** — *COOLEST: COde-independent Organized LEns STandard*
  (JOSS 8, 5567): the standard whose `MassField` entity the PyAutoLens
  class mirrors. See [[herculens]].

## See also

- [[external-convergence-shear]]
- [[line-of-sight-effects]]
- [[mass-sheet-degeneracy]]
- [[shear-ellipticity-degeneracy]]
- [[pyautolens]]
- [[herculens]]
- [[lenstronomy]]
- [[sources-external-shear-los]]
