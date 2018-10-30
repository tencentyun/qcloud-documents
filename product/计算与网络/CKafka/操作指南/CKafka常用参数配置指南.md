## CKafka常用参数配置指南

### 1. broker配置参数说明

当前CKafka broker端的一些配置如下，供参考：
```
# 消息体的最大大小，单位是字节
message.max.bytes=1000012

# 是否允许自动创建topic, 默认是false，当前可以通过控制台或云API创建。 
auto.create.topics.enable=false

# 是否允许调用接口删除Topic
delete.topic.enable=true

# Broker允许的最大请求大小为16MB 
socket.request.max.bytes=16777216

# 每个IP与Broker最多建立5000个连接
max.connections.per.ip=5000

# offset保留时间，默认为7天
offsets.retention.minutes=10080

# 没有ACL设置时，允许任何人访问
allow.everyone.if.no.acl.found=true

# 日志分片大小为1G
log.segment.bytes=1073741824

# 日志滚动检查间隔5分钟，当设置保留时间小于5分钟时，也可能需要等待五分钟才会清空日志
log.retention.check.interval.ms=300000
```
注：其他未列出的Broker配置参考[开源Kafka默认配置](http://kafka.apache.org/0102/documentation.html#brokerconfigs)

### 2. Topic配置参数说明
#### 2.1 选取合适的分区数量

从生产者的角度来看，向不同的partition写入是完全并行的；从消费者的角度来看，并发数完全取决于partition的数量（如果consumer数量大于partition数量，则必有consumer闲置）。因此选取合适的分区数量对于发挥CKafka实例的性能十分重要。

partition的数量需要根据生产和消费的吞吐来判断。理想情况下，可以通过如下公式来判断分区的数目。

> **Num =  max( T/PT , T/CT ) = T / min( PT ,  CT )**
> 
> 其中，Num代表partition数量，T代表目标吞吐量，PT代表生产者写入单个partition的最大吞吐，CT代表消费者从单个partition消费的最大吞吐。则partition数量应该等于T/PT和T/CT中较大的那一个。

在实际情况中，生产者写入但partition的最大吞吐PT的影响因素和批处理的规模、压缩算法、确认机制、副本数等有关。消费者从单个partition消费的最大吞吐CT的影响因素和业务逻辑有关，需要在不同场景下实测得出。

**通常建议partition的数量一定要大于等于消费者的数量来实现最大并发。 如果消费者数量是5，则partition的数目也应该是>=5的。**同时，过多的分区会导致生产吞吐的降低和选举耗时的增加，因此也不建议过多分区。提供如下信息供参考：

a、单个partition是可以实现消息的顺序写入的。
b、单个partition只能被同消费者组的单个消费者进程消费。
c、单个消费者进程可同时消费多个partition，即partition限制了消费端的并发能力。
d、partition越多则失败选举的耗时越长。
e、offset的粒度最细是在partition级别的，partition越多，查询offset就越耗时。
f、partition的数量是可以动态增加的，只能增加不能减少。但增加会出现消息rebalance的情况。

#### 2.2 选取合适的副本

目前为了保证可用性副本数必须大于等于2。

#### 2.3 日志保留时间

Topic的log.retention.ms配置通过控制台实例的保留时间统一设置。

#### 2.4 其他Topic级别配置
```
# Topic级别最大消息大小
max.message.bytes=1000012

# 0.10.2版本消息格式为V1格式
message.format.version=0.10.2-IV0

# 不在ISR中的replica允许选择为Leader，可用性高于可靠性，存在数据丢失风险。
unclean.leader.election.enable=true

# ISR提交生产者请求的最小副本数。如果同步状态的副本数小于该值，服务器将不再接受request.required.acks为-1或all的写入请求。
min.insync.replicas=1

```

### 3. 生产者配置指南

生产端常用参数配置如下，建议客户根据实际业务场景调整配置：

```
# 生产者会尝试将业务发送到相同的Partition的消息合包发送到Broker，batch.size设置合包的大小上限。默认为16K。batch.size设太小会导致吞吐下降，设太大会导致内存使用过多。
batch.size=16384

# Kafka producer的ack有3种机制，分别说明如下：
# -1或all：Broker在leader收到数据并同步给所有ISR中的follower后，才应答给Producer继续发送下一条（批）消息。 这种配置提供了最高的数据可靠性，只要有一个已同步的副本存活就不会有消息丢失。注意：这种配置不能确保所有的副本读写入该数据才返回，可以配合Topic级别参数min.insync.replicas使用。
# 0：生产者不等待来自broker同步完成的确认，继续发送下一条（批）消息。这种配置生产性能最高，但数据可靠性最低（当服务器故障时可能会有数据丢失，如果leader已死但是producer不知情，则broker收不到消息）
# 1：生产者在leader已成功收到的数据并得到确认后再发送下一条（批）消息。这种配置是在生产吞吐和数据可靠性之间的权衡（如果leader已死但是尚未复制，则消息可能丢失）
# 用户不显示配置时，默认值为1。用户根据自己的业务情况进行设置。
acks=1

# 控制生产请求在Broker等待副本同步满足acks设置的条件所等待的最大时间
timeout.ms=30000

# 配置生产者用来缓存消息等待发送到Broker的内存。用户要根据生产者所在进程的内存总大小调节。
buffer.memory=33554432

# 当生产消息的速度比Sender线程发送到Broker速度快，导致buffer.memory配置的内存用完时会阻塞生产者send操作，该参数设置最大的阻塞时间
max.block.ms=60000

# 客户端在每个连接上最多可发送的最大的未确认请求数，该参数大于1且retries大于0时可能导致数据乱序
max.in.flight.requests.per.connection=5

# 设置消息延迟发送的时间，这样可以等待更多的消息组成batch发送。默认为0表示立即发送。当待发送的消息达到batch.size设置的大小时，不管是否达到linger.ms设置的时间，请求也会立即发送
linger.ms=0

# 生产者能够发送的请求包大小上限，默认为1M。在修改该值时注意不能超过Broker配置的包大小上限16M
max.request.size=1048576

# 压缩格式配置，目前0.9(包含)以下版本不允许使用压缩，0.10（包含）以上不允许使用GZip压缩
compression.type=[none, snappy, lz4]

# 客户端发送给Broker的请求的超时时间，不能小于Broker配置的replica.lag.time.max.ms，目前该值为10000ms
request.timeout.ms=30000

# 请求发生错误时重试次数，当retries大于0且max.in.flight.requests.per.connection大于1时可能会导致乱序。建议客户将该值改成大于0，既重复发送失败的消息
retries=0

# 发送请求失败时到下一次重试请求之间的时间
retry.backoff.ms=100

```

### 4. 消费者配置指南

生产端常用参数配置如下，建议客户根据实际业务场景调整配置：

```
# 是否在消费消息后将offset同步到Broker，当Consumer失败后就能从Broker获取最新的offset
auto.commit.enable=true
# 当auto.commit.enable=true时，自动提交Offset的时间间隔。建议设置至少1000
auto.commit.interval.ms=5000
# 当Broker端没有offset（如第一次消费或offset超过7天过期）时如何初始化offset，当收到OFFSET_OUT_OF_RANGE错误时，如何重置Offset
# earliest：表示自动重置到partition的最小offset
# latest：默认为latest，表示自动重置到partition的最大offset
# none：不自动进行offset重置，抛出OffsetOutOfRangeException异常
auto.offset.reset=latest

# 标识消费者所属的消费分组
group.id=""
# 使用Kafka消费分组机制时，消费者超时时间。当Broker在该时间内没有收到消费者的心跳时，认为该消费者故障失败，Broker发起重新Rebalance过程。目前该值的配置必须在Broker配置group.min.session.timeout.ms=6000和group.max.session.timeout.ms=300000之间
session.timeout.ms=10000
# 使用Kafka消费分组机制时，消费者发送心跳的间隔。这个值必须小于session.timeout.ms，一般小于它的三分之一
heartbeat.interval.ms=3000
# 使用Kafka消费分组机制时，再次调用poll允许的最大间隔。如果在该时间内没有再次调用poll，则认为该消费者已经失败，Broker会重新发起Rebalance把分配给它的partition分配给其他消费者
max.poll.interval.ms=300000

# Fecth请求最少返回的数据大小。默认设置为1B，表示请求能够尽快返回。增大该值会增加吞吐，同时也会增加延迟
fetch.min.bytes=1
# Fetch请求最多返回的数据大小，默认设置为50MB
fetch.max.bytes=52428800
# Fetch请求等待时间
fetch.max.wait.ms=500
# Fetch请求每个partition返回的最大数据大小，默认为10MB
max.partition.fetch.bytes=1048576
# 在一次poll调用中返回的记录数
max.poll.records=500

# 客户端请求超时时间，如果超过这个时间没有收到应答，则请求超时失败
request.timeout.ms=305000
 
```
