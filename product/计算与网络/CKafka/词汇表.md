### Broker
Broker 是一个单独的 CKafka server。Broker 主要用来接收生产者发送的消息、分配 Offset、并将消息保存到磁盘中；同时，Broker 也接收来自消费者、其他 Broker 的请求，根据请求类型进行相应处理并返回响应。

### 分区
分区（Partition）是用于存储消息的物理概念。每个 Topic 可以划分成多个分区，且每个 Topic 至少有一个分区，同一 Topic 下的不同分区包含不同的消息。同一 Topic 的不同分区会分配给不同的 Broker。分区是 CKafka 水平扩展性能的基础，我们可以通过增加服务器，并在服务器上分配分区的方式，增加 CKafka 的并行处理能力。

### 副本
副本（Replica）是消息的冗余备份，以保证服务的高可用，每个分区可以有多个副本，每个副本包含的消息是一样的（在同一时刻，副本之间并不完全一样，这依赖同步机制）。在 CKafka 中每个分区至少有双副本，保障服务的高可用。

### Offset 
Offset 是消息在分区（Partition）的唯一序号。

### 生产者
生产者（Producer）是用来生产消息，并将消息按照一定规则推送到 Topic 的分区。

### 实例
实例（Instance）是购买 CKafka 的单位。按照峰值吞吐量（MB/s）、磁盘容量（GB）的不同，将实例分为不同规格。购买不同规格的实例，以保证 CKafka 的高可靠和高可用，默认购买的是高可用的集群服务，服务中包含多个 Broker 服务器，且客户无需关心硬件设备。

### 私有网络
[私有网络（Virtual Private Cloud）](https://cloud.tencent.com/document/product/215) 在腾讯云构建出独立的网络空间，与您在数据中心运行的传统网络极其相似，但是托管在腾讯云私有网络内的是您在腾讯云上的服务资源，包括：云服务器、负载均衡、云数据库等云服务资源。您不用关心网络设备的采购和运维，我们通过软件自定义网段划分、IP 地址、路由策略等。您不仅可以通过弹性 IP 、NAT 网关和公网网关等灵活访问 Internet，也可以通过 VPN / 专线接入将私有网络与您的数据中心连通。

### 消费者
消费者（Consumer）是从 Topic 中拉取消息，并对消息进行消费的服务。消费者将自行维护其消费到 Partition 的 offset 的相关信息。

### 消费者分组
消费者分组（Consumer Group）是消费者的集合，在 CKafka 中，多个 Consumer 可以组成一个 Consumer Group，且一个 Consumer 只能属于一个 Consumer Group。Consumer Group 保证其订阅 Topic 的每个分区只被分配给该 Consumer Group 中的一个 Consumer 处理。
建议您在消费时指定消费分组 ID，若不指定， CKafka 系统会随机生成一个消费分组，但是容易触发实例创建消费分组的个数上限，具体限制可参考 [CKafka 计费说明](https://cloud.tencent.com/document/product/597/11745)。

### 主题
主题（Topic）是用于存储消息的逻辑概念，可以看做一个消息集合。每个 Topic 可以有多个生产者向其中推送（push）消息，也可以有任意多个消费者消费其中的消息。

### ZooKeeper	
ZooKeeper	是一个为分布式应用提供一致性服务的软件，提供的功能包括：配置维护、域名服务、分布式同步、组服务等。在消息队列 CKafka 中，ZooKeeper 主要用于存储集群的元数据（MetaData）、进行 Leader 选举、故障容错等。
