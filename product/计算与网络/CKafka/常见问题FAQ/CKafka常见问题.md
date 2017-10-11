
### Cloud Kafka 兼容哪一版的开源 Kafka？
目前 CKafka 服务可以完美兼容 0.9及以上版本的开源 Kafka api，实现用户零成本上云。

### 什么是主题（TOPIC）？
Topic 是每条发布到 Cloud Kafka 集群的消息所属的类别，即 Cloud Kafka 是面向 topic 的。用户需要先创建 topic 然后才能读写。

### 什么是分区（PARTITION）？
Partition 是物理上的概念，每个 topic 会被分成一个或多个 partition。partition 可以用来水平扩展 topic 的吞吐，发布的消息将被写入不同 partition，并被若干消费者同时读取。由于 Cloud Kafka 分配的单位是 partition，因此在本质上，topic 的并行吞吐量和 partition 个数成正比。

### Cloud Kafka 和 CMQ 有什么区别？
CMQ 提供金融级的高可靠、高数据持久性消息传输，保证数据强一致性。
Cloud Kafka 适用于要求更高吞吐率，对可靠性要求相对较低的场景（如日志聚合等业务）。此外，Cloud Kafka 完美兼容 kafka 的老用户，可以做到零迁移成本，实例完全独占。

### Kafka 客户端是否可以直接连接 Cloud Kafka 服务？
Cloud Kafka 可以兼容 0.9及以上版本的开源 Kafka，您可以通过 Kafka 客户端连接消息中心，并且把代码部署在腾讯云服务中生产或消费消息。

### Cloud Kafka 如何保证安全性？
Cloud Kafka 通过如下安全特性确保安全性：

租户隔离：实例的网络访问在账户间天然隔离。
权限控制：Cloud Kafka 额外应用层上做了来源ip白名单的鉴权机制。
安全防护：提供多纬度的安全防护、防 DDoS 攻击等服务；

### CKafka 是否会丢失消息？
1. 开源的 Apache Kafka 不保证不丢消息；CKafka 针对可用性做了优化，腾讯云承诺 CKafka 的可用性超 99.95%。
2. CKafka 客户可以通过生产时开启 ACK ，尽量保障不丢失和少丢失消息，提升消息可靠性。
3. 变更集群或升级过程对客户透明，秒级变更。
4. CKafka 面向的使用场景主要是需要高吞吐、高性能的大数据处理场景，对数据可靠性要求不十分苛刻，极端场景下可能会有少量的消息丢失；若需保障完全不丢失消息，且对性能要求不是非常高的场景，推荐使用 CMQ。

### CKafka的产品限制有哪些？
产品形态限制：
1. 每个实例最多可以创建 50个 partition、20个 group。
2. 每个 topic 当前最多可以创建 8个 partition、3个副本。
3. consumer group 空闲存活时间 1个月
