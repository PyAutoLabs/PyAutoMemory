# PyAutoLens AI Assistant — Strong Lensing Wiki

This wiki gives a PyAutoLens AI assistant broad scientific context for strong
gravitational lensing. It follows Karpathy's "LLM Wiki" pattern: concise,
cross-linked pages are read at query time, while canonical citation metadata
lives separately in `../bibliography/`.

## Layout

```
PyAutoMemory/                  # repo root
├── lensing_wiki/             # this folder — the compiled wiki (in git)
│   ├── CLAUDE.md             # this file — schema + usage rules
│   ├── index.md              # top-level navigation
│   ├── log.md                # append-only compilation log
│   ├── concepts/             # one topic per page — the science
│   ├── entities/             # specific surveys, lenses, collaborations, software
│   └── sources/              # compact claim support (one paper = one section)
└── bibliography/             # canonical BibTeX, aliases, citation instructions
```

Papers are the ground truth; wiki pages are syntheses. If they disagree, update
the wiki and note the change in `log.md`.

## References and citation metadata

- `sources/*.md` records compact guidance about what claims a paper supports.
- `../bibliography/pyautomemory.bib` records canonical metadata and keys.
- `../bibliography/bibkey_aliases.yaml` maps known alternate keys to canonical keys.

Never record local PDF paths or fabricate metadata. A canonical key is local to
PyAutoMemory: resolve it against a target project's `.bib` before patching LaTeX.
See [`../bibliography/README.md`](../bibliography/README.md) for the workflow.

## Page types

| Type        | Folder       | Scope                                                 |
|-------------|--------------|-------------------------------------------------------|
| Concept     | `concepts/`  | One scientific concept (e.g. mass-sheet degeneracy)   |
| Entity      | `entities/`  | One named thing (survey, lens, code, collaboration)   |
| Sources     | `sources/`   | Claim support for one topic, one section per paper    |
| Index/log   | root         | Navigation and provenance                             |

## Naming

- File names are lowercase kebab-case: `mass-sheet-degeneracy.md`,
  `slacs.md`, `time-delay-cosmography.md`.
- One concept per concept page. If a page tries to cover two ideas, split it.
- Source-collection pages are named by topic: `sources/dark-matter-substructure.md`.

## Cross-references

Use `[[page-slug]]` for wiki-internal links — for example
`[[mass-sheet-degeneracy]]` or `[[slacs]]`. Slugs match the filename without
`.md`. A `[[link]]` that has no target file yet is fine — it marks a future
page to write.

External references use verified DOI, arXiv, journal, or author/year/title
metadata, never a local path.

## Frontmatter

Every wiki file starts with YAML frontmatter:

```yaml
---
title: Mass-sheet degeneracy
type: concept            # concept | entity | sources | meta
topics: [degeneracies, cosmography]
sources:                 # optional — papers most relevant to this page
  - Suyu et al. 2017 — H0LiCOW overview
  - Birrer et al. 2020 — TDCOSMO IV
status: stub             # stub | drafted | reviewed
---
```

Sources may be `[]` for pages that synthesize general field knowledge.

## Concept page structure

```
# Title

## TL;DR
One paragraph an assistant can quote back to a user.

## What it is
The physics / definition.

## Why it matters for PyAutoLens
How this concept shows up in lens-modeling decisions a PyAutoLens user makes.

## Key results from the literature
Bullet list. Each bullet ends with `([[author-year-stub]])` so the LLM can
follow the link to the per-paper section.

## See also
- [[related-concept-1]]
- [[related-concept-2]]
```

## Entity page structure

Same idea but the headings are "What it is / Key facts / Papers / See also".
Use entity pages for: surveys (SLACS, BELLS, H0liCOW), specific lenses
(Abell 1201, the Cosmic Horseshoe), software (PyAutoLens, lenstronomy),
collaborations (TDCOSMO, Space Warps).

## Source-collection page structure

```
# Sources: <topic>

Papers covering this topic. Each paper has its own H2 section; cross-link with
`[[sources-<topic>#author-year-slug]]`.

## Author Year — short tag

**Canonical BibTeX key:** `KeyYYYY`
**Reference:** DOI/arXiv/journal reference if known
**Concepts:** [[concept-1]], [[concept-2]]

**Supports:**
- Claim this paper directly supports.
- Another claim this paper directly supports.

**Use when:**
- Situation where the citation is appropriate.

**Do not use for:**
- Similar but unsupported claim.
```

Keep entries short: normally 2–5 support bullets and no long prose. Do not copy
abstracts or infer claims from filenames. Add a TODO when support is unverified.

## How the assistant should use this wiki

1. On a user question, first open `index.md`.
2. Follow the relevant `concepts/` or `entities/` page.
3. Follow the source entry for claim scope and its canonical key for metadata.
4. Resolve that key against downstream `.bib` files before changing LaTeX.
5. If support or metadata is unclear, read the public paper and add a TODO
   rather than guessing. Log verified upgrades.

## Scope

In-scope folders for the current wiki build:

- `Strong_Lens/`           — primary
- `Substructure/`
- `StrongLensCluster/`
- `Dark_Matter_Detection/`
- `DarkMatterModels/`

Other folders (`WeakLensing/`, `Ellipticals/`, `Deep Learning/`, etc.)
contain papers that touch lensing tangentially but are out of scope until
explicitly added — see `log.md` for the decision.

This is the **lensing** sub-wiki. Sibling domain wikis inherit this schema.
