# CasePrompt 汇总

本文档汇总了项目中所有的案例提示词，按编号排列，供查阅和复用。

---

## 案例 1：ESG 与企业盈利能力的初版理论模型

> **工作目录**：本案例根目录 `case1/`
> **输出规范**：代码文件放入 `scripts/`，文档放入 `documents/`，数据文件放入 `data/`
> **依赖**：无

我想研究企业 ESG 表现如何影响企业盈利能力。请你基于这个想法完成以下任务：

1. 先给执行计划；
2. 搭建一个最小理论模型；
3. 明确参与者、时序、状态变量、控制变量和约束；
4. 写出企业最优化问题，并说明 ESG 如何进入利润函数；
5. 说明 ESG 可能通过哪些机制影响盈利能力；
6. 给出至少两个可检验命题，例如 ESG 对 ROA、利润率或长期绩效的影响；
7. 输出 `documents/model_setup.md` 和 `documents/model_setup.lyx`，写出整个模型；
8. 单独列出所有额外假设，并说明其经济含义；
9. 最后告诉我哪些结论是模型严格推出的，哪些只是合理直觉。

---

## 案例 2：ESG、融资约束与盈利能力的理论拓展

> **工作目录**：本案例根目录 `case2/`
> **输出规范**：代码文件放入 `scripts/`，文档放入 `documents/`，数据文件放入 `data/`
> **依赖**：`../case1/documents/model_setup.md`（案例 1 产出的基准模型）

下面给你一个"ESG 直接影响企业盈利能力"的基准模型 `../case1/documents/model_setup.md`。请你完成以下任务：

1. 先给执行计划；
2. 在原模型中加入融资能力这一中介机制；
3. 设定 ESG 可以缓解融资约束，从而影响企业资本投入和盈利能力；
4. 说明原有均衡条件哪些保持不变，哪些需要修改；
5. 推导 ESG 通过融资约束影响盈利能力的新条件；
6. 给出至少一个新的比较静态结论；
7. 输出 `documents/extension_notes.md` 和 `documents/extension.lyx`；
8. 明确列出拓展后新增的假设以及它们的经济含义；
9. 最后指出这个拓展模型最容易出错的三步。

---

## 案例 3：下载上市公司财务数据

> **工作目录**：本案例根目录 `case3/`
> **输出规范**：代码文件放入 `scripts/`，文档放入 `documents/`，数据文件放入 `data/`
> **依赖**：无

我想研究上市公司 ESG、融资约束与盈利能力之间的关系。请你完成以下任务：

1. 先给执行计划；
2. 从公开渠道获得免费的上市公司财务数据。
3. 找到渠道后，从中证500的目录中的300家公司，存为 `data/company_list.csv`，然后下载这300家上市公司2010-2024年度财务数据；
4. 提取营业收入、净利润、总资产、资产负债率、ROA、ROE、现金持有和资本支出等变量；
5. 整理成公司-年份面板格式；
6. 统一公司代码、年份和变量名称；
7. 构造基础盈利能力指标和财务控制变量；
8. 输出 `scripts/financial_data_download.py`、`data/financial_panel.csv` 和 `documents/variable_notes.md`；
9. 在 `variable_notes.md` 中写清楚每个变量的数据库字段、计算方法和经济含义；
10. 最后告诉我哪些变量口径最需要人工核查。

---

## 案例 4：从年报构造 ESG 面板

> **工作目录**：本案例根目录 `case4/`
> **输出规范**：代码文件放入 `scripts/`，文档放入 `documents/`，数据文件放入 `data/`
> **依赖**：`../case3/data/company_list.csv`（案例 3 产出的公司列表）

我想基于 `../case3/data/company_list.csv` 中的 A 股上市公司 2010-2024 年年报构造一个公司-年份层面的 ESG 指数。

1. 先给执行计划；
2. 根据csv文档里面的上市公司公司代码和年份，去公开的渠道例如AKshare查找对应年报；
3. 运用文本分析，优先定位环境保护、社会责任、公司治理、员工、合规和风险披露等章节；
4. 设计一个可复核的 ESG 评分规则；
5. 为每个公司-年份构造 `E_score`、`S_score`、`G_score` 和 `ESG_total`；
6. 输出面板数据集 `data/esg_panel.csv`；
7. 输出 `documents/evidence_log.md`，保留每个得分对应的原文证据和页码或章节位置；
8. 输出 `documents/codebook.md`，定义评分口径和赋分规则；
9. 最后告诉我哪些得分最容易因为文本措辞而误判。

---

## 案例 5：裁判文书数据库

> **工作目录**：本案例根目录 `case5/`
> **输出规范**：代码文件（`.py`、`.sql`）放入 `scripts/`，文档放入 `documents/`，数据文件放入 `data/`
> **依赖**：无

请寻找裁判文书网的千万份裁判文书，希望研究债务违约案件。请你完成以下任务：

1. 先给执行计划；
2. 查找公开的裁判文书数据来源，然后询问我用哪一个数据来源。
3. 设计一个适合裁判文书存储、元数据管理和字段抽取的数据库 schema；
4. 生成建表 SQL；
5. 生成导入脚本，把本地裁判文书及其元数据写入数据库；
6. 设计抽取流程，从文书中抽取案件发生地点、法官姓名、涉案金额、案由、年份等字段；
7. 生成若干查询模板，用于筛选债务违约案件；
8. 构造 `region_year` 和 `judge_year` 两类聚合指标；
9. 输出 `scripts/schema.sql`、`scripts/build_database.py`、`scripts/extract_case_fields.py`、`scripts/query_templates.sql` 和 `documents/database_notes.md`；
10. 最后告诉我哪些字段适合规则抽取，哪些字段更适合模型辅助抽取。

