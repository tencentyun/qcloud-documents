## 现象描述
服务端（CKafka）数据丢失，导致无法正常消费。


## 可能原因
- partition 的 leader 在未完成副本数 followers 的备份时就宕机，即使选举出了新的 leader 但是数据因为未来得及备份就丢失。
- 开源 Kafka 的落盘机制为异步落盘，也就是数据是先存在 PageCache 中的，当还没有正式落盘时，broker 出现断点或者重启或者故障时，PageCache 上的数据由于没有来及落磁盘进而丢失。
- 磁盘故障导致已经落盘的数据丢失。

## 解决方法
现有的技术无法保证数据100%不丢失，您可以通过一些配置参数最大可能保证数据高可靠。
- 开源 Kafka 是多副本的，官方推荐通过副本来保证数据的完整性，此时如果是多副本，同时出现多副本多 broker 同时挂掉才会丢数据，比单副本数据的可靠性高很多，所以消息队列 CKafka 强制 Topic 是双副本，可配置3副本。
- 消息队列 CKafka 服务配置了更合理的参数 log.flush.interval.messages 和 log.flush.interval.ms，对数据进行刷盘。
- 消息队列 CKafka 对磁盘做了特殊处理，保证部分磁盘损坏时也不会影响数据的可靠性。

## 建议配置的参数值
非同步状态的副本可以选举为 leader：`unclean.leader.election.enable=false // 关闭`
