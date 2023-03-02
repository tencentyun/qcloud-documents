## 介绍
Pulsar SQL connector 允许您使用简单的 SQL 查询或 Flink Table API 从 Pulsar topic 查询数据或将数据写入 Pulsar。

## 版本说明

| Flink 版本 | 说明 |
| -------------- | -------- |
| 1.11           | 不支持   |
| 1.13           | 支持     |
| 1.14           | 支持     |

## 使用范围
- 可以作为源表，以及 Tuple、Upsert 数据流的目的表。
- 不支持维表。

## 如何创建 Pulsar 表
以下示例展示了如何创建 Pulsar 表：
```Bash
CREATE TABLE PulsarTable (
  `user_id` bigint,
  `item_id` bigint,
  `behavior` STRING,
  `publish_time` TIMESTAMP_LTZ(3) METADATA FROM 'publish_time' VIRTUAL
) WITH (
    'connector' = 'pulsar',
    'service-url' = 'pulsar://pulsar:6650',
    'admin-url' = 'http://pulsar:8080',
    'topics' = 'user_behavior',
    'format' = 'json',
    'source.subscription-name' = 'flink',
    'source.start.message-id' = 'earliest'
);
```

## Connector 参数

| 参数值                                | 必填 | 默认值                         | 数据类型 | 描述                                                   |
| ------------------------------------------ | -------- | ----------------------------------- | ------------ | ------------------------------------------------------------ |
| connector                                  | 必选     | (none)                              | String       | 指定要使用的连接器，Apache Pulsar 连接器使用：`'pulsar'`、`'upsert-pulsar'`。 |
| admin-url                                  | 必选     | (none)                              | String       | Pulsar 管理端地址 HTTP 地址，例如 `http://my-broker.example.com:8080` 或者 `https://my-broker.example.com:8443`。 |
| service-url                                | 必选     | (none)                              | String       | Pulsar 服务端 URL<li>pulsar client 连接 puslar 集群需要 pulsar 协议的 URL。例如：`pulsar://localhost:6650`。<li>多个 broker 节点的 URL： `pulsar://localhost:6550,localhost:6651,localhost:6652`。<li>生产环境集群一般以域名方式访问，例如：`pulsar://pulsar.us-west.example.com:6650`。<li>开启 TLS 验证的 URL：`pulsar+ssl://pulsar.us-west.example.com:6651`。 |
| topics                                     | 必选     | (none)                              | String       | 用于读取和写入的 Apache Pulsar 的 topic 名称。<li>可以是单个 topic 名称，也可以是以“;”分割的 topic 列表，例如：`topic-1;topic-2`。<li>可以指定一组 topic 或者分区或者是两者都有，例如：`topic-a-partition-0;topic-a-partition-2;some-topic2`。<li>如果同时指定了某个 topic 和其下属的分区，那么将会自动将两者合并，仅使用外层的 topic，例如：`some-topic1;some-topic1-partition-0`等价于 `some-topic1`。 |
| pulsar.client.authPluginClassName          | 可选     | (none)                              | String       | 鉴权插件类名，token 鉴权填写：`org.apache.pulsar.client.impl.auth.AuthenticationToken`。 |
| pulsar.client.authParams                   | 可选     | (none)                              | String       | 鉴权参数，token 鉴权填写格式为：`token:xxxx`。               |
| explicit                                   | 可选     | true                                | Boolean      | 是否为 explicit flink 表，用于 pulsar catalog。参考 pulsar catalog 介绍。 |
| key.fields                                 | 可选     | （none）                            | List&lt;String> | Pulsar 消息中的 key 字段对应的 flink 表物理字段。注意这些字段与 primary key 没有关系。 |
| key.format                                 | 可选     | (none)                              | String       | 用于对 Pulsar 消息中 key 部分序列化和反序列化的格式。<br>支持的格式包括 `'csv'`、`'json'`、`'avro'`等。请参考 [格式](https://nightlies.apache.org/flink/flink-docs-release-1.14/zh/docs/connectors/table/formats/overview/) 页面以获取更多详细信息和格式参数。 |
| format                                     | 可选     | (none)                              | String       | 用于对 pulsar 消息中 value 部分序列化和反序列化的格式。<br>支持的格式包括 `'csv'`、`'json'`、`'avro'`。请参考 [格式](https://nightlies.apache.org/flink/flink-docs-release-1.14/zh/docs/connectors/table/formats/overview/) 页面以获取更多详细信息和格式参数。<br>选项 `format `和 `value.format` 必选其一，format 具有高优先级。 |
| value.format                               | 可选     | (none)                              | String       | 用于对 pulsar 消息中 value 部分序列化和反序列化的格式。<br>支持的格式包括 `'csv'`、`'json'`、`'avro'`。请参考 [格式](https://nightlies.apache.org/flink/flink-docs-release-1.14/zh/docs/connectors/table/formats/overview/) 页面以获取更多详细信息和格式参数。<br>选项 `format `和 `value.format` 必选其一，format 具有高优先级。 |
| sink.topic-routing-mode                    | 可选     | round-robin                         | Enum         | Topic 路由策略。可用选项为 `round-robin` 和 `message-key-hash`。默认情况下，它设置为 `round-robin`。如果要使用自定义 topic 路由策略，请使用 `sink.custom-topic-router` 选项设置。 |
| sink.custom-topic-router                   | 可选     | （none）                            | String       | 自定义 topic 路由策略完整类名，如果设置了该选项，请不要设置` sink.topic-routing-mode`。 |
| sink.message-delay-interval                | 可选     | 0                                   | Duration     | 延迟消息投递间隔，示例：`10ms、1s、1min`。延迟消息投递功能使得消息被延迟消费，参考 pulsar 文档 [Delayed message delivery](https://pulsar.apache.org/docs/concepts-messaging#delayed-message-delivery)。 |
| pulsar.sink.deliveryGuarantee              | 可选     | none                                | Enum         | Pulsar sink 的数据一致性保证，可选 `none`、`at-least-once`、`exactly-once`。`exactly-once` 需要 Pulsar 集群支持事务。 |
| pulsar.sink.transactionTimeoutMillis       | 可选     | 10800000                            | Long         | 单位毫秒，Pulsar 事务超时时间，默认为 3 小时（10800000 毫秒），注意必须保证事务超时时间大于 checkpoint 时间间隔。 |
| pulsar.producer.batchingEnabled            | 可选     | false                               | Boolean      | 是否开启分批写。                                             |
| pulsar.producer.batchingMaxMessages        | 可选     | 1000                                | Int          | Pulsar 批次写入最大消息条数。                                |
| source.start.message-id                    | 可选     | (none)                              | String       | 指定 source 消费起始位点，可选值为 `earliest`, `latest` 或消息 ID (格式 `ledgerId:entryId:partitionId`, 例如 "12:2:-1")。 |
| source.start.publish-time                  | 可选     | (none)                              | Long         | 指定 source 消费起始点的发布时间戳（unix 毫秒级时间戳）。    |
| source.subscription-name                   | 可选     | flink-sql-connector-pulsar-<RANDOM> | String       | Pulsar 消息订阅名字。默认为 `flink-sql-connector-pulsar-<RANDOM>`，其中 `RANDOM `为长度为 5 的随机字母。 |
| source.subscription-type                   | 可选     | Exclusive                           | Enum         | Pulsar 消息订阅类型，目前只支持 `Exclusive `、`Shared`，消息订阅类型的更多信息请参考 [Subscription types](https://pulsar.apache.org/docs/concepts-messaging#subscription-types)。 |
| source.stop.at-message-id                  | 可选     | (none)                              | String       | 指定 source 消费结束位点，可选值 `never`, `latest` 或消息 ID (格式 `ledgerId:entryId:partitionId`, 例如 "12:2:-1")。 |
| source.stop.at-publish-time                | 可选     | (none)                              | Long         | 指定 source 消费结束点的发布时间戳（unix 毫秒级时间戳）。    |
| source.stop.after-message-id               | 可选     | (none)                              | String       | 指定 source 消费结束位点的消息 ID（包含该消息），格式 `ledgerId:entryId:partitionId`, 例如 "12:2:-1"。 |
| pulsar.source.partitionDiscoveryIntervalMs | 可选     | 30000                               | Long         | 单位毫秒，pulsar source 自动探测新增 partition 的时间间隔。设置为 0 或者负值禁用 partition 探测。 |
| pulsar.admin.requestRetries                | 可选     | 5                                   | Int          | Pulsar admin Rest API 调用失败重试次数。                     |
| pulsar.client.*                            | 可选     | (none)                              | -            | 该选项可以传递任意的的 pulsar client 参数。                  |
| pulsar.admin.*                             | 可选     | (none)                              | -            | 该选项可以传递任意的 pulsar 管理端参数。                     |
| pulsar.sink..*                             | 可选     | (none)                              | -            | 该选项可以传递其他的 pulsar sink connector 参数。            |
| pulsar.producer.*                          | 可选     | (none)                              | -            | 该选项可以传递任意的 pulsar producer API 配置参数。          |
| pulsar.source..*                           | 可选     | (none)                              | -            | 该选项可以传递其他的 pulsar source connector 参数。          |
| pulsar.consumer.*                          | 可选     | (none)                              | -            | 该选项可以传递任意的 pulsar consumer API 配置参数。          |

## 可用元数据

| 元数据 Key | 数据类型               | R/W| 描述                           |
| ------------- | ---------------------------- | ------- | ----------------------------------- |
| topic         | STRING NOT NULL              | R       | Pulsar 消息的  Topic name 字段。    |
| message_size  | INT NOT NULL                 | R       | Pulsar 消息大小。                   |
| producer_name | STRING NOT NULL              | R       | Pulsar 消息的  Producer name 字段。 |
| message_id    | BYTES NOT NULL               | R       | Pulsar 消息的  Message ID 字段。    |
| sequenceId    | BIGINT NOT NULL              | R       | Pulsar 消息的  Sequence ID 字段。   |
| publish_time  | TIMESTAMP_LTZ(3) NOT NULL    | R       | Pulsar 消息的  Publish time 字段。  |
| event_time    | TIMESTAMP_LTZ(3) NOT NULL    | R/W     | Pulsar 消息的  Properties 字段。    |
| properties    | MAP	&lt;STRING, STRING> NOT NULL | R/W     | Pulsar 消息的  Event time 字段。    |

>?
> - `R/W` 列定义了一个元数据是可读的（`R`）还是可写的（`W`）。 只读列必须声明为 `VIRTUAL` 以在 `INSERT INTO` 操作中排除它们。
> - Pulsar 消息的字段列表参考 pulsar 官网文档 [Messages](https://pulsar.apache.org/docs/concepts-messaging#messages)。

## 数据类型映射

| Pulsar schema | Flink forma  |
| ----------------- | ----------------- |
| AVRO              | avro              |
| JSON              | json              |
| PROTOBUF          | Not supported yet |
| PROTOBUF_NATIVE   | Not supported yet |
| AUTO_CONSUME      | Not supported yet |
| AUTO_PUBLISH      | Not supported yet |
| NONE/BYTES        | raw               |
| BOOLEAN           | raw               |
| STRING            | raw               |
| DOUBLE            | raw               |
| FLOAT             | raw               |
| INT8              | raw               |
| INT16             | raw               |
| INT32             | raw               |
| INT64             | raw               |
| LOCAL_DATE        | Not supported yet |
| LOCAL_TIME        | Not supported yet |
| LOCAL_DATE_TIME   | Not supported yet |

### PulsarCatalog
PulsarCatalog 支持将 Pulsar 集群配置为 Flink 表的元数据存储。

### Explicit 表和 native 表

PulsarCatalog 定义了两种类型的表: `explicit` 表 and `native` tables。
- `explicit` 表是使用 CREATE 语句或 table API 显式创建的表，它类似于其他 SQL connector 中的常用模式。您可以创建表，然后从表中查询数据或向表中写入数据。
- `native` 表由 PulsarCatalog 自动创建。PulsarCatalog 扫描 Pulsar 集群中的所有非系统主题，然后将每个 topic 映射成 Flink 表，而不使用 CREATE 语句。

#### Explicit 表
PulsarCatalog 使用 topic schema 的 `schemaInfo` 字段存储 `explicit` 表的元数据信息。对于每个 `explicit` 表，PulsarCatalog 在默认为`__flink_catalog` 的 tenant 下创建一个占位 topic。可通过 `catalog-tenant` 选项设置 tenant。Flink 的 database 映射为该 tenant 下同样名字的 namespace。然后创建一个名为 `table_<FLINK_TABLE_NAME>` 的 topic，该 topic 的 schema 存储了 Flink 表的 schema 元数据信息。

例如，如果您创建了database 为 `testdb`，表为 `users` 的 flink 表，那么 PulsarCatalog 创建 tenant 为  `__flink_catalog` ，namespace 为 `testdb` 的 topic `table_users`。

Topic `table_users` 只所以称之为占位 topic 是因为它没有任何 producer 或者 consumer，您可以使用占位 topic 的 schema 来存储 Flink 表的元数据信息。

您可以使用 `pulsar-admin` 命令行工具来获取 topic 的元数据信息：
```Bash
pulsar-admin schemas get persistent://<tenant>/<namespace>/<topic>
```

#### Native 表
`native` 表没有任何占位 topic，PulsarCatalog 把 topic 的 schema 映射为 Flink 表的 schema。关于 Pulsar schema，参考 Pulsar 官网文档 [Understand schema](https://pulsar.apache.org/docs/schema-understand)。

| Pulsar schema | Flink data type                      | Flink format  | Work or not |
| ----------------- | ----------------------------------------- | ----------------- | --------------- |
| AVRO              | It is decided by the Avro format.         | avro              | Yes             |
| JSON              | It is decided by the JSON format.         | json              | Yes             |
| PROTOBUF          | Not supported yet                         | /                 | No              |
| PROTOBUF_NATIVE   | It is decided by the Protobuf definition. | Not supported yet | No              |
| AUTO_CONSUME      | Not supported yet                         | /                 | No              |
| AUTO_PUBLISH      | Not supported yet                         | /                 | No              |
| NONE/BYTES        | DataTypes.BYTES()                         | raw               | Yes             |
| BOOLEAN           | DataTypes.BOOLEAN()                       | raw               | Yes             |
| LOCAL_DATE        | DataTypes.DATE()                          | /                 | No              |
| LOCAL_TIME        | DataTypes.TIME()                          | /                 | No              |
| LOCAL_DATE_TIME   | DataTypes.TIMESTAMP(3)                    | /                 | No              |
| STRING            | DataTypes.STRING()                        | raw               | Yes             |
| DOUBLE            | DataTypes.DOUBLE()                        | raw               | Yes             |
| FLOAT             | DataTypes.FLOAT()                         | raw               | Yes             |
| INT8              | DataTypes.TINYINT()                       | raw               | Yes             |
| INT16             | DataTypes.SMALLINT()                      | raw               | Yes             |
| INT32             | DataTypes.INT()                           | raw               | Yes             |
| INT64             | DataTypes.BIGINT()                        | raw               | Yes             |

>? 尽管对于 Pulsar schema 的 `LOCAL_DATE`, `LOCAL_TIME` 和 `LOCAL_DATE_TIME` 有相应的 flink 数据类型，但 flink 基于这几种 Pulsar schema 无法解析数据，因此自动 schema 映射会失败。

#### Explicit 和 native 表对比
使用 `native` 表，您可以从现有 Pulsar topic 中查询数据。PulsarCatalog 自动读取 topic 的 schema，并决定使用哪种 format 来解码/编码。但是，`native `表不支持 `watermark` 和主键，因此，不能使用 `native `表进行基于事件时间的窗口聚合。`native `表将 `tenant/namespace` 映射到 flink 的 database，topic 名字映射为 flink 表名。

要完全管理表，可以使用 `explicit` 表定义 `watermark`、指定元数据字段和指定自定义格式。其用法类似于在 `GenericInMemoryCatalog` 中创建 Pulsar 表。您可以将 `explicit` 表绑定到 Pulsar 的 topic，每个 Pulsar topic 可以绑定到多个 Flink 表（包括 `native` 表）。

### PulsarCatalog 参数

| Key                 | Default                                        | Type | Description                                              | Required |
| ----------------------- | -------------------------------------------------- | -------- | ------------------------------------------------------------ | ------------ |
| **catalog-admin-url**   | "http://localhost:8080"                            | String   | Pulsar 管理端地址 HTTP 地址，例如 `http://my-broker.example.com:8080` 或者 `https://my-broker.example.com:8443`。 | Yes          |
| **catalog-auth-params** | (none)                                             | String   | 访问 Pulsar 集群的认证参数。                                 |              |
| **catalog-auth-plugin** | (none)                                             | String   | 访问 Pulsar 集群的认证 plugin 名字。                         |              |
| **catalog-service-url** | "pulsar://[localhost:6650](http://localhost:6650)" | String   | Pulsar 服务端 URL<li>pulsar client 连接 puslar 集群需要 pulsar 协议的 URL。例如：`pulsar://localhost:6650`。<li>多个 broker 节点的 URL： `pulsar://localhost:6550,localhost:6651,localhost:6652`。<li>生产环境集群一般以域名方式访问，例如：`pulsar://pulsar.us-west.example.com:6650`。<li>开启 TLS 验证的 URL：`pulsar+ssl://pulsar.us-west.example.com:6651`。 | Yes          |
| **catalog-tenant**      | "__flink_catalog"                                  | String   | 存储表信息的 Pulsar tenant。                                 |              |
| **default-database**    | "default_database"                                 | String   | PulsarCatalog 的默认 database，不存在时会自动创建。          |              |

###  PulsarCatalog 示例
```SQL
CREATE CATALOG pulsar WITH (
    'type' = 'pulsar-catalog',
    'catalog-admin-url' = '<ADMIN_URL>',
    'catalog-service-url' = '<SERVICE_URL>'
);
```

## 完整示例
### Pulsar source 和 sink 示例
如下示例展示了 Pulsar 数据源写入 Pulsar 数据目的，`exactly-once` 的数据一致性保证，事务超时时间 2 分钟（注意必须保证事务超时时间大于 checkpoint 时间间隔）。
```SQL
CREATE TABLE `pulsar_source` (
  `user_id` bigint,
  `item_id` bigint,
  `behavior` STRING
) WITH (
  'connector' = 'pulsar',
  'service-url' = 'pulsar://pulsar:6650',
  'admin-url' = 'http://pulsar:8080',
  'topics' = 'topic_source',
  'format' = 'json',
  'source.subscription-name' = 'flink',
  'source.start.message-id' = 'earliest'
);

CREATE TABLE `pulsar_sink` (
  `user_id` bigint,
  `item_id` bigint,
  `behavior` STRING
) WITH (
  'connector' = 'pulsar',
  'service-url' = 'pulsar://pulsar:6650',
  'admin-url' = 'http://pulsar:8080',
  'topics' = 'topic_sink',
  'format' = 'json',
  'pulsar.sink.deliveryGuarantee' = 'exactly-once',
  'pulsar.sink.transactionTimeoutMillis' = '120000'
);

INSERT INTO `pulsar_sink` SELECT * FROM `pulsar_source`;
```

### PulsarCatalog 示例
#### Explicit 表示例
```SQL
CREATE CATALOG `pulsar` WITH (
  'type' = 'pulsar-catalog',
  'catalog-admin-url' = 'http://pulsar:8080',
  'catalog-service-url' = 'pulsar://pulsar:6650'
);
INSERT INTO `pulsar`.`default_database`.`pulsar_sink` SELECT * FROM `pulsar`.`default_database`.`pulsar_source`;
```
其中的 `pulsar_source` 和 `pulsar_sink` 表用下面语句创建（可以放到同一个 SQL 作业里）。
```SQL
CREATE TABLE IF NOT EXISTS `pulsar`.`default_database`.`pulsar_source` (
  `user_id` bigint,
  `item_id` bigint,
  `behavior` STRING
) WITH (
  'connector' = 'pulsar',
  'service-url' = 'pulsar://pulsar:6650',
  'admin-url' = 'http://pulsar:8080',
  'topics' = 'topic_source',
  'format' = 'json',
  'source.subscription-name' = 'flink',
  'source.start.message-id' = 'earliest'
);

CREATE TABLE IF NOT EXISTS `pulsar`.`default_database`.`pulsar_sink` (
  `user_id` bigint,
  `item_id` bigint,
  `behavior` STRING
) WITH (
  'connector' = 'pulsar',
  'service-url' = 'pulsar://pulsar:6650',
  'admin-url' = 'http://pulsar:8080',
  'topics' = 'topic_sink',
  'format' = 'json',
  'pulsar.sink.deliveryGuarantee' = 'exactly-once',
  'pulsar.sink.transactionTimeoutMillis' = '120000'
);
```

#### Native 表示例
1. 准备 topic schema 的 json 格式文件，命名为 schema.json
```SQL
{
  "schema": "{\"type\":\"record\",\"name\":\"userBehavior\",\"namespace\":\"my.example\",\"fields\":[{\"name\":\"user_id\",\"type\":\"long\"},{\"name\":\"item_id\",\"type\":\"long\"},{\"name\":\"behavior\",\"type\":\"string\"}]}",
  "type": "JSON",
  "properties": {}
}
```

2. Pulsar admin 命令行工具设置 topic 的 schema。
```Bash
# 设置 schema
bin/pulsar-admin schemas upload -f ./schema.json topic_source
bin/pulsar-admin schemas upload -f ./schema.json topic_sink

# 检查 schema
bin/pulsar-admin schemas get topic_source
bin/pulsar-admin schemas get topic_sink
```

3. 作业示例。其中 flink 表的 database `public/default`格式为 `tenant/namespace`，为 Pulsar 集群的默认值。
```SQL
CREATE CATALOG `pulsar` WITH (
  'type' = 'pulsar-catalog',
  'catalog-admin-url' = 'http://pulsar:8080',
  'catalog-service-url' = 'pulsar://pulsar:6650'
);

INSERT INTO `pulsar`.`public/default`.`topic_sink` SELECT * FROM `pulsar`.`public/default`.`topic_source`;
```

## 常见问题
### 事务未开启异常
```Bash
java.lang.NullPointerException: You haven't enable transaction in Pulsar client.
```
参考 [How to use transactions?](https://pulsar.apache.org/docs/txn-use) 开启集群事务功能。

### Pulsar sink exactly-once 默认写入消息，作业异常重启后，topic 数据无法消费
**现象原因**：这是由于作业异常重启前的事务可能未提交，当 topic 存在 OPEN 状态的事务时，阻塞了该 topic 后续写入的数据的读取。可用命令 <code>pulsar-admin transactions slow-transactions -t 1s</code>查看 OPEN 状态的事务。当 OPEN 状态的事务提交或者回滚后，topic 后续写入的数据即可读取。
**规避建议**：使用 with 参数设置合适的事务超时时间（pulsar 默认为 3 小时），例如 <code>'pulsar.sink.transactionTimeoutMillis' = '120000'</code>设置事务超时时间为 2 分钟。注意必须保证事务超时时间大于 checkpoint 时间间隔。

### Pulsar source 在批量消息场景快照恢复失败
如果您遇到错误<code>java.lang.IllegalArgumentException: We only support normal message id currently</code>，这是因为 Pulsar 写入端开启了批次写，当前 Pulsar source 不支持批量写消息的状态恢复。Oceanus Pulsar sink 默认不开启批量写。
```Bash
Caused by: java.lang.IllegalArgumentException: We only support normal message id currently.
```

### Pulsar source 消费起始位点与 subscription 的关系
- 如果 topic 不存在 subscription，则按起始位点对应的消息 ID 创建 subscription（参考 PulsarSourceEnumerator#createSubscription）。 
- 如果 topic 存在 subscription，则起始位点不起作用。
- 若不是从快照恢复，则从 subscription 的 cursor 开始消费。如果是从快照恢复，则从快照记录的消息 ID 的下一条消息开始消费（通过重置 subscription 的 cursor 的方式，参考 PulsarOrderedPartitionSplitReader#beforeCreatingConsumer）

### Pulsar source 无法使用 <code>NonDurable</code> 订阅模式
- PulsarSourceEnumerator#createSubscription 会先创建了 <code>Durable</code> 的 subscription。
- PulsarPartitionSplitReaderBase#createPulsarConsumer 再以 <code>NonDurable</code> 模式消费数据，报错 <code>Durable subscription with the same name already exists</code>。

|参数值  |      必填    |    默认值    |    数据类型       | 描述|
| -------------------------------- | ---- | ------- | ---- | ------------------------------------------------------------ |
| pulsar.consumer.subscriptionMode | 可选 | Durable | Enum | Pulsar 消息订阅模式，可选 <code>Durable</code>、 <code>NonDurable</code>。 <code>Durable</code> 模式下，cursor 是持久的，它保留消息并持久化当前位置。如果 broker 从故障中重新启动，它可以从持久存储（bookie）中恢复 cursor，以便消息可以从上次消费的位置继续消费。<code>NonDurable</code> 模式下，一旦 broker 停止，cursor 将丢失且无法恢复，因此无法从上次消费的位置继续消费。更多信息参考 [Subscription modes](https://pulsar.apache.org/docs/concepts-messaging#subscription-modes)。 |


### MessageId 注意事项
参考 [消息存储原理与 ID 规则](https://cloud.tencent.com/document/product/1179/58527)，消息 ID 可比较大小，例如 <code>174:1:0 > 174:1:-1</code>。

### Pulsar source 根据消息 publish-time 消费数据失败
**原因**：如果连接的 broker 没有提供 topic 的 namespace 信息，那么根据 publish-time 获取消息 ID 的 Rest API 接口会返回 <code>HTTP 307 Temporary Redirect</code>，flink connector 中使用的 pulsar-client api 则会返回 <code>HTTP 500 Server Error</code> 错误，导致作业无法启动。可用 [get-message-by-id](https://pulsar.apache.org/docs/admin-api-topics#get-message-by-id) 的 Rest API 接口查看错误情况。

```Bash
## 1662480195714 为毫秒级的消息 publish-time
curl http://${adminUrl}:8080/admin/v2/persistent/public/default/${topic}/messageid/1662480195714
```

>? <code>source.stop.at-publish-time</code> 可以使用，因为不涉及到到根据 publish-time 查找消息 ID 的 Rest API 调用。

**建议**：可通过适当调大 Rest API 调用失败的重试次数（选项 <code>pulsar.admin.requestRetries</code>，默认 5）来规避该问题。 

### Pulsar source 设置了结束位点作业在消费完数据后没有停止
**解决方案**：请关闭 partition 自动探测功能，设置选项 <code>'pulsar.source.partitionDiscoveryIntervalMs' ='0'</code>
