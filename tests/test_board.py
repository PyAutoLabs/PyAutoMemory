"""tests/test_board.py — the PyAutoMemory Dashboard (scripts/board.py).

The board's contract: counts are computed correctly from a synthetic tree,
every fmt renders, the work-queue prompts reference the repo's documented
workflow, the html is self-contained (no external assets), and — the privacy
guarantee — outputs are CONTENTS-LEVEL only: page titles and counts, never
page body text.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import board  # noqa: E402

BODY_MARKER = "the-secret-claim-text-that-must-never-leak"


def _tree(tmp_path: Path) -> Path:
    w = tmp_path / "wiki" / "demo"
    (w / "concepts").mkdir(parents=True)
    (w / "sources").mkdir()
    (w / "concepts" / "alpha.md").write_text(
        f"---\ntitle: Alpha\ntype: concept\nstatus: drafted\n---\n\n"
        f"{BODY_MARKER} with a [[beta]] link and a [[gamma]] link.\n")
    (w / "sources" / "papers.md").write_text(
        "---\ntitle: Papers\ntype: sources\nstatus: stub\n---\n\n"
        "## One\n**Canonical BibTeX key:** `Key2020`\n\n"
        "## Two\n**Canonical BibTeX key:** TODO — no unique match found.\n")
    (w / "index.md").write_text("# Demo index\n- [[alpha]]\n")
    bib = tmp_path / "bibliography"
    bib.mkdir()
    (bib / "demo.bib").write_text("@article{Key2020,\n title={T}\n}\n"
                                  "@book{Other2021,\n title={U}\n}\n")
    (tmp_path / "reading-queue.md").write_text(
        "# Reading queue\n\nintro prose\n\n---\n\n"
        "## Demo Papers\n\nTitle One\nTitle Two — 2406.01234\n"
        "DONE 2026-06-01 — Old Title\n\n## Other Things\n\nTitle Three\n")
    return tmp_path


def _snap_with_remote(tmp_path):
    """A synthetic snapshot with repo identity, as a live checkout has."""
    snap = board.collect(_tree(tmp_path))
    snap["owner"], snap["repo"] = "PyAutoLabs", "PyAutoMemory"
    return snap


def test_counts_from_a_synthetic_tree(tmp_path):
    snap = board.collect(_tree(tmp_path))
    (w,) = snap["wikis"]
    assert w["name"] == "demo" and w["pages"] == 3
    assert w["concepts"] == 1 and w["sources"] == 1
    assert w["statuses"] == {"drafted": 1, "stub": 1}
    assert w["sections"] == 2 and w["todo"] == 1 and w["resolved_keys"] == 1
    assert snap["bib_entries"] == 2
    assert snap["queue"] == [
        {"section": "Demo Papers", "count": 2, "done": 1, "papers": [
            {"title": "Title One", "ref": None, "done": False,
             "done_date": None, "line": "Title One"},
            {"title": "Title Two", "ref": "2406.01234", "done": False,
             "done_date": None, "line": "Title Two — 2406.01234"},
            {"title": "Old Title", "ref": None, "done": True,
             "done_date": "2026-06-01",
             "line": "DONE 2026-06-01 — Old Title"}]},
        {"section": "Other Things", "count": 1, "done": 0, "papers": [
            {"title": "Title Three", "ref": None, "done": False,
             "done_date": None, "line": "Title Three"}]}]
    # alpha exists; beta/gamma are wanted
    assert snap["links"]["wanted"] == 2


def test_every_fmt_renders(tmp_path):
    snap = board.collect(_tree(tmp_path))
    for fmt in ("md", "md-brief", "html", "badge", "json"):
        assert board.render(snap, fmt)


def test_contents_level_only_no_body_text_leaks(tmp_path):
    snap = board.collect(_tree(tmp_path))
    for fmt in ("md", "md-brief", "html", "badge", "json"):
        assert BODY_MARKER not in board.render(snap, fmt)


def test_work_queue_prompts_reference_the_documented_workflow(tmp_path):
    snap = board.collect(_tree(tmp_path))
    html = board.render(snap, "html")
    assert "data-copy=" in html and "cp(this,event)" in html
    assert "reading-queue.md" in html          # file-the-next-paper prompt
    assert "make validate" in html             # every prompt ends at the gate
    assert "/memory demo" in html              # the recall chip
    assert "wiki/CLAUDE.md" in html            # the schema anchor


def test_paper_links_and_issue_actions(tmp_path):
    html = board.render(_snap_with_remote(tmp_path), "html")
    # ref'd paper → its abstract page; bare title → an arXiv title search
    assert "https://arxiv.org/abs/2406.01234" in html
    assert ("https://arxiv.org/search/?searchtype=title&amp;query=Title%20One"
            in html)
    # both prefilled-issue actions, on the repo's own issue tracker
    assert "https://github.com/PyAutoLabs/PyAutoMemory/issues/new?" in html
    assert "labels=queue-read" in html and "labels=queue-intake" in html
    assert "labels=queue-cite" in html
    # a DONE paper renders as history, with no action buttons on its line
    assert "DONE 2026-06-01 — Old Title" in html
    assert "reading history (1)" in html
    # the issue body round-trips the exact queue line for queue_mark_done.py
    from urllib.parse import quote
    assert quote("line: Title Two — 2406.01234", safe="") in html


def test_no_issue_links_without_a_remote(tmp_path):
    """A spawned-template checkout (no remote) renders without dead buttons."""
    html = board.render(board.collect(_tree(tmp_path)), "html")
    assert "issues/new" not in html
    assert "arxiv.org/search" in html  # paper links still work


def test_md_lists_papers(tmp_path):
    md = board.render(_snap_with_remote(tmp_path), "md")
    assert "<details><summary>Demo Papers: 2 waiting, 1 read</summary>" in md
    assert "[Title One](https://arxiv.org/search/" in md
    assert "labels=queue-read" in md and "labels=queue-intake" in md
    assert "labels=queue-cite" in md


def test_md_brief_is_one_line(tmp_path):
    out = board.render(board.collect(_tree(tmp_path)), "md-brief")
    assert "\n" not in out and "pages" in out


def test_badge_shape(tmp_path):
    badge = json.loads(board.render(board.collect(_tree(tmp_path)), "badge"))
    assert badge["schemaVersion"] == 1 and badge["label"] == "knowledge"
    assert "50% cited" in badge["message"]


def test_html_is_self_contained(tmp_path):
    out = board.render(board.collect(_tree(tmp_path)), "html")
    assert out.lstrip().startswith("<!doctype html>")
    assert "src=" not in out and "<link" not in out.lower()
    assert "fetch(" not in out and "XMLHttpRequest" not in out
    stripped = re.sub(r'data-copy="[^"]*"', "", out)
    for m in re.finditer(r"(?:http|https)://", stripped):
        before = stripped[max(0, m.start() - 30):m.start()]
        assert 'href="' in before or "href='" in before, f"non-href URL at {m.start()}"


def test_live_repo_statuses_are_schema_valid():
    """The schema allows stub|drafted|reviewed; anything else is drift."""
    snap = board.collect()
    seen = set()
    for w in snap["wikis"]:
        seen |= set(w["statuses"])
    assert seen <= {"stub", "drafted", "reviewed"}, f"schema-invalid statuses: {seen}"
