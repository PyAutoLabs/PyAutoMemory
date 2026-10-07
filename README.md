<p align="center">
  <img src="logo.png" alt="PyAutoMemory" width="400">
</p>

# PyAutoMemory

[![PyAutoScientist GitHub](https://img.shields.io/badge/%F0%9F%A7%AE%20PyAutoScientist-GitHub-181717?style=flat-square)](https://github.com/PyAutoLabs/PyAutoScientist) [![PyAutoScientist ReadTheDocs](https://img.shields.io/badge/%F0%9F%93%96%20PyAutoScientist-ReadTheDocs-8CA1AF?style=flat-square)](https://pyautoscientist.readthedocs.io)

[![knowledge](https://img.shields.io/endpoint?url=https://pyautolabs.github.io/PyAutoMemory/badge.json)](https://pyautolabs.github.io/PyAutoMemory/)

**PyAutoMemory is the Memory of the PyAutoScientist** — the long-term memory
of the organism: what it has learned, distilled into cross-linked LLM wikis —
literature summaries, scientific concepts, and the citation metadata to
verify them. Memory holds *what the science says*; what the organism *did*
lives in the Mind. Source PDFs live off-repo; what's here is the durable
knowledge. Start at [`index.md`](index.md).

See the **[PyAutoMemory Dashboard](https://pyautolabs.github.io/PyAutoMemory/)**
for managing all of it from one page: the reading
queue, the paper sections still needing a canonical citation key, and each
sub-wiki's maturity — every work queue carrying a one-tap 📋 button that
copies a paste-ready AI assistant prompt (file the next paper, resolve keys,
upgrade a stub, or `Use the memory skill. <domain>` to recall what's known). Every queued
paper links to its arXiv abstract page and carries a 📄 button onto the PDF
itself, so a phone can collect a stack of papers to read offline in one tap
each.

**One-tap mode.** Out of the box each action button opens a prefilled GitHub
issue you then submit. Tap the 🔑 chip under the header once and paste a
fine-grained token (Resource owner PyAutoLabs, repository PyAutoMemory only,
*Issues: read and write*): from then on every button files that same issue
from the page, the row disappears at once, and 📥/📑 ask for your notes in an
inline box first. The token lives in that browser's local storage and nowhere
else; tap the chip again to sign out. The workflows behind the buttons see
exactly the issue the link would have opened.

The per-paper buttons file GitHub issues that two workflows act on:
`queue_actions.yml` makes the mechanical moves (➕ ✅ ✖️ 🧹) and closes the
issue; `queue_filing.yml` has Claude file a 📥/📑 paper onto a
`queue-filing/issue-<n>` branch, gated, for a human to merge — and it opens
that PR itself when a `QUEUE_PR_TOKEN` repo secret (a fine-grained PAT with
pull-requests write on this repo) exists, or when *Allow GitHub Actions to
create and approve pull requests* is on (Settings → Actions → General). A tap
whose label the issue
form dropped is read from its title; whatever nothing acted on is
re-dispatched by the nightly `queue_sweep.yml`; and a filing that reached its
branch but not `main` sits at the top of the board under **Filings awaiting
merge** until its PR lands — the paper is not in memory before then.

## Current contents

<!-- The line below is auto-updated by .github/workflows/knowledge_board.yml (everything -->
<!-- between the memory:begin/memory:end markers is replaced with the rendered strip). -->
<!-- memory:begin -->
🧠 **166 pages** · 69 drafted · 40% of 651 paper sections cite a resolved key · 228 papers queued · [dashboard →](https://pyautolabs.github.io/PyAutoMemory/)
<!-- memory:end -->

## The sub-wikis

Self-contained, shared schema:

| Wiki | Covers |
|------|--------|
| [`wiki/lensing/`](wiki/lensing/index.md) | strong gravitational lensing (the primary wiki) |
| [`wiki/smbh/`](wiki/smbh/index.md) | supermassive black holes, binaries, recoil, GW background |
| [`wiki/cti/`](wiki/cti/index.md) | charge transfer inefficiency, Euclid VIS calibration |
| [`wiki/methods/`](wiki/methods/index.md) | Bayesian inference, samplers, deep learning, simulations |
| [`wiki/galaxies/`](wiki/galaxies/index.md) | galaxy formation and evolution |

[`bibliography/`](bibliography/README.md) holds the canonical BibTeX
metadata every wiki cites against; [`reading-queue.md`](reading-queue.md)
is what's waiting to be read and filed. Two overnight tiers sit in front of it:
[`arxiv-inbox.md`](arxiv-inbox.md) (strong lensing, a seven-day timer) and
[`arxiv-interests.md`](arxiv-interests.md) (everything else — black holes,
dark matter, galaxy formation, statistics — as one day's ten at a time, a
backlog you clear a day at a time rather than a timer). New knowledge updates
the metadata
and the claim support together, then passes `make validate` (CI-enforced on
every push).

Away for a while? [`/catch_up`](skills/catch_up/catch_up.md) collects every
paper missed since memory last ingested one — lapsed suggestions from git
history, the open queue, and an arXiv gap-fill over days the digest never ran
(`scripts/catch_up.py`) — for one triage and one filing PR. The dashboard
shows a strong-lensing catch-up banner after seven days without recorded lensing
paper activity. Recent activity in other topics does not reset that clock.

The same `lensing_catch_up` record backs the banner and cockpit feed: canonical
state, cutoff date, age, seven-day threshold/deadline, observation time, evidence
links and explicit action descriptors. Healthy work adds no attention row;
missing, invalid or future dates are unknown. `last_ingestion` identifies the
verified bib-plus-sources commit, while `last_completed` is a queue DONE date
(which may mean read-without-filing); `last_activity` is the existing catch-up
cutoff, the later of those dates. Legacy all-scope fields remain available.

The cockpit copies an instruction to read `skills/catch_up/SKILL.md` and use
the catch_up skill with `lensing`, and links to its procedure. Its safety is `scientific_judgement`: candidate selection and filing
retain the procedure's human review. Observing staleness executes nothing, and
no scientific choice is fabricated before candidates are harvested.

The feed also exposes independent `digests.lensing` and `digests.interests`
records, shared with the board freshness indicators. Each records its canonical
state, last recorded date, checked time, elapsed weekdays, two-weekday threshold,
reason and evidence/action links. Empty queues with a recent stamp stay healthy;
missing, invalid or future stamps are unknown. The stamp proves a digest was
recorded, not that every workflow step succeeded. Stale/unknown cockpit rows
link to the owning Mind workflow and offer a manual investigation prompt
(`requires_approval`); detection never reruns a workflow. Digest delivery and
human lensing catch-up remain separate clocks.

The wiki schema is defined in
[`wiki/AGENTS.md`](wiki/AGENTS.md) and inherited by every
sub-wiki. How agents should read this repo: [AGENTS.md](AGENTS.md). The
organism this repo is the Memory of:
[PyAutoBrain/ORGANISM.md](https://github.com/PyAutoLabs/PyAutoBrain/blob/main/ORGANISM.md),
documented in full at <https://pyautoscientist.readthedocs.io>.

Licence: structure and tooling MIT; wiki content CC BY 4.0 — see
[LICENSE](LICENSE).
