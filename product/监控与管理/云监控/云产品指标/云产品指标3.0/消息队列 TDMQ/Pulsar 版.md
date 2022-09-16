## 命名空间

Namespace = QCE/TDMQ

## 监控指标

> ?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

### TDMQ Pulsar 版

| 指标英文名                   | 指标含义                                                     | 单位  | 维度                                        | 统计粒度q        |
| ---------------------------- | ------------------------------------------------------------ | ----- | ------------------------------------------- | ---------------- |
| MsgAverageSize               | 生产消息平均大小                                             | B     | environmentId、tenantId、topicName          | 60s、300s、3600s |
| MsgRateIn                    | 消息生产速率                                                 | 条/秒 | environmentId、tenantId、topicName          | 60s、300s、3600s |
| MsgThroughputIn              | 消息生产流量                                                 | B/S   | environmentId、tenantId、topicName          | 60s、300s、3600s |
| InMessagesTotal              | 当前 Topic 生产消息总数，该指标在发生服务端重启或者切换时会归零 | 条    | environmentId、tenantId、topicName          | 60s、300s、3600s |
| ProducersCount               | 生产者数量                                                   | 个    | environmentId、tenantId、topicName          | 60s、300s、3600s |
| StorageSize                  | 积压消息大小                                                 | B     | environmentId、tenantId、topicName          | 60s、300s、3600s |
| BacklogSize                  | 积压消息数量                                                 | 条    | environmentId、tenantId、topicName          | 60s、300s、3600s |
| SubscriptionsCount           | 订阅者数量                                                   | 个    | environmentId、tenantId、topicName          | 60s、300s、3600s |
| ConsumersCount               | 消费者数量                                                   | 个    | environmentId、tenantId、topicName          | 60s、300s、3600s |
| SubMsgBacklog                | 所选时间范围内，已经生产到 TDMQ，但并未被消费的消息数量。消息堆积不宜太多，如有明显增长趋势，请对消费者服务进行扩容以减少堆积量。 | 条    | environmentId、subName、tenantId、topicName | 60s、300s、3600s |
| SubMsgDelayed                | 所选时间范围内，使用了 TDMQ 延迟消息功能的消息数量，这种消息在生产后不会马上被消费，用户会指定一条延迟时间，过后才允许消费者消费。 | 条    | environmentId、subName、tenantId、topicName | 60s、300s、3600s |
| SubUnackedMsg                | 在所选时间范围内，已发送给消费者消息但是没有接收到确认信息回传的消息数量。如果存在很多这种消息，请检查您的消费者服务是否正常，以及是否使用官方 SDK 进行消费。 | 条    | environmentId、subName、tenantId、topicName | 60s、300s、3600s |
| SubConsumerCount             | 在所选时间范围内有效连接上本 Topic 的消费者数量。            | 个    | environmentId、subName、tenantId、topicName | 60s、300s、3600s |
| SubMsgRateRedeliver          | 在所选时间范围中，本 Topic 下某一秒内所有的重传消息的数量    | 条/秒 | environmentId、subName、tenantId、topicName | 60s、300s、3600s |
| SubMsgRateExpired            | 消息过期删除速率                                             | 条/秒 | environmentId、subName、tenantId、topicName | 60s、300s、3600s |
| SubMsgRateOut                | 消息消费速率                                                 | 条/秒 | environmentId、subName、tenantId、topicName | 60s、300s、3600s |
| SubMsgThroughputOut          | 消息消费流量                                                 | B/S   | environmentId、subName、tenantId、topicName | 60s、300s、3600s |
| NsStorageSize                | 命名空间消息积压大小                                         | B     | namespace、tenant                           | 60s、300s、3600s |
| TenantInMessagesTotal        | 虚拟集群入消息总数                                           | 条    | tenant                                      | 60s、300s、3600s |
| TenantMsgAverageSize         | 租户级别消息平均大小                                         | B     | tenant                                      | 60s、300s、3600s |
| TenantRateIn                 | 租户级别消息生产速率                                         | 条    | tenant                                      | 60s、300s、3600s |
| TenantRateOut                | 租户级别消息消费速率                                         | 条    | tenant                                      | 60s、300s、3600s |
| TenantStorageSize            | 租户级别消息积压大小                                         | B     | tenant                                      | 60s、300s、3600s |
| TenantIn entry Count         | 生产消息 entry 数量                                          | 条    | tenant                                      | 60s、300s、3600s |
| TenantInentrySizeLe128       | 生产消息小于等于128B的 entry 数量                            | 条    | tenant                                      | 60s、300s、3600s |
| TenantInentrySizeLe1Kb       | 生产消息大小512B_1KB的 entry 数量                            | 条    | tenant                                      | 60s、300s、3600s |
| TenantInentrySizeLe2Kb       | 生产消息大小1KB_2KB的 entry 数量                             | 条    | tenant                                      | 60s、300s、3600s |
| TenantInentrySizeLe4Kb       | 生产消息大小2KB_4KB的 entry 数量                             | 条    | tenant                                      | 60s、300s、3600s |
| TenantInentrySizeLe16Kb      | 生产消息大小1KB_2KB的 entry 数量                             | 条    | tenant                                      | 60s、300s、3600s |
| TenantInentrySizeLe1Mb       | 生产消息大小100KB_1MB的 entry 数量                           | 条    | tenant                                      | 60s、300s、3600s |
| TenantInentrySizeLe100Kb     | 生产消息大小16KB_100KB的 entry 数量                          | 条    | tenant                                      | 60s、300s、3600s |
| TenantInentrySizeLeOverflow  | 生产消息大小1KB_2KB的 entry 数量                             | 条    | tenant                                      | 60s、300s、3600s |
| TenantIn entry SizeSum       | 生产消息 entry 总大小                                        | 条    | tenant                                      | 60s、300s、3600s |
| TenantInentrySizeLe512       | 生产消息大小128B_512B的 entry 数量                           | 条    | tenant                                      | 60s、300s、3600s |
| TenantOutentrySizeCount      | 消费消息 entry 数量                                          | 条    | tenant                                      | 60s、300s、3600s |
| TenantOutentrySizeLe100Kb    | 消费消息大小16KB_100KB的 entry 数量                          | 条    | tenant                                      | 60s、300s、3600s |
| TenantOutentrySizeLe128      | 消费消息小于等于128B的 entry 数量                            | 条    | tenant                                      | 60s、300s、3600s |
| TenantOutentry SizeLe1Kb     | 消费消息大小512B_1KB的 entry 数量                            | 条    | tenant                                      | 60s、300s、3600s |
| TenantOutentrySizeLe16Kb     | 消费消息大小4KB_16KB的 entry 数量                            | 条    | tenant                                      | 60s、300s、3600s |
| TenantOutentrySizeLe1Mb      | 消费消息大小100KB_1MB的 entry 数量                           | 条    | tenant                                      | 60s、300s、3600s |
| TenantOutentrySizeLe2Kb      | 消费消息大小1KB_2KB的 entry 数量                             | 条    | tenant                                      | 60s、300s、3600s |
| TenantOutentrySizeLe4Kb      | 消费消息大小2KB_4KB的 entry 数量                             | 条    | tenant                                      | 60s、300s、3600s |
| TenantOutentrySizeLe512      | 消费消息大小128B_512B的 entry 数量                           | 条    | tenant                                      | 60s、300s、3600s |
| TenantOutentrySizeLeOverflow | 消费消息大于1MB的 entry 数量                                 | 条    | tenant                                      | 60s、300s、3600s |
| TenantOutentrySizeSum        | 消费消息 entry 总大小                                        | 条    | tenant                                      | 60s、300s、3600s |

