## Introduction to Apache Flume
Apache Flume is a tool/service or a data aggregation mechanism, which collects data resources such as logs and events and centrally stores large amounts of data from various data sources. As a highly available and distributed configuration tool, Flume is designed by means of aggregating data streams, such as log data, from many different website servers to a centralized storage like HDFS and HBase.
 
 The basic structure of Flume is shown below:
![Alt text](https://mc.qcloudimg.com/static/img/291cf61049ab4820c10c05c6f0900850/00.png)

Flume uses agent as the minimum unit of an independent operation. An agent is a JVM. A single agent consists of three major components: Source, Sink and Channel.
![Alt text](https://mc.qcloudimg.com/static/img/17244b0d3460b838f7b6764db5497c98/11.png)

## Why Flume + Kafka
When you store data in a downstream storage module or a computing module such as HDFS or HBase, a variety of complex scenarios must be considered, for example, the amount of concurrent writes, system-loading pressure, network delay, etc. Flume is designed as a flexible distributed system with multiple APIs, and also provides customizable pipelines.
During production processing, the processing speeds are generally different. In this case, Kafka can be used as a cache. With "partition" structure and "append" for data addition, Kafka has an excellent throughput performance. Besides, "replication" also makes it highly fault-tolerant.
Therefore, most of the requirements in the production environment can be met by combining these two tools.

## How to Connect to Open-source Kafka
### Supported Version
1.	The current version of Flume - Apache Flume 1.7.0 Released (released on October 17, 2016, and compatible with Kafka since version 1.6).
2.	Kafka 0.9.x series are supported, while 0.8 is not supported now.

### Preparations
1.	Apache Flume (1.6.0 or later)
2.	Kafka (0.9.x or later)
3.	Flume's Kafka - Source, Sink components (confirmed to be used in Flume)
### Flume and Kafka

Kafka can be used as "Source" or "Sink" to import or export messages.
**1.	Kafka Source**
By configuring Kafka as a message source, you can pull the data from Kafka to the specified Sink as a consumer.
Main configuration options:

| Configuration Item | Description |  
| :-------- | :--------| 
| channels |   Self-configured channel | 
| type	| Must be: org.apache.flume.source.kafka.KafkaSource |
| kafka.bootstrap.servers	| The server of Kafka broker |
| kafka.consumer.group.id	| The group id on the Kafka consumer side |
| kafka.topics	| The topic of data source in Kafka |
| batchSize	| The size of channel for each write |
| batchDurationMillis	 | The maximum time interval for each write |

Example:

```
tier1.sources.source1.type = org.apache.flume.source.kafka.KafkaSource 
tier1.sources.source1.channels = channel1
tier1.sources.source1.batchSize = 5000
tier1.sources.source1.batchDurationMillis = 2000
tier1.sources.source1.kafka.bootstrap.servers = localhost:9092
tier1.sources.source1.kafka.topics = test1, test2
tier1.sources.source1.kafka.consumer.group.id = custom.g.id
```

**2.	Kafka Sink**
By configuring Kafka as the content receiver, you can push the data to Kafka Server for subsequent operations as a producer.

Main configuration options:

| Configuration Item | Description |  
| :-------- | :--------| 
| channel |   Self-configured channel | 
| type	| Must be: org.apache.flume.sink.kafka.KafkaSink |
| kafka.bootstrap.servers	| The server of Kafka broker |
| kafka.topics	| The topic of data source in Kafka |
| flumeBatchSize	| The size of Batch for each write |
| kafka.producer.acks	 | 	The production policy of Kafka producer |

```
a1.sinks.k1.channel = c1
a1.sinks.k1.type = org.apache.flume.sink.kafka.KafkaSink
a1.sinks.k1.kafka.topic = mytopic
a1.sinks.k1.kafka.bootstrap.servers = localhost:9092
a1.sinks.k1.kafka.flumeBatchSize = 20
a1.sinks.k1.kafka.producer.acks = 1
```

For more information, please see official website:
https://flume.apache.org/FlumeUserGuide.html

## Connecting Flume to CKafka

### Preparations
- Apply for an instance in the Ckafka application page, and create a corresponding Topic.
- For apache flume, this tutorial uses the latest flume 1.7.0 (http://flume.apache.org/download.html).

### Creation of Ckafka
1)	After the application for instance is approved, you can see the information of your instance from the console.
 ![Alt text](https://mc.qcloudimg.com/static/img/6d7a67a6a7620f54fe6c81fe2374d358/10777-01.jpg)
2)	By clicking the instance name, you can see the specific information of assigned instance:
![](https://mc.qcloudimg.com/static/img/524d8de21d13ea5e3023cf25063a302a/10777-02.jpg)
3)	Click "Topic Management" to create a topic, where the name is flume_test.
 ![](https://mc.qcloudimg.com/static/img/734b0c829d949b045aa7ea1de75c89cc/10777-03.jpg)

Now, the operating environment of Ckafka has been created.

### Flume
1)	Download the Apache flume package from the official website, and then decompress it.
2)	Configure Flume options.
- Use Ckafka as Sink
a)	Write a configuration file, and focus on the combination of Flume and CKafka as Sink. Therefore, the default configuration is used for Source and Channel, which is not discussed here. The following is a simple demo (configured in the conf folder of the decompressed directory). Please note that, unless specified otherwise, use your own instance IP and topic to replace those in the configuration file:
 ![](https://mc.qcloudimg.com/static/img/daf5063d3c2c74eddb93f729eb6feb5b/55.png)
b)	The source used here is tail -F flume-test, which is the new information in the file
c)	Launch Flume:
```
./bin/flume-ng agent -n agentckafka -c conf -f conf/flume-kafka-sink.properties
```
d)	Write a message to the flume-test file, and then the message is written into CKafka by Flume
![](https://mc.qcloudimg.com/static/img/c9dc1f539e00f21fca1ead546f4e007e/66.png)
e)	Launch the CKafka client for consumption:
```
./kafka-console-consumer.sh --bootstrap-server 172.16.16.12:9092 --topic flume_test --from-beginning --new-consumer
```
You can see that the above message has been consumed out
 ![](https://mc.qcloudimg.com/static/img/ee394af9d8280bfef988d71ccc30f805/77.png)

- Use Ckafka as Source
a)	Write a configuration file, and focus on the combination of Flume and CKafka as Source. Therefore, the default configuration is used for Sink and Channel, which is not discussed here. The following is a simple demo (configured in the conf folder of the decompressed directory). Please note that, unless specified otherwise, use your own instance IP and topic to replace those in the configuration file:
 ![](https://mc.qcloudimg.com/static/img/18e5d3b3a533ef8e385e18301cc08961/88.png)

b)	The sink used here is logger
c)	Launch Flume:
```
./bin/flume-ng agent -n agentckafka -c conf -f conf/flume-kafka-source.properties
```
d)	View the output information of logger (default path is logs/flume.log)
![](https://mc.qcloudimg.com/static/img/d6b51f8de1a063e51171b2996764f40d/99.png)
 


