Tencent Cloud API authenticates each access request, so each request is required to include signature information in the common request parameters for user authentication.
The signature is generated with user's security credentials, which consist of a SecretId and a SecretKey. If you don't have security credentials, apply for the credentials on the [Cloud API Key](https://console.cloud.tencent.com/capi) page. Otherwise, you will not be able to call the cloud APIs.

## 1. Apply for Security Credentials
Before using Tencent Cloud's APIs for the first time, you need to apply for security credentials on the [Cloud API Key](https://console.cloud.tencent.com/capi) page.
Security credentials consist of a SecretId and a SecretKey.
> SecretId is used to identify the API caller.
> SecretKey is a key used for signature string encryption and signature string verification by the server.
> The security credential must be kept confidential to avoid leakage.

Apply for security credentials by following the steps below:

(1) Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/).

(2) Go to the [Cloud API Key](https://console.cloud.tencent.com/capi) page on the console.

(3) On the [Cloud API Key](https://console.cloud.tencent.com/capi) page, click **New** to create a pair of SecretId/SecretKey.

> A developer account can have two pairs of SecretId/SecretKey at most.



## 2. Generate the Signature String

With the SecretId and SecretKey, a signature string can be generated. The following describes how to generate a signature string:

Suppose that you have the following SecretId and SecretKey:
>  SecretId: AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE
>  SecretKey: Gu5t9xGARNpq86cd98joQYCN3EXAMPLE

**Note: This information is only for demonstration purpose. Make sure you proceed with your actual SecretId and SecretKey.**

Take "View CVM Instance List" (DescribeInstances) as an example. When you call the API, the request parameters are as follows:

| Parameter Name | Description | Parameter Value |
|---------|---------|---------|
| Action | Method name |  DescribeInstances |
| SecretId | Key ID |  AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE |
| Timestamp | Current timestamp |  1465185768 |
| Nonce | A random positive integer |  11886 |
| Region | The region where the instance resides |  ap-guangzhou |
| InstanceIds.0 | ID of the instance to be queried |  ins-09dx96dg |
| Offset | Offset |  0 |
| Limit | Maximum number of output results |  20 |
| Version | API version |  2017-03-12 |


### 2.1 Sort parameters

First, sort all the request parameters in an ascending lexicographical order by their names. This is like sorting words in a dictionary in an ascending alphabetical order or numerical order. That is to say, sort the parameters by their first letters, then by their second letters if their first letters are the same, and so on. You can complete the sorting process using relevant sorting functions in the programming language, such as the ksort function in PHP. The parameters in the example are sorted as follows:

```
{
    'Action' : 'DescribeInstances',
    'InstanceIds.0' : 'ins-09dx96dg',
    'Limit' : 20,
    'Nonce' : 11886,
    'Offset' : 0,
    'Region' : 'ap-guangzhou',
    'SecretId' : 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE',
    'Timestamp' : 1465185768,
    'Version': '2017-03-12',
}
```
Any other programming language can be used to sort these parameters as long as the same result is produced.

### 2.2 Construct the request string

This step is used to generate the request string.
Format the request parameters sorted in the previous step as "parameter name"="parameter value". For example, if the parameter value of "Action" is "DescribeInstances", the resulting format is Action=DescribeInstances.
**Note: "Parameter value" is the original value, instead of URL encoded value.**

Then, join the formatted parameters together using "&" to generate the final request string:

```
Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE&Timestamp=1465185768&Version=2017-03-12
```

### 2.3. Construct the original signature string
This step is used to generate the original signature string.
The original signature string is composed of the following parameters:

(1) Request method: The POST and GET methods are supported. In this case, a GET request is used. The methods must be in uppercase.
(2) Request CVM: The request domain name for "View Instance List" (DescribeInstances) is cvm.tencentcloudapi.com. The actual request domain name varies with the module to which the API belongs. For more information, please see the relevant API description.
(3) Request path: The request path of the current version of cloud API is always /.
(4) Request string: The request string generated in the previous step.

The original signature string is constructed as follows:
> **Request method+Request CVM+Request path+?+Request string**

The resulting string is:

```
GETcvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE&Timestamp=1465185768&Version=2017-03-12
```

### 2.4. Generate the signature string
This step is to generate the signature string.
Sign the **original signature string** obtained in the previous step using HMAC-SHA1 algorithm, and then encode the signature string using Base64 to obtain the final signature string.

In this example, PHP language is used:

```
$secretKey = 'Gu5t9xGARNpq86cd98joQYCN3EXAMPLE';
$srcStr = 'GETcvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE&Timestamp=1465185768&Version=2017-03-12';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $secretKey, true));
echo $signStr;
```

The resulting signature string is as follows:

```
EliP9YW3pW28FpsEdkXt/+WcGeI=
```

If another programming language is used, the original signature string in the above example can be used for verification, as long as the signature string generated is the same as the one in the example.

## 3. Encode the Signature String
The generated signature string cannot be directly used as the request parameter, and needs to be URL encoded.
**Note: If GET method is used, all request parameters need to be URL encoded.**
For example, the signature string "EliP9YW3pW28FpsEdkXt/+WcGeI=" generated in the previous step is converted to the final signature string request parameter (Signature): "EliP9YW3pW28FpsEdkXt%2f%2bWcGeI%3d", which will be used to generate the final request URL.

## 4. Authentication Failure
The following authentication error codes may be returned depending on the actual situation.

| Error Code | Error Description |
|----------|---------|
| AuthFailure.SignatureExpire | Signature expired |
| AuthFailure.UnauthorizedOperation | Authorization via CAM failed for the request |
| AuthFailure.SecretIdNotFound | Key does not exist |
| AuthFailure.SignatureFailure | Invalid signature |
| AuthFailure.TokenFailure | token error |
| AuthFailure.MFAFailure | MFA error |
| AuthFailure.InvalidSecretId | Invalid key (it is not a cloud API key) |


