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

from urllib.parse import unquote  # noqa: E402

import board  # noqa: E402
import inbox_actions  # noqa: E402
import interests_actions  # noqa: E402

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
        "DONE 2026-06-01 — Old Title\n\n## Other Things\n\nTitle Three\n"
        "Title Four — https://arxiv.org/pdf/2201.00042.pdf\n"
        "__A Sub Heading__\nNOTE — just a remark\n"
        "https://example.org/not-a-paper\n"
        "https://arxiv.org/abs/2202.00099\n")
    (tmp_path / "arxiv-inbox.md").write_text(
        "# arXiv inbox\n\nintro prose\n\n---\n"
        "2026-08-24 — Suggested One — 2608.00001\n"
        "2026-08-24 — Suggested Two\n")
    # Two day batches, oldest first: the board must show only the first.
    (tmp_path / "arxiv-interests.md").write_text(
        "# arXiv interests\n\nintro prose\n\n---\n"
        "last digest: 2026-08-26\n"
        "2026-08-25 — [Demo Papers] Interest One — 2608.10001\n"
        "2026-08-25 — [Nowhere] Interest Two — 2608.10002\n"
        "2026-08-26 — [Demo Papers] Interest Three — 2608.10003\n")
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
    def _paper(kind, title, ref, line, done=False, done_date=None):
        return {"kind": kind, "title": title, "ref": ref, "done": done,
                "done_date": done_date, "line": line}

    assert snap["queue"] == [
        {"section": "Demo Papers", "count": 2, "done": 1, "papers": [
            _paper("paper", "Title One", None, "Title One"),
            _paper("paper", "Title Two", "2406.01234",
                   "Title Two — 2406.01234"),
            _paper("paper", "Old Title", None, "DONE 2026-06-01 — Old Title",
                   done=True, done_date="2026-06-01")]},
        # count is 3, not 6: the heading, the remark and the non-arXiv link are
        # carried in file order but are not queue work.
        {"section": "Other Things", "count": 3, "done": 0, "papers": [
            _paper("paper", "Title Three", None, "Title Three"),
            _paper("paper", "Title Four",
                   "https://arxiv.org/pdf/2201.00042.pdf",
                   "Title Four — https://arxiv.org/pdf/2201.00042.pdf"),
            _paper("subhead", "A Sub Heading", None, "__A Sub Heading__"),
            _paper("note", "just a remark", None, "NOTE — just a remark"),
            _paper("note", "https://example.org/not-a-paper", None,
                   "https://example.org/not-a-paper"),
            # a bare arXiv link IS a paper — the title was just never written,
            # so the id in the line stands in for it
            _paper("paper", "arXiv:2202.00099",
                   "https://arxiv.org/abs/2202.00099",
                   "https://arxiv.org/abs/2202.00099")]}]
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
    assert "data-cmd=" in html  # the shared copy handler's payload hook
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
    # a ref written as a /pdf/ URL still titles onto the abstract page, so
    # every paper row reads the same way
    assert "https://arxiv.org/abs/2201.00042" in html
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


def test_read_trend_from_done_history(tmp_path):
    snap = board.collect(_tree(tmp_path))
    # fixture DONE date is 2026-06-01; pin "now" via the generated stamp
    snap["generated"] = "2026-06-10T00:00:00+00:00"
    trend = board._read_trend(snap)
    assert trend == {"d7": 0, "d30": 1,
                     "weeks": [0, 0, 0, 0, 0, 0, 1, 0]}  # age 9d → bucket 6
    html = board.render(snap, "html")
    assert "0 read last 7d · 1 last 30d" in html
    assert "class='spark'" in html
    assert "1 in the last 30." in board.render(snap, "md")


def test_filter_box_markup(tmp_path):
    html = board.render(board.collect(_tree(tmp_path)), "html")
    assert "id='pfilter'" in html and "function flt(" in html


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
    stripped = re.sub(r'data-cmd="[^"]*"', "", out)
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


