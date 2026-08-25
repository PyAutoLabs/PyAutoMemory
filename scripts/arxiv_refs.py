"""scripts/arxiv_refs.py — the arXiv ref grammar, in one place.

A reading-queue / arXiv-inbox paper line is a bare title, optionally followed
by ` — <arXiv id or URL>`. That trailing **ref** is what turns a queue line
into a one-tap paper on the Dashboard: with it the board can link the arXiv
*abstract* page and, next to it, the PDF itself — the whole point being that a
phone can collect the PDFs before a flight without a search-results detour.
Without a ref the board can only offer an arXiv title *search*, which costs a
page load and a tap per paper and never reaches a PDF.

So this module holds two things, and nothing else:

* **The grammar (pure, offline).** Every ref shape the queue has ever carried —
  ``2103.16254``, ``arXiv:2103.16254v2``, ``https://arxiv.org/abs/2103.16254``,
  ``https://arxiv.org/pdf/2103.16254.pdf``, the pre-2007 ``astro-ph/0601001`` —
  normalises to one canonical id, from which :func:`abs_url` and :func:`pdf_url`
  follow. A ref that is not an arXiv paper (a journal DOI, a PDF on a group
  page) stays exactly as written: it is still a link, just not one with a
  derivable PDF sibling.
* **The lookup (networked).** :func:`resolve_title` asks the arXiv API for the
  id of a bare title. It is used only by ``scripts/backfill_arxiv_refs.py``,
  which is what fills in the refs the historical bulk-pasted queue lines never
  had. The board itself never calls it — the board stays fully local, rendered
  from the checkout with no network (see ``scripts/board.py``).

``scripts/board.py`` and ``scripts/inbox_actions.py`` keep their own
``…REF_RE`` line-splitting regexes: those answer "where does the title end",
which is a *line* question. This module answers "what paper is that ref", which
is an *arXiv* question. They are deliberately separate.
"""

from __future__ import annotations

import re
import unicodedata
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ATOM = "{http://www.w3.org/2005/Atom}"

#: Post-2007 identifiers: ``YYMM.NNNNN``, optionally versioned.
NEW_ID = r"\d{4}\.\d{4,5}"
#: Pre-2007 identifiers: ``archive[.subject]/YYMMNNN``, e.g. ``astro-ph/0601001``.
OLD_ID = r"[a-z-]+(?:\.[A-Z]{2})?/\d{7}"

_ID_RE = re.compile(rf"^(?:arxiv:)?({NEW_ID}|{OLD_ID})(?:v\d+)?$", re.I)
_URL_RE = re.compile(
    rf"^https?://(?:www\.)?arxiv\.org/(?:abs|pdf|format|ps)/"
    rf"({NEW_ID}|{OLD_ID})(?:v\d+)?(?:\.pdf)?/?$",
    re.I,
)

ABS_BASE = "https://arxiv.org/abs/"
PDF_BASE = "https://arxiv.org/pdf/"
SEARCH_BASE = "https://arxiv.org/search/?searchtype=title&query="

API_URL = "https://export.arxiv.org/api/query"
#: arXiv asks for one request every few seconds; the backfill honours this.
API_DELAY_SECONDS = 3.0


def arxiv_id(ref: str | None) -> str | None:
    """The canonical, version-stripped arXiv id in `ref`, or None.

    Accepts a bare id, an ``arXiv:``-prefixed id, or any arxiv.org abs/pdf URL.
    Anything else — a DOI, a publisher link, a PDF hosted elsewhere — is not an
    arXiv paper as far as this repo is concerned, and returns None.
    """
    if not ref:
        return None
    ref = ref.strip()
    for pattern in (_ID_RE, _URL_RE):
        m = pattern.match(ref)
        if m:
            return m.group(1).lower() if "/" in m.group(1) else m.group(1)
    return None


