Tencent Cloud API performs identity authentication on each access request, so each request is required to include signature in the common request parameters for user authentication.
Signature is generated from security credential, which includes SecretId and SecretKey. If you do not have security credential yet, go to [Cloud API Key page](https://console.cloud.tencent.com/capi) to apply for it. Otherwise, you cannot call Cloud APIs.

## 1. Apply for a security credential
Before using Cloud APIs for the first time, go to the [Cloud API Key](https://console.cloud.tencent.com/capi) page to apply for a security credential.
Security credential consists of a SecretId and a SecretKey, where:
> SecretId is used to identify an API caller, and SecretKey is used to encrypt the signature string and verify its key on the server.<font color='red'>The security credential must be kept confidential to avoid leakage.</font>

Apply for a security credential by following the steps below:

(1) Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/).

(2) Go to the console page of [Cloud API Key](https://console.cloud.tencent.com/capi).

(3) On the [Cloud API Key](https://console.cloud.tencent.com/capi) page, click **Create** to create a pair of SecretId/SecretKey.

> <font color='red'>A developer account can have two pairs of SecretId/SecretKey at most.</font>



## 2. Generate signature string

With the SecretId and SecretKey, a signature string can be generated. The following describes how to generate a signature string:

Suppose that you have the following SecretId and SecretKey:
>  SecretId: AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE
>  SecretKey: Gu5t9xGARNpq86cd98joQYCN3EXAMPLE

**Note: This information is only for demonstration purposes. Please proceed with your actual SecretId and SecretKey.**

Take "View CVM Instance List" (DescribeInstances) as an example. The possible request parameters are as follows when this API is called:

| Parameter Name | Description| Parameter Value|
|---------|---------|---------|
| Action | Method name | DescribeInstances |
| SecretId | Key ID | AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE |
| Timestamp | Current time stamp | 1465185768 |
| Nonce | A random positive integer | 11886 |
| Region | The region where the instance resides | ap-guangzhou |
| InstanceIds.0 | ID of the instance to be queried | ins-09dx96dg |
| Offset | Offset value | 0 |
| Limit | Maximum number of output results | 20 |
| Version | API version | 2017-03-12 |


### 2.1. Sort parameters

First, sort all the request parameters in ascending lexicographical order by their names, just like sorting words in a dictionary in ascending alphabetical order or numerical order. That is to say, sort the parameters by their first letters, and then sort the parameters with the same first letter by their second letters, and so on. You can complete the sorting with the relevant sorting functions in programming language, such as the ksort function in PHP. The sorting result of the above sample parameters is as follows:

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

### 2.2. Generate request string

This step is used to generate the request string.
Format the above sorted request parameters as "parameter name"="parameter value". Take the parameter "Action" as an example. If the parameter value is "DescribeInstances", the resulting format is "Action=DescribeInstances".
**Note: "Parameter value" is the original value instead of URL encoded value.**

Then, join the formatted parameters together using "&" to generate the final request string:

```
Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE&Timestamp=1465185768&Version=2017-03-12
```

### 2.3. Generate original signature string
This step is used to generate the original signature string.
The original signature string is composed of the following parameters:

(1) Request method: The POST and GET methods are supported. In this case, a GET request is used. Please note that the methods must be in uppercase.
(2) Request server: The request domain name for View Instance List (DescribeInstances) is cvm.tencentcloudapi.com. The actual request domain name varies with the module to which the API belongs. For more information, please see the relevant API description.
(3) Request path: The request path of the current version of cloud API is always /.
(4) Request string: The request string generated in the previous step.

Construction rule of original signature string:
> Request Method + Request CVM Server + Request Path + ? + Request String

The resulting string is:

```
GETcvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE&Timestamp=1465185768&Version=2017-03-12
```

### 2.4. Generate signature string
This step is to generate the signature string.
Sign the **original signature string** obtained in the previous step using HMAC-SHA1 algorithm, and then encode the signature string using Base64 to obtain the final signature string.

For example, the code is as follows if written in PHP:

```
$secretKey = 'Gu5t9xGARNpq86cd98joQYCN3EXAMPLE';
$srcStr = 'GETcvm.tencentcloudapi.com/?Action=DescribeInstances&InstanceIds.0=ins-09dx96dg&Limit=20&Nonce=11886&Offset=0&Region=ap-guangzhou&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3EXAMPLE&Timestamp=1465185768&Version=2017-03-12';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $secretKey, true));
echo $signStr;
```

The resulting signature string is as follows:

```
v9MVG3fopp/gCsLSZ4gMFeYGgDU=
```

When another programming language is used, you can perform the signature verification using the original signature in the above example. If the resulting signature string is identical to the one in the example, it is considered to pass the verification.

## 3. Encode signature string
The generated signature string cannot be directly used as the request parameter, and needs to be URL encoded.
**Note: If the GET method is used, all request parameters need to be encoded with URL encoding.**
For example, the signature string generated in the previous step v9MVG3fopp/gCsLSZ4gMFeYGgDU= is converted to the final signature string request parameter (Signature): v9MVG3fopp%2fgCsLSZ4gMFeYGgDU%3d, which will be used to generate the final request URL.

## 4. Authentication failure
The following authentication error codes may be returned depending on the actual situation.

| Error Code | Error Description |
|----------|---------|
| AuthFailure.SignatureExpire | Signature expired |
| AuthFailure.UnauthorizedOperation | Authorization via CAM failed for the request |
| AuthFailure.SecretIdNotFound | Key does not exist |
| AuthFailure.SignatureFailure | Invalid signature |
| AuthFailure.TokenFailure | Invalid token |
| AuthFailure.MFAFailure | MFA failure |
| AuthFailure.InvalidSecretId | Invalid key (it is not a cloud API key) |


