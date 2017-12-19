## 1. API Description

This API (DescribeInstancesStatus) is used to query the status of one or more instances.

Domain name for API request: cvm.api.qcloud.com

* You can query the status of an instance according to its `ID`.
* If the parameter is empty, the status of a certain number (specified by Limit, the default is 20) of instances is returned to the current user.

## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version number, used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceIds.N | array of Strings | No | To query according to one or more instance IDs, such as `ins-11112222`. For the format of this parameter, please see `id.n` section of API [Introduction](https://cloud.tencent.com/doc/api/229/568).
| Offset | Integer | No | Offset. Default is 0. For more information on `offset`, please see relevant sections of API [Introduction](/doc/api/229/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89). |
| Limit | Integer | No | Number of results to be returned. Default is 20. Maximum is 100. For more information on `limit`, please see relevant sections of API [Introduction](/doc/api/229/568#.E8.BE.93.E5.85.A5.E5.8F.82.E6.95.B0.E4.B8.8E.E8.BF.94.E5.9B.9E.E5.8F.82.E6.95.B0.E9.87.8A.E4.B9.89). |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |
| TotalCount | Integer | Number of instance statuses that meet the condition. |
| InstanceStatusSet | array of [InstanceStatus](https://cloud.tencent.com/document/api/213/9451#instancestatus) objects | [Instance Status](/document/api/213/9452#INSTANCE_STATE) list. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).

| Error code | Description |
|---------|---------|
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| InternalServerError | Internal service error. |


## 5. Example

Input

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeInstancesStatus
&Version=2017-03-12
&InstanceIds.1=ins-r8hr2upy
&InstanceIds.2=ins-5d8a23rs
&Offset=0
&Limit=2
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

Output

<pre>
{
    "Response": {
        "TotalCount": 2,
        "InstanceStatusSet": [
            {
                "InstanceId": "ins-r8hr2upy",
                "InstanceState": "RUNNING"
            },
            {
                "InstanceId": "ins-5d8a23rs",
                "InstanceState": "STOPPED"
            }
        ],
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>

