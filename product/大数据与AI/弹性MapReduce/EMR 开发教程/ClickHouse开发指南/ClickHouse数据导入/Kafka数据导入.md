## 概述
本文介绍如何将 Kafka 中的数据导入到 ClickHouse 集群的方案。
>?想获取更多关于 ClickHouse 技术交流，可 [提交工单](https://console.cloud.tencent.com/workorder/category)，我们将您拉入 ClickHouse 技术交流群。

Kafka 是目前应用非常广泛的开源消息中间件，常用场景就是做数据总线收集各个服务的数据，下游各种数据服务订阅消费数据，生成各种报表或数据应用等。Clickhouse 自带了 Kafka Engine，使得 Clickhouse 和 Kafka 的集成变得非常容易。
 
将 Kafka 中数据导入到 ClickHouse 的标准流程是：
- 在 ClickHouse 中建立 Kafka Engine 外表，作为 Kafka 数据源的一个接口。
- 在 ClickHouse 中创建普通表（通常是 MergeTree 系列）存储 Kafka 中的数据。
- 在 ClickHouse 中创建 Materialized View，监听 Kafka 中的数据，并将数据写入到 ClickHouse 存储表中。

完成上述三个步骤，就可以将 Kafka 中的数据导入到 ClickHouse 集群中。

## Kafka 数据导入到 ClickHouse
ClickHouse 提供了 Kafka Engine 作为访问 Kafka 集群的一个接口（数据流），具体步骤如下：

- **步骤1：**创建 Kafka Engine
```
CREATE TABLE source
(
    `ts` DateTime, 
    `tag` String, 
    `message` String
)
ENGINE = Kafka()
SETTINGS kafka_broker_list = '172.19.0.47:9092', 
         kafka_topic_list = 'tag',
         kafka_group_name = 'clickhouse', 
         kafka_format = 'JSONEachRow',
         kafka_skip_broken_messages = 1,
         kafka_num_consumers = 2
```
必选参数：
 - `kafka_broker_list`：这里填写 Kafka 服务的 broker 列表，用逗号分隔。
 - `kafka_topic_list`：这里填写 Kafka topic，多个 topic 用逗号分隔。
 - `kafka_group_name`：这里填写消费者 group 名称。
 - `kafka_format`：Kafka 数据格式，ClickHouse 支持的 Format 详见 [Formats for Input and Output Data](https://clickhouse.tech/docs/en/interfaces/formats/)。

 可选参数：
 - `kafka_skip_broken_messages`：填写大于等于0的整数，表示忽略解析异常的 Kafka 数据的条数。如果出现了 N 条异常后，后台线程结束，Materialized View 会被重新安排后台线程去监听数据。
 - `kafka_num_consumers`：单个 Kafka Engine 的消费者数量，通过增加该参数，可以提高消费数据吞吐，但总数不应超过对应 topic 的 partitions 总数。
 - `kafka_row_delimiter`：消息分隔符。
 - `kafka_schema`：对于 kafka_format 需要 schema 定义时，其 schema 由该参数确定。
 - `kafka_max_block_size`：该参数控制 Kafka 数据写入目标表的 Block 大小，超过该数值后，就将数据刷盘。
- **步骤2：**创建存储 Kafka 数据的目标表，该表就是最终存储 Kafka 数据
本文采用 MergeTree 来存储 Kafka 数据：
```
CREATE TABLE target
(
    `ts` DateTime, 
    `tag` String
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(ts)
ORDER BY tag
```
- **步骤3：**创建 Metrialized View 抓取数据
本文采用如下语句创建 MV：
```
CREATE MATERIALIZED VIEW source_mv TO target AS
SELECT 
    ts, 
    tag
FROM source
```
完成上述三个步骤，即可在表 target 中查询到来自 Kafka 的数据。

在上述数据导入流程中，Materialized View 起到了一个中间管道作用，将 Kafka Engine 代表的数据流，写入到目标表中。实际上，一个数据流可以关联多个 Materialized View，将 Kafka 中的数据同时导入到多个不同目的的表中。也可以通过 DETACH/ATTACH 来取消关联，或者重新关联到某个目标表。
