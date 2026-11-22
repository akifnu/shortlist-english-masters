#!/usr/bin/env python3
"""Inspect a research checkpoint and export its verified programs to Excel."""

import argparse
from collections import Counter
from datetime import date
import json
import math
import os
from pathlib import Path
import tempfile
from urllib.parse import urlsplit

STATUSES = ("pending", "qualified", "excluded", "unverified")
ELIGIBILITY_TYPES = ("degree", "grade", "credits", "english")
REPORT_TYPES = (
    "instruction", "intake", "deadline", "application", "tuition",
    "semester_fee", "other_fees", "curriculum",
)
RESULTS = ("met", "verified", "procedural", "not_applicable")
PROGRAM_COLUMNS = (
    ("university", "University", 29),
    ("program", "Master's program / track", 39),
    ("country", "Country", 18),
    ("city", "Campus / city", 20),
    ("intake", "Intake semester", 24),
    ("application_status", "Application status", 21),
    ("application_window", "Application window", 30),
    ("deadline", "Application deadline", 33),
    ("tuition", "Tuition", 32),
    ("semester_fee", "Semester contribution", 29),
    ("other_fees", "Other mandatory fees", 31),
    ("program_url", "Program page", 20),
    ("application_url", "Application portal", 21),
    ("extra_application_url", "Additional portal", 21),
    ("admissions_url", "Admission rules", 21),
    ("application_notes", "Application and selection notes", 51),
    ("fit", "Academic fit (150 words)", 85),
)

LINK_LABELS = {
    "program_url": "Open program",
    "application_url": "Open application",
    "extra_application_url": "Open additional portal",
    "admissions_url": "Open admission rules",
}