def abs_url(ref: str | None) -> str | None:
    """The arXiv abstract page for `ref`, or None when it is not an arXiv id.

    The abstract page — never the PDF — because it is the page that carries the
    authors, the abstract and arXiv's own download links; the direct PDF is
    offered beside it, as its own button.
    """
    aid = arxiv_id(ref)
    return ABS_BASE + aid if aid else None


def pdf_url(ref: str | None) -> str | None:
    """The direct PDF for `ref`, or None when it is not an arXiv id.

    No ``.pdf`` suffix: arXiv serves the extensionless form and phones open it
    in the built-in viewer, from which "save to Files" is one more tap.
    """
    aid = arxiv_id(ref)
    return PDF_BASE + aid if aid else None


def search_url(title: str) -> str:
    """The arXiv title search for `title` — the fallback for a ref-less line.

    Strictly worse than a real ref (a results page, not a paper, and no PDF to
    tap), which is why ``backfill_arxiv_refs.py`` exists to retire it.
    """
    return SEARCH_BASE + urllib.parse.quote(title, safe="")


# --- title matching -----------------------------------------------------------
_PUNCT_RE = re.compile(r"[^a-z0-9]+")


def normalise_title(title: str) -> str:
    """A title reduced to its comparable core: lowercase alphanumerics only.

    arXiv, the digest and a hand-pasted queue line disagree constantly about
    LaTeX (``$z=2.48$``), dashes (``-``/``–``/``—``), accents and double spaces,
    and none of that disagreement is about *which paper it is*. Stripping it all
    lets the backfill demand an exact match on what remains, rather than a fuzzy
    match on what does not — a wrong id is worse than no id, because it links
    the reader confidently to somebody else's paper.
    """
    folded = unicodedata.normalize("NFKD", title)
    folded = "".join(c for c in folded if not unicodedata.combining(c))
    return _PUNCT_RE.sub("", folded.lower())


def _api_query(params: dict) -> bytes:
    url = f"{API_URL}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(
        url, headers={"User-Agent": "PyAutoMemory reading-queue backfill "
                                    "(+https://github.com/PyAutoLabs/PyAutoMemory)"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def parse_api_entries(raw: bytes) -> list[dict]:
    """``[{'id': …, 'title': …}, …]`` from an arXiv Atom response."""
    entries = []
    for entry in ET.fromstring(raw).findall(f"{ATOM}entry"):
        ident = (entry.findtext(f"{ATOM}id") or "").strip()
        title = " ".join((entry.findtext(f"{ATOM}title") or "").split())
        aid = arxiv_id(ident)
        if aid and title:
            entries.append({"id": aid, "title": title})
    return entries


def match_entries(title: str, entries: list[dict]) -> str | None:
    """The id of the one entry whose title matches `title`, or None.

    "One" is literal: a title that normalises onto two different arXiv papers
    (v1 cross-lists, a comment sharing its parent's title, two genuinely
    identically-titled papers) is left for a human. Silence is the safe answer.
    """
    want = normalise_title(title)
    hits = {e["id"] for e in entries if normalise_title(e["title"]) == want}
    return hits.pop() if len(hits) == 1 else None


def resolve_title(title: str, max_results: int = 20,
                  query: object = _api_query) -> str | None:
    """Look `title` up on the arXiv API and return its id, or None.

    Networked — the Dashboard never calls this; only the backfill does.
    `query` is injected so the matching can be tested without arXiv.
    """
    # `ti:"…"` is a phrase search over titles. arXiv's search index chokes on
    # unbalanced quotes and LaTeX, so the phrase is sent as plain words; the
    # exactness comes from match_entries afterwards, never from the query.
    words = re.sub(r'[^\w\s]', " ", title).split()
    if not words:
        return None
    phrase = " ".join(words)
    try:
        raw = query({"search_query": f'ti:"{phrase}"',
                     "start": 0, "max_results": max_results})
    except Exception:
        return None
    return match_entries(title, parse_api_entries(raw))
