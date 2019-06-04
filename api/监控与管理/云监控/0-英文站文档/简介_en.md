Welcome to Tencent Cloud Monitor service. Cloud Monitor provides comprehensive data monitoring for cloud services, intelligent data analysis, real-time failure alarm and customized data report configuration. It allows you to accurately know the health status of businesses and various cloud services in real time.
Users can use APIs described in this document to perform related operations, such as reading monitoring data. For information on supported operations, please see <a href="https://cloud.tencent.com/document/product/248/4474" title="API Overview">API Overview</a>.
Before using these APIs, please make sure that you have a thorough understanding of <a href="https://cloud.tencent.com/doc/product/248/967">CM products</a> and <a href="https://cloud.tencent.com/doc/product/248/1045">how to use them</a>.


The key terms for Cloud Monitor are as follows:
## 1. Glossary
| Term | Full Name  | Full Name | Description |
|---------|---------|---------|---------|
| Namespace  | Namespace | <a href="https://cloud.tencent.com/doc/product/248/968">Namespace</a> | Namespace is the container of metrics. Metrics in different namespaces are independent from each other, so the metrics from different applications will not be mistakenly aggregated into the same statistical information. |
| Metric  | Metric | <a href="https://cloud.tencent.com/doc/product/248/968">Metric</a> | A metric is used as a monitoring variable, and a data point refers to the time-varying value of the metric. For example, the CPU utilization of a CVM is a metric, and the space usage of a cloud database is another metric. |
| Dimension | Dimension |<a href="https://cloud.tencent.com/doc/product/248/968">Dimension</a> | Dimension is a structure of name/value pair for identifying a monitoring object, and is used to describe the characteristics of the monitoring object. |


## 2. API Quick Start

You can directly query the data by using Cloud Monitor via API:
You can use <a href="/doc/api/405/读取监控数据(新)" title="Read Monitoring Data (New)">Read Monitoring Data (New)</a> to query the data.



## 3. Service Limits

None.





