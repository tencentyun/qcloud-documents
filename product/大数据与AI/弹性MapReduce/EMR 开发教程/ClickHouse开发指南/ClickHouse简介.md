腾讯云弹性 MapReduce（EMR）- ClickHouse 提供开源列式数据库 ClickHouse 的云上托管服务，提供了便捷的 ClickHouse 集群部署、配置修改、监控告警等功能，为企业及用户提供安全稳定的 OLAP 解决方案。ClickHouse 具备极佳的查询性能，非常适合数据在线查询分析场景。

## ClickHouse 功能特征

### 架构

支持单节点、多节点以及多副本架构。根据业务需求，灵活选择。

### 运维

在控制台提供了开箱即用的监控、日志检索、参数调整等服务。

### 数据

弹性 MapReduce（EMR）- ClickHouse 提供了完整的数据导入导出支持，可方便地将数据从 COS、HDFS、KAFKA、MySQL 等其他数据源导入或导出到 ClickHouse 集群。

## ClickHouse 优势

### 高性能

充分发挥多核并行优势（SIMD 高效指令集、向量化执行引擎）并借助分布式技术，加速计算提供实时分析能力。开源公开 benchmark 显示比传统方法快100 - 1000倍，提供50MB/s - 200MB/s的高吞吐实时导入能力。

### 低成本

借助于精心设计的列式存储、高效的数据压缩算法，提供高达10倍的压缩比，大幅提升单机数据存储和计算能力，大幅降低使用成本，是构建海量数据仓库的绝佳方案。

### 易用

- 提供完善 SQL 支持，上手十分简单。
- 提供 json、map、array 等灵活数据类型适配业务快速变化。
- 支持近似计算、概率数据结构等应对海量数据处理。

## EMR-ClickHouse 表引擎介绍

### 表引擎的作用

表引擎（即表的类型）决定了：
- 数据的存储方式和位置，写到哪里以及从哪里读取数据。
- 支持哪些查询以及如何支持。
- 并发数据访问。
- 索引的使用（如果存在）。
- 是否可以执行多线程请求。
- 数据复制参数。

### 引擎类型

#### MergeTree 系列

适用于高负载任务的最通用和功能最强大的表引擎。这些引擎的共同特点是可以快速插入数据并进行后续的后台数据处理。MergeTree 系列引擎支持数据复制（使用 Replicated\* 的引擎版本），分区和一些其他引擎不支持的功能。

