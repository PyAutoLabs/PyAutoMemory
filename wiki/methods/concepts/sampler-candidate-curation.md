---
title: Sampler candidate curation
type: concept
topics: [samplers, literature, inference]
sources:
  - Speagle 2020 — dynesty
  - Lange 2023 — Nautilus
  - Cabezas et al. 2024 — BlackJAX
  - Buchner 2021 — UltraNest
  - Karamanis et al. 2022 — pocoMC
status: drafted
---

# Sampler candidate curation

## TL;DR

A sampler paper establishes a method and reported experiments, not its suitability
for an untested likelihood. Keep a bounded shortlist with public paper/code
provenance, explicit requirements, a dated integration check and unanswered
benchmark questions. Curate on demand; literature ingestion never submits compute.

## What it is

A candidate is a hypothesis for investigation. This initial selection spans
existing evidence baselines, gradient posterior sampling and two alternative
evidence approaches. It is deliberately non-exhaustive and carries no ranking.

## Why it matters

Posterior sampling, evidence estimation and optimization answer different
questions. Compare only methods that deliver the required output. A library
wrapper, an installed optional dependency and demonstrated scientific performance
are three distinct facts.

## Key results from the literature

- dynesty offers static/dynamic evidence and posterior estimation, making it an
  allocation baseline ([[sources-samplers#dynesty]]).
- Nautilus learns proposals for importance nested sampling; published advantages
  motivate a test, with unseen-mode coverage still a benchmark question
  ([[sources-samplers#nautilus-2023]]).
- BlackJAX supplies composable JAX inference; NUTS adapts gradient trajectories.
  Gradient compatibility, initialization and chain diagnostics must be checked
  ([[sources-samplers#blackjax-nuts-2024]],
  [[sources-samplers#hoffman-and-gelman-2011-nuts]]).
- UltraNest prioritizes reliable inference for challenging shapes. Repeated-seed
  evidence checks would test that promise locally
  ([[sources-samplers#ultranest-2021]]).
- pocoMC uses flow preconditioning; correlated and multimodal targets motivate
  investigating population coverage and training cost
  ([[sources-samplers#pocomc-2022]]).

The coverage checks and benchmark design above are investigation proposals,
not claims that these papers prove PyAutoFit correctness or speed.

## Dated integration check

On 2026-10-08, PyAutoFit revision
`8bb5f6e8fab809d47f785e9f2ac8289b3e3c9e3e` exported `DynestyStatic`,
`DynestyDynamic`, `Nautilus` and `BlackJAXNUTS` from `autofit/__init__.py`.
The search tree contained no UltraNest or pocoMC wrapper. This was a read-only
source inspection, not an import, install, run or completeness guarantee.
Benchmark status for this shortlist is **not assessed**; consult actual project
evidence separately rather than interpreting this status as “never run.”

## On-demand Memory to Insight handoff

1. For missed literature, reuse Memory's existing harvest:
   `python scripts/catch_up.py --scope interests --topic Stats --since YYYY-MM-DD --json`.
   Retain its source counts, cutoff, dropped-in-memory count and warnings,
   including truncated or unavailable arXiv coverage. Harvest is optional;
   a requested named paper can go directly to verification. This bounded
   initial survey verified named records directly and did not run a gap-fill.
2. Follow the existing catch-up tier curation and human filing confirmation
   when invoking that workflow. Verify the primary record and official code;
   deduplicate by DOI/arXiv identity, file compact claim support and canonical
   bibliography metadata, then run `make validate`.
3. Prepare an independent public-source-derived candidate JSON for Insight.
   Each record has `id`, `name`, `family`, `paper_url`, `code_url`,
   `expected_uses`, `limitations`, `integration_status`, `benchmark_status`,
   `reviewed_at` and `investigation_prompt`. Use stable kebab-case identifiers,
   HTTPS provenance, string-array uses/limitations and an ISO review date.
   Investigation prompts request a bounded comparison with output accuracy,
   repeated seeds, configuration/version capture and total cost including
   compilation or training. They are proposals, not executable orders.
4. Insight owns review/publication of its independent candidate list. Export
   no Memory wiki excerpts, private references, archival filenames or local
   paths. The public paper and official code must support the published text
   without Memory access. Literature records do not set integration or science
   acceptance; recheck the actual PyAutoFit roster when refreshing them.

No autonomous scan or schedule is introduced. Any benchmark launch requires the
separate campaign workflow and its authorization.

## See also

- [[nested-sampling]]
- [[hamiltonian-monte-carlo]]
- [[sampler-benchmarks]]
- [Existing catch-up procedure](../../../skills/catch_up/catch_up.md)
