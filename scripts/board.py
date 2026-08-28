"""scripts/board.py — the PyAutoMemory Dashboard.

A phone-readable, MANAGEMENT-FIRST view of the repo's knowledge: what is
waiting to be read, which paper sections still need a canonical BibTeX key,
how mature each sub-wiki is — each work queue carrying a one-tap 📋 copy
block holding a paste-ready Claude Code prompt that executes this repo's own
documented workflow (``bibliography/README.md`` "Adding a paper",
``wiki/CLAUDE.md``'s schema) — plus contents cards with ``/memory <domain>``
recall chips. Reading-queue sections expand to the individual papers: each
title links out to the arXiv abstract page (or, when the line carries no ref,
a title search — see ``scripts/arxiv_refs.py``), carries a 📄 button onto the
PDF itself so a phone can collect a stack of papers without a detour through
search, and carries three prefilled-GitHub-issue actions — 📥 intake-into-memory
(really interesting: full filing), 📑 make-citeable (worth citing, not
pivotal: bib entry + minimal sources section), both open work items carrying
the human's free-text notes, and ✅ read-don't-file (processed automatically
by ``queue_actions.yml`` via ``queue_mark_done.py``). Nothing changes state
until the human submits the issue.

Above the queue sits the **arXiv inbox** (``arxiv-inbox.md``): what the nightly
digest suggested overnight, each line showing how many days it has left before
it lapses and carrying the same 📄 PDF button plus two further actions —
➕ add-to-the-queue and ✖️ dismiss.
The inbox's format, window and transitions live in ``scripts/inbox_actions.py``;
this module reads them rather than re-deriving them.

Below the inbox sits the **arXiv interests list** (``arxiv-interests.md``):
the same overnight machinery pointed at everything that is *not* strong
lensing — black holes, dark matter, galaxy formation, statistics — as one
day-batch of ten. It renders the same five actions per paper, plus one 🧹
*clear* button on the batch itself: the list is a backlog rather than a timer,
so the board shows the OLDEST un-cleared day only and clearing it reveals the
next. ``scripts/interests_actions.py`` owns that format and those transitions.

Both suggestion tiers also carry a **freshness line**: the date of the last digest run,
so an empty inbox says *which* kind of empty it is — arXiv was quiet, or the
filing broke. The date is rendered into the page, but the "this looks broken"
warning is computed in the reader's browser (see ``_EXTRA_JS``), because the
page freezes at its last good render in exactly the failure the warning is for.

A queue section is not a flat list of papers: a `__Bold__` line is a
sub-heading the human wrote, and a `NOTE `-prefixed line (or a bare non-arXiv
link) is an annotation. Both render as themselves — no link, no buttons, no
slot in the "N waiting" count — because a heading is not a paper you can
download. `_parse_paper` decides which is which; see `reading-queue.md`.

**Contents-level only.** The board shows titles and counts, never claim text
or summaries — the knowledge itself stays in the wiki pages.

**Fully local.** Everything renders from the checkout (no network):
frontmatter statuses, ``**Canonical BibTeX key:**`` markers, bib entry
counts, reading-queue sections, wikilink totals. Repo identity (for links)
derives from ``git remote`` — nothing is hardcoded, so the script travels
into spawned templates unchanged.

Published by ``.github/workflows/knowledge_board.yml`` (Pages + badge + the
README ``memory:begin/end`` strip). Nothing is committed —
``validate_structure.py`` bans ``.html`` and gates the root allowlist, so the
board is rendered fresh in CI, the Heart pattern.

Usage:
    python scripts/board.py [--md | --md-brief | --html | --badge | --json]
"""

from __future__ import annotations

import datetime
import html as _html
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote as _quote

MEMORY_HOME = Path(__file__).resolve().parents[1]

# The arXiv inbox owns its own line format, window and transitions; the
# board reads them rather than re-deriving them (scripts/inbox_actions.py).
sys.path.insert(0, str(Path(__file__).resolve().parent))
import arxiv_refs  # noqa: E402
import inbox_actions  # noqa: E402
import interests_actions  # noqa: E402

# The family look lives once, in the Brain (``board/_theme.py``): the
# stylesheet, the hero that redraws this organ's logo as a mark, and the
# cross-board footer. Imported rather than copied, so the look moves for the
# whole family at once — knowledge_board.yml checks PyAutoBrain out beside
# this repo, and a local run finds the sibling checkout the way the other
# PyAuto tools resolve each other.
BOARD_KEY = "memory"  # this board's entry in the Brain's palette table


def _workspace_root() -> Path:
    """Where the sibling PyAuto checkouts live: `$PYAUTO_ROOT`, else `~/Code`.

    The org's own directory name is an instance fact, so it is never written
    here — a workspace that does not follow the default sets `$PYAUTO_ROOT`
    (the same variable the dev-flow doors read).
    """
    return Path(os.environ.get("PYAUTO_ROOT") or Path.home() / "Code")


def theme():
    """The shared theme module, or a RuntimeError naming the fix.

    Only the html path needs it; ``--md``/``--badge``/``--json`` never call
    here, so the digest keeps working with no PyAutoBrain in reach.
    """
    for cand in (os.environ.get("PYAUTO_BRAIN"), MEMORY_HOME / "PyAutoBrain",
                 MEMORY_HOME.parent / "PyAutoBrain",
                 _workspace_root() / "PyAutoBrain"):
        if not cand:
            continue
        board = Path(cand) / "board"
        if (board / "_theme.py").is_file():
            if str(board) not in sys.path:
                sys.path.insert(0, str(board))
            import _theme
            return _theme
    raise RuntimeError(
        "the shared board theme (PyAutoBrain/board/_theme.py) is not in reach "
        "— check PyAutoBrain out beside this repo or set PYAUTO_BRAIN")

KEY_MARK = "**Canonical BibTeX key:**"
STATUS_RE = re.compile(r"^status:\s*(\S+)", re.MULTILINE)
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
BIB_ENTRY_RE = re.compile(r"^@\w+\{", re.MULTILINE)
RESOLVED_KEY_RE = re.compile(r"\*\*Canonical BibTeX key:\*\* `([^`]+)`")
# Queue sections are real `## ` headers (the 2026-08 restructure, #35); a
# consumed paper stays in place as a `DONE <date> — <title>` line, so the
# queue is also the reading history.
QUEUE_SECTION_RE = re.compile(r"^##\s+(.+?)\s*$")
QUEUE_DONE_RE = re.compile(r"^DONE\b")
QUEUE_DONE_LINE_RE = re.compile(r"^DONE\s+(\d{4}-\d{2}-\d{2})\s*—\s*(.*)$")
# A paper line may end ` — <arXiv id or URL>`; anything else after an em dash
# is part of the title.
QUEUE_REF_RE = re.compile(
    r"^(.*\S)\s+—\s+((?:arXiv:)?\d{4}\.\d{4,5}(?:v\d+)?|https?://\S+)$")
