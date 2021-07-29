CKafka 兼容0.9及以上的生产/消费接口（目前可以直接购买的版本包括0.10.2、1.1.1、2.4.1、2.8.1版本），如果接入低版本（如0.8版本）的自建 Kafka，您需要对接口进行相应改造。本文将从生产端和消费端对比0.8版本 Kafka 和高版本 Kafka，并提供改造方式。

## Kafka Producer 

### 概述

Kafka 0.8.1版本中，Producer API 被重写。该客户端为官方推荐版本，其拥有更好的性能和更多的功能，社区将维护新版本的 Producer API。


### 新旧版本 Producer API 对比

- 新版 Producer API Demo

```
Properties props = new Properties();
props.put("bootstrap.servers", "localhost:4242");
props.put("acks", "all");
props.put("retries",0);
props.put("batch.size", 16384);
props.put("linger.ms", 1);
props.put("buffer.memory", 33554432);
props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
Producer<String, String> producer = new KafkaProducer<>(props);
producer.send(new ProducerRecord<String, String>("my-topic", Integer.toString(0), Integer.toString(0)));
producer.close();
```

- 旧版 Producer API Demo

```
Properties props = new Properties();
props.put("metadata.broker.list", "broker1:9092");
props.put("serializer.class", "kafka.serializer.StringEncoder");
props.put("partitioner.class", "example.producer.SimplePartitioner");
props.put("request.required.acks", "1");
ProducerConfig config = new ProducerConfig(props);
Producer<String, String> producer = new Producer<String, String>(config);
KeyedMessage<String, String> data = new KeyedMessage<String, String>("page_visits", ip, msg);
producer.send(data);
producer.close();
```

可以看出新旧版本的使用方法基本一致，只有一些参数的配置不同，改造代价不大。

### 兼容性说明

对于 Kafka 而言，0.8.x 版本的 Producer API 都可以顺利接入 CKafka，无需改造。推荐使用新版 Kafka Producer API。

## Kafka Consumer 

### 概述

开源 Apache Kafka 0.8版本中提供了两种消费者 API，分别为：

- High Level Consumer API （屏蔽配置细节）
- Simple Consumer API （配置细节支持指定）

Kafka 0.9.x 版本引入了 New Consumer，其融合了 Old Consumer（0.8版本）两种 Consumer API 的特性，减轻了 ZooKeeper 的负载。
因此下文给出了0.8版本 Consumer 转换为0.9版本 New Consumer 的方式。

### 新旧版本 Consumer API 对比   

#### 0.8版本 Consumer API 

