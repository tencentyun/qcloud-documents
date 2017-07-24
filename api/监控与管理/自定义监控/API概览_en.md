
## 1. Namespace Related APIs

| Feature | Action ID | Description |
|---------|---------|---------|
| [Create Namespace](/doc/api/255/创建命名空间) | CreateNamespace | Create namespace where users can create metrics |
| [Query Namespace](/doc/api/255/查询命名空间) | DescribeNamespace | Query current namespaces |
| [Delete Namespace](/doc/api/255/删除命名空间) | DeleteNamespace | Delete namespace according to namespace name |

## 2. Metric Related APIs

| Feature | Action ID | Description |
|---------|---------|---------|
| [Create Metric](/doc/api/255/创建指标) |  CreateMetric | Create metric under namespace and specify its corresponding statistical information |
| [Query Metric](/doc/api/255/查询指标) |  DescribeMetric | Query the metrics under the specified namespace |
| [Modify Metric](/doc/api/255/修改指标) | ModifyMetric| Modify the unit or metricCname of a metric |
| [Delete Metric](/doc/api/255/删除指标) | DeleteMetric | Delete metric according to namespace name and metric name |
| [Create Metric Aggregation](/doc/api/255/创建指标聚合)  | CreateMetricAggeration | Aggregate the specified dimensions under the metric to achieve features that can collect or query information of a certain group of dimensions under the metric |
| [Delete Metric Aggregation](/doc/api/255/删除指标聚合)  | DeleteMetricAggeration| Delete aggregation according to specified dimensions of the aggregation |
| [Add Statistical Type](/doc/api/255/添加统计类型) | CreateMetricStatisticsType| Add statistical type for specified dimension under the metric |
| [Delete Statistical Type](/doc/api/255/删除统计类型) | DeleteMetricStatisticsType| Delete statistical type under specified metric |

## 3. Data Report and Query Related APIs

| Feature | Action ID | Description |
|---------|---------|---------|
| [API for Data Reporting](/doc/api/255/数据上报接口) | PutMonitorData | Users can report data once they have created namespaces and metrics. Objects will be generated when data is reported |
| [Query Metric Object List](/doc/api/255/查询指标对象列表) | DescribeObjects | When data is reported, objects corresponding to each of the dimensions will be generated. This API is used to query the objects according to metric-related information |
| [Query Monitoring Data of Metric](/doc/api/255/查询指标监控数据) | GetMonitorData| Acquire monitoring data. The API is used to acquire multiple sets of data (between startTime and endTime) of the specified dimension under the metric |
| [Query Real-Time Monitoring Data of Metric](/doc/api/255/查询指标实时监控数据) | GetMonitorRealtimeData | Acquire real-time monitoring data of the metric. Data within the most recent period for the specified dimension of the monitored metric will be returned. |

## 4. Alarm Related APIs

| Feature | Action ID | Description |
|---------|---------|---------|
| [Create Alarm Rule](/doc/api/255/创建告警规则) |CreateAlarmRule | Add alarm rule for the statistical type under the metric. Alarm is triggered when the condition is met |
| [Query Alarm Rule](/doc/api/255/查询告警规则) | DescribeAlarmRuleList | Query the alarm rules under the specified metric of specified namespace |
| [Modify Alarm Rule](/doc/api/255/修改告警规则) | ModifyAlarmRule | Modify certain information of the alarm rule |
| [Delete Alarm Rule](/doc/api/255/删除告警规则)| DeleteAlarmRule | Delete alarm rule according to alarmRuleId |
| [Bind Alarm Rule to Object](/doc/api/255/绑定告警规则到对象) | BindAlarmRuleObjects | Bind objects with alarm rule. Corresponding objects will be generated when data is reported |
| [Query Objects Bound with Alarm Rule](/doc/api/255/查询告警规则绑定的对象) | DescribeAlarmRuleObjects | Query which objects are bound according to alarm rule ID |
| [Query Alarm Rule Bound with Object](/doc/api/255/查询对象绑定的告警规则) | DescribeAlarmRuleByObject | Query corresponding alarm rule of the object according to information such as its dimension |
| [Unbind Alarm Rule from Object](/doc/api/255/解绑告警规则和对象) | UnbindAlarmRuleObjects | Unbind alarm rule from object according to the alarm rule ID and the dimension information of the object |
| [Bind Alarm Rule from Alarm Recipient](/doc/api/255/绑定告警规则和告警接收人) | BindAlarmRuleReceivers | Bind alarm rule from alarm recipient according to the alarm rule ID and receiving group ID |
| [Unbind Alarm Rule from Alarm Recipient](/doc/api/255/解绑告警规则和告警接收人) | UnbindAlarmRuleReceivers | Unbind alarm rule from receivers that are bound with this rule according to the alarm rule ID |
| [Query Alarm List](/doc/api/255/查询告警列表) | DescribeAlarmList | Query the alarms for the specified object during specified time period |





