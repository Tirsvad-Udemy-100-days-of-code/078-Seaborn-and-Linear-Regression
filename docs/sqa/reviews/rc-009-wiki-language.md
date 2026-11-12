# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [WIKI-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-12 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [WIKI-001]
- Checklist used: [QC-LANG-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none yet; a person who reads Danish and Bahasa Malaysia is needed (criteria 3, 5, 9 are Pending)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | N-A | Wiki pages are documentation without a Metadata table (`framework/process/wiki.md`: no ID); the language is stated by the file name and the language line. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | Codes `da` and `ms` are BCP 47; the registry lists `en`, `da` and `ms` as wiki languages. |
| 3 | The content (prose and table cells) is written in the stated language | Pending | The AI translated the pages; only a person reading Danish and Bahasa Malaysia can confirm them. English read by the AI as author proposal: consistent. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Pages use a technical register for IT readers. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pending | Domain terms (aggregering, spredningsdiagram; pengagregatan, carta serakan) were chosen by the translating AI; a person must confirm them. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Section headings of the English text are translated by design in the wiki; Metadata keys do not exist here. Page file names and IDs stay English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No `<name>.<language>.md` twin; the wiki uses the `-da` and `-ms` file naming that `framework/process/wiki.md` prescribes. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pending | No competent reviewer for da or ms has confirmed the domain terms yet. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out on first use. |

## Overall Verdict

Go-with-conditions — criteria 3, 5 and 9 are Pending: the Danish and Bahasa Malaysia pages were written by the AI and need a person who reads the language. English passes. Mode: autonomous, not independent; a stand-in cannot close these criteria.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Read the Danish pages and confirm or correct them (criteria 3, 5, 9) | S01 | 2026-11-30 |
| Find a reader of Bahasa Malaysia to confirm or correct the `-ms` pages (criteria 3, 5, 9) | S01 | 2026-11-30 |

---

[WIKI-001]: ../../wiki/Home.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
