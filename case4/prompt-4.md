# 案例 4：从年报构造 ESG 面板

> **工作目录**：本案例根目录 `case4/`
> **输出规范**：代码文件放入 `scripts/`，文档放入 `documents/`，数据文件放入 `data/`
> **依赖**：`../case3/data/company_list.csv`（案例 3 产出的公司列表）

---

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
