腾讯云云监控为CKafka实例提供以下监控指标：

| 指标中文名         | 指标英文名          | 指标含义                                     | 单位   | 维度             |
| ------------- | -------------- | ---------------------------------------- | ---- | -------------- |
| 生产流量          | pro_flow       | 实例级别生产流量，按粒度（1分钟、5分钟）统计求和                | MB   | 实例             |
| 消费流量          | con_flow       | 实例级别消费流量，按粒度（1分钟、5分钟）统计求和                | MB   | 实例             |
| 消息堆积量         | instance_heap  | 实例级别落盘消息量，按粒度（1分钟、5分钟）取最新值               | MB   | 实例             |
| 生产条数          | pro_count      | 实例级别生产条数，按粒度（1分钟、5分钟）统计求和                | 条    | 实例             |
| 消费条数          | con_count      | 实例级别消费条数，按粒度（1分钟、5分钟）统计求和                | 条    | 实例             |
| 生产请求的次数       | pro_req_count  | 实例级别生产请求次数，按粒度（1分钟、5分钟）统计求和              | 条    | 实例             |
| 消费请求的次数       | con_req_count  | 实例级别消费请求次数，按粒度（1分钟、5分钟）统计求和              | 条    | 实例             |
| 消息堆积条数        | msg_count      | 实例级别落盘消息条数，按粒度（1分钟、5分钟）取最新值              | 条    | 实例             |
| 生产流量          | pro_flow       | Topic级别生产流量，按粒度（1分钟、5分钟）统计求和             | MB   | Topic          |
| 消费流量          | con_flow       | Topic级别消费流量，按粒度（1分钟、5分钟）统计求和             | MB   | Topic          |
| 消息堆积量         | msg_heap       | Topic级别落盘消息量，按粒度（1分钟、5分钟）取最新值            | MB   | Topic          |
| 生产条数          | pro_count      | Topic级别生产条数，按粒度（1分钟、5分钟）统计求和             | 条    | Topic          |
| 消费条数          | con_count      | Topic级别消费条数，按粒度（1分钟、5分钟）统计求和             | 条    | Topic          |
| 生产请求的次数       | pro_req_count  | Topic级别生产请求次数，按粒度（1分钟、5分钟）统计求和           | 条    | Topic          |
| 消费请求的次数       | con_req_count  | Topic级别消费请求次数，按粒度（1分钟、5分钟）统计求和           | 条    | Topic          |
| 消息堆积条数        | msg_count      | Topic级别落盘消息条数，按粒度（1分钟、5分钟）取最新值           | 条    | Topic          |
| 当前分区最大堆积      | max_offset     | 消费分组对应partition的最大offset，按粒度（1分钟、5分钟）取最新值 | 条    | consumer group |
| 当前消费offset       | offset         | 消费分组对应partition当前消费offset，按粒度（1分钟、5分钟）取最新值 | 条    | consumer group |
| 未消费的消息条数      | unconsume      | 消费分组对应partition未被消费消息条数，按粒度（1分钟、5分钟）取最新值 | 条    | consumer group |
| 未消费消息堆积量 (MB) | unconsume_size | 消费分组对应partition未被消费的消息总大小，按粒度（1分钟、5分钟）取最新值 | MB   | consumer group |


有关更多如何使用CKafka的监控指标内容，可以查看云监控 API 中的[读取监控数据接口](https://cloud.tencent.com/document/api/248/4667)。
