Tencent Cloud API performs identity authentication on each access request, so each request is required to include signature in the common request parameters for user authentication.
Signature is generated from security credential, which includes SecretId and SecretKey. If you do not have security credential yet, go to [Cloud API Key Page] (https://console.cloud.tencent.com/capi) to apply for it. Otherwise, you can not call Cloud APIs.

## 1. Apply for security credential
Before using Cloud APIs for the first time, go to the [Cloud API Key](https://console.cloud.tencent.com/capi) page to apply for a security credential.
Security credential consists of a SecretId and a SecretKey, where:
> SecretId is used to identify the API caller;
> SecretKey is a key used to encrypt signature string, and is also used by the server to verify the signature string.
> <font color='red'> The security credential must be kept confidential to avoid leakage. </font>

Apply for a security credential by following the steps below:

1) Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/).

2) Go to the console page of [Cloud API Key](https://console.cloud.tencent.com/capi).
![](//mccdn.qcloud.com/img568f5fb824757.png)

3) On the [Cloud API Key](https://console.cloud.tencent.com/capi) page, click "New" to create a pair of SecretId/SecretKey.

> <font color='red'>A developer account can have two pairs of SecretId/SecretKey at most.</br>
> QQ accounts that are added as sub-users by a developer can apply for different security credentials on different developer consoles.</br>
> Currently, the security credential of a sub-user can only be used to call the cloud APIs of CDN.</font>


## 2. Generate signature string
With the SecretId and SecretKey, a signature string can be generated. The following describes how to generate a signature string:

Suppose that you have the following SecretId and SecretKey:
>  SecretId: AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
>  SecretKey: Gu5t9xGARNpq86cd98joQYCN3Cozk1qA

**Note: This is just an example. Please perform subsequent operations based on your actual SecretId and SecretKey.**

Take [View CVM Instance List](/doc/api/229/查看实例列表) (DescribeInstances) as an example. When this API is called, the request parameters may be as follows:

| Parameter Name | Description| Parameter Value| 
|---------|---------|---------|
| Action | Method name | DescribeInstances | 
| SecretId | Key ID | AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA | 
| Timestamp | Current time stamp | 1465185768 | 
| Nonce | A random positive integer | 11886 | 
| Region | Region where the instance resides in | gz | 
| instanceIds.0 | ID of the instance to be queried | ins-09dx96dg | 
| offset | Offset value | 0 | 
| limit | Maximum number of output results | 20 | 

According to the above table, among the request parameters, there are only 5 common request parameters (Action, SecretId, Timestamp, Nonce and Region), instead of 6 ones as described in "Common Request Parameters". Actually, Signature (the sixth one) is generated from other parameters (including the instruction request parameters) using the following procedure:
### 2.1. Sort parameters
First, sort all the request parameters in ascending lexicographical order by their names, just like sorting words in a dictionary in ascending alphabetical order or numerical order. That is to say, sort the parameters by their first letters, and then sort the parameters with the same first letter by their second letters, and so on. You can complete the sorting with the relevant sorting functions in programming language, such as the ksort function in PHP. The sorting result of the above sample parameters is as follows:

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
### 2.2. Construct request string
This step is used to generate request string.
Format the above sorted request parameters as "parameter name"="parameter value". Take the parameter "Action" as an example. If the parameter value is "DescribeInstances", the resulting format is "Action=DescribeInstances".
**Note: 1. The parameter value is the original value, instead of a URL encoded value. 2. Any underscore in the input parameters needs to be converted to ".".**

Then, join the formatted parameters together using "&" to generate the final request string:

```
Action=DescribeInstances&Nonce=11886&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1465185768&instanceIds.0=ins-09dx96dg&limit=20&offset=0
```

### 2.3. Construct original signature string
This step is used to generate the original signature string.
The original signature string is composed of the following parameters:

1) Request method: The POST and GET methods are supported. In this case, a GET request is used. Please note that the methods must be in upper-case.
2) Request CVM server: The request domain name for [View Instance List](/doc/api/229/查看实例列表) (DescribeInstances) is cvm.api.qcloud.com. The actual request domain name varies with the module to which the API belongs. For more information, please see the relevant API description.
3) Request path: The request path of Cloud APIs is always /v2/index.php.
4) Request string: The request string generated in the previous step.

Construction rule of original signature string:
> Request Method + Request CVM Server + Request Path + ? + Request String

The resulting string is:

```
GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances&Nonce=11886&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1465185768&instanceIds.0=ins-09dx96dg&limit=20&offset=0
```

### 2.4. Generate signature string
This step is used to generate a signature string.
Sign the **original signature string** obtained in the previous step using HMAC-SHA1 algorithm, and then encode the signature string using Base64 to obtain the final signature string.

For example, the code is as follows if written in PHP:

```
$secretKey = 'Gu5t9xGARNpq86cd98joQYCN3Cozk1qA';
$srcStr = 'GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances&Nonce=11886&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1465185768&instanceIds.0=ins-09dx96dg&limit=20&offset=0';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $secretKey, true));
echo $signStr;
```

The resulting signature string is as follows:

```
NSI3UqqD99b/UJb4tbG/xZpRW64=
```

When another programming language is used, you can perform the signature verification using the original signature in the above example. If the resulting signature string is identical to the one in the example, it is considered to pass the verification.

## 3. Encode signature string
The generated signature string cannot be directly used as a request parameter, and needs to be encoded with URL encoding.
**Note: If the GET method is used, all the request parameters need to be URL encoded.**
For example, if the signature string generated in the previous step is NSI3UqqD99b/UJb4tbG/xZpRW64=, it is converted to NSI3UqqD99b%2FUJb4tbG%2FxZpRW64%3D after being encoded. Therefore, the resulting signature string request parameter (Signature) is NSI3UqqD99b%2FUJb4tbG%2FxZpRW64%3D, which will be used to generate the final request URL.

## 4. Authentication failure
The following authentication error codes may be returned depending on the actual situation.

| Error Code | Error Type | Error Description |
|---------|---------|---------|
| 4100 | Authentication failed.| Key is invalid or is disabled.|
| 4101 | Authentication failed | The SecretID is not authorized to call this API. Please contact the developer for authorization. For more information, please see [Authorization Policy](/doc/product/378/4513).|
| 4102 | Authentication failed | A resource that you're not authorized to access by the developer exists in the requested resources. Check the message field for the resource ID that you have no permission to view. </br> Please contact the developer for authorization. For more information, please see [Authorization Policy](/doc/product/378/4513) |
| 4103 | Authentication failed | This API is currently unavailable for the SecretId of a sub-user. Only the developer is allowed to call this API.




