## 1. API Description

This API (DescribeBaseMetrics) is used to query the type of basic monitoring metrics under the corresponding namespace.

Domain: monitor.api.qcloud.com


 

## 2. Input Parameters

The following request parameter list only provides API request parameters. Common request parameters need to be added when the API is called. For more information, please see [Common Request Parameters](https://www.qcloud.com/doc/api/405/%E5%85%AC%E5%85%B1%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0).
The Action field for this API is DescribeBaseMetrics.

| Parameter Name       | Required   | Type     | Description                                       |
| ---------- | ---- | ------ | ---------------------------------------- |
| namespace  | Yes    | String | Namespace. A namespace refers to a category of resources. After specifying a namespace, you can obtain all types of monitoring metrics under the specified category of resource. Currently, the namespaces supported by this API are consistent with those provided in [Read Monitoring Data (New)](https://www.qcloud.com/document/api/248/4667), namely, all the namespaces under which the monitoring data can be pulled via API GetMonitorData |
| metricName | No    | String | Monitoring metric name, such as "cpu_usage" and "mem_usage", which should contain 1-64 characters. If it is not specified, the list of all the metrics under the namespace will be returned |

 

## 3. Output Parameters

| Parameter Name      | Type     | Description                         |
| --------- | ------ | -------------------------- |
| code      | Int    | Error code, 0:  Succeeded; other values: Failed. For more information, please see Error Codes |
| message   | String | Error message                       |
| metricSet | Array  | Metric set                       |



Parameters of metricSet:

| Parameter Name        | Type     | Description                    |
| ----------- | ------ | --------------------- |
| namespace   | String | Namespace of a metric, such as qce/cvm  |
| metricName  | String | Metric name                  |
| metricCname | String | Chinese name of a metric                  |
| dimensions  | String | Dimension name                  |
| period      | Array  | Supported statistical granularity, i.e., the length of a statistical period (in seconds) |
| unit        | String | Metric unit (null means no unit)      |
| unitCname   | String | Chinese name of a metric unit (null means no unit)      |



## 4. Error Codes

| Error Code | Meaning    | Description                                 |
| ---- | ------- | ------------------------------------ |
| -502 | Resource does not exist   | OperationDenied.SourceNotExists      |
| -503 | Incorrect request parameter  | InvalidParameter                     |
| -505 | Parameter is missing    | InvalidParameter.MissingParameter    |
| -507 | Limit has been exceeded    | OperationDenied.ExceedLimit          |
| -509 | Incorrect combination of dimensions | InvalidParameter.DimensionGroupError |
| -513 | DB operation failed  | InternalError.DBoperationFail        |



## 5. Example

Input

```
https://monitor.api.qcloud.com/v2/index.php?
&<Common request parameters>
&namespace=qce/cvm`
```

Output

```
{
    "code" : 0,
    "message" : "ok",
    "metricSet" : [
        {
            "namespace" : "qce/cvm",
            "metricName" : "outtraffic",
            "metricCname" : "Outbound traffic of public network",
            "dimensions" : "instanceId", // Dimension
            "unit" : "Bps", // Unit
            "unitCname" : "Bps",
            "period" : [300]
        },
        {
            "namespace" : "qce/cvm",
            "metricName" : "inpkg",
            "metricCname" : "Inbound packets of public network",
            "dimensions" : "instanceId", // Dimension
            "unit" : "count/s", // Unit
            "unitCname" : "count/s",
            "period" : [300]
        }
    ]
}
```


