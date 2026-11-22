# Public higher education institutions in Germany

Use the [bundled directory](../assets/german-public-universities.csv) as a discovery queue. It covers 273 public institutions across the 16 German states as of 22 November 2026. It includes universities, universities of applied sciences, arts and music institutions, public administration colleges, and other specialist institutions. The directory includes specialist institutions with restricted entry so nationwide coverage is visible. Inspect their own catalog and admission route when the subject and applicant category are relevant.

## Read a small batch

Run from the skill directory using Python 3 and its standard library.

```text
python3 scripts/directory.py --limit 8
python3 scripts/directory.py --state BY --offset 8 --limit 8
```

For nationwide searches omit `--state`. For a regional search filter by state code. Keep a separate offset for each selected state, because offsets count rows after filtering. Read only the returned batch. If code execution is unavailable, open only the relevant slice of the CSV. For each batch, use institution websites to check official master's catalogs and search for the requested subject and synonyms. In `discovery.md`, record the snapshot date, state filter, next offset, institutions or catalogs already checked, and any unreachable campus or missing catalog. Resume from that offset. A `null` next offset means the matching directory rows have been read.

Run a complementary discovery pass in [DAAD International Programmes](https://www2.daad.de/deutschland/studienangebote/international-programmes/en/) and [Hochschulkompass](https://www.hochschulkompass.de/en/study-in-germany.html). The CSV tracks institutions and website entry points. Degree availability, institutional changes, language, fees and eligibility still need direct official verification. Check the current [Hochschulkompass institution search](https://www.hochschulkompass.de/en/higher-education-institutions.html) with the public ownership filter and confirm any changes with the institution or its state. State the actual coverage and any gaps in the Search Summary.

## Directory sources and attribution

- The institution inventory is adapted from the German Wikipedia contributors' [23 October 2026 revision of Liste der Hochschulen in Deutschland](https://de.wikipedia.org/w/index.php?title=Liste_der_Hochschulen_in_Deutschland&oldid=271561915), which lists provider status. The adaptation keeps public entries, translates category and state labels, and adds independently confirmed entries and website links. The CSV is available under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- Website links start with the official website property (P856) from [Wikidata](https://www.wikidata.org/wiki/Wikidata:Licensing), whose structured data is CC0. The CSV's `website_source` field identifies the source per row. First-party or government sources were used for missing links, recent additions, and corrections to outdated links.
- The scope was cross-checked against the [German Rectors' Conference's Hochschulkompass](https://www.hochschulkompass.de/en/higher-education-institutions.html) and the [2026 HRK statistics for public institutions](https://www.hrk.de/hochschulsystem/hochschulstatistik/). The additions are [Medizinische Universität Lausitz – Carl Thiem](https://mwfk.brandenburg.de/mwfk/de/wissenschaft/medizinische-universitaet-lausitz-carl-thiem/) and [Duale Hochschule Sachsen](https://www.dhsn.de/).
