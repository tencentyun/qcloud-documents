消息队列 CKafka（Cloud Kafka）是基于开源 Apache Kafka 消息队列引擎，提供高吞吐性能、高可扩展性的消息队列服务。消息队列 CKafka 完美兼容 Apache kafka 0.9、0.10、1.1 版本接口，在性能、扩展性、业务安全保障、运维等方面具有超强优势，让您在享受低成本、超强功能的同时，免除繁琐运维工作。

下表为云审计支持的消息队列 CKafka 操作列表：

| 操作名称             | 资源类型   | 事件名称                       |
|------------------|--------|----------------------------|
| 增加分区             | ckafka | AddPartition               |
| 添加路由             | ckafka | AddRoute                   |
| 增加分区             | ckafka | CreatePartition            |
| 添加路由             | ckafka | CreateRoute                |
| 创建主题             | ckafka | CreateTopic                |
| 增加主题白名单          | ckafka | CreateTopicIpWhiteList     |
| 删除路由             | ckafka | DeleteRoute                |
| 删除主题             | ckafka | DeleteTopic                |
| 删除主题白名单          | ckafka | DeleteTopicIpwhitelist     |
| 列出消息分组           | ckafka | DescribeConsumerGroup      |
| 获取实例属性           | ckafka | DescribeInstanceAttributes |
| 获取实例列表           | ckafka | DescribeInstances          |
| 路由详情             | ckafka | DescribeRoute              |
| 获取主题列表           | ckafka | DescribeTopic              |
| 获取主题属性           | ckafka | DescribeTopicAttributes    |
| 获取实例属性           | ckafka | GetInstanceAttributes      |
| 获取主题属性           | ckafka | GetTopicAttributes         |
| 列出消费分组           | ckafka | ListConsumerGroup          |
| 获取实例列表           | ckafka | ListInstance               |
| 路由详情             | ckafka | ListRoute                  |
| 获取主题列表           | ckafka | ListTopic                  |
| 设置 ckafka 消息转发到 cos | ckafka | ModifyForward              |
| 设置实例属性           | ckafka | ModifyInstanceAttributes   |
| 修改主题属性           | ckafka | ModifyTopicAttributes      |
