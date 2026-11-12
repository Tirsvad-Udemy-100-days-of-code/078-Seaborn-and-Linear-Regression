# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Executive Summary

This project turns the Day 78 assignment of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp" (Seaborn and linear regression on movie budget and revenue data) into a readable, runnable Python repository. It delivers a tested Python package that answers the questions of the nine lecture steps, a Jupyter notebook that follows them, a README and a three-language wiki (English, Danish, Bahasa Malaysia) with one screenshot per lecture step. The project proceeds because it is small, has a fixed source, and serves both the course participant and the people who compare solutions.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/`: artifacts are reviewed against their QC checklists, and quality criteria are tagged with ISO/IEC 25010:2023 characteristics. Domain modelling follows Larman's *Applying UML and Patterns* where a design artifact is needed. Source code follows the Python conventions of the `coding-conventions` skill and the layering of the `clean-architecture` skill.

## Problem Statement

The assignment ships as a single notebook with unstructured cells and no tests. A participant who wants to keep the work, share it or compare it with others has no runnable repository, no installation instructions, no explanation of what each step teaches, and no evidence that the answers are correct.

## Business Opportunity

A clean repository makes the solution reusable as a reference for other course participants and as a portfolio piece, and it records what was learned in each lecture step in three languages. The question it answers is a real one: do higher film budgets lead to more revenue at the box office?

## Objectives

1. Answer the questions of the lecture steps (explore and clean, zero-revenue films, international releases, bubble chart, decades by floor division, regression plot, scikit-learn regression) with functions in a Python package.
2. Provide a Jupyter notebook that reproduces every lecture step, including the charts.
3. Provide automated tests that check each answer against the dataset.
4. Provide a README with set-up, run and test instructions, and a wiki in English, Danish and Bahasa Malaysia that explains what each lecture step teaches, with a Getting Started page for both Windows and Linux.
5. Provide one screenshot per lecture step in the README and the wiki.
6. Publish the repository with a description and topics.

## Scope

### In Scope

- The nine Day 78 lecture steps: goals, explore and clean the data, films with zero revenue, filtering on multiple conditions, Seaborn bubble charts, floor division to convert years to decades, regression plots with Seaborn, regression with scikit-learn, and the summary.
- A Python package under `src/`, tests under `tests/`, the notebook and the dataset supplied with the lecture.
- `pyproject.toml`, a Python `.gitignore`, a `.venv` set-up guide, README and wiki.
- A local scan with opengrep before every push.

### Out of Scope

- Other days of the bootcamp.
- A web or desktop user interface.
- Updating the dataset beyond the snapshot supplied with the lecture.
- Hosting the notebook in Google Colab.

## Expected Benefits

### Tangible Benefits

- A repository that runs with three commands and passes its tests.
- Nine step screenshots and a three-language wiki that can be reused for later days.

### Intangible Benefits

- Understanding of data cleaning, boolean filtering, Seaborn charts and linear regression.
- A pattern for turning a course notebook into tested code.

## Strategic Alignment

The project supports the course participant's goal of completing the bootcamp with work that is worth sharing, and it practises the framework's plan-first workflow on a small project.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Lecture questions answered | Values equal the data's: 5,391 films, 512 with zero domestic gross, 357 with zero worldwide gross, 155 international-only releases, 153 films before 1970 and 5,238 from 1970 | automated tests pass |
| 2 | Notebook runs | 100 % of cells execute without error from a fresh `.venv` | `jupyter nbconvert --execute` exits 0 |
| 3 | Documentation languages | 3 of 3 wiki languages with the same page set | file listing of `docs/wiki/` |
| 4 | Screenshots | 9 of 9 lecture steps have a screenshot in the README and the wiki | file listing of `docs/images/` |
| 5 | Security scan | 0 findings from opengrep before each push | opengrep exit code |
| 6 | Runtime dependencies | at most 4 (pandas, matplotlib, seaborn, scikit-learn) | `pyproject.toml` |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The dataset licence or the course material licence forbids republishing | The repository must be private or the data removed | The data is the small CSV supplied with the lecture; the README names the source and states it belongs to the course |
| A lecture value differs from the computed value because of a different library version | A test fails | Tests assert exact values from the supplied snapshot; `pyproject.toml` pins a minimum version only |
| Screenshots drift from the code | The documentation misleads | One script regenerates all screenshots from the code |
| A token leaks into the repository | Account compromise | `.env` is ignored by git, is never read by the project code and is never printed |

## Assumptions

- S01 is the Product Owner (PO), developer and reviewer; the AI acts as stand-in reviewer in autonomous mode.
- The dataset supplied with the lecture is the only data source.
- Python 3.13 is installed on the machine of S01.

## Constraints

- Target completion: 2026-11-12 (one working day plus review).
- Python 3.13 or newer, a local `.venv`, configuration in `pyproject.toml`.
- Folder structure `src/`, `tests/`, `docs/`.
- One branch and one pull request per milestone.
- Runtime dependencies only where needed; the notebook tools are development dependencies.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About one working day of effort by S01 with AI assistance; no licence or hosting cost | A shareable, tested reference solution and a three-language explanation; the justification is qualitative because the project has no revenue |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Completes the assignment and owns the result |
| S02 | Runs and compares the code |
| S03 | Browses the repository for ideas |

## Recommendation

Proceed — the scope is small, the data is available and the result serves all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
