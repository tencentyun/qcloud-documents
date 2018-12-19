## 1. API Description

This API (ImportKeyPair) is used to import key pairs.

* This API is designed to import the key pair to the user account, instead of binding it to an instance automatically. You can bind the key pair to an instance using API [AssociasteInstancesKeyPair](https://cloud.tencent.com/document/api/213/9404).
* The key pair name and the public key text of the key pair need to be specified.
* If you have only the private key, you can convert the private key to a public key using SSL tool before importing it.

## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. Value used in this API: ImportKeyPair |
| Version | Yes | String | Common parameter. Value used in this API: 2017-03-12 |
| KeyName | Yes | String | Name of key pair, which can consist of numbers, letters, and underscores, with a length of not more than 25 characters. |
| ProjectId | Yes | Integer | The ID of the [project](/document/product/378/10863) to which the created key pair belongs.<br><br> You can obtain the project ID by either of the following ways: <li>query the project ID via [Project List](https://console.cloud.tencent.com/project);</li><li>obtain the project ID from the `projectId` field in the returned values of API [DescribeProject](https://cloud.tencent.com/document/api/378/4400). </li><br>If it is the default project, enter 0. |
| PublicKey | Yes | String | The public key text of the key pair which is in an format of `OpenSSH RSA`. |

## 3. Output Parameters



| Parameter Name | Type | Description |
|---------|---------|---------|
| KeyId | String | ID of key pair. |
| RequestId | String | The unique request ID, which is returned for each request. When locating the problem, the RequestId of the request needs to be provided. |

## 4. Error Codes



| Error Code | Description |
|---------|---------|
| InternalServerError | Internal operation error. |
| InvalidKeyPair.LimitExceeded | The number of key pairs exceeds the limit. |
| InvalidKeyPairName.Duplicate | Duplicate key pair name exists. |
| InvalidKeyPairNameEmpty | Key pair name is empty. |
| InvalidKeyPairNameIncludeIllega l Char | Key pair name contains invalid characters. Only letters, numbers and underscores are allowed in the name. |
| InvalidKeyPairNameTooLong | The length of key pair name exceeds 25 characters. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidPublicKey.Duplicate | Invalid public key. The specified key already exists. |
| InvalidPublicKey.Malformed | Invalid public key. The specified public key is in an incorrect format that does not conform to `OpenSSH RSA`. |
| MissingParameter | Missing parameter. A required parameter is missing in the request. |

## 5. Example

## Example 1 Import a key pair

### Request parameters

```
https://cvm.tencentcloudapi.com/?Action=ImportKeyPair
&keyName=operation_key
&ProjectId=0
&PublicKey=ssh-rsa XXXXXXXXXXXX== skey_45071
&<Common request parameters>
```
### Response parameters

```
{
  "Response": {
    "KeyId": "skey-4e5ty7i8",
    "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
  }
}
```


      
