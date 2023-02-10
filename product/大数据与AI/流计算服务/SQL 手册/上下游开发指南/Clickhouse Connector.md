## 介绍
ClickHouse Sink Connector 提供了对 ClickHouse 数据仓库的写入支持。ClickHouse Source Connector 提供了 ClickHouse 作为批数据源和维表的功能。

## 版本说明

| Flink 版本 | 说明                |
| :--------- | :------------------ |
| 1.11       | 支持 Sink           |
| 1.13       | 支持 Source 和 Sink |
| 1.14       | 支持 Source 和 Sink |

## 使用范围
ClickHouse 不支持标准的 update 和 delete 操作。作为 Sink 时，若您的任务有 update 和 delete 操作，可以通过 [CollapsingMergeTree](https://clickhouse.tech/docs/en/engines/table-engines/mergetree-family/collapsingmergetree/) 来实现。

对于 JAR 作业，Java/Scala 编写的作业可以参考 [JDBC](https://cloud.tencent.com/document/product/849/48312) 方式写入 ClickHouse，这里不做阐述。

## DDL 定义
### 用作数据目的（不包含更新）（Sink with insert only）
```sql
CREATE TABLE clickhouse_sink_table (
   `id` INT,
   `name` STRING
) WITH (
   -- 指定数据库连接参数
   'connector' = 'clickhouse',                       -- 指定使用clickhouse连接器
   'url' = 'clickhouse://172.28.28.160:8123',        -- 指定集群地址，可以通过ClickHouse集群界面查看
   -- 如果ClickHouse集群未配置账号密码可以不指定
   --'username' = 'root',                            -- ClickHouse集群用户名
   --'password' = 'root',                            -- ClickHouse集群的密码
   'database-name' = 'db',                           -- 数据写入目的数据库
   'table-name' = 'table',                           -- 数据写入目的数据表
   'sink.batch-size' = '1000'                        -- 触发批量写的条数
);
```

### 包含 update 和 delete 操作的数据目的（Sink with upsert）
```sql
CREATE TABLE clickhouse_upsert_sink_table (
   `id` INT,
   `name` STRING,
  PRIMARY KEY (`id`) NOT ENFORCED -- 如果要同步的数据库表定义了主键, 则这里也需要定义
) WITH (
   -- 指定数据库连接参数
   'connector' = 'clickhouse',                     -- 指定使用clickhouse连接器
   'url' = 'clickhouse://172.28.28.160:8123',      -- 指定集群地址，可以通过ClickHouse集群界面查看
   -- 如果ClickHouse集群未配置账号密码可以不指定
   --'username' = 'root',                          -- ClickHouse集群用户名
   --'password' = 'root',                          -- ClickHouse集群的密码
   'database-name' = 'db',                         -- 数据写入目的数据库
   'table-name' = 'table',                         -- 数据写入目的数据表
   'table.collapsing.field' = 'Sign',              -- CollapsingMergeTree 类型列字段的名称
   'sink.batch-size' = '1000'                      -- 触发批量写的条数
);
```

>! 一定要定义 pk 和申明 table.collapsing.field 字段，才会启动该功能。对应的 ClickHouse 建表语句，请参考 [常见问题](#ID)。

### 作为批数据源
```
CREATE TABLE `clickhosue_batch_source` (
    `when`     TIMESTAMP,
    `userid`   BIGINT,
    `bytes`    FLOAT
) WITH (
    'connector' = 'clickhouse',
    'url' = 'clickhouse://172.28.1.21:8123',
    'database-name' = 'dts',
    'table-name' = 'download_dist'
--    'scan.by-part.enabled' = 'false', -- 是否启用读 ClickHouse 表 part。若启用，必须先在所有节点上使用命令 'STOP MERGES' 和 'STOP TTL MERGES' 停止表的后台 merge 和基于 TTL 的数据删除操作，否则读取的数据会不正确。
--    'scan.part.modification-time.lower-bound' = '2021-09-24 16:00:00', -- 用于根据 modification_time 过滤 ClickHouse 表 part 的最小时间（包含），格式 yyyy-MM-dd HH:mm:ss。
--     'scan.part.modification-time.upper-bound' = '2021-09-17 19:16:26', -- 用于根据 modification_time 过滤 ClickHouse 表 part 的最大时间（不包含），格式 yyyy-MM-dd HH:mm:ss。
--    'local.read-write' = 'false', -- 是否读本地表，默认 false 。
--    'table.local-nodes' = '172.28.1.24:8123,172.28.1.226:8123,172.28.1.109:8123,172.28.1.36:8123' -- local node 列表，需要使用 http port。注意一个 shard 只能配置一个 replica 节点地址，否则会读取到重复数据。
);
```

>! MergeTree 系列引擎才支持按 part 读取，且一定要停止待读取表所有节点的后台 merge 和基于 TTL 的数据删除操作，避免 part 变化导致数据读取不准确。本地读时一个 shard 只能配置一个 replica 地址，避免重复数据。

### 作为维表
```
CREATE TABLE `clickhouse_dimension` (
    `userid` BIGINT,
    `comment` STRING
) WITH (
    'connector' = 'clickhouse',
    'url' = 'clickhouse://172.28.1.21:8123',
    'database-name' = 'dimension',
    'table-name' = 'download_dist',
    'lookup.cache.max-rows' = '500', -- 查询缓存（Lookup Cache）中最多缓存的数据条数。
    'lookup.cache.ttl' = '10min', -- 查询缓存中每条记录最长的缓存时间。
    'lookup.max-retries' = '10' -- 数据库查询失败时，最多重试的次数。
);
```

##  WITH 参数

| 参数值                                  | 必填 | 默认值           | 描述                                                         |
| :-------------------------------------- | :--- | :--------------- | :----------------------------------------------------------- |
| connector                               | 是   | -                | 当要使用 ClickHouse 作为数据目的（Sink）需要填写，取值 `clickhouse` 。 |
| url                                     | 是   | -                | ClickHouse 集群连接 url，可以通过集群界面查看，举例 'clickhouse://127.1.1.1:8123'。 |
| username                                | 否   | -                | ClickHouse 集群用户名。                                      |
| password                                | 否   | -                | ClickHouse 集群密码。                                        |
| database-name                           | 是   | -                | ClickHouse 集群数据库。                                      |
| table-name                              | 是   | -                | ClickHouse 集群数据表。                                      |
| sink.batch-size                         | 否   | 1000             | Connector batch 写入的条数。                                 |
| sink.flush-interval                     | 否   | 1000 （单位 ms） | Connector 异步线程刷新写入 ClickHouse 间隔。                 |
| table.collapsing.field                  | 否   | -                | CollapsingMergeTree 类型列字段的名称。                       |
| sink.max-retries                        | 否   | 3                | 写入失败时的重试次数。                                       |
| local.read-write                        | 否   | false            | 是否启用直写本地表功能。默认不开启。<br>注意：该功能仅供高级用户使用，需配合下面几个参数使用。详见本文后续的 ”写入本地表“ 章节。 |
| table.local-nodes                       | 否   | -                | 启用写本地表（`local.read-write` 为 `true`）时，local node 列表，举例 '127.1.1.10:8123,127.1.2.13:8123'（**需要使用 http port**）。 |
| sink.partition-strategy                 | 否   | balanced         | 启用写本地表（`local.read-write` 为 `true`）时，需要设置数据分发策略，支持 balanced/shuffle/hash。如果希望实现数据的动态更新，且表引擎使用 CollapsingMergeTree，则取值必须为 `hash`，且需要配合 `sink.partition-key` 一同使用。<br>取值说明：`balanced ` 轮询模式写入，`shuffle ` 随机挑选节点写入， `hash ` 根据 `sink.partition-key` 的 hash 值，选择节点写入。 |
| sink.partition-key                      | 否   | -                | 启用写本地表（`local.read-write` 为 `true`），且 `sink.partition-strategy` 为  `hash ` 时需要设置，值为所定义表中的主键。如果主键包含多个字段，则需要指定为第一个字段。 |
| sink.ignore-delete                      | 否   | false            | 启用该参数后，会过滤所有向 ClickHouse 写入的 DELETE（删除）消息。该选项适用于使用 ReplacingMergeTree 表引擎，并期望实现数据的动态更新的场景。 |
| sink.backpressure-aware                 | 否   | false            | 当 Flink 日志频繁出现 "Too many parts" 报错，且作业因此崩溃时，启用该参数可以大幅减轻服务端负载，提升整体的吞吐量和稳定性。 |
| sink.max-partitions-per-insert          | 否   | 20               | 当clickhouse是分区表，且分区函数CK内置为intHash32、toYYYYMM 或toYYYYMMDD 之一时，Flink写入Clickhouse会通过预先在sink端按分区攒数据buffer，当攒的分区数目到达设定值时会触发往下游clickhouse写入（如果`sink.flush-interval` 和`sink.batch-size`  先到的话也会先触发写入），极大的提高写入clickhouse的吞吐效率。设置为-1时会关闭分区聚合写入功能。 |
| scan.fetch-size                         | 否   | 100              | 每次从数据库读取时，批量获取的行数。                         |
| scan.by-part.enabled                    | 否   | false            | 是否启用读 ClickHouse 表 part。若启用，必须先在所有节点上使用命令'STOP MERGES'和'STOP TTL MERGES'停止表的后台 merge 和基于 TTL 的数据删除操作，否则读取的数据会不正确。 |
| scan.part.modification-time.lower-bound | 否   | -                | 用于根据 modification_time 过滤 ClickHouse 表  part 的最小时间（包含），格式 yyyy-MM-dd HH:mm:ss。 |
| scan.part.modification-time.upper-bound | 否   | -                | 用于根据 modification_time 过滤 ClickHouse 表  part 的最大时间（不包含），格式 yyyy-MM-dd HH:mm:ss。 |
| lookup.cache.max-rows                   | 否   | 无               | 查询缓存（Lookup Cache）中最多缓存的数据条数。               |
| lookup.cache.ttl                        | 否   | 无               | 查询缓存中每条记录最长的缓存时间。                           |
| lookup.max-retries                      | 否   | 3                | 数据库查询失败时，最多重试的次数。                           |


>!定义 WITH 参数时，通常只需要填写必填参数即可。当您启用非必须参数时，请您一定要明确参数含义以及可能对数据写入产生的影响。

## 类型映射

关于 ClickHouse 支持的数据类型定义及其使用，可参考 [ClickHouse data-types](https://clickhouse.tech/docs/en/sql-reference/data-types/)，这里列举了常用的数据类型，及其与 Flink 类型的对应关系。

| Flink 数据类型                 | ClickHouse 对应数据类型                                      |
| :----------------------------- | :----------------------------------------------------------- |
| VARCHAR                        | String/FixedString(N)                                        |
| STRING                         | String/FixedString(N)                                        |
| BOOLEAN                        | 没有单独类型存储，可以使用 UInt8 来存储布尔类型，将取值限制为0或1；或者使用字符串存储 true/false 来表示 |
| DECIMAL                        | Decimal32(S)/Decimal64(S)/Decimal128(S)                      |
| TINYINT                        | Int8                                                         |
| SMALLINT                       | Int16                                                        |
| INTEGER                        | Int32                                                        |
| BIGINT                         | Int64                                                        |
| FLOAT                          | Float32                                                      |
| DOUBLE                         | Float64                                                      |
| DATE                           | Date                                                         |
| TIMESTAMP                      | DateTime                                                     |
| TIMESTAMP WITH LOCAL TIME ZONE | DateTime，示例 DateTime64(3, 'Asia/Shanghai')                |
| Array                          | Array                                                        |
| Map                            | Map                                                          |
| Row                            | Tuple                                                        |

## 代码示例

```sql
CREATE TABLE datagen_source_table ( 
	id INT, 
	name STRING 
) WITH ( 
   'connector' = 'datagen',
   'rows-per-second'='1'  -- 每秒产生的数据条数
);
CREATE TABLE clickhouse_sink_table (
   `id` INT,
   `name` STRING
) WITH (
   -- 指定数据库连接参数
   'connector' = 'clickhouse',                       -- 指定使用clickhouse连接器
   'url' = 'clickhouse://172.28.28.160:8123',        -- 指定集群地址，可以通过ClickHouse集群界面查看
   -- 如果ClickHouse集群未配置账号密码可以不指定
   --'username' = 'root',                            -- ClickHouse集群用户名
   --'password' = 'root',                            -- ClickHouse集群的密码
   'database-name' = 'db',                           -- 数据写入目的数据库
   'table-name' = 'table',                           -- 数据写入目的数据表
   'sink.batch-size' = '1000'                        -- 触发批量写的条数
);
insert into clickhouse_sink_table select * from datagen_source_table;
```

## 常见问题
### 关于数据更新（Upsert）和删除（Delete）语义
对于需要动态更新和删除数据的场景，由于 ClickHouse 并不完全支持 Upsert 语义，我们通常使用 ReplacingMergeTree 或 CollapsingMergeTree 来模拟更新或删除操作，他们有各自的适用场景。

#### ReplacingMergeTree 表引擎

如果 ClickHouse 底层表引擎使用 ReplacingMergeTree，则可以设置 `sink.ignore-delete  ` 参数为 `true`。此后 Flink 会自动过滤所有的删除（DELETE）消息，并将插入（INSERT）和更新（UPDATE_AFTER）消息则统一转为插入（INSERT）消息。随后，ClickHouse 底层会自动使用最新写入的记录来覆盖之前同主键的旧记录，从而实现数据的更新。

需要注意的是，此模式只支持插入、更新，而**不支持删除**数据。因此如果对于 CDC 等需要精确同步的简单 ETL 场景，则使用下面介绍的 CollapsingMergeTree 表引擎会有更好的效果。

#### CollapsingMergeTree 表引擎

如果 ClickHouse 底层表引擎使用 CollapsingMergeTree，则可以通过 `table.collapsing.field` 参数来指定 Sign 字段。它的原理是通过发送内容相同，但符号（Sign）相反的消息，来实现旧数据的删除（抵消），以及新数据的插入。

此外，在生产环境中，一般会使用 ReplicatedCollapsingMergeTree，而 `ReplicatedMergeTree` 的自动去重可能会使得短期内多次写入到 ClickHouse 的数据被判断为重复数据，导致数据丢失。此时，可在建表（或者修改表）时，指定 `replicated_deduplication_window=0`，以关闭自动去重功能。

例如：

```sql
CREATE TABLE testdb.testtable on cluster default_cluster (`id` Int32,`name` Nullable(String),`age` Nullable(Int32),`weight` Nullable(Float64),`Sign` Int8) ENGINE = ReplicatedCollapsingMergeTree('/clickhouse/tables/{layer}-{shard}/testdb/testtable', '{replica}', Sign) ORDER BY id SETTINGS  replicated_deduplication_window = 0;
```

自动去重更多详情可参见 [Data Replication](https://clickhouse.tech/docs/en/engines/table-engines/mergetree-family/replication/)。

#### ClickHouse 分布式表的 sharding_key

创建分布式表时，语句中的 `ENGINE = Distributed(cluster_name, database_name, table_name[, sharding_key]);` 中 sharding_key 需为 Flink SQL 的 sink 表中的主键（Primary Key），**以保证同一个 Primary Key 的记录写入到同一个节点中**。

**各个参数的含义分别如下：**

- cluster_name：集群名称，与集群配置中的自定义名称相对应。
- database_name：数据库名称。
- table_name：表名称。
- sharding_key：选填，用于分片的 key 值，在数据写入的过程中，分布式表会依据分片 key 的规则，将数据分布到各个节点的本地表。

### 写入本地表（高级内容）

如果将 `local.read-write ` 参数设置为 `true`，则 Flink 可以直接写入本地表。

> !
>
> 启用写本地表功能后，吞吐量可能会大幅提升。但是如果后续 ClickHouse 集群发生扩容、缩容、节点替换时，可能造成数据分布不均匀甚至写入失败、数据无法更新。因此仅供高级用户使用。

如果表含有主键，且使用了 UPDATE 和 DELETE 语义，建议建表时使用 CollapsingMergeTree 表引擎。我们可以通过 `table.collapsing.field` 参数来指定 Sign 字段，并设置 `sink.partition-strategy` 为 `hash` 以令相同主键的数据落在同一个 shard 上，并将 `sink.partition-key  ` 参数设置为主键字段（对于多字段的混合主键，则设置为第一个字段）。

### 关于 null 数据

若数据的某些字段可能为空，则需要在 ClickHouse 的建表语句（DDL）中，把字段声明改为 Nullable，否则会导致数据写入异常。

```sql
CREATE TABLE testdb.testtable on cluster default_cluster (`id` Int32,`name` Nullable(String),`age` Nullable(Int32),`weight` Nullable(Float64),`Sign` Int8) ENGINE = ReplicatedCollapsingMergeTree('/clickhouse/tables/{layer}-{shard}/testdb/testtable', '{replica}', Sign) ORDER BY id ;
```

### 分区表写入优化

Oceanus 在写入到 Clickhouse 分区表时，如果 clickhouse 的分区定义中使用的函数在 Oceanus 的支持范围内（intHash32、toYYYYMM、toYYYYMMDD），写入时默认会开启按分区预先攒 buffer 数据再写入的功能。启用后，Oceanus 单批次写入数据会包含尽量少的分区数量（业务分区数据吞吐足够大时，每个批次仅包含一个分区），从而提高 ClickHouse 的 merge 性能。如果单个分区数据不够批大小时，多个分区数据合并成一个批次写入 ClickHouse。详细的配置项可以参见上文中`sink.max-partitions-per-insert` 参数。



### 示例：ClickHouse 建表语句

#### 支持 UPDATE、DELETE 的 CollapsingMergeTree 建表语句

```sql
-- 创建数据库
CREATE DATABASE test ON cluster default_cluster;

-- 创建本地表
CREATE TABLE test.datagen ON cluster default_cluster (`id` Int32,`name` Nullable(String),`age` Nullable(Int32),`weight` Nullable(Float64),`Sign` Int8) ENGINE = ReplicatedCollapsingMergeTree('/clickhouse/tables/{layer}-{shard}/test/datagen', '{replica}', Sign) ORDER BY id SETTINGS replicated_deduplication_window = 0;

-- 基于本地表，创建分布式表
CREATE TABLE test.datagen_all ON CLUSTER default_cluster AS test.datagen ENGINE = Distributed(default_cluster, test, datagen, id);
```

#### 仅包含 INSERT 的普通 MergeTree 建表语句

```sql
-- 创建数据库
CREATE DATABASE test ON cluster default_cluster;

-- 创建本地表
CREATE TABLE test.datagen ON cluster default_cluster (`id` Int32,`name` Nullable(String),`age` Nullable(Int32),`weight` Nullable(Float64) ) ENGINE = ReplicatedMergeTree('/clickhouse/tables/{layer}-{shard}/test/datagen', '{replica}') ORDER BY id SETTINGS replicated_deduplication_window = 0;

-- 基于本地表，创建分布式表
CREATE TABLE test.datagen_all ON CLUSTER default_cluster AS test.datagen ENGINE = Distributed(default_cluster, test, datagen, id);
```
