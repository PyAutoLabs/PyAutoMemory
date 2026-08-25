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
copies a paste-ready Claude prompt (file the next paper, resolve keys,
upgrade a stub, or `/memory <domain>` to recall what's known). Every queued
paper links to its arXiv abstract page and carries a 📄 button onto the PDF
itself, so a phone can collect a stack of papers to read offline in one tap
each.

## Current contents

<!-- The line below is auto-updated by .github/workflows/knowledge_board.yml (everything -->
<!-- between the memory:begin/memory:end markers is replaced with the rendered strip). -->
<!-- memory:begin -->
🧠 **166 pages** · 69 drafted · 40% of 645 paper sections cite a resolved key · 208 papers queued · [dashboard →](https://pyautolabs.github.io/PyAutoMemory/)
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
is what's waiting to be read and filed, and
[`arxiv-inbox.md`](arxiv-inbox.md) is the overnight suggestions tier in front
of it. New knowledge updates the metadata
and the claim support together, then passes `make validate` (CI-enforced on
every push).

The wiki schema is defined in
[`wiki/CLAUDE.md`](wiki/CLAUDE.md) and inherited by every
sub-wiki. How agents should read this repo: [AGENTS.md](AGENTS.md). The
organism this repo is the Memory of:
[PyAutoBrain/ORGANISM.md](https://github.com/PyAutoLabs/PyAutoBrain/blob/main/ORGANISM.md),
documented in full at <https://pyautoscientist.readthedocs.io>.

Licence: structure and tooling MIT; wiki content CC BY 4.0 — see
[LICENSE](LICENSE).
