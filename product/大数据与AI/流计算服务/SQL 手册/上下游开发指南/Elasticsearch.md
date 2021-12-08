## 介绍

Elasticsearch Connector 提供了对 Elasticsearch  写入支持。目前 Oceanus 支持 Elasticsearch 6.x 和 7.x 版本提供支持。

## 版本说明

| Flink 版本 | 说明 |
| :-------- | :--- |
| 1.11      | 支持 |
| 1.13      | 支持 |


## 使用范围
Elasticsearch 只支持写入，可以作为 Tuple 数据流的目的表（Sink），也可以作为 Upsert 数据流的目的表（Sink，自动以文档 `_id` 字段生成主键，并更新之前的文档版本）。

如果希望将 JDBC 数据库的变动记录，将其作为流式源表消费，可以使用 [Debezium](https://debezium.io/documentation/reference/1.2/tutorial.html)、[Canal](https://github.com/alibaba/canal) 等，对 JDBC 据库的变更进行捕获和订阅，然后 Flink 即可对这些变更事件进行进一步的处理。可参见 [Kafka](https://cloud.tencent.com/document/product/849/48310)。

## DDL 定义
### 用作 Elasticsearch 6 数据目的（Sink）
```sql
CREATE TABLE elasticsearch6_sink_table (
    `id` INT,
    `name` STRING
) WITH (
    'connector' = 'elasticsearch-6',       -- 输出到 Elasticsearch 6
    'username' = '$username',              -- 选填 用户名
    'password' = '$password',              -- 选填 密码
    'hosts' = 'http://10.28.28.94:9200',   -- Elasticsearch 的连接地址
    'index' = 'my-index',                  -- Elasticsearch 的 Index 名
    'document-type' = '_doc',              -- Elasticsearch 的 Document 类型
    'sink.bulk-flush.max-actions' = '1',   -- 每条数据都刷新
    'format' = 'json'                      -- 输出数据格式，目前只支持 'json'
);
```
### 用作 Elasticsearch 7 数据目的（Sink）
```sql
CREATE TABLE elasticsearch7_sink_table (
    `id` INT,
    `name` STRING
) WITH (
    'connector' = 'elasticsearch-7',       -- 输出到 Elasticsearch 7
    'username' = '$username',              -- 选填 用户名
    'password' = '$password',              -- 选填 密码
    'hosts' = 'http://10.28.28.94:9200',   -- Elasticsearch 的连接地址
    'index' = 'my-index',                  -- Elasticsearch 的 Index 名
    'sink.bulk-flush.max-actions' = '1',   -- 每条数据都刷新
    'format' = 'json'                      -- 输出数据格式，目前只支持 'json'
);
```

## 通用 WITH 参数

| 参数值                              |                必填                |  默认值  | 描述                                                         |
| :---------------------------------- | :--------------------------------: | :------: | :----------------------------------------------------------- |
| connector                           |                 是                 |    无    | 当写入 Elasticsearch 6.x 版本时，取值`elasticsearch-6`。当写入 Elasticsearch 7.x 及以上版本时，取值`elasticsearch-7`。 |
| username                            |                 否                 |    无    | 用户名。                                                     |
| password                            |                 否                 |    无    | 密码。                                                       |
| hosts                               |                 是                 |    无    | Elasticsearch 的连接地址。                                   |
| index                               |                 是                 |    无    | 数据要写入的 Index。支持固定 Index（例如 `'myIndex'`），也支持动态 Index（例如`'index-{log_ts\|yyyy-MM-dd}'`）。 |
| document-type                       | 6.x 版本：必填<br/>7.x 版本：不需要 |    无    | Elasticsearch 文档的 Type 信息。当选择 `elasticsearch-7` 时，不能填写这个字段，否则会报错。 |
| document-id.key-delimiter           |                 否                 |    _     | 为复合键生成 \_id 时的分隔符 (默认是 "\_")。例如有 a、b、c 三个主键，某条数据的 a 字段为 "1"，b 字段为 "2"，c 字段为 "3"，使用默认分隔符，则最终写入 Elasticsearch 的 \_id 是 "1\_2\_3"。 |
| failure-handler                     |                 否                 |   fail   | 指定请求 Elasticsearch 失败时，错误处理策略。选项为：<li/>`fail`：抛出一个异常。<li/>`ignore`：忽略错误，直接继续。<li/>`retry-rejected`：重试写入该条记录。<br/>另外也支持自定义错误处理器，这里可以填写用户自己编写的 Handler 的类全名（需要上传自定义程序包）。 |
| sink.flush-on-checkpoint            |                 否                 |   true   | Flink 进行快照时，是否等待现有记录完全写入 Elasticsearch 。如果设置为 false，则可能造成恢复时部分数据丢失或者重复等异常情况，但快照速度会提升。 |
| sink.bulk-flush.max-actions         |                 否                 |   1000   | 批量写入的最大条数。设置为 `0` 则禁用批量功能。              |
| sink.bulk-flush.max-size            |                 否                 |   2mb    | 批量写入缓存的最大容量，必须以 `mb` 为单位。设置为 `0` 则禁用批量功能。 |
| sink.bulk-flush.interval            |                 否                 |    1s    | 批量写入的刷新周期。设置为`0`则禁用批量功能。                |
| sink.bulk-flush.backoff.strategy    |                 否                 | DISABLED | 批量写入时，失败重试的策略。<li/>`DISABLED`：不重试。<li/>`CONSTANT`：等待 `sink.bulk-flush.backoff.delay` 选项设置的毫秒后重试。<li/>`EXPONENTIAL`：一开始等待 `sink.bulk-flush.backoff.delay` 选项设置的毫秒后重试，每次失败后将指数增加下次的等待时间。 |
| sink.bulk-flush.backoff.max-retries |                 否                 |    8     | 批量写入时，最多失败重试的次数。                             |
| sink.bulk-flush.backoff.delay       |                 否                 |   50ms   | 批量写入失败时，每次重试之间的等待间隔（对于 CONSTANT 策略而言）或间隔的初始基数（对于 EXPONENTIAL 策略而言）。 |
| connection.max-retry-timeout        |                 否                 |    无    | 重试请求的最大超时时间。                                     |
| connection.path-prefix              |                 否                 |    无    | 指定每个 REST 请求的前缀，例如 `'/v1'`。通常不需要设置该选项。 |
| format                              |                 否                 |   json   | 指定输出的格式，默认是内置的 `json` 格式，可以使用 前文（Kafka）描述过的 JSON 格式选项，例如 `json.fail-on-missing-field`、`json.ignore-parse-errors`、`json.timestamp-format.standard` 等。 |

## 代码示例

```sql
CREATE TABLE datagen_source_table (
	id INT, 
	name STRING 
) WITH ( 
	'connector' = 'datagen',
    'rows-per-second'='1'  -- 每秒产生的数据条数
);

CREATE TABLE elasticsearch7_sink_table (
    `id` INT,
    `name` STRING
) WITH (
    'connector' = 'elasticsearch-7',       -- 输出到 Elasticsearch 7
    'username' = '$username',              -- 选填 用户名
    'password' = '$password',              -- 选填 密码
    'hosts' = 'http://10.28.28.94:9200',   -- Elasticsearch 的连接地址
    'index' = 'my-index',                  -- Elasticsearch 的 Index 名
    'sink.bulk-flush.max-actions' = '1',   -- 每条数据都刷新
    'format' = 'json'                      -- 输出数据格式，目前只支持 'json'
);

INSERT INTO elasticsearch7_sink_table select * from datagen_source_table;
```

## 注意事项

如果您希望连接其他版本的 Elasticsearch，请通过附加**自定义程序包**的方式，上传相应的 Elasticsearch Sink 的 JAR 包。
