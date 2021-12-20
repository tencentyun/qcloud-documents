## 介绍
Kudu Connector 提供了对 Kudu 的读写支持。

## 版本说明

| Flink 版本 | 说明 |
| :-------- | :--- |
| 1.11      | 支持 |
| 1.13      | 支持 |

## 使用范围
Kudu Connector 支持用作数据源表（Source，仅限于普通和维表 JOIN 的右表），也可以作为 Tuple 数据流的目的表（Sink），还可以作为 Upsert 数据流的目的表（Sink，需要包含主键）。

## DDL 定义
### 用作数据源（Source）
```sql
CREATE TABLE `kudu_source_table` (
	`id` INT,
	`name` STRING
) WITH (
	-- 指定Kudu连接参数
	'connector.type' = 'kudu',
	'kudu.masters' = 'master-01:7051,master-02:7051,master-03:7051', -- 连接地址
	'kudu.table' = 'TableName1', -- 替换为 Kudu 中对应的表，如 default.TestTable1
	'kudu.hash-columns' = 'id', -- 可选参数，Hash 键
	'kudu.primary-key-columns' = 'id', -- 可选参数，主键
	'kudu.operation-timeout' = '10000', -- 可选参数，插入超时时间
	'kudu.max-buffer-size' = '2000', -- 可选参数，buffer 大小
	'kudu.flush-interval' = '1000' -- 可选参数，刷新数据到 kudu 的时间间隔
);
```

### 用作数据目的（Tuple Sink）
```sql
CREATE TABLE `kudu_sink_table` (
	`id` INT,
	`name` STRING
) WITH (
	-- 指定Kudu连接参数
	'connector.type' = 'kudu',
	'kudu.masters' = 'master-01:7051,master-02:7051,master-03:7051', -- 连接地址
	'kudu.table' = 'TableName1', -- 替换为Kudu中对应的表，如 default.TestTable1
	'kudu.igonre-duplicate' = 'true' --可选参数，为 true 时会忽略主键重复的数据
);
```

### 用作数据目的（Upsert Sink）

```sql
CREATE TABLE `kudu_upsert_sink_table` (
	`id` INT,
	`name` STRING
) WITH (
	-- 指定 Kudu 连接参数
	'connector.type' = 'kudu',
	'kudu.masters' = 'master-01:7051,master-02:7051,master-03:7051', -- 连接地址
	'kudu.table' = 'TableName1', -- 替换为 Kudu 中对应的表，如default.TestTable1
	'kudu.hash-columns' = 'id', -- 可选参数，Hash 键
	'kudu.primary-key-columns' = 'id' -- 必选参数，主键。Upsert Sink 需要包含主键。
);
```

## WITH 参数

| 参数值                   | 必填 | 默认值 | 描述                                                         |
| :----------------------- | :--- | :----- | :----------------------------------------------------------- |
| connector.type           | 是   | 无     | 连接 Kudu 数据库时，需要填写 `'kudu'`                        |
| kudu.masters             | 是   | 无     | Kudu 数据库 MasterServer 的连接地址。端口默认为7051。若使用腾讯云的 Kudu 组件，master 地址和端口可以在 [弹性 MapReduce 控制台](https://console.cloud.tencent.com/emr) 的集群列表，单击集群 **ID/名称**，进入集群详情页，然后在**集群服务 > Kudu > 操作 > 查看端口**中找到对应的 master server IP 和端口 |
| kudu.table               | 是   | 无     | 数据库表名。例如 Impala 创建的 kudu 内表一般为 `impala::db_name.table_name`，Java API 创建的 Kudu 表 `db_name.tablename` |
| kudu.hash-columns        | 否   | 无     | Hash 键                                                      |
| kudu.primary-key-columns | 否   | 无     | 主键                                                         |
| kudu.replicas            | 否   | 无     | 副本数量                                                     |
| kudu.operation-timeout   | 否   | 30000  | 插入超时时间，单位为毫秒                                     |
| kudu.max-buffer-size     | 否   | 1000   | 默认为1000                                                   |
| kudu.flush-interval      | 否   | 1000   | 默认为1000                                                   |
| kudu.ignore-not-found    | 否   | false  | 是否忽略未找到的数据                                         |
| kudu.ignore-duplicate    | 否   | false  | 插入数据时是否会忽略主键重复的数据                           |

## 类型映射

| Flink 类型   | Kudu            |
| :----------- | :-------------- |
| STRING       | STRING          |
| BOOLEAN      | BOOL            |
| TINYINT      | INT8            |
| SMALLINT     | INT16           |
| INT          | INT32           |
| BIGINT       | INT64           |
| FLOAT        | FLOAT           |
| DOUBLE       | DOUBLE          |
| BYTES        | BINARY          |
| TIMESTAMP(3) | UNIXTIME_MICROS |

## 代码示例

```sql
CREATE TABLE `kudu_source_table` (
	`id` INT,
	`name` STRING
) WITH (
	-- 指定Kudu连接参数
	'connector.type' = 'kudu',
	'kudu.masters' = 'master-01:7051,master-02:7051,master-03:7051', -- 连接地址
	'kudu.table' = 'TableName1', -- 替换为 Kudu 中对应的表，如 default.TestTable1
	'kudu.hash-columns' = 'id', -- 可选参数，Hash 键
	'kudu.primary-key-columns' = 'id', -- 可选参数，主键
	'kudu.operation-timeout' = '10000', -- 可选参数，插入超时时间
	'kudu.max-buffer-size' = '2000', -- 可选参数，buffer 大小
	'kudu.flush-interval' = '1000' -- 可选参数，刷新数据到 kudu 的时间间隔
);
CREATE TABLE `kudu_upsert_sink_table` (
	`id` INT,
	`name` STRING
) WITH (
	-- 指定 Kudu 连接参数
	'connector.type' = 'kudu',
	'kudu.masters' = 'master-01:7051,master-02:7051,master-03:7051', -- 连接地址
	'kudu.table' = 'TableName1', -- 替换为 Kudu 中对应的表，如default.TestTable1
	'kudu.hash-columns' = 'id', -- 可选参数，Hash 键
	'kudu.primary-key-columns' = 'id' -- 必选参数，主键。Upsert Sink 需要包含主键。
);
insert into kudu_upsert_sink_table select * from kudu_source_table;
```

## 注意事项

1. 若需要使用 Impala 查询 Kudu 数据库的表时，需确认是否已经创建了对应的外表。
2. 非 Impala-shell 创建的表，默认在 Impala 中没有对应的外表，需创建对应的 Kudu 外表才能查到记录。
3. Kudu 作为 Oceanus 的 Sink 端时，若 Kudu 中该表不存在，则会在 Kudu 中创建对应的内表。