---

## 案例 6：ESG、融资约束与盈利能力的回归分析

> **工作目录**：本案例根目录 `case6/`
> **输出规范**：代码文件放入 `scripts/`，文档放入 `documents/`，数据文件放入 `data/`
> **依赖**：`../case3/data/financial_panel.csv`（财务数据）、`../case4/data/esg_panel.csv`（ESG 数据）

根据 `../case3/data/financial_panel.csv` 的上市公司财务数据和 `../case4/data/esg_panel.csv` 的上市公司 ESG 数据，构建一个上市公司的财务以及 ESG 的面板数据集 `data/panel_data.csv`，检验 ESG、融资约束与企业盈利能力之间的关系。

1. 先给执行计划；
2. 设定 `profitability` 为因变量，`esg_total` 为核心解释变量，估计 ESG 对盈利能力的基准回归；
3. 再设定 `financing_constraint` 为因变量，检验 ESG 是否缓解融资约束；
4. 最后同时纳入 `esg_total` 和 `financing_constraint`，讨论融资约束的中介作用；
5. 加入 `firm fixed effects` 和 `year fixed effects`；
6. 标准误聚类到 `firm` 层面；
7. 加入 `size`、`lev`、`industry` 等控制变量；
8. 给出至少两个稳健性检验建议；
9. 输出 `scripts/regression.py`（或 `scripts/regression.do`）、`data/results_table.csv` 和 `documents/empirical_notes.md`；
10. 最后告诉我哪些地方最容易把相关关系误写成因果关系。

---

## 案例 7：简单 DSGE 模型

> **工作目录**：本案例根目录 `case7/`
> **输出规范**：代码文件放入 `scripts/`，文档放入 `documents/`，数据文件和图片放入 `data/`
> **依赖**：无

请为一个简单 DSGE 模型完成数值求解任务。

1. 先给执行计划；
2. 写出模型方程，包括欧拉方程、资源约束、资本积累方程和技术冲击过程；
3. 设定一组基础参数；
4. 生成可运行的 Python 或 Dynare 代码，保存为 `scripts/dsge_model.py`；
5. 求稳态并模拟一个技术冲击的脉冲响应；
6. 输出产出、消费、投资和劳动的动态图，保存到 `data/`；
7. 在 `documents/notes.md` 中解释每一步的经济含义；
8. 如果模型不收敛，请给出调试建议；
9. 最后告诉我哪些图形结果最需要结合经济逻辑进行人工检查。

---

## 案例 8：把理论与回归写成论文

> **工作目录**：本案例根目录 `case8/`
> **输出规范**：文档放入 `documents/`
> **依赖**：`../case1/documents/model_setup.md`（理论模型）、`../case2/documents/extension_notes.md`（理论拓展）、`../case6/data/results_table.csv`（回归结果）

请根据以下材料，写一篇论文的核心内容。研究主题是：ESG 是否通过缓解融资约束提高企业盈利能力。

**参考材料**：
- 理论模型：`../case1/documents/model_setup.md`
- 理论拓展：`../case2/documents/extension_notes.md`
- 回归结果：`../case6/data/results_table.csv`

1. 先给执行计划；
2. 写一个简短的理论机制概述，说明 ESG 如何影响盈利能力，以及融资约束的中介作用；
3. 根据回归结果写一个 Results 段落；
4. 区分理论命题、经验结果、统计显著性和经济显著性；
5. 不要编造表中没有的机制证据；
6. 如果结果存在不稳健之处，请明确指出；
7. 输出中文论文版本 `documents/paper_cn.md`；
8. 再补一个英文摘要式总结 `documents/abstract_en.md`；
9. 最后列出三句常见但不严谨的表述，并给出更好的改写。

---

## 案例 9：修稿与回复审稿人

> **工作目录**：本案例根目录 `case9/`
> **输出规范**：文档放入 `documents/`
> **依赖**：`documents/referee_comments.txt`（审稿意见，需手动放入）

请读取 `documents/referee_comments.txt`，围绕"ESG、融资约束与企业盈利能力"这篇论文完成修稿设计。

1. 先给执行计划；
2. 将评论分为识别问题、机制问题、稳健性问题、写作问题；
3. 为每类问题生成一个修稿任务列表；
4. 区分"必须回应"和"可解释不改"的问题；
5. 起草 `documents/response_letter.md`；
6. 给出 `documents/revision_plan.md`，并按优先级排序；
7. 对每项修改说明它会影响论文的哪一部分；
8. 最后告诉我哪些意见需要补做分析，哪些主要是改写表达。

---

## 案例 10：研究写作全流程整合

> **工作目录**：本案例根目录 `case10/`
> **输出规范**：文档放入 `documents/`
> **依赖**：`../case6/data/results_table.csv`（回归结果表）、`../case8/documents/paper_cn.md`（引言草稿）、`documents/referee_comments.txt`（审稿意见，需手动放入）

请围绕"ESG、融资约束与企业盈利能力"这篇论文完成一个完整写作工作流。

你将使用以下材料：
- 回归结果表：`../case6/data/results_table.csv`
- 引言草稿：`../case8/documents/paper_cn.md`
- 审稿意见：`documents/referee_comments.txt`

请按以下步骤完成：

1. 先给执行计划；
2. 根据回归结果写一个结果段落；
3. 根据现有引言，补写一个能连接研究问题和实证结果的过渡段；
4. 根据 referee comment，指出现有写作中最需要修改的三处；
5. 生成 `documents/writing_revision_plan.md`；
6. 所有修改建议都要说明它们服务于哪一个研究目标；
7. 最后总结这篇论文当前最强的贡献和最弱的环节。
