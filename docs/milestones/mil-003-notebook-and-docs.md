# MIL-003 Notebook, screenshots, README and wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [MIL-002] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decides whether a reader can follow the nine lecture steps in a notebook, see each step in a screenshot, and read what each step teaches in English, Danish and Bahasa Malaysia, with set-up guides for Windows and Linux.

## Deliverable

A Jupyter notebook that runs top to bottom, nine step screenshots in `docs/images/`, a finished README built from the framework template, and a wiki in `docs/wiki/` in three languages with a Getting Started page that covers Windows and Linux.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `jupyter nbconvert --execute` on the notebook | Exit code 0 | Any error |
| 2 | `docs/images/` holds nine `step-N-*.png` files, each shown in the README and in the wiki | 9 of 9 | A step is missing |
| 3 | The wiki has the same page set in `en`, `da` and `ms`, and a `_Sidebar.md` | Page sets equal | A page is missing in a language |
| 4 | The Getting Started page has a Windows (PowerShell) and a Linux (bash) guide in every language | Both guides present | One missing |
| 5 | The wiki reviewed against `QC-WIKI-001` and the README against `check-readme.sh` | Verdict Go, script exit 0 | No-Go |
| 6 | opengrep scan reports no findings | 0 findings | Any finding |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | The functions the notebook, the screenshots and the wiki use |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] objectives 2, 4 and 5, success criteria 2, 3 and 4 | CN-003, CN-005 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-12 — inside the Business Case constraint.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Build the notebook | A Jupyter notebook that follows the nine lecture steps with the package functions, and runs top to bottom in a fresh `.venv`. | No |  |
| 2 | Generate step screenshots | One script `scripts/make_screenshots.py` renders nine screenshots (`docs/images/step-N-*.png`) from the code, one per lecture step. | No |  |
| 3 | Finish the README | Fill the framework README template: overview, the nine screenshots, requirements, set-up, run, tests, opengrep, links. | No |  |
| 4 | Write the English wiki | Home, Getting Started (Windows and Linux), one page per lecture step with what you gain, Summary, and `_Sidebar.md`. | No |  |
| 5 | Translate the wiki to Danish | The same page set as English, with `-da` suffix and the language line. | No |  |
| 6 | Translate the wiki to Bahasa Malaysia | The same page set as English, with `-ms` suffix and the language line. | No |  |
| 7 | Review the wiki and README | Review against `QC-WIKI-001` and run `check-readme.sh`; record the RC. | No |  |

---

[BC-001]: ../business-case.md
[MIL-002]: ./mil-002-analysis-library.md
