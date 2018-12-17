## 查询 Consumer Group 信息

在消费组页面下，可以查看到当前 CKafka 实例的消费组列表展示。消费组信息包含状态、协议类型及均衡算法等。 同时可以支持对消费组订阅 topic 的 offset 重置，对历史消息进行重新消费。
1. 单击消费者组名称，可以查看消费者组中的消费者详情，以及具体消费者和订阅 topic 的对应关系。
2. 将对应的 Consumer group 展开，可以展示出该消费者组订阅的主题信息，包含主题名称和分区数目，提交 offset 的位置，最大 offset 位置以及未消费消息条数等。单击【查看分区详情】可以看到分区级别的 offset 消费情况。

> **注意：**
> 由于 offset 信息是在消费端维护的，因此 offset 的位置和消费者提交 offset 的方式有关，是异步展示的，并不一定代表实时的消费情况。

![](https://main.qcloudimg.com/raw/3882b8a3fd5d8cde4e32333aaf19c6b4.jpg)

## offset 设置

在离线数据处理等场景下，有时需要对 offset 进行重置，用于消费前一时间段的消息。此时可以通过设置 offset 重新消费。

1. 在消费者组列表中，单击 offset 设置，需要选取希望重置 offset 的 topic 信息（不选则默认全部 topic 的 offset 均重置）。
2. 对 offset 进行指定（通过以下四种方式）：
 - 将 offset 移动到指定的位置
 - 将 offset 向前或向后移动若干条
 - 从最新/最开始的位置开始消费
 - 从某一时间点开始进行重新消费

>**注意：**
> offset 设置范围要在最小 offset 和最大 offset 之间。在配置时，如果小于最小 offset 会从最小 offset 进行消费，如果大于最大 offset 会从最大 offset 进行消费。
> 重置消费分组时，需保证没有消费者在消费分组内才能进行重置，否则不能进行重置。

![](https://main.qcloudimg.com/raw/7b5d80d6d02317c7e760871289ac6772.jpg)

## Consumer Group 状态说明

列表页中 Consumer Group 的状态主要有 Dead、Empty、PreparingRebalance、AwaitingSync、Stable 几种，其中最常见的是 Empty、Stable 和 Dead 三种状态。Consumer Group 中的状态机转换如下图所示：
![](https://main.qcloudimg.com/raw/978ac0f373276ae3ec7bcce8a0c01978.jpg)
- Dead：消费者组内无成员并且 Metadata 已经被移除。
- Empty：消费分组内当前没有任何成员。如果组内所有 offset 过期的话就会变为 dead 状态。一般新创建 Group 的时候都会是 Empty 状态。
- Stable：消费分组中各个消费者已经加入，处于稳定状态。