def test_html_wears_the_shared_family_theme(tmp_path):
    # The look is the Brain's `board/_theme.py`, not a stylesheet copied in
    # here: the page must carry this board's hero (mark, wordmark, tagline)
    # and its accent, or it has silently fallen out of the family.
    t = board.theme()
    html = board.render(board.collect(_tree(tmp_path)), "html")
    assert t.MARKS[board.BOARD_KEY] in html
    assert t.ORGANS[board.BOARD_KEY]["tagline"] in html
    assert t.ORGANS[board.BOARD_KEY]["ink_dark"] in html
    assert "#58a6ff" not in html  # the old hard-coded GitHub blue


# --- the arXiv inbox ----------------------------------------------------------
def test_inbox_is_collected_with_days_left(tmp_path):
    snap = board.collect(_tree(tmp_path))
    assert [p["title"] for p in snap["inbox"]] == ["Suggested One", "Suggested Two"]
    assert snap["inbox"][0]["ref"] == "2608.00001"
    assert snap["inbox"][1]["ref"] is None
    # dates in the fixture are fixed, so only the invariant is asserted
    assert all(0 <= p["days_left"] <= inbox_actions.INBOX_WINDOW_DAYS
               for p in snap["inbox"])


def test_a_missing_inbox_is_not_an_error(tmp_path):
    root = _tree(tmp_path)
    (root / "arxiv-inbox.md").unlink()
    snap = board.collect(root)
    assert snap["inbox"] == []
    assert "nothing waiting" in board._render_md(snap)
    assert "nothing waiting" in board._render_html(snap)


def test_inbox_papers_carry_all_four_actions(tmp_path):
    snap = _snap_with_remote(tmp_path)
    html = board._render_html(snap)
    for label in ("queue-add", "queue-intake", "queue-cite", "queue-dismiss"):
        assert label in html, label


def test_inbox_actions_name_the_inbox_file_not_the_queue(tmp_path):
    """The workflows branch on `file:` — an inbox tap must say so."""
    snap = _snap_with_remote(tmp_path)
    url = board._queue_issue_url(snap, "Demo Papers", snap["inbox"][0], "add",
                                 source=inbox_actions.INBOX_FILE)
    body = unquote(url)
    assert "file: arxiv-inbox.md" in body
    assert "line: 2026-08-24 — Suggested One — 2608.00001" in body


def test_reading_queue_actions_still_name_the_queue_file(tmp_path):
    snap = _snap_with_remote(tmp_path)
    paper = snap["queue"][0]["papers"][0]
    body = unquote(board._queue_issue_url(snap, "Demo Papers", paper, "read"))
    assert "file: reading-queue.md" in body


def test_inbox_filing_actions_warn_there_is_no_queue_line(tmp_path):
    snap = _snap_with_remote(tmp_path)
    body = unquote(board._queue_issue_url(
        snap, "Demo Papers", snap["inbox"][0], "intake",
        source=inbox_actions.INBOX_FILE))
    assert "NOT in the reading queue yet" in body
    queue_body = unquote(board._queue_issue_url(
        snap, "Demo Papers", snap["queue"][0]["papers"][0], "intake"))
    assert "NOT in the reading queue yet" not in queue_body


def test_inbox_renders_before_the_reading_queue(tmp_path):
    """The inbox is the thing to act on; it sits above the backlog."""
    snap = _snap_with_remote(tmp_path)
    for text in (board._render_md(snap), board._render_html(snap)):
        assert text.index("arXiv inbox") < text.index("Reading queue")


# --- the inbox's freshness line -----------------------------------------------
# The point of the stamp is that an EMPTY inbox stops being ambiguous. These
# cover the three empty states (quiet / never run / suspect) plus the populated
# one, on both renderers.
def _inbox(tmp_path, stamp=None, papers=()):
    # A fresh subdirectory per call: _tree() builds the tree with mkdir() and
    # cannot be re-run over one it already made.
    base = tmp_path / f"t{len(list(tmp_path.iterdir()))}"
    base.mkdir()
    root = _tree(base)
    text = "# arXiv inbox\n\nintro prose\n\n---\n" + "".join(
        f"{line}\n" for line in papers)
    if stamp:
        text = inbox_actions.set_last_digest(text, stamp)
    (root / "arxiv-inbox.md").write_text(text)
    # The page carries two stamped tiers; blank the other one so these assert
    # about the inbox's freshness and not the interests list's.
    (root / "arxiv-interests.md").write_text(
        "# arXiv interests\n\nintro prose\n\n---\n")
    snap = board.collect(root)
    snap["owner"], snap["repo"] = "PyAutoLabs", "PyAutoMemory"
    snap["generated"] = "2026-08-25T09:00:00+00:00"
    return snap


