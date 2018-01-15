## 1. API Description

This API (CreateKeyPair) is used to create an `OpenSSH RSA` key pair to be used for login to `Linux` instances.

Domain name for API request: cvm.api.qcloud.com

* Developers only need to specify the key name, and the system can automatically create a key pair and return the ID of the generated key pair as well as its public and private keys.
* The name of key pair must be unique.
* The private key can be saved to a file as an authentication method for `SSH`.
* Tencent Cloud does not retain user's private key. Please keep it well.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| KeyName     | String | Yes  | Name of key pair, which can consist of numbers, letters, and underscores, with a length of not more than 25 characters.      |
|ProjectId| Integer| Yes| The ID of the [project](/document/product/378/10863) to which the created key pair belongs.<br><br> You can obtain the project ID by either of the following ways: <br><li>Query the project ID via [Project List](https://console.cloud.tencent.com/project);<br><li>Obtain the project ID from the `projectId` field in the retured values of API [DescribeProject](/document/api/378/4400).|


## 3. Output Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |
| KeyPair | [KeyPair](/document/api/213/9451#keypair) object| Information of key pair. |


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).


| Error code | Description |
|---------|---------|
| MissingParameter | Missing parameter. A required parameter is missing in the request. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidKeyPairName.Duplicate | Duplicate key pair name exists. |
| InvalidKeyPair.LimitExceeded | The number of key pairs exceeds the limit. |
| InvalidKeyPairNameEmpty | Key pair name is empty. |
| InvalidKeyPairNameTooLong | The length of key pair name exceeds 25 characters. |
| InvalidKeyPairNameIncludeIllegalChar | Key pair name contains invalid characters. Only letters, numbers and underscores are allowed in the name. |
| InvalidProjectId.NotFound | Invalid project ID. The specified project ID does not exist. |
| InternalServerError | Internal operation error. |


## 5. Example

Input

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=CreateKeyPair
&Version=2017-03-12
&KeyName=Tencent
&ProjectId=0
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

Output

<pre>
{
    "Response": {
        "KeyPair": {
            "KeyId": "skey-mv9yzyjj",
            "KeyName": "Tencent",
            "ProjectId": 0,
            "PublicKey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDP0Yw2T4itUKOJQIK69c1Asy1UO88cxEbujR5Jbr0e/Ey1v4ZKAUzDnsBnFlf4hKPA1YvMB8RBYj4GcLtM7PrKnBNNram8rgl73X/klOO8oqKv+J/XUA7KHH1Y6wcn1RTRTMdDHbGhW1q/UpfeylNTbf+wEIWhEfaL5FKQm4hqCw== skey_112168",
            "PrivateKey": "-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQDP0Yw2T4itUKOJQIK69c1Asy1UO88cxEbujR5Jbr0e/Ey1v4ZK\nAUzDnsBnFlf4hKPA1YvMB8RBYj4GcLtM7PrKnBNNram8rgl73X/klOO8oqKv+J/X\nUA7KHH1Y6wcn1RTRTMdDHbGhW1q/UpfeylNTbf+wEIWhEfaL5FKQm4hqCwIDAQAB\nAoGBAJEvSu5SaCD02hs0F2C4Aln2E2/qjMoDEa7spcEVfUhdaNX8ZLvk5pUvnikm\nwfSb7a71QUIcFu66zKxBK4kVcirBRCR8nTAQbQ6AhXQYP+y6ihZ9Z/g6BBEeqCpV\nuGPmKnhdxdJ8Al2huEZKJFUQhKM8XdP7dqn6yFDm0L2sTK6RAkEA9IbhP4/2CVSC\n6d8j5nj3ejPx25R3wc4G+st1tZn1O/TRqUknbVEvsxZC63bRjHiw086QIWr61L8f\nqQBLZ58DMwJBANmRv3aHVxv5sMlV0F3hD5ZgWEDIIjxD7oiBzU1rqvF6OpTQc1cF\nrnwxAXDtYYJ75B8qQEL1ph/zIE5YW0hlfckCQQCyVTwpUyCopU3kqqxQBaDXKtMU\nxS6h1VQZzBDIpMPJOj8+Ku/qNe+HuJCNkVY6EDtF/bv340GTrt+0LVbQ95MpAkEA\nxcvwUdTXB9LnuxKuHTsoDaFHepW4MivcJvRC7njM7z4dFf+wbFP4/mUbF0xoUtVJ\nXl/uDjH/tpo1K6S+UEIcqQJAfLQywCQdZ/qOJn0PwxiOhwniikSnZuZPNSw8T+kg\n/oxijESOLAJBnt3S/g+D530Enjitvfc9mEB7mh0VmwWvPg==\n-----END RSA PRIVATE KEY-----\n"
        },
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
</pre>

