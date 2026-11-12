# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [75358c9] |

---

## Purpose

This analysis names the people the Seaborn and linear regression project serves, how much power and interest each has, and what each needs from the result. It uses the power/interest grid and maps concerns to FURPS+ attributes.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant: Product Owner, developer and reviewer | Tirsvad (private) | HIGH | HIGH | Manage Closely | A correct, finished assignment that is worth sharing |
| S02 | Udemy coursists | Fellow participants of the bootcamp | Udemy (public) | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | GitHub (public) | LOW | MEDIUM | Keep Informed | A clear description, topics and README, and no runtime dependencies beyond what is needed |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, accepts every plan and owns the repository.
- **Keep Informed (S02, S03):** cannot change the project but judge its usefulness; they are served by documentation, not by consultation.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | Every lecture step is answered correctly | Functionality |
| CN-002 | S01 | Work follows the plan-first process with traceable reviews | Supportability |
| CN-003 | S02 | Code can be run from the README without guessing, on Windows and on Linux | Usability |
| CN-004 | S02 | Function and library names match the assignment (pandas, Seaborn, scikit-learn) | Usability |
| CN-005 | S03 | The repository explains itself: description, topics, README, wiki | Usability |
| CN-006 | S03 | Few dependencies and no hidden set-up | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Chat with S01 | At plan acceptance and at the end of the run | Plan dry run and run summary | All milestones |
| CR-002 | README and wiki | Each milestone that changes behaviour | Instructions and explanations | MIL-003 |
| CR-003 | Repository description and topics | Once | Public summary for S02 and S03 | MIL-001 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S03 wants no dependencies; the lecture needs Pandas, Matplotlib, Seaborn and scikit-learn | S03, S01 | Only those four are runtime dependencies; the notebook tools are development dependencies |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001, CN-002 | [BC-001] objectives 1 and 3 |
| S02 | CN-003, CN-004 | [BC-001] objectives 2 and 4 |
| S03 | CN-005, CN-006 | [BC-001] objectives 5 and 6 |

## Sign-Off

Accepted by S01 when the plan is accepted in chat; reviewed by the AI as stand-in for S01 (autonomous mode, not independent).

---

[BC-001]: ./business-case.md
[75358c9]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn-and-Linear-Regression/commit/75358c998f55477ee25c074190b930f013dacf95
