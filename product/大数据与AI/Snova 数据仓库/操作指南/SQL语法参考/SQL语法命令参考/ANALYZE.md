收集有关一个数据库的统计信息。

## 概要

```sql
ANALYZE [VERBOSE] [ROOTPARTITION [ALL] ] 
   [table [ (column [, ...] ) ]]
```

## 描述

ANALYZE 收集一个数据库中的表的内容的统计信息，并且将结果存储在 pg_statistic 系统目录中。接下来，查询规划器会使用这些统计信息来帮助确定查询最有效的执行计划。

如果不带参数，ANALYZE 会检查当前数据库中的所有表。用户可以指定表名来收集单个表的统计信息。用户可以指定一组列名称，在这种情况下，仅收集这些列的统计信息。

ANALYZE 不收集外部表上的统计信息。

**如果用户想要在启用 GPORCA（默认启用）时在分区表上执行查询，那么用户必须在分区表的根分区上用 ANALYZE ROOTPARTITION 命令收集统计信息。有关 GPORCA 的信息，请参见“数据库管理员指南”中的“查询数据”。

>!用户还可以使用的数据库工具 analyzedb 更新表统计信息。analyzedb 工具可以并发地为多个表更新统计信息。该工具还能检查表、统计信息并且只在统计信息不是当前最新或者不存在时更新。有关该工具的信息，请参见“数据库工具指南”。

## 参数

ROOTPARTITION [ALL]
只在分区表的根分区上根据分区表中的数据收集统计信息。不会在叶子子分区上收集统计信息，其中的数据只会被采样。当用户指定 ROOTPARTITION 时，必须指定 ALL 或者一个分区表的名称。

如果用户在 ROOTPARTITION 中指定 ALL，数据库会为该数据库中所有分区表的根分区收集统计信息。如果在数据库中没有分区表，会返回一个消息说明没有分区表。对于非分区表不会收集统计信息。

如果用户在 ROOTPARTITION 中指定一个表名并且该表不是分区表，则不会为该表收集统计信息并且会返回一个警告消息。

ROOTPARTITION 子句对 VACUUM ANALYZE 不合法。命令 VACUUM ANALYZE ROOTPARTITION 会返回一个错误。

运行 ANALYZE ROOTPARTITION 所需的时间类似于分析一个有着相同数据的非分区表所需的时间，因为 ANALYZE ROOTPARTITION 仅采样叶子子分区数据。

对于分区表 sales_curr_yr，这个命令例子只在分区表的根分区上收集统计信息。

ANALYZE ROOTPARTITION sales_curr_yr
这个 ANALYZE 命令的例子在数据库中所有分区表的根分区上收集统计信息。

```sql
ANALYZE ROOTPARTITION ALL;
```

VERBOSE
启用进度消息的显示。被指定时，ANALYZE 会发出这些信息。

- The      table that is being processed.
- The      query that is executed to generate the sample table.
- The      column for which statistics is being computed.
- The      queries that are issued to collect the different statistics for a single      column.
- The      statistics that are generated.

table
要分析的特定表的名称（可能被方案限定）。默认为当前数据库中的所有表。

column
要分析的特定列的名称。默认为所有列。

## 注解

