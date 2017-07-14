In order to help you get started with Cloud Monitor APIs quickly, we provide an example on how to use these APIs. In this example, we will query the CPU utilization of a CVM:

## 1. Reading Monitoring Data

To query the CPU utilization of a CVM, the values of namespace and metricName are qce/cvm and cpu_usage respectively.
The Action field of common request parameters is GetMetricStatistics. The request parameters of this API are shown in the following table:
The metric dimensions.n.name for querying a CVM is always instanceId. The value of dimensions.n.value can be queried by calling the API <a href=https://www.qcloud.com/doc/api/229/%E6%9F%A5%E7%9C%8B%E5%AE%9E%E4%BE%8B%E5%88%97%E8%A1%A8>View List of Instances</a>(DescribeInstances).
In the input parameters, period is 300 s and statistics is avg by default, which means getting the average CPU utilization within 5 minutes.
The startTime and endTime by default are 00:00:00 and the current time of that day respectively.

| Parameter Name | Description | Value |
|---------|---------|---------|
| namespace | Namespace. It refers to the product type of the statistical metric, for example, "qce/cvm" refers to a CVM | qce/cvm |
| metricName | Metric name | cpu_usage |
| dimensions.n.name | Metric dimension name | instanceId |
| dimensions.n.value | Metric dimension value | ins-dyhv4ltt |
| period | Statistical period | None |
| statistics | The statistical method of data to be reported | None |
| startTime | The start time of statistics | None |
| endTime | The end time of statistics | None |

By combining common request parameters and API request parameters, you can get the final request as follows:
```
https://monitor.api.qcloud.com/v2/index.php?
Action=GetMetricStatistics
&Region=gz
&Timestamp=1465750149
&Nonce=46364
&SecretId=AKIDxxxxugEY
&Signature=5umi9gUWpTTyk18V2g%2FYi56hqls%3D
&namespace=qce/cvm
&dimensions.1.name=instanceId
&dimensions.1.value=ins-dyhv4ltt
&metricName=cpu_usage
```
The returned result of the above request is as follows:

```
{
    "metricName": "cpu_usage",
    "dataPoints": [
        0.4,
        0.5,
        ...
        0.4,
        0.4
    ],
    "code": 0,
    "message": ""
}
```
According to the returned result, the instanceId is the cpu_usage data of ins-dyhv4ltt on the day, with each data referring to the average CUP utilization within 5 minutes.


