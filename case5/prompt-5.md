# 案例 5：裁判文书数据库

> **工作目录**：本案例根目录 `case5/`
> **输出规范**：代码文件（`.py`、`.sql`）放入 `scripts/`，文档放入 `documents/`，数据文件放入 `data/`
> **依赖**：无

---

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
