## 介绍
JDBC-PG Connector 提供了对 CDW PostgreSQL 数据库写支持。

## 版本说明

| Flink 版本 | 说明     |
| ---------- | -------- |
| 1.11       | 暂不支持 |
| 1.13       | 支持     |

## 使用范围

支持用作数据目的表（sink），用于 Tuple 数据流表和用于 Upsert 数据流表（需要指定主键）。

## DDL 定义
### 用作数据目的（Tuple Sink）
```
CREATE TABLE `jdbc_sink_table` (
    `id` INT,
    `name` STRING
) WITH (
    -- 指定数据库连接参数
    'connector' = 'jdbcPG',
    'url' = 'jdbc:postgresql://10.1.28.93:3306/CDB?rewriteBatchedStatements=true&serverTimezone=Asia/Shanghai', -- 请替换为您的实际 PG 连接参数
    'table-name' = 'my-table',  -- 需要写入的数据表
    'username' = 'admin',       -- 数据库访问的用户名（需要提供 INSERT 权限）
    'password' = 'MyPa$$w0rd',  -- 数据库访问的密码
    'sink.buffer-flush.max-rows' = '200',  -- 批量输出的条数
    'sink.buffer-flush.interval' = '2s'    -- 批量输出的间隔
);
```

### 用作数据目的（Upsert Sink）

```
CREATE TABLE `jdbc_upsert_sink_table` (
    `id` INT PRIMARY KEY NOT ENFORCED,
    `name` STRING
) WITH (
    -- 指定数据库连接参数
    'connector' = 'jdbcPG',
    'url' = 'jdbc:postgresql://10.1.28.93:3306/CDB?rewriteBatchedStatements=true&serverTimezone=Asia/Shanghai', -- 请替换为您的实际 PG 连接参数
    'table-name' = 'my-upsert-table', -- 需要写入的数据表
    'username' = 'admin',             -- 数据库访问的用户名（需要提供 INSERT 权限）
    'password' = 'MyPa$$w0rd',        -- 数据库访问的密码
    'sink.buffer-flush.max-rows' = '200',  -- 批量输出的条数
    'sink.buffer-flush.interval' = '2s'    -- 批量输出的间隔
);
```

>! Upsert 需要定义 PRIMARY KEY。

## WITH 参数

| 参数值                     | 必填 | 默认值 | 描述                                                         |
| -------------------------- | ---- | ------ | ------------------------------------------------------------ |
| connector                  | 是   | 无     | 连接数据库时，需要填写 `'jdbc'`。                            |
| url                        | 是   | 无     | JDBC 数据库的连接 URL。                                      |
| table-name                 | 是   | 无     | 数据库表名。                                                 |
| driver                     | 否   | 无     | JDBC Driver 的类名。如果不输入，则自动从 url 中推断。        |
| username                   | 否   | 无     | 数据库用户名。`'username'` 和`'password'` 必须同时使用。     |
| password                   | 否   | 无     | 数据库密码。                                                 |
| scan.partition.column      | 否   | 无     | 指定对输入分区扫描（Partitioned Scan）的列名，该列必须是数值类型、日期类型、时间戳类型等。关于分区扫描的细节，可参见 [分区扫描](https://cloud.tencent.com/document/product/849/48312#jump)。 |
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
```
CREATE TABLE jdbc_upsert_sink_table (
  id INT ,
  age INT,
  name STRING,
  PRIMARY KEY (id) NOT ENFORCED -- 如果要同步的数据库表定义了主键, 则这里也需要定义
) WITH (
    -- 指定数据库连接参数
    'connector' = 'jdbcPG',
    'url' = 'jdbc:postgresql://10.0.0.2:5436/postgres', 
    'table-name' = 'my-upsert-table', -- 需要写入的数据表
    'username' = 'admin',             -- 数据库访问的用户名（需要提供 INSERT 权限）
    'password' = 'password',        -- 数据库访问的密码
    'sink.buffer-flush.max-rows' = '300',  -- 批量输出的条数
    'sink.buffer-flush.interval' = '100s'    -- 批量输出的间隔
);


-- MySQL CDC Source。配合 flink-connector-mysql-cdc 使用。要求 MySQL 版本 >= 5.7
-- 参见 https://cloud.tencent.com/document/product/849/52698
CREATE TABLE mysql_cdc_source_table (
  id INT,
  age INT,
  name STRING,
  PRIMARY KEY (id) NOT ENFORCED -- 如果要同步的数据库表定义了主键, 则这里也需要定义
) WITH (
  'connector' = 'mysql-cdc',	  -- 固定值 'mysql-cdc'
  'hostname' = '10.0.0.6',   -- 数据库的 IP
  'port' = '3360',                -- 数据库的访问端口
  'username' = 'root',        -- 数据库访问的用户名（需要提供 SHOW DATABASES、REPLICATION SLAVE、REPLICATION CLIENT、SELECT 和 RELOAD 权限）
  'password' = 'password',    -- 数据库访问的密码
  -- 'scan.incremental.snapshot.enabled' = 'false' -- 如果 source 表没有设置 PRIMARY Key，需要启用该设置 
  'database-name' = 'database',   -- 需要同步的数据库
  'table-name' = 'table'      -- 需要同步的数据表名
);


INSERT INTO jdbc_upsert_sink_table select * from mysql_cdc_source_table;
```

## 主键说明
- 对于 Append（Tuple）数据，作业 DDL 不需要设置主键，JDBC 数据库的表也不需要定义主键，也不建议定义主键（否则可能因为重复数据而造成写入失败）。
- 对于 Upsert 数据，JDBC 数据库的表**必须**定义主键，并需要在 DDL 语句的 CREATE TABLE 中，将相应列名也加上 `PRIMARY KEY NOT ENFORCED` 约束。

> !Upsert 功能实现不依赖于 `INSERT .. ON CONFLICT .. DO UPDATE SET ..` 语法，而是依赖于攒批 upsert +攒批 delete。该语法兼容 PostgreSQL 9.5以下版本。

## 批量写入优化

通过设置 sink.buffer-flush 开头的两个参数，可以实现批量写入数据库。建议配合相应底层数据库的参数，以达到更好的批量写入效果，否则底层仍然会一条一条写入，效率不高。
- 对于 PostgreSQL，建议在 url 连接参数后加入 reWriteBatchedInserts=true 参数。
```
jdbc:postgresql://10.1.28.93:3306/PG?reWriteBatchedInserts=true&?currentSchema=数据库的Schema
```
