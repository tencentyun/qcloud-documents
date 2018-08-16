## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (ImportKeyPair) is used to import key pairs.

* This API only imports a key pair to user's account and does not automatically bind the key pair to an instance. You can use API [AssociasteInstancesKeyPair](https://cloud.tencent.com/document/api/213/9404) to bind a key pair to an instance.
* The key pair name and the public key text of the key pair need to be specified.
* If you have only the private key, you can convert the private key to a public key using SSL tool before importing it.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: ImportKeyPair |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| KeyName | Yes | String | Name of key pair, which can consist of numbers, letters, and underscores, with a length of not more than 25 characters. |
| ProjectId | Yes | Integer | The ID of the [project](/document/product/378/10863) to which the created key pair belongs.<br><br> You can obtain the project ID by either of the following ways: <br><li>Query the project ID via the [project list](https://console.cloud.tencent.com/project)<br><li> Obtain the project ID from the `projectId ` field value in the returned result of API [DescribeProject](https://cloud.tencent.com/document/api/378/4400).<br/><br/> If it is the default project, enter 0. |
| PublicKey | Yes | String | The key pair's public key text, such as `OpenSSH RSA`. | |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| KeyId | String | Key pair ID. |
| RequestId | String | The unique request ID, which is returned for each request. RequestId is required for locating a problem. |

## 4. Error Codes

The following only lists the error codes related to the API business logic. For other error codes, see [Common Error Codes](/document/api/213/15694#.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81).

| Error Code | Description |
|---------|---------|
| InternalServerError | Internal error. |
| InvalidKeyPair.LimitExceeded | Number of key pairs exceeds the limit. |
| InvalidKeyPairName.Duplicate | Duplicate key pair name. |
| InvalidKeyPairNameEmpty | Key name is empty. |
| InvalidKeyPairNameIncludeIllegalChar | Key name contains invalid characters. Key name can only contain letters, numbers and underscores. |
| InvalidKeyPairNameTooLong | Key name length exceeded 25 characters |
| InvalidParameterValue | Invalid parameter value. The parameter value is in an incorrect format or is not supported. |
| InvalidPublicKey.Duplicate | Invalid public key. The specified public key already exists. |
| InvalidPublicKey.Malformed | Invalid public key. The specified public key is in an incorrect format and does not conform to the `OpenSSH RSA` format. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Import a key pair

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=ImportKeyPair
&keyName=operation_key
&ProjectId=0
&PublicKey=ssh-rsa XXXXXXXXXXXX== skey_45071
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "KeyId": "skey-4e5ty7i8",
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
  }
}
```


