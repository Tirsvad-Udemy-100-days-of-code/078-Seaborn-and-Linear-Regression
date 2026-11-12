# MIL-002 Analysis library

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [MIL-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Purpose

Decides whether the analysis functions are correct, tested and reviewed against the Python checklist before the notebook and the documentation depend on them.

## Deliverable

The Python package `movie_regression` with data loading and cleaning, the analysis functions for each lecture step, chart functions (bubble chart, regression plot) and a command line entry point, plus a pytest suite that asserts every value of the dataset's analysis.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pytest` passes | All tests pass | Any failure |
| 2 | Tests assert the dataset values (5,391 films, 512 zero domestic, 357 zero worldwide, 155 international-only, 153 old and 5,238 new films) and the regression coefficients | All assertions present and passing | A value is not asserted |
| 3 | Python code reviewed against `QC-PY` and recorded as an RC | Verdict Go | No-Go |
| 4 | opengrep scan reports no findings | 0 findings | Any finding |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | The package, configuration and data it builds on |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] objectives 1 and 3, success criterion 1 | CN-001, CN-004 |

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
| 1 | Implement data loading and cleaning | Read the CSV, answer the shape, NaN, duplicate and dtype questions, strip `$` and `,` from the three money columns in a nested loop and convert `Release_Date` to a datetime. | No |  |
| 2 | Implement descriptive statistics | `describe()` based answers: mean budget and gross, minimums, bottom 25 %, maximums, and the revenue of the cheapest and dearest films. | No |  |
| 3 | Implement zero-revenue functions | Films with zero domestic gross and zero worldwide gross, with the highest-budget flops of each. | No |  |
| 4 | Implement multi-condition filters | International releases (zero domestic, non-zero worldwide) with `.loc[]` and `&`, and the same with `.query()`. | No |  |
| 5 | Implement decade conversion | A `Decade` column from `DatetimeIndex.year` with floor division `//`, and the split into films before 1970 and from 1970. | No |  |
| 6 | Implement bubble and regression charts | Seaborn scatter and bubble charts and `regplot` returning figures so tests and screenshots work without a display. | No |  |
| 7 | Implement scikit-learn regression | Fit `LinearRegression` on budget versus worldwide gross, return intercept, slope and R-squared for old and new films. | No |  |
| 8 | Add command line entry point | `python -m movie_regression` prints the answers of every lecture step. | No |  |
| 9 | Write pytest suite | Assert every dataset value and every function's edge cases. | No |  |
| 10 | Review code against QC-PY | Review `src/` against `qc-programming-python.md` and record the RC. | No |  |

---

[BC-001]: ../business-case.md
[MIL-001]: ./mil-001-foundation.md
