## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (ResetInstancesPassword) is used to reset the password of the instance operating system to a user-defined one.

* This API only modifies the password of administrator account. The administrator account ID varies with the operating system of instance (`Administrator` for `Windows`, `ubuntu` for `Ubuntu`, and `root` for other systems).
* To reset the password for a running instance, you need to explicitly specify the parameter `ForceStop` for a forced shutdown. If not, you can only reset password for the instances that have been shut down.
* Batch operations are supported. Reset the passwords of multiple instance operating systems to the same value. A maximum of 100 instances are allowed in a batch for each request.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes |  String | Common parameter. The value used for this API: ResetInstancesPassword |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceIds.N | Yes |  Array of String | ID(s) of one or more instances you are working with. You can obtain the parameter value from the `InstanceId` field value in the returned result of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). A maximum of 100 instances are allowed for each request. |
| Password | Yes |  String | Instance login password. Password complexity requirement varies with different operating systems, as shown below: <br><li>Password for a `Linux` instance should be a combination of 8 to 16 characters comprised of at least two of the following types: `[a-z, A-Z], [0-9]`, and `[( ) ~ ~ ! @ # $ % ^ & * - + = _ &#124; { } [ ] : ; ' < > , . ? /]`. The password cannot start with `/`.<br><li> The password for a `Windows` instance should be a combination of 12-16 characters comprised of at least three of the following types: `[a-z], [A-Z], [0-9]`, and `[( ) ~ ~ ! @ # $ % ^ & * - + = _ &#124; { } [ ] : ; ' < > , . ? /]`. The password cannot start with `/`.<br><li> If both `Linux` and `Windows` instances are included, the password complexity is subject to the requirement for a `Windows` instance. |
| UserName | No |  String | Username of the instance operating system for which the password needs to be reset. It cannot exceed 64 characters. |
| ForceStop | No | Boolean | Indicates whether to perform a forced shutdown on a running instance. It is recommended to manually shut down the running instance before resetting the user password. Supported values: <br><li>TRUE: Perform a forced shutdown<br><li>FALSE: Do not perform a forced shutdown<br><br>Default: FALSE.<br><br> Just like powering off a physical PC, a forced shutdown may cause data loss or the corruption of file system. Be sure to perform forced shutdown only when the server cannot be shut down normally. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalServerError | Internal error. |
| InvalidInstance.NotSupported | Unsupported instance. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. Specified instance `ID` is not in a correct format. For example, `ins-1122` has an invalid instance `ID` length. |
| InvalidInstanceId.NotFound | No instance found. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | Number of parameter values exceeds the limit. |
| InvalidParameterValue.TooLong | Invalid parameter value. The parameter value is too long. |
| InvalidPassword | Invalid password. The specified password does not conform to the rule of password complexity. For example, the password length does not meet the requirement. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Reset a password for a Linux/Windows instance

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=ResetInstancesPassword
&InstanceIds.0=ins-r8hr2upy
&InstanceIds.1=ins-5d8a23rs
&Password=abc123ABC!@#
&ForceStop=TRUE
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
  }
}
```


