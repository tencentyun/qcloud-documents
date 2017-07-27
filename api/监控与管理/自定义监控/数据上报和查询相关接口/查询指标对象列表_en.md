## 1. API Description

This API (DescribeObjects) is used to query the metric object list. After the data is reported, you can call this API to query the dimension information of the data you reported.

Domain name: monitor.api.qcloud.com


## 2. Input Parameters
The following request parameter list only provides API request parameters. Common request parameters are also needed when this API is called. For more information, please see <a href="/doc/api/255/公共请求参数" title="Common Request Parameters">Common Request Parameters</a>. The Action field for this API is DescribeObjects.

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| namespace | Yes | String | Namespace. This can be queried by calling the API <a href="/doc/api/255/查询命名空间" title="Query Namespace">Query Namespace</a> (DescribeNamespace) |
| metricName | Yes | String | Metric name. This can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric) |
| dimensionNames.n | Yes | Array | Group of dimension names. This can be queried by calling the API <a href="/doc/api/255/查询指标" title="Query Metric">Query Metric</a> (DescribeMetric). Enter all the dimensions or part of the aggregated dimensions under the metric |
| offset | No | Int | Offset. Default is 0 (result is displayed from the first record) |
| limit | No | Int | The number of records displayed on each page. Default is 30. The record is displayed from offset, and the number of records displayed is limit |



## 3. Output Parameters
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Error code, 0:  Successful. Other values: Failed. For more information, please see <a href="/doc/api/255/错误码" title="Error Codes">Common Error Codes</a> on the Error Codes page |
| message | String | Error message |
| data | Array | Specific information of object |
| total | Int | Total number of objects |

"data" of the records contains dimension name and the corresponding dimension group list


## 4. Example
Input
<pre>
https://monitor.api.qcloud.com/v2/index.php?
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
&namespace=cvm
&metricName=diskusage
&dimensionNames.0=ip
&dimensionNames.1=diskname
</pre>

Output
```
{
    "code": 0,
    "message": "",
    "data": {
        "records": [
            {
                "diskname": "sda",
                "ip": "172.31.58.160"
            },
            {
                "diskname": "sda",
                "ip": "172.31.58.161"
            }
        ],
        "total": 2
    }
}

```



