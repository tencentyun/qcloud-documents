## 操作场景

部分场景下，Consumer Group 会很长一段时间不消费后重新消费，可将消费者组删除，其中的消费者重新建立连接时，会重置 Offset，从头开始消费。

### 删除 Consumer Group

>?Broker 版本不低于1.1.1，且 Consumer Group 的状态为 Empty 时，消费组才能被删除。

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在左侧导航栏单击**实例列表**，单击目标实例的“ID/名称”，进入实例详情页。
3. 在实例详情页，单击目标 Consumer Group 操作栏的**删除**，可直接删除 Consumer Group。
   ![](https://main.qcloudimg.com/raw/8acd42cf309d8b2f4868e1987ec4feb0.png)



### 删除关联 Topic 的订阅关系

当 Consumer group 状态为 Empty 时，支持删除关联的某个 Topic 的订阅关系。操作方法如下：

在 Consumer Group 列表页面，点击要删除的订阅关系旁的![](https://qcloudimg.tencent-cloud.cn/raw/319b76792ab9eed74c2ae3262cfa1f49.png)图标，确认后即可删除所关联 Topic 的订阅关系。



![](https://qcloudimg.tencent-cloud.cn/raw/1f6e47d9c765d0bd845dd098fae5c661.png)
