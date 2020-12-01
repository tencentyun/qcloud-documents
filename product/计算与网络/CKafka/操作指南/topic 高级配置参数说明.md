## 操作场景
新版本 CKafka 实例支持对 Topic 进行细粒度的参数配置，您可以通过 CKafka 控制台进行配置。

## 前提条件
- 已 [创建实例](https://cloud.tencent.com/document/product/597/30931)。
- 已 [创建 Topic](https://cloud.tencent.com/document/product/597/40415)。

## 操作步骤
1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在实例列表中，单击目标实例 ID，进入**Topic 管理**页面。
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