**该类型的引擎：**
- [MergeTree](https://clickhouse.tech/docs/zh/operations/table_engines/mergetree/)：Clickhouse 中最强大的表引擎为 MergeTree（合并树）引擎。
- [ReplacingMergeTree](https://clickhouse.tech/docs/zh/operations/table_engines/replacingmergetree/)：该引擎和 MergeTree 的不同之处在于它会删除具有相同主键的重复项。
- [SummingMergeTree](https://clickhouse.tech/docs/zh/operations/table_engines/summingmergetree/)：该引擎继承自 MergeTree。区别在于，当合并 SummingMergeTree 表的数据片段时，ClickHouse 会把所有具有相同主键的行合并为一行，该行包含了被合并的行中具有数值数据类型的列的汇总值。如果主键的组合方式使得单个键值对应于大量的行，则可以显著的减少存储空间并加快数据查询的速度。
- [AggregatingMergeTree](https://clickhouse.tech/docs/zh/operations/table_engines/aggregatingmergetree/)：该引擎继承自 MergeTree，并改变了数据片段的合并逻辑。ClickHouse 会将相同主键的所有行（在一个数据片段内）替换为单个存储一系列聚合函数状态的行。
- [CollapsingMergeTree](https://clickhouse.tech/docs/zh/operations/table_engines/collapsingmergetree/)：该引擎继承于 MergeTree，并在数据块合并算法中添加了折叠行的逻辑。
- [VersionedCollapsingMergeTree](https://clickhouse.tech/docs/zh/operations/table_engines/versionedcollapsingmergetree/)：VersionedCollapsingMergeTree 是 collapsingmergetree 的升级，使用不同的 collapsing 算法，该算法允许使用多个线程以任何顺序插入数据。
- [GraphiteMergeTree](https://clickhouse.tech/docs/zh/operations/table_engines/graphitemergetree/)：应用于 Graphite data 的数据汇总，该引擎减少了存储容量，提高了 Graphite 查询的效率。

#### Log 系列

具有最小功能的轻量级引擎。当您需要快速写入许多小表（最多约100万行）并在以后整体读取它们时，该类型的引擎是最有效的。

**该类型的引擎：**
- [TinyLog](https://clickhouse.tech/docs/zh/operations/table_engines/tinylog/)：最简单的表引擎，用于将数据存储在磁盘上。每列都存储在单独的压缩文件中。写入时，数据将附加到文件末尾。
- [StripeLog](https://clickhouse.tech/docs/zh/operations/table_engines/stripelog/)：该引擎属于日志引擎系列。在需要写入许多小数据量（小于一百万行）的表的场景下使用这个引擎。
- [Log](https://clickhouse.tech/docs/zh/operations/table_engines/log/)：日志与 TinyLog 的不同之处在于，“标记”的小文件与列文件存在一起。这些标记写在每个数据块上，并且包含偏移量，这些偏移量指示从哪里开始读取文件以便跳过指定的行数。这使得可以在多个线程中读取表数据。对于并发数据访问，可以同时执行读取操作，而写入操作则阻塞读取和其它写入。Log 引擎不支持索引。同样，如果写入表失败，则该表将被破坏，并且从该表读取将返回错误。Log 引擎适用于临时数据，write-once 表以及测试或演示目的。 

#### Intergation engines

用于与其他的数据存储与处理系统集成的引擎。

- [Kafka](https://clickhouse.tech/docs/zh/operations/table_engines/kafka/)：此引擎与 Apache Kafka 结合使用。
- [MySQL](https://clickhouse.tech/docs/zh/operations/table_engines/mysql/)：MySQL 引擎可以对存储在远程 MySQL 服务器上的数据执行 SELECT 查询。
- [ODBC](https://clickhouse.tech/docs/zh/engines/table_engines/integrations/odbc/)：此引擎允许 ClickHouse 通过 ODBC 接口访问外部数据库。
- [JDBC](https://clickhouse.tech/docs/zh/operations/table_engines/jdbc/)：此引擎允许 ClickHouse 通过 JDBC 接口访问外部数据库。
- [HDFS](https://clickhouse.tech/docs/zh/operations/table_engines/hdfs/)：此引擎允许 ClickHouse 访问 HDFS 上的数据。

#### 用于其他特定功能的引擎

- [Distributed](https://clickhouse.tech/docs/zh/operations/table_engines/distributed/)：分布式引擎本身不存储数据，但可以在多个服务器上进行分布式查询。读是自动并行的。读取时，远程服务器表的索引（如果有的话）会被使用。
- [MaterializedView](https://clickhouse.tech/docs/zh/operations/table_engines/materializedview/)：物化视图的使用（更多信息请参阅 CREATE TABLE）。它需要使用一个不同的引擎来存储数据，这个引擎要在创建物化视图时指定。当从表中读取时，就会使用该引擎。
- [Dictionary](https://clickhouse.tech/docs/zh/operations/table_engines/dictionary/)：Dictionary 引擎将字典数据展示为一个 ClickHouse 的表。
- [Merge](https://clickhouse.tech/docs/zh/operations/table_engines/merge/)：Merge 引擎 (不要和 MergeTree 引擎混淆) 本身不存储数据，但可用于同时从任意多个其他的表中读取数据。
- [File](https://clickhouse.tech/docs/zh/operations/table_engines/file/)：数据源是以 Clickhouse 支持的一种输入格式（TabSeparated，Native 等）存储数据的文件。
- [Null](https://clickhouse.tech/docs/zh/operations/table_engines/null/)：当写入 Null 类型的表时，将忽略数据。从 Null 类型的表中读取时，返回空。但是，可以在 Null 类型的表上创建物化视图。写入表的数据将转发到视图中。
- [Set](https://clickhouse.tech/docs/zh/operations/table_engines/set/)：始终存在于 RAM 中的数据集。
- [Join](https://clickhouse.tech/docs/zh/operations/table_engines/join/)：加载好的 JOIN 表数据会常驻内存中。
- [URL](https://clickhouse.tech/docs/zh/operations/table_engines/url/)：用于管理远程 HTTP/HTTPS 服务器上的数据。该引擎类似 File 引擎。
- [View](https://clickhouse.tech/docs/zh/operations/table_engines/view/)：用于构建视图（有关更多信息，请参阅     CREATE VIEW 查询）。它不存储数据，仅存储指定的 SELECT 查询。 从表中读取时，会运行此查询（并从查询中删除所有不必要的列）。
- [Memory](https://clickhouse.tech/docs/zh/operations/table_engines/memory/)：Memory 引擎以未压缩的形式将数据存储在 RAM 中。
- [Buffer](https://clickhouse.tech/docs/zh/operations/table_engines/buffer/)：缓冲数据写入 RAM 中，周期性地将数据刷新到另一个表。在读取操作时，同时从缓冲区和另一个表读取数据。

### 虚拟列

虚拟列是表引擎组成的一部分，它在对应的表引擎的源代码中定义。

不能在 CREATE TABLE 中指定虚拟列，并且虚拟列不会包含在 SHOW CREATE TABLE 和 DESCRIBE TABLE 的查询结果中。虚拟列是只读的，所以不能向虚拟列中写入数据。

如果想要查询虚拟列中的数据，您必须在 SELECT 查询中包含虚拟列的名字。`SELECT *`不会返回虚拟列的内容。

若您创建的表中有一列与虚拟列的名字相同，那么虚拟列将不能再被访问（不建议这样操作）。为了避免这种列名的冲突，虚拟列的名字一般都以下划线开头。
