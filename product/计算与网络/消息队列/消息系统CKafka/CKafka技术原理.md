## 技术原理
Cloud Kafka的架构图如下所示：
![](https://mc.qcloudimg.com/static/img/c1094d009fa433ef2598e0deb51dde68/image.png)
一个典型的Cloud Kafka集群如上所示。其中的生产者Producer可能是网页活动产生的消息、或是服务日志等信息。生产者通过push模式将消息发布到Cloud Kafka的Broker集群，消费者通过pull模式从broker中消费消息。消费者Consumer被划分为若干个Consumer Group，此外，集群通过Zookeeper管理集群配置，进行leader选举，故障容错等。

### 高吞吐的实现
Cloud Kafka中存在大量的网络数据持久化到磁盘和磁盘文件通过网络发送的过程。这一过程的性能直接影响Kafka的整体吞吐量，主要通过以下几点实现。

1. 高效使用磁盘
- 磁盘中顺序读写数据，提高磁盘利用率
**写message**
消息写到page cache，由异步线程刷盘
**读message**
消息直接从page cache转入socket发送出去
当从page cache没有找到相应数据时，此时会产生磁盘IO,从磁盘加载消息到page cache,然后直接从socket发出去
2. Broker的零拷贝(Zero Copy)机制
     使用sendfile系统调用，将数据直接从页缓存发送到网络上
3. 减少网络开销
- 数据压缩降低网络负载
- 批处理机制：Producer批量向Broker写数据、Consumer批量从Broker拉数据

### 数据持久化
Cloud Kafka的数据持久化主要通过如下原理实现：
1. topic中partition存储分布
   在Cloud Kafka文件存储中，同一topic有多个不同partition，每个partition在物理上对应一个文件夹，用户存储该partition中的消息和索引文件。例如，创建两个topic，topic1中存在5个partition，topic2中存在10个partition，则整个集群上会相应生成5+10=15个文件夹。
   
2. partition中文件存储方式
   partition物理上由多个segment组成，每个segment大小相等，顺序读写，快速删除过期segment, 提高磁盘利用率。
   
### 水平扩展Scale Out
一个Topic可分多个Partition, 分布在一个或多个Broker上
一个消费者可订阅其中一个或者多个Partition
Producer负责将消息均衡分配到对应的Partition
Partition内消息有序的 

### Consumer Group设计
Cloud Kafka不删除已消费的消息
任何consumer必须属于一个group
同一Consumer Group中的多个Consumer不同时消费同一个partition
不同Group同时消费同一条消息，多元化 (队列模式、发布订阅模式）

### 多副本
为何需要多副本设计？  
 增强系统可用性、可靠性
Replica均匀分布到整个集群
Replica的算法如下：
1、将所有Broker（假设共n个Broker）和待分配的Partition排序
2、将第i个Partition分配到第（i mod n）个Broker上
3、将第i个Partition的第j个Replica分配到第（(i + j) mode n）个Broker上

### Leader Election选举机制

Cloud Kafka在Zookeeper中动态维护了一个ISR（in-sync replicas），
ISR里的所有Replica都跟上了leader
只有ISR里的成员才有被选为Leader的可能。

ISR中f+1个Replica，一个Partition能在保证不丢失已commit的消息的前提下
容忍f个Replica的失败。
共有2f+1个Replica（包含Leader和Follower），commit之前必须保证有f+1个
Replica复制完消息，为了保证正确选出新的Leader，fail的Replica不能超过f个。
