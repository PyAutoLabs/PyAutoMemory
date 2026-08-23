"""scripts/board.py — the PyAutoMemory Dashboard.

A phone-readable, MANAGEMENT-FIRST view of the repo's knowledge: what is
waiting to be read, which paper sections still need a canonical BibTeX key,
how mature each sub-wiki is — each work queue carrying a one-tap 📋 copy
block holding a paste-ready Claude Code prompt that executes this repo's own
documented workflow (``bibliography/README.md`` "Adding a paper",
``wiki/CLAUDE.md``'s schema) — plus contents cards with ``/memory <domain>``
recall chips. Reading-queue sections expand to the individual papers: each
title links out (arXiv abstract page, or a title search when the line has no
ref) and carries three prefilled-GitHub-issue actions — 📥 intake-into-memory
(really interesting: full filing), 📑 make-citeable (worth citing, not
pivotal: bib entry + minimal sources section), both open work items carrying
the human's free-text notes, and ✅ read-don't-file (processed automatically
by ``queue_actions.yml`` via ``queue_mark_done.py``). Nothing changes state
until the human submits the issue.

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
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote as _quote

MEMORY_HOME = Path(__file__).resolve().parents[1]

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
                    "count": sum(1 for p in papers if not p["done"]),
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
    """One queue line → {title, ref, done, done_date, line} (line = as written)."""
    raw, done_date = text, None
    m = QUEUE_DONE_LINE_RE.match(text)
    if m:
        done_date, text = m.group(1), m.group(2)
    elif QUEUE_DONE_RE.match(text):
        done_date, text = "", text[4:].lstrip(" —-")
    ref = None
    m = QUEUE_REF_RE.match(text)
    if m:
        text, ref = m.group(1), m.group(2)
    return {"title": text, "ref": ref, "done": done_date is not None,
            "done_date": done_date or None, "line": raw}


def paper_url(paper: dict) -> str:
    """Where to read the paper: its abstract page, or an arXiv title search."""
    ref = paper.get("ref")
    if ref:
        if ref.startswith("http"):
            return ref
        return "https://arxiv.org/abs/" + ref.removeprefix("arXiv:")
    return ("https://arxiv.org/search/?searchtype=title&query="
            + _quote(paper.get("title", ""), safe=""))


def _queue_issue_url(snapshot: dict, section: str, paper: dict,
                     action: str) -> str:
    """A prefilled new-issue URL for a per-paper action.

    Three tiers — 'intake' (really interesting: full wiki filing), 'cite'
    (worth citing, not pivotal: bib entry + a minimal sources section), and
    'read' (done with it: DONE-mark only, processed automatically by
    queue_actions.yml). Nothing changes state until the human submits the
    issue on GitHub; intake/cite issues stay open as the filing work item,
    and their `notes:` field is free text the human edits before submitting.
    Empty when the checkout has no remote (spawned templates).
    """
    repo_url = _repo_url(snapshot)
    if not repo_url:
        return ""
    where = f"section: {section}\nline: {paper['line']}"
    notes = ("notes: (optional — replace this with why you added it or "
             "what was noteworthy, in your own words; whoever files the "
             "paper folds it in)")
    if action == "read":
        issue_title = f"queue read: {paper['title']}"[:200]
        label = "queue-read"
        body = ("Mark this reading-queue paper as read without filing it "
                "(the line stays, DONE-prefixed — the reading history).\n\n"
                f"{where}\n\n"
                "Processed automatically by queue_actions.yml.")
    elif action == "cite":
        issue_title = f"queue cite: {paper['title']}"[:200]
        label = "queue-cite"
        body = ("Make this reading-queue paper citeable — read, worth "
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
        body = ("File this reading-queue paper into memory.\n\n"
                f"{where}\n\n"
                f"{notes}\n\n"
                "Workflow (bibliography/README.md \"Adding a paper\", "
                "wiki/CLAUDE.md): verify the paper against an authoritative "
                "record, add its canonical entry to the bibliography/ BibTeX "
                "file, stub it in the matching wiki/<domain>/sources/ page — "
                "incorporating the notes above — mark its queue line "
                "'DONE <date> — <title>' in reading-queue.md, and run "
                "make validate.")
    return (f"{repo_url}/issues/new?title={_quote(issue_title, safe='')}"
            f"&body={_quote(body, safe='')}&labels={_quote(label, safe='')}")


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
    owner = str(snapshot.get("owner") or "").lower()
    if not owner:
        return ""
    return " · ".join(f'<a href="https://{owner}.github.io/{repo}/">{name}</a>'
                      for name, repo in BOARD_FAMILY)


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
    lines += ["", "## Reading queue", ""]
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
            bits = [f"- [{label}]({paper_url(p)})"]
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
            f"data-copy=\"{_html.escape(payload, quote=True)}\" "
            f"onclick='cp(this,event)'>📋</button>")


def _bar(statuses: dict) -> str:
    stub = statuses.get("stub", 0)
    drafted = statuses.get("drafted", 0)
    reviewed = statuses.get("reviewed", 0)
    total = max(1, stub + drafted + reviewed)
    seg = lambda n, cls: (f"<span class='seg {cls}' style='width:{100 * n / total:.0f}%'></span>"
                          if n else "")
    return f"<span class='bar'>{seg(reviewed, 'ok')}{seg(drafted, 'mid')}{seg(stub, 'lo')}</span>"


def _render_html(snapshot: dict) -> str:
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
            acts = []
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

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PyAutoMemory — {t['pages']} pages</title>
<style>
  :root {{ color-scheme: light dark; }}
  * {{ box-sizing: border-box; }}
  body {{ font: 15px/1.5 -apple-system, Segoe UI, Roboto, sans-serif;
         margin: 0; padding: 2rem 1rem; background: #0d1117; color: #c9d1d9; }}
  .wrap {{ max-width: 760px; margin: 0 auto; }}
  h1 {{ font-size: 1.3rem; margin: 0 0 .25rem; }}
  h2 {{ font-size: 1rem; margin: 1.5rem 0 .5rem; }}
  .pill {{ display: inline-block; padding: .3rem .9rem; border-radius: 999px;
          font-weight: 700; background: #8957e5; color: #fff; }}
  .meta {{ color: #8b949e; font-size: .9rem; }}
  table {{ width: 100%; border-collapse: collapse; }}
  td {{ padding: .5rem .5rem; border-top: 1px solid #21262d; vertical-align: top; }}
  td.name {{ font-weight: 600; white-space: nowrap; }}
  a {{ color: #58a6ff; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  .bar {{ display: inline-block; width: 90px; height: 8px; border-radius: 4px;
         overflow: hidden; background: #21262d; vertical-align: middle; }}
  .seg {{ display: inline-block; height: 8px; float: left; }}
  .seg.ok {{ background: #3fb950; }}
  .seg.mid {{ background: #58a6ff; }}
  .seg.lo {{ background: #6e7681; }}
  button.copy {{ background: #21262d; border: 1px solid #30363d; border-radius: 6px;
                color: #c9d1d9; cursor: pointer; padding: .05rem .45rem;
                margin-left: .35rem; font-size: .85rem; line-height: 1.4; }}
  button.copy:hover {{ background: #30363d; }}
  details.qsec {{ border-top: 1px solid #21262d; padding: .5rem .25rem; }}
  details.qsec > summary {{ cursor: pointer; list-style: none; }}
  details.qsec > summary::-webkit-details-marker {{ display: none; }}
  details.qsec > summary .name::before {{ content: "▸ "; color: #8b949e; }}
  details.qsec[open] > summary .name::before {{ content: "▾ "; }}
  .name {{ font-weight: 600; }}
  ul.papers {{ margin: .5rem 0 .25rem; padding-left: 1.3rem; }}
  ul.papers li {{ margin: .4rem 0; }}
  ul.papers li.done {{ color: #8b949e; }}
  a.act {{ margin-left: .35rem; padding: .05rem .35rem; font-size: .85rem;
          border: 1px solid #30363d; border-radius: 6px; background: #21262d; }}
  a.act:hover {{ background: #30363d; text-decoration: none; }}
  details.hist {{ margin: .25rem 0 .25rem 1.3rem; }}
  details.hist > summary {{ cursor: pointer; }}
  #pfilter {{ width: 100%; padding: .45rem .6rem; margin: .25rem 0 .5rem;
             background: #0d1117; color: #c9d1d9; border: 1px solid #30363d;
             border-radius: 6px; font: inherit; }}
  .spark {{ display: inline-flex; align-items: flex-end; gap: 2px; height: 12px;
           margin-left: .45rem; }}
  .spark .sb {{ width: 5px; background: #8957e5; border-radius: 1px;
               display: inline-block; }}
  footer {{ margin-top: 2rem; color: #8b949e; font-size: .8rem; }}
</style>
<script>
function cp(b,e){{if(e){{e.preventDefault();e.stopPropagation();}}
 var t=b.getAttribute('data-copy');
 if(navigator.clipboard&&navigator.clipboard.writeText){{
   navigator.clipboard.writeText(t).then(function(){{ok(b)}},function(){{fb(t)}});
 }}else{{fb(t)}}}}
function ok(b){{b.textContent='✓';setTimeout(function(){{b.textContent='📋'}},1200)}}
function fb(t){{window.prompt('Copy this:',t)}}
function flt(q){{q=q.toLowerCase();
 var secs=document.querySelectorAll('details.qsec');
 for(var i=0;i<secs.length;i++){{var d=secs[i],any=false,histHit=false;
  var lis=d.querySelectorAll('ul.papers li');
  for(var j=0;j<lis.length;j++){{var li=lis[j];
   var hit=!q||li.textContent.toLowerCase().indexOf(q)>=0;
   li.style.display=hit?'':'none';
   if(hit){{any=true;if(li.className==='done')histHit=true;}}}}
  if(q){{d.style.display=any?'':'none';d.open=any;}}
  else{{d.style.display='';d.open=false;}}
  var h=d.querySelector('details.hist');
  if(h){{h.style.display=(q&&!histHit)?'none':'';h.open=!!q&&histHit;}}}}}}
</script></head>
<body><div class="wrap">
  <h1>PyAutoMemory Dashboard</h1>
  <p><span class="pill">{t['pages']} pages · {pct}% cited</span> <span class="meta"><a href="dashboard.md">markdown version</a></span></p>
  <p class="meta">On a paper: 📥 intake · 📑 cite · ✅ mark read — each opens a
  prefilled issue (add notes, submit to act). 📋 copies a Claude Code prompt.</p>
  <h2>Reading queue <span class='meta'>({trend_bits})</span>{spark}</h2>
  {filter_box}
  {''.join(queue_blocks)}
  <h2>Citation work queue <span class='meta'>({t['todo']} sections need a canonical key)</span></h2>
  <table>{''.join(todo_rows)}</table>
  <h2>Sub-wikis <span class='meta'>({snapshot.get('bib_entries', 0)} bibliography entries ·
  {snapshot.get('links', {}).get('wanted', 0)} wanted pages)</span></h2>
  <table>{''.join(wiki_rows)}</table>
  <footer>Rendered by <code>scripts/board.py</code> from the checkout —
  nothing here is committed; generated {_html.escape(str(snapshot.get('generated') or '?'))}.</footer>
  <p class="meta">Boards: {_boards_nav(snapshot)}</p>
</div></body></html>
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
