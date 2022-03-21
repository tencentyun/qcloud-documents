通过事件规则，您可以将收集到的事件投递到指定的投递目标完成处理与消费，目前事件总线支持 [Ckafka](https://cloud.tencent.com/product/ckafka) 作为投递目标，完成事件到下游的直接消费。

### 配置方式
1. 登录 [事件总线控制台](https://console.cloud.tencent.com/eb)，选择指定事件集。
2. 在事件集详情页，单击**管理事件规则**，进行新增规则配置。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/cef9f9a2eb8b0e49b197097c241c88f5.png)
3. 进入**事件规则**页面，单击**新建事件规则**。
4. 根据页面提示填写相关信息。在绑定投递目标时，选择**消息队列（Kafka）**，根据提示，绑定 Ckafka 实例和 Topic。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/7063da30465e595a6fd3d446fd506466.png)
5. 单击**完成**，创建成功后即可在事件规则列表页查看。
>! 如果事件集上游事件源也是 Ckafka，请注意目标绑定的 Ckafka Topic 与事件源 Topic 不同，否则可能造成无穷递归，产生大量费用

### 投递事件
EventBridge 会自动为您解析 CloudEvent 字段，并只将 **Data** 字段内容投递至 Ckafka Topic。
