#!/usr/bin/env python3
"""Read one batch of public German institutions from the bundled directory."""

import argparse
import csv
import json
from pathlib import Path

DIRECTORY = Path(__file__).resolve().parents[1] / "assets" / "german-public-universities.csv"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state", help="Filter by a two-letter German state code (for example, BY)")
    parser.add_argument("--offset", type=int, default=0, help="Zero-based offset after filtering")
    parser.add_argument("--limit", type=int, default=8, choices=range(1, 26), metavar="1–25")
    args = parser.parse_args()
    if args.offset < 0:
        parser.error("--offset must be zero or greater")

    with DIRECTORY.open(encoding="utf-8", newline="") as handle:
        institutions = list(csv.DictReader(handle))
    if args.state:
        code = args.state.upper()
        if code not in {institution["state_code"] for institution in institutions}:
            parser.error(f"unknown state code: {args.state}")
        institutions = [institution for institution in institutions if institution["state_code"] == code]

    stop = args.offset + args.limit
    fields = ("institution", "state_code", "type", "website")
    batch = [{field: institution[field] for field in fields}
             for institution in institutions[args.offset:stop]]
    print(json.dumps({
        "total": len(institutions),
        "offset": args.offset,
        "next_offset": stop if stop < len(institutions) else None,
        "institutions": batch,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
