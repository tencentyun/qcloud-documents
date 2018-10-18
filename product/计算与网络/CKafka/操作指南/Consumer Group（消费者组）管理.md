## Consumer Group（消费者组）管理


### 1. 查询Consumer Group信息

在消费组页面下，可以查看到当前CKafka实例的消费组列表展示。消费组信息包含状态、协议类型及均衡算法等。 同时可以支持对消费组订阅topic的offset重置，对历史消息进行重新消费。

点击消费者组名称，可以查看消费者组中的消费者详情，以及具体消费者和订阅topic的对应关系。

将对应的Consumer group展开，可以展示出该消费者组订阅的主题信息，包含主题名称和分区数目，提交offset的位置，最大offset位置以及未消费消息条数等。点击【查看分区详情】可以看到分区级别的offset消费情况。

> 注：由于offset信息是在消费端维护的，因此offset的位置和消费者提交offset的方式有关，是异步展示的，并不一定代表实时的消费情况。

![](https://main.qcloudimg.com/raw/3882b8a3fd5d8cde4e32333aaf19c6b4.jpg)

### 2. offset设置

在离线数据处理等场景下，有时需要对offset进行重置，用于消费前一时间段的消息。此时可以通过设置offset重新消费。

首先在消费者组列表中，点击offset设置，需要选取希望重置offset的topic信息（不选则默认全部topic的offset均重置）。之后可以通过四种方式对offset进行指定：
1. 将offset移动到指定的位置
2. 将offset向前或向后移动若干条
3. 从最新/最开始的位置开始消费
4. 从某一时间点开始进行重新消费

> 注：offset设置范围要在最小offset和最大offset之间。在配置时，如小于最小offset会从最小offset进行消费，如果大于最大offset会从最大offset进行消费。

![](https://main.qcloudimg.com/raw/7b5d80d6d02317c7e760871289ac6772.jpg)

### 3. Consumer Group状态说明

列表页中Consumer Group的状态主要有Dead、Empty、PreparingRebalance、AwaitingSync、Stable几种，其中最常见的是Empty，Stable和Dead三种状态。Consumer Group中的状态机转换如下图所示：

- Dead：消费者组内无成员并且Metadata已经被移除
- Empty：消费分组内当前没有任何成员。如果组内所有offset过期的话就会变为dead状态。一般新创建Group的时候都会是Empty状态。
- Stable：消费分组中各个消费者已经加入，处于稳定状态。

![](https://main.qcloudimg.com/raw/978ac0f373276ae3ec7bcce8a0c01978.jpg)


