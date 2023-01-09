## 命名空间

Namespace = QCE/TDMQ

## 监控指标

> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。


### TDMQ RocketMQ 版

| 指标英文名              | 指标含义                                                     | 单位  | 维度                                | 统计粒度q       |
| ----------------------- | ------------------------------------------------------------ | ----- | ----------------------------------- | ---------------- |
| CmqQueueMsgBacklog | Queue 消息堆积数量                       | 条  | environmentId、tenantId、topicName  | 60s、300s、3600s |
| CmqTopicMsgBacklog | Topic 消息堆积数量                                           | 条 | environmentId、tenantId、topicName  | 60s、300s、3600s |
| InactiveMsgNum | 不可见消息条数                                 | 条    | appId、resourceId、resourceName | 60s、300s、3600s |
| CmqInactiveMsgPercentage | cmq 不可见消息百分比 | %     | environmentId、tenantId、topicName  | 60s、300s、3600s |
| MsgRateIn | 消息生产速率                                 | 条/秒 | environmentId、tenantId、topicName  | 60s、300s、3600s |
| MsgRateOut | 在所选时间范围中，本 Topic 下所有消费者某一秒内消费消息的数量 | 条/秒 | environmentId、tenantId、topicName | 60s、300s、3600s |
| MsgThroughputIn | 在所选时间范围内某一秒，本 Topic 下所有消费者消费的消息数据量大小 | B/S | environmentId、tenantId、topicName | 60s、300s、3600s |
| SubMsgThroughputOut | 消息消费流量                          | B/S | environmentId、tenantId、topicName | 60s、300s、3600s |
| StorageSize | 积压消息大小 | B | environmentId、tenantId、topicName | 60s、300s、3600s |
| MsgAverageSize | 生产消息平均大小 | B | environmentId、tenantId、topicName | 60s、300s、3600s |
| StorageBacklogPercentage | 消息积压已使用配额百分比 | % | environmentId、tenantId、topicName | 60s、300s、3600s |
| CmqRequestCount | 该指标用于计算API调用次数费用，并非实际调用次数 | 次 | appId、resourceId、resourceName | 60s、300s、3600s |

## 各维度对应参数总览

| 参数名称                       | 维度名称      | 维度解释                   | 维度解释                                 |
| ------------------------------ | ------------- | -------------------------- | ---------------------------------------- |
| Instances.N.Dimensions.0.Name  | environmentId | environmentId 的维度名称         | 输入 String 类型维度名称：environmentId  |
| Instances.N.Dimensions.0.Value | environmentId | 具体命名空间          | 输入具体命名空间，例如："CMQ_QUEUE-test99"，可在 [DescribeCmqQueues](https://cloud.tencent.com/document/product/1179/55909) 接口中获取，字段名为 “NamespaceName” |
| Instances.N.Dimensions.0.Name  | tenantId      | 集群 ID 的维度名称         | 输入 String 类型维度名称：tenantId       |
| Instances.N.Dimensions.0.Value | tenantId      | 具体集群 ID                | 输入具体集群 ID，例如：cmqq-xxxxxxxx ，可在 [DescribeCmqQueues](https://cloud.tencent.com/document/product/1179/55909) 接口中获取，字段名为 “QueueId” |
| Instances.N.Dimensions.0.Name  | topicName     | 主题名称的维度名称         | 输入 String 类型维度名称：topicName      |
| Instances.N.Dimensions.0.Value | topicName     | 具体主题名称               | 具体主题名称，例如：testTopic          输入具体集群 ID，例如：cmq-xxxxxxxx ，可在 [DescribeCmqQueues](https://cloud.tencent.com/document/product/1179/55909) 接口中获取，字段名为 “QueueName” |
| Instances.N.Dimensions.0.Name | appId | 主账号 APPID 的维度名称 | 输入 String 类型维度名称：appId |
| Instances.N.Dimensions.0.Value | appId | 主账号的具体 APPID | 输入主账号 APPID，例如：1250000000 |
| Instances.N.Dimensions.0.Name | resourceId | 集群 ID 的维度名称 | 输入 String 类型维度名称：resourceId |
| Instances.N.Dimensions.0.Value | resourceId | 具体集群 ID | 输入具体集群 ID，例如：cmq-xxxxxxxx ，可在 [DescribeCmqQueues](https://cloud.tencent.com/document/product/1179/55909) 接口中获取，字段名为 “TenantId” |
| Instances.N.Dimensions.0.Name | resourceName | 主题名称的维度名称 | 输入 String 类型维度名称：resourceName |
| Instances.N.Dimensions.0.Value | resourceName | 具体主题名称 | 具体主题名称，例如：testTopic          输入具体集群 ID，例如：cmq-xxxxxxxx ，可在 [DescribeCmqQueues](https://cloud.tencent.com/document/product/1179/55909) 接口中获取，字段名为 “QueueName” |


## 入参说明

**查询消息队列监控数据，入参取值如下：**

指标一：

&Namespace = QCE/TDMQ 
&Instances.N.Dimensions.0.Name = environmentId
&Instances.N.Dimensions.0.Value =具体命名空间
&Instances.N.Dimensions.1.Name = tenantId 
&Instances.N.Dimensions.1.Value = 具体集群 ID 
&Instances.N.Dimensions.2.Name = topicName 
&Instances.N.Dimensions.2.Value = 具体主题名称

指标二：

&Namespace = QCE/TDMQ 
&Instances.N.Dimensions.0.Name = appId
&Instances.N.Dimensions.0.Value =主账号 APPID
&Instances.N.Dimensions.1.Name = resourceId
&Instances.N.Dimensions.1.Value = 具体集群 ID 
&Instances.N.Dimensions.2.Name = resourceName
&Instances.N.Dimensions.2.Value = 具体主题名称
