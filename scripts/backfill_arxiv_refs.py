#!/usr/bin/env python3
"""scripts/backfill_arxiv_refs.py — give every queue line its arXiv ref.

The Dashboard can only offer a paper's abstract page and its 📄 PDF button when
the queue line carries a ref (``… — 2608.23534``). The nightly digest has
written refs since it existed, but the bulk of ``reading-queue.md`` predates it:
those lines are bare titles, and a bare title can only be rendered as an arXiv
*title search* — a results page, a squint and a tap, per paper, on a phone.

This script retires that fallback. For every ref-less line it asks the arXiv API
for the title, and appends ``— <id>`` **only** when exactly one arXiv paper's
title matches after normalisation (``arxiv_refs.match_entries``). Anything
looser is left alone: a wrong id is worse than a search box, because it sends
the reader confidently to somebody else's paper.

It is idempotent and resumable — a line that already has a ref is skipped, so
successive runs only ever work on what is left. Lines arXiv genuinely does not
have (a journal-only paper, a thesis, a talk) are simply never matched and are
re-attempted each run; that is the cost of holding no per-line failure state,
and it is bounded by ``--limit``.

Run by ``.github/workflows/arxiv_refs.yml`` (a checkout has no arXiv access
inside a sandboxed session; CI does). Locally:

    python scripts/backfill_arxiv_refs.py                 # report, change nothing
    python scripts/backfill_arxiv_refs.py --write         # apply
    python scripts/backfill_arxiv_refs.py --write --limit 60
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import arxiv_refs  # noqa: E402
import board  # noqa: E402
import inbox_actions  # noqa: E402

MEMORY_HOME = Path(__file__).resolve().parents[1]

#: The files whose paper lines carry refs. Both use the same title/ref grammar,
#: so both are backfilled by the same pass.
TARGETS = (inbox_actions.QUEUE_FILE, inbox_actions.INBOX_FILE)


def candidates(text: str, source: str) -> list[tuple[int, str]]:
    """``[(line_index, title), …]`` for the lines this pass could fill in.

    Which lines *are* papers is not re-decided here: the queue's section gating
    and the inbox's date-stamped line grammar are read straight off the two
    parsers that render the board, so a line the board does not show as a paper
    is never touched. Of those, a line qualifies when it is not already DONE
    (reading history needs no new links) and carries no ref.
    """
    out = []
    in_section = False
    for i, raw in enumerate(text.splitlines()):
        if source == inbox_actions.INBOX_FILE:
            stamped = inbox_actions.parse_line(raw)
            if not stamped:
                continue
            body = stamped[1]
        else:
            m = board.QUEUE_SECTION_RE.match(raw)
            if m and not m.group(1).startswith("#"):
                in_section = True
                continue
            if not in_section or not raw.strip():
                continue
            body = raw.strip()
        paper = board._parse_paper(body)
        if paper["done"] or paper["ref"] or not paper["title"]:
            continue
        out.append((i, paper["title"]))
    return out


def apply_ref(raw_line: str, ref: str) -> str:
    """`raw_line` with ``— <ref>`` appended, preserving its exact prefix.

    Appending rather than rewriting keeps the inbox's date stamp, any stray
    indentation and the title's own punctuation byte-for-byte intact — the queue
    is a human-edited file and this script is a guest in it.
    """
    return f"{raw_line.rstrip()} — {ref}"


def backfill(root: Path, *, write: bool, limit: int,
             resolve=arxiv_refs.resolve_title,
             delay: float = arxiv_refs.API_DELAY_SECONDS,
             sleep=time.sleep, log=print) -> dict:
    """Resolve up to `limit` ref-less titles across the queue and the inbox."""
    stats = {"scanned": 0, "matched": 0, "unmatched": 0, "files": []}
    budget = limit
    for name in TARGETS:
        path = root / name
        if not path.exists():
            continue
        lines = path.read_text(errors="replace").splitlines()
        todo = candidates("\n".join(lines), name)
        stats["scanned"] += len(todo)
        changed = 0
        for idx, title in todo:
            if budget <= 0:
                break
            budget -= 1
            ref = resolve(title)
            if ref:
                lines[idx] = apply_ref(lines[idx], ref)
                changed += 1
                stats["matched"] += 1
                log(f"  ✔ {ref}  {title[:90]}")
            else:
                stats["unmatched"] += 1
                log(f"  · no unique match  {title[:90]}")
            # Politeness, not throughput: arXiv asks for a few seconds between
            # calls, and this job has all night.
            if budget > 0:
                sleep(delay)
        if changed:
            stats["files"].append(name)
            if write:
                path.write_text("\n".join(lines) + "\n")
        log(f"{name}: {len(todo)} ref-less, {changed} resolved"
            f"{'' if write else ' (dry run — nothing written)'}")
    return stats


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--write", action="store_true",
                    help="apply the refs (default: report only)")
    ap.add_argument("--limit", type=int, default=60,
                    help="most arXiv lookups to make in one run (default 60)")
    ap.add_argument("--root", type=Path, default=MEMORY_HOME)
    args = ap.parse_args(argv)

    stats = backfill(args.root, write=args.write, limit=args.limit)
    print(f"\n{stats['matched']} resolved, {stats['unmatched']} unresolved, "
          f"{stats['scanned']} ref-less lines in total.")
    # Not an error: an unresolved title is a normal outcome (not on arXiv, or
    # too ambiguous to be safe), and a run that resolves nothing must not fail
    # the nightly job.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
