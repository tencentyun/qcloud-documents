### Cloud Kafka 兼容哪一版的开源 Kafka？
目前 CKafka 服务可以完美兼容 0.9 0.10 版本的开源 Kafka api，实现用户零成本上云。

### CKafka的产品限制有哪些？
根据实例的不同规格，有如下限制：

| 产品规格 | 实例级别topic数 | 实例级别partition数 | 实例级别consumer group数 | 单topic支持的partition数   |
| :-------- | :-------- | :------ |:------ |:------ |
| 入门型 |   25 |  60 | 20 | 8 |
| 标准型 |   40 |  100 | 30 | 20 |
| 进阶型 |   50 |  150 | 50 | 20 |
| 容量型 |  150 |  300 | 100 | 30 |
| 高io型 |  150 |  300 | 100 | 30 |
| 高阶型 |   250 |  500 | 300 | 50 |
| 独享型 |   1000 |  1500 | 500 | 100 |

> 注：实例级别的paritition限制包含了副本数。举例，一个实例下有1个双副本、4分区的topic，还有2个3副本，3分区的topic，则这个实例的总partition个数为(1×2×4)+(2×3×3)=26个。

> consumer group 空闲存活时间 1 个月

### Cloud Kafka 是否支持消息压缩？
当前Cloud Kafka支持开源的snappy和lz4的消息压缩格式。由于Gzip压缩对于CPU的消耗较高，暂未支持。
测试期间建议客户关闭消息压缩参数进行测试。

### Cloud Kafka 是否支持公网访问？
当前Cloud Kafka默认内网传输，由于公网访问会涉及延时、网络环境和安全性等问题，不建议客户长期开启公网传输。
如果有临时公网传输需求建议联系客户经理评估。

### Cloud Kafka 是否支持自动创建 topic（auto.create.topic）？
当前 Cloud Kafka 未开放自动创建 topic 的开源接口，建议客户通过标准的 API 接口 [CreateTopic](https://cloud.tencent.com/document/product/597/10096) 创建 topic。

### 什么是主题（TOPIC）？
Topic 是每条发布到 Cloud Kafka 集群的消息所属的类别，即 Cloud Kafka 是面向 topic 的。用户需要先创建 topic 然后才能读写。

### 什么是分区（PARTITION）？
Partition 是物理上的概念，每个 topic 会被分成一个或多个 partition。partition 可以用来水平扩展 topic 的吞吐，发布的消息将被写入不同 partition，并被若干消费者同时读取。由于 Cloud Kafka 分配的单位是 partition，因此在本质上，topic 的并行吞吐量和 partition 个数成正比。

### Cloud Kafka 和 CMQ 有什么区别？
CMQ 提供金融级的高可靠、高数据持久性消息传输，保证数据强一致性。
Cloud Kafka 适用于要求更高吞吐率，对可靠性要求相对较低的场景（如日志聚合等业务）。此外，Cloud Kafka 完美兼容 kafka 的老用户，可以做到零迁移成本，实例完全独占。

### Kafka 客户端是否可以直接连接 Cloud Kafka 服务？
Cloud Kafka 可以兼容 0.9 0.10 版本的开源 Kafka，您可以通过 Kafka 客户端连接消息中心，并且把代码部署在腾讯云服务中生产或消费消息。

### Cloud Kafka 如何保证安全性？
Cloud Kafka 通过如下安全特性确保安全性：

租户隔离：实例的网络访问在账户间天然隔离。
权限控制：Cloud Kafka 额外应用层上做了来源ip白名单的鉴权机制,即将支持SASL鉴权。
安全防护：提供多纬度的安全防护、防 DDoS 攻击等服务；

### CKafka 是否会丢失消息？
- 开源的 Apache Kafka 不保证不丢消息；CKafka 针对可用性做了优化，腾讯云承诺 CKafka 的可用性超 99.95%。
- CKafka 客户可以通过生产时开启 ACK ，尽量保障不丢失和少丢失消息，提升消息可靠性。
- 变更集群或升级过程对客户透明，秒级变更。
- CKafka 面向的使用场景主要是需要高吞吐、高性能的大数据处理场景，对数据可靠性要求不十分苛刻，极端场景下可能会有少量的消息丢失；若需保障完全不丢失消息，且对性能要求不是非常高的场景，推荐使用 CMQ。


