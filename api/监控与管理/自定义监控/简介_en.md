Welcome to Tencent Custom Cloud Monitor (CCM) service.
CCM allows you to monitor and configure alarm rules against the resource utilization and application data to provide precise and real-time health status information on your business.
Users can use the APIs described in this document to work with CCM, including Create Namespace, Create Metric, etc. For more information, please see API overview.
Before using these APIs, please make sure that you have a thorough understanding of CCM's <a href="https://www.qcloud.com/doc/product/397/3984">Product Overview</a> and <a href="https://www.qcloud.com/doc/product/397/3989">Quick Start</a>.


The following are some commonly used terms in CCM:
## 1. Glossary

| Term | Full Name | Full Name | Description |
|---------|---------|---------|---------|
| Namespace | Namespace | <a href="https://www.qcloud.com/doc/product/397/3984">Namespace</a> | Namespace is a container of metrics. Metrics in different namespaces are independent from each other. The name of namespace can be customized. For example, the value of namespace is proc_monitor, which is process monitoring |
| Metric  | Metric | <a href="https://www.qcloud.com/doc/product/397/3984">Metric</a> | Metric is the variable to be monitored. For example, process CPU utilization is proc_cpu_usage, and process memory usage is proc_mem_usage |
| Dimension | Dimension |<a href="https://www.qcloud.com/doc/product/397/3984">Dimension</a> | Dimension is the name/value pair structure for identifying a monitoring object. It is used to describe the characteristics of the monitoring object. For example, when monitoring CPU utilization of a process, you can define the dimension name as machine ip, the process name as proc_name, to distinguish different processes on different machines |
| MetricAggregation | MetricAggregation | <a href="https://www.qcloud.com/doc/product/397/3984">Metric aggregation</a> | Choose and aggregate some of the dimensions under the metric to analyze the data of aggregated dimensions. For example, the metric proc_cpu_usage have two dimensions: ip and proc_name. Use machine ip dimension for aggregation to analyze the CPU utilization of multiple processes under the specified machine ip.
| StatisticsType | statistics Type | <a href="https://www.qcloud.com/doc/product/397/3984">Statistical type</a> | Statistical type is the method for calculating data, which consists of statistical period and statistical method. It means that the original data is analyzed using the statistical method within statistical period. For example, to calculate the average value of the original data within 5 minutes.
|statisticsType period|statisticsType period|<a href="https://www.qcloud.com/doc/product/397/3984">Statistical period</a> | Period within which the data is calculated. Currently, the supported period is 5 minutes |
|statisticsType statistics|statisticsType statistics| <a href="https://www.qcloud.com/doc/product/397/3984">Statistical method</a> | It is used to analyze the data set within a specified statistical period. Available analytical methods are: max (to take the maximum value in the data set), min (to take the minimum value in the data set), sum (to take the sum of all data in the data set), avg (to take the average value of all data in the data set), last (to take the last value in the data set) |


## 2.API Quick Start
To use CCM APIs, you need to complete at least the following four steps:

1. Create Namespace
You can use the API [Create Namespace](/doc/api/255/创建命名空间) to create a namespace.
2. Create Metric
After the namespace is created, you can use the API [Create Metric](/doc/api/255/创建指标) to create a metric in the namespace. When you create dimensions under the metric, choose whether to add statistical types to all dimensions of the metric.
3. Report Data
After the statistical types are created, you can use the [API for Data Reporting](/doc/api/255/数据上报接口) to report your data. The dimensions of the reported data should be the same with the dimension group defined in the created metric.
4. Query Data
After the data has been reported for a period of time, you can call the API [Query Monitoring Data of Metric](/doc/api/255/查询指标监控数据) to obtain the analysis result.

For more information on how to call the function API, please see [Examples](/doc/api/255/使用示例) page.



## 3. Service Limits
Currently, CCM is not supported in Hong Kong region.