定期运行 ANALYZE 是个好主意，或者只在表内容发生大量变化时才运行。准确的统计信息会帮助数据库选择最合适的查询计划，并且因此改进查询处理的速度。一种常用的策略是每天在系统负载低的时候运行一次 [VACUUM](https://gp-docs-cn.github.io/docs/ref_guide/sql_commands/VACUUM.html#topic1)和ANALYZE。

ANALYZE 要求目标表上的 SHARE UPDATE EXCLUSIVE 锁。这个锁会与这些锁冲突：SHARE UPDATE EXCLUSIVE、 SHARE、SHARE ROW EXCLUSIVE、EXCLUSIVE、 ACCESS EXCLUSIVE。

对于分区表，指定要分析该表的哪一部分，如果分区表有大量已经分析过的分区并且只有少数叶子子表改变，根分区或者子分区（叶子子表）会很有用。

- 当用户在根分区表上运行 ANALYZE 时，会为所有的叶子子表（数据库为分区表创建的子表层次中最底层的表）收集统计信息。
- 当用户在一个叶子子表上运行 ANALYZE 时，只会为该叶子子表收集统计信息。当用户在非叶子子表的子表上运行 ANALYZE 时，不会有统计信息被收集。

例如，用户可以创建一个分区从2006年到2016年的分区表，每年中的每个月是一个子分区。如果用户在2013年的子表上运行 ANALYZE，则不会有统计信息被收集。如果用户在2013年三月的叶子子表上运行 ANALYZE，则只会为该叶子子表收集统计信息。

>!当用户用 CREATE TABLE 命令创建一个分区表时，数据库会创建用户指定的表（根分区或者父表），还会基于用户指定的分区层次创建表的层次（子表）。分区表、子表和它们的继承层次关系通过系统视图 *pg_partitions* 跟踪。

对于一个含有被交换为使用外部表的叶子子分区的分区表，ANALYZE 不会为外部表分区收集统计信息：
-  如果 ANALYZE [ROOTPARTITION] 被运行，外部表不会被采样并且根表统计信息不包括外部表分区。
-  如果在外部表分区上运行 ANALYZE，该分区不会被分析。
-  如果指定了 VERBOSE 子句，会显示一个报告消息：skipping external table.

数据库服务器配置参数 optimizer_analyze_root_partition 影响何时在分区表的根分区上收集统计信息。如果该参数被启用，当用户运行 ANALYZE（没有 ROOTPARTITON 关键词）并且指定根分区时，会在根分区上收集统计信息。

ANALYZE 收集的统计信息通常包括每个列中一些最常见值构成的列表以及显示每列中近似数据分布的柱状图。如果 ANALYZE 觉得对两者中的一个或者全部不感兴趣（例如，在一个唯一键列中，其中没有常见值）或者该列的数据类型不支持合适的操作符，它可能会忽略它们。

对于大型表，ANALYZE 会取得该表内容的一份随机采样，而不是检查每一行。这允许非常大的表在很短的时间内被分析完。不过要注意，这样的统计信息只是近似的，并且即使实际表内容没有改变，统计信息也将会在每次运行 ANALYZE 后发生少许变化。这可能会导致 EXPLAIN 所显示的规划器估计代价出现少许变化。在很少见的情况下，这无疑将导致在两次 ANALYZE 运行之间查询优化器选择不同的查询计划。
为了避免这种情况，可以通过调整 default_statistics_target 配置参数增加 ANALYZE 收集的统计信息量，或者逐列用 ALTER TABLE ... ALTER COLUMN ... SET STATISTICS（见 ALTER TABLE）设置每列的统计信息目标。该目标值设置最常见值列表中的最大项数以及柱状图中的最大箱数。默认的目标值是10，但可以改变它以平衡规划器估计精度以及 ANALYZE 所花的时间和在 pg_statistic 中所占用的空间。特别地，将统计信息目标设置为零会禁用该列的统计信息收集。对那些从不出现在查询的 WHERE、GROUP BY 或者 ORDER BY 子句中的列来说，这可能会很有用，因为规划器将不会使用这类列上的统计信息。

被分析列中最大的统计信息目标决定了为准备统计信息要采样的表行数。增加该目标会导致执行 ANALYZE 所需的时间空间成比例增加。

当数据库执行一次 ANALYZE 操作为一个表收集统计信息并且检测到所有被采样表的数据页为空（不含有效数据）时，数据库会显示应该执行一次 VACUUM FULL 操作的消息。如果被采样页为空，该表的统计信息将不准确。页面会在对表的大量更新后变为空，例如删除了大量行。一次 VACUUM FULL 操作会移除空页并且允许 ANALYZE 操作收集准确的统计信息。

如果表没有统计信息，服务器配置参数 gp_enable_relsize_collection 控制传统查询优化器是否使用默认统计信息文件或者使用 pg_relation_size 函数估算表的尺寸。默认情况下，如果统计信息不可用，传统优化器使用默认统计信息文件来估算行数。

## 示例

为表 mytable 收集统计信息：

```sql
ANALYZE mytable;
```

## 兼容性

SQL 标准中没有 ANALYZE 语句。

## 另见

ALTER TABLE、 EXPLAIN、 VACUUM
