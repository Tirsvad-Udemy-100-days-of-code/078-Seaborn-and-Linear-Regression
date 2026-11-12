# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [WIKI-001], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [f9d4ac3] |

---

## Artifact Under Review

- Instance reviewed: [WIKI-001]
- Checklist used: [QC-WIKI-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none yet; a person who reads Danish and Bahasa Malaysia is needed (criteria 3, 5, 9 are Pending)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Bold title, then one list of the 11 English pages, `Home` first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | All 11 English pages are listed; a script checked that every link target exists. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | No related wikis, so there is no `Related` section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | `Languages` is last: `English: [Home](Home)`, `Dansk: [Hjem](Home-da)`, `Bahasa Melayu: [Utama](Home-ms)`. |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is written by hand, not generated. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page has the language line (criterion 11). |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English, Danish (`da`) and Bahasa Malaysia (`ms`); the registry names `en` as PO language and adds `da` and `ms`. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | 11 English pages, 11 `-da`, 11 `-ms`; a script compared the sets. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | First line of every page, current language in bold, links to the other two; a script checked it. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Files are `<Page>-da.md` and `<Page>-ms.md`; English has no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Code blocks, commands, function names, file names and image URLs are unchanged in da and ms. |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | The published wiki exists only after the merge to main. Checked in the follow-up review record after publication (delta re-review). |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | Optional; no generator is used. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | `docs/wiki/` is flat: 34 Markdown files, no subfolder. |

## Overall Verdict

Go-with-conditions — every checkable Mandatory criterion passes; criterion 14 (check on the published wiki) is Pending until the merge publishes the wiki. A delta re-review closes it. Mode: autonomous, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Check the published wiki (sidebar, pages, links, images) and record a delta re-review for criterion 14 | S01 | 2026-11-12 |

---

[WIKI-001]: ../../wiki/Home.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
[f9d4ac3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn-and-Linear-Regression/commit/f9d4ac3fbb194f0e2879e383fd8fa26b8a281fb5
