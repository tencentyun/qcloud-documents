本文介绍如何从 [Kafka](https://cloud.tencent.com/product/ckafka) 中实时消费数据到云数据仓库 ClickHouse。

## 前提条件
数据源 Kafka 集群和目的端云数据仓库 ClickHouse 集群必须在同一个 VPC 下。

## 操作步骤
1. [登录](https://cloud.tencent.com/document/product/1299/49824) 云数据仓库 ClickHouse 集群，创建 Kafka 消费表。
```
	CREATE TABLE queue (
			timestamp UInt64,
			level String,
			message String
	) ENGINE = Kafka
	SETTINGS
					kafka_broker_list = 'localhost:9092',
					kafka_topic_list = 'topic',
					kafka_group_name = 'group',
					kafka_format = 'JSONEachRow',
					kafka_num_consumers = 1,
					kafka_max_block_size = 65536,
					kafka_skip_broken_messages = 0,
					kafka_auto_offset_reset = 'latest';
```

**常用参数说明如下：**

<table>
<thread>
<tr>
<th >名称</th>
<th >是否必选</th>
<th >说明</th>
</tr>
</thread>
<tbody>
<tr>
<td >kafka_broker_list</td>
<td >是</td>
<td >Kafka 服务的 broker 列表，用逗号分隔，这里建议用 Ip:port， 不要用域名（可能存在 DNS 解析问题）。</td>
</tr>
<tr>
<td >kafka_topic_list</td>
<td >是</td>
<td >Kafka topic，多个 topic 用逗号分隔。</td>
</tr><tr>
<td >kafka_group_name</td>
<td >是</td>
<td >Kafka 的消费组名称。</td>
</tr><tr>
<td >kafka_format</td>
<td >是</td>
<td >Kafka 数据格式, ClickHouse 支持的 Format, 详见 <a href="https://clickhouse.com/docs/en/interfaces/formats/">文档</a> 可选参数。</td>
</tr><tr>
<td >kafka_row_delimiter</td>
<td >否</td>
<td >行分隔符，用于分割不同的数据行。默认为“\n”，您也可以根据数据写入的实际分割格式进行设置。</td>
</tr>
<tr>
<td >kafka_num_consumers</td>
<td >否</td>
<td >单个 Kafka Engine 的消费者数量，通过增加该参数，可以提高消费数据吞吐，但总数不应超过对应 topic 的 partitions 总数。</td>
</tr>
<tr>
<td >kafka_max_block_size</td>
<td >否</td>
<td >Kafka 数据写入目标表的 Block 大小，超过该数值后，就将数据刷盘；单位：Byte，默认值为65536 Byte。</td>
</tr>
<tr>
<td >kafka_skip_broken_messages</td>
<td >否</td>
<td >表示忽略解析异常的 Kafka 数据的条数。如果出现了 N 条异常后，后台线程结束 默认值为0。</td>
</tr><tr>
<td >kafka_commit_every_batch</td>
<td >否</td>
<td >执行 Kafka commit 的频率，取值如下：<br>0：完全写入一整个Block数据块的数据后才执行commit；<br>1：每写完一个Batch批次的数据就执行一次commit。</td>
</tr><tr>
<td >kafka_auto_offset_reset</td>
<td >否</td>
<td >从哪个 offset 开始读取 Kafka 数据。取值范围：earlist，latest。</td>
</tr>
</tbody>
</table>

2. 创建 ClickHouse 本地表（目标表）。
 
 - 如果您的集群是单副本版：
```
CREATE TABLE daily on cluster default_cluster
(
    day Date,
    level String,
    total UInt64
)
engine = SummingMergeTree()
order by int_id;
```
 - 如果您的集群是双副本版：
```
create table daily on cluster default_cluster
(
    day Date,
    level String,
    total UInt64
)
engine = ReplicatedSummingMergeTree('/clickhouse/tables/test/test/{shard}', '{replica}')
order by int_id;`
```
 - 创建分布式表：
```
create table daily_dis on cluster default_cluster
AS test.test
engine = Distributed('default_cluster', 'default', 'daily', rand());
```

3. 创建物化视图，把 Kafka 消费表消费到的数据同步到 ClickHouse 目的表。
```
CREATE MATERIALIZED VIEW consumer TO daily
AS SELECT toDate(toDateTime(timestamp)) AS day, level, count() as total
FROM queue GROUP BY day, level;
```

4. 查询。
```
SELECT level, sum(total) FROM daily GROUP BY level;
```

## 其他
如果要停止接收主题数据或更改转换逻辑，可以进行 detach 和 attach 视图操作。
```
  DETACH TABLE consumer;
  ATTACH TABLE consumer;
```
