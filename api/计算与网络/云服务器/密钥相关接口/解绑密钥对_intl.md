## 1. API Description

This API (DisassociateInstancesKeyPairs) is used to unbind a key pair from an instance.

Domain name for API request: <font style="color:red">cvm.api.qcloud.com</font>

* Only `Linux` instances with a status of [`STOPPED`](/document/api/213/9452#INSTANCE_STATE) are supported.
* After the key pair is unbound, the instance can be logged in with the original password.
* If no password was set, you cannot log in to the instance using `SSH` after unbinding. You can call API [ResetInstancesPassword](/document/api/213/9397) to set a login password.
* Batch operations are supported. The maximum number of instances in a batch for each request is 100. If any instance that does not allow batch operations exists in the batch, an [error code] is returned.
 
## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter Name | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| InstanceIds.N | array of Strings | Yes | ID(s) of one or more instances you are working with. The maximum number of instances in a batch for each request is 100. <br><br>You can obtain the available instance IDs by either of the following ways: <br><li>Log in to [console](https://console.cloud.tencent.com/cvm/index) to query the instance ID; <br><li>Obtain the instance ID from the `InstanceId` field in the returned values of API [DescribeInstances](/document/api/213/9388). |
| KeyIds.N | array of Strings | Yes | ID(s) of one or more key pairs you are working with. The maximum number of key pairs in a batch for each request is 100. The key pair ID is in a format such as `skey-11112222`.<br><br> You can obtain the available key pair IDs by either of the following ways: <br><li>Log in to [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair ID; <br><li>Obtain the key pair ID from the `KeyId` parameter of the returned values of API [DescribeKeyPairs](/document/api/213/9403). |
| ForceStop | Boolean | No | Whether to perform forced shutdown on the running instance. It is recommended to manually shut down the running instance before resetting the user password. Values: <br><li>TRUE: Perform a forced shutdown in case of a failure of normal shut-down. <br><li>FALSE: Do not. <br><br>Default: FALSE. |


## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).


| Error Code | Description |
|---------|---------|
| MissingParameter | Missing parameter. A required parameter is missing in the request. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| InvalidInstanceId.NotFound | Invalid instance ID. The specified instance ID does not exist. |
| InvalidInstanceId.Malformed | Invalid instance ID. The specified instance ID is in an incorrect format. For example, `ins-1122` indicates an ID length error. |
| InvalidInstance.NotSupported | This operation is not supported for the instance. |
| InvalidKeyPairId.Malformed | Invalid key pair ID. The specified key pair ID is in an incorrect format. For example, `skey-1122` indicates an ID length error. |
| InvalidKeyPairId.NotFound | Invalid key pair ID. The specified key pair ID does not exist. |
| InternalServerError | Internal operation error. |


## 5. Example

Input
<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=DisassociateInstancesKeyPairs
&Version=2017-03-12
&InstanceIds.1=ins-1e4r6y8i
&InstanceIds.2=ins-3e56fg78
&KeyIds.1=skey-4e5ty7i8
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

