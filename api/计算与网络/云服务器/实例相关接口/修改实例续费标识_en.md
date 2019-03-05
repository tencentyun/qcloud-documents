## 1. API Description

This API (ModifyInstancesRenewFlag) is used to modify the renewal flags of prepaid instances.

Domain name for API request: cvm.api.qcloud.com

* Any instance marked "Auto Renewal" is automatically renewed for one month whenever it expires.
* Batch operations are supported. Up to 100 instances can be modified each time. For the instances that do not allow batch operations, an [Error Code](#4.-.E9.94.99.E8.AF.AF.E7.A0.81) is returned.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceIds.N | Array of Strings | Yes | ID(s) of one or more instances you want to modify. This can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](/document/api/213/9388). The maximum number of instances in a batch for each request is 100. |
| RenewFlag | String | Yes | Automatic renewal flag. Value range:<br><li>NOTIFY_AND_AUTO_RENEW: notify expiry and renew automatically<br><li>NOTIFY_AND_MANUAL_RENEW: notify expiry but not renew automatically<br><li>DISABLE_NOTIFY_AND_MANUAL_RENEW: neither notify expiry nor renew automatically<br><br>If this parameter is specified as NOTIFY_AND_AUTO_RENEW, the instance will be automatically renewed on a monthly basis when the account balance is sufficient. |


## 3. Output Parameters
| Parameter| Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).

| Error code | Description |
|---------|---------|
| InvalidInstanceId.NotFound | Invalid instance `ID`. The specified instance `ID` does not exist. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| InvalidInstance.NotSupported | This operation is not supported for the instance. |
| InternalServerError | Internal operation error. |


## 5. Example

Input
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=ModifyInstancesRenewFlag
&Version=2017-03-12
&InstanceIds.1=ins-r8hr2upy
&InstanceIds.2=ins-5d8a23rs
&RenewFlag=NOTIFY_AND_AUTO_RENEW
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

