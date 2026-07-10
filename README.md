# PyAutoMemory

The long-term memory of the PyAuto organism: what it has learned, distilled
into cross-linked LLM wikis — literature summaries, scientific concepts, and
the citation metadata to verify them. When the plain-English task you lead
needs domain grounding, this is where the agents look. Source PDFs live
off-repo; what's here is the durable knowledge. Start at
[`index.md`](index.md).

The sub-wikis (self-contained, shared schema):

| Wiki | Covers |
|------|--------|
| [`lensing_wiki/`](lensing_wiki/index.md) | strong gravitational lensing (the primary wiki) |
| [`smbh_wiki/`](smbh_wiki/index.md) | supermassive black holes, binaries, recoil, GW background |
| [`cti_wiki/`](cti_wiki/index.md) | charge transfer inefficiency, Euclid VIS calibration |
| [`methods_wiki/`](methods_wiki/index.md) | Bayesian inference, samplers, deep learning, simulations |
| [`galaxies_wiki/`](galaxies_wiki/index.md) | galaxy formation and evolution |

[`bibliography/`](bibliography/README.md) holds the canonical BibTeX
metadata every wiki cites against; [`reading-queue.md`](reading-queue.md)
is what's waiting to be read and filed. New knowledge updates the metadata
and the claim support together, then passes
`make validate-literature-citations`.

The wiki schema is defined in
[`lensing_wiki/CLAUDE.md`](lensing_wiki/CLAUDE.md) and inherited by every
sub-wiki. How agents should read this repo: [AGENTS.md](AGENTS.md). The
organism this repo is the Memory of:
[PyAutoBrain/ORGANISM.md](https://github.com/PyAutoLabs/PyAutoBrain/blob/main/ORGANISM.md),
documented in full at <https://pyautoscientist.readthedocs.io>.

Licence: structure and tooling MIT; wiki content CC BY 4.0 — see
[LICENSE](LICENSE).
