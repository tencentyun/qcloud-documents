## 查询 Consumer Group
在 Consumer Group 页面，您可以查看到当前 CKafka 实例的消费组信息。消费组信息包含状态、协议类型、均衡算法及操作。 您可以对消费组订阅 topic 进行 offset 重置，对历史消息进行重新消费。
![](https://main.qcloudimg.com/raw/1cd6c59ae22fabaa882759c978b4ffac.jpg)
- 在 Consumer Group 列表页，单击操作列的【查看消费者详情】，可以查看该消费组中的消费者信息，以及具体消费者和订阅 topic 的对应关系。
- 在 Consumer Group 列表页，单击消费者名称列左侧的小三角，可以展示出该消费者组订阅的主题信息，包含主题名称、分区数目、提交的 offset位置，最大的 offset 位置以及未消费消息条数等。单击操作列的【查看分区详情】可以看到分区级别的 offset 消费情况。

>?由于 offset 信息是在消费端维护的，因此 offset 的位置和消费者提交 offset 的方式有关，是异步展示的，并不一定代表实时的消费情况。

## 设置 offset 
在离线数据处理等场景下，有时需要对 offset 进行重置，用于消费前一时间段的消息。此时可以通过设置 offset 重新消费。
1. 在消费者组列表中，单击【offset 设置】
2. 在 offset 设置窗口，选取需要重置 offset 的 topic 信息（不选则默认全部 topic 的 offset 均重置）。
3. 对 offset 进行指定（通过以下四种方式）：
 - 将 offset 移动到指定的位置
 - 将 offset 向前或向后移动若干条
 - 从最新/最开始位置开始消费
 - 按时间点进行消费位置重置
![](https://main.qcloudimg.com/raw/2c912a8f81f66d2df1fcc3fc408c0d64.jpg)

>!
- offset 设置范围要在最小 offset 和最大 offset 之间。在配置时，如果小于最小 offset 会从最小 offset 进行消费，如果大于最大 offset 会从最大 offset 进行消费。
- 重置消费分组时，需保证没有消费者在消费分组内才能进行重置，否则不能进行重置。



## Consumer Group 状态说明
消费组列表页中 Consumer Group 的状态主要有 Dead、Empty、PreparingRebalance、AwaitingSync、Stable 几种，其中最常见的是 Empty、Stable 和 Dead 三种状态。Consumer Group 中的状态机转换如下图所示：
![](https://main.qcloudimg.com/raw/f35cb27ac35bef4628df17427e46c912.jpg)
- Dead：消费者组内无成员并且 Metadata 已经被移除。
- Empty：消费分组内当前没有任何成员。如果组内所有 offset 都已过期，则会变为 Dead 状态。一般新创建的 Group 默认为 Empty 状态。
开源 Kafka 0.10.x 版本规定，**当消费分组内没有任何成员且状态持续超过7天，此消费分组将会被自动删除**。
- Stable：消费分组中各个消费者已经加入，处于稳定状态。

##  Rebalance 状态详解
###  Rebalance 发生原因
根据 Consumer Group 的状态机可知，当 Consumer Group 为 Empty、AwaitSync 或 Stable 状态时，Group 可能会进行 Rebalance。以下情况可能会发生 Rebalance：
- 一个消费者订阅了 Topic。
- 消费者被关闭。
- 某个 Consumer 被 Group Coordinator（协调器）认为是 Dead 状态时。
如果某个Consumer 在`session.timeout.ms`时间内没有给 Group Coordinator 发心跳，则该 Consumer 将被认为是 Dead 状态，并且发起 Rebalance。详请参见 [CKafka 常用参数配置指南](https://cloud.tencent.com/document/product/597/30203)。
- 分区数增加。
- 订阅了不存在的 Topic。
如果您订阅了一个还未创建的 Topic，那么当这个 Topic 创建后会发生 Rebalance；同理，如果一个已经被订阅的 Topic 被删除，也会发生 Rebalance。
- 应用崩溃。

### Rebalance 过程分析
以0.10版本Kafka 的机制为例，Rebalance 过程分析如下：
1. 任何一个 Consumer 想要加入到一个 Consumer Group 中时，会发送一个 JoinGroup 的请求给 Group Coordinator。第一个加入 Group 的 Consumer 会变成 Group Leader。
2. Leader 会从 Group Coordinator 处收到这个 Group  中所有 Consumer 列表，并且负责给 Group 中的 Consumer 分配 partition。分区的分配可以通过 PartitionAssignor 接口来实现。
3. 分配完成后，Leader 会把分配结果发给 Group Coordinator，Coordinator 会把结果发送给所有的  Consumer。
因此每个 Consumer 只能查看到自己被分配的 partition，Leader 是唯一能够拿到Consumer Group 中的 Consumer 以及其分区情况的节点的 Consumer。

上述过程会在每次 Rebalance 发生时执行一次。

