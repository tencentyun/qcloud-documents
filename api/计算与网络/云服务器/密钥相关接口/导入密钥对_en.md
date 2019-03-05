## 1. API Description

This API (ImportKeyPair) is used to import key pairs.

Domain name for API request: cvm.api.qcloud.com

* This API is designed to import the key pair to the user account, instead of binding it to an instance automatically. You can bind the key pair to an instance using API [AssociasteInstancesKeyPair](/document/api/213/9404).
* The key pair name and the public key text of the key pair need to be specified.
* If you have only the private key, you can convert the private key to a public key using `SSL` tool before importing it.


## 2. Input Parameters

The following request parameter list only provides API request parameters. For other parameters, please see [Common Request Parameters](https://cloud.tencent.com/document/api/213/11650).

| Parameter | Type | Required | Description |
|---------|---------|---------|---------|
| Version | String | Yes | API version No., used to identify the API version you are requesting. For the first version of this API, input "2017-03-12". |
| KeyName  | String | Yes | Name of key pair, which can consist of numbers, letters, and underscores, with a length of not more than 25 characters. |
| ProjectId | Integer | Yes | The ID of the [project](/document/product/378/10863) to which the created key pair belongs.<br><br> You can obtain the project ID by either of the following ways: <br><li>Query the project ID via [Project List](https://console.cloud.tencent.com/project);<br><li>Obtain the project ID from the `projectId` field in the returned values of API [DescribeProject](/document/api/378/4400). |
| PublicKey | String | Yes | The public key text of the key pair which is in an format of `OpenSSH RSA`.|


## 3. Output Parameters

| Parameter | Type | Description |
|---------|---------|---------|
| RequestId | String | Unique request ID. `RequestId` is returned for each request. In case of a failed call to the API, `RequestId` needs to be provided when you contact the developer at backend. |
| KeyId | String | ID of key pair.


## 4. Error Codes

The following error codes only include the business logic error codes for this API. For additional error codes, please see [Common Error Codes](https://cloud.tencent.com/document/api/213/11657).


| Error Code | Description |
|---------|---------|
| MissingParameter | Missing parameter. A required parameter is missing in the request. |
| InvalidParameterValue | Invalid parameter value. Parameter value is in an incorrect format or is not supported. |
| InvalidKeyPairName.Duplicate | Duplicate key pair name exists. |
| InvalidKeyPair.LimitExceeded | The number of key pairs exceeds the limit. |
| InvalidKeyPairNameEmpty | Key pair name is empty. |
| InvalidKeyPairNameTooLong | The length of key pair name exceeds 25 characters. |
| InvalidKeyPairNameIncludeIllega l Char | Key pair name contains invalid characters. Only letters, numbers and underscores are allowed in the name. |
| InvalidPublicKey.Malformed | Invalid public key. The specified public key is in an incorrect format that does not conform to `OpenSSH RSA`. |
| InvalidPublicKey.Duplicate | Invalid public key. The specified key already exists. |
| InternalServerError | Internal operation error. |


## 5. Example
 
Input

<pre>
https://cvm.api.qcloud.com/v2/index.php?Action=ImportKeyPair
&Version=2017-03-12
&keyName=operation_key
&ProjectId=0
&PublicKey=ssh-rsa XXXXXXXXXXXX== skey_45071
&<<a href="/document/api/213/11650">Common request parameters</a>>
</pre>

Output

<pre>
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "KeyId":"skey-4e5ty7i8"
    }
}
</pre>

