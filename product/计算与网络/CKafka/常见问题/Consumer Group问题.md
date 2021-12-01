
### 怎样设置合理的消费者数量？

消费组和消费者的对应关系如下：
- 一个消费者可以同时订阅多个 Topic。
- 一个 Topic 里面包含了1到多个分区。
- 一个分区只能被一个消费者消费。

所以，一个消费组里面，消费者数量上限 = topic1的分区数 + topic2的分区数 +...... + topicN 的分区数。

关于消费者的定义：消费者在代码层面指的是一个 Consumer 的对象，一个机器上可以有多个消费者，例如起多个线程，一个线程里面有一个 Consumer，以此类推，如下面代码所示：
```java
Properties props = new Properties();
props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrap);
KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
consumer.subscribe(Arrays.asList(topic));
while (true) {
            ConsumerRecords<String, String> records = consumer.poll(100);
}
```
初始的消费者数量可以根据客户端的资源情况进行初始的部署，然后配置消费者组的堆积告警，如果出现堆积的时候再扩容消费者。配置告警方式参考 [配置告警](https://cloud.tencent.com/document/product/597/57244)，配置页面如下图所示。
![](https://main.qcloudimg.com/raw/d84892ff3a2cf3f37340e213454e3308.png)