def test_the_stamp_is_collected(tmp_path):
    assert _inbox(tmp_path, "2026-08-24")["inbox_last_digest"] == "2026-08-24"
    assert _inbox(tmp_path)["inbox_last_digest"] is None


def test_a_quiet_day_says_the_digest_ran(tmp_path):
    """The state the old wording could not distinguish from a broken run."""
    md = board._render_md(_inbox(tmp_path, "2026-08-25"))
    assert "the last digest ran 2026-08-25 and found nothing" in md
    assert "⚠" not in md


def test_a_stale_inbox_says_the_filing_may_be_broken(tmp_path):
    for render in (board._render_md, board._render_html):
        out = render(_inbox(tmp_path, "2026-08-19"))
        assert "no digest since 2026-08-19" in out
        assert "the nightly filing may be broken" in out


def test_a_never_run_inbox_does_not_cry_wolf(tmp_path):
    """spawn.py ships the template with an empty inbox and no stamp."""
    for render in (board._render_md, board._render_html):
        out = render(_inbox(tmp_path))
        assert "no run recorded yet" in out
        assert "may be broken" not in out


def test_a_populated_inbox_still_carries_the_date(tmp_path):
    snap = _inbox(tmp_path, "2026-08-25", ["2026-08-25 — One — 2608.00001"])
    assert "last digest 2026-08-25" in board._render_md(snap)
    assert "last digest 2026-08-25" in board._render_html(snap)


# --- the client-side contract -------------------------------------------------
# knowledge_board.yml republishes on pushes to arxiv-inbox.md, which is what
# stops happening when filing breaks — so the published page freezes and a
# render-time warning could never fire. The date is rendered; the verdict is
# recomputed in the browser. These tests pin the handshake between the two.
def test_the_html_hands_the_browser_what_it_needs(tmp_path):
    html = board._render_html(_inbox(tmp_path, "2026-08-25"))
    assert "data-last-digest='2026-08-25'" in html
    assert (f"data-stale-weekdays='{inbox_actions.INBOX_STALE_WEEKDAYS}'"
            in html)
    assert "{n}" in html, "the warning template must keep its placeholder"
    assert "freshness()" in html


def test_a_page_rendered_while_stale_warns_without_js(tmp_path):
    html = board._render_html(_inbox(tmp_path, "2026-08-19"))
    assert "class='meta stale fresh'" in html


def test_an_unstamped_inbox_hands_the_browser_nothing_to_check(tmp_path):
    # The attribute-with-value form: the script's own selector text mentions
    # the bare attribute name and is always present.
    assert "data-last-digest='" not in board._render_html(_inbox(tmp_path))


def test_a_reffed_paper_carries_a_one_tap_pdf_button(tmp_path):
    """The 📄 button: the PDF itself, no search and no abstract page first.

    The reason the queue wants refs at all — a phone collecting a stack of
    papers before a flight taps once per paper, not three times.
    """
    snap = _snap_with_remote(tmp_path)
    html = board.render(snap, "html")
    md = board.render(snap, "md")
    for fmt in (html, md):
        assert "https://arxiv.org/pdf/2406.01234" in fmt   # bare-id ref
        assert "https://arxiv.org/pdf/2201.00042" in fmt   # /pdf/ URL ref
        assert "https://arxiv.org/pdf/2608.00001" in fmt   # inbox paper
    # it opens away from the board, so collecting a stack does not lose the page
    assert "class='act pdf'" in html and "rel='noopener'" in html


