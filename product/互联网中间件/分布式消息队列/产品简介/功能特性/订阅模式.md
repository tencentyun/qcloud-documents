为了适用不同场景的需求，Pulsar 支持四种订阅模式：Exclusive、Shared、Failover、Key_Shared。

![订阅模式](https://qcloudimg.tencent-cloud.cn/raw/fbfd9ecad9703182e4a01412fe536d9f.png)

## 独占模式（Exclusive）

**Exclusive 独占模式（默认模式）**：一个 Subscription 只能与一个 Consumer 关联，只有这个 Consumer 可以接收到 Topic 的全部消息，如果该 Consumer 出现故障了就会停止消费。

Exclusive 订阅模式下，同一个 Subscription 里只有一个 Consumer 能消费 Topic，如果多个 Consumer 订阅则会报错，适用于全局有序消费的场景。

![Exclusive 模型图](https://qcloudimg.tencent-cloud.cn/raw/eb8883954cc273035acaf72b75869955.png)
<dx-codeblock>
:::  java
// 构建消费者
Consumer<byte[]> consumer = pulsarClient.newConsumer()
    // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称，从【Topic管理】处复制
    .topic("persistent://pulsar-xxx/sdk_java/topic1")
    // 需要在控制台Topic详情页创建好一个订阅，此处填写订阅名
    .subscriptionName("sub_topic1")
    // 声明消费模式为exclusive（独占）模式
    .subscriptionType(SubscriptionType.Exclusive)
    .subscribe();
:::
</dx-codeblock>

启动多个消费者将收到错误信息。
![](https://qcloudimg.tencent-cloud.cn/raw/a5643f95aa4fbbaa14f6fbdba2317066.png)

## 共享模式（Shared）

消息通过 round robin 轮询机制（也可以自定义）分发给不同的消费者，并且每个消息仅会被分发给一个消费者。当消费者断开连接，所有被发送给他，但没有被确认的消息将被重新安排，分发给其它存活的消费者。

![Shared 模型图](https://qcloudimg.tencent-cloud.cn/raw/81bc25f19440fff8229a1fe716879f1e.png)
<dx-codeblock>
:::  java
// 构建消费者
Consumer<byte[]> consumer = pulsarClient.newConsumer()
    // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称，从【Topic管理】处复制
    .topic("persistent://pulsar-xxx/sdk_java/topic1")
    // 需要在控制台Topic详情页创建好一个订阅，此处填写订阅名
    .subscriptionName("sub_topic1")
    // 声明消费模式为 Shared（共享）模式
    .subscriptionType(SubscriptionType.Shared)
    .subscribe();
:::
</dx-codeblock>

多个 Shared 模式消费者。
![](https://qcloudimg.tencent-cloud.cn/raw/b4d26ed3eb60d8828d281a48a7ddc771.png)

## 灾备模式（Failover）

当存在多个 Consumer 时，将会按字典顺序排序，第一个 Consumer 被初始化为唯一接受消息的消费者。当第一个 Consumer 断开时，所有的消息（未被确认和后续进入的）将会被分发给队列中的下一个 Consumer。

![Failover 模型图](https://qcloudimg.tencent-cloud.cn/raw/7a2be3e1e0a9a60cca6a2f9facccf5a8.png)
<dx-codeblock>
:::  java
// 构建消费者
Consumer<byte[]> consumer = pulsarClient.newConsumer()
    // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称，从【Topic管理】处复制
    .topic("persistent://pulsar-xxx/sdk_java/topic1")
    // 需要在控制台Topic详情页创建好一个订阅，此处填写订阅名
    .subscriptionName("sub_topic1")
    // 声明消费模式为灾备模式
    .subscriptionType(SubscriptionType.Failover)
    .subscribe();
:::
</dx-codeblock>

多个 Failover 模式消费者。
![](https://qcloudimg.tencent-cloud.cn/raw/78d1859db165635424337c1b31cfb87d.png)

## KEY 共享模式（Key_Shared）
>!Key_Shared 本身在使用上存在一定的限制条件，由于其工程实现复杂度较高，在社区版本迭代中，不断有对 Key_Shared 的功能进行改进以及优化，整体稳定性相较 Exclusive,Failover 和 Shared 这三种订阅类型偏弱。如果上述三种订阅类型能满足业务需要，可以优先选用上述三种订阅类型。

当存在多个 Consumer 时，将根据消息的 Key 进行分发，Key 相同的消息只会被分发到同一个消费者。

![Key_Shared 模型图](https://qcloudimg.tencent-cloud.cn/raw/7a7a764e6769ca6b120c9708c3c31741.png)
默认情况下，Pulsar 在生产消息时是开启 Batch 功能的，Pulsar 的 Batch 消息解析是在 Consumer 侧处理的。所以在 Broker 侧一个 Batch 消息是被当作一条 Entry 处理的，所以对于 Key_shared 的基于消息 Key 有序订阅类型来说，是没办法处理这种 Case 的，因为不同 Key 的消息有可能被打包到同一个 Batch 中。针对这种情况在创建 Producer 时有如下两种规避方式：
1. 禁用 Batch。
<dx-codeblock>
:::  java
// 构建生产者
Producer<byte[]> producer pulsarClient.newProducer()
                .topic(topic)
                .enableBatching(false)
                .create();
// 发送消息时设置key
MessageId msgId = producer.newMessage()
    // 消息内容
    .value(value.getBytes(StandardCharsets.UTF_8))
    // 在此处设置key，key相同的消息只会被分发到同一个消费者。
    .key("youKey1")
    .send();
:::
</dx-codeblock>
2. 使用 key_based batch 类型。
<dx-codeblock>
:::  java
// 构建生产者
Producer<byte[]> producer = pulsarClient.newProducer()
                .topic(topic)
                .enableBatching(true)
                .batcherBuilder(BatcherBuilder.KEY_BASED)
                .create();
// 发送消息时设置key
MessageId msgId = producer.newMessage()
    // 消息内容
    .value(value.getBytes(StandardCharsets.UTF_8))
    // 在此处设置key，key相同的消息只会被分发到同一个消费者。
    .key("youKey1")
    .send();
:::
</dx-codeblock>

消费者代码示例：
<dx-codeblock>
:::  java
// 构建消费者
Consumer<byte[]> consumer = pulsarClient.newConsumer()
    // topic完整路径，格式为persistent://集群（租户）ID/命名空间/Topic名称，从【Topic管理】处复制
    .topic("persistent://pulsar-xxx/sdk_java/topic1")
    // 需要在控制台Topic详情页创建好一个订阅，此处填写订阅名
    .subscriptionName("sub_topic1")
    // 声明消费模式为 Key_Shared（Key 共享）模式
    .subscriptionType(SubscriptionType.Key_Shared)
    .subscribe();
:::
</dx-codeblock>

多个 Key_Shared 模式消费者。
![](https://qcloudimg.tencent-cloud.cn/raw/d74fc90e27c1b01c2132980bb8ec3088.png)
