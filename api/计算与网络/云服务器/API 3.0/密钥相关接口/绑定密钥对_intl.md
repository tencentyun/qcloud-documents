## 1. API Description

This API (AssociateInstancesKeyPairs) is used to bind a key pair to an instance.

* When the public key of a key pair is written to the `SSH` configuration of the instance, you can log in to the instance through the private key of the key pair.
* If the instance has been bound to a key, the original key will become invalid.
* If the instance was originally logged in through a password, the password becomes unavailable after the key is bound to the instance.
* Batch operations are supported. The maximum number of instances in a batch for each request is 100. If any instance that does not allow batch operations exists in the batch, an [error code] is returned.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value​used in this API: AssociateInstancesKeyPairs |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| InstanceIds.N | Yes | Array of String | ID(s) of one or more instances you are working with. The maximum number of instances in a batch for each request is 100. <br>You can obtain the available instance IDs by either of the following ways: <li>log in to the [console](https://console.cloud.tencent.com/cvm/index) to query the instance ID; </li><li>obtain the instance ID from the `InstanceId` parameter of the returned values of API [DescribeInstances](https://cloud.tencent.com/document/api/213/15728). |
| KeyIds.N | Yes | Array of String | ID(s) of one or more key pairs you are working with. The maximum number of key pairs in a batch for each request is 100. The key pair ID is in a format such as `skey-3glfot13`. <br>You can obtain the available key pair IDs by either of the following ways: <li>log in to the [console](https://console.cloud.tencent.com/cvm/sshkey) to query the key pair ID; </li><li>obtain the key pair ID from the `KeyId` parameter of the returned values of API [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699).</li> |
| ForceStop | No | Boolean | Whether to perform forced shutdown on the running instance. It is recommended to manually shut down the running instance before resetting the user password. Values: <li>TRUE: Perform a forced shutdown in case of a failure of normal shut-down. </li><li>FALSE: Do not. </li>Default: FALSE. |

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

## Example 1 Bind a CVM key pair

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=AssociateInstancesKeyPairs
&InstanceIds.0=ins-1e4r6y8i
&InstanceIds.1=ins-3e56fg78
&KeyIds.0=skey-4e5ty7i8
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


        