def test_no_pdf_button_where_there_is_no_ref(tmp_path):
    """A button that cannot work is never rendered — a search is not a PDF."""
    snap = _snap_with_remote(tmp_path)
    for fmt in ("html", "md"):
        out = board.render(snap, fmt)
        # Title One / Title Three / Suggested Two are ref-less, and the
        # heading and the two annotations are not papers at all; the only PDF
        # links on the page belong to the six papers that carry a ref — four
        # in the queue and inbox, plus the current interests batch's two.
        assert out.count("arxiv.org/pdf/") == 6
    bare = {"title": "Title One", "ref": None}
    assert board.paper_pdf_url(bare) == ""
    # a non-arXiv ref is still a link, but there is no PDF to derive from it
    assert board.paper_url({"title": "T", "ref": "https://doi.org/10.1/x"}) == \
        "https://doi.org/10.1/x"
    assert board.paper_pdf_url({"title": "T", "ref": "https://doi.org/10.1/x"}) == ""


def test_headings_and_notes_render_as_themselves_not_as_papers(tmp_path):
    """A `__Bold__` grouping and a `NOTE ` annotation are structure, not work.

    Before line kinds the board rendered both as papers: a search link, three
    issue buttons and a slot in the "N waiting" count, for a line that is a
    heading or a remark.
    """
    snap = _snap_with_remote(tmp_path)
    html = board.render(snap, "html")
    md = board.render(snap, "md")

    assert "<li class='subhead'>A Sub Heading</li>" in html
    assert "- **A Sub Heading**" in md
    assert "just a remark" in html and "- _just a remark_" in md

    # neither carries a paper's buttons
    for fragment in ("A Sub Heading", "just a remark"):
        i = html.index(fragment)
        assert "class='act'" not in html[i:html.index("</li>", i)]
        assert "issues/new" not in html[i:html.index("</li>", i)]

    # and neither inflates the count: 3 papers waiting in Other Things, not 6
    other = next(q for q in snap["queue"] if q["section"] == "Other Things")
    assert other["count"] == 3
    assert "Other Things: 3 waiting" in md


def test_a_bare_link_is_a_paper_only_when_it_points_at_arxiv(tmp_path):
    snap = _snap_with_remote(tmp_path)
    html = board.render(snap, "html")
    # the arXiv one becomes a real paper, labelled by its id, with a PDF button
    assert "arXiv:2202.00099" in html
    assert "https://arxiv.org/pdf/2202.00099" in html
    # the other stays an annotation: still clickable, but no paper buttons,
    # and labelled by host rather than a wall of URL
    assert "<li class='note'><a href=\"https://example.org/not-a-paper\"" in html
    assert "example.org →" in html
    i = html.index("example.org →")
    assert "issues/new" not in html[i:html.index("</li>", i)]


# --- the arXiv interests list -------------------------------------------------
# The sibling suggestion tier. What is tested here is only what makes it
# DIFFERENT from the inbox: it is a backlog of day batches with the oldest one
# current, the 🧹 button clears that whole day, and its papers route by their
# own topic rather than to one section. The per-paper actions themselves are
# the inbox's, already covered above.
def _interests(tmp_path, lines, stamp=None):
    base = tmp_path / f"t{len(list(tmp_path.iterdir()))}"
    base.mkdir()
    root = _tree(base)
    text = "# arXiv interests\n\nintro prose\n\n---\n" + "".join(
        f"{line}\n" for line in lines)
    if stamp:
        text = inbox_actions.set_last_digest(text, stamp)
    (root / "arxiv-interests.md").write_text(text)
    (root / "arxiv-inbox.md").write_text(
        "# arXiv inbox\n\nintro prose\n\n---\n")
    snap = board.collect(root)
    snap["owner"], snap["repo"] = "PyAutoLabs", "PyAutoMemory"
    return snap


def test_only_the_oldest_batch_is_collected(tmp_path):
    snap = _snap_with_remote(tmp_path)
    assert snap["interests_date"] == "2026-08-25"
    assert [p["title"] for p in snap["interests"]] == ["Interest One",
                                                       "Interest Two"]
    assert snap["interests_batches"] == 2
    assert snap["interests_backlog"] == 3


def test_a_missing_interests_file_is_not_an_error(tmp_path):
    root = _tree(tmp_path)
    (root / "arxiv-interests.md").unlink()
    snap = board.collect(root)
    assert snap["interests"] == []
    assert snap["interests_date"] is None
    for fmt in ("md", "html", "json", "badge", "md-brief"):
        board.render({**snap, "owner": "o", "repo": "r"}, fmt)


