## 操作场景

该任务指导您在 CKafka 控制台查看实例下的消费者组信息。

## 操作步骤

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航栏单击**实例列表**，单击目标实例的“ID/名称”，进入实例详情页。
3. 在实例详情页，单击**Consumer Group**标签页，查看到当前 CKafka 实例的消费组信息。
   ![](https://main.qcloudimg.com/raw/05c88d97f36784e5f83c08b24e229265.png)
	- 在 Consumer Group 列表页，单击操作列的**查看消费者详情**，可以查看该消费组中的消费者信息，具体消费者和订阅 topic 的对应关系。
	- 在 Consumer Group 列表页，单击消费者名称列左侧的小三角，可以展示出该消费者组订阅的主题信息，包含主题名称、分区数目、提交的 offset 位置，最大的 offset 位置以及未消费消息条数等。单击操作列的**查看详情**可以看到分区级别的 offset 消费情况。
>?由于 offset 信息是在消费端维护的，因此 offset 的位置和消费者提交 offset 的方式有关，是异步展示的，并不一定代表实时的消费情况。
