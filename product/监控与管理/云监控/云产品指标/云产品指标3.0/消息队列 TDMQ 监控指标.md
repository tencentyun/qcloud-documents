## 命名空间

Namespace=QCE/TDMQ

## 监控指标

#### CPU 监控

| 指标英文名          | 指标中文名                   | 指标说明                                                     | 单位 | 维度                                              | 统计粒度         |
| ------------------- | ---------------------------- | ------------------------------------------------------------ | ---- | ------------------------------------------------- | ---------------- |
| Averagemsgsize      | 消息平均大小                 | 在一个统计粒度内，所有消息平均大小                           | B    | tenantId、topicName                               | 60s、300s、3600s |
| Msgratein           | 生产速率                     | 在一个统计粒度内，平均每一秒生产的消息数量                 | S    | environmentId、               tenantId、topicName | 60s、300s、3600s |
| Msgrateout          | 消费消息的数量               | 在一个统计粒度内，所有消费者某一秒内消费消息的数量           | 个   | tenantId、topicName                               | 60s、300s、3600s |
| Msgthroughputout    | 消息数据量大小               | 在一个统计粒度内，所有消费者消费的消息数据量大小             | B    | tenantId、topicName                               | 60s、300s、3600s |
| Msgthroughputin     | 生产流量                     | 在一个统计粒度内，所有生产者生产的消息数据量大小             | B    | tenantId、topicName                               | 60s、300s、3600s |
| Numberofentries     | 消息当前总数量               | 已经生产到服务端的消息总数量                                 | 个   | tenantId、topicName                               | 60s、300s、3600s |
| Numproducers        | 生产者数量                   | 当前已经建立连接的生产者数量                                 | 个   | tenantId、topicName                               | 60s、300s、3600s |
| Storagesize         | 消息总大小                   | 当前存储在服务端的消息总大小                                 | 个   | tenantId、topicName                               | 60s、300s、3600s |
| Numsubscriptions    | 订阅者数量                   | 当前已创建的订阅者数量                                       | 个   | tenantId、topicName                               | 60s、300s、3600s |
| SubMsgrateout       | 消费速率                     | 在一个统计粒度内，平均每秒消费的消息条数                     | s    | environmentId、               tenantId、topicName | 60s、300s、3600s |
| SubMsgthroughputout | 消费流量                     | 在一个统计粒度内的全部消费流量                               | B    | environmentId、               tenantId、topicName | 60s、300s、3600s |
| SubMsgbacklog       | 未被消费的消息数量           | 在一个统计粒度内，已经生产到 TDMQ，但并未被消费的消息数量。消息堆积不宜太多，如有明显增长趋势，请对消费者服务进行扩容以减少堆积量 | 个   | environmentId、               tenantId、topicName | 60s、300s、3600s |
| SubMsgdelayed       | 延迟消息功能的消息数量       | 在一个统计粒度内，使用了 TDMQ 延迟消息功能的消息数量，这种消息在生产后不会马上被消费，用户会指定一个延迟时间，过后才允许消费者消费 | 个   | environmentId、               tenantId、topicName | 60s、300s、3600s |
| Unackedmessages     | 未接收到确认信息回传的消息数 | 在一个统计粒度内，已发送给消费者消息但是没有接收到确认信息回传的消息数量。如果存在很多这种消息，请检查您的消费者服务是否正常，以及是否使用官方 SDK 进行消费 | 个   | environmentId、               tenantId、topicName | 60s、300s、3600s |
| Numconsumers        | 有效连接 的消费者数量        | 当前已经建立连接的消费者数量                                 | 个   | environmentId、               tenantId、topicName | 60s、300s、3600s |
| Msgrateredeliver    | 重传消息的数量               | 在一个统计粒度内，某一秒内所有的重传消息的数量               | 个   | environmentId、               tenantId、topicName | 60s、300s、3600s |
| Msgrateexpired      | 消息删除速率                 | 消息过了最大保留时间后，系统自动进行删除的速率               | s    | environmentId、               tenantId、topicName | 60s、300s、3600s |

>?每个指标的统计粒度（Period）可取值不一定相同，可通过 [DescribeBaseMetrics](https://cloud.tencent.com/document/product/248/30351) 接口获取每个指标支持的统计粒度。

## 各维度对应参数总览

| 参数名称                       | 维度名称      | 维度解释           | 格式                                    |
| ------------------------------ | ------------- | ------------------ | --------------------------------------- |
| Instances.N.Dimensions.0.Name  | environmentId | 环境名称的维度名称 | 输入 String 类型维度名称：environmentId |
| Instances.N.Dimensions.0.Value | environmentId | 具体环境名称       | 输入环境名称，例如：test1               |
| Instances.N.Dimensions.1.Name  | tenantId      | 租户 ID 的维度名称   | 输入 String 类型维度名称：tenantId      |
| Instances.N.Dimensions.1.Value | tenantId      | 具体租户 ID         | 输入租户 ID，例如：pulsar-1234567891     |
| Instances.N.Dimensions.2.Name  | topicName     | 主题名称的维度名称 | 输入 String 类型维度名称：topicName     |
| Instances.N.Dimensions.2.Value | topicName     | 具体主题名称       | 输入具体主题名称，例如：test_topic      |

## 入参说明

**查询云服务器监控数据，入参取值如下：**
&Namespace=QCE/TDMQ
&Instances.N.Dimensions.0.Name=environmentId
&Instances.N.Dimensions.0.Value=具体环境名称
&Instances.N.Dimensions.1.Name=tenantId
&Instances.N.Dimensions.1.Value=具体租户 ID
&Instances.N.Dimensions.2.Name=topicName
&Instances.N.Dimensions.2.Value=具体主题名称
