### 消费组列表详情缺失如何处理？

#### 现象描述

CKafka 的消费组列表有消费组名称，点开详情，却没有消费详情。例如：下图的消费组 CR 没有展示详情。
![](https://main.qcloudimg.com/raw/c1cdbfb124ec0dfd2829a6c011c4c9b3.png)

#### 可能原因

Kafka 的数据消费有两种模式，消费组模式和自定义分区消费模式。

- 当使用消费组模式消费，客户端会通过消费协调者进行协调消费，在消费数据完成后，会往服务端提交 offset 的存储请求。则此时服务端会存储消费的 Topic、分区进度、客户端等信息。
- 当使用自定义分区消费的模式，则客户端不会自动往服务端提交 offset 存储请求，则此时如果客户端没有主动发起提交 offset 请求，则服务端是看不到消费的相关信息的。
- 当 Topic 设置了 ACL 以后，某些实例可能会出现无法看到消费者组的详情，如果出现无法看详情，请先检查是否有 ACL，如果有，则需要您 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行处理。


#### 解决方法

1. 查看实例的消费组列表。
   ```
   ]$ bin/kafka-consumer-groups.sh --bootstrap-server 9.146.153.249:9092 --list
   CR
   ```
   可以看到当前的所有消费组名称。  

2. 查看实例特定的消费组详情。
   ```
   ]$ bin/kafka-consumer-groups.sh --bootstrap-server 9.146.153.249:9092 --describe --group CR
   Note: This will not show information about old Zookeeper-based consumers.
   ```
   会发现该消费组并没有详情。这表示消费者客户端没有使用 consumerGroup 机制去消费数据。即客户端没有往服务端提交消费详情，服务端没有存储消费数据，则不会正常显示。

3. 定位是否是服务端的问题
   通过原生自带的消费组命令，指定消费组名称 test1 进行消费，如下所示: 
   ```
   ]$ bin/kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --from-beginning --topic test --group test1
   ```
   则在控制台能正常显示的消费组，通过 `--describe` 命令是可以看到详情的，如下所示：
   ![](https://main.qcloudimg.com/raw/d54eb823fe66da94364849e670f83fba.png)

   



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


### Consumer Group 持续出现 PreparingRebalance 的状态的原因是什么？

以下情况可能会发生 Rebalance：
1. 有新的消费者加入消费者组。
2. 当前运行消费者停止运行，离开消费者组。常见的情况如消费者重启，消费者应用崩溃，消费者进程上报的心跳超时等（详请参见 [CKafka 常用参数配置指南](https://cloud.tencent.com/document/product/597/30203)）。
3. 分区数变动的时候(增加或删除)。

其中，1和3两种情况无法避免 rebalance。正常情况，rebalance 在30s内能完成。如果出现长期的 rebalance，需要 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行处理。

如果是由于心跳超时或者两次 poll 时间间隔太大导致的问题，您可以调整如下参数：
```bash
# 使用 Kafka 消费分组机制时，消费者超时时间。当 Broker 在该时间内没有收到消费者的心跳时，认为该消费者故障失败，Broker 发起重新 Rebalance 过程。目前该值的配置必须在 Broker 配置group.min.session.timeout.ms=6000和group.max.session.timeout.ms=300000 之间
session.timeout.ms=10000

# 使用 Kafka 消费分组机制时，消费者发送心跳的间隔。这个值必须小于 session.timeout.ms，一般小于它的三分之一
heartbeat.interval.ms=3000

# 使用 Kafka 消费分组机制时，再次调用 poll 允许的最大间隔。如果在该时间内没有再次调用 poll，则认为该消费者已经失败，Broker 会重新发起 Rebalance 把分配给它的 partition 分配给其他消费者
max.poll.interval.ms=300000
```

如果出现一个消费者订阅了很多的 Topic，您可以尝试减少 Group 订阅 Topic 的数量。
