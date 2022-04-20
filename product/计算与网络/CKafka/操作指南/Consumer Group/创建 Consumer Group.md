## 操作场景

消息队列 CKafka 支持在控制台直接创建 Consumer Group，本文介绍在控制台创建 Consumer Group 的具体步骤。

> ? 单个实例建议不超过 50 个消费分组，超出会有一定限制。

## 操作步骤

### 创建 Consumer Group

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航栏单击**实例列表**，单击目标实例的“ID/名称”，进入实例详情页。
3. 在实例详情页，选择 **Consumer Group** 标签页，单击**新建**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/ef4f61dd7ece6194858d084326e746d5.png)
4. 在弹窗中填写消费者名称，勾选所要订阅的 Topic。
   <dx-alert infotype="explain" title="">
   支持同时勾选多个 Topic。
   </dx-alert>
5. 单击**提交**，在 Consumer Group 列表可以看到刚刚创建的消费者组。



### 关闭自动创建 Consumer Group

CKafka 默认允许自动创建 Consumer Group，您可以在 CKafka 控制台关闭允许自动创建 Consumer Group 开关，关闭后只能消费在控制台上已有的消费组，无法正常新建数据同步任务。

![](https://qcloudimg.tencent-cloud.cn/raw/294107dd0591e3a0d9c46c8a9e9df61d.png)
<dx-alert infotype="explain" title="">
仅支持专业版和2.4.1及以上版本。
</dx-alert>
