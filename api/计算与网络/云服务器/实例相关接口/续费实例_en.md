## 1. API Description

This API (RenewInstances) is used to renew prepaid instances.

Domain name for API request: cvm.api.qcloud.com

* This operation only supported for prepaid instances, otherwise an [Error Code](#4.-.E9.94.99.E8.AF.AF.E7.A0.81) is returned.
* Please ensure that the user account has sufficient balance. The balance can be queried using the API [`DescribeAccountBalance`](/document/product/378/4397).


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceIds.N | array of Strings | Yes | ID(s) of one or more instances to be operated. This can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](/document/api/213/9388). The maximum number of instances for each request for batch operation is 100. |
| InstanceChargePrepaid | [InstanceChargePrepaid object](https://cloud.tencent.com/document/api/213/9451#instancechargeprepaid) | Yes | Prepaid mode, parameter configuration of prepaid by year/month. This parameter can specify the renewal length, whether to set automatic renewal and other attributes of the instance purchased on a prepaid basis. |


## 3. Output Parameters

| Parameter| Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. A unique `requestId` is returned for each request. In case of a failed call to the API, `requestId` needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).


| Error code | Description |
|---------|---------|
| MissingParameter |A required parameter is missing in the request. |
| InvalidInstanceId.NotFound | Invalid instance ID. The specified instance ID does not exist. |
| InvalidInstanceId.Malformed | Invalid instance ID. The specified instance ID is in an incorrect format. For example, `ins-1122` indicates an ID length error. |
| InvalidPeriod | Invalid renewal period. Value range: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36] (in month) |
| InvalidParameterValue | Parameter value is in an incorrect format or is not supported. |
| InvalidInstance.NotSupported | This operation is not supported for the instance. |
| InvalidAccount.InsufficientBalance | The account balance is sufficient. |
| InvalidAccount.UnpaidOrder | There is an unpaid order related to this account. |
| InternalServerError | Tencent Cloud server error. |


## 5. Example

Input
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=RenewInstances
&Version=2017-03-12
&InstanceIds.1=ins-r8hr2upy
&InstanceChargePrepaid.Period=1
&InstanceChargePrepaid.RenewFlag=NOTIFY_AND_MANUAL_RENEW
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

