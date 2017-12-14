Tencent Cloud API will perform identity authentication on each access request, so each request is required to include signature information in the common request parameter for user authentication. The signature is generated with the user's security credential, which consists of a SecretId and a SecretKey. Users with no security credential can apply for a credential from the Tencent Cloud official website. Otherwise they will not be able to call cloud APIs.

## 1. Applying for Security Credential
Before using Cloud APIs for the first time, a user needs to apply for a security credential in the Tencent Cloud CVM console.
Security credential consists of a SecretId and a SecretKey, where:

> SecretId is used to identify the API caller;

> SecretKey is a private key used to encrypt signature string, and is also used by the server to verify the signature string.

Note: API private key is an important credential when building Tencent Cloud API requests. With Tencent Cloud APIs, you can operate all of your Tencent Cloud resources under your account. To keep your property and services secure, please keep the private key well and change it on a timely basis (if you do, delete the old key in time).

To apply for a security credential, please proceed as follows:

1) Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/).

2) Select account name in the top right corner on the navigation bar, and choose "Cloud API Key" in the drop-down box to access the Cloud API key management page.

![](https://mc.qcloudimg.com/static/img/d32aa65f20cfce5af6f30ba5ee792490/capi_1.jpg)

3) On the [Cloud API Key Management](https://console.cloud.tencent.com/capi) page, click "New" to create a pair of SecretId/SecretKey.
> A developer account can have two pairs of SecretId/SecretKey at most.

> QQ accounts that are added as sub-users by a developer can apply for different security credentials on different developer consoles.

> Currently, the security credential of a sub user can only be used to call some of cloud APIs.

## 2. Generating Signature String
With the SecretID and SecretKey, a signature string can be generated. The following procedure is a detailed example for generating a signature string.

Assume that a user has the following SecretId and SecretKey:
>  SecretId: AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA

>  SecretKey: Gu5t9xGARNpq86cd98joQYCN3Cozk1qA

**Note: This is just an example. Please proceed with your actual SecretId and SecretKey!**
Take [View List of Instances](/doc/api/229/查看实例列表) (DescribeInstances) as an example. The possible request parameters are as follows when this API is called:

| Parameter Name | Description | Parameter Value | 
|---------|---------|---------|
| Action | Method name | DescribeInstances | 
| SecretId | Private Key ID | AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA | 
| Timestamp | Current timestamp | 1465185768 | 
| Nonce | Random positive integer | 11886 | 
| Region | Region where the instance is located | gz | 
| instanceIds.0 | ID of the instance to be queried | ins-09dx96dg | 
| offset | Offset value | 0 | 
| limit | Maximum number of outputs allowed | 20 | 

According to the above table, among the request parameters, there are only 5 common request parameters (Action, SecretId, Timestamp, Nonce and Region), instead of 6 ones as described in "Common Request Parameters". Actually, the sixth parameter Signature (signature string) is generated from the other parameters (including instruction request parameters) using the following procedure:
### 2.1. Sorting Parameters
First, sort all request parameters in ascending lexicographical order by their names, just like sorting words in a dictionary in ascending alphabetical order or numerical order. That is to say, sort the parameters by their first letters, then by their second letters if their first letters are the same, and so on. You can complete the sorting process using relevant sorting functions in programming language, such as the ksort function in PHP. The sorting result of the above sample parameters is as follows:

```
{
    'Action' : 'DescribeInstances',
    'Nonce' : 11886,
    'Region' : 'gz',
    'SecretId' : 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA',
    'Timestamp' : 1465185768,
	'instanceIds.0' : 'ins-09dx96dg',
    'limit' : 20,
    'offset' : 0,
}
```
Any other programming language can be used to sort these parameters as long as the same result is produced.
### 2.2. Generating Request String
This step is used to generate a request string.
Format the above sorted parameters as "parameter name"="parameter value". Take the parameter "Action" as an example. If the parameter value is "DescribeInstances", the resulting format will be "Action=DescribeInstances".
** Note: 1. "Parameter value" is the original value instead of url encoded value. 2. If the input parameter contains an underscore"_", you need to convert it to ".".**

Then, joint the formatted parameters together using "&" to generate the final request string:

```
Action=DescribeInstances&Nonce=11886&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1465185768&instanceIds.0=ins-09dx96dg&limit=20&offset=0
```

### 2.3. Generating Original Signature String
This step is used to generate an original signature string.
The original signature string is composed of the following parameters:

1) Request method: POST and GET methods are supported. In this case, we use a GET request. Note that the method must be in uppercase.
2) Request CVM: The request domain for [View List of Instances](/doc/api/229/查看实例列表) (DescribeInstances) is cvm.api.qcloud.com. The actual request domain varies depending on the module to which the API belongs. For more information, refer to the descriptions of each API.
3) Request path: The request path of Cloud API is always /v2/index.php.
4) Request string: This is the request string generated in the previous step.

Combination rule of original signature string:
> Request method + Request CVM +Request path + ? + Request string

The combination result is as follows:

```
GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances&Nonce=11886&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1465185768&instanceIds.0=ins-09dx96dg&limit=20&offset=0
```

### 2.4. Generating Signature String
This step is used to generate a signature string.
Sign the **original signature string** obtained in the previous step using HMAC-SHA1 algorithm, then encode the generated signature string using Base64 to obtain the final signature string.

For example, the codes are as follows if written in PHP:

```
$secretKey = 'Gu5t9xGARNpq86cd98joQYCN3Cozk1qA';
$srcStr = 'GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances&Nonce=11886&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1465185768&instanceIds.0=ins-09dx96dg&limit=20&offset=0';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $secretKey, true));
echo $signStr;
```

The final signature string is:

```
NSI3UqqD99b/UJb4tbG/xZpRW64=
```

When another programming language is used, you can perform the signature verification using the original signature string in the above example as long as the resulting signature string is identical to the one in the example.

## 3. Encoding Signature String
The generated signature string cannot be directly used as a request parameter, and needs to be encoded with URL encoding.
For example, the signature string generated in the previous step is: NSI3UqqD99b/UJb4tbG/xZpRW64=. When encoded, it should be: NSI3UqqD99b%2FUJb4tbG%2FxZpRW64%3D. The resulting signature string request parameter (Signature) is NSI3UqqD99b%2FUJb4tbG%2FxZpRW64%3D, which will be used to generate the final request URL.
**Note: If the user used GET method, all request parameters need to be encoded with URL encoding. Some language libraries will automatically encode URLs. Reduplicate encoding will cause signature authentication to fail.**

## 4. Authentication Failure
The following table lists possible errors when authentication fails:

| Error code | Error type | Error description |
|---------|---------|---------|
| 4100 | Authentication failed | Signature verification failed. Please make sure that the Signature in the request parameter is calculated correctly. This may also be caused by incorrect private key status, make sure the API key is valid and is not disabled. |
| 4101 | Not authorized by the developer to access this API | The sub user is not authorized to call the API. Please contact the developer for authorization. For details, refer to [Authorization Policy](/doc/product/378/4513). |
| 4102 | Not authorized by the developer to access the resources operated by the API | The user is not authorized by the developer to access some of the resources among the resource parameters. Please check the message field for the ID of resources that you're not authorized to access. 
Please contact the developer for authorization. For details, refer to [Authorization Policy](/doc/product/378/4513). |
| 4103 | The API is currently not available for SecretId of a non-developer | The sub-user with this SecretID cannot call this API. Only the developer is authorized to call this API. |
