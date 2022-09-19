## 命名空间

Namespace = QCE/TDMQ

## 监控指标

> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。


### TDMQ RocketMQ 版

| 指标英文名              | 指标含义                                                     | 单位  | 维度                                | 统计粒度q       |
| ----------------------- | ------------------------------------------------------------ | ----- | ----------------------------------- | ---------------- |
| RopRateIn | rop 消息生产速率                                   | 条/秒  | environmentId、tenantId、topicName  | 60s、300s、3600s |
| RopRateOut | rop 消息消费速率                                        | 条/秒 | environmentId、tenantId、topicName  | 60s、300s、3600s |
| RopThroughputIn | rop 消息生产流量                                        | B/S   | environmentId、tenantId、topicName  | 60s、300s、3600s |
| RopThroughputOut | rop 消息消费流量 | B/S | environmentId、tenantId、topicName  | 60s、300s、3600s |
| RopMsgBacklog | rop 消息积压数量                                       | 条    | environmentId、tenantId、topicName  | 60s、300s、3600s |
| RopMsgAverageSize | rop 消息平均大小                                 | B   | environmentId、tenantId、topicName | 60s、300s、3600s |
| RopInMessageTotal | rop 消息发送总数量                              | 条    | environmentId、tenantId、topicName | 60s、300s、3600s |
| RopGroupCount | rop 消费组数量                                | 条    | environmentId、tenantId、topicName | 60s、300s、3600s |

## 各维度对应参数总览

| 参数名称                       | 维度名称      | 维度解释                   | 维度解释                                 |
| ------------------------------ | ------------- | -------------------------- | ---------------------------------------- |
| Instances.N.Dimensions.0.Name  | environmentId | environmentId 的维度名称         | 输入 String 类型维度名称：environmentId  |
| Instances.N.Dimensions.0.Value | environmentId | 具体命名空间          | 输入具体命名空间，例如：default，可在 [消息队列 RocketMQ 版本控制台-集群管理](https://console.cloud.tencent.com/tdmq/rocket-cluster)-命令空间列表中获取 |
| Instances.N.Dimensions.0.Name  | tenantId      | 集群 ID 的维度名称         | 输入 String 类型维度名称：tenantId       |
| Instances.N.Dimensions.0.Value | tenantId      | 具体集群 ID                | 输入具体集群 ID，例如：pulsar-xxxxxxxxxx ，可在 [消息队列 RocketMQ 版本控制台-集群管理](https://console.cloud.tencent.com/tdmq/rocket-cluster) 中获取集群 ID；或从 [DescribeRocketMQClusters](https://cloud.tencent.com/document/api/1179/63421) 接口中获取，字段名为“ClusterId”。 |
| Instances.N.Dimensions.0.Name  | topicName     | 主题名称的维度名称         | 输入 String 类型维度名称：topicName      |
| Instances.N.Dimensions.0.Value | topicName     | 具体主题名称               | 具体主题名称，例如：testTopic 可在控制台 [消息队列 RocketMQ 版本控制台-集群管理](https://console.cloud.tencent.com/tdmq/rocket-cluster)-Topic 列表中获取 |


## 入参说明

**查询消息队列监控数据，入参取值如下：**
&Namespace = QCE/TDMQ 
&Instances.N.Dimensions.0.Name = environmentId
&Instances.N.Dimensions.0.Value =具体命名空间
&Instances.N.Dimensions.1.Name = tenantId 
&Instances.N.Dimensions.1.Value = 具体集群 ID 
&Instances.N.Dimensions.2.Name = topicName 
&Instances.N.Dimensions.2.Value = 具体主题名称

