---
title: Aggregator performance (result loading at catalogue scale)
type: concept
topics: [software, aggregator, performance, profiling, sqlite, database, io, pyautofit]
sources:
  - PyAutoFit issues #1375, #1377, #1385; PyAutoConf #129; autolens_workspace_test #171
  - Merged PRs: PyAutoFit #1376/#1380/#1384/#1386, PyAutoConf #130, autofit_workspace_test #48/#49/#50/#51, autolens_workspace_test #172
  - Harnesses: autofit_workspace_test scripts/profiling/aggregator/ + autolens_workspace_test scripts/profiling/aggregator/
  - Raw grids: <workspace>/output/profiling_aggregator/results/*.json (local, 2026-07-16/17)
status: draft
last_updated: 2026-07-17
---

# Aggregator performance (result loading at catalogue scale)

## TL;DR

A 2026-07-16/17 campaign (PyAutoFit #1375 arc, 10 PRs) profiled every way PyAutoFit
loads modelling results at Euclid catalogue scale (3000+ lenses) using mock result
trees fabricated in seconds via `PYAUTO_TEST_MODE_SAMPLES` bypass fits — no sampler
ever runs. Central results:

> **The scaling axis is samples-per-result, not number of results.** The directory
> scan costs ~0.2 ms/result even at 3000 results; the full `samples.csv` parse
> dominates everything. After the fixes, per-result costs: summaries ~6.5 ms,
> model ~4.6 ms, full samples ~45 ms @1k rows (−45% at 10k rows).
> **Every workflow stage is floor-bounded by JSON→object deserialization
> (`from_dict`), not by lens math or file scanning.**

Three latent **crash-level bugs** were found by profiling realistic data, all fixed:
`from_dict` silently dropped dict entries whose value is exactly `0.0`;
`AggregateFITS` leaked one file handle per HDU per result (hard crash ~500 results);
database aggregator slicing was inverted (`agg[:5]` returned `len−5` fits).

## What was measured (per-result, mock results)

| pathway | before | after | change |
|---|---|---|---|
| `values("samples")` @10k rows | 611 ms | 334 ms | −45% (csv headers parsed once, not per row) |
| `values("samples")` @1k rows × 1000 results | 68 ms | 45 ms | −34% |
| `values("model")` | 8.2 ms | 4.6 ms | −44% (prior-config lookup caching, Conf#130) |
| `values("samples_summary")` | 8.7 ms | 6.6 ms | −25% |
| `AggregateCSV` (csv_make) @15-param models | 110 ms | 83 ms | −25% (row caching + double-eval fix) |
| `AggregateFITS` (fits_make) @2 HDUs | 5.6 ms | 4.5 ms | −19% + fd leak fixed |
| `AggregateImages` (png_make) | ~1.5 ms | — | profiled clean, no change |
| `Aggregator.from_directory` scan | ~0.2 ms | ~0.2 ms | zips no longer re-extracted on repeat opens |

Lens-level (`TracerAgg`/`FitImagingAgg`, autolens_workspace_test#172): reconstruction
adds only ~20–60% over the raw summary load at 7×7 fixture scale — deserialization
dominates, not lens computation.

## The sqlite verdict (revised at representative scale)

- Small/simple mock data said sqlite reads were 2–10× slower than the directory
  Aggregator. **At representative scale** (10k samples × 18-param model, the
  ~9 MB SLaM parity target) **the full-samples read is comparable** (150 vs
  165 ms/result). Small-data benchmarks mislead here — always measure at
  production shape.
- What stands against sqlite: build cost ~0.35 s/result up front (~17.5 min + ~5 GB
  at 3000 lenses), dominated by loading every result's samples into the ORM.
- What stands for it: single-file storage (HPC inode limits) and fast indexed
  queries (~1–6 ms) once built.
- The direct-write (session) path is **not** broken as suspected — its real gap was
  `samples_summary` never being stored (`DatabasePaths` no-op, fixed in #1380);
  minimised samples (~1 row) are by design (`save_all_samples=False`).

## Memory scaling limit (open)

`values("samples")` across 3000 × 1k-sample results OOMs (~6.6 GB RSS): every
`SearchOutput` caches its `Samples`, so even generator-style iteration accumulates.
Workaround: process in slices. Candidate fix (not taken): opt-out/weak cache for
bulk iteration.

## Bugs found by profiling realistic data (all fixed)

1. **`from_dict` dropped 0.0-valued dict entries** (Fit#1384): the `type=="dict"`
   branch filtered `if value`. Exposed by bypass output writing exact prior medians
   — lens centres/ell_comps are zero-median, so summaries lost 8/15 parameters and
   `TracerAgg` crashed. Pre-existing; affected any stored dict with legit zeros.
2. **`AggregateFITS` fd leak** (Fit#1386): one `fits.open` per requested HDU per
   result, handles kept alive by returned memmaps — "Too many open files" at ~500
   results (default ulimit 1024); a 3000-lens fits_make run would have died.
3. **Database aggregator slicing inverted** (Fit#1380): `agg[:5]` on 26 fits
   returned 21 (`len − stop` instead of `stop − start`); the old unit test passed
   only by a 2-fit coincidence where `len − stop == stop`.
4. **`JSONPriorConfig` re-sorted the whole flattened config on every lookup**
   (Conf#130) and linear-scanned identical repeated queries — 77% of the model
   deserialization floor was default-prior construction that `from_dict` then
   overwrote.

## Durable methodology lessons

- **Mock the outputs, never run the sampler**: one template result written through
  the real library write path (`PYAUTO_TEST_MODE=2/3` + `PYAUTO_TEST_MODE_SAMPLES=N`
  bypass fit), stamped N times with per-copy `unique_tag`/`dataset_name` — thousands
  of results in seconds, formats can never drift. The database keys fits by the
  (search, model, unique_tag) identifier hash: identical copies collapse to one row.
- **Time each stage on a fresh Aggregator**: `SearchOutput` caches model/samples/
  summaries per instance, so stage order otherwise contaminates the numbers.
- **Benchmark grids need an idle machine**: a concurrent pytest run inverted a
  before/after signal once. Under unavoidable load, use interleaved in-process A/B
  of old-vs-new implementations instead of cross-run comparison.
- **Background `cmd | tail` pipelines mask OOM kills** (pipeline exit code is
  tail's 0) — check `dmesg` for "Out of memory".
- **`open_database` silently prepends `conf.instance.output_path`** (plus the
  test-mode segment) to relative sqlite paths — a decoy empty file appears at the
  literal path; use absolute paths in tooling.

## Where the remaining time goes (deliberately not pursued)

After all fixes the floor is ~4.6 ms/result for a model load: sample-json
`from_dict` recursion and prior-object construction itself. No repeated-waste
pattern remains — further gains would need a redesign (e.g. schema-aware
deserialization or model memoization across identical `model.json` files), judged
diminishing returns as of 2026-07-17.