- **High Level Consumer API**（[参考 Demo](https://cwiki.apache.org/confluence/display/KAFKA/Consumer+Group+Example)）
  如果您只需要数据而不考虑消息 offset 相关的处理时，High Level API 可以满足一般性消费要求。High Level Consumer API 围绕着 Consumer Group 逻辑概念展开，屏蔽 Offset 管理、具有 Broker 异常处理、Consumer 负载均衡功能。使开发者可以快速上手 Consumer 客户端。
  在使用 High Level Consumer 时需要注意以下几点：
 - 如果消费线程大于 Partition 个数，某些消费线程将无法获得数据。
 - 如果 Partition 个数大于线程数目，某些线程会消费多个 Partition。
 - Partition 和消费者变动会影响 Rebalance。


- **Low Level Consumer API**（[参考 Demo](https://cwiki.apache.org/confluence/display/KAFKA/0.8.0+SimpleConsumer+Example)）
  如果使用者关心消息的 offset 并且希望进行重复消费或者跳读等功能、又或者希望指定某些 partition 进行消费时和确保更多消费语义时推荐使用 Low Level Consumer API。但是使用者需要自己处理 Offset 以及 Broker 的异常情况。
  在使用 Low Level Consumer 时需要注意以下几点：
 - 自行跟踪维护 Offset，控制消费进度。
 - 查找 Topic 相应 Partition 的 Leader，以及处理 Partition 变更情况。


#### 0.9版本 New Consumer API

Kafka 0.9.x 版本引入了 New Consumer，其融合了 Old Consumer 两种 Consumer API 的特性，同时提供消费者的协调(高级 API)和 lower-level 访问，并构建自定义的消费策略。New Consumer 还简化了消费者客户端，引入中心 Coordinator，解决分别连接 ZooKeeper 产生的 Herd Effect 和 Split Brain 问题，同时也减轻了 ZooKeeper 的负载。

**优势：**

- Coordinator 引入
  当前版本的 High Level Consumer 存在 Herd Effect 和 Split Brain 的问题。将失败探测和 Rebalance 的逻辑放到一个高可用的中心 Coordinator，那么这两个问题即可解决。同时还可很大程度的减少 ZooKeeper 的负载。
- 允许自己分配 Partition
  为了保持本地每个分区的一些状态不变，所以需要将 Partition 的映射也保持不变。另外一些场景是为了让 Consumer 与地域相关的 Broker 关联。
- 允许自己管理 Offset
  可以根据自己需要去管理 Offset，实现重复、跳跃消费等语意。
- Rebalance 后触发用户指定的回调
- 非阻塞式 Consumer API

#### 新旧版本 Consumer API 功能对比

| 种类                | 引入版本   | Offset 自动保存 | Offset 自行管理 | 自动进行异常处理 | Rebalance 自动处理 | Leader 自动查找 | 优缺点                     |
| ------------------- | ---------- | --------------- | --------------- | ---------------- | ------------------ | --------------- | -------------------------- |
| High Level Consumer | Before 0.9 | 支持            | 不支持          | 支持             | 支持               | 支持            | Herd Effect 和 Split Brain |
| Simple Consumer     | Before 0.9 | 不支持          | 支持            | 不支持           | 不支持             | 不支持          | 需要处理多种异常情况       |
| New Consumer        | After 0.9  | 支持            | 支持            | 支持             | 支持               | 支持            | 成熟，当前版本推荐         |

####  Old Consumer 转换 New Consumer

-  New Consumer

```
//config中主要变化是 ZooKeeper 参数被替换了
Properties props = new Properties();
props.put("bootstrap.servers", "localhost:9092");
props.put("group.id", "test");
props.put("enable.auto.commit", "true");
props.put("auto.commit.interval.ms", "1000");
props.put("session.timeout.ms", "30000");
props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
// 相比old consumer 而言，这里创建消费者更加简单 
KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
consumer.subscribe(Arrays.asList("foo", "bar"));
while (true) {
    ConsumerRecords<String, String> records = consumer.poll(100);
    for (ConsumerRecord<String, String> record : records)
       System.out.printf("offset = %d, key = %s, value = %s", record.offset(), record.key(), record.value());}
```

- Old Consumer （High Level）

```
//  old consumer 需要 ZooKeeper
Properties props = new Properties();
props.put("zookeeper.connect", "localhsot:2181");
props.put("group.id", "test");
props.put("auto.commit.enable", "true");
props.put("auto.commit.interval.ms", "1000");
props.put("auto.offset.reset", "smallest");
ConsumerConfig config = new ConsumerConfig(props);
// 需要创建connector 
ConsumerConnector connector = Consumer.createJavaConsumerConnector(config);
// 创建message stream
Map<String, Integer> topicCountMap = new HashMap<String, Integer>();
topicCountMap.put("foo", 1);
Map<String, List<KafkaStream<byte[], byte[]>>> streams =
 connector.createMessageStreams(topicCountMap);
// 获取数据 
KafkaStream<byte[], byte[]> stream = streams.get("foo").get(0);
ConsumerIterator<byte[], byte[]> iterator = stream.iterator();
MessageAndMetadata<byte[], byte[]> msg = null;
while (iterator.hasNext()) {
     msg = iterator.next();
     System.out.println(//
            " group " + props.get("group.id") + //
            ", partition " + msg.partition() + ", " + //
             new String(msg.message()));
}
```

可以看到，改造成 New Consumer 编写更加简单，最主要的变化是将 ZooKeeper 参数的输入替代成了 Kafka 地址输入。同时，New Consumer 也增加了与 Coodinator 交互的参数配置，一般情况下使用默认配置就足够。

### 兼容性说明

CKafka 与开源社区高版本的 Kafka 一致，支持重写后的 New Consumer API，屏蔽了 Consumer 客户端与 Zookeeper 的交互（Zookeeper不再向用户暴露）。New Consumer 解决原有与 Zookeeper 直接交互的 Herd Effect 和 Split Brain 问题，以及融合了原有 Old Consumer 的特性，使消费环节更加可靠。
