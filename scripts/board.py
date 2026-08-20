"""scripts/board.py — the PyAutoMemory Dashboard.

A phone-readable, MANAGEMENT-FIRST view of the repo's knowledge: what is
waiting to be read, which paper sections still need a canonical BibTeX key,
how mature each sub-wiki is — each work queue carrying a one-tap 📋 copy
block holding a paste-ready Claude Code prompt that executes this repo's own
documented workflow (``bibliography/README.md`` "Adding a paper",
``wiki/CLAUDE.md``'s schema) — plus contents cards with ``/memory <domain>``
recall chips.

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
        section, count, done = None, 0, 0
        def _flush():
            if section is not None:
                snapshot["queue"].append({"section": section, "count": count,
                                          "done": done})
        for line in queue.read_text(errors="replace").splitlines():
            m = QUEUE_SECTION_RE.match(line)
            if m and not m.group(1).startswith("#"):
                _flush()
                section, count, done = m.group(1), 0, 0
            elif section is not None and line.strip():
                if QUEUE_DONE_RE.match(line.strip()):
                    done += 1
                else:
                    count += 1
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
    for q in snapshot.get("queue") or []:
        done = f", {q['done']} read" if q.get("done") else ""
        lines.append(f"- {q['section']}: {q['count']} waiting{done}")
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
            f"onclick='cp(this)'>📋</button>")


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

    queue_rows = []
    for q in snapshot.get("queue") or []:
        done = (f" <span class='meta'>· {q['done']} read</span>"
                if q.get("done") else "")
        queue_rows.append(
            f"<tr><td class='name'>{_html.escape(q['section'])}</td>"
            f"<td>{q['count']} waiting{done} "
            f"{_copy_btn(_read_prompt(snapshot, q['section']), 'copy: file the next paper')}"
            f"</td></tr>")
    if not queue_rows:
        queue_rows.append("<tr><td colspan='2'>queue empty or unavailable</td></tr>")

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
  footer {{ margin-top: 2rem; color: #8b949e; font-size: .8rem; }}
</style>
<script>
function cp(b){{var t=b.getAttribute('data-copy');
 if(navigator.clipboard&&navigator.clipboard.writeText){{
   navigator.clipboard.writeText(t).then(function(){{ok(b)}},function(){{fb(t)}});
 }}else{{fb(t)}}}}
function ok(b){{b.textContent='✓';setTimeout(function(){{b.textContent='📋'}},1200)}}
function fb(t){{window.prompt('Copy this:',t)}}
</script></head>
<body><div class="wrap">
  <h1>PyAutoMemory Dashboard</h1>
  <p><span class="pill">{t['pages']} pages · {pct}% cited</span> <span class="meta"><a href="dashboard.md">markdown version</a></span></p>
  <p class="meta">Contents and work queues for the organism's long-term memory
  — titles and counts only; the knowledge itself lives in the wiki pages.
  📋 copies a paste-ready prompt for a Claude Code chat.</p>
  <h2>Reading queue <span class='meta'>({t['queued']} papers waiting)</span></h2>
  <table>{''.join(queue_rows)}</table>
  <h2>Citation work queue <span class='meta'>({t['todo']} sections need a canonical key)</span></h2>
  <table>{''.join(todo_rows)}</table>
  <h2>Sub-wikis <span class='meta'>({snapshot.get('bib_entries', 0)} bibliography entries ·
  {snapshot.get('links', {}).get('wanted', 0)} wanted pages)</span></h2>
  <table>{''.join(wiki_rows)}</table>
  <footer>Rendered by <code>scripts/board.py</code> from the checkout —
  nothing here is committed; generated {_html.escape(str(snapshot.get('generated') or '?'))}.</footer>
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