def test_interests_papers_carry_the_same_five_actions(tmp_path):
    snap = _snap_with_remote(tmp_path)
    html = board._render_html(snap)
    for label in ("interests-add", "queue-intake", "queue-cite",
                  "interests-dismiss"):
        assert label in html, label
    assert "arxiv.org/pdf/2608.10001" in html


def test_interests_actions_name_the_interests_file(tmp_path):
    snap = _snap_with_remote(tmp_path)
    body = unquote(board._queue_issue_url(
        snap, "Demo Papers", snap["interests"][0], "add",
        source=interests_actions.INTERESTS_FILE))
    assert "file: arxiv-interests.md" in body
    assert "line: 2026-08-25 — [Demo Papers] Interest One — 2608.10001" in body


def test_interests_filing_actions_warn_there_is_no_queue_line(tmp_path):
    snap = _snap_with_remote(tmp_path)
    body = unquote(board._queue_issue_url(
        snap, "Demo Papers", snap["interests"][0], "intake",
        source=interests_actions.INTERESTS_FILE))
    assert "NOT in the reading queue yet" in body
    assert "arxiv-interests.md" in body
    assert "arxiv-inbox.md" not in body


def test_a_paper_routes_to_its_own_topic(tmp_path):
    snap = _snap_with_remote(tmp_path)
    assert snap["interests"][0]["section"] == "Demo Papers"
    body = unquote(board._queue_issue_url(
        snap, snap["interests"][0]["section"], snap["interests"][0], "add",
        source=interests_actions.INTERESTS_FILE))
    assert "section: Demo Papers" in body


def test_a_topicless_paper_falls_back_rather_than_stranding(tmp_path):
    snap = _interests(tmp_path, ["2026-08-25 — No topic here — 2608.10001"])
    assert snap["interests"][0]["section"] == interests_actions.FALLBACK_SECTION


def test_the_clear_button_names_the_batch_date(tmp_path):
    snap = _snap_with_remote(tmp_path)
    html = board._render_html(snap)
    assert "interests-clear" in html
    url = board._interests_clear_url(snap, "2026-08-25", 2)
    body = unquote(url)
    assert "file: arxiv-interests.md" in body
    assert "date: 2026-08-25" in body
    # A batch clear is not a per-paper action: it must not carry a line.
    assert "line:" not in body


def test_no_clear_button_without_a_remote(tmp_path):
    snap = board.collect(_tree(tmp_path))
    assert board._interests_clear_url(snap, "2026-08-25", 2) == ""
    assert "interests-clear" not in board.render(snap, "html")


def test_interests_render_between_the_inbox_and_the_queue(tmp_path):
    """The human asked for it under strong lensing: inbox, then this, then
    the backlog it feeds."""
    snap = _snap_with_remote(tmp_path)
    for text in (board._render_md(snap), board._render_html(snap)):
        assert text.index("arXiv inbox") < text.index("arXiv interests")
        assert text.index("arXiv interests") < text.index("Reading queue")


def test_the_backlog_depth_is_on_the_page(tmp_path):
    """A day cleared is a day revealed — the human needs to know how many are
    behind the one they are looking at."""
    snap = _snap_with_remote(tmp_path)
    assert "1 more day behind it" in board._render_html(snap)
    assert "2 days of backlog" in board._render_html(snap)
    assert "1 more day behind it" in board._render_md(snap)


def test_an_empty_interests_list_says_which_kind_of_empty(tmp_path):
    quiet = _interests(tmp_path, [], stamp="2026-08-26")
    assert "the last digest ran 2026-08-26" in board._render_md(quiet)
    never = _interests(tmp_path, [])
    assert "no run recorded yet" in board._render_md(never)


def test_the_two_tiers_carry_their_own_stamps(tmp_path):
    """One digest can break while the other keeps running; the page must not
    report the healthy one's date for the broken one."""
    snap = _snap_with_remote(tmp_path)
    snap["inbox_last_digest"] = "2026-08-27"
    snap["interests_last_digest"] = "2026-08-20"
    html = board._render_html(snap)
    assert "data-last-digest='2026-08-27'" in html
    assert "data-last-digest='2026-08-20'" in html

