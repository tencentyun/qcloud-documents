## 操作场景

部分场景下，Consumer Group 会很长一段时间不消费后重新消费，可将消费者组删除，其中的消费者重新建立连接时，会重置 Offset，从头开始消费。

>?Broker 版本不低于1.1.1，且 Consumer Group 的状态为 Empty 时，消费组才能被删除。

## 操作步骤

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在左侧导航栏单击**实例列表**，单击目标实例的“ID/名称”，进入实例详情页。
3. 在实例详情页，单击目标 Consumer Group 操作栏的**删除**，可直接删除 Consumer Group。
   ![](https://main.qcloudimg.com/raw/8acd42cf309d8b2f4868e1987ec4feb0.png)

