CREATE TABLE 语句用来描述数据源（Source）或者数据目的（Sink）表。

**语法：**
```sql
CREATE TABLE `表名` (
	`字段名` 字段类型
	[, `字段名` 字段类型 ]*
	[, WATERMARK FOR BOUNDED(时间戳字段名, 最大容忍乱序时间) ]
	[, WATERMARK FOR ROWS(多少行生成一次 Watermark) ]
	[, PRIMARY KEY (主键字段1, … ) ]
) WITH (
	`参数名` = '参数值'
	[, `参数名` = '参数值' ]*
)
```
其中`BOUNDED`和`ROWS`属于 Event Time 时间模式（即数据源中自带时间戳字段），而且`ROWS`和`WATERMARK`两种 WATERMARK 语句是互斥的，只可最多选择一项。

最大容忍乱序时间只在 Event Time 模式下有意义，而 Processing Time 模式不严格保证处理顺序，因为源数据没有时间戳定义。

**示例：**
```sql
CREATE TABLE KafkaSource1 (
  `time_` VARCHAR,
  `client_ip` VARCHAR,
  `method` VARCHAR,
) WITH (
  `type`='ckafka',
  `instanceId` = 'ckafka-cky18a42',
  `encoding` = 'json',
  `topic` = 'test-input'
);
```

## 数据源（Source）和数据目的（Sink）

