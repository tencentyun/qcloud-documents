Apache Flume 是一个分布式、可靠、高可用的日志收集系统，支持各种各样的数据来源（如 HTTP、Log 文件、JMS、监听端口数据等），能将这些数据源的海量日志数据进行高效收集、聚合、移动，最后存储到指定存储系统中（如 Kafka、分布式文件系统、Solr 搜索服务器等）。

Flume 基本结构如下：
![](https://mc.qcloudimg.com/static/img/291cf61049ab4820c10c05c6f0900850/00.png)

Flume 以 agent 为最小的独立运行单位。一个 agent 就是一个 JVM，单个 agent 由 Source、Sink 和 Channel 三大组件构成。
![](https://mc.qcloudimg.com/static/img/17244b0d3460b838f7b6764db5497c98/11.png)

**Flume 与 Kafka**

把数据存储到 HDFS 或者 HBase 等下游存储模块或者计算模块时需要考虑各种复杂的场景，例如并发写入的量以及系统承载压力、网络延迟等问题。Flume 作为灵活的分布式系统具有多种接口，同时提供可定制化的管道。
在生产处理环节中，当生产与处理速度不一致时，Kafka 可以充当缓存角色。Kafka 拥有 partition 结构以及采用 append 追加数据，使 Kafka 具有优秀的吞吐能力；同时其拥有 replication 结构，使 Kafka 具有很高的容错性。
所以将 Flume 和 Kafka 结合起来，可以满足生产环境中绝大多数要求。

## Flume 接入开源 Kafka

### 准备工作

-	 下载 [Apache Flume](http://flume.apache.org/download.html) （1.6.0以上版本兼容 Kafka）
-	 下载 [Kafka工具包](https://kafka.apache.org/downloads) （0.9.x以上版本，0.8已经不支持）
-	 确认 Kafka 的 Source、 Sink 组件已经在 Flume 中。

### 接入方式

Kafka 可作为 Source 或者 Sink 端对消息进行导入或者导出。

<dx-tabs>
::: Kafka\sSource
配置 kafka 作为消息来源，即将自己作为消费者，从 Kafka 中拉取数据传入到指定 Sink 中。主要配置选项如下：

| 配置项                  | 说明                                              |
| :---------------------- | :------------------------------------------------ |
| channels                | 自己配置的 Channel                                |
| type                    | 必须为：org.apache.flume.source.kafka.KafkaSource |
| kafka.bootstrap.servers | Kafka Broker 的服务器地址                         |
| kafka.consumer.group.id | 作为 Kafka 消费端的 Group ID                      |
| kafka.topics            | Kafka 中数据来源 Topic                            |
| batchSize               | 每次写入 Channel 的大小                           |
| batchDurationMillis     | 每次写入最大间隔时间                              |

示例：

```
tier1.sources.source1.type = org.apache.flume.source.kafka.KafkaSource 
tier1.sources.source1.channels = channel1
tier1.sources.source1.batchSize = 5000
tier1.sources.source1.batchDurationMillis = 2000
tier1.sources.source1.kafka.bootstrap.servers = localhost:9092
tier1.sources.source1.kafka.topics = test1, test2
tier1.sources.source1.kafka.consumer.group.id = custom.g.id
```

更多内容请参考 [Apache Flume 官网](https://flume.apache.org/FlumeUserGuide.html)。

:::
:::Kafka\sSink
配置 Kafka 作为内容接收方，即将自己作为生产者，推到 Kafka Server 中等待后续操作。主要配置选项如下：

| 配置项                  | 说明                                          |
| :---------------------- | :-------------------------------------------- |
| channel                 | 自己配置的 Channel                            |
| type                    | 必须为：org.apache.flume.sink.kafka.KafkaSink |
| kafka.bootstrap.servers | Kafka Broker 的服务器                         |
| kafka.topics            | Kafka 中数据来源 Topic                        |
| kafka.flumeBatchSize    | 每次写入的 Bacth 大小                         |
| kafka.producer.acks     | Kafka 生产者的生产策略                        |

示例：

```
a1.sinks.k1.channel = c1
a1.sinks.k1.type = org.apache.flume.sink.kafka.KafkaSink
a1.sinks.k1.kafka.topic = mytopic
a1.sinks.k1.kafka.bootstrap.servers = localhost:9092
a1.sinks.k1.kafka.flumeBatchSize = 20
a1.sinks.k1.kafka.producer.acks = 1
```

更多内容请参考 [Apache Flume 官网](https://flume.apache.org/FlumeUserGuide.html)。

:::

</dx-tabs>

## Flume 接入 CKafka

<dx-tabs>
:::使用\sCKafka\s作为\sSink

#### 步骤1：获取 CKafka 实例接入地址
1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在左侧导航栏选择**实例列表**，单击实例的“ID”，进入实例基本信息页面。
3. 在实例的基本信息页面的**接入方式**模块，可获取实例的接入地址。
   ![](https://main.qcloudimg.com/raw/a28b5599889166095c168510ce1f5e89.png)


#### 步骤2：创建 Topic
1. 在实例基本信息页面，选择顶部**Topic管理**页签。
2. 在Topic管理页面，单击**新建**，创建一个名为 flume_test 的 Topic。
   ![](https://main.qcloudimg.com/raw/63f4119691d504bb759a11fbded9e4b0.png)


#### 步骤3：配置 Flume 
1. 下载 [Apache Flume 工具包并解压](http://flume.apache.org/download.html) 。
2. 编写配置文件 flume-kafka-sink.properties，以下是一个简单的 Demo（配置在解压目录的 conf 文件夹下），若无特殊要求则将自己的实例 IP 与 Topic 替换到配置文件当中即可。本例使用的 source 为 tail -F flume-test ，即文件中新增的信息。
   ![](https://mc.qcloudimg.com/static/img/daf5063d3c2c74eddb93f729eb6feb5b/55.png)
3. 执行如下命令启动 Flume。
   ```bash
   ./bin/flume-ng agent -n agentckafka -c conf -f conf/flume-kafka-sink.properties
   ```
4. 写入消息到 flume-test 文件中，此时消息将由 Flume 写入到 CKafka。
   ![](https://mc.qcloudimg.com/static/img/c9dc1f539e00f21fca1ead546f4e007e/66.png)
5. 启动 CKafka 客户端进行消费。
   ```bash
   ./kafka-console-consumer.sh --bootstrap-server xx.xx.xx.xx:xxxx --topic flume_test --from-beginning --new-consumer
   ```
	 
	 <dx-alert infotype="explain" title="">
	bootstrap-server 填写刚创建的 CKafka 实例的接入地址，topic 填写刚创建的 Topic 名称。
	</dx-alert>
   可以看到刚才的消息被消费出来。
   ![](https://mc.qcloudimg.com/static/img/ee394af9d8280bfef988d71ccc30f805/77.png)

:::

:::使用\sCKafka\s作为\sSource

#### 步骤1：获取 CKafka 实例接入地址

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在左侧导航栏选择**实例列表**，单击实例的“ID”，进入实例基本信息页面。
3. 在实例的基本信息页面的**接入方式**模块，可获取实例的接入地址。
   ![](https://main.qcloudimg.com/raw/a28b5599889166095c168510ce1f5e89.png)


#### 步骤2：创建 Topic

1. 在实例基本信息页面，选择顶部**Topic管理**页签。
2. 在 Topic 管理页面，单击**新建**，创建一个名为 flume_test 的 Topic。
   ![](https://main.qcloudimg.com/raw/63f4119691d504bb759a11fbded9e4b0.png)


#### 步骤3：配置 Flume

1. 下载 [Apache Flume 工具包并解压](http://flume.apache.org/download.html) 。
2. 编写配置文件 flume-kafka-source.properties，以下是一个简单的 Demo（配置在解压目录的 conf 文件夹下）。若无特殊要求则将自己的实例 IP 与 Topic 替换到配置文件当中即可。此处使用的 sink 为 logger。
   ![](https://mc.qcloudimg.com/static/img/18e5d3b3a533ef8e385e18301cc08961/88.png)
3. 执行如下命令启动 Flume。
   ```bash
   ./bin/flume-ng agent -n agentckafka -c conf -f conf/flume-kafka-source.properties
   ```
4. 查看 logger 输出信息（默认路径为`logs/flume.log`）。
   ![](https://mc.qcloudimg.com/static/img/d6b51f8de1a063e51171b2996764f40d/99.png)

:::

</dx-tabs>
