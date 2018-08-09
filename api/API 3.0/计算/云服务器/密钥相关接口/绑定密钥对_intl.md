## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (AssociateInstancesKeyPairs) is used to bind a key pair to an instance.

* When the public key of a key pair is written to the `SSH` configuration of the instance, you can log in to the instance through the private key of the key pair.
* If the instance has been bound with a key, the old key will become invalid.
* If the instance was originally logged in through a password, the password becomes unavailable after the key is bound to the instance.
* Batch operations are supported. A maximum of 100 instances are allowed in a batch for each request. If there is any instance that is unsupported for the operation in the batch of instances, an error code is returned.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: AssociateInstancesKeyPairs |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| InstanceIds.N | Yes | Array of String | ID(s) of one or more instances you are working with. A maximum of 100 instances are allowed in a batch for each request.<br> You can obtain the available instance ID by either of the following ways:<br><li>Query the instance ID by logging in to the [Console](https://console.cloud.tencent.com/cvm/index).<br><li> Call the API [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) to obtain the instance ID from the `InstanceId` field value in the returned result. |
| KeyIds.N | Yes | Array of String | ID(s) of one or more key pairs you are working with. A maximum of 100 key pairs are allowed in a batch for each request. A key pair ID takes a format such as `skey-3glfot13`.<br> You can obtain the available key ID by either of the following ways: <br><li>Query the key ID by logging in to the [Console](https://console.cloud.tencent.com/cvm/sshkey).<br><li> Call the API [DescribeKeyPairs](https://cloud.tencent.com/document/api/213/15699) to obtain the key pair ID from the `KeyId` field value in the returned result. |
| ForceStop | No | Boolean | Indicates whether to perform a forced shutdown on a running instance. It is recommended to manually shut down the running instance before resetting the user password. Supported values: <br><li>TRUE: Perform a forced shutdown in case of a failed normal shutdown.<br><li> FALSE: Do not perform a forced shutdown.<br> Default: FALSE. |

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
| InvalidKeyPairId.Malformed | Invalid key pair ID. The specified key pair ID is in an incorrect format. For example, `skey-1122` has an invalid `ID` length. |
| InvalidKeyPairId.NotFound | Invalid key pair ID. The specified key pair ID does not exist. |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidParameterValue.LimitExceeded | Number of parameter values exceeds the limit. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Bind a key pair to a CVM

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=AssociateInstancesKeyPairs
&InstanceIds.0=ins-1e4r6y8i
&InstanceIds.1=ins-3e56fg78
&KeyIds.0=skey-4e5ty7i8
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


