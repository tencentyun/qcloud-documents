### Cloud Kafka 兼容哪一版的开源 Kafka？当前的 CKafka 是基于开源 Kafka 的哪个版本？
目前 CKafka 服务可以完美兼容 0.9 0.10 版本的开源 Kafka API，实现用户零成本上云。
**当前 CKafka 基于 Apache Kafka 0.10 版本，推荐生产消费端选取 0.10 版本的 SDK。**

### Cloud Kafka 的产品限制有哪些？

1. 根据实例的不同规格，有如下限制：

| 产品规格 | 实例级别 topic 数 | 实例级别 partition 数 | 实例级别 consumer group 数 | 单 topic 支持的 partition 数   |
| :-------- | :-------- | :------ |:------ |:------ |
| 入门型 |   25 |  60 | 20 | 8 |
| 标准型 |   40 |  100 | 30 | 20 |
| 进阶型 |   50 |  150 | 50 | 20 |
| 容量型 |  150 |  300 | 100 | 30 |
| 高io型 |  150 |  300 | 100 | 30 |
| 高阶型 |   250 |  500 | 300 | 50 |
| 专享型 |   1000+ |  1500+ | 500+ | 100+ |

>**注意：**
>实例级别的 paritition 限制包含了副本数。举例，一个实例下有 1 个双副本、4 分区的 topic，还有 2 个 3 副本，3 分区的 topic，则这个实例的总 partition 个数为 (1×2×4)+(2×3×3)=26 个。
2.  consumer group 空闲存活时间 1 个月
3.  CKafka单条消息大小（message.max.bytes）限制为1M 

### 生产消费者是否只需配置 vip:port？
--bootstrap-server 参数中填写 CKafka 实例的 vip:port 即可,新购 CKafka 实例后，默认通过 9092 端口接入，但 9093-9095 端口也可通。
主要原因在于，CKafka VIP 封装了后端节点的 broker IP，并通过 9092 端口负载均衡到 9093-9095 端口，因此接入时仅需配置 CKafka 实例的 vip:port。

### Cloud Kafka 是否支持消息压缩？
当前 Cloud Kafka 支持开源的 snappy 和 lz4 的消息压缩格式。由于 Gzip 压缩对于 CPU 的消耗较高，暂未支持。
测试期间建议客户关闭消息压缩参数进行测试。

配置开启方法：Producer 的配置文件中参数 compression.type = snappy 或者 lz4，默认为关闭 none。

### Cloud Kafka 消息保留时间配置为 1min，是否会在 1min 后立即删除堆积消息？
不一定。消息删除不仅和保留时间配置有关，也和生产消息的数据量级有关。
CKafka 删除堆积消息的最小单位是 partition 级别的文件分片，当前文件分片大小为 1GB，堆积不达到一个文件分片是不会删除的。如果有 10 partition，在 1 分钟内如果没有达到 10GB 的量，就不会有文件滚动，也就不会删除。

### Cloud Kafka 是否支持公网访问？
当前 Cloud Kafka 默认内网传输，由于公网访问会涉及延时、网络环境和安全性等问题，不建议客户长期开启公网传输。
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
权限控制：Cloud Kafka 额外应用层上做了来源 IP 白名单的鉴权机制,即将支持SASL鉴权。
安全防护：提供多纬度的安全防护、防 DDoS 攻击等服务；

### CKafka 副本数怎样选取？

强烈建议 topic 创建时选择双副本或三副本存储数据，保障数据可靠性。当前 CKafka 已经禁止单副本 topic 的创建，如您账户下有单副本的 topic，建议按如下步骤迁移：
1. 创建新的 topic，选择相同的分区，选取双副本；
2. 生产消息到新的 topic 中，存量的单副本 topic 继续被消费；
3. 消费完毕后修改消费者配置，订阅新的 topic 进行消费。

### CKafka 是否会丢失消息？
- 开源的 Apache Kafka 不保证不丢消息；CKafka 针对可用性做了优化，腾讯云承诺 CKafka 的可用性超 99.95%。
- CKafka 客户可以通过生产时开启 ACK ，尽量保障不丢失和少丢失消息，提升消息可靠性。
- 变更集群或升级过程对客户透明，秒级变更。
- CKafka 面向的使用场景主要是需要高吞吐、高性能的大数据处理场景，对数据可靠性要求不十分苛刻，极端场景下可能会有少量的消息丢失；若需保障完全不丢失消息，且对性能要求不是非常高的场景，推荐使用 CMQ。

### CKafka 消息堆积了很多如何处理？
CKafka 跟开源的 Kafka 是一模一样的机制和原理。您可以通过以下步骤来排错：
1. 确定下您的业务有几个消费者在消费； 
2. 若消费者消费能力比较差，直接加消费者即可；
3. 消费者已经到最高设置（>=您的分区数），建议您再提高主题分区数，可以提交工单申请开同白名单，我们后台审核帮忙提高分区个数。