# Not every line under a `## Section` is a paper. Two kinds are not, and saying
# so is what stops the board rendering a search button for a heading and the
# backfill spending an arXiv lookup on one every night:
#   `__Dark Matter__`  a bold sub-heading the human wrote to group the papers
#                      below it — structure, rendered as structure.
#   `NOTE <text>`      an annotation: a free-text remark, a link that is not a
#                      paper, a stray line of pasted prose. Sibling of the
#                      `DONE ` prefix — same shape, same never-delete rule, and
#                      the marker `backfill_arxiv_refs.py --mark-unresolved`
#                      writes so a line it cannot identify is asked about once
#                      and then left alone.
QUEUE_SUBHEAD_RE = re.compile(r"^__(.+?)__$")
QUEUE_NOTE_RE = re.compile(r"^NOTE\b\s*(?:—\s*)?(.*)$")
#: A line that is nothing but a URL. An arXiv one is a paper whose title was
#: never written (the ref is the whole line); anything else is an annotation.
QUEUE_BARE_URL_RE = re.compile(r"^https?://\S+$")


def _owner_repo() -> tuple[str, str]:
    out = subprocess.run(
        ["git", "-C", str(MEMORY_HOME), "remote", "get-url", "origin"],
        capture_output=True, text=True,
    ).stdout.strip()
    m = re.search(r"[:/]([^/:]+)/([^/]+?)(?:\.git)?/?$", out)
    return (m.group(1), m.group(2)) if m else ("", "")


# --- collect (local files only) ----------------------------------------------
def collect(root: Path | None = None) -> dict:
    root = root or MEMORY_HOME
    owner, repo = _owner_repo() if root == MEMORY_HOME else ("", "")
    snapshot: dict = {
        "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "owner": owner,
        "repo": repo,
        "wikis": [],
        "bib_entries": 0,
        "queue": [],
        "inbox": [],
        "inbox_last_digest": None,
        # The interests list is day-batched: `interests` is the oldest
        # un-cleared batch (what the board shows), and `interests_batches` /
        # `interests_backlog` are how much is queued behind it.
        "interests": [],
        "interests_date": None,
        "interests_batches": 0,
        "interests_backlog": 0,
        "interests_last_digest": None,
        "links": {"total": 0, "unique": 0, "wanted": 0},
    }

    stems: set[str] = set()
    all_slugs: list[str] = []
    wiki_root = root / "wiki"
    for wdir in sorted(d for d in wiki_root.glob("*") if d.is_dir()):
        pages = sorted(wdir.rglob("*.md"))
        stems |= {p.stem for p in pages}
        statuses: dict[str, int] = {}
        kinds = {"concepts": 0, "entities": 0, "sources": 0}
        sections = 0
        todo = 0
        resolved: set[str] = set()
        for p in pages:
            text = p.read_text(errors="replace")
            m = STATUS_RE.search(text)
            if m:
                statuses[m.group(1)] = statuses.get(m.group(1), 0) + 1
            if p.parent.name in kinds:
                kinds[p.parent.name] += 1
            n_marks = text.count(KEY_MARK)
            sections += n_marks
            keys = RESOLVED_KEY_RE.findall(text)
            resolved |= set(keys)
            todo += n_marks - len(keys)
            all_slugs += WIKILINK_RE.findall(text)
        snapshot["wikis"].append({
            "name": wdir.name,
            "pages": len(pages),
            **kinds,
            "statuses": statuses,
            "sections": sections,
            "todo": todo,
            "resolved_keys": len(resolved),
        })

    for bib in sorted((root / "bibliography").glob("*.bib")):
        snapshot["bib_entries"] += len(BIB_ENTRY_RE.findall(
            bib.read_text(errors="replace")))

    queue = root / "reading-queue.md"
    if queue.exists():
        section, papers = None, []
        def _flush():
            if section is not None:
                snapshot["queue"].append({
                    "section": section,
                    # Headings and annotations are carried in `papers` so the
                    # section renders in file order, but they are not work:
                    # counting them would inflate every "N waiting" on the board.
                    "count": sum(1 for p in papers
                                 if p["kind"] == "paper" and not p["done"]),
                    "done": sum(1 for p in papers if p["done"]),
                    "papers": papers,
                })
        for line in queue.read_text(errors="replace").splitlines():
            m = QUEUE_SECTION_RE.match(line)
            if m and not m.group(1).startswith("#"):
                _flush()
                section, papers = m.group(1), []
            elif section is not None and line.strip():
                papers.append(_parse_paper(line.strip()))
        _flush()

    inbox = root / inbox_actions.INBOX_FILE
    if inbox.exists():
        today = datetime.datetime.now(datetime.timezone.utc).date()
        inbox_text = inbox.read_text(errors="replace")
        snapshot["inbox_last_digest"] = inbox_actions.last_digest(inbox_text)
        for entry in inbox_actions.papers(inbox_text):
            snapshot["inbox"].append({
                "title": entry["title"],
                "ref": entry["ref"],
                "line": entry["line"],
                "added": entry["added"],
                "days_left": inbox_actions.days_left(entry["added"], today),
                "done": False,
                "done_date": None,
            })

    interests = root / interests_actions.INTERESTS_FILE
    if interests.exists():
        text = interests.read_text(errors="replace")
        snapshot["interests_last_digest"] = inbox_actions.last_digest(text)
        every = interests_actions.batches(text)
        snapshot["interests_batches"] = len(every)
        snapshot["interests_backlog"] = sum(len(b) for _, b in every)
        current = interests_actions.current_batch(text)
        if current:
            snapshot["interests_date"] = current[0]
            for entry in current[1]:
                snapshot["interests"].append({
                    "title": entry["title"],
                    "ref": entry["ref"],
                    "line": entry["line"],
                    "added": entry["added"],
                    "topic": entry["topic"],
                    "section": interests_actions.section_for(entry),
                    "done": False,
                    "done_date": None,
                })

    slugs = [s.split("|")[0].strip() for s in all_slugs]
    uniq = set(slugs)
    snapshot["links"] = {
        "total": len(slugs),
        "unique": len(uniq),
        "wanted": len({s for s in uniq if s not in stems}),
    }
    return snapshot


# --- pure helpers --------------------------------------------------------------
def _parse_paper(text: str) -> dict:
    """One queue line → {kind, title, ref, done, done_date, line}.

    `line` is the line as written — the token every issue button round-trips.
    `kind` is what the line *is*: a `paper`, a `subhead` (a `__Bold__` grouping
    the human wrote), or a `note` (a `NOTE `-prefixed annotation, or a bare
    non-arXiv link). Only a `paper` is counted, given buttons, or looked up on
    arXiv; the other two are carried through and rendered as themselves, which
    is the whole point — a heading is not a paper you can download.
    """
    raw, done_date = text, None
    m = QUEUE_DONE_LINE_RE.match(text)
    if m:
        done_date, text = m.group(1), m.group(2)
    elif QUEUE_DONE_RE.match(text):
        done_date, text = "", text[4:].lstrip(" —-")

    def _built(kind, title, ref=None):
        return {"kind": kind, "title": title, "ref": ref,
                "done": done_date is not None,
                "done_date": done_date or None, "line": raw}

    # Checked before the ref split: a heading or an annotation has no ref to
    # find, and `NOTE https://…` must not be read as a titleless paper.
    m = QUEUE_SUBHEAD_RE.match(text)
    if m:
        return _built("subhead", m.group(1).strip())
    m = QUEUE_NOTE_RE.match(text)
    if m:
        return _built("note", m.group(1).strip())

    ref = None
    m = QUEUE_REF_RE.match(text)
    if m:
        text, ref = m.group(1), m.group(2)
    elif QUEUE_BARE_URL_RE.match(text):
        # A line that is only a URL. If it points at arXiv the human did write a
        # paper — just as a link instead of a title — so it earns its abstract
        # page and its PDF button, labelled by the identifier the line already
        # contains rather than by a hundred characters of raw URL. (No title is
        # invented: the id is read out of the line, and the line itself is what
        # every issue button still round-trips.) Any other bare link is an
        # annotation.
        aid = arxiv_refs.arxiv_id(text)
        if not aid:
            return _built("note", text)
        return _built("paper", f"arXiv:{aid}", text)
    return _built("paper", text, ref)


