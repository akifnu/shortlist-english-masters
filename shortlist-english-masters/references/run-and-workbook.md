# Run state and Excel export

## Checkpoint and resume

Create a private run directory with an initially empty `programs/` subdirectory. Use `run.json` for export settings, a small `profile.md` for relevant normalized academic evidence, `discovery.md` for search sources and the next discovery action, and `programs/<id>.json` for each candidate. Use stable slugs and one record per distinct offering. Create candidate records at discovery with status `pending`. Edit one candidate at a time by writing a temporary file next to it, then atomically replacing the JSON file. After each source, record its citation, applicable sections reviewed, extracted rules and next action in that candidate record. Keep findings in compact paraphrases. Use the same pattern for `run.json` and discovery cursor updates.

After context compaction or interruption, reopen the skill, `profile.md`, `run.json` and the tail or cursor of `discovery.md`. Resume institution discovery from the saved directory snapshot, state filter and next offset. Run the status command to see a small batch of pending candidates, then read one record at a time. Resume from its next action and the first unread section. Keep batches to roughly 5–10 discovery leads and 1–3 PDF pages per read when needed. These are working sizes. Continue until all required sections and the defined search scope are covered. Avoid replaying completed browsing output.

Keep the run in the workspace while tools can continue. If a session boundary prevents continuation and the files will disappear, make a private resumable bundle of the compact run files, including only the minimum academic facts needed. Share it with the applicant when resumption requires it. Ask for any redacted original attachments again if they are needed. Update or revalidate decisions when the profile or intake changes.

## JSON contract

Set `complete` to true when the defined search is finished and every candidate has a final research disposition. `unverified` is a final disposition for material details that remain unconfirmed after reasonable follow-up. Save open cases as `pending` until the follow-up is done. Report coverage limits and unresolved cases in aggregate on the workbook summary. Enter any personal details only in the private state. The exporter includes the stated scope and coverage, so describe them without applicant identifiers or excluded program names.

```json
{
  "scope": "Public institutions in Germany, English-taught MSc in data science, winter 2027/28, tuition cap EUR 1,500 per semester",
  "coverage": "Regions, catalogs and official search paths checked, with scope limits",
  "checked_on": "2026-11-22",
  "complete": false,
  "allow_closed": false
}
```

A pending candidate needs `status`, `university`, and `program`. Add `program_url`, a `next_action`, and working evidence as available. For excluded and unverified candidates, retain a short `reason` and the deciding citation or unanswered question. For qualified candidates, populate every required field below. The filename stem is the program ID. Include the track in the program title where applicable.

| Qualified record key | Value |
| --- | --- |
| `status`, `university`, `program`, `country`, `city` | Use `qualified`, official program identity and campus, and `Germany` for country |
| `intake`, `application_status` | Official semester and year, with `open`, `forthcoming`, `rolling` or `closed` |
| `application_window`, `deadline` | Applicant-specific opening/window and final deadline or explicit official rolling policy, including any different steps in notes |
| `program_url`, `application_url`, `admissions_url` | Official program page, responsible portal or application entry, and controlling admissions source URL |
| `tuition`, `semester_fee`, `other_fees` | Applicable amount, currency, basis, and category. State explicit zero or `No other mandatory fee found in the published schedule` after reviewing the schedule. If a schedule or a material charge is unknown, keep the candidate unverified |
| `application_notes` | Applicable route, required steps, second portal if needed, selection and procedural details. Use a useful complete note for a single route too |
| `extra_application_url` | Optional verified additional portal or pre-check URL. Explain its role in application notes |
| `fit` | Exactly 150 whitespace-delimited words in English about curriculum fit. Keep bibliographic details in evidence rows |
| `ordinance_compliance` | Applicant-specific prose in English explaining how the controlling clauses are met. Name and cite the clauses, compare the applicant’s values to thresholds, name the modules and credits that establish every subject minimum, and report any remaining university decision or applicable exception. Use the linked Admissions Evidence rows for full detail |
| `documents` | List of objects with `title`, `url`, `source_scope` (sections/pages reviewed, decision scope, edition or date where available) |
| `evidence` | List of objects with `type`, `requirement`, `assessment`, `result`, `source_title`, `source_url`, `locator` (section/paragraph/page/table/row). Link every source URL to a reviewed document entry by using the same URL |

Use evidence types `degree`, `grade`, `credits`, `english`, `instruction`, `intake`, `deadline`, `application`, `tuition`, `semester_fee`, `other_fees`, `curriculum`, and `other`. Supply at least one row for each of the first twelve types. Use separate rows for each rule within a type. Use `met` for a satisfied eligibility rule, `verified` for corroborated facts, `procedural` for remaining application or selection steps, and `not_applicable` where the reviewed rules establish that a check (such as a distinct credit minimum or specified overall grade threshold) does not apply. For degree, grade, credits and English use `met` or `not_applicable` for substantive eligibility coverage, with `met` required for degree. For instruction, intake, deadline, application, tuition, semester fee, other fees and curriculum, include `verified` coverage.

## Workbook commands

Run with Python 3 and openpyxl. Resolve the script relative to the skill folder and pass absolute run and output paths.

```text
python3 scripts/shortlist.py status RUN_DIR --limit 8
python3 scripts/shortlist.py export RUN_DIR english-taught-masters.xlsx
```

For older checkpoints, add `ordinance_compliance` to each qualified record from its verified rules and applicant evidence before exporting. Use the existing evidence and revisit only any gaps.

The script checks complete records, the presence of written ordinance compliance, linked sources, fit length, presence of applicant-facing evidence, duplicate offerings, and consistency between run state and shortlist. Inspect cited official sources to verify meaning and applicability. Review the workbook after export. In an environment without openpyxl, use the available spreadsheet tools to generate a real .xlsx with the same fields and checks. The four tabs are Shortlist, Admissions Evidence, Documents Reviewed and Search Summary. Identify the program and its campus and intake on both evidence tabs. Give links friendly display text, freeze the header, enable filters, and make the written compliance assessment, academic fit and evidence readable with wrapped text. Keep excluded and unverified cases out of all tabs except anonymous counts in the summary.

If completion is genuinely blocked and a partial export would help, keep `complete` false and name the file accordingly. A valid empty shortlist must distinguish completed review with no confirmed matches from an unfinished search. In the final message report the number of confirmed matches and material coverage limits, and provide the workbook link.
