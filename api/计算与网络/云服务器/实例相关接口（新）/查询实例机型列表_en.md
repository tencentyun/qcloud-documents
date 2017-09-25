## 1. API Description

This API (DescribeInstanceTypeConfigs) is used to query the instance model configuration.

Domain name for API request: cvm.api.qcloud.com

* You can query the instance model configuration via `zone` and `instance-family`. Filter criteria can be found in `Filter`.
* If the parameter is empty, model configuration of all instances under the specified region are returned.


## 2. Input Parameters

The following request parameter list only provides API request parameters. Other parameters can be found in [Common Request Parameters](/document/api/213/6976).

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | Indicates API version No., used for identifying the API version of the request. To indicate the first version of this API, you can input the value "2017-03-12" to the parameter. |
| Filters.N | [array of [Filter]() objects](https://www.qcloud.com/document/api/213/9451#filter) | No | Filtering criteria can be found in [Table of Instance Filter Criteria](). The maximum number of `Filters ' of each request is 10, and the maximum number of` Filter.Values`' is 1. |

Table of Instance Filter Criteria

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| Zone | String | No | (Filter criteria) Filter by [Availability Zone](/ document / api / 213/806). |
| Instance-family | String | No | (Filter criteria) Filter by instance model series, such as: `S1`, `I1`, `M1`, etc. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. `RequestId` should be provided to the backend developer for a help when the user fails to call the API. |
InstanceTypeConfigSet | array of [InstanceTypeConfig](https://www.qcloud.com/document/api/213/9451#instance) objects | List of Instance Model Configuration. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://www.qcloud.com/document/api/213/10146).

| Error code | Description |
|---------|---------|
| InvalidParameterValue | Invalid parameter value. Parameter value is not in a correct format or not supported, etc. |
| InvalidFilter | [The specified `Filter` is not supported. ](https://www.qcloud.com/document/api/213/9451#filter) |
| InvalidFilterValue.LimitExceeded | The number of values of parameter `Filter` exceeds the limit. (https://www.qcloud.com/document/api/213/9451#filter) |
| InvalidZone.MismatchRegion | The specified `zone` does not exist. |
| InternalServerError | Internal service error. |


## 5. Example

Input

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeInstanceTypeConfigs
&Version=2017-03-12
&Filters.1.Name=zone
&Filters.1.Values.1=ap-guangzhou-2
&Filters.1.Name=instance-family
&Filters.1.Values.1=I1
&<<a href="https://www.qcloud.com/doc/api/229/6976">Common request parameters</a>>
</pre>

Output

<pre>
{
    "Response": {
        "InstanceTypeConfigSet": [
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "I1",
                "InstanceType": "I1.MEDIUM4",
                "CPU": 2,
                "Memory": 4
            },
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "I1",
                "InstanceType": "I1.MEDIUM8",
                "CPU": 2,
                "Memory": 8
            },
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "I1",
                "InstanceType": "I1.MEDIUM16",
                "CPU": 2,
                "Memory": 16
            },
            {
                "Zone": "ap-guangzhou-2",
                "InstanceFamily": "I1",
                "InstanceType": "I1.LARGE8",
                "CPU": 4,
                "Memory": 8
            },
			......
        ],
        "RequestId": "2f1fd71e-95ab-4f10-8adb-895e99d33ff5"
    }
}
</pre>

