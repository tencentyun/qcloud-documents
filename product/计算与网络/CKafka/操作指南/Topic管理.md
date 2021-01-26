## 操作场景
Topic（主题）是某一种分类的名字，消息在 Topic 中可以被存储和发布。CKafka 对外使用 Topic 的概念，生产者往 Topic 中写消息，消费者从 Topic 中读消息。为了做到水平扩展，一个 Topic 实际是由多个 [Partition（分区）](https://cloud.tencent.com/document/product/597/32544#F)组成，遇到瓶颈时，可以通过增加 Partition 的数量进行横向扩容。

该任务指导您通过 CKafka 控制台，在已有实例下 Topic 进行管理。


## 前提条件
已创建实例和 Topic（参考 [资源创建与准备](https://cloud.tencent.com/document/product/597/52493)）。

## 操作步骤
###  查看 Topic
1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在左侧导航栏单击【实例列表】，单击目标实例的“ID/名称”，进入实例详情页。
3. 在实例详情页，点击【topic管理】标签页，查看 Topic 信息。
![](https://main.qcloudimg.com/raw/51252cbe37e61b6d8f647fb48754a0ad.png)

### 删除 Topic
 > !
 > - 删除 Topic 的同时，存储在此 Topic 中的消息也将被删除，请谨慎操作。
 > - Topic 删除是异步操作，配置删除成功后，ZooKeeper 配置将会在1分钟后生效。若此期间创建同名 Topic，系统会提示错误码 [4000]10011，届时请您稍后重试。

1. 在实例列表页，单击目标实例的“ID/名称”，进入实例详情页。
2. 在实例详情页，单击【topic管理】标签页，在操作栏单击【删除】。
3. 在弹出窗口单击【确认】，Topic 将被删除。


### 配置 Topic 高级参数

1. 在实例列表页，单击目标实例的“ID/名称”，进入实例详情页。
2. 在实例详情页，单击【topic管理】标签页。
3. 单击操作列的【编辑】>【展示高级配置】，设置如下参数：
   ![](https://main.qcloudimg.com/raw/8f81b750e5bac17a011c8c531a579129.png)

参数说明如下：

| 参数名     | 默认值 | 参数范围  |说明|
| :-------- | :--------| :------ |:------ |
|cleanup.policy|delete|delete/compact|支持日志按保存时间删除，或者日志按 key 压缩（Kafka Connect 时需要使用 compact 模式）。|
|min.insync.replicas|1|-|当 producer 设置 request.required.acks 为1时，min.insync.replicas 指定 replicas 的最小数目。|
|unclean.leader.election.enable|true|true/false|指定是否能够设置不在 ISR 中 replicas 作为 leader。|
|segment.ms|-|1day - 90days|Segment 分片滚动的时长，单位为 ms，最小值为86400000ms。 |
|retention.ms|默认为实例的消息保留时间|60000ms - 90days|Topic 维度的消息保留时间。|
|max.message.bytes|-|0B - 8MB|Topic 维度的最大消息大小。不填写则默认实例维度消息大小为1MB。|

