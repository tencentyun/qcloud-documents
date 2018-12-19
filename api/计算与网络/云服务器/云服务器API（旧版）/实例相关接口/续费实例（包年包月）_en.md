## 1. API Description
 
This API (RenewInstance) is used to renew instances with an annual or monthly plan.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

* Please ensure that the user account has sufficient balance. The balance can be queried with [DescribeAccountBalance](/document/product/378/4397) API.

## 2. Input Parameters

The following list only provides API request parameters. For additional parameters, refer to [Public Request Parameters](/document/api/213/6976) page.
 
| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| instanceId | Yes | String | ID of the instance to be operated. It can be obtained from unInstanceId in the returned value of [DescribeInstances](https://cloud.tencent.com/doc/api/229/831) API. |
| period | Yes | Renewal length (in months); The minimum is 1 month and maximum is 36 months. |


## 3. Output Parameters
 
| Parameter Name | Type | Description |
|---------|---------|---------|
| code | Int | Common error code. A value of 0 indicates success, and other values indicate failure. For more information, refer to [Common Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#1.E3.80.81.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
| message | String | Module error message description depending on API. For more information, refer to [Module Error Codes](https://cloud.tencent.com/doc/api/372/%E9%94%99%E8%AF%AF%E7%A0%81#2.E3.80.81.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) on Error Code page. |
 
 
## 4. Error Codes
The following list only provides the business logic error codes for this API. For additional common error codes, refer to [CVM Error Codes](/document/product/213/6982) page.

| Error Code | Description |
|---|---|
OperationConstraints.InvaildInstanceStatus | Instance status is incorrect or the attempt to obtain the instance status failed
OperationConstraints.AccountBalanceNotEnough | Your balance is insufficient. Please top up first.
PermissionDenied.UserQualificationAuditFailed | Failed to pass user qualification verification
NotSupport.SharedInstance | Renewal is not allowed for a shared instance
OperationFail.SystemBusy | System is busy with resource purchase

## 5. Example
 
Input
<pre>
  https://cvm.api.qcloud.com/v2/index.php?Action=RenewInstance
  &instanceId=qcvm8e7bf56c115c53ce2d2a1ac2ea6e657a
  &period=1
  &<<a href="https://cloud.tencent.com/doc/api/229/6976">Public request parameters</a>>
</pre>

Output
```
{
    "codeDesc": "Success",
    "message": "",
    "code": 0,
    "dealId": "2790804"
}
```


