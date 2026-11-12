# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-013 |
| CrossReference | [PY-001], [QC-PY-001], [RC-007], [RC-010] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Delta review: strict type checking and pinned dependencies | pending |

---

## Artifact Under Review

- Instance reviewed: [PY-001]
- Checklist used: [QC-PY-001]
- Scope: delta review that closes the action items of [RC-007] and [RC-010]: criterion 12 (mypy strict) and criterion 13 (pinned dependencies); the other criteria are unchanged and were re-checked by the 52 passing tests
- Language and domain: n/a
- Language reviewer: none (S01 confirmed criteria 3, 5 and 9 in chat on 2026-11-12)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | snake_case modules and functions, UPPER_SNAKE constants in `domain/rules.py`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`convert_money_to_numbers`, `remove_unreleased`, `international_releases`); names follow the lecture and the pandas, Seaborn and scikit-learn APIs. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check` and `ruff check .` pass; no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every signature is annotated; ruff rules E, F, I, UP, B pass. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No `except` clause in `src/`. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults (rule B006 enabled); no builtin shadowed. |
| 7 | Files, locks and connections are managed with context managers | Pass | File access is done by `pandas.read_csv` and Matplotlib `savefig`; no manual file handles exist. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Public modules and functions have docstrings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | The only `print` is the CLI result in `presentation/cli.py`, which is the program output, not a diagnostic; there is no logging and no secret in output. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No Design Class Diagram exists: the plan has no use cases (all tasks are plain technical tasks, MIL-002 table). The layered module layout is the design, recorded in this review. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 52 pytest tests, named for behaviour, offline, display-free (Agg backend, `Figure` API), independent of order. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `python -m mypy` (strict = true in `pyproject.toml`) reports no issues in 29 files (`src`, `tests`, `scripts`). Four findings were fixed in code (string key in `describe_structure`, float conversion in `build_report`, list for table cells, array access in a test). `sklearn`, `seaborn` and `nbformat` ship no type information and are listed as exceptions in `pyproject.toml`, each with a comment; the one `Any` (`to_decade`) keeps its comment. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Every runtime and dev dependency in `pyproject.toml` is pinned to an exact version (`==`), including `mypy` and `pandas-stubs`; `pip check` finds no broken requirement; none is unused. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Column names, the characters to remove, the data collection date, the 1970 cut-off and the decade rule are defined once in `domain/rules.py`. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `tests/unit/test_architecture.py` parses imports: domain imports no other layer and no library but `datetime`; application imports no infrastructure or presentation; no cycles. The application layer works on pandas DataFrames and scikit-learn, the working types of a data analysis; that is the house style of the 074 project. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Modules are small pure functions with one reason to change each; no type tests or inheritance. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | `domain`, `application`, `infrastructure`, `presentation` under `src/movie_regression/`, and `unit` and `integration` under `tests/`. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | English snake_case names without spaces. |

## Overall Verdict

Go — every criterion passes; the two Optional criteria that failed in [RC-007] and [RC-010] (12, 13) now pass. Mode: autonomous, not independent; S01 may challenge this record.

## Action Items

None open. The action items of [RC-007] and [RC-010] are closed by this record.

---

[PY-001]: ../../../src/movie_regression
[RC-007]: ./rc-007-python-code-mil-002.md
[RC-010]: ./rc-010-python-code-mil-003.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
