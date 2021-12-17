
本文将分别通过生产端、服务端（CKafka）和消费端介绍影响消息队列 CKafka 可靠性的因素，并提供对应的解决方法。

### 生产端数据丢失如何处理？

#### 数据丢失原因

生产者将数据发送到消息队列 CKafka 时，数据可能因为网络抖动而丢失，此时消息队列 CKafka 未收到该数据。可能情况：

- 网络负载高或者磁盘繁忙时，生产者又没有重试机制。
- 磁盘超过购买规格的限制，例如实例磁盘规格为9000GB，在磁盘写满后未及时扩容，会导致数据无法写入到消息队列 CKafka。
- 突发或持续增长峰值流量超过购买规格的限制，例如实例峰值吞吐规格为100MB/s，在长时间峰值吞吐超过限制后未及时扩容，会导致数据写入消息队列 CKafka 变慢，生产者有排队超时机制时，导致数据无法写入到消息队列 CKafka。

#### 解决方法

- 生产者对自己重要的数据，开启失败重试机制。
- 针对磁盘使用，在配置实例时设置好监控和 [告警策略](https://console.cloud.tencent.com/monitor/policylist/create) ，可以做到事先预防。
  遇到磁盘写满时，可以在控制台及时升配（消息队列 CKafka 非独占实例间升配为平滑升配不停机且也可以单独升配磁盘）或者通过修改消息保留时间降低磁盘存储。
- 为了尽可能减少生产端消息丢失，您可以通过 buffer.memory 和 batch.size（以字节为单位）调优缓冲区的大小。缓冲区并非越大越好，如果由于某种原因生产者宕机了，那么缓冲区存在的数据越多，需要回收的垃圾越多，恢复就会越慢。应该**时刻注意生产者的生产消息数情况、平均消息大小**等（消息队列 CKafka 监控中有丰富的监控指标）。
- 配置生产端 ACK
  当 producer 向 leader 发送数据时，可以通过 request.required.acks 参数以及 min.insync.replicas 设置数据可靠性的级别。
 - 当 acks = 1时（默认值），生产者在 ISR 中的 leader 已成功收到数据可以继续发送下一条数据。如果 leader 宕机，由于数据可能还未来得及同步给其 follower，则会丢失数据。
 - 当 acks = 0时，生产者不等待来自 broker 的确认就发送下一条消息。这种情况下数据传输效率最高，但数据可靠性确最低。
 - 当 acks = -1或者 all 时，生产者需要等待 ISR 中的所有 follower 都确认接收到消息后才能发送下一条消息，可靠性最高。
   即使按照上述配置 ACK，也不能保证数据不丢，例如，当 ISR 中只有 leader 时（ISR 中的成员由于某些情况会增加也会减少，最少时只剩一个 leader），此时会变成 acks = 1的情况。所以需要同时在配合 min.insync.replicas 参数（此参数可以在消息队列 CKafka 控制台 Topic 配置开启高级配置中进行配置），min.insync.replicas 表示在 ISR 中最小副本的个数，默认值是1，当且仅当 acks = -1或者 all 时生效。

#### 建议配置的参数值

此参数值仅供参考，实际数值需要依业务实际情况而定。

 - 重试机制：`message.send.max.retries=3;retry.backoff.ms=10000;`
 - 高可靠的保证：`request.required.acks=-1;min.insync.replicas=2;`
 - 高性能的保证：`request.required.acks=0;`
 - 可靠性+性能：`request.required.acks=1;`

### 服务端（CKafka）数据丢失如何处理？

#### 数据丢失原因

- partition 的 leader 在未完成副本数 followers 的备份时就宕机，即使选举出了新的 leader 但是数据因为未来得及备份就丢失。
- 开源 Kafka 的落盘机制为异步落盘，也就是数据是先存在 PageCache 中的，当还没有正式落盘时，broker 出现断开连接或者重启或者故障时，PageCache 上的数据由于没有来及落磁盘进而丢失。
- 磁盘故障导致已经落盘的数据丢失。

#### 解决方法

- 开源 Kafka 是多副本的，官方推荐通过副本来保证数据的完整性，此时如果是多副本，同时出现多副本多 broker 同时挂掉才会丢数据，比单副本数据的可靠性高很多，所以消息队列 CKafka 强制 Topic 是双副本，可配置3副本。
- 消息队列 CKafka 服务配置了更合理的参数 log.flush.interval.messages 和 log.flush.interval.ms，对数据进行刷盘。
- 消息队列 CKafka 对磁盘做了特殊处理，保证部分磁盘损坏时也不会影响数据的可靠性。

#### 建议配置的参数值

非同步状态的副本可以选举为 leader：`unclean.leader.election.enable=false // 关闭`

### 消费端数据丢失如何处理？

#### 数据丢失原因

- 还未真正消费到数据就提交 commit 了 offset，若过程中消费者挂掉，但 offset 已经刷新，消费者错过了一条数据，需要消费分组重新设置 offset 才能找回数据。
- 消费速度和生产速度相差太久，而消息保存时间太短，导致消息还未及时消费就被过期删除。

#### 解决方法

- 合理配置参数 auto.commit.enable，等于 true 时表示自动提交。建议使用定时提交，避免频繁 commit offset。
- 监控消费者的情况，正确调整数据的保留时间。监控当前消费 offset 以及未消费的消息条数，并配置告警，防止由于消费速度过慢导致消息过期删除。

### 数据丢失排查方案

#### 在本地打印分区 partition 和偏移量 offset 进行排查

打印信息代码如下：

```java
Future<RecordMetadata> future = producer.send(new ProducerRecord<>(topic, messageKey, messageStr));
RecordMetadata recordMetadata = future.get();
log.info("partition: {}", recordMetadata.partition());
log.info("offset: {}", recordMetadata.offset());
```

- 如果能够打印出 partition 和 offset，则表示当前发送的消息在服务端已经被正确保存。此时可以通过消息查询的工具去查询相关位点的消息即可。
- 如果打印不出 partition 和 offset，则表示消息没有被服务端保存，客户端需要重试。

