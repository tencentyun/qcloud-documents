
## 客户端配置或服务异常
以下异常属于客户端配置或服务异常，客户端不会自动重试。

| 异常 | 描述 | 分析与说明 |
| ------ | ------ | ------ |
| UnknownServerException | 服务器处理请求发生未知错误。| 老版本流控会返回这个错误；新版本则可能是服务器出现 BUG 导致。 |
| RecordTooLargeException | 消息太大。| 目前配置 message.max.bytes=1000012。 |
| InvalidRequiredAcksException | 生产者配置的 acks 参数不合法。 | - |
| InconsistentGroupProtocolException | Group 的协议不一致。| 检查 Consumer 和 Connector 是否配置了相同的 group.id，这两者使用的不同的协议，不能加入相同的组。|
| InvalidGroupIdException | Consumer Group ID不合法。 | 建议使用 [a-zA-Z0-9._-] 这些字符，长度不超过 128。 |
| InvalidTopicException | Topic 不合法。| 开启自动创建 Topic 选项后，客户端使用的 Topic 不合法会返回这个异常。检查 Topic 是否使用了不合法的字符或长度是否超过限制。 |
| InvalidSessionTimeoutException | 消费者配置的 session.timeout.ms 不合法。| 目前服务器端允许的最小值为：group.min.session.timeout.ms=6000，最大值为：group.max.session.timeout.ms=300000。 |
| InvalidCommitOffsetSizeException | 提交 Offset 信息太大超过最大消息大小，无法写入__consumer_offsets。 | 目前配置 message.max.bytes=1000012。 |
| OffsetMetadataTooLarge | Offset 提交请求包含的 Metadata 太大。| 服务器配置的 offset.metadata.max.bytes=4096。 |
| UnsupportedVersionException | Broker 不支持该版本的请求。| 建议使用 0.10.2.x 版本的客户端。 |

## 程序正常运行时的短暂异常
以下异常在程序正常运行过程中可能会短暂出现，客户端会自动重试。 持续出现则服务不正常。

| 异常 | 描述 | 分析与说明 |
| ------ | ------ | ------ |
| TimeoutException | 请求超时。 | 首次连接报请求超时，先检查地址是否正确，telnet 确定网络能够联通。程序运行中偶尔抛出此异常可能属于网络抖动。 |
| CorruptRecordException | 消息不合法。| 可能 CRC 检查不通过，数据大小不合法。此外，如果压缩方式使用 **GZip** 或 0.9 以下版本 **使用压缩** 也会导致这个错误。 |
| UnknownTopicOrPartitionException | Topic 或 Partition 不存在。| 到控制台检查是否已经创建对应的 Topic。注意：客户端通过TopicName生产消费，而不是TopicId。此外，客户端没有权限访问 Topic 时也会报 Topic 不存在。 |
| LeaderNotAvailableException | Partition 没有 Leader。| 当 Topic 刚创建时服务器还未选出合适的 Leader，此时会返回此错误给客户端，客户端会自动重试获取 Leader信息。**旧版本才会有这个异常，0.10.2.1 已经去掉**。 |
| NotLeaderForPartitionException | Partition 的 Leader 不可用。| 由于客户端会缓存 Topic 的 Metadata，所以当 Partition 的 Leader 切换时，生产或消费请求可能仍然发送到旧 Leader 上，此时会返回此错误给客户端，客户端会自动更新 Metadata 信息。 |
| NetworkException | 客户端连接被服务器端关闭。| 网络异常或连接数超过限制。 |
| NotEnoughReplicasException | ISR 数量不够。| 在写入数据时 Partition 的 ISR 数量小于 Topic 配置的 min.insync.replicas，可能由于 ISR 抖动导致。 |
| NotEnoughReplicasAfterAppendException | 数据写入 Broker 本地后，发生 ISR 抖动导致无法满足 min.insync.replicas。 | - | 
| BrokerNotAvailableError |  未找到该分区的 Leader。 | 由于客户端会缓存 Topic 的 Metadata，所以当 Partition 的 Leader 切换时，生产或消费请求可能仍然发送到旧 Leader 上，此时会返回该错误给客户端。客户端会自动更新 Metadata 信息，在 Leader 切换后，新生产的请求发送到老的 Leader 报错应该后会自动调整到新的 Leader 上，理论上不会影响数据写入消费的完整性。 |
| NotLeaderForPartitionError | 未找到该分区的 Leader。  | 由于客户端会缓存 Topic 的 Metadata，所以当 Partition 的 Leader 切换时，生产或消费请求可能仍然发送到旧 Leader 上，此时会返回此错误给客户端，客户端会自动更新 Metadata 信息，在 Leader 切换后，新生产的请求发送到老的 Leader 报错应该后会自动调整到新的 Leader 上，理论上不会影响数据写入消费的完整性。 |

## 日志配置为 DEBUG 级别时异常
以下异常在日志配置为 DEBUG 级别会出现，客户端会自动处理。 

| 异常 | 描述 | 分析与说明 |
| ------ | ------ | ------ |
| OffsetOutOfRangeException | 消费者拉取消息时传入的 Offset 超出范围。| 如果客户端设置了 Offset 重置策略（earliest 或 latest），则客户端会根据策略进行 Offset 重置，否则需要用户程序处理这个异常 |
| GroupLoadInProgressException | ConsumerGroup 对应的 Coordinator正在加载。| 服务器端升级时可能短暂出现，客户端会自动重试。 |
| GroupCoordinatorNotAvailableException | Coordinator 不可用。| 服务器端升级时可能短暂出现，客户端会自动重试。 |
| NotCoordinatorForGroupException | 当前节点不是该 ConsumerGroup的Coordinator，Coordinator 迁移到别的节点。| 服务器端升级时可能短暂出现，客户端会自动重试。 |
| IllegalGenerationException | ConsumerGroup 的 generation不合法。| 可能心跳超时或有新消费者加入，Consumer 会自动重新尝试加入 ConsumerGroup。 |
| RebalanceInProgressException | ConsumerGroup 正在进行 rebalance。| 可能心跳超时或有新消费者加入，Consumer 会自动重新尝试加入 ConsumerGroup。 |


