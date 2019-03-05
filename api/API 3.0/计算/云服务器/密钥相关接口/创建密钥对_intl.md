## 1. API Description

Domain name for API request: cvm.tencentcloudapi.com

This API (CreateKeyPair) is used to create an `OpenSSH RSA` key pair to be used for login to `Linux` instances.

* Developers only need to specify the key name, and the system can automatically create a key pair and return the ID of the generated key pair as well as its public and private keys.
* The name of key pair must be unique.
* The private key can be saved to a file as an authentication method for `SSH`.
* Tencent Cloud does not retain user's private key. Please keep it well.

A maximum of 10 requests can be initiated per second for this API.

Note: This API supports Finance regions. If the common parameter Region is a Finance region, a domain name with the Finance region needs to be specified, for example: cvm.ap-shanghai-fsi.tencentcloudapi.com



## 2. Input Parameters

The following request parameter list only provides API request parameters and some common parameters. For the complete common parameter list, see [Common Request Parameters](/document/api/213/15692).

| Parameter Name | Required | Type | Description |
|---------|---------|---------|---------|
| Action | Yes | String | Common parameter. The value used for this API: CreateKeyPair |
| Version | Yes |  String | Common parameter. The value used for this API: 2017-03-12 |
| Region | Yes |  String | Common parameter. For more information, please see the [list of regions](/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8) supported by the product. |
| KeyName | Yes | String | Name of key pair, which can consist of numbers, letters, and underscores, with a length of not more than 25 characters. |
| ProjectId | Yes | Integer | The ID of the project to which the created key pair belongs.<br/> You can obtain the project ID by either of the following ways: <br/><li>Query the project ID via the project list.<br/><li> Obtain the project ID from the `projectId ` field value in the returned result of API DescribeProject. |

## 3. Output Parameters

| Parameter Name | Type | Description |
|---------|---------|---------|
| KeyPair | [KeyPair](/document/api/213/##KeyPair) | The information of key pair. |
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
| InvalidProjectId.NotFound | Invalid project ID. The specified project ID does not exist. |
| MissingParameter | Parameter is missing. A required parameter is missing in the request. |

## 5. Example

### Example 1 Create a key pair

#### Input example

```
https://cvm.tencentcloudapi.com/?Action=CreateKeyPair
&KeyName=Tencent
&ProjectId=0
&<Common request parameters>
```

#### Output example

```
{
  "Response": {
    "KeyPair": {
      "KeyId": "skey-mv9yzyjj",
      "KeyName": "Tencent",
      "PrivateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDP0Yw2T4itUKOJQIK69c1Asy1UO88cxEbujR5Jbr0e/Ey1v4ZK\nAUzDnsBnFlf4hKPA1YvMB8RBYj4GcLtM7PrKnBNNram8rgl73X/klOO8oqKv+J/X\nUA7KHH1Y6wcn1RTRTMdDHbGhW1q/UpfeylNTbf+wEIWhEfaL5FKQm4hqCwIDAQAB\nAoGBAJEvSu5SaCD02hs0F2C4Aln2E2/qjMoDEa7spcEVfUhdaNX8ZLvk5pUvnikm\nwfSb7a71QUIcFu66zKxBK4kVcirBRCR8nTAQbQ6AhXQYP+y6ihZ9Z/g6BBEeqCpV\nuGPmKnhdxdJ8Al2huEZKJFUQhKM8XdP7dqn6yFDm0L2sTK6RAkEA9IbhP4/2CVSC\n6d8j5nj3ejPx25R3wc4G+st1tZn1O/TRqUknbVEvsxZC63bRjHiw086QIWr61L8f\nqQBLZ58DMwJBANmRv3aHVxv5sMlV0F3hD5ZgWEDIIjxD7oiBzU1rqvF6OpTQc1cF\nrnwxAXDtYYJ75B8qQEL1ph/zIE5YW0hlfckCQQCyVTwpUyCopU3kqqxQBaDXKtMU\nxS6h1VQZzBDIpMPJOj8+Ku/qNe+HuJCNkVY6EDtF/bv340GTrt+0LVbQ95MpAkEA\nxcvwUdTXB9LnuxKuHTsoDaFHepW4MivcJvRC7njM7z4dFf+wbFP4/mUbF0xoUtVJ\nXl/uDjH/tpo1K6S+UEIcqQJAfLQywCQdZ/qOJn0PwxiOhwniikSnZuZPNSw8T+kg\n/oxijESOLAJBnt3S/g+D530Enjitvfc9mEB7mh0VmwWvPg==\n-----END RSA PRIVATE KEY-----\n",
      "ProjectId": 0,
      "PublicKey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDP0Yw2T4itUKOJQIK69c1Asy1UO88cxEbujR5Jbr0e/Ey1v4ZKAUzDnsBnFlf4hKPA1YvMB8RBYj4GcLtM7PrKnBNNram8rgl73X/klOO8oqKv+J/XUA7KHH1Y6wcn1RTRTMdDHbGhW1q/UpfeylNTbf+wEIWhEfaL5FKQm4hqCw== skey_112168"
    },
    "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
  }
}
```


