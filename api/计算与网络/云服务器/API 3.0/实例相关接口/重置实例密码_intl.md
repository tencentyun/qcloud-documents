## 1. API Description

This API (ResetInstancePassword) is used to reset the password of the instance operating system to a user-specified value.

* This API only modifies the password of administrator account. The administrator account ID varies with the operating system of instance (e.g., `Administrator` for `Windows`, `ubuntu` for `Ubuntu`, and `root` for other systems).
* To reset the password for a running instance, you need to explicitly specify the parameter `ForceStop` for a forced shutdown. If not, you can only reset password for the instances that have been shut down.
* Batch operations are supported. You can reset the passwords of multiple instance operating systems to the same value. The maximum number of instances in a batch for each request is 100.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: ResetInstancesPassword |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceIds.N | Yes | Array of String | ID(s) of one or more instances you are working with, which can be obtained from `InstanceId` in the returned value of API [`DescribeInstances`](https://cloud.tencent.com/document/api/213/15728). The maximum number of instances for each request is 100. |
| Password | Yes | String | Login password of the instance. The rule of password complexity varies with different operating systems: <li>For `Linux` instances, the password must be a combination of 8-16 characters comprised of at least two of the following types: `[a-z, A-Z], [0-9]` and `[( ) ~ ~ ! @ # $ % ^ & * - + = _ &#124; { } [ ] : ; ' < > , . ? /]`, and must not begin with `/`.</li><li>For `Windows` instances, the password must be a combination of 12-16 characters comprised of at least three of the following types: `[a-z], [A-Z], [0-9]` and `[( ) ~ ~ ! @ # $ % ^ & * - + = _ &#124; { } [ ] : ; ' < > , . ? /]`, and must not begin with `/`.</li><li>If both `Linux` and `Windows` instances are involved, the password complexity is subject to the rule for `Windows` instances.</li> |
| UserName | No | String | Username of the instance operating system for which the password needs to be reset. This parameter is limited to 64 characters. |
| ForceStop | No | Boolean | Indicate whether a forced shutdown is performed on running instances. It is recommended that you manually shut down a running instance before resetting the user password. Values: <li>TRUE: indicates the forced shutdown will be performed after a normal shutdown failure. </li><li>FALSE: indicates that the forced shutdown is not performed after a normal shutdown failure. </li>Default value: FALSE. The result of forced shutdown is the same as turning off the power switch of the physical computer. Forced shutdown may lead to data loss or damage to file systems. Use this only when the server cannot be shut down properly. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidInstance.NotSupported | Unsupported instance. |
| InvalidInstanceId.Malformed | Invalid instance `ID`. The specified instance `ID` is in an incorrect format. For example, `ins-1122` indicates an `ID` length error. |
| InvalidInstanceId.NotFound | This instance cannot be found. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| InvalidParameterValue.TooLong | Invalid parameter value. The parameter value is too long. |
| InvalidPassword | Invalid password. The specified password does not conform to the rule of password complexity. For example, the password length does not meet the requirement. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Reset the password of a Linux/Windows instance

### Scenario description

Reset the password of a Linux/Windows instance, and then you can use this password to log in to the instance.

                
### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=ResetInstancesPassword
&InstanceIds.0=ins-r8hr2upy
&InstanceIds.1=ins-5d8a23rs
&Password=abc123ABC!@#
&ForceStop=TRUE
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
  }
}
```


        
