# Shortlist English-Taught Masters

An Agent Skill for finding fully English-taught master's programs an applicant qualifies for. It checks official admissions rules against the applicant's degree, grades, and transcript, then produces an Excel shortlist with source citations.

## Install

Download [shortlist-english-masters.zip](shortlist-english-masters.zip) from this repository.

- **ChatGPT**. Open **Plugins → Skills → Create → Upload from your computer** and upload the ZIP. [OpenAI's installation guide](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- **Claude**. Enable **Code execution and file creation** and web search. Open **Customize → Skills → + → Create skill → Upload a skill** and upload the ZIP. [Anthropic's installation guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- **Codex or Claude Code**. Install the [skill folder](shortlist-english-masters/) using the client's local skill directory. The workflow needs web access and the ability to create files. The bundled Excel exporter uses Python 3 and openpyxl.

## Try it

> Use Shortlist English-Taught Masters to find fully English-taught data science master's programs in Germany for winter 2027/28. My tuition limit is €1,500 per semester. Ask me what you need from my transcript before checking eligibility.

Share a redacted transcript or a list of completed modules and credits for programs with subject-credit requirements. The workbook includes verified matches, deadlines, application portals, fees, a 150-word explanation of academic fit for each program, and citations to the governing rules. The skill checkpoints research to disk so it can resume from the last recorded source.

## Source

- [Skill instructions](shortlist-english-masters/SKILL.md)
- [Admissions review guide](shortlist-english-masters/references/admissions-review.md)
- [Checkpoint and workbook format](shortlist-english-masters/references/run-and-workbook.md)
- [Excel exporter](shortlist-english-masters/scripts/shortlist.py)
