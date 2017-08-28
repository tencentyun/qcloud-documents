Ckafka起初以兼容0.9.x版本为目标，后续开发了0.10.x兼容版本。Ckafka兼容0.9系列以及0.10系列的生产/消费接口。但是现在暂不开放Zookeeper地址，所以对于需要Zookeeper地址的High Level Consumer API暂不提供支持。
## Kafka Producer Type
### Producer变化
Kafka 0.8.1版本中，Producer API被重写。该客户端被官方推荐，其拥有更好的性能以及更多的功能，后续社区将维护新版本的Producer API。
### Producer改造
1）	新API写法DEMO
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
2）	旧API写法DEMO
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
可以看出两者区别不大，基本使用方法保持一致只是一些参数配置的变化，改造代价不大。
### Ckafka兼容性说明
对于Ckafka而言，0.8.x的 新/旧 的Producer API都可以顺利接入Ckafka无需改造，我们推荐与社区一样使用新的Kafka Producer Api，其拥有更多配置，功能更加完善。
## Kafka Consumer Type
### Old Consumer
- High Level Consumer API
如果只需要数据而不需要考虑消息offset相关的处理时，High Level API就满足一般性消费要求，High Level Consumer API围绕着Consumer Group这个逻辑概念展开，它屏蔽Offset管理、具有Broker异常处理、Consumer负载均衡功能。使开发者可以快速的上手Consumer客户端。
在使用High Level Consumer时需要注意以下几点：
1）如果消费线程大于Partition个数，意味着某些消费线程将无法获得数据
2）如果Partition个数大于线程数目，某些线程会消费多个Partition
3）Partition和消费者变动会影响Rebalance

[参考DEMO](https://cwiki.apache.org/confluence/display/KAFKA/Consumer+Group+Example)

- Low Level Consumer API
如果使用者关心消息的offset并且希望进行重复消费或者跳读等功能、又或者希望指定某些partition进行消费时和确保更多消费语义时推荐使用Low Level Consumer API。但是使用者需要自己处理Offset以及Broker的异常情况。
在使用Low Level Consumer时需要注意以下几点：
1）	自行跟踪维护Offset，控制消费进度
2）	查找Topic相应Partition的Leader，以及处理Partition变更情况

[参考DEMO](https://cwiki.apache.org/confluence/display/KAFKA/0.8.0+SimpleConsumer+Example)
- New Consumer （After 0.9.x）
**为什么使用 New Consumer**
Kafka 0.9.x 版本引入了 New Consumer，其融合了Old Consumer两种Consumer API的特性,同时提供消费者的协调(高级API)和lower-level的访问,来构建自定义的消费策略。New Consumer还简化了消费者客户端并且引入了中心Coordinator解决分别连接Zookeeper产生的 Herd Effect和Split Brain 问题同时还减轻了Zookeeper的负载。
**优势：**
1）	Coordinator引入
当前版本的High Level Consumer存在Herd Effect和Split Brain的问题。将失败探测和Rebalance的逻辑放到一个高可用的中心Coordinator，那么这两个问题即可解决。同时还可大大减少 Zookeeper的负载。
2）	允许自己分配Partition
为了保持本地每个分区的一些状态不变，所以需要将Partition的映射也保持不变。另外一些场景是为了让Consumer与地域相关的Broker关联。
3）	允许自己管理Offset
可以根据自己需要去管理Offset，实现重复、跳跃消费等语意。
4）	Rebalance后触发用户指定的回调
5）	非阻塞式Consumer API

**New Consumer 对比 Old Consumer**

| 种类 | 引入版本 | Offset自动保存 | Offset自行管理 | 自动进行异常处理 | Rebalance自动处理 | Leader自动查找 | 缺点 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| High Level Consumer | Before 0.9 | 支持 | 不支持 | 支持 | 支持 | 支持 | Herd Effect和Split Brain |
| Simple Consumer | Before 0.9 | 不支持 | 支持 | 不支持 | 不支持 | 不支持 | 需要处理多种异常情况 |
| New Consumer | After 0.9 | 支持 | 支持 | 支持 | 支持 | 支持 | 成熟，当前版本推荐 |

**Old Consumer 转成 New Consumer**
1. New Consumer

```
//config中主要变化是 zookeeper参数被替换了
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

2. Old Consumer （High Level）

```
//  old consumer 需要 zookeeper
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
}}
```

对比可以看到，改造成New Consumer编写更加简单，最主要的变化是隐藏了Zookeeper的参数的输入替代成了Kafka地址输入。同时，New Consumer也增加了与Coodinator交互的参数配置，一般情况下使用默认配置就足够。
### Ckafka版本推荐
Ckafka与社区新版本Kafka一致支持New Consumer方式，屏蔽了Consumer客户端与Zookeeper的交互（Zookeeper不再向用户暴露）。使用New Consumer解决原有与Zookeeper直接交互的 Herd Effect和Split Brain 问题，以及融合了原有Old Consumer的特性，使消费环节更加可靠。



