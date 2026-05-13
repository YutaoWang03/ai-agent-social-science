# AI Agent for Social Science Research

# 智能体与社会科学研究

A collection of 10 structured case studies demonstrating how AI agents can assist social science research workflows — from theoretical modeling and data collection to empirical analysis and academic writing.

本项目包含 10 个结构化案例，展示 AI 智能体如何辅助社会科学研究全流程——从理论建模、数据采集到实证分析与学术写作。

---

## Case Overview / 案例总览

| # | Case / 案例 | Description / 说明 | Outputs / 产出 |
|---|------------|-------------------|----------------|
| 1 | 初版理论模型 | 搭建 ESG 影响企业盈利能力的最小理论模型 | `model_setup.md`, `model_setup.lyx` |
| 2 | 理论拓展 | 加入融资约束中介机制，推导新条件 | `extension_notes.md`, `extension.lyx` |
| 3 | 财务数据下载 | 从公开渠道下载中证 500 上市公司财务数据 | `financial_data_download.py`, `financial_panel.csv`, `variable_notes.md` |
| 4 | ESG 面板构建 | 基于年报文本分析构造公司-年份 ESG 指数 | `esg_panel.csv`, `codebook.md`, `evidence_log.md` |
| 5 | 裁判文书数据库 | 设计裁判文书数据库 schema 与字段抽取流程 | `schema.sql`, `build_database.py`, `query_templates.sql` |
| 6 | 回归分析 | 面板回归检验 ESG、融资约束与盈利能力 | `regression.py`, `results_table.csv`, `empirical_notes.md` |
| 7 | DSGE 模型 | 简单 DSGE 模型的数值求解与脉冲响应 | Python/Dynare code, impulse response plots |
| 8 | 论文写作 | 将理论与回归结果整合为论文核心内容 | Chinese paper draft, English abstract |
| 9 | 修稿与回复 | 根据审稿意见设计修稿方案 | `response_letter.md`, `revision_plan.md` |
| 10 | 写作全流程 | 整合回归、引言与审稿意见的完整写作工作流 | `writing_revision_plan.md` |

## Project Structure / 项目结构

```
.
├── CasePrompt.md                    # 提示词汇总 / All prompts in one file
├── case1/                           # 案例 1：初版理论模型
│   ├── documents/
│   │   ├── prompt-1.md
│   │   ├── model_setup.md
│   │   └── model_setup.lyx
│   ├── scripts/
│   └── data/
├── case2/                           # 案例 2：理论拓展
│   ├── documents/
│   │   ├── prompt-2.md
│   │   ├── extension_notes.md
│   │   └── extension.lyx
│   ├── scripts/
│   └── data/
├── case3/                           # 案例 3：财务数据下载
│   ├── documents/
│   │   ├── prompt-3.md
│   │   └── variable_notes.md
│   ├── scripts/
│   │   └── financial_data_download.py
│   └── data/
│       ├── company_list.csv
│       └── financial_panel.csv
├── case4/                           # 案例 4：ESG 面板构建
│   ├── documents/
│   │   ├── prompt-4.md
│   │   ├── codebook.md
│   │   └── evidence_log.md
│   ├── scripts/
│   │   └── esg_analysis.py
│   └── data/
│       ├── esg_panel.csv
│       ├── evidence_log.csv
│       └── pdf_cache/              # 年报 PDF 样本 / Sample annual reports
├── case5/                           # 案例 5：裁判文书数据库（待实现）
│   └── documents/
│       └── prompt-5.md
├── case6/                           # 案例 6：回归分析（待实现）
│   └── documents/
│       └── prompt-6.md
├── case7/                           # 案例 7：DSGE 模型（待实现）
│   └── documents/
│       └── prompt-7.md
├── case8/                           # 案例 8：论文写作（待实现）
│   └── documents/
│       └── prompt-8.md
├── case9/                           # 案例 9：修稿与回复（待实现）
│   └── documents/
│       └── prompt-9.md
└── case10/                          # 案例 10：写作全流程（待实现）
    └── documents/
        └── prompt-10.md
```

Each case directory follows a consistent structure:
- `scripts/` — Python 代码 / Python scripts
- `documents/` — 说明文档 / Documentation and notes
- `data/` — 数据文件 / Data files and outputs

## How to Use / 使用方法

1. **选择案例**：进入对应目录（如 `case3/`），找到 `documents/` 中的提示词。
2. **运行 AI Agent**：将提示词输入 AI agent（如 Claude Code），即可开始实验。
3. **查看产出**：每个案例目录包含 agent 生成的代码（`scripts/`）、数据（`data/`）和文档（`documents/`）。

Each case's prompt is self-contained — copy it into any AI agent to reproduce the workflow.

## Research Theme / 研究主题

All cases围绕同一研究主题展开：**ESG 表现是否通过缓解融资约束提高企业盈利能力**。

- Cases 1–2：理论模型与机制推导
- Cases 3–4：数据采集与变量构造
- Case 5：独立应用场景（裁判文书数据库）
- Cases 6–7：实证分析（面板回归 + DSGE）
- Cases 8–10：学术写作与修稿

## Requirements / 依赖

- Python 3.10+（for data download and analysis scripts）
- LyX（for opening `.lyx` theoretical model files）
- AI Agent（Claude Code, ChatGPT, or similar）

## License

MIT
