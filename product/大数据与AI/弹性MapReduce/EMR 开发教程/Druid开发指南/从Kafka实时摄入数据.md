本文介绍如何使用 Apache Druid Kafka Indexing Service 实时消费 Kafka 数据。开始本节前，类似 Hadoop 集群，需要确保 Kafka 集群和 Druid 集群之间能够正常通信。

>?
>- 两个集群在同一个 VPC 下，或两个集群在不同 VPC，但两个 VPC 之间能够正常通信（如通过云联网或者对等连接）。
>- 如有必要需要将 Kafka 集群的 Host 信息配置到 Druid 集群中。

## 命令行方式
1. 首先在 Kafka 集群启动 kafka broker。
```
./bin/kafka-server-start.sh config/server.properties
```
1. 创建一个kafka topic，名为 mytopic。
```
./bin/kafka-topics.sh --create --zookeeper {kafka_zk_ip}:2181 --replication-factor 1 --partitions 1 --topic mytopic
输出：
Created topic "mytopic".
```
`{kafka_zk_ip}:2181`为 kafka 集群的 zookeeper 地址。
1. 在 Druid 集群上准备一个数据描述文件 kafka-mytopic.json。
```
{
     "type": "kafka",
     "dataSchema": {
         "dataSource": "mytopic-kafka",
         "parser": {
             "type": "string",
             "parseSpec": {
                 "timestampSpec": {
                     "column": "time",
                     "format": "auto"
                 },
                 "dimensionsSpec": {
                     "dimensions": ["url", "user"]
                 },
                 "format": "json"
             }
         },
         "granularitySpec": {
             "type": "uniform",
             "segmentGranularity": "hour",
             "queryGranularity": "none"
         },
         "metricsSpec": [{
                 "type": "count",
                 "name": "views"
             },
             {
                 "name": "latencyMs",
                 "type": "doubleSum",
                 "fieldName": "latencyMs"
             }
         ]
     },
     "ioConfig": {
         "topic": "mytopic",
         "consumerProperties": {
             "bootstrap.servers": "{kafka_ip}:9092",
             "group.id": "kafka-indexing-service"
         },
         "taskCount": 1,
         "replicas": 1,
         "taskDuration": "PT1H"
     },
     "tuningConfig": {
         "type": "kafka",
         "maxRowsInMemory": "100000"
     }
 }
```
`{kafka_ip}:9092`为您 Kafka 集群的 bootstrap.servers IP 和端口。
1. 在 Druid 集群的 Master 节点上添加 Kafka supervisor。
```
curl -XPOST -H 'Content-Type: application/json' -d @kafka-mytopic.json http://{druid_master_ip}:8090/druid/indexer/v1/supervisor
输出：
{"id":"mytopic-kafka"}
```
`{druid_master_ip}:8090`为 overlord 进程部署的节点，一般是 Master 节点。
1. 在 Kafka 集群上开启一个  console producer。
```
./bin/kafka-console-producer.sh --broker-list {kafka_ip}:9092 --topic mytopic
```
`{kafka_ip}:9092`为您 Kafka 集群的 bootstrap.servers IP 和端口。
1. 在 druid 集群准备一个查询文件，命名为 query-mytopic.json。
```
{
     "queryType" : "search",
     "dataSource" : "mytopic-kafka",
     "intervals" : ["2020-03-13T00:00:00.000/2020-03-20T00:00:00.000"],
     "granularity" : "all",
     "searchDimensions": [
         "url",
         "user"
     ],
     "query": {
         "type": "insensitive_contains",
         "value": "roni"
     }
 }
```
1. 在 kafka 上实时输入一些数据。
```
{"time": "2020-03-19T09:57:58Z", "url": "/foo/bar", "user": "brozo", "latencyMs": 62}
{"time": "2020-03-19T16:57:59Z", "url": "/", "user": "roni", "latencyMs": 15}
{"time": "2020-03-19T17:50:00Z", "url": "/foo/bar", "user": "roni", "latencyMs": 25}
```
时间戳生成命令：
```
python -c 'import datetime; print(datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"))'
```
1. 在 Druid 集群上查询。
```
curl -XPOST -H 'Content-Type: application/json' -d @query-mytopic.json http://{druid_ip}:8082/druid/v2/?pretty
```
`{druid_ip}:8082`为您 Druid 集群的 broker 节点，一般在 Master 或 Router 节点上。
**查询结果：**
```
[ {
  "timestamp" : "2020-03-19T16:00:00.000Z",
  "result" : [ {
    "dimension" : "user",
    "value" : "roni",
    "count" : 2
  } ]
} ]
```

## Web 可视化方式

您可通过 Druid Web UI 控制台可视化方式，从 Kafka 集群摄入数据并查询，详细步骤请参考 [通过 data loader 加载 Kafka 数据](https://druid.apache.org/docs/latest/tutorials/tutorial-kafka.html#loading-data-with-the-data-loader)。
