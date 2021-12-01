## 介绍
JDBC Connector 提供了对 MySQL、PostgreSQL、Oracle 等常见的数据库读写支持。

目前 Oceanus 提供的 `flink-connector-jdbc` Connector 组件已经内置了 MySQL 和 PostgreSQL 的驱动程序。若需要连接 Oracle 等其他的数据库，可通过附加**自定义程序包**的方式，上传相应的 JDBC Driver 的 JAR 包。

## 版本说明

| Flink 版本 | 说明 |
| :-------- | :--- |
| 1.11      | 支持 |
| 1.13      | 支持 |

## 使用范围
JDBC 支持用作数据源表（Source），用于按固定列扫描表和用于 JOIN 的右表（维表）；也支持用作数据目的表（sink），用于 Tuple 数据流表和用于 Upsert 数据流表（需要指定主键）。

若需要将 JDBC 数据库的变动记录作为流式源表消费，请使用内置的 CDC 数据源。若内置的 CDC 数据源无法满足需求，还可使用 [Debezium](https://debezium.io/documentation/reference/1.2/tutorial.html)、[Canal](https://github.com/alibaba/canal) 等，对 JDBC 数据库的变更进行捕获和订阅，然后 Oceanus 即可对这些变更事件进行进一步的处理。详情可参见 [消息队列 Kafka](https://cloud.tencent.com/document/product/849/48310)。

## DDL 定义

### 用作按列扫描的数据源（Source）

```sql
CREATE TABLE `jdbc_source_table` (
    `id` INT,
    `name` STRING
) WITH (
    -- 指定数据库连接参数
    'connector' = 'jdbc',
    'url' = 'jdbc:mysql://10.1.28.93:3306/CDB?rewriteBatchedStatements=true&serverTimezone=Asia/Shanghai', -- 请替换为您的实际 MySQL 连接参数
    'table-name' = 'my-table', -- 需要写入的数据表
    'username' = 'admin',      -- 数据库访问的用户名（需要提供 INSERT 权限）
    'password' = 'MyPa$$w0rd',  -- 数据库访问的密码
    'scan.partition.column' = 'id',   -- 分区扫描列名
    'scan.partition.num' = '2',       -- 分区数量
    'scan.partition.lower-bound' = '0', -- 首个分区的最小值
    'scan.partition.upper-bound' = '100', -- 最后一个分区的最大值
    'scan.fetch-size' = '1' -- 每次从数据库读取时，批量获取的行数
);
```

### 用作维表数据源（Source）

```sql
CREATE TABLE `jdbc_dim_table` (
    `id` INT,
    `name` STRING
) WITH (
    -- 指定数据库连接参数
    'connector' = 'jdbc',
    'url' = 'jdbc:mysql://10.1.28.93:3306/CDB?rewriteBatchedStatements=true&serverTimezone=Asia/Shanghai', -- 请替换为您的实际 MySQL 连接参数
    'table-name' = 'my-table', -- 需要写入的数据表
    'username' = 'admin',      -- 数据库访问的用户名（需要提供 INSERT 权限）
    'password' = 'MyPa$$w0rd',  -- 数据库访问的密码
    'lookup.cache.max-rows' = '100',   -- 读缓存大小
    'lookup.cache.ttl' = '5000'       -- 读缓存的 TTL
);
```

### 用作数据目的（Tuple Sink）

```sql
CREATE TABLE `jdbc_sink_table` (
    `id` INT,
    `name` STRING
) WITH (
    -- 指定数据库连接参数
    'connector' = 'jdbc',
    'url' = 'jdbc:mysql://10.1.28.93:3306/CDB?rewriteBatchedStatements=true&serverTimezone=Asia/Shanghai', -- 请替换为您的实际 MySQL 连接参数
    'table-name' = 'my-table',  -- 需要写入的数据表
    'username' = 'admin',       -- 数据库访问的用户名（需要提供 INSERT 权限）
    'password' = 'MyPa$$w0rd',  -- 数据库访问的密码
    'sink.buffer-flush.max-rows' = '200',  -- 批量输出的条数
    'sink.buffer-flush.interval' = '2s'    -- 批量输出的间隔
);
```

### 用作数据目的（Upsert Sink）

```sql
CREATE TABLE `jdbc_upsert_sink_table` (
    `id` INT PRIMARY KEY NOT ENFORCED,
    `name` STRING
) WITH (
    -- 指定数据库连接参数
    'connector' = 'jdbc',
    'url' = 'jdbc:mysql://10.1.28.93:3306/CDB?rewriteBatchedStatements=true&serverTimezone=Asia/Shanghai', -- 请替换为您的实际 MySQL 连接参数
    'table-name' = 'my-upsert-table', -- 需要写入的数据表
    'username' = 'admin',             -- 数据库访问的用户名（需要提供 INSERT 权限）
    'password' = 'MyPa$$w0rd',        -- 数据库访问的密码
    'sink.buffer-flush.max-rows' = '200',  -- 批量输出的条数
    'sink.buffer-flush.interval' = '2s'    -- 批量输出的间隔
);
```

> Upsert 需要定义 PRIMARY KEY。

## WITH 参数

| 参数值                     | 必填 | 默认值 | 描述                                                         |
| :------------------------- | :--- | :----- | :----------------------------------------------------------- |
| connector                  | 是   | 无     | 连接数据库时，需要填写 `'jdbc'`。                            |
| url                        | 是   | 无     | JDBC 数据库的连接 URL。                                      |
| table-name                 | 是   | 无     | 数据库表名。                                                 |
| driver                     | 否   | 无     | JDBC Driver 的类名。如果不输入，则自动从 url 中推断。        |
| username                   | 否   | 无     | 数据库用户名。`'username'` 和`'password'` 必须同时使用。     |
| password                   | 否   | 无     | 数据库密码。                                                 |
| scan.partition.column      | 否   | 无     | 指定对输入分区扫描（Partitioned Scan）的列名，该列必须是数值类型、日期类型、时间戳类型等。关于分区扫描的细节，可参见 [分区扫描](#jump)。 |
| scan.partition.num         | 否   | 无     | 分区扫描启用后，指定分区数。                                 |
| scan.partition.lower-bound | 否   | 无     | 分区扫描启用后，指定首个分区的最小值。                       |
| scan.partition.upper-bound | 否   | 无     | 分区扫描启用后，指定最后一个分区的最大值。                   |
| scan.fetch-size            | 否   | 0      | 每次从数据库读取时，批量获取的行数。默认为0，表示一行一行读取，效率较低（吞吐量不高）。 |
| lookup.cache.max-rows      | 否   | 无     | 查询缓存（Lookup Cache）中最多缓存的数据条数。               |
| lookup.cache.ttl           | 否   | 无     | 查询缓存中每条记录最长的缓存时间。                           |
| lookup.max-retries         | 否   | 3      | 数据库查询失败时，最多重试的次数。                           |
| sink.buffer-flush.max-rows | 否   | 100    | 批量输出时，缓存中最多缓存多少数据。如果设置为0，表示禁止输出缓存。 |
| sink.buffer-flush.interval | 否   | 1s     | 批量输出时，每批次最大的间隔（毫秒）。**如果 `'sink.buffer-flush.max-rows'` 设为 `'0'`，而这个选项不为零，则说明启用纯异步输出功能，即数据输出到算子、从算子最终写入数据库这两部分线程完全解耦。** |
| sink.max-retries           | 否   | 3      | 数据库写入失败时，最多重试的次数。                           |

## 代码示例

```sql
CREATE TABLE `jdbc_source_table` (
    `id` INT,
    `name` STRING
) WITH (
    -- 指定数据库连接参数
    'connector' = 'jdbc',
    'url' = 'jdbc:mysql://10.1.28.93:3306/CDB?rewriteBatchedStatements=true&serverTimezone=Asia/Shanghai', -- 请替换为您的实际 MySQL 连接参数
    'table-name' = 'my-table', -- 需要写入的数据表
    'username' = 'admin',      -- 数据库访问的用户名（需要提供 INSERT 权限）
    'password' = 'MyPa$$w0rd',  -- 数据库访问的密码
    'scan.partition.column' = 'id',   -- 分区扫描列名
    'scan.partition.num' = '2',       -- 分区数量
    'scan.partition.lower-bound' = '0', -- 首个分区的最小值
    'scan.partition.upper-bound' = '100', -- 最后一个分区的最大值
    'scan.fetch-size' = '1' -- 每次从数据库读取时，批量获取的行数
);
CREATE TABLE `jdbc_upsert_sink_table` (
    `id` INT PRIMARY KEY NOT ENFORCED,
    `name` STRING
) WITH (
    -- 指定数据库连接参数
    'connector' = 'jdbc',
    'url' = 'jdbc:mysql://10.1.28.93:3306/CDB?rewriteBatchedStatements=true&serverTimezone=Asia/Shanghai', -- 请替换为您的实际 MySQL 连接参数
    'table-name' = 'my-upsert-table', -- 需要写入的数据表
    'username' = 'admin',             -- 数据库访问的用户名（需要提供 INSERT 权限）
    'password' = 'MyPa$$w0rd',        -- 数据库访问的密码
    'sink.buffer-flush.max-rows' = '200',  -- 批量输出的条数
    'sink.buffer-flush.interval' = '2s'    -- 批量输出的间隔
);
insert into jdbc_upsert_sink_table select * from jdbc_source_table;
```

## 主键说明

- 对于 Append（Tuple）数据，作业 DDL 不需要设置主键，JDBC 数据库的表也不需要定义主键，也不建议定义主键（否则可能因为重复数据而造成写入失败）。
- 对于 Upsert 数据，JDBC 数据库的表**必须**定义主键，并需要在 DDL 语句的 CREATE TABLE 中，将相应列名也加上 `PRIMARY KEY NOT ENFORCED` 约束。

> ! 
> - 对于 MySQL 表，Upsert 功能的实现依赖于 `INSERT .. ON DUPLICATE KEY UPDATE ..` 语法，常见版本的 MySQL 均支持该语法。
> - 对于 PostgreSQL 表，Upsert 功能实现依赖于 `INSERT .. ON CONFLICT .. DO UPDATE SET ..` 语法，该语法需要 PostgreSQL 9.5 及以上版本才可支持。
> - 对于 Oracle 表，Upsert 功能实现依赖`MERGE .. INTO .. USING ON .. WHEN UPDATE .. WHEN INSERT ..`语法，该语法需要 Oracle 9i 及以上版本才可以支持。

[](id:jump)

## 分区扫描
分区扫描（Partitioned Scan）可以加速多个并行度的 Source 算子读取 JDBC 数据表，每个子任务可以读取自己的专属分区。使用该功能时，所有四个 `scan.partition` 开头的参数都必须指定，否则会报错。

> ! 这里的 `scan.partition.upper-bound` 指定的最大值和 `scan.partition.lower-bound` 指定的最小值，指的是每个分区的步长，不会影响最终读取的数据条数和精确性。

## 读取缓存
Flink 提供了读取缓存（Lookup Cache）功能，可以提升维表读取的性能。目前该缓存的实现是同步的，默认未启用（每次请求都会读取数据库，吞吐量很低），必须手动设置 `lookup.cache.max-rows` 和 `lookup.cache.ttl` 两个参数来启用该功能。

> ! 如果缓存的 TTL 太长，或者缓存的条数太多，可能会造成数据库中数据更新后，Flink 作业仍然读取的是缓存中的旧数据。因此对于数据库变动敏感的作业，请谨慎使用缓存功能。

## 批量写入优化
通过设置 sink.buffer-flush 开头的两个参数，可以实现批量写入数据库。建议配合相应底层数据库的参数，以达到更好的批量写入效果，否则底层仍然会一条一条写入，效率不高。

- 对于 MySQL，建议在 url 连接参数后加入 rewriteBatchedStatements=true 参数。
```
jdbc:mysql://10.1.28.93:3306/CDB?rewriteBatchedStatements=true
```
- 对于 PostgreSQL，建议在 url 连接参数后加入 reWriteBatchedInserts=true 参数。
```
jdbc:postgresql://10.1.28.93:3306/PG?reWriteBatchedInserts=true&?currentSchema=数据库的Schema
```
