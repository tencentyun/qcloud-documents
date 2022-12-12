TDSQL-C MySQL 版设置了多种监控指标帮助您实时监控数据库中有关并行查询的相关操作。本文为您介绍并行查询的相关监控指标。

## 前提条件
数据库版本：TDSQL-C MySQL 版8.0内核版本3.1.8及以上。

## 并行查询相关监控指标

| 监控项（中文） | 监控项（英文） | 单位 | 说明 | 数据聚合方式 |
|---------|---------|---------|---------|---------|
| 当前并行查询线程数 | txsql_parallel_threads_currently_used | 个 | 并行查询当前使用的线程数量。 | MAX |
| 并行查询错误数 | txsql_parallel_stmt_error | 个 | 并行查询报错的语句数量。 | SUM |
| 已执行并行查询数 | txsql_parallel_stmt_executed | 个 | 已执行的并行查询语句数量。 | SUM |
| 回滚串行查询数 | txsql_parallel_stmt_fallback | 个 | 并行查询回滚到串行查询的语句数量。 | SUM |

## 监控项最佳实践
下面列举部分特殊场景问题需对应查看监控项和解决方法。
**示例1：**
当前并行查询线程数始终等于 txsql_max_parallel_worker_threads 所设置的值。
**解决方法：**
示例表明线程数始终处于满载状态，建议在 CPU 使用率未达到高负载的情况下，增大参数 txsql_max_parallel_worker_threads 的值。

**示例2：**
并行查询错误数增加。
**解决方法：**
查询监控项 CPU 使用率与内存使用率，若负载明显变高，建议降低 txsql_parallel_degree 值为 CPU 核数的1/4。

**示例3：**
回滚串行查询数增加。
**解决方法：**
表明当前执行 SQL 不满足执行并行查询条件，建议增大线程资源总数 txsql_max_parallel_worker_threads 或增大单条语句可申请的并行查询计划环境最大内存限制 txsql_optimizer_context_max_mem_size，保证 SQL 语句可以使用并行查询。
