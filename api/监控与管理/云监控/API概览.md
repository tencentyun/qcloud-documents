##  云监控相关接口

| 接口功能                                     | Action ID           | 功能描述                              |
| ---------------------------------------- | ------------------- | --------------------------------- |
| [获取监控指标列表](https://cloud.tencent.com/document/api/248/7630) | DescribeBaseMetrics | 根据用户输入的命名空间和指标名查询对应监控指标           |
| [读取监控数据](https://cloud.tencent.com/document/api/248/4667)| GetMonitorData      | 获取云产品的监控数据，目前可以获取云服务器和 VPC 专线等监控数据 |
| [发送自定义消息告警](https://cloud.tencent.com/document/product/248/17913)    | SendCustomAlarmMsg | 根据传递的策略 ID 与消息内容将自定义告警内容推送至对应消息策略          |
