# AI Agent Empowering Full-Chain Training for "Economics Research Paper Writing" — Digital-Intelligence Teaching Practice for New Liberal Arts

[中文](./README.md)

10 structured case studies demonstrating how AI agents can assist social science research workflows — from theoretical modeling and data collection to empirical analysis and academic writing.

---

## Contributors

**School of Economics, Jinan University**

- **Bin Wang** — [Bilibili](https://space.bilibili.com/321279199)
- **Yutao Wang**

Copyright 2024 School of Economics, Jinan University. Bin Wang, Yutao Wang. All rights reserved.

---

## Video Tutorials

> Case teaching videos are being continuously updated

| Content | Link |
|---------|------|
| Introduction | [BV1VLoCBHE4A](https://www.bilibili.com/video/BV1VLoCBHE4A/) |
| Installation | [BV11aoCBzEqJ](https://www.bilibili.com/video/BV11aoCBzEqJ/) |
| Case 1: Initial Model | [BV11aoCBzECc](https://www.bilibili.com/video/BV11aoCBzECc) |
| Case 2: Theoretical Extension | [BV1yz9SB7E9Z](https://www.bilibili.com/video/BV1yz9SB7E9Z/) |
| Case 3: Financial Data | [BV14aRhBPEF7](https://www.bilibili.com/video/BV14aRhBPEF7/) |
| Case 4: ESG Panel | [BV1xaRhBPEkY](https://www.bilibili.com/video/BV1xaRhBPEkY/) |

---

## Table of Contents

- [About](#about)
- [Quick Start](#quick-start)
- [Cases](#cases)
  - [Case 1: Initial Theoretical Model](#case-1-initial-theoretical-model)
  - [Case 2: Theoretical Extension](#case-2-theoretical-extension)
  - [Case 3: Financial Data Download](#case-3-financial-data-download)
  - [Case 4: ESG Panel Construction](#case-4-esg-panel-construction)
  - [Case 5: Court Documents Database](#case-5-court-documents-database)
  - [Case 6: Regression Analysis](#case-6-regression-analysis)
  - [Case 7: DSGE Model](#case-7-dsge-model)
  - [Case 8: Paper Writing](#case-8-paper-writing)
  - [Case 9: Revision & Referee Response](#case-9-revision--referee-response)
  - [Case 10: Full Writing Workflow](#case-10-full-writing-workflow)
- [Project Structure](#project-structure)

---

## About

This project centers on one research question: **Does ESG performance improve firm profitability by alleviating financing constraints?**

10 cases progress through the research workflow:

| Phase | Cases | Topic |
|-------|-------|-------|
| Theory | [Case 1](#case-1-initial-theoretical-model) [Case 2](#case-2-theoretical-extension) | ESG-profitability mechanism and extension |
| Data | [Case 3](#case-3-financial-data-download) [Case 4](#case-4-esg-panel-construction) | Financial data + ESG panel |
| Standalone | [Case 5](#case-5-court-documents-database) | Court documents database design |
| Empirical | [Case 6](#case-6-regression-analysis) [Case 7](#case-7-dsge-model) | Panel regression + DSGE |
| Writing | [Case 8](#case-8-paper-writing) [Case 9](#case-9-revision--referee-response) [Case 10](#case-10-full-writing-workflow) | Paper writing, revision, and integration |

---

## Quick Start

### Requirements

- Python 3.10+
- LyX (for `.lyx` theoretical model files)
- AI Agent (Claude Code, ChatGPT, or similar)

### Usage

1. Enter the case directory (e.g. `case3/`)
2. Find `prompt-N.md` and input it into an AI agent
3. Check outputs: code in `scripts/`, documents in `documents/`, data in `data/`

Each prompt is self-contained and can be run independently.

---

## Cases

### Case 1: Initial Theoretical Model

> Minimal model of ESG affecting firm profitability

| Prompt | Documents |
|--------|-----------|
| [prompt-1.md](./case1/prompt-1.md) | [model_setup.md](./case1/documents/model_setup.md) · [model_setup.lyx](./case1/documents/model_setup.lyx) |

---

### Case 2: Theoretical Extension

> Add financing constraints as a mediating mechanism

| Prompt | Documents | Depends on |
|--------|-----------|------------|
| [prompt-2.md](./case2/prompt-2.md) | [extension_notes.md](./case2/documents/extension_notes.md) · [extension.lyx](./case2/documents/extension.lyx) | [Case 1 output](./case1/documents/model_setup.md) |

---

### Case 3: Financial Data Download

> Download CSI-500 company financial data from public sources

| Prompt | Scripts | Documents | Data |
|--------|---------|-----------|------|
| [prompt-3.md](./case3/prompt-3.md) | [financial_data_download.py](./case3/scripts/financial_data_download.py) | [variable_notes.md](./case3/documents/variable_notes.md) | [company_list.csv](./case3/data/company_list.csv) · [financial_panel.csv](./case3/data/financial_panel.csv) |

---

### Case 4: ESG Panel Construction

> Construct firm-year ESG index from annual report text analysis

| Prompt | Scripts | Documents | Data |
|--------|---------|-----------|------|
| [prompt-4.md](./case4/prompt-4.md) | [esg_analysis.py](./case4/scripts/esg_analysis.py) | [codebook.md](./case4/documents/codebook.md) · [evidence_log.md](./case4/documents/evidence_log.md) | [esg_panel.csv](./case4/data/esg_panel.csv) · [evidence_log.csv](./case4/data/evidence_log.csv) |

Depends on: [Case 3 company list](./case3/data/company_list.csv)

---

### Case 5: Court Documents Database

> Design court judgment database schema and field extraction

| Prompt |
|--------|
| [prompt-5.md](./case5/prompt-5.md) |

---

### Case 6: Regression Analysis

> Panel regression testing ESG, financing constraints, and profitability

| Prompt |
|--------|
| [prompt-6.md](./case6/prompt-6.md) |

Depends on: [Case 3 financial data](./case3/data/financial_panel.csv) · [Case 4 ESG data](./case4/data/esg_panel.csv)

---

### Case 7: DSGE Model

> Numerical solution of a simple DSGE model with impulse response

| Prompt |
|--------|
| [prompt-7.md](./case7/prompt-7.md) |

---

### Case 8: Paper Writing

> Integrate theory and regression results into paper content

| Prompt |
|--------|
| [prompt-8.md](./case8/prompt-8.md) |

Depends on: [Case 1 model](./case1/documents/model_setup.md) · [Case 2 extension](./case2/documents/extension_notes.md) · [Case 6 regression](./case6/data/results_table.csv)

---

### Case 9: Revision & Referee Response

> Design revision plan based on referee comments

| Prompt |
|--------|
| [prompt-9.md](./case9/prompt-9.md) |

---

### Case 10: Full Writing Workflow

> Complete writing workflow integrating regression, introduction, and referee comments

| Prompt |
|--------|
| [prompt-10.md](./case10/prompt-10.md) |

Depends on: [Case 6 regression](./case6/data/results_table.csv) · [Case 8 paper draft](./case8/documents/paper_cn.md)

---

## Project Structure

```
.
├── [CasePrompt.md](./CasePrompt.md)          # All prompts in one file
├── case1/                                    # Case 1: Initial Model
│   ├── [prompt-1.md](./case1/prompt-1.md)
│   ├── documents/
│   │   ├── [model_setup.md](./case1/documents/model_setup.md)
│   │   └── [model_setup.lyx](./case1/documents/model_setup.lyx)
│   ├── scripts/
│   └── data/
├── case2/                                    # Case 2: Extension
│   ├── [prompt-2.md](./case2/prompt-2.md)
│   ├── documents/
│   │   ├── [extension_notes.md](./case2/documents/extension_notes.md)
│   │   └── [extension.lyx](./case2/documents/extension.lyx)
│   ├── scripts/
│   └── data/
├── case3/                                    # Case 3: Financial Data
│   ├── [prompt-3.md](./case3/prompt-3.md)
│   ├── documents/
│   │   └── [variable_notes.md](./case3/documents/variable_notes.md)
│   ├── scripts/
│   │   └── [financial_data_download.py](./case3/scripts/financial_data_download.py)
│   └── data/
│       ├── [company_list.csv](./case3/data/company_list.csv)
│       └── [financial_panel.csv](./case3/data/financial_panel.csv)
├── case4/                                    # Case 4: ESG Panel
│   ├── [prompt-4.md](./case4/prompt-4.md)
│   ├── documents/
│   │   ├── [codebook.md](./case4/documents/codebook.md)
│   │   └── [evidence_log.md](./case4/documents/evidence_log.md)
│   ├── scripts/
│   │   └── [esg_analysis.py](./case4/scripts/esg_analysis.py)
│   └── data/
│       ├── [esg_panel.csv](./case4/data/esg_panel.csv)
│       ├── [evidence_log.csv](./case4/data/evidence_log.csv)
│       └── pdf_cache/
├── case5/                                    # Case 5: Court Docs DB
│   └── [prompt-5.md](./case5/prompt-5.md)
├── case6/                                    # Case 6: Regression
│   └── [prompt-6.md](./case6/prompt-6.md)
├── case7/                                    # Case 7: DSGE
│   └── [prompt-7.md](./case7/prompt-7.md)
├── case8/                                    # Case 8: Paper Writing
│   └── [prompt-8.md](./case8/prompt-8.md)
├── case9/                                    # Case 9: Revision
│   └── [prompt-9.md](./case9/prompt-9.md)
└── case10/                                   # Case 10: Full Workflow
    └── [prompt-10.md](./case10/prompt-10.md)
```

Each case follows a consistent structure:
- `scripts/` — Python code
- `documents/` — Documentation
- `data/` — Data files

---

## License

[MIT License](./LICENSE)
