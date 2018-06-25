
## 1. API Description

This API (DisassociateInstancesKeyPairs) is used to unbind a key pair from an instance.

* Only `Linux` instances with a status of [`STOPPED`](https://cloud.tencent.com/document/api/213/9452#INSTANCE_STATE) are supported.
* After the key pair is unbound, the instance can be logged in with the original password.
* If no password was set, you cannot log in to the instance using `SSH` after unbinding. You can call API [ResetInstancesPassword](https://cloud.tencent.com/document/api/213/9397) to set a login password.
* Batch operations are supported. The maximum number of instances in a batch for each request is 100. If any instance that does not allow batch operations exists in the batch, an [error code] is returned.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: DisassociateInstancesKeyPairs |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceIds.N | Yes | Array of String | ID(s) of one or more instances you are working with. The maximum number of instances in a batch for each request is 100. You can obtain the available instance IDs by either of the following ways: <li>log in to the [console](https://console.cloud.tencent.com/cvm/index) to query the instance ID; </li><li>obtain the instance ID from the `InstanceId` parameter of the returned values of API [DescribeInstances](https://cloud.tencent.com/document/api/213/15728). |
| KeyIds.N | Yes | Array of String | List of key pair IDs. The maximum number of key pairs in a batch for each request is 100. The key pair ID is in a format such as `skey-11112222`. You can obtain the available key pair IDs by either of the following ways: <li>log in to the [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair ID; </li><li>obtain the key pair ID from the `KeyId` parameter of the returned values of API [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699). |
| ForceStop | No | Boolean | Whether to perform forced shutdown on the running instance. It is recommended to manually shut down the running instance before resetting the user password. Values: <li>TRUE: Perform a forced shutdown in case of a failure of normal shut-down. </li><li>FALSE: Do not. </li><br>Default: FALSE. |

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
| InvalidKeyPairId.Malformed | Invalid key pair ID. The specified key pair ID is in an incorrect format. For example, `skey-1122` indicates an ID length error. |
| InvalidKeyPairId.NotFound | Invalid key pair ID. The specified key pair ID does not exist. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | The number of parameter values exceeds the limit. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Unbind a key pair from an instance

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=unBindInstanceKey
&instanceIds.0=ins-w34e5rl9
&keyId=skey-e3r6y7ji
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


        
