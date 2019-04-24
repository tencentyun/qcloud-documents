## Apache Flume简介
Apache Flume 是一个从可以收集例如日志，事件等数据资源，并将这些数量庞大的数据从各项数据资源中集中起来存储的工具/服务，或者数集中机制。flume具有高可用，分布式，配置工具，其设计的原理也是基于将数据流。
 
 Flume基本结构如下图所示：
![Alt text](https://mc.qcloudimg.com/static/img/291cf61049ab4820c10c05c6f0900850/00.png)

Flume以agent为最小的独立运行单位。一个agent就是一个JVM。单agent由Source、Sink和Channel三大组件构成。
![Alt text](https://mc.qcloudimg.com/static/img/17244b0d3460b838f7b6764db5497c98/11.png)

## Why Flume + Kafka
把数据存储到hdfs或者hbase等下游存储模块或者计算模块时需要考虑各种复杂的场景，比如并发写入的量以及系统承载压力，网络延迟等等问题。flume设计为灵活的分布式系统具有多种接口，同时提供可定制化的管道。
在成产处理环节中，往往出现生产处理速度不一致的情况，此时kafka可以充当缓存角色。拥用partition结构以及采用append追加数据，使kafka具有优秀的吞吐能力。同时其拥有replication具有很高的容错性。
所以将两者结合起来，可以满足生产环境中绝大多数要求。

## 开源Kafka接入方式
### 版本支持
1.	Flume当前版本 – Apache Flume 1.7.0 Released （October 17, 2016发布，1.6之后才兼容kafka）
2.	支持Kafka 0.9.x series， 0.8已经不支持

### 准备工作
1.	Apache Flume （版本1.6.0以上）
2.	Kafka （版本0.9.x以上）
3.	Flume的Kafka –Source、 Sink组件（确认已经在Flume中）
### Flume与Kafka

Kafka可作为Source或者Sink端对消息进行导入或者导出。
**1.	Kafka Source**
配置kafka作为消息来源，即将自己作为消费者，从Kafka中拉取数据传入到指定Sink中
主要配置选项：

| 配置项 |  说明  |  
| :-------- | :--------| 
| channels |   自己配置的channel | 
| type	| 必须为：org.apache.flume.source.kafka.KafkaSource|
| kafka.bootstrap.servers	| Kafka broker的服务器 |
|kafka.consumer.group.id	| 作为Kafka消费端的group id |
|kafka.topics	| Kafka中数据来源topic.|
|batchSize	| 每次写入channel的大小|
|batchDurationMillis	 | 每次写入最大间隔时间|

example：

```
tier1.sources.source1.type = org.apache.flume.source.kafka.KafkaSource 
tier1.sources.source1.channels = channel1
tier1.sources.source1.batchSize = 5000
tier1.sources.source1.batchDurationMillis = 2000
tier1.sources.source1.kafka.bootstrap.servers = localhost:9092
tier1.sources.source1.kafka.topics = test1, test2
tier1.sources.source1.kafka.consumer.group.id = custom.g.id
```

2.	Kafka Sink
配置kafka作为内容接收方，即将自己作为生产者，推到Kafka Server中等待后续操作

主要配置选项：

| 配置项 |  说明  |  
| :-------- | :--------| 
| channel |   自己配置的channel | 
| type	| 必须为：org.apache.flume.sink.kafka.KafkaSink |
| kafka.bootstrap.servers	| Kafka broker的服务器 |
|kafka.topics	| Kafka中数据来源topic.|
|flumeBatchSize	| 每次写入的Bacth大小 |
|kafka.producer.acks	 | 	Kafka生产者的生产策略 |

```
a1.sinks.k1.channel = c1
a1.sinks.k1.type = org.apache.flume.sink.kafka.KafkaSink
a1.sinks.k1.kafka.topic = mytopic
a1.sinks.k1.kafka.bootstrap.servers = localhost:9092
a1.sinks.k1.kafka.flumeBatchSize = 20
a1.sinks.k1.kafka.producer.acks = 1
```

更详细的内容可以参考官网链接：
https://flume.apache.org/FlumeUserGuide.html

## Flume接入CKafka

### 准备工作
- 在Ckafka申请页中申请实例，并且创建对应的Topic
- apache flume ，本教程使用的是最新的flume 1.7.0 （http://flume.apache.org/download.html)

### Ckafka创建
1）	拥有实例后，可从控制台中可以看到自己的实例信息
 ![Alt text](https://mc.qcloudimg.com/static/img/67f19ef17a73e768fba188d58ae08f9a/22.png)
2）	点击实例名称可以看到实例分配的具体信息：
![](https://mc.qcloudimg.com/static/img/3841d4eb19ad992d35e60196b38498ce/33.png)
3）	点击topic管理，创建topic，此处名字为flume_test
 ![](https://mc.qcloudimg.com/static/img/9f069263c59539be5dcf845bba0b0455/44.png)

至此，Ckafka相关的工作环境完成。

### Flume
1）	从官方下载Apache flume压缩包，进行解压
2）	配置Flume选项
- 使用 Ckafka 作为Sink
a)	编写配置文件，此处重点放在flume 与ckafka作为Sink结合上，所以Source和Channel使用默认配置，不做详细介绍。以下是一个简单的demo （配置在解压目录的conf文件夹下），需要注意的是，若无特殊要求则将自己的实例ip与topic替换到配置文件当中即可：
 ![](https://mc.qcloudimg.com/static/img/daf5063d3c2c74eddb93f729eb6feb5b/55.png)
b)	此处使用的source为tail -F flume-test ，即文件中新增的信息
c)	启动flume ：
```
./bin/flume-ng agent -n agentckafka -c conf -f conf/flume-kafka-sink.properties
```
d)	写入消息到flume-test文件中，此时消息将由flume写入到ckafka
![](https://mc.qcloudimg.com/static/img/c9dc1f539e00f21fca1ead546f4e007e/66.png)
e)	启动ckafka客户端进行消费：
```
./kafka-console-consumer.sh --bootstrap-server 172.16.16.12:9092 --topic flume_test --from-beginning --new-consumer
```
可以看到刚刚的消息被消费出来了
 ![](https://mc.qcloudimg.com/static/img/ee394af9d8280bfef988d71ccc30f805/77.png)

- 使用 Ckafka 作为Source
a)	编写配置文件，此处重点放在flume 与ckafka作为Source结合上，所以Sink和Channel使用默认配置，不做详细介绍。以下是一个简单的demo （配置在解压目录的conf文件夹下）。需要注意的是，若无特殊要求则将自己的实例ip与topic替换到配置文件当中即可：
 ![](https://mc.qcloudimg.com/static/img/18e5d3b3a533ef8e385e18301cc08961/88.png)

b)	此处使用的sink为logger
c)	启动flume ：
```
./bin/flume-ng agent -n agentckafka -c conf -f conf/flume-kafka-source.properties
```
d)	查看logger输出信息（默认路径 logs/flume.log）
![](https://mc.qcloudimg.com/static/img/d6b51f8de1a063e51171b2996764f40d/99.png)
 

