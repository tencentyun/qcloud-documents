>!您目前查阅的是旧版自定义监控文档，新版自定义监控已灰度上线，如需使用可进入 [申请页面](https://url.cn/5OoeGnQ) 申请体验，详情您可查阅 [新版自定义监控](https://cloud.tencent.com/document/product/397/40203) 文档。
若在使用过程中遇到任何问题，您可以加入自定义监控交流 QQ 群（793979710）进行咨询，我们将竭诚为您服务！  

## 命名空间相关接口

| 接口功能                          | Action ID         | 功能描述                  |
| ----------------------------- | ----------------- | --------------------- |
| [创建命名空间](/doc/api/255/创建命名空间) | CreateNamespace   | 创建命名空间，用户可以在命名空间下创建指标 |
| [查询命名空间](/doc/api/255/查询命名空间) | DescribeNamespace | 查询当前命名空间              |
| [删除命名空间](/doc/api/255/删除命名空间) | DeleteNamespace   | 根据命名空间名称删除命名空间        |

## 指标相关接口

| 接口功能                          | Action ID                  | 功能描述                                     |
| ----------------------------- | -------------------------- | ---------------------------------------- |
| [创建指标](/doc/api/255/创建指标)     | CreateMetric               | 在命名空间下创建指标，指定指标对应的统计信息                   |
| [查询指标](/doc/api/255/查询指标)     | DescribeMetric             | 查询指定命名空间下的指标                             |
| [修改指标](/doc/api/255/修改指标)     | ModifyMetric               | 修改指标的 unit 或者 metricCname                   |
| [删除指标](/doc/api/255/删除指标)     | DeleteMetric               | 根据命名空间名和指标名删除指标                          |
| [创建指标聚合](/doc/api/255/创建指标聚合) | CreateMetricAggeration     | 将指标下的指定维度聚合起来，以实现统计指标下部分维度的信息的功能以及查询指标下部分维度信息的功能 |
| [删除指标聚合](/doc/api/255/删除指标聚合) | DeleteMetricAggeration     | 依据聚合的维度信息将该聚合删除                          |
| [添加统计类型](/doc/api/255/添加统计类型) | CreateMetricStatisticsType | 为指标下的指定维度添加统计类型                          |
| [删除统计类型](/doc/api/255/删除统计类型) | DeleteMetricStatisticsType | 删除指定指标下的统计类型                             |

## 数据上报和查询相关接口

| 接口功能                                  | Action ID              | 功能描述                                     |
| ------------------------------------- | ---------------------- | ---------------------------------------- |
| [数据上报接口](/doc/api/255/数据上报接口)         | PutMonitorData         | 用户创建命名空间，指标之后可以上报数据，上报数据之后会产生对象          |
| [查询指标对象列表](/doc/api/255/查询指标对象列表)     | DescribeObjects        | 当上报数据之后，会产生各个维度对应的对象，根据指标相关信息查询          |
| [查询指标监控数据](/doc/api/255/查询指标监控数据)     | GetMonitorData         | 获取监控数据，此接口获取指标下指定维度的在 startTime 和 endTime 之间的多组数据 |
| [查询指标实时监控数据](/doc/api/255/查询指标实时监控数据) | GetMonitorRealtimeData | 获取指标实时监控数据，返回最近的 period 内，监控的指标的指定维度的数据。   |

## 告警相关接口

| 接口功能                                     | Action ID                 | 功能描述                        |
| ---------------------------------------- | ------------------------- | --------------------------- |
| [创建告警规则](/doc/api/255/创建告警规则)            | CreateAlarmRule           | 为指标下的统计类型添加告警规则，当满足条件时，触发告警 |
| [查询告警规则](/doc/api/255/查询告警规则)            | DescribeAlarmRuleList     | 查询指定命名空间，指标下的告警规则           |
| [修改告警规则](/doc/api/255/修改告警规则)            | ModifyAlarmRule           | 修改规则中的部分信息                  |
| [删除告警规则](/doc/api/255/删除告警规则)            | DeleteAlarmRule           | 依据 alarmRuleId 删除规则           |
| [绑定告警规则到对象](https://cloud.tencent.com/document/api/397/4256) | BindAlarmRuleObjects      | 将对象绑定到告警规则，当上报数据之后，会产生对应的对象 |
| [查询告警规则绑定的对象](/doc/api/255/查询告警规则绑定的对象)  | DescribeAlarmRuleObjects  | 依据告警规则 ID 查询绑定的对象             |
| [查询对象绑定的告警规则](/doc/api/255/查询对象绑定的告警规则)  | DescribeAlarmRuleByObject | 依据对象的维度信息等，查询其对应的告警规则       |
| [解绑告警规则和对象](/doc/api/255/解绑告警规则和对象)      | UnbindAlarmRuleObjects    | 依据告警规则 ID 和对象维度信息将两者解绑        |
| [绑定告警规则和告警接收人](https://cloud.tencent.com/document/api/397/4260) | BindAlarmRuleReceivers    | 依据告警规则 ID 和接收组 ID 将两者绑定         |
| [解绑告警规则和告警接收人](/doc/api/255/解绑告警规则和告警接收人) | UnbindAlarmRuleReceivers  | 依据告警规则id解绑规则绑定的接收人          |
| [查询告警列表](/doc/api/255/查询告警列表)            | DescribeAlarmList         | 查询指定时间段内指定对象的告警             |




