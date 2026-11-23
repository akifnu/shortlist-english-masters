# Shortlist English-Taught Masters in Germany

Find fully English-taught master's programs you qualify for at public higher education institutions in Germany. The workflow checks your transcript against official admissions rules, including course prerequisites and minimum credits, and turns verified matches into a cited Excel workbook.

## Choose your setup

| Where you use it | Start here |
| --- | --- |
| **Free ChatGPT** or regular ChatGPT chat | [Open or save the starter prompt (.txt)][starter]. Paste it into a new chat. |
| **ChatGPT Work** with skill uploads enabled | [Download the installable skill (.zip)][skill]. Import it under **Plugins → Skills**. |
| **Claude** | [Download the installable skill (.zip)][skill]. Import it under **Customize → Skills**. |

### Free ChatGPT

1. [Open the starter prompt][starter], copy its text, and paste it into a new ChatGPT chat. You can also save the text file and attach it with the message “Follow the attached instructions and start by asking me for my profile.”
2. Answer each short question as it comes up. You can also give several details in one reply, or attach a redacted transcript. The workflow uses what you already shared.
3. Ask ChatGPT to browse the universities' official sites and return a downloadable **Excel (.xlsx)** file. Choose a specific field and intake. Add a German state or city if you want to narrow the search.
4. If you run into a usage limit, save the latest checkpoint. Paste it along with the starter into a new chat to resume when the required tools are available. If file creation is unavailable, ask for separate copyable tables to put into an Excel workbook.

Web search, uploads, and data analysis are available on Free with usage limits. The starter runs as instructions in a regular chat. [ChatGPT Free Tier FAQ][free-help]

### ChatGPT Work

1. [Download the skill ZIP][skill] and keep it zipped.
2. In ChatGPT, open **Plugins → Skills**, select **Create → Upload from your computer**, and select the ZIP.
3. Open a new Work chat and use the example request below. The skill asks one short question at a time and presents selectable answers when the interface supports them. You can type your own answer, paste a module list, or attach a redacted transcript when asked.

Skill uploads depend on your plan and workspace settings. If the upload option is unavailable, paste the [starter prompt][starter] into Work and use the same request. [ChatGPT Skills guide][skills-help] · [Creating spreadsheets in Work][work-help]

### Claude

1. [Download the skill ZIP][skill] and keep it zipped.
2. In Claude, enable **Code execution and file creation** and turn on **Web search**.
3. Go to **Customize → Skills**, select **+ → Create skill → Upload a skill**, and upload the ZIP.
4. Start a new chat, ask Claude to use **Shortlist English-Taught Masters in Germany**, and provide your academic profile when prompted. Ask for a downloadable **Excel (.xlsx)** workbook.

If custom skill uploads are unavailable in your workspace, paste the [starter prompt][starter] into a Claude chat. [Claude Skills guide][claude-help] · [Claude web search guide][claude-search]

## German public university directory

[Download the directory of 273 public institutions (.csv)][directory] or [view it on GitHub](shortlist-english-masters/assets/german-public-universities.csv). The directory covers all 16 states and includes the official website and institution type for each entry. It includes universities of applied sciences, art and music schools, and specialist public institutions alongside traditional universities.

The ZIP includes the directory and reads it in small batches. For a regular chat, the starter links to the CSV. Attach it if the chat cannot open the link. The directory is a starting point for finding programs. Each shortlisted program still requires current admissions, teaching language, fee, and application checks. [Directory sources and coverage](shortlist-english-masters/references/german-university-directory.md)

## Example request

> Use Shortlist English-Taught Masters to find fully English-taught data science master's programs at public universities in Germany for winter 2027/28. My tuition cap is €1,500 per semester, excluding semester contributions. Ask me one short question at a time for any missing details. Browse official university sources and give me a downloadable Excel workbook.

Share course names, credits, grades and, when needed, module descriptions. Remove your name, student number, address, and document identifiers from any transcript you share.

## What the workbook includes

| Tab | Contents |
| --- | --- |
| **Shortlist** | Verified eligible programs, official program and application links, intake, application window and deadline, tuition and mandatory fees, a 150-word explanation of academic fit per program, and a separate written ordinance compliance assessment that maps completed modules and credits to the exact admission clauses. |
| **Admissions Evidence** | Individual requirements and the applicant's evidence for each, with links and page or section citations. |
| **Documents Reviewed** | The official ordinances, appendices, application guides, and fee sources used for the shortlisted programs. |
| **Search Summary** | The search scope, date, coverage limits, and counts. Excluded and unverified programs appear only in the counts. |

The installed skill saves progress after reviewing each source. If the chat or session must end, retain the latest checkpoint so you can resume without repeating completed reviews.

## Source files

- [Skill instructions](shortlist-english-masters/SKILL.md)
- [Admissions review guide](shortlist-english-masters/references/admissions-review.md)
- [Checkpoint and workbook format](shortlist-english-masters/references/run-and-workbook.md)
- [Excel exporter](shortlist-english-masters/scripts/shortlist.py)

Codex and Claude Code users can install the [skill folder](shortlist-english-masters/) in their client's local skill directory. The workflow uses web access and file creation. The bundled exporter requires Python 3 and openpyxl.

[directory]: https://raw.githubusercontent.com/akifnu/shortlist-english-masters/main/shortlist-english-masters/assets/german-public-universities.csv
[starter]: https://raw.githubusercontent.com/akifnu/shortlist-english-masters/main/chatgpt-free-starter.txt
[skill]: https://raw.githubusercontent.com/akifnu/shortlist-english-masters/main/shortlist-english-masters.zip
[free-help]: https://help.openai.com/en/articles/9275245-chatgpt-free-tier-faq
[skills-help]: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
[work-help]: https://help.openai.com/en/articles/20001278-creating-and-editing-documents-spreadsheets-and-presentations-with-chatgpt-work
[claude-help]: https://support.claude.com/en/articles/12512180-use-skills-in-claude
[claude-search]: https://support.claude.com/en/articles/10684626-enable-and-use-web-search
