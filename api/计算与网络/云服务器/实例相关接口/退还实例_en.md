## 1. API Description

This API (TerminateInstances) is used to return instances.

Domain name for API request: cvm.api.qcloud.com

* You can use this API to return unused instances.
* All postpaid instances can be returned via this API. Prepaid instances that conform to the [rules for return](https://cloud.tencent.com/document/product/213/9711) can also be returned via this API.
* Batch operations are supported. Up to 100 instances can be returned in a time. If any instance that does not allow batch operations exists in the batch, an [error code](#4.-.E9.94.99.E8.AF.AF.E7.A0.81) is returned.


## 2. Input Parameters
The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Required | Type | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceIds.N | array of Strings | Yes | ID(s) of one or more instances you are working with. This can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](/document/api/213/9388). The maximum number of instances in a batch for each request is 100. |


## 3. Output Parameters
| Parameter | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).

| Error Code | Description |
|---------|---------|
| MissingParameter | A required parameter is missing in the request. |
| InvalidInstanceId.Malformed | The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidParameterValue | Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| InvalidInstance.NotSupported | This operation is not supported for the instance. |
|InvalidInstanceNotSupportedPrepaidInstance|This instance cannot be returned. For details, please see [Returning Prepaid Instances](https://cloud.tencent.com/document/product/213/9711)。|
| InternalServerError | Tencent Cloud server error. |


## 5. Example

Input
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=TerminateInstances
&Version=2017-03-12
&InstanceIds.1=ins-r8hr2upy
&InstanceIds.2=ins-5d8a23rs
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

Output
<pre>
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>

