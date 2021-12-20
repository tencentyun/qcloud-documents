消息队列 CKafka 的架构图如下所示：
![](https://mc.qcloudimg.com/static/img/c1094d009fa433ef2598e0deb51dde68/image.png)
- 生产者 Producer 可能是网页活动产生的消息、服务日志等信息。生产者通过 push 模式将消息发布到 Cloud Kafka 的 Broker 集群。
- 集群通过 Zookeeper 管理集群配置，进行 leader 选举，故障容错等。
- 消费者 Consumer 被划分为若干个 Consumer Group。消费者通过 pull 模式从 Broker 中消费消息。

消息队列 CKafka 相比于自建开源 Apache Kafka 所具备的优势请参考 [产品优势](https://cloud.tencent.com/document/product/597/37142)。

## 高吞吐
消息队列 CKafka 中存在大量的网络数据持久化到磁盘和磁盘文件通过网络发送的过程。这一过程的性能直接影响 Kafka 的整体吞吐量，主要通过以下几点实现：
- **高效使用磁盘**：磁盘中顺序读写数据，提高磁盘利用率。
 - 写 message：消息写到 page cache，由异步线程刷盘。
 - 读 message：消息直接从 page cache 转入 socket 发送出去。
 - 当从 page cache 没有找到相应数据时，此时会产生磁盘 IO，从磁盘加载消息到 page cache，然后直接从 socket 发出去。
- **Broker 的零拷贝（Zero Copy）机制**：使用 sendfile 系统调用，将数据直接从页缓存发送到网络上。 
- **减少网络开销**
 - 数据压缩降低网络负载。
 - 批处理机制：Producer 批量向 Broker 写数据、Consumer 批量从 Broker 拉数据。

## 数据持久化
消息队列 CKafka 的数据持久化主要通过如下原理实现：
- **Topic 中 Partition 存储分布**
   在消息队列 CKafka 文件存储中，同一 Topic 有多个不同 Partition，每个 Partition 在物理上对应一个文件夹，用户存储该 Partition 中的消息和索引文件。例如，创建两个 Topic，Topic1 中存在5个 Partition，Topic2 中存在10个 Partition，则整个集群上会相应生成5 + 10 = 15个文件夹。
   
- **Partition 中文件存储方式**
   Partition 物理上由多个 segment 组成，每个 segment 大小相等，顺序读写，快速删除过期 segment, 提高磁盘利用率。
   
## 水平扩展（Scale Out） 
- 一个 Topic 可包含多个 Partition，分布在一个或多个 Broker 上。
- 一个消费者可订阅其中一个或者多个 Partition。
- Producer 负责将消息均衡分配到对应的 Partition。
- Partition 内消息是有序的。 

## 消费者分组（Consumer Group）
- 消息队列 CKafka 不删除已消费的消息。
- 任何 Consumer 必须属于一个 Group。
- 同一 Consumer Group 中的多个 Consumer 不同时消费同一个 Partition。
- 不同 Group 同时消费同一条消息，多元化（队列模式、发布订阅模式）。

## 多副本
多副本设计可增强系统可用性、可靠性。
Replica 均匀分布到整个集群，Replica 的算法如下：
1. 将所有 Broker（假设共 n 个 Broker）和待分配的 Partition 排序。
2. 将第 i 个 Partition 分配到第（i mod n）个 Broker 上。
3. 将第 i 个 Partition 的第 j 个 Replica 分配到第（(i + j) mod n）个 Broker 上。

## Leader Election 选举机制
消息队列 CKafka 在 ZooKeeper 中动态维护了一个 ISR（in-sync replicas），ISR 里的所有 Replica 都跟上了 Leader。只有 ISR 里的成员才有被选为 Leader 的可能。
- 假设 ISR 中 f + 1个 Replica，一个 Partition 能在保证不丢失已 commit 的消息的前提下
容忍 f 个 Replica 的失败。
- 假设共有 2f + 1个 Replica（包含 Leader 和 Follower），commit 之前必须保证有 f + 1个
 Replica 复制完消息，为了保证正确选出新的 Leader，fail 的 Replica 不能超过 f 个。
