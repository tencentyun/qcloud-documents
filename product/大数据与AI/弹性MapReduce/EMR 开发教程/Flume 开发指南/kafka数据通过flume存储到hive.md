## 场景说明
将 Kafka 中的数据通过 Flume 收集并存储到 Hive。

## 开发准备
- 因为任务中需要访问腾讯云消息队列 CKafka，所以需要先创建一个 CKafka 实例，具体见 [消息队列 CKafka](https://cloud.tencent.com/document/product/597)。
- 确认您已开通腾讯云，且已创建一个 EMR 集群。创建 EMR 集群时，需要在软件配置界面选择 Spark 组件。

## 在 EMR 集群使用 Kafka 工具包
首先需要查看 CKafka 的内网 IP 与端口号。登录消息队列 CKafka 的控制台，选择您要使用的 CKafka 实例，在基本消息中查看其内网 IP 为 $kafkaIP，而端口号一般默认为9092。在 topic 管理界面新建一个 topic 为 kafka_test。

## 配置 flume
1. 创建 flume 的配置文件`hive_kafka.properties`
```
vim hive_kafka.properties
agent.sources = kafka_source
agent.channels = mem_channel
agent.sinks = hive_sink
# 以下配置 source
agent.sources.kafka_source.type = org.apache.flume.source.kafka.KafkaSource
agent.sources.kafka_source.channels = mem_channel
agent.sources.kafka_source.batchSize = 5000
agent.sources.kafka_source.kafka.bootstrap.servers = $kafkaIP:9092
agent.sources.kafka_source.kafka.topics = kafka_test
# 以下配置 sink
agent.sinks.hive_sink.channel = mem_channel
agent.sinks.hive_sink.type = hive
agent.sinks.hive_sink.hive.metastore = thrift://172.16.32.51:7004
agent.sinks.hive_sink.hive.database = default
agent.sinks.hive_sink.hive.table = weblogs
agent.sinks.hive_sink.hive.partition = asia,india,%y-%m-%d-%H-%M
agent.sinks.hive_sink.useLocalTimeStamp = true
agent.sinks.hive_sink.round = true
agent.sinks.hive_sink.roundValue = 10
agent.sinks.hive_sink.roundUnit = minute
agent.sinks.hive_sink.serializer = DELIMITED
agent.sinks.hive_sink.serializer.delimiter = ","
agent.sinks.hive_sink.serializer.serdeSeparator = ','
agent.sinks.hive_sink.serializer.fieldnames =id,msg
# 以下配置 channel
agent.channels.mem_channel.type = memory
agent.channels.mem_channel.capacity = 100000
agent.channels.mem_channel.transactionCapacity = 100000
```
其中 hive.metastore 可以通过以下方式确认：
```
grep "hive.metastore.uris" -C 2 /usr/local/service/hive/conf/hive-site.xml
```
```
<property>
<name>hive.metastore.uris</name>
<value>thrift://172.16.32.51:7004</value>
</property>
```
2. 创建 hive 表
```
create table weblogs ( id int , msg string )
partitioned by (continent string, country string, time string)
clustered by (id) into 5 buckets
stored as orc TBLPROPERTIES ('transactional'='true');
```
>!一定要是分区且分桶的表，存储为 orc 且设置 TBLPROPERTIES ('transactional'='true')，以上条件缺一不可。
3. 开启 hive 事务
在控制台给`hive-site.xml`添加以下配置项。
```
<property>
<name>hive.support.concurrency</name>
<value>true</value>
</property>
<property>
<name>hive.exec.dynamic.partition.mode</name>
<value>nonstrict</value>
</property>
<property>
<name>hive.txn.manager</name>
<value>org.apache.hadoop.hive.ql.lockmgr.DbTxnManager</value>
</property>
<property>
<name>hive.compactor.initiator.on</name>
<value>true</value>
</property>
<property>
<name>hive.compactor.worker.threads</name>
<value>1</value>
</property>
<property>
<name>hive.enforce.bucketing</name>
<value>true</value>
</property>
```
>!配置下发并重启后，在`hadoop-hive`日志中会提示 metastore 无法连接，请忽略该错误。由于进程启动顺序导致，需先启动 metastore 再启动 hiveserver2。
4. 复制 hive 的`hive-hcatalog-streaming-xxx.jar`到 flume 的 lib 目录
```
cp -ra /usr/local/service/hive/hcatalog/share/hcatalog/hive-hcatalog-streaming-2.3.3.jar /usr/local/service/flume/lib/
```
5. 运行 flume
```
./bin/flume-ng agent --conf ./conf/ -f hive_kafka.properties -n agent -Dflume.root.logger=INFO,console
```
6. 运行 kafka producer
```
[hadoop@172 kafka]$ ./bin/kafka-console-producer.sh --broker-list $kafkaIP:9092 --topic kafka_test
1,hello
2,hi
```

## 测试
 - 在 kafka 生产者客户端输入信息并回车。
 - 观察 hive 表中是否有相应数据。

## 参考文档
- [hive-sink 配置说明](https://flume.apache.org/FlumeUserGuide.html#hive-sink)
- [hive 日志配置说明](https://cwiki.apache.org/confluence/display/Hive/Hive+Transactions#HiveTransactions-NewConfigurationParametersforTransactions)
