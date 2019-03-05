
### Cloud Kafka兼容哪一版的开源Kafka？
目前CKafka服务可以完美兼容0.9及以上版本的开源Kafka api，实现用户零成本上云。

### 什么是主题（TOPIC）？
Topic是每条发布到 Cloud Kafka 集群的消息所属的类别，即 Cloud Kafka 是面向 topic 的。用户需要先创建topic 然后才能读写。

### 什么是分区（PARTITION）？
Partition 是物理上的概念，每个 topic 会被分成一个或多个 partition。partition可以用来水平扩展topic的吞吐，发布的消息将被写入不同partition，并被若干消费者同时读取。由于Cloud Kafka 分配的单位是 partition，因此在本质上，topic的并行吞吐量和partition个数成正比。

### Cloud Kafka和CMQ有什么区别？
CMQ提供金融级的高可靠、高数据持久性消息传输，保证数据强一致性。
Cloud Kafka适用于要求更高吞吐率，对可靠性要求相对较低的场景（如日志聚合等业务）。此外，Cloud Kafka完美兼容kafka的老用户，可以做到零迁移成本，实例完全独占。

### Kafka客户端是否可以直接连接Cloud Kafka服务？
Cloud Kafka可以兼容0.9及以上版本的开源Kafka，您可以通过Kafka客户端连接消息中心，并且把代码部署在腾讯云服务中生产或消费消息。

### Cloud Kafka如何保证安全性？
Cloud Kafka通过如下安全特性确保安全性：

租户隔离：实例的网络访问在账户间天然隔离。
权限控制：Cloud Kafka额外应用层上做了来源ip白名单的鉴权机制。
安全防护：提供多纬度的安全防护、防 DDoS 攻击等服务；