目前流计算 Oceanus 可以根据后续的插入语句（`INSERT INTO`）和选择语句（`SELECT FROM`）自动判断源和目的表，因而用户无需显式指定源和目的表的类型，但仍然需要注意，有些数据源和数据目的会有单独的限制和特性，详情请参见创建 JAR 作业中 [准备上下游数据](https://cloud.tencent.com/document/product/849/38284) 和创建 SQL 作业中 [准备上下游数据](https://cloud.tencent.com/document/product/849/38287)。

用户可以在`CREATE TABLE`的`WITH`参数中指定数据源或数据目的类型，例如`type = 'ckafka'`表明使用 CKafka、`type = 'mysql'`表明使用腾讯云 MySQL 作为数据源等。
>!
>- 等号后面的参数必须使用半角单引号，不允许使用双引号或者全角引号。
- 通常情况下，字段名不区分大小写（例如 `type` 和 `TYPE` 等同），但单引号内部的字符串在引用外部值时要区分大小写（例如 `root` 和 `ROOT` 作为用户名时是不同的）。
- 本文的所有时间戳，均以 UTC+8（北京时间）为准。

各种数据源（Source）和数据目的（Sink）所需 WITH 参数如下：
### CKafka

| WITH 参数      | 含义                                                         | 是否必选 |
| -------------- | ------------------------------------------------------------ | ------------------- |
| type           | 当数据源、数据目的为 CKafka 时，需要指定值为`'ckafka'`。    | 是            |
| instanceId     | CKafka 的 Instance ID，可在产品列表页查看，例如`'ckafka-cky18a42'`。 | 是        |
| encoding       | 可以为`'json'`或`'csv'`，如果选择`'csv'`则需要同时指定 fieldDelimiter。 | 是            |
| topic          | Ckafka 指定 instanceId 下的 topic，表示要消费的 Kafka 主题。 |是             |
| timestampMode  | 可选项，用于指定数据源或数据目的表中 TIMESTAMP 字段时间戳的处理格式，默认值为 'AUTO'。<br>1. 对于数据源（Source）表，默认将根据输入数据的格式自动判断（仅适用于数字格式的时间戳，大于99999999999则视为`MILLISECOND`，小于等于99999999999则视为`SECOND`）。<br>2. 对于数据目的（Sink）表，默认按`MILLISECOND`格式输出时间戳类型的字段。<br>3. 若显式设定值为`'MILLISECOND'`，表示采用毫秒为单位的 Unix 时间戳。<br>4. 若显式设定值为`'SECOND'`表示采用秒为单位的 Unix 时间戳。<br>5. 如果需要自定义时间戳格式，则可以输入与 Java SimpleDateFormat 兼容的格式化字符串，例如`'yyyy-MM-dd HH:mm:SS'`可以解析为`2019-10-09 15:37:21`这样的时间戳字符串。<br>**由于默认的 AUTO 模式会对每条数据做判断，可能会略微降低性能。若在低延时、高吞吐的环境下使用，请显式指定 timestampMode 参数以获得更好的性能。** | 否             |
| fieldDelimiter | encoding 为 CSV 时可选，指定 CSV 各字段的分隔符。默认以逗号（,）分隔。**分隔符只允许填入一个半角字符，不允许多个字符作为分隔符使用；分隔符也不能为分号（;）。** | 否         |
| startMode      | 可选项，值可以为`EARLIEST`（从最早 Offset 读取）、`LATEST`（从最新 Offset 读取），也可以设置为`T+毫秒单位的 Unix 时间戳`，例如`T1560510495355`表示从2019年6月14日晚上7点08分开始读取数据。 |否        |
| ignoreErrors | 可选项，默认为 true，表示跳过错误的行，如果设为 false 则遇到错误数据会导致程序直接终止。|否|

>!
>- 如果数据中包含与分隔符相同的字符，则系统会自动使用双引号将该字符引起来以避免歧义。如果数据本身存在双引号，则会使用两个双引号（“”）来替换每个出现的双引号。
>- CKafka 只支持 Append 类型流的写入，不支持 Upsert 流。如需写入 Upsert 流，请使用【云数据库 MySQL】、【云数据库 PostgreSQL】以及【Elasticsearch Service】等支持 Upsert 数据流的腾讯云服务作为 Sink。
>- CKafka Sink 表单条数据的限制为 5MB（5242880 Byte）。单条数据超出此大小时，数据会被丢弃。如果有特殊需求，请联系我们。

### 云数据库 TencentDB

目前流计算支持云数据库 MySQL 和云数据库 PostgreSQL 作为数据目的。MySQL 也可作为数据源（受限制），作为 JOIN 条件的右表，或者`QUERY_DB_STR()`这个数据库查询 UDF 的查询表。详情请参见 [数据库查询函数](https://cloud.tencent.com/document/product/849/32997)。

| WITH 参数        | 含义                                                         | 是否必选 |
| ---------------- | ------------------------------------------------------------ | -------------------- |
| type             | 对于 MySQL，需要填写`'mysql'`；对于 PostgreSQL，需要填写为 `'postgresql'`。 | 是         |
| instanceId       | TencentDB 的实例 ID，大小写敏感。例如 MySQL 的`'cdb-xxxxxxxx'`，或者 PostgreSQL 的`'postgres-xxxxxxxx'`。 | 是                  |
| database         | 数据库名，大小写敏感。                                   |是                 |
| *schema*         | PostgreSQL 专用，模式（Schema）名，大小写敏感。          | PostgreSQL 必选      |
| table            | 表名，大小写敏感。 | 是               |
| user             | 用户名，大小写敏感。                                     | 是               |
| password         | 密码，大小写敏感。                                       | 是                  |
| maxRecordBatch   | 可选参数，大于1则启用分批写入功能，即每若干条作为一批次写入数据库。启用后，可能极大的增加吞吐量。 | 否           |
| maxRecordLatency | 可选参数，表示每批次最多等待的时间（毫秒）。如果提前达到了 maxRecordBatch 参数指定的条数，则会提前输出；如果超过本参数指定的时间，则即使该批次未达到 maxRecordBatch 参数指定的条数，也会向下游数据库发送数据。 | 否          |

> ! 
>-  如果将 MySQL 数据库用作**数据源**（例如使用 QUERY_DB_STR 函数），则流计算作业中 CREATE TABLE 所定义的表名，必须和数据库中的实际表名（WITH 参数的 table 字段）保持严格一致，否则语法检查会报错。
> - 如果将 MySQL 数据库用作数据目的，则 CREATE TABLE 所定义的表名不受限制。

数据流分为 Tuple 和 Upsert 两类。Upsert 是 Update OR Insert 的简写，即对于一条数据，如果之前输出过与其同主键的记录，则更新该记录；否则插入新的数据。
- Tuple 类型数据流，只能写入不设主键（即没有 PRIMARY KEY 语句）的数据表。
- Upsert 类型数据流，只能写入含有主键（PRIMARY KEY 语句）的数据表。

对于含主键的表（即使用 PRIMARY KEY 定义了主键），支持插入或更新（Upsert）操作，可接收由 DISTINCT、不含窗口的 JOIN、不含窗口的 GROUP BY 等操作产生的 Upsert 数据流。

**示例：Tuple 类型 MySQL 数据表，使用 Processing Time 时间模式**

对于时间模式和 WATERMARK 的介绍，参见 [WATERMARK](https://cloud.tencent.com/document/product/849/18034#watermark)。
```
CREATE TABLE `DDL_TUPLE` (
  `f1` VARCHAR,
  `f2` VARCHAR
) WITH (
  `type` = 'mysql',
  `instanceId` = 'cdb-xxxxxxxx',
  `user` = 'hello',
  `password` = 'world',
  `database` = 'MyIP',
  `table` = 'DDL_TUPLE'
);
```
此时使用 Processing Time 模式，定义了一个包含`f1`、`f2`列的 MySQL Tuple 类型的表，既可以作为有限制的数据源（Source），也可以作为数据目的（Sink）。

**示例：Upsert 类型 MySQL 数据目的表**
```
CREATE TABLE `public_traffic_output` (
  `f1` VARCHAR,
  `f2` BIGINT,
  PRIMARY KEY(`f1`)  -- 定义主键的 MySQL 表为 Upsert 类型
) WITH (
  `type` = 'mysql',
  `instanceId` = 'cdb-xxxxxxxx',
  `user` = 'hello',
  `password` = 'world',
  `database` = 'MyIP',
  `table` = 'DDL_UPSERT'
);
```
上述表定义了一个包含`f1`、`f2`列的 MySQL Upsert 类型的表，只能作为数据目的表。

## WATERMARK

### Event Time/Processing Time
对于基于窗口的操作（例如 GROUP BY、OVER、JOIN 条件中时间段的指定），流计算 Oceanus 支持 Event Time 和 Processing Time 两种时间处理模式。
![](https://main.qcloudimg.com/raw/3b1452e12aa27378ad022b23cba6896c.png)
- Event Time 模式使用输入数据自带的时间戳，容忍一定程度的乱序数据输入（例如，更早的数据由于各节点处理能力、网络波动等不可预知的原因，来的却更晚），这个参数可以通过 BOUNDED 的第二个参数指定，单位是毫秒。该处理模式最精确，但要求输入数据自带时间戳。目前只支持数据源中以 timestamp 类型定义的字段，未来将会支持虚拟列，可将其他类型的列应用处理函数转换为系统接受的时间戳。
- Processing Time 处理模式不要求输入数据有时间戳，而是将该条数据被处理的时间戳自动加入数据，并以 PROCTIME（必须全为大写）字段命名。该列是隐藏的，`SELECT *`时不会出现，只有用户手动使用时才会被读取。

>! 对于同一个任务的所有数据源，只允许采用一种时间模式。若某个使用 Event Time 模式，则必须要求所有定义的 Table Source 都定义时间戳并声明 WATERMARK 时间戳字段。

### ROWS/BOUNDED
如果您希望处理基于窗口（Window）的数据，而数据中正好包含时间戳信息（以 SQL 规范的时间戳或 Unix 时间戳表示的列），则建议使用 Event Time 处理模式。

启用 Event Time 时间处理模式示例如下：
- 数据有一个 generation_time 字段，最大允许的乱序误差是1000毫秒，则可以声明：`WATERMARK FOR BOUNDED(generation_time, 1000)`。
- 如果希望每隔100条数据生成一次 Watermark，那么可以声明：`WATERMARK FOR ROWS(generation_time, 100)` 

若不声明 WATERMARK 已指定时间戳字段，则会使用 Processing Time 时间模式，该模式以数据被处理的时间戳来生成 Watermark 并在后续使用，顺序和精确性不能得到保证，可用于时间精确度要求不高的应用场景。