def _url_host(url: str) -> str:
    """`https://sub.example.org/a/b?c` → `sub.example.org` (the url if unparsable)."""
    m = re.match(r"^https?://([^/?#]+)", url)
    return m.group(1) if m else url


def paper_url(paper: dict) -> str:
    """Where to read the paper: its abstract page, or an arXiv title search.

    An arXiv ref in any shape — bare id, ``arXiv:``-prefixed, an abs URL, a
    ``/pdf/…pdf`` URL — resolves to the *abstract* page, so every queue line
    lands on the same kind of page and the PDF is a separate, explicit button
    (:func:`paper_pdf_url`). A non-arXiv ref is a link the human wrote and is
    followed verbatim. A line with no ref at all can only be searched for; the
    search is the fallback, not the design (``scripts/arxiv_refs.py``).
    """
    ref = paper.get("ref")
    if ref:
        return arxiv_refs.abs_url(ref) or ref
    return arxiv_refs.search_url(paper.get("title", ""))


def paper_pdf_url(paper: dict) -> str:
    """The paper's direct PDF, or "" when the line carries no arXiv ref.

    Empty is a rendering instruction: no ref, no 📄 button — the board never
    shows a button that cannot work. Retiring those empties is the backfill's
    job (``scripts/backfill_arxiv_refs.py``), not the renderer's.
    """
    return arxiv_refs.pdf_url(paper.get("ref")) or ""


def _queue_issue_url(snapshot: dict, section: str, paper: dict,
                     action: str,
                     source: str = inbox_actions.QUEUE_FILE) -> str:
    """A prefilled new-issue URL for a per-paper action.

    Five tiers — 'intake' (really interesting: full wiki filing), 'cite'
    (worth citing, not pivotal: bib entry + a minimal sources section), 'read'
    (done with it: DONE-mark only), and, for the suggestion tiers
    (arXiv-inbox, arXiv-interests), 'add' (into the reading queue) and
    'dismiss' (not for me). All but intake/cite are
    processed automatically by queue_actions.yml. Nothing changes state until
    the human submits the issue on GitHub; intake/cite issues stay open as the
    filing work item, and their `notes:` field is free text the human edits
    before submitting. Empty when the checkout has no remote (spawned
    templates).

    `source` names the file the line lives in. It is emitted for every tier,
    including the reading-queue ones, so the workflows never have to guess —
    the older scripts ignore the extra key.
    """
    repo_url = _repo_url(snapshot)
    if not repo_url:
        return ""
    # Two of the three sources are *suggestion* tiers: a paper there has no
    # reading-queue line yet, which is what the ➕/✖️ actions and the filing
    # NOTE below both turn on. Naming that once keeps the interests list from
    # being a second special case bolted beside the inbox.
    staged = source != inbox_actions.QUEUE_FILE
    whose, tier = {
        inbox_actions.INBOX_FILE: ("arXiv-inbox", "the arXiv inbox"),
        interests_actions.INTERESTS_FILE: ("arXiv-interests",
                                           "the arXiv interests list"),
    }.get(source, ("reading-queue", "the reading queue"))
    where = f"file: {source}\nsection: {section}\nline: {paper['line']}"
    notes = ("notes: (optional — replace this with why you added it or "
             "what was noteworthy, in your own words; whoever files the "
             "paper folds it in)")
    from_interests = source == interests_actions.INTERESTS_FILE
    if action == "add":
        issue_title = f"queue add: {paper['title']}"[:200]
        label = "interests-add" if from_interests else "queue-add"
        body = (f"Move this {whose} paper into the reading queue "
                f"(section: {section}) — worth reading, not yet read.\n\n"
                f"{where}\n\n"
                "Processed automatically by queue_actions.yml.")
    elif action == "dismiss":
        issue_title = f"queue dismiss: {paper['title']}"[:200]
        label = "interests-dismiss" if from_interests else "queue-dismiss"
        body = (f"Drop this paper from {tier} — not one for me. The "
                "line is removed rather than DONE-marked: an un-acted "
                "suggestion is not reading history, and git history holds it "
                "either way.\n\n"
                f"{where}\n\n"
                "Processed automatically by queue_actions.yml.")
    elif action == "read":
        issue_title = f"queue read: {paper['title']}"[:200]
        label = "queue-read"
        body = (f"Mark this {whose} paper as read without filing it "
                "(the line stays, DONE-prefixed — the reading history).\n\n"
                f"{where}\n\n"
                "Processed automatically by queue_actions.yml.")
    elif action == "cite":
        issue_title = f"queue cite: {paper['title']}"[:200]
        label = "queue-cite"
        body = (f"Make this {whose} paper citeable — read, worth "
                "citing, but not pivotal enough for full wiki treatment.\n\n"
                f"{where}\n\n"
                f"{notes}\n\n"
                "Workflow (bibliography/README.md \"Adding a paper\", "
                "wiki/CLAUDE.md): verify the paper against an authoritative "
                "record, add its canonical entry to the bibliography/ BibTeX "
                "file, add a minimal section to the matching "
                "wiki/<domain>/sources/ page — canonical key plus the notes "
                "above, nothing deeper — mark its queue line "
                "'DONE <date> — <title>' in reading-queue.md, and run "
                "make validate.")
    else:
        issue_title = f"queue intake: {paper['title']}"[:200]
        label = "queue-intake"
        body = (f"File this {whose} paper into memory.\n\n"
                f"{where}\n\n"
                f"{notes}\n\n"
                "Workflow (bibliography/README.md \"Adding a paper\", "
                "wiki/CLAUDE.md): verify the paper against an authoritative "
                "record, add its canonical entry to the bibliography/ BibTeX "
                "file, stub it in the matching wiki/<domain>/sources/ page — "
                "incorporating the notes above — mark its queue line "
                "'DONE <date> — <title>' in reading-queue.md, and run "
                "make validate.")
    if staged and action not in ("add", "dismiss", "read"):
        # A suggestion-tier paper has no reading-queue line to DONE-mark:
        # filing it creates that line, already read, and clears the tier one.
        body += (f"\n\nNOTE: this paper is in {source} and is NOT in the "
                 "reading queue yet, so there is no line to mark. Instead "
                 f"append it to the '{section}' section of reading-queue.md "
                 "already DONE-prefixed (it is being filed now, not queued to "
                 f"read later) and remove its {source} line.")
    return (f"{repo_url}/issues/new?title={_quote(issue_title, safe='')}"
            f"&body={_quote(body, safe='')}&labels={_quote(label, safe='')}")


