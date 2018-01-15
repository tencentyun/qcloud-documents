## 1. API Description

This API (ResetInstancePassword) is used to reset the password of the instance operating system to a user-specified value.

Domain name for API request: cvm.api.qcloud.com

* This API only modifies the password of administrator account. The administrator account ID varies with the operating system of instance (e.g., `Administrator` for `Windows`, `ubuntu` for `Ubuntu`, and `root` for other systems).
* To reset the password for a running instance, you need to explicitly specify the parameter `ForceStop` for a forced shutdown. If not, you can only reset password for the instances that have been shut down.
* Batch operations are supported. You can reset the passwords of multiple instance operating systems to the same value. The maximum number of instances in a batch for each request is 100. If any instance that does not allow batch operations exists in the batch, an [error code](#4.-.E9.94.99.E8.AF.AF.E7.A0.81) is returned.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceIds.N | array of Strings | Yes | ID(s) of one or more instances you are working with. This can be obtained from `InstanceId` in the returned values of API [`DescribeInstances`](/document/api/213/9388). The maximum number of instances in a batch for each request is 100. |
|Password|String|Yes|Login password of the instance. The rule of password complexity varies with different operating systems: <br><li>For `Linux` instances, the password must be a combination of 8-16 characters comprised of at least two of the following types: `[a-z，A-Z], [0-9]` and `[( ) &#126; ~ ! @ # $ % ^ & * - + = _ &#124; { } [ ] : ; ' < > , . ? /]`, and must not begin with `/`.<br><li>For `Windows` instances, the password must be a combination of 12-16 characters comprised of at least three of the following types: `[a-z], [A-Z], [0-9]` and`[( ) &#126; ~ ! @ # $ % ^ & * - + = _ &#124; { } [ ] : ; ' < > , . ? /]`, and must not begin with `/`.<br><li>If both `Linux` and `Windows` instances are involved, the password complexity is subject to the rule for `Windows` instances. |
|UserName|String|No|Username of the instance operating system for which the password needs to be reset. This parameter is limited to 64 characters.|
|ForceStop| Boolean| No | Whether to perform a forced shutdown on a running instance. It is recommended to manually shut down the running instance before resetting the user password for it. Values: <br><li>TRUE: Perform a forced shutdown in case of a failure of normal shutdown; <br><li>FALSE: Do not.<br><br> Default: FALSE. <br><br>Just like shutting down a physical PC, forced shutdown may cause data loss or the corruption of file system. Be sure to perform forced shutdown only when the server cannot be shut down normally.|


## 3. Output Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).


| Error code | Description |
|---------|---------|
| MissingParameter |  A required parameter is missing in the request. |
| InvalidInstanceId.NotFound | Invalid instance ID. The specified instance ID does not exist. |
| InvalidInstanceId.Malformed | Invalid instance ID. The specified instance ID is in an incorrect format. For example, `ins-1122` indicates an ID length error. |
|InvalidPassword| Invalid password. The specified password does not conform to the rule of password complexity. For example, the password length does not meet the requirement. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
|InvalidParameterValue.TooLong| Invalid parameter value. The parameter value is too long.|
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| InvalidInstance.NotSupported | This operation is not supported for the instance. |
| InternalServerError | Tencent Cloud server error. |


## 5. Example

Input
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=ResetInstancesPassword
&Version=2017-03-12
&InstanceIds.1=ins-r8hr2upy
&InstanceIds.2=ins-5d8a23rs
&Password=abc123ABC!@#
&ForceStop=TRUE
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

