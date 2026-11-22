---
name: shortlist-english-masters
description: Finds fully English-taught master's programs at public German universities and delivers a cited Excel shortlist of verified eligible programs. Use for master's program searches or eligibility checks that require reviewing official admission ordinances, prerequisite courses and credit minima, intake, fees, deadlines, and application portals against the applicant's academic record.
---

# Shortlist English-Taught Master's Programs in Germany

## 1. Get the applicant profile

Respond in English. Limit research to public higher education institutions in Germany. Use the information the applicant has already given, including any attached transcript. If their request supplies enough to start, begin research.

**Ask one short question at a time.** Pick the missing detail that matters next. Wait for the answer before asking another question. If the answer covers several details, record them and skip those questions. Use the checklist below privately. Open with the question or one brief lead-in.

In ChatGPT Work, prefer `request_user_input_async` when available. Use the native `ask_user_input` widget for choice questions if that is the interactive option your client provides. Send one question per prompt. For a short set of choices, provide two to four clear answers and allow a custom answer. Use a free-text field for answers such as a subject or grade when supported. Otherwise ask one plain chat question. Follow the tool's wait or end-of-turn behavior. Treat an answer as selected only after the applicant submits it. In other clients, use the same one-question flow in chat unless interactive input is available.

Use natural questions such as “Which semester would you like to start?” with **Winter**, **Summer**, and **Either**, followed by a question about the year if needed. Ask “What did you study for your bachelor's degree?” for the subject, or “What's your tuition limit per semester?” with a short example if it helps. If the user says “not sure” or prefers to skip, record that answer. Start any research the known information supports and defer unresolved eligibility decisions until the evidence is available.

- Get the bachelor's subject and degree title, awarding country and institution, completed or expected completion date, and cumulative grade with its scale and direction. Ask for the best possible and lowest passing grade if conversion might be required.
- Ask for a redacted transcript or a module list with credits, credit system, completion status, and grades where available. A summary is enough to begin. At the point of asking, remind the user to remove names, student numbers, addresses, and document identifiers. Request module descriptions only when a specific rule requires them.
- Get the target intake and academic year, plus the preferred master's fields or tracks. Use any supplied German state, city, or program filter. Search nationwide by default.
- Get the tuition budget, currency and period, whether it is a hard cap, and whether it includes compulsory fees. Ask for the applicant's fee category when it can change the result. Ask what English proof or exemption they have, and follow up for test details when applicable.

## 2. Discover and verify one program at a time

Read [the directory guide](references/german-university-directory.md) and [the run guide](references/run-and-workbook.md) to start. Read [the admissions review guide](references/admissions-review.md) before verifying candidates.

1. Record the search scope, term, preferences and minimal academic profile in a local run folder. Start from the bundled [directory of public German institutions](assets/german-public-universities.csv). Scan its official websites in small batches and use DAAD and Hochschulkompass for a complementary discovery pass. Add each candidate once per university, degree/track, campus and intake. Save the directory batch offset and discovery coverage after each batch.
2. Use the available browser to open each program's official pages one by one and follow their links to governing documents. If an interactive browser is unavailable, use web tools that fetch full pages and PDFs. Check the official program, admissions rules and ordinances, relevant annexes and amendments, language of instruction, tuition and compulsory fees, intake dates, deadlines, and actual application route. Inspect each complete applicable admissions source in manageable sections and record precise citations. Search snippets and directory summaries are discovery aids.
3. Compare each mandatory rule against the applicant's evidence. Confirm an entirely English-taught path through all compulsory parts of the degree. Include a candidate only when all verifiable eligibility requirements and hard filters are supported and the application and fee details are complete. Distinguish routine application steps and competitive selection from missing qualifications. Save the decision and concise evidence after each source or candidate. Mark unmet criteria privately as excluded and unresolved criteria as unverified.
4. Continue through the agreed scope. When a missing applicant fact could unlock plausible candidates, ask one targeted follow-up and continue verifying independent candidates when the client can do so while waiting. Before concluding, chase material gaps through official sources, close out each reviewed case, and record what the search covered and any limits.

## 3. Produce the workbook

- Export one Excel workbook with the qualified shortlist, rule-by-rule admissions evidence, governing documents reviewed, and a search summary. Include official program and direct application links, term and applicable deadlines, tuition and compulsory fees, and exactly 150 words per program explaining where the applicant's studies align with the curriculum. Cite the specific curriculum used and ground every academic claim in the applicant's record.
- Run the bundled exporter and reopen the workbook to verify the shortlist, links, and evidence. When the completed review yields no confirmed matches, return the same workbook with an empty shortlist and a plain explanation on the summary tab. Never include the names of excluded or unverified candidates in the workbook.
- Keep source excerpts, transcripts, the full queue, and resolved candidates out of working context. Carry forward only the current program, a small pending batch, and open evidence questions. Resume from disk after context compaction. If the environment must stop before the defined scope is finished, label any export partial and preserve the checkpoint for resumption.
