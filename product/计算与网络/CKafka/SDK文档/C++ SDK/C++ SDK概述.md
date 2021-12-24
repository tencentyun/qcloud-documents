[C/C++客户端](https://github.com/edenhill/librdkafka) 可以通过 CKafka 提供的多种接入点接入并收发消息，本示例仅列举了部分配置信息如何配置，如需了解更多配置请参考 [C/C++ sdk 配置列表](https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md)、[CKafka 常用参数配置指南](https://cloud.tencent.com/document/product/597/30203)。



## 全局配置

| **配置项**          | **默认值** | **说明**                                                     |
| :------------------ | ---------- | ------------------------------------------------------------ |
| api.version.request | true       | kafka 消息格式版本协商，由于kafka支持多种消息格式，客户端需要先查询broker端支持的消息格式，然后根据broker返回的版本适配，建议开启。 |
| debug               | none       | debug信息配置，默认不打印debug信息，本示例中为了调试方便将debug设置成all，打印所有的debug信息，线上业务部署的时候请注意谨慎设置该参数。 |

## 生产者

| **配置项**       | **默认值** | **说明**                                                     |
| :--------------- | ---------- | ------------------------------------------------------------ |
| acks             | -1         | Kafka producer 的 ack 有 3 种机制，分别说明如下：<li>-1 或 all：Broker 在 leader 收到数据并同步给所有 ISR 中的 follower 后，才应答给 Producer 继续发送下一条（批）消息。 这种配置提供了最高的数据可靠性，只要有一个已同步的副本存活就不会有消息丢失。注意：这种配置不能确保所有的副本读写入该数据才返回，可以配合 Topic 级别参数 min.insync.replicas 使用。</li><li>0：生产者不等待来自 broker 同步完成的确认，继续发送下一条（批）消息。这种配置生产性能最高，但数据可靠性最低（当服务器故障时可能会有数据丢失，如果 leader 已死但是 producer 不知情，则 broker 收不到消息）</li><li>1：生产者在 leader 已成功收到的数据并得到确认后再发送下一条（批）消息。这种配置是在生产吞吐和数据可靠性之间的权衡（如果leader已死但是尚未复制，则消息可能丢失）<br>用户不显示配置时，默认值为1。用户根据自己的业务情况进行设置。</li> |
| linger.ms        | 5          | 请在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) -基本信息-接入方式-公网域名接入方式确认 SASL 接入点信息。 |
| compression.type | none       | 压缩格式配置，目前 0.9(包含)以下版本不允许使用压缩，0.10（包含）以上不允许使用 GZip 压缩。 |
| retries          | 2147483647 | 请求发生错误时重试次数，建议将该值设置为大于0，失败重试最大程度保证消息不丢失。 |
| retry.backoff.ms | 100        | 发送请求失败时到下一次重试请求之间的时间。                   |

## 消费者

| **配置项**              | **默认值** | **说明**                                                     |
| :---------------------- | ---------- | ------------------------------------------------------------ |
| enable.auto.commit      | true       | 是否在消费消息后将 offset 同步到 Broker，当 Consumer 失败后就能从 Broker 获取最新的 offset。 |
| auto.commit.interval.ms | 5000       | 当 auto.commit.enable=true 时，自动提交 Offset 的时间间隔，建议设置至少1000。 |
| auto.offset.reset       | largest    | 当 Broker 端没有 offset（如第一次消费或 offset 超过7天过期）时如何初始化 offset，当收到 OFFSET_OUT_OF_RANGE 错误时，如何重置 Offset。 <li>earliest：表示自动重置到 partition 的最小 offset。 </li><li>latest：默认为 latest，表示自动重置到 partition 的最大 offset。</li><li>none：不自动进行 offset 重置，抛出 OffsetOutOfRangeException 异常。</li> |
| session.timeout.ms      | 10000      | 使用 Kafka 消费分组机制时，消费者超时时间。当 Broker 在该时间内没有收到消费者的心跳时，认为该消费者故障失败，Broker 发起重新 Rebalance 过程。目前该值的配置必须在 Broker 配置group.min.session.timeout.ms=6000和group.max.session.timeout.ms=300000 之间。 |
| heartbeat.interval.ms   | 3000       | 使用 Kafka 消费分组机制时，消费者发送心跳的间隔。这个值必须小于 session.timeout.ms，一般小于它的三分之一。 |



C/C++客户端可以通过消息队列 CKafka 提供的多种接入点接入并收发消息。

| 项目     | **默认接入点**         | **SASL接入点**                                               |
| :------- | ---------------------- | ------------------------------------------------------------ |
| 网络     | VPC                    | VPC/公网                                                     |
| 协议     | PLAINTEXT              | SASL_PLAINTEXT                                               |
| 端口     | 9092                   | 请在 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 实例基本信息页面的**接入方式模块**获取SASL接入点信息。<br>![](https://main.qcloudimg.com/raw/6855a9d500dcbefbabed91515b695050.png) |
| SASL 机制 | 不适用                 | PLAIN：一种简单的用户名密码校验机制。                        |
| Demo     | [PLAINTEXT](https://github.com/TencentCloud/ckafka-sdk-demo/tree/main/cppkafkademo)          | [SASL_PLAINTEXT/PLAIN](https://github.com/TencentCloud/ckafka-sdk-demo/tree/main/cppkafkademo)                                     |
| 文档     | [默认接入点收发消息](https://cloud.tencent.com/document/product/597/54866) | [SASL 接入点 PLAIN 机制收发消息](https://cloud.tencent.com/document/product/597/54867)                              |