## 各维度对应参数总览

| 参数名称                       | 维度名称      | 维度解释                   | 维度解释                                 |
| ------------------------------ | ------------- | -------------------------- | ---------------------------------------- |
| Instances.N.Dimensions.0.Name  | environmentId | environmentId 的维度名称         | 输入 String 类型维度名称：environmentId  |
| Instances.N.Dimensions.0.Value | environmentId | 具体命名空间          | 输入具体命名空间，例如：default，可从 [DescribeEnvironments](https://cloud.tencent.com/document/api/1179/46078) 接口中获取，字段名为“EnvironmentId”      |
| Instances.N.Dimensions.0.Name  | tenantId      | 集群 ID 的维度名称         | 输入 String 类型维度名称：tenantId       |
| Instances.N.Dimensions.0.Value | tenantId      | 具体集群 ID                | 输入具体集群 ID，例如：pulsar-xxxxxxxxxx，可在 [消息队列 Pulsar 版控制台-集群管理](https://console.cloud.tencent.com/tdmq/cluster) 中获取集群ID；或从 [DescribeClusterDetail](https://cloud.tencent.com/document/api/1179/52184) 接口中获取，字段名为“ClusterId”。|
| Instances.N.Dimensions.0.Name  | topicName     | 主题名称的维度名称         | 输入 String 类型维度名称：topicName      |
| Instances.N.Dimensions.0.Value | topicName     | 具体主题名称               | 具体主题名称，例如：testTopic 可在控制台 [消息队列 Pulsar 版控制台-Topic管理](https://console.cloud.tencent.com/tdmq/topic)  |
| Instances.N.Dimensions.0.Name  | namespace     | 集群所在命名空间的维度名称 | 输入 String 类型维度名称：namespace      |
| Instances.N.Dimensions.0.Value | namespace     | 具体命名空间               | 输入具体命名空间：例如：test，可从 [DescribeEnvironments](https://cloud.tencent.com/document/api/1179/46078) 接口中获取，字段“NamespaceName”               |
| Instances.N.Dimensions.0.Name  | tenant        | 集群 ID 的维度名称         | 输入 String 类型维度名称：tenant       |
| Instances.N.Dimensions.0.Value | tenant        | 具体集群 ID                | 输入具体集群 ID，例如：pulsar-xxxxxxxxxx，可从 [DescribeClusterDetail](https://cloud.tencent.com/document/api/1179/52184) 中获取，字段“ClusterId” |

## 入参说明

**查询消息队列监控数据，入参取值如下：**

指标类型一：
&Namespace = QCE/TDMQ 
&Instances.N.Dimensions.0.Name = environmentId
&Instances.N.Dimensions.0.Value = 具体命名空间
&Instances.N.Dimensions.1.Name = tenantId 
&Instances.N.Dimensions.1.Value = 具体集群 ID 
&Instances.N.Dimensions.2.Name = topicName 
&Instances.N.Dimensions.2.Value = 具体主题名称


指标类型二：
&Namespace = QCE/TDMQ 
&Instances.N.Dimensions.0.Name = tenant 
&Instances.N.Dimensions.0.Value = 具体集群 ID
