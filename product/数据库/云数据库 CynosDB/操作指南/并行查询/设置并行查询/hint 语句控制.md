TDSQL-C MySQL 版支持通过调整相关参数开启或关闭并行查询功能，通过控制台可实现对整个 SQL 语句开启或关闭并行查询能力、设置执行条件参数，也支持使用 hint 语句对单条 SQL 语句进行指定并行执行方式。
>?hint 语句可以指定 SQL 语句是否执行，并对指定 SQL 语句可以应用 session 级参数。hint 语句同时支持查询指定的并行表。
>

## hint 语句使用范例

| 功能 | 命令行 | 说明 |
|---------|---------|---------|
| 开启并行查询 | `SELECT /*+PARALLEL(x)*/ ... FROM ...;` | x 需大于0，x 表示该条 SQL 语句所使用的并行查询并行度。 |
| 关闭并行查询 | `SELECT /*+PARALLEL(x)*/ ... FROM ...;` | x 设置为0，表示关闭并行查询能力。 |
| 指定并行表 | 可通过以下两种方式指定允许哪些表执行或不执行并行查询计划：<li>通过 PARALLEL 可指定表执行并行查询计划<br>`SELECT /*+PARALLEL(t)*/ ... FROM ...;`<li>通过 NO_PARALLEL 可以指定表禁止执行并行查询计划<br>`SELECT /*+NO_PARALLEL(t)*/ ... FROM ...;` | t 为表的名称。 |
| 同时指定并行表与并行查询并行度 | `SELECT /*+PARALLEL(t x)*/ * ... FROM ...;` | x 需大于0，x 表示该条 SQL 语句所使用的并行查询并行度，t 为表的名称。 |
| 通过 hint 语句设置 session 级参数，仅对指定 SQL 语句生效 | `SELECT /*+SET_VAR(var=n)*/ * ... FROM ...;` | var 为支持 session 作用域的并行查询参数。|

## hint 语句使用场景示例
**场景一：**
`select /*+PARALLEL（）*/ * FROM t1，t2；`
强制并行度为 txsql_parallel_degree 所设置的数值（默认并行度）执行并行查询，当语句不符合并行查询执行条件时，将回退为串行查询。

**场景二：**
`select /*+PARALLEL（4）*/ * FROM t1，t2；`
无论系统默认并行度数值为多少，强制该条语句使用并行度为4执行并行查询，设置该条语句的 txsql_parallel_degree = 4 ，当语句不符合并行查询执行条件时，将回退为串行查询。

**场景三：**
`select /*+PARALLEL（t1）*/ * FROM t1，t2；`
选择 t1 表执行并行查询，并行度为系统默认并行度，当 t1 表小于 txsql_parallel_table_record_threshold 所设置的值时，将回退为串行查询。

**场景四：**
`select /*+PARALLEL（t1 8）*/ * FROM t1，t2；`
选择 t1 表执行并行查询，并行度为8，当 t1 表小于 txsql_parallel_table_record_threshold 所设置的值时，将回退为串行查询。

**场景五：**
`select /*+NO_PARALLEL（t1）*/ * FROM t1，t2；`
选择 t1 表禁止执行并行查询，当 t1 表大于 txsql_parallel_table_record_threshold 所设置的值时，将回退为串行查询。

**场景六：**
`select /*+SET_VAR(txsql_parallel_degree=8)*/ * FROM t1，t2；`
无论系统默认并行度数值为多少，强制该条语句使用并行度为8执行并行查询，设置该条语句的 txsql_parallel_degree = 8。

**场景七：**
`select /*+SET_VAR(txsql_parallel_cost_threshold=1000)*/ * FROM t1，t2`
设置该条语句的 txsql_parallel_cost_threshold=1000，当该条语句的执行代价大于1000时，即可使用并行查询。

**场景八：**
`select /*+SET_VAR(txsql_optimizer_context_max_mem_size=500000)*/ * FROM t1，t2`
设置单条语句的 txsql_optimizer_context_max_mem_size=500000，该条语句可申请的并行查询计划环境最大内存限制调整为500000。

## 相关文档
- [开启或关闭并行查询](https://cloud.tencent.com/document/product/1003/81872)
- [查看并行查询](https://cloud.tencent.com/document/product/1003/81873)
- [并行查询指标](https://cloud.tencent.com/document/product/1003/81871)
