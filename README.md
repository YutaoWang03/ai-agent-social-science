# 智能体框架赋能《经济学科研论文写作》全链条训练——新文科数智教学实践

[English](./README_en.md)

10 个结构化案例，展示 AI 智能体如何辅助社会科学研究全流程——从理论建模、数据采集到实证分析与学术写作。

---

## 贡献者 | Contributors

- **王彬Macro** — [B 站主页](https://space.bilibili.com/321279199)
- YutaoWang

---

## 配套视频 | Video Tutorials

> 案例教学视频持续更新中

| 内容                           | 链接                                                      |
| ------------------------------ | --------------------------------------------------------- |
| 智能体简介                     | [BV1VLoCBHE4A](https://www.bilibili.com/video/BV1VLoCBHE4A/) |
| 安装配置                       | [BV11aoCBzEqJ](https://www.bilibili.com/video/BV11aoCBzEqJ/) |
| 案例 1：初版理论模型           | [BV11aoCBzECc](https://www.bilibili.com/video/BV11aoCBzECc)  |
| 案例 2：理论拓展               | [BV1yz9SB7E9Z](https://www.bilibili.com/video/BV1yz9SB7E9Z/) |
| 案例 3：财务数据下载           | [BV14aRhBPEF7](https://www.bilibili.com/video/BV14aRhBPEF7/) |
| 案例 4：ESG 面板构建           | [BV1xaRhBPEkY](https://www.bilibili.com/video/BV1xaRhBPEkY/) |
| 案例 5：大数据与本地数据库构建 | [BV1kvLp6rEua](https://www.bilibili.com/video/BV1kvLp6rEua/) |

---

## 目录 | Table of Contents

- [项目简介](#项目简介)
- [快速开始](#快速开始)
- [案例详情](#案例详情)
  - [案例 1：初版理论模型](#案例-1初版理论模型)
  - [案例 2：理论拓展](#案例-2理论拓展)
  - [案例 3：财务数据下载](#案例-3财务数据下载)
  - [案例 4：ESG 面板构建](#案例-4esg-面板构建)
  - [案例 5：裁判文书数据库](#案例-5裁判文书数据库)
  - [案例 6：回归分析](#案例-6回归分析)
  - [案例 7：DSGE 模型](#案例-7dsge-模型)
  - [案例 8：论文写作](#案例-8论文写作)
  - [案例 9：修稿与回复](#案例-9修稿与回复)
  - [案例 10：写作全流程](#案例-10写作全流程)
- [项目结构](#项目结构)

---

## 项目简介

本项目围绕一个核心研究问题展开：**ESG 表现是否通过缓解融资约束提高企业盈利能力**。

10 个案例按研究流程递进排列：

| 阶段     | 案例                                                                       | 主题                         |
| -------- | -------------------------------------------------------------------------- | ---------------------------- |
| 理论建模 | [案例 1](#案例-1初版理论模型) [案例 2](#案例-2理论拓展)                          | ESG 影响盈利能力的机制与拓展 |
| 数据采集 | [案例 3](#案例-3财务数据下载) [案例 4](#案例-4esg-面板构建)                      | 财务数据下载 + ESG 面板构造  |
| 独立场景 | [案例 5](#案例-5裁判文书数据库)                                               | 裁判文书数据库设计           |
| 实证分析 | [案例 6](#案例-6回归分析) [案例 7](#案例-7dsge-模型)                             | 面板回归 + DSGE 求解         |
| 学术写作 | [案例 8](#案例-8论文写作) [案例 9](#案例-9修稿与回复) [案例 10](#案例-10写作全流程) | 论文写作、修稿与全流程整合   |

---

## 快速开始

### 环境要求

- Python 3.10+
- LyX（打开 `.lyx` 理论模型文件）
- AI Agent（Claude Code、ChatGPT 或类似工具）

### 使用方法

1. 进入对应案例目录（如 `case3/`）
2. 找到 `prompt-N.md`，将提示词输入 AI agent
3. 查看产出：代码在 `scripts/`，文档在 `documents/`，数据在 `data/`

每个 prompt 自包含，可独立运行。

---

## 案例详情

### 案例 1：初版理论模型

> ESG 影响企业盈利能力的最小理论模型

| 提示词                          | 文档                                                                                                 |
| ------------------------------- | ---------------------------------------------------------------------------------------------------- |
| [prompt-1.md](./case1/prompt-1.md) | [model_setup.md](./case1/documents/model_setup.md) · [model_setup.lyx](./case1/documents/model_setup.lyx) |

---

### 案例 2：理论拓展

> 加入融资约束中介机制，推导新条件

| 提示词                          | 文档                                                                                                     | 依赖                                         |
| ------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [prompt-2.md](./case2/prompt-2.md) | [extension_notes.md](./case2/documents/extension_notes.md) · [extension.lyx](./case2/documents/extension.lyx) | [案例 1 产出](./case1/documents/model_setup.md) |

---

### 案例 3：财务数据下载

> 从公开渠道下载中证 500 上市公司财务数据

| 提示词                          | 代码                                                                  | 文档                                                  | 数据                                                                                                   |
| ------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| [prompt-3.md](./case3/prompt-3.md) | [financial_data_download.py](./case3/scripts/financial_data_download.py) | [variable_notes.md](./case3/documents/variable_notes.md) | [company_list.csv](./case3/data/company_list.csv) · [financial_panel.csv](./case3/data/financial_panel.csv) |

---

### 案例 4：ESG 面板构建

> 基于年报文本分析构造公司-年份 ESG 指数

| 提示词                          | 代码                                            | 文档                                                                                           | 数据                                                                                       |
| ------------------------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| [prompt-4.md](./case4/prompt-4.md) | [esg_analysis.py](./case4/scripts/esg_analysis.py) | [codebook.md](./case4/documents/codebook.md) · [evidence_log.md](./case4/documents/evidence_log.md) | [esg_panel.csv](./case4/data/esg_panel.csv) · [evidence_log.csv](./case4/data/evidence_log.csv) |

依赖：[案例 3 公司列表](./case3/data/company_list.csv)

---

### 案例 5：裁判文书数据库

> 设计裁判文书数据库 schema 与字段抽取流程

| 提示词                          |
| ------------------------------- |
| [prompt-5.md](./case5/prompt-5.md) |

---

### 案例 6：回归分析

> 面板回归检验 ESG、融资约束与盈利能力

| 提示词                          |
| ------------------------------- |
| [prompt-6.md](./case6/prompt-6.md) |

依赖：[案例 3 财务数据](./case3/data/financial_panel.csv) · [案例 4 ESG 数据](./case4/data/esg_panel.csv)

---

### 案例 7：DSGE 模型

> 简单 DSGE 模型的数值求解与脉冲响应

| 提示词                          |
| ------------------------------- |
| [prompt-7.md](./case7/prompt-7.md) |

---

### 案例 8：论文写作

> 将理论与回归结果整合为论文核心内容

| 提示词                          |
| ------------------------------- |
| [prompt-8.md](./case8/prompt-8.md) |

依赖：[案例 1 理论模型](./case1/documents/model_setup.md) · [案例 2 理论拓展](./case2/documents/extension_notes.md) · [案例 6 回归结果](./case6/data/results_table.csv)

---

### 案例 9：修稿与回复

> 根据审稿意见设计修稿方案

| 提示词                          |
| ------------------------------- |
| [prompt-9.md](./case9/prompt-9.md) |

---

### 案例 10：写作全流程

> 整合回归、引言与审稿意见的完整写作工作流

| 提示词                             |
| ---------------------------------- |
| [prompt-10.md](./case10/prompt-10.md) |

依赖：[案例 6 回归结果](./case6/data/results_table.csv) · [案例 8 论文草稿](./case8/documents/paper_cn.md)

---

## 项目结构

```
.
├── [CasePrompt.md](./CasePrompt.md)          # 全部提示词汇总
├── case1/                                    # 案例 1：初版理论模型
│   ├── [prompt-1.md](./case1/prompt-1.md)
│   ├── documents/
│   │   ├── [model_setup.md](./case1/documents/model_setup.md)
│   │   └── [model_setup.lyx](./case1/documents/model_setup.lyx)
│   ├── scripts/
│   └── data/
├── case2/                                    # 案例 2：理论拓展
│   ├── [prompt-2.md](./case2/prompt-2.md)
│   ├── documents/
│   │   ├── [extension_notes.md](./case2/documents/extension_notes.md)
│   │   └── [extension.lyx](./case2/documents/extension.lyx)
│   ├── scripts/
│   └── data/
├── case3/                                    # 案例 3：财务数据下载
│   ├── [prompt-3.md](./case3/prompt-3.md)
│   ├── documents/
│   │   └── [variable_notes.md](./case3/documents/variable_notes.md)
│   ├── scripts/
│   │   └── [financial_data_download.py](./case3/scripts/financial_data_download.py)
│   └── data/
│       ├── [company_list.csv](./case3/data/company_list.csv)
│       └── [financial_panel.csv](./case3/data/financial_panel.csv)
├── case4/                                    # 案例 4：ESG 面板构建
│   ├── [prompt-4.md](./case4/prompt-4.md)
│   ├── documents/
│   │   ├── [codebook.md](./case4/documents/codebook.md)
│   │   └── [evidence_log.md](./case4/documents/evidence_log.md)
│   ├── scripts/
│   │   └── [esg_analysis.py](./case4/scripts/esg_analysis.py)
│   └── data/
│       ├── [esg_panel.csv](./case4/data/esg_panel.csv)
│       ├── [evidence_log.csv](./case4/data/evidence_log.csv)
│       └── pdf_cache/                      # 年报 PDF 样本
├── case5/                                    # 案例 5：裁判文书数据库
│   └── [prompt-5.md](./case5/prompt-5.md)
├── case6/                                    # 案例 6：回归分析
│   └── [prompt-6.md](./case6/prompt-6.md)
├── case7/                                    # 案例 7：DSGE 模型
│   └── [prompt-7.md](./case7/prompt-7.md)
├── case8/                                    # 案例 8：论文写作
│   └── [prompt-8.md](./case8/prompt-8.md)
├── case9/                                    # 案例 9：修稿与回复
│   └── [prompt-9.md](./case9/prompt-9.md)
└── case10/                                   # 案例 10：写作全流程
    └── [prompt-10.md](./case10/prompt-10.md)
```

每个案例遵循统一结构：

- `scripts/` — Python 代码
- `documents/` — 说明文档
- `data/` — 数据文件

---

## 许可证

[MIT License](./LICENSE)
