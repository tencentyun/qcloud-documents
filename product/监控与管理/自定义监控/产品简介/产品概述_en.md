## 1. Overview of Custom Monitor Console (CCM)
In addition to regular monitoring metrics, CCM provides more entries forsimple self-report of monitoring data. With intelligent data analysis, real-time failure alarm and customized data report configuration, CCM allows you to accurately get an overall sense of the business health status in real time.

## 2. Basic Concepts of CCM
| Term | Description | 
|---------|---------|
| Namespace | Namespace is a container of metrics. Metrics in different namespaces are independent from each other. So the metrics from different applications will not be mistakenly aggregated into the same statistical information. CCM allows you to customize namespace and store data across multiple regions. For example, proc_monitor, i.e. monitoring A process in Guangzhou region |
| Metric | A metric is a CCM variable. Data point refers to the time-varying value of the variable. For example, process CPU utilization |
| Dimension | Dimension is a unique structure used to identify the monitoring object. The metric can be used only after the dimension value is determined. Dimension is helpful to design the statistical data aggregation structure. For example, when dimension values machine IP and proc_name are determined, you can determine a monitoring object: monitoring object A (IP=1.1.1.1&proc_name=test) |
| Dimension aggregation | Select different dimension groups based on the original dimensions (historical dimensions) for advanced data analysis. Aggregation is not performed across regions, namespaces and original dimensions. For example, calculate the average CPU utilization based on machine IP, i.e. to aggregate based on machine IP dimension |
| Statistical type | A set of statistical method and statistical period |
| Statistical method | Methods for calculating data including max (to take the maximum value), min (to take the minimum value), sum (to take the sum of all data), avg (to take the average of all data), last (to take the last value within the report period), etc. |
| Statistical period | Period for data calculation. Currently, the supported granularity is 5 minutes |
| Authentication | [API Authentication Details](http://www.qcloud.com/doc/api/229/%E6%8E%A5%E5%8F%A3%E9%89%B4%E6%9D%83) |


For example, a user needs to monitor the process CPU utilization of machine, and notifies relevant admin of the processes with 80% or higher CPU utilization.
In this scenario, the values for the above parameters are as follows:
- Namespce (namespace): proc_monitor (process monitoring)
- Metric (metricName): proc_cpu (process CPU utilization)
- Dimension: (dimensionNames): proc_name (process name); ip (IP of the reporting machine). The unique process is determined using process name and machine IP.
- Dimension Aggregation: IP (IP of the reporting machine). After performing aggregation based on machine IP dimension, you can calculate the CPU utilization of all the processes of the machine.
- Statistical method (statistics): Take max value from all the reported data within statistical period 
- Statistical period (period): Calculate data once every 5 minutes

