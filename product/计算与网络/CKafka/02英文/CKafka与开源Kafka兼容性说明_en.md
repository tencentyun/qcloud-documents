Ckafka was initially designed to be compatible with version 0.9.x of Producer/Consumer APIs. With the 0.10.x-compatible versions developed, Ckafka now has the compatibility with 0.9.x and 0.10.x versions of producer/consumer APIs. As the Zookeeper address is unavailable, the High Level Consumer API requiring Zookeeper address is not supported.
## Kafka Producer Type
### Changes to Producer
In Kafka 0.8.1, the Producer API is overwritten. This version of client is officially recommended for its better performance and more features. The community will maintain a new version of the Producer API.
### Transformation of Producer
(1)	DEMO on how the new API is written
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
(2)	DEMO on how the old API is written
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
As shown above, there is not much difference between the two. The basic usage remains the same, except for the changes in the configuration of some parameters. Therefore, the transformation cost is not high.
### Ckafka Compatibility
Both the new and old 0.8.x Producer APIs can be interfaced with Ckafka smoothly without modification. We recommend using the new Kafka Producer API, as the community does, for more configurations and features.
## Kafka Consumer Type
### Old Consumer
- High Level Consumer API
The High Level API can meet the general consumption requirements if only data is needed and you don't need to consider the processing of message offset. The High-Level Consumer API, built on the logic of Consumer Group, blocks the Offset management and features the capability of Broker exception handling and Consumer load balancing, allowing developers to get started with the Consumer client quickly.
The following need to be considered when you use the High Level Consumer:
(1) If the number of consumer threads is greater than the number of Partitions, some consumer threads cannot get the data.
(2) If the number of Partitions is greater than the number of threads, some threads consume more than one Partitions.
(3) The changes in Partitions and consumers can affect the Rebalance.

[DEMO](https://cwiki.apache.org/confluence/display/KAFKA/Consumer+Group+Example)

- Low Level Consumer API
Low Level Consumer API is recommended if you care about the message offset and need such features as repeated consumption or skip read, or want to specify certain partitions for consumption and ensure more consumption semantics. But in this case, you need to handle the exceptions of Offset and Broker by yourself.
The following need to be considered when you use the Low Level Consumer:
(1) You need to track and maintain the Offset and control the consumption progress by yourself.
(2) You need to find the Leader of Partitions for the Topic, and deal with the Partition changes.

[DEMO](https://cwiki.apache.org/confluence/display/KAFKA/0.8.0+SimpleConsumer+Example)
- New Consumer (After 0.9.x)
**Why use the New Consumer**
Kafka 0.9.x has introduced the New Consumer, which incorporates the features of Old Consumer while providing consumer coordination (advanced API) and lower-level access to build the custom consumption policies. The New Consumer also simplifies the consumer client and introduces a central Coordinator to solve the Herd Effect and Split Brain problems resulting from the separate connections to Zookeeper, and to reduce the load on Zookeeper.
**Advantages:**
(1) Introduction of Coordinator
The current version of High Level Consumer has the Herd Effect and Split Brain problems .Putting the logics of failure detection and Rebalance into a highly available central Coordinator can solve both of the problems, while greatly reducing the load on the Zookeeper.
(2)	Allow you to assign partitions by yourself.
In order to keep some statuses of each local Partition the same, you need to maintain the mapping of Partitions. Some other scenarios are designed to associate the Consumer with the region-dependent Broker.
(3)	Allow you to manage Offset
You can manage the Offset as needed and implement repeated consumption, skipped consumption and other semantics.
(4)	Trigger user-specified callbacks after Rebalance
(5)	Non-blocking Consumer API

**Comparison between New Consumer and Old Consumer**

| Category | Introduced Version | AutoSave of Offset | Self-management of Offset | Automatic Exception Handling | Automatic Rebalance Processing | Auto Search of Leader | Disadvantages |
| --- | --- | --- | --- | --- | --- | --- | --- |
| High Level Consumer | Before 0.9 | Yes | No | Yes | Yes | Yes | Herd Effect and Split Brain |
| Simple Consumer | Before 0.9 | No | Yes | No | No | No | Multiple exceptions need to be handled |
| New Consumer | After 0.9 | Yes | Yes | Yes | Yes | Yes | Mature. The current version is recommended |

**Old Consumer is transformed to New Consumer**
1. New Consumer

```
//The main change in config is that the Zookeeper parameter is replaced
Properties props = new Properties();
props.put("bootstrap.servers", "localhost:9092");
props.put("group.id", "test");
props.put("enable.auto.commit", "true");
props.put("auto.commit.interval.ms", "1000");
props.put("session.timeout.ms", "30000");
props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
// Compared to old Consumer, the new Consumer makes it easier to create consumers 
KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
consumer.subscribe(Arrays.asList("foo", "bar"));

while (true) {
    ConsumerRecords<String, String> records = consumer.poll(100);
    for (ConsumerRecord<String, String> record : records)
       System.out.printf("offset = %d, key = %s, value = %s", record.offset(), record.key(), record.value());}
```

2. Old Consumer (High Level)

```
//  Zookeeper is needed
Properties props = new Properties();
props.put("zookeeper.connect", "localhsot:2181");
props.put("group.id", "test");
props.put("auto.commit.enable", "true");
props.put("auto.commit.interval.ms", "1000");
props.put("auto.offset.reset", "smallest");
ConsumerConfig config = new ConsumerConfig(props);
// Creation of connector is needed 
ConsumerConnector connector = Consumer.createJavaConsumerConnector(config);
// Create message stream
Map<String, Integer> topicCountMap = new HashMap<String, Integer>();
topicCountMap.put("foo", 1);
Map<String, List<KafkaStream<byte[], byte[]>>> streams =
 connector.createMessageStreams(topicCountMap);
// Get data 
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

As shown above, transforming into New Consumer simplifies the writing. The main change is the input of Zookeeper parameters is replaced by the input of Kafka address. In addition, the configuration of parameters interacting with Coordinator are added. Generally, it is sufficient to use the default configuration.
### Recommended Ckafka version
Both Ckafka and the new version of Kafka in the community support the New Consumer, which blocks the interaction between the Consumer client and Zookeeper (Zookeeper is not exposed to users any longer). The New Consumer solves the Herd Effect and Split Brain problems resulting from the direct interaction with Zookeeper, and integrates the features of Old Consumer, thus making the consumption more reliable.




