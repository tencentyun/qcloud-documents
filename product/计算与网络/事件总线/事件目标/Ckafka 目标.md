通过事件规则，您可以将收集到的事件投递到指定的投递目标完成处理与消费，目前事件总线支持 [Ckafka](https://cloud.tencent.com/product/ckafka) 作为投递目标，完成事件到下游的直接消费。

### 配置方式
1. 登录 [事件总线控制台](https://console.cloud.tencent.com/eb)，选择指定事件集，点击**管理事件规则**，进行新增规则配置
![](https://qcloudimg.tencent-cloud.cn/raw/88794089a9b493f9aff405efef8928b6.png)

2. 进入**事件规则**页面，单击**新建事件规则**。
![](https://qcloudimg.tencent-cloud.cn/raw/a2bec9c540de79684084dfe00deae4fb.png)

3. 根据提示，填写基本信息和筛选规则，点击**下一步**，绑定投递目标，选择**消息队列（Kafka）**，根据提示，绑定 Ckafka 实例和 Topic
![](https://qcloudimg.tencent-cloud.cn/raw/7063da30465e595a6fd3d446fd506466.png)

> 注意：如果事件集上游事件源也是 Ckafka，请注意目标绑定的 Ckafka Topic 与事件源 Topic 不同，否则可能造成无穷递归，产生大量费用

### 投递事件
EventBridge 会自动为您解析 CloudEvent 字段，并只将 **Data** 字段内容投递至 Ckafka Topic
