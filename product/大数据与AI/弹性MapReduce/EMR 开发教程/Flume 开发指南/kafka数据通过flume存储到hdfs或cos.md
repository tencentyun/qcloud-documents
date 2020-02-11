## 场景说明
将 Kafka 中的数据通过 Flume 收集并存储到 HDFS 或 COS。

## 开发准备
- 因为任务中需要访问腾讯云消息队列 CKafka，所以需要先创建一个 CKafka 实例，具体见 [消息队列 CKafka](https://cloud.tencent.com/document/product/597)。
- 确认您已开通腾讯云，且已创建一个 EMR 集群。创建 EMR 集群时需要在软件配置界面选择 Spark 组件。

## 在 EMR 集群使用 Kafka 工具包
首先需要查看 CKafka 的内网 IP 与端口号。登录消息队列 CKafka 的控制台，选择您要使用的 CKafka 实例，在基本消息中查看其内网 IP 为 $kafkaIP，而端口号一般默认为9092。在 topic 管理界面新建一个 topic 为 kafka_test。

## 配置 flume
1.	创建 flume 的配置文件`kafka.properties`
```
vim kafka.properties
agent.sources = kafka_source
agent.channels = mem_channel
agent.sinks = hdfs_sink
# 以下配置 source
agent.sources.kafka_source.type = org.apache.flume.source.kafka.KafkaSource
agent.sources.kafka_source.channels = mem_channel
agent.sources.kafka_source.batchSize = 5000
agent.sources.kafka_source.kafka.bootstrap.servers = $kafkaIP:9092
agent.sources.kafka_source.kafka.topics = kafka_test
# 以下配置 sink
agent.sinks.hdfs_sink.type = hdfs
agent.sinks.hdfs_sink.channel = mem_channel
agent.sinks.hdfs_sink.hdfs.path = /data/flume/kafka/%Y%m%d（或cosn://bucket/xxx）
agent.sinks.hdfs_sink.hdfs.rollSize = 0  
agent.sinks.hdfs_sink.hdfs.rollCount = 0  
agent.sinks.hdfs_sink.hdfs.rollInterval = 3600  
agent.sinks.hdfs_sink.hdfs.threadsPoolSize = 30
agent.sinks.hdfs_sink.hdfs.fileType=DataStream    
agent.sinks.hdfs_sink.hdfs.useLocalTimeStamp=true
agent.sinks.hdfs_sink.hdfs.writeFormat=Text
# 以下配置 channel
agent.channels.mem_channel.type = memory
agent.channels.mem_channel.capacity = 100000
agent.channels.mem_channel.transactionCapacity = 10000
```
2. 运行 flume
```
./bin/flume-ng agent --conf ./conf/ -f kafka.properties -n agent -Dflume.root.logger=INFO,console
```
3. 运行 kafka 
```
producer./bin/kafka-console-producer.sh --broker-list $kafkaIP:9092 --topic kafka_test
test
hello
```

## 测试
 - 在 kafka 生产者客户端输入信息并回车。
 - 观察 hdfs 是否生成相应目录和文件`hadoop fs -ls /data/flume/kafka/`。

## 参考文档
[kafka-source 配置说明](https://flume.apache.org/FlumeUserGuide.html#kafka-source )
