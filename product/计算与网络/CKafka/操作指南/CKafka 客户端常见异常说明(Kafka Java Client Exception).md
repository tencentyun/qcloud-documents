# Kafka Java Client Exception

1. 以下异常属于客户端配置或服务异常，客户端不会自动重试
| Exception | Description |
| ------ | ------ |
| UnknownServerException | 服务器处理请求发生未知错误。老版本流控会返回这个错误；新版本则可能是服务器出现BUG导致。 |
| RecordTooLargeException | 消息太大。目前配置message.max.bytes=1000012。 |
| InvalidRequiredAcksException | 生产者配置的acks参数不合法。 |
| InconsistentGroupProtocolException | Group的协议不一致。检查Consumer和Connector是否配置了相同的group.id，这两者使用的不同的协议，不能加入相同的组。|
| InvalidGroupIdException | Consumer Group ID不合法，建议使用[a-zA-Z0-9._-]这些字符，长度不超过128。 |
| InvalidTopicException | Topic不合法。开启自动创建Topic选项后，客户端使用的Topic不合法会返回这个异常。检查Topic是否使用了不合法的字符或长度是否超过限制。 |
| InvalidSessionTimeoutException | 消费者配置的session.timeout.ms不合法。目前服务器端允许的最小值为：group.min.session.timeout.ms=6000，最大值为：group.max.session.timeout.ms=300000。 |
| InvalidCommitOffsetSizeException | 提交Offset信息太大超过最大消息大小，无法写入__consumer_offsets。目前配置message.max.bytes=1000012。 |
| OffsetMetadataTooLarge | Offset提交请求包含的Metadata太大。服务器配置的offset.metadata.max.bytes=4096。 |
| UnsupportedVersionException | Broker不支持该版本的请求。建议使用0.10.2.x版本的客户端。 |

2. 以下异常在程序正常运行过程中可能会短暂出现，客户端会自动重试。 持续出现则服务不正常。
| Exception | Description |
| ------ | ------ |
| TimeoutException | 请求超时。首次连接报请求超时，先检查地址是否正确，telnet确定网络能够联通。程序运行中偶尔抛出此异常可能属于网络抖动。 |
| CorruptRecordException | 消息不合法。可能CRC检查不通过，数据大小不合法。此外，如果压缩方式使用**GZip**或0.9以下版本**使用压缩**也会导致这个错误。 |
| UnknownTopicOrPartitionException | Topic或Partition不存在。到控制台检查是否已经创建对应的Topic。注意：客户端通过TopicName生产消费，而不是TopicId。此外，客户端没有权限访问Topic时也会报Topic不存在。 |
| LeaderNotAvailableException | Partition没有Leader。当Topic刚创建时服务器还未选出合适的Leader，此时会返回此错误给客户端，客户端会自动重试获取Leader信息。注：旧版本才会有这个异常，0.10.2.1已经去掉。 |
| NotLeaderForPartitionException | Partition的Leader不可用。由于客户端会缓存Topic的Metadata，所以当Partition的Leader切换时，生产或消费请求可能仍然发送到旧Leader上，此时会返回此错误给客户端，客户端会自动更新Metadata信息。 |
| NetworkException | 客户端连接被服务器端关闭。网络异常或连接数超过限制。 |
| NotEnoughReplicasException | ISR数量不够。在写入数据时Partition的ISR数量小于Topic配置的min.insync.replicas，可能由于ISR抖动导致。 |
| NotEnoughReplicasAfterAppendException | 数据写入Broker本地后，发生ISR抖动导致无法满足min.insync.replicas。 |

3. 以下异常在日志配置为DEBUG级别会出现，客户端会自动处理。 
| Exception | Description |
| ------ | ------ |
| OffsetOutOfRangeException | 消费者拉取消息时传入的Offset超出范围。如果客户端设置了Offset重置策略（earliest或latest），则客户端会根据策略进行Offset重置，否则需要用户程序处理这个异常 |
| GroupLoadInProgressException | ConsumerGroup对应的Coordinator正在加载。服务器端升级时可能短暂出现，客户端会自动重试。 |
| GroupCoordinatorNotAvailableException | Coordinator不可用。服务器端升级时可能短暂出现，客户端会自动重试。 |
| NotCoordinatorForGroupException | 当前节点不是该ConsumerGroup的Coordinator，Coordinator迁移到别的节点。服务器端升级时可能短暂出现，客户端会自动重试。 |
| IllegalGenerationException | ConsumerGroup的generation不合法。可能心跳超时或有新消费者加入，Consumer会自动重新尝试加入ConsumerGroup。 |
| RebalanceInProgressException | ConsumerGroup正在进行rebalance。可能心跳超时或有新消费者加入，Consumer会自动重新尝试加入ConsumerGroup。 |
