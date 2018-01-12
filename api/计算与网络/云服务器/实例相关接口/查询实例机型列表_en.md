## 1. API Description

This API (DescribeInstanceTypeConfigs) is used to query the instance model configuration.

Domain name for API request: cvm.api.qcloud.com

* You can query the instance model configuration via `zone` and `instance-family`. Filter criteria can be found in `Filter`.
* If the parameter is empty, model configuration of all instances under the specified region are returned.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| Filters.N | [array of [Filter](https://cloud.tencent.com/document/api/213/9451#filter) objects | No | Filtering criteria can be found in Table of Instance Filter Criteria. The maximum number of `Filters` of each request is 10, and the maximum number of` Filter.Values`' is 1. |

Table of Instance Filter Criteria

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| zone | String | No | (Filter criteria) Filter by [Availability Zone](/document/product/213/9452#zone). |
| instance-family | String | No | (Filter criteria) Filter by instance model series, such as: `S1`, `I1`, `M1`, etc. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |
|InstanceTypeConfigSet | Array of [InstanceTypeConfig](https://cloud.tencent.com/document/api/213/9451#instance) object | Instance Model Configuration |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).

| Error code | Description |
|---------|---------|
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidFilter | [The specified `Filter` is not supported. ](https://cloud.tencent.com/document/api/213/9451#filter) |
| InvalidFilterValue.LimitExceeded | [The number of values of parameter `Filter` exceeds the limit.](https://cloud.tencent.com/document/api/213/9451#filter) |
| InvalidZone.MismatchRegion | The specified `zone` does not exist. |
| InternalServerError | Tencent Cloud server error |


## 5. Example

Input

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeInstanceTypeConfigs
&Version=2017-03-12
&Filters.1.Name=zone
&Filters.1.Values.1=ap-guangzhou-2
&Filters.1.Name=instance-family
&Filters.1.Values.1=I1
&<<a href="/document/api/213/11650">Common request parameters</a>>
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