def read_object(path):
    with path.open(encoding="utf-8") as handle:
        obj = json.load(handle)
    if not isinstance(obj, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return obj


def required_text(obj, keys):
    for key in keys:
        value = obj.get(key)
        if not isinstance(value, str) or not value.strip() or len(value) > 32767:
            raise ValueError(f"{key}: expected nonempty Excel-compatible text")


def check_url(obj, key):
    required_text(obj, (key,))
    url = urlsplit(obj[key])
    if url.scheme not in ("http", "https") or not url.hostname or url.username or url.password:
        raise ValueError(f"{key}: expected a public web link")


def read_run(directory):
    run = read_object(directory / "run.json")
    required_text(run, ("scope", "coverage", "checked_on"))
    if date.fromisoformat(run["checked_on"]).isoformat() != run["checked_on"]:
        raise ValueError("checked_on: expected YYYY-MM-DD")
    for key in ("complete", "allow_closed"):
        if not isinstance(run.get(key), bool):
            raise ValueError(f"{key}: expected true or false")
    return run


def read_programs(directory):
    records = directory / "programs"
    if not records.is_dir():
        raise ValueError("run folder has no programs directory")
    for path in sorted(records.glob("*.json")):
        try:
            record = read_object(path)
            required_text(record, ("university", "program"))
            if record.get("status") not in STATUSES:
                raise ValueError("status: expected pending, qualified, excluded, or unverified")
        except ValueError as exc:
            raise ValueError(f"{path.name}: {exc}") from exc
        yield path.stem, record


def validate_program(record, allow_closed):
    required_text(record, [key for key, _, _ in PROGRAM_COLUMNS if key != "extra_application_url"])
    if record["country"].strip().casefold() != "germany":
        raise ValueError("country: the shortlist covers Germany")
    for key in ("program_url", "application_url", "admissions_url"):
        check_url(record, key)
    if record.get("extra_application_url") is not None:
        check_url(record, "extra_application_url")
    statuses = ("open", "forthcoming", "rolling", "closed") if allow_closed else (
        "open", "forthcoming", "rolling"
    )
    if record["application_status"] not in statuses:
        raise ValueError("application_status: invalid or outside agreed search scope")
    words = len(record["fit"].split())
    if words != 150:
        raise ValueError(f"fit: expected 150 words, got {words}")

    documents = record.get("documents")
    if not isinstance(documents, list) or not documents:
        raise ValueError("documents: expected a nonempty list")
    document_urls = set()
    for doc in documents:
        if not isinstance(doc, dict):
            raise ValueError("documents: expected objects")
        required_text(doc, ("title", "source_scope"))
        check_url(doc, "url")
        document_urls.add(doc["url"])
    for key in LINK_LABELS:
        if record.get(key) and record[key] not in document_urls:
            raise ValueError(f"{key}: link has no matching reviewed document")

    evidence = record.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        raise ValueError("evidence: expected a nonempty list")
    coverage = set()
    for row in evidence:
        if not isinstance(row, dict):
            raise ValueError("evidence: expected objects")
        required_text(row, ("type", "requirement", "assessment", "result", "source_title", "locator"))
        check_url(row, "source_url")
        kind, result = row["type"], row["result"]
        if kind not in ELIGIBILITY_TYPES + REPORT_TYPES + ("other",) or result not in RESULTS:
            raise ValueError(f"evidence: unknown type or result ({kind}, {result})")
        if row["source_url"] not in document_urls:
            raise ValueError(f"evidence: {kind} has no matching reviewed document")
        if kind == "degree" and result == "met":
            coverage.add(kind)
        if kind in ELIGIBILITY_TYPES[1:] and result in ("met", "not_applicable"):
            coverage.add(kind)
        if kind in REPORT_TYPES and result == "verified":
            coverage.add(kind)
    missing = set(ELIGIBILITY_TYPES + REPORT_TYPES) - coverage
    if missing:
        raise ValueError(f"evidence: missing qualifying rows for {', '.join(sorted(missing))}")


def status(directory, limit):
    run = read_run(directory)
    counts = Counter()
    queue = []
    for key, record in read_programs(directory):
        state = record["status"]
        counts[state] += 1
        if state == "pending" and len(queue) < limit:
            queue.append(key)
    print(json.dumps({
        "complete": run["complete"],
        "counts": {state: counts[state] for state in STATUSES},
        "pending": queue,
    }, ensure_ascii=False))


def add_row(sheet, values, links=None):
    # Every value is literal text, including a value beginning with "=".
    from openpyxl.styles import Alignment
    from openpyxl.utils import get_column_letter

    sheet.append(values)
    lines = 1
    for column, cell in enumerate(sheet[sheet.max_row], start=1):
        if cell.value is None:
            continue
        cell.data_type = "s" if isinstance(cell.value, str) else cell.data_type
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        if links and column in links:
            cell.hyperlink = links[column]
            cell.style = "Hyperlink"
        width = sheet.column_dimensions[get_column_letter(column)].width
        lines = max(lines, sum(max(1, math.ceil(len(line) / (width * 0.85)))
                               for line in str(cell.value).splitlines()))
    sheet.row_dimensions[sheet.max_row].height = min(395, max(24, 15 * lines + 8))


def setup_sheet(sheet, columns):
    from openpyxl.styles import Font, PatternFill
    from openpyxl.utils import get_column_letter

    for index, (_, width) in enumerate(columns, start=1):
        sheet.column_dimensions[get_column_letter(index)].width = width
    add_row(sheet, [label for label, _ in columns])
    for cell in sheet[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="18334A")
    sheet.freeze_panes = "C2" if sheet.title == "Shortlist" else "A2"


def export(directory, output):
    from openpyxl import Workbook, load_workbook

    if output.suffix.lower() != ".xlsx":
        raise ValueError("output must end in .xlsx")
    run = read_run(directory)
    counts = Counter()
    qualified = []
    identities = set()
    for key, record in read_programs(directory):
        counts[record["status"]] += 1
        if record["status"] != "qualified":
            continue
        try:
            validate_program(record, run["allow_closed"])
            identity = tuple(" ".join(record[field].casefold().split())
                             for field in ("university", "program", "country", "city", "intake"))
            if identity in identities:
                raise ValueError("duplicate university, program, campus and intake")
            identities.add(identity)
        except ValueError as exc:
            raise ValueError(f"{key}: {exc}") from exc
        qualified.append(record)
    if run["complete"] and counts["pending"]:
        raise ValueError("run is marked complete with pending candidates")

    workbook = Workbook()
    shortlist = workbook.active
    shortlist.title = "Shortlist"
    evidence = workbook.create_sheet("Admissions Evidence")
    documents = workbook.create_sheet("Documents Reviewed")
    summary = workbook.create_sheet("Search Summary")
    setup_sheet(shortlist, [(label, width) for _, label, width in PROGRAM_COLUMNS])
    identity_columns = [
        ("University", 29), ("Master's program / track", 39),
        ("Campus / city", 20), ("Intake semester", 24),
    ]
    setup_sheet(evidence, identity_columns + [
        ("Category", 23),
        ("Official requirement / fact", 58), ("Applicant assessment / finding", 63),
        ("Result", 19), ("Source", 48), ("Section / page / table", 40),
    ])
    setup_sheet(documents, identity_columns + [
        ("Official document", 55), ("Version and coverage reviewed", 90),
    ])
    setup_sheet(summary, [("Item", 30), ("Value", 100)])

    ordered = sorted(qualified, key=lambda record: (record["university"].casefold(),
                                                    record["program"].casefold(), record["intake"]))
    for record in ordered:
        values = []
        links = {}
        for column, (key, _, _) in enumerate(PROGRAM_COLUMNS, start=1):
            value = record.get(key)
            if key in LINK_LABELS and value:
                links[column] = value
                value = LINK_LABELS[key]
            values.append(value)
        add_row(shortlist, values, links)
        identity = [record[field] for field in ("university", "program", "city", "intake")]
        for row in record["evidence"]:
            add_row(evidence, identity + [
                row["type"].replace("_", " ").title(), row["requirement"], row["assessment"],
                row["result"].replace("_", " ").title(), row["source_title"], row["locator"],
            ], {9: row["source_url"]})
        for doc in record["documents"]:
            add_row(documents, identity + [doc["title"], doc["source_scope"]], {5: doc["url"]})

    outcome = "Complete within the stated scope" if run["complete"] else "Partial research"
    if not qualified:
        outcome += ". No confirmed eligible programs to list."
    for label, value in (
        ("Outcome", outcome), ("Search scope", run["scope"]),
        ("Coverage and limits", run["coverage"]), ("Checked on", run["checked_on"]),
        ("Candidates identified", sum(counts.values())),
        ("Confirmed eligible", counts["qualified"]), ("Excluded", counts["excluded"]),
        ("Unverified", counts["unverified"]), ("Pending", counts["pending"]),
    ):
        add_row(summary, [label, value])
    for sheet in (shortlist, evidence, documents):
        sheet.auto_filter.ref = sheet.dimensions

    with tempfile.NamedTemporaryFile(dir=output.parent, suffix=".xlsx", delete=False) as handle:
        temporary = Path(handle.name)
    try:
        workbook.save(temporary)
        saved = load_workbook(temporary)
        try:
            if saved.sheetnames != workbook.sheetnames or saved["Shortlist"].max_row != len(ordered) + 1:
                raise ValueError("workbook failed its reopen check")
        finally:
            saved.close()
        os.replace(temporary, output)
    finally:
        workbook.close()
        temporary.unlink(missing_ok=True)
    print(f"Exported {len(ordered)} confirmed program(s) to {output}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    status_parser = commands.add_parser("status", help="Read a compact progress summary")
    status_parser.add_argument("run", type=Path)
    status_parser.add_argument("--limit", type=int, default=8)
    export_parser = commands.add_parser("export", help="Validate and write the shortlist")
    export_parser.add_argument("run", type=Path)
    export_parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "status":
            status(args.run, max(0, args.limit))
        else:
            export(args.run, args.output)
    except (OSError, ValueError, ImportError) as exc:
        parser.exit(1, f"Error: {exc}\n")


if __name__ == "__main__":
    main()