def _interests_clear_url(snapshot: dict, date: str, count: int) -> str:
    """The 🧹 button: a prefilled issue that drops one whole interests batch.

    The only board action that is not per-paper, because the list is not a
    per-paper decision: the human walks a backlog of days, taking what they
    want out of a day and clearing the rest of it in one tap. Everything still
    goes through the same gate — an issue, submitted by hand, processed by
    queue_actions.yml — so nothing changes state on a mis-tap.
    """
    repo_url = _repo_url(snapshot)
    if not repo_url:
        return ""
    title = f"interests clear: {date}"
    body = (f"Clear the {date} batch ({count} paper(s)) from "
            f"{interests_actions.INTERESTS_FILE} — done with this day, show "
            "the next one.\n\n"
            f"file: {interests_actions.INTERESTS_FILE}\n"
            f"date: {date}\n\n"
            "The lines are removed rather than DONE-marked: an un-acted "
            "suggestion is not reading history, and git history holds the "
            "batch either way.\n\n"
            "Processed automatically by queue_actions.yml.")
    return (f"{repo_url}/issues/new?title={_quote(title, safe='')}"
            f"&body={_quote(body, safe='')}"
            f"&labels={_quote('interests-clear', safe='')}")


def _read_trend(snapshot: dict) -> dict:
    """Read counts from the DONE history, relative to the snapshot's
    `generated` timestamp (pure — no wall clock): papers read in the last
    7/30 days plus eight weekly buckets, oldest first."""
    trend = {"d7": 0, "d30": 0, "weeks": [0] * 8}
    try:
        now = datetime.date.fromisoformat(str(snapshot.get("generated"))[:10])
    except ValueError:
        return trend
    for q in snapshot.get("queue") or []:
        for p in q.get("papers") or []:
            if not p.get("done_date"):
                continue
            try:
                age = (now - datetime.date.fromisoformat(p["done_date"])).days
            except ValueError:
                continue
            if age < 0:
                continue
            if age < 7:
                trend["d7"] += 1
            if age < 30:
                trend["d30"] += 1
            if age < 56:
                trend["weeks"][7 - age // 7] += 1
    return trend


def _totals(snapshot: dict) -> dict:
    wikis = snapshot.get("wikis") or []
    statuses: dict[str, int] = {}
    for w in wikis:
        for k, v in (w.get("statuses") or {}).items():
            statuses[k] = statuses.get(k, 0) + v
    sections = sum(w.get("sections", 0) for w in wikis)
    todo = sum(w.get("todo", 0) for w in wikis)
    return {
        "pages": sum(w.get("pages", 0) for w in wikis),
        "statuses": statuses,
        "sections": sections,
        "todo": todo,
        "resolved": sections - todo,
        "queued": sum(q.get("count", 0) for q in snapshot.get("queue") or []),
    }


def pages_url(snapshot: dict) -> str:
    owner = str(snapshot.get("owner") or "").lower()
    repo = snapshot.get("repo") or ""
    return f"https://{owner}.github.io/{repo}/" if owner and repo else ""


def _repo_url(snapshot: dict) -> str:
    owner, repo = snapshot.get("owner"), snapshot.get("repo")
    return f"https://github.com/{owner}/{repo}" if owner and repo else ""


# The one-tap board family — the cross-board footer nav every board carries,
# each board skipping its own entry. Owner comes from the snapshot.
BOARD_FAMILY = (("mind", "PyAutoMind"), ("brain", "PyAutoBrain"),
                ("heart", "PyAutoHeart"), ("hands", "PyAutoHands"),
                ("organism", "PyAutoScientist"))


def _boards_nav(snapshot: dict) -> str:
    """The cross-board footer — one chip per sibling, each in its own organ's
    colour (the theme owns the chip palette; this board owns the URLs)."""
    owner = str(snapshot.get("owner") or "").lower()
    if not owner:
        return ""
    links = {key: f"https://{owner}.github.io/{repo}/"
             for key, repo in BOARD_FAMILY}
    return theme().boards_footer(links, BOARD_KEY)


def _read_prompt(snapshot: dict, section: str) -> str:
    repo = snapshot.get("repo") or "the memory repo"
    return (f"Work through the next paper in the '## {section}' section of "
            f"{repo}/reading-queue.md: verify it against an authoritative "
            f"record, add its canonical entry to the bibliography/ BibTeX "
            f"file, stub it in the matching wiki/<domain>/sources/ page per "
            f"wiki/CLAUDE.md, mark its queue line 'DONE <date> — <title>', "
            f"and run make validate.")


def _todo_prompt(snapshot: dict, wiki: str) -> str:
    repo = snapshot.get("repo") or "the memory repo"
    return (f"Resolve TODO canonical BibTeX keys in {repo}/wiki/{wiki}/sources/: "
            f"for each '{KEY_MARK} TODO' section, search the bibliography/ "
            f"BibTeX file by DOI, arXiv ID and title, set the canonical key "
            f"per bibliography/README.md, and run make validate. Work through "
            f"a handful, then stop for review.")


def _stub_prompt(snapshot: dict, wiki: str) -> str:
    repo = snapshot.get("repo") or "the memory repo"
    return (f"Upgrade one stub page in {repo}/wiki/{wiki}/ to drafted: verify "
            f"its claims against the cited sources, expand it per the schema "
            f"in wiki/CLAUDE.md, set status: drafted, and run make validate.")


def _inbox_freshness(snapshot: dict, key: str = "inbox_last_digest") -> dict:
    """A suggestion tier's freshness facts, shared by both renderers.

    ``key`` picks the tier — the strong-lensing inbox or the interests list.
    Each has its own nightly digest and so its own way to be silently broken.

    ``stale`` is what the *markdown* fallback can say. The HTML page must not
    trust it for the warning: see ``_EXTRA_JS``.
    """
    stamp = snapshot.get(key)
    try:
        today = datetime.datetime.fromisoformat(
            str(snapshot.get("generated"))).date()
    except (TypeError, ValueError):
        today = datetime.datetime.now(datetime.timezone.utc).date()
    return {
        "stamp": stamp,
        "weekdays": inbox_actions.weekdays_since(stamp, today) if stamp else 0,
        "stale": inbox_actions.is_stale(stamp, today),
    }


def _inbox_empty_note(fresh: dict) -> str:
    """Why a tier is empty — quiet, suspect, or never run. Plain text."""
    if fresh["stale"]:
        return (f"no digest since {fresh['stamp']} "
                f"({fresh['weekdays']} weekdays) — the nightly filing may be "
                f"broken")
    if fresh["stamp"]:
        return f"the last digest ran {fresh['stamp']} and found nothing"
    return "the nightly arXiv digest fills this — no run recorded yet"


# --- renderers ------------------------------------------------------------------
def _render_md(snapshot: dict) -> str:
    t = _totals(snapshot)
    lines = ["# PyAutoMemory Dashboard", "",
             "_Contents and work queues — the knowledge itself lives in the "
             "wiki pages._", "",
             f"**{t['pages']} pages** across {len(snapshot.get('wikis') or [])} "
             f"sub-wikis · **{t['resolved']}/{t['sections']}** paper sections "
             f"cite a resolved key · **{snapshot.get('bib_entries', 0)}** "
             f"bibliography entries · **{t['queued']}** papers queued", ""]
    lines += ["| Wiki | Pages | Stub | Drafted | Reviewed | Key TODOs |",
              "|---|---|---|---|---|---|"]
    for w in snapshot.get("wikis") or []:
        s = w.get("statuses") or {}
        lines.append(f"| {w['name']} | {w['pages']} | {s.get('stub', 0)} | "
                     f"{s.get('drafted', 0)} | {s.get('reviewed', 0)} | "
                     f"{w.get('todo', 0)} |")
    lines += ["", "## arXiv inbox", ""]
    inbox = snapshot.get("inbox") or []
    fresh = _inbox_freshness(snapshot)
    if inbox:
        digest = (f"last digest {fresh['stamp']} · " if fresh["stamp"] else "")
        warn = ("⚠ " if fresh["stale"] else "")
        lines += [f"_{len(inbox)} waiting · {warn}{digest}un-acted suggestions "
                  f"lapse after {inbox_actions.INBOX_WINDOW_DAYS} days._", ""]
        for p in inbox:
            label = p["title"].replace("[", "\\[").replace("]", "\\]")
            bits = [f"- [{label}]({paper_url(p)}) — _{p['days_left']}d left_"]
            pdf = paper_pdf_url(p)
            if pdf:
                bits.append(f"[pdf 📄]({pdf})")
            for action, chip in (("add", "queue ➕"), ("intake", "intake 📥"),
                                 ("cite", "cite 📑"), ("dismiss", "dismiss ✖️")):
                u = _queue_issue_url(snapshot, inbox_actions.INBOX_TARGET_SECTION,
                                     p, action, source=inbox_actions.INBOX_FILE)
                if u:
                    bits.append(f"[{chip}]({u})")
            lines.append(" · ".join(bits))
        lines.append("")
    else:
        warn = ("⚠ " if fresh["stale"] else "")
        lines += [f"- _(nothing waiting — {warn}{_inbox_empty_note(fresh)})_", ""]

    lines += ["", "## arXiv interests", ""]
    interests = snapshot.get("interests") or []
    ifresh = _inbox_freshness(snapshot, "interests_last_digest")
    if interests:
        date = snapshot.get("interests_date") or "?"
        left = max(0, (snapshot.get("interests_batches") or 1) - 1)
        backlog = (f" · {left} more day{'s' if left != 1 else ''} behind it"
                   if left else " · nothing behind it")
        clear_url = _interests_clear_url(snapshot, date, len(interests))
        clear = f" · [clear this day \U0001f9f9]({clear_url})" if clear_url else ""
        lines += [f"_{date} · {len(interests)} "
                  f"paper{'s' if len(interests) != 1 else ''}{backlog}{clear}_",
                  ""]
        for p_ in interests:
            label = p_["title"].replace("[", "\\[").replace("]", "\\]")
            bits = [f"- [{label}]({paper_url(p_)})"]
            if p_.get("topic"):
                bits.append(f"_{p_['topic']}_")
            pdf = paper_pdf_url(p_)
            if pdf:
                bits.append(f"[pdf 📄]({pdf})")
            for action, chip in (("add", "queue ➕"), ("intake", "intake 📥"),
                                 ("cite", "cite 📑"), ("dismiss", "dismiss ✖️")):
                u = _queue_issue_url(snapshot, p_["section"], p_, action,
                                     source=interests_actions.INTERESTS_FILE)
                if u:
                    bits.append(f"[{chip}]({u})")
            lines.append(" · ".join(bits))
        lines.append("")
    else:
        warn = ("⚠ " if ifresh["stale"] else "")
        lines += [f"- _(no batch waiting — {warn}{_inbox_empty_note(ifresh)})_",
                  ""]

    lines += ["## Reading queue", ""]
    trend = _read_trend(snapshot)
    if sum(q.get("done", 0) for q in snapshot.get("queue") or []):
        lines += [f"_{trend['d7']} read in the last 7 days · "
                  f"{trend['d30']} in the last 30._", ""]
    for q in snapshot.get("queue") or []:
        done = f", {q['done']} read" if q.get("done") else ""
        lines += [f"<details><summary>{q['section']}: {q['count']} "
                  f"waiting{done}</summary>", ""]
        for p in q.get("papers") or []:
            if p["done"]:
                continue
            label = p["title"].replace("[", "\\[").replace("]", "\\]")
            if p["kind"] == "subhead":
                lines.append(f"- **{label}**")
                continue
            if p["kind"] == "note":
                if QUEUE_BARE_URL_RE.match(p["title"]):
                    label = f"[{_url_host(p['title'])} →]({p['title']})"
                lines.append(f"- _{label}_")
                continue
            bits = [f"- [{label}]({paper_url(p)})"]
            pdf = paper_pdf_url(p)
            if pdf:
                bits.append(f"[pdf 📄]({pdf})")
            for action, chip in (("intake", "intake 📥"), ("cite", "cite 📑"),
                                 ("read", "read ✅")):
                u = _queue_issue_url(snapshot, q["section"], p, action)
                if u:
                    bits.append(f"[{chip}]({u})")
            lines.append(" · ".join(bits))
        lines += ["", "</details>"]
    if not snapshot.get("queue"):
        lines.append("- _(queue empty or unavailable)_")
    url = pages_url(snapshot)
    if url:
        lines += ["", f"[Dashboard]({url}) — one-tap 📋 work prompts"]
    return "\n".join(lines)


def _render_md_brief(snapshot: dict) -> str:
    t = _totals(snapshot)
    pct = round(100 * t["resolved"] / t["sections"]) if t["sections"] else 0
    bits = [f"🧠 **{t['pages']} pages** · {t['statuses'].get('drafted', 0)} drafted",
            f"{pct}% of {t['sections']} paper sections cite a resolved key",
            f"{t['queued']} papers queued"]
    url = pages_url(snapshot)
    if url:
        bits.append(f"[dashboard →]({url})")
    return " · ".join(bits)


def _copy_btn(payload: str, label: str = "copy") -> str:
    return (f"<button class='copy' type='button' "
            f"title='{_html.escape(label, quote=True)}' "
            f"data-cmd=\"{_html.escape(payload, quote=True)}\">📋</button>")


def _bar(statuses: dict) -> str:
    stub = statuses.get("stub", 0)
    drafted = statuses.get("drafted", 0)
    reviewed = statuses.get("reviewed", 0)
    total = max(1, stub + drafted + reviewed)
    seg = lambda n, cls: (f"<span class='seg {cls}' style='width:{100 * n / total:.0f}%'></span>"
                          if n else "")
    return f"<span class='bar'>{seg(reviewed, 'ok')}{seg(drafted, 'mid')}{seg(stub, 'lo')}</span>"


# The lede, and the page-specific shapes the shared sheet has no opinion on:
# the citation bar, the collapsible queue sections, the paper list and its
# filter, the read-rate sparkline. All written against the theme's variables,
# so this board follows the family accent instead of setting a second palette.
_LEDE = ("What the organism knows, and what it still owes a citation. On a "
         "paper: \U0001f4e5 intake · \U0001f4d1 cite · \u2705 mark read — each opens a "
         "prefilled issue (add notes, submit to act). \U0001f9f9 clears a whole "
         "interests day. \U0001f4cb copies a Claude Code prompt.")

_EXTRA_CSS = """
.bar{display:inline-block;width:90px;height:8px;border-radius:4px;
 overflow:hidden;background:var(--btn);vertical-align:middle;
 border:1px solid var(--line)}
.seg{display:inline-block;height:8px;float:left}
.seg.ok{background:var(--ok)}
.seg.mid{background:var(--accent)}
.seg.lo{background:var(--muted)}
details.qsec{border-top:1px solid var(--line);padding:.5rem .25rem}
details.qsec>summary{cursor:pointer;list-style:none}
details.qsec>summary::-webkit-details-marker{display:none}
details.qsec>summary .name::before{content:"\u25b8 ";color:var(--accent)}
details.qsec[open]>summary .name::before{content:"\u25be "}
.name{font-weight:600}
ul.papers{margin:.5rem 0 .25rem;padding-left:1.3rem}
ul.papers li{margin:.4rem 0}
ul.papers li.done{color:var(--muted)}
/* A heading the human wrote inside a section, and a line that is not a paper:
   both render as themselves — no link, no buttons, nothing to tap. */
ul.papers li.subhead{list-style:none;margin:.7rem 0 .2rem -1.3rem;
 font-weight:600;letter-spacing:.02em}
ul.papers li.note{color:var(--muted);font-style:italic}
a.act{margin-left:.35rem;padding:.05rem .4rem;font-size:.85rem;
 border:1px solid var(--line);border-radius:6px;background:var(--btn)}
a.act:hover{background:var(--tint);border-color:var(--accent);
 text-decoration:none}
a.act.pdf{border-color:var(--accent)}
/* The one batch-level action: it clears a whole day, so it is worded rather
   than an icon alone — a mis-tap here costs ten papers, not one. */
a.act.clear{border-color:var(--warn);color:var(--warn);font-weight:600}
a.act.clear:hover{background:var(--warn);color:var(--bg);border-color:var(--warn)}
.topic{color:var(--muted);font-size:.82em;margin-left:.4rem;
 padding:.05rem .35rem;border:1px solid var(--line);border-radius:6px}
details.hist{margin:.25rem 0 .25rem 1.3rem}
details.hist>summary{cursor:pointer}
#pfilter{width:100%;padding:.45rem .6rem;margin:.25rem 0 .5rem;
 background:var(--btn);color:var(--fg);border:1px solid var(--line);
 border-radius:8px;font:inherit}
#pfilter:focus{outline:none;border-color:var(--accent)}
.spark{display:inline-flex;align-items:flex-end;gap:2px;height:12px;
 margin-left:.45rem}
.spark .sb{width:5px;background:var(--accent);border-radius:1px;
 display:inline-block}
.fresh.stale{color:var(--warn);font-weight:600}
table.recent td.name{white-space:nowrap}
footer{margin-top:2rem;color:var(--muted);font-size:.82em}
"""

# The shared copy handler is delegated, so a chip inside a <summary> would
# also toggle its section. Swallow that one default; the filter is this
# board's own behaviour and stays here.
#
# freshness() is the inbox's staleness warning, and it runs HERE rather than in
# the renderer on purpose. knowledge_board.yml re-publishes on pushes to
# arxiv-inbox.md — which is precisely what stops happening when the nightly
# filing breaks. The page then freezes at its last good render, so a warning
# baked in at render time would sit at "0 weekdays" forever and never fire in
# the one failure it exists for. The rendered date is a fact and survives the
# freeze; the verdict is recomputed against the reader's own clock.
_EXTRA_JS = """
function freshness(){
 var els=document.querySelectorAll('.fresh[data-last-digest]');
 for(var i=0;i<els.length;i++){var el=els[i];
  var p=el.getAttribute('data-last-digest').split('-');
  var d=new Date(Date.UTC(+p[0],+p[1]-1,+p[2]));
  var now=new Date();
  var today=Date.UTC(now.getUTCFullYear(),now.getUTCMonth(),now.getUTCDate());
  var n=0,guard=0;
  while(d.getTime()<today&&guard++<400){
   d.setUTCDate(d.getUTCDate()+1);
   var w=d.getUTCDay(); if(w>0&&w<6){n++;}}
  if(n>=+el.getAttribute('data-stale-weekdays')){
   el.textContent=el.getAttribute('data-stale-text').replace('{n}',n);
   el.classList.add('stale');}}}
freshness();
document.addEventListener("click",function(e){
  var b=e.target.closest("button.copy");
  if(b&&b.closest("summary")){e.preventDefault();}},true);
function flt(q){q=q.toLowerCase();
 var secs=document.querySelectorAll('details.qsec');
 for(var i=0;i<secs.length;i++){var d=secs[i],any=false,histHit=false;
  var lis=d.querySelectorAll('ul.papers li');
  for(var j=0;j<lis.length;j++){var li=lis[j];
   var hit=!q||li.textContent.toLowerCase().indexOf(q)>=0;
   li.style.display=hit?'':'none';
   if(hit){any=true;if(li.className==='done')histHit=true;}}
  var openByDefault=d.classList.contains('inbox')||
                    d.classList.contains('interests');
  if(q){d.style.display=any?'':'none';d.open=any;}
  else{d.style.display='';d.open=openByDefault;}
  var h=d.querySelector('details.hist');
  if(h){h.style.display=(q&&!histHit)?'none':'';h.open=!!q&&histHit;}}}
"""


def _pdf_act(paper: dict) -> str:
    """The 📄 chip: the paper's PDF, one tap from the board.

    First in the row on purpose — the filing actions (📥 📑 ✅) decide what to do
    *after* reading, and this is the one that gets the paper onto the phone in
    the first place. ``rel='noopener'`` + ``target='_blank'`` so collecting a
    dozen PDFs before a flight does not keep navigating the board away.
    """
    url = paper_pdf_url(paper)
    if not url:
        return ""
    hint = ("download the PDF: opens arXiv's PDF directly — no search, no "
            "abstract page in between")
    return (f"<a class='act pdf' href=\"{_html.escape(url, quote=True)}\" "
            f"target='_blank' rel='noopener' "
            f"title='{_html.escape(hint, quote=True)}'>\U0001f4c4</a>")


def _render_html(snapshot: dict) -> str:
    t_ = theme()
    t = _totals(snapshot)
    pct = round(100 * t["resolved"] / t["sections"]) if t["sections"] else 0
    repo_url = _repo_url(snapshot)

    queue_blocks = []
    for q in snapshot.get("queue") or []:
        done = (f" · {q['done']} read" if q.get("done") else "")
        items = []
        hist_items = []
        for p in q.get("papers") or []:
            if p["done"]:
                hist_items.append(
                    f"<li class='done'>DONE {_html.escape(p.get('done_date') or '?')}"
                    f" — {_html.escape(p['title'])}</li>")
                continue
            if p["kind"] == "subhead":
                items.append(f"<li class='subhead'>"
                             f"{_html.escape(p['title'])}</li>")
                continue
            if p["kind"] == "note":
                text = _html.escape(p["title"])
                if QUEUE_BARE_URL_RE.match(p["title"]):
                    # A saved link is still a link: render it clickable, just
                    # without the paper buttons it cannot honour. Labelled by
                    # host — a tracking-wrapped URL is hundreds of characters
                    # of noise on a phone, and the line itself keeps the whole
                    # thing.
                    text = (f"<a href=\"{_html.escape(p['title'], quote=True)}\" "
                            f"target='_blank' rel='noopener'>"
                            f"{_html.escape(_url_host(p['title']))} →</a>")
                items.append(f"<li class='note'>{text}</li>")
                continue
            acts = [_pdf_act(p)]
            for action, icon, hint in (
                    ("intake", "📥", "intake into memory: really interesting — "
                                     "opens a prefilled issue (add your notes) "
                                     "that becomes the full filing work item"),
                    ("cite", "📑", "make citeable: worth citing, not pivotal — "
                                   "opens a prefilled issue (add your notes) "
                                   "for a bib entry + minimal sources section"),
                    ("read", "✅", "read — don't file: opens a prefilled issue; "
                                   "submitting marks this line DONE")):
                u = _queue_issue_url(snapshot, q["section"], p, action)
                if u:
                    acts.append(f"<a class='act' href=\"{_html.escape(u, quote=True)}\" "
                                f"title='{_html.escape(hint, quote=True)}'>{icon}</a>")
            items.append(
                f"<li><a href=\"{_html.escape(paper_url(p), quote=True)}\">"
                f"{_html.escape(p['title'])}</a>{''.join(acts)}</li>")
        hist = (f"<details class='hist'><summary class='meta'>reading history "
                f"({len(hist_items)})</summary><ul class='papers'>"
                f"{''.join(hist_items)}</ul></details>" if hist_items else "")
        queue_blocks.append(
            f"<details class='qsec'><summary><span class='name'>"
            f"{_html.escape(q['section'])}</span> <span class='meta'>"
            f"{q['count']} waiting{done}</span> "
            f"{_copy_btn(_read_prompt(snapshot, q['section']), 'copy: file the next paper')}"
            f"</summary><ul class='papers'>{''.join(items)}</ul>{hist}</details>")
    if not queue_blocks:
        queue_blocks.append("<p class='meta'>queue empty or unavailable</p>")

    inbox = snapshot.get("inbox") or []
    inbox_items = []
    for p in inbox:
        acts = [_pdf_act(p)]
        for action, icon, hint in (
                ("add", "➕", "add to the reading queue: worth reading — opens "
                              "a prefilled issue; submitting files the line"),
                ("intake", "📥", "intake into memory: really interesting — "
                                 "opens a prefilled issue (add your notes) "
                                 "that becomes the full filing work item"),
                ("cite", "📑", "make citeable: worth citing, not pivotal — "
                               "opens a prefilled issue (add your notes) for a "
                               "bib entry + minimal sources section"),
                ("dismiss", "✖️", "not for me: opens a prefilled issue; "
                                  "submitting drops the line from the inbox")):
            u = _queue_issue_url(snapshot, inbox_actions.INBOX_TARGET_SECTION,
                                 p, action, source=inbox_actions.INBOX_FILE)
            if u:
                acts.append(f"<a class='act' href=\"{_html.escape(u, quote=True)}\" "
                            f"title='{_html.escape(hint, quote=True)}'>{icon}</a>")
        inbox_items.append(
            f"<li><a href=\"{_html.escape(paper_url(p), quote=True)}\">"
            f"{_html.escape(p['title'])}</a> "
            f"<span class='meta'>{p['days_left']}d left</span>{''.join(acts)}</li>")
    # The date goes into the page; the "this looks broken" verdict is left to
    # the reader's browser (_EXTRA_JS). A stale render is exactly the case the
    # warning exists for, and a stale render cannot warn about itself.
    fresh = _inbox_freshness(snapshot)
    stale_tmpl = (f"⚠ no digest since {fresh['stamp']} ({{n}} weekdays) — the "
                  f"nightly filing may be broken") if fresh["stamp"] else ""

    def _fresh_span(fresh: dict, now_text: str, stale_text: str,
                    cls: str = "meta") -> str:
        """`fresh` is explicit because the page renders two tiers, each with
        its own digest, its own stamp and its own way of going silent."""
        if not fresh["stamp"]:
            return f"<span class='{cls}'>{_html.escape(now_text)}</span>"
        if fresh["stale"]:
            # Already stale at render time: show the warning now, so a reader
            # with JS off still sees it. The script recomputes `n` regardless.
            now_text = stale_text.replace("{n}", str(fresh["weekdays"]))
            cls += " stale"
        return (f"<span class='{cls} fresh' data-last-digest='{fresh['stamp']}' "
                f"data-stale-weekdays='{inbox_actions.INBOX_STALE_WEEKDAYS}' "
                f"data-stale-text=\"{_html.escape(stale_text, quote=True)}\">"
                f"{_html.escape(now_text)}</span>")

    if inbox_items:
        digest = f" · last digest {fresh['stamp']}" if fresh["stamp"] else ""
        meta = _fresh_span(
            fresh,
            f"{len(inbox_items)} waiting{digest} · lapse after "
            f"{inbox_actions.INBOX_WINDOW_DAYS}d",
            f"{len(inbox_items)} waiting · {stale_tmpl}")
        inbox_block = (
            f"<details class='qsec inbox' open><summary><span class='name'>"
            f"arXiv inbox</span> {meta}</summary>"
            f"<ul class='papers'>{''.join(inbox_items)}</ul></details>")
    else:
        note = _inbox_empty_note(fresh)
        inbox_block = ("<p>" + _fresh_span(
            fresh,
            f"nothing waiting — {note}",
            f"nothing waiting — {stale_tmpl}") + "</p>")

    interests = snapshot.get("interests") or []
    interest_items = []
    for p in interests:
        acts = [_pdf_act(p)]
        for action, icon, hint in (
                ("add", "\u2795", "add to the reading queue: worth reading — opens "
                              "a prefilled issue; submitting files the line"),
                ("intake", "\U0001f4e5", "intake into memory: really interesting — "
                                 "opens a prefilled issue (add your notes) "
                                 "that becomes the full filing work item"),
                ("cite", "\U0001f4d1", "make citeable: worth citing, not pivotal — "
                               "opens a prefilled issue (add your notes) for a "
                               "bib entry + minimal sources section"),
                ("dismiss", "\u2716\ufe0f", "not for me: opens a prefilled issue; "
                                  "submitting drops the line from this batch")):
            u = _queue_issue_url(snapshot, p["section"], p, action,
                                 source=interests_actions.INTERESTS_FILE)
            if u:
                acts.append(f"<a class='act' href=\"{_html.escape(u, quote=True)}\" "
                            f"title='{_html.escape(hint, quote=True)}'>{icon}</a>")
        topic = (f" <span class='topic'>{_html.escape(p['topic'])}</span>"
                 if p.get("topic") else "")
        interest_items.append(
            f"<li><a href=\"{_html.escape(paper_url(p), quote=True)}\">"
            f"{_html.escape(p['title'])}</a>{topic}{''.join(acts)}</li>")
    ifresh = _inbox_freshness(snapshot, "interests_last_digest")
    istale_tmpl = (f"\u26a0 no digest since {ifresh['stamp']} ({{n}} weekdays) — "
                   f"the nightly filing may be broken") if ifresh["stamp"] else ""
    if interest_items:
        idate = snapshot.get("interests_date") or "?"
        left = max(0, (snapshot.get("interests_batches") or 1) - 1)
        behind = (f" · {left} more day{'s' if left != 1 else ''} behind it"
                  if left else "")
        # The one non-per-paper action on the board. It sits in the <summary>
        # beside the count, because that is what it acts on: the day, not a
        # paper. No click handling needed, unlike the 📋 buttons beside it: a
        # link navigates away from the board, so whether the section also
        # toggles on the way out is not observable.
        clear_url = _interests_clear_url(snapshot, idate, len(interest_items))
        clear = (f"<a class='act clear' href=\"{_html.escape(clear_url, quote=True)}\" "
                 f"title='clear this whole day: opens a prefilled issue; "
                 f"submitting drops the {len(interest_items)} paper(s) left in "
                 f"the {idate} batch and reveals the next day'>"
                 f"\U0001f9f9 clear</a>" if clear_url else "")
        # `behind` rides on BOTH texts. A late digest is exactly when the
        # backlog depth matters most, and dropping it from the stale variant
        # hid it twice over: on a render that is already stale, and on a fresh
        # render the moment _EXTRA_JS swaps in `data-stale-text`.
        imeta = _fresh_span(
            ifresh,
            f"{len(interest_items)} paper"
            f"{'s' if len(interest_items) != 1 else ''}{behind}",
            f"{len(interest_items)} paper(s){behind} · {istale_tmpl}")
        # The batch's date IS its name — this is a backlog of days, and which
        # day you are looking at is the first thing to know.
        interests_block = (
            f"<details class='qsec interests' open><summary><span class='name'>"
            f"{_html.escape(idate)}</span> {imeta} {clear}</summary>"
            f"<ul class='papers'>{''.join(interest_items)}</ul></details>")
    else:
        interests_block = ("<p>" + _fresh_span(
            ifresh,
            f"no batch waiting — {_inbox_empty_note(ifresh)}",
            f"no batch waiting — {istale_tmpl}") + "</p>")

    trend = _read_trend(snapshot)
    total_done = sum(q.get("done", 0) for q in snapshot.get("queue") or [])
    trend_bits = f"{t['queued']} papers waiting"
    spark = ""
    if total_done:
        trend_bits += (f" · {trend['d7']} read last 7d · "
                       f"{trend['d30']} last 30d")
        if sum(trend["weeks"]):
            mx = max(trend["weeks"])
            bars = "".join(
                f"<span class='sb' style='height:{max(2, round(12 * w / mx))}px'"
                f" title='{w}'></span>" for w in trend["weeks"])
            spark = (f" <span class='spark' title='papers read per week, "
                     f"last 8 weeks'>{bars}</span>")
    filter_box = ""
    if t["queued"]:
        filter_box = (f"<input id='pfilter' type='search' "
                      f"placeholder='filter {t['queued']} papers…' "
                      f"oninput='flt(this.value)'>")

    todo_rows = []
    for w in snapshot.get("wikis") or []:
        if not w.get("todo"):
            continue
        todo_rows.append(
            f"<tr><td class='name'>{_html.escape(w['name'])}</td>"
            f"<td>{w['todo']} of {w['sections']} sections "
            f"{_copy_btn(_todo_prompt(snapshot, w['name']), 'copy: resolve canonical keys')}"
            f"</td></tr>")
    if not todo_rows:
        todo_rows.append("<tr><td colspan='2'>every paper section cites a resolved key</td></tr>")

    wiki_rows = []
    for w in snapshot.get("wikis") or []:
        s = w.get("statuses") or {}
        link = (f"<a href=\"{_html.escape(repo_url + '/blob/main/wiki/' + w['name'] + '/index.md', quote=True)}\">"
                f"{_html.escape(w['name'])}</a>" if repo_url else _html.escape(w["name"]))
        wiki_rows.append(
            f"<tr><td class='name'>{link}</td>"
            f"<td>{w['pages']} pages · {w.get('concepts', 0)}c/"
            f"{w.get('entities', 0)}e/{w.get('sources', 0)}s</td>"
            f"<td>{_bar(s)} <span class='meta'>{s.get('stub', 0)} stub · "
            f"{s.get('drafted', 0)} drafted</span> "
            f"{_copy_btn(_stub_prompt(snapshot, w['name']), 'copy: upgrade a stub')} "
            f"{_copy_btn('/memory ' + w['name'], 'copy: recall this domain')}"
            f"</td></tr>")

    n_batches = snapshot.get("interests_batches") or 0
    interests_backlog_note = (
        f"; {n_batches} day{'s' if n_batches != 1 else ''} of backlog, "
        f"{snapshot.get('interests_backlog') or 0} papers"
        if n_batches else "")

    hero = t_.hero(BOARD_KEY, "Dashboard", _LEDE)
    stats = t_.stats((t["pages"], "Pages"), (f"{pct}%", "Cited"),
                     (t["todo"], "To cite"), (t["queued"], "Queued"))
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PyAutoMemory Dashboard</title>
<style>{t_.css(BOARD_KEY)}{_EXTRA_CSS}</style>
</head>
<body>
{hero}
{stats}
<p class="muted mdsrc"><a href="dashboard.md">markdown version</a></p>
<h2>arXiv inbox <span class="muted">(suggested overnight — un-acted papers
 lapse after {inbox_actions.INBOX_WINDOW_DAYS} days)</span></h2>
{inbox_block}
<h2>arXiv interests <span class="muted">(everything that is not strong
 lensing — one day's ten at a time; \U0001f9f9 clears the day and shows the
 next{interests_backlog_note})</span></h2>
{interests_block}
<h2>Reading queue <span class="muted">({trend_bits})</span>{spark}</h2>
{filter_box}
{''.join(queue_blocks)}
<h2>Citation work queue <span class="muted">({t['todo']} sections need a
 canonical key)</span></h2>
<table class="recent">{''.join(todo_rows)}</table>
<h2>Sub-wikis <span class="muted">({snapshot.get('bib_entries', 0)} bibliography
 entries · {snapshot.get('links', {}).get('wanted', 0)} wanted pages)</span></h2>
<table class="recent">{''.join(wiki_rows)}</table>
{_boards_nav(snapshot)}
<footer>Rendered by <code>scripts/board.py</code> from the checkout —
nothing here is committed; generated
{_html.escape(str(snapshot.get('generated') or '?'))}.</footer>
<script>{t_.JS}{_EXTRA_JS}</script>
</body></html>
"""


def badge_endpoint(snapshot: dict) -> dict:
    t = _totals(snapshot)
    if not t["pages"]:
        return {"schemaVersion": 1, "label": "knowledge",
                "message": "unknown", "color": "lightgrey"}
    pct = round(100 * t["resolved"] / t["sections"]) if t["sections"] else 0
    return {"schemaVersion": 1, "label": "knowledge",
            "message": f"{t['pages']} pages · {pct}% cited", "color": "blueviolet"}


def render(snapshot: dict, fmt: str = "md") -> str:
    if fmt == "md":
        return _render_md(snapshot)
    if fmt == "md-brief":
        return _render_md_brief(snapshot)
    if fmt == "html":
        return _render_html(snapshot)
    if fmt == "badge":
        return json.dumps(badge_endpoint(snapshot))
    if fmt == "json":
        return json.dumps({**snapshot, "pages_url": pages_url(snapshot)},
                          indent=2, sort_keys=True)
    raise ValueError(f"unknown board fmt: {fmt!r}")


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(prog="scripts/board.py", description=__doc__)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--md", action="store_true", help="markdown board (default)")
    g.add_argument("--md-brief", action="store_true", help="the README strip")
    g.add_argument("--html", action="store_true", help="the Pages page")
    g.add_argument("--badge", action="store_true", help="shields endpoint JSON")
    g.add_argument("--json", action="store_true", help="the machine surface")
    ns = ap.parse_args(argv)
    snap = collect()
    fmt = "md"
    for name, label in (("md", "md"), ("md_brief", "md-brief"),
                        ("html", "html"), ("badge", "badge"), ("json", "json")):
        if getattr(ns, name):
            fmt = label
            break
    print(render(snap, fmt))
    return 0


if __name__ == "__main__":
    sys.exit(main())
