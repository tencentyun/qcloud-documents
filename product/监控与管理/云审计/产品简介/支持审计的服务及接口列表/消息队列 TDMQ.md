腾讯云消息队列 TDMQ（Tencent Distributed Message Queue，简称 TDMQ）是一款基于 Apache 顶级开源项目 Pulsar 自研的金融级分布式消息中间件，具备跨城高一致、高可靠、高并发的特性。 TDMQ 目前已应用在腾讯计费绝大部分场景，包括支付主路径、实时对账、实时监控、大数据实时分析等方面。

下表为云审计支持的消息队列 TDMQ 操作列表：

| 操作名称                           | 资源类型 | 事件名称                          |
|--------------------------------|------|-------------------------------|
| 创建环境                           | tdmq | CreateEnvironment             |
| 创建一个 topic 的订阅关系                 | tdmq | CreateSubscription            |
| 新增主题                           | tdmq | CreateTopic                   |
| 删除环境                           | tdmq | DeleteEnvironments            |
| 删除订阅关系                         | tdmq | DeleteSubscriptions           |
| 批量删除 topics                     | tdmq | DeleteTopics                  |
| 获取环境属性                         | tdmq | DescribeEnvironmentAttributes |
| 获取环境列表                         | tdmq | DescribeEnvironments          |
| 消费订阅列表                         | tdmq | DescribeSubscriptions         |
| 查询主题列表                         | tdmq | DescribeTopics                |
| 修改环境属性                         | tdmq | ModifyEnvironmentAttributes   |
| 修改主题                           | tdmq | ModifyTopic                   |
| 根据时间戳进行消息回溯，精确到毫秒              | tdmq | ResetMsgSubOffsetByTimestamp  |
| 发送消息，此接口仅用于测试发生消息，不能作为现网正式生产使用 | tdmq | SendMsg                       |


