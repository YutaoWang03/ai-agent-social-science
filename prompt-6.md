# 案例 6：ESG、融资约束与盈利能力的回归分析

在该目录下运行 AI agent，输入以下提示词即可开始实验。

---

根据上一级文件夹下面的case_03_financial/test3的所有上市公司的财务数据和case_04_esg/test3构建的上市公司esg的数据，构建一个上市公司的财务以及esg的面板数据集`panel_data.csv`，检验 ESG、融资约束与企业盈利能力之间的关系。
1. 先给执行计划；
2. 设定 `profitability` 为因变量，`esg_total` 为核心解释变量，估计 ESG 对盈利能力的基准回归；
3. 再设定 `financing_constraint` 为因变量，检验 ESG 是否缓解融资约束；
4. 最后同时纳入 `esg_total` 和 `financing_constraint`，讨论融资约束的中介作用；
5. 加入 `firm fixed effects` 和 `year fixed effects`；
6. 标准误聚类到 `firm` 层面；
7. 加入 `size`、`lev`、`industry` 等控制变量；
8. 给出至少两个稳健性检验建议；
9. 输出 `regression.py` 或 `regression.do`、`results_table.csv` 和 `empirical_notes.md`；
10. 最后告诉我哪些地方最容易把相关关系误写成因果关系。
