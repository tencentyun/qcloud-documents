Tencent Cloud API authenticates each access request, so each request is required to include the Signature in the common request parameters for user identity authentication. The signature is generated with user's security credentials, which consist of a SecretId and a SecretKey. If you don't have security credentials, apply for the credentials from the Tencent Cloud official website. Otherwise, you will not be able to call the cloud APIs.

## 1. Apply for Security Credentials
Before calling the Cloud API for the first time, user needs to apply for security credentials on the Tencent Cloud console. Security credentials consists of a SecretId, which is used to identify an API caller, and a SecretKey, which is used to encrypt the signature string and verify its key on the server. Users must keep their SecretKeys private to avoid disclosure.

Apply for security credentials by following the steps below:

(1) Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/).

(2) Click **Cloud Products**, and select **Cloud API Key** under **Monitor and Management** to go to the cloud API key management page.
![](//mccdn.qcloud.com/img568f5fb824757.png)

(3) On the [Cloud API Key Management](https://console.cloud.tencent.com/capi) page, click **New** to create a pair of SecretId/SecretKey. Each account can have two pairs of SecretId/SecretKey at most.

## 2. Generate the Signature String
With the SecretId and SecretKey, a signature string can be generated. The following shows how to generate a signature:

Suppose that you have the following SecretId and SecretKey:
>  SecretId: AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
>  SecretKey: Gu5t9xGARNpq86cd98joQYCN3Cozk1qA

**Note: This information is only for demonstration purpose. Make sure you proceed with your actual SecretId and SecretKey.**
Take [View Instance List](/doc/api/229/查看实例列表) (DescribeInstances) as an example. The possible request parameters are as follows when this API is called:

| Parameter Name | Description | Parameter Value | 
|---------|---------|---------|
| Action | Method name |  DescribeInstances | 
| SecretId | Key ID |  AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA | 
| Timestamp | Current timestamp |  1465185768 | 
| Nonce | A random positive integer |  11886 | 
| Region | The region where the instance resides |  gz | 
| instanceIds.0 | ID of the instance to be queried |  ins-09dx96dg | 
| offset | Offset | 0 | 
| limit | Maximum number of output results | 20 | 

According to the above table, among the request parameters, there are only 5 common request parameters (Action, SecretId, Timestamp, Nonce and Region), instead of 6 ones as described in "Common Request Parameters". Actually, Signature (the sixth one) is generated from other parameters (including the instruction request parameters) using the following procedure:
### 2.1. Sort parameters
First, sort all the request parameters in an ascending lexicographical order by their names, just like sorting words in a dictionary in ascending alphabetical order or numerical order. That is to say, sort the parameters by their first letters, then by their second letters if their first letters are the same, and so on. You can complete the sorting process using relevant sorting functions in programming language, such as the ksort function in PHP. The parameters in the example are sorted as follows:

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
### 2.2. Construct the request string
This step is used to generate the request string.
Format the request parameters sorted in the previous step as "parameter name"="parameter value". For example, if the parameter value of "Action" is "DescribeInstances", the resulting format is Action=DescribeInstances.
**Note: 1. "Parameter value" is the original value, instead of the URL encoded value. 2. Any underscore in the Key of input parameter needs to be replaced with ".".**

Then, join the formatted parameters together with "&" to generate the final request string:

```
Action=DescribeInstances&Nonce=11886&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1465185768&instanceIds.0=ins-09dx96dg&limit=20&offset=0
```

### 2.3. Construct the original signature string
This step is used to generate the original signature string.
The original signature string is composed of the following parameters:

(1) Request method: The POST and GET methods are supported. In this case, a GET request is used. The methods must be in upper-case.
(2) Request CVM: The request domain name for [View Instance List](/doc/api/229/查看实例列表) (DescribeInstances) is cvm.api.qcloud.com. The actual request domain name varies with the module to which the API belongs. For more information, please see the relevant API description.
(3) Request path: The request path of cloud API is always /v2/index.php.
(4) Request string: The request string generated in the previous step.

The original signature string is constructed as follows:
> Request Method + Request CVM + Request Path + ? + Request String

The resulting string is:

```
GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances&Nonce=11886&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1465185768&instanceIds.0=ins-09dx96dg&limit=20&offset=0
```

### 2.4. Generate the signature string
This step is to generate the signature string.
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

If another programming language is used, the original signature string in the above example can be used for verification, as long as the signature string generated is the same as the one in the example.

## 3. Encode the Signature String
The generated signature string cannot be directly used as the request parameter, and needs to be URL encoded.
**Note: If the GET method is used, all request parameters need to be encoded with URL encoding.**
For example, the signature string generated in the previous step NSI3UqqD99b/UJb4tbG/xZpRW64= is converted to NSI3UqqD99b%2FUJb4tbG%2FxZpRW64%3D after being encoded. The resulting request parameter for signature string (Signature) is NSI3UqqD99b%2FUJb4tbG%2FxZpRW64%3D, which will be used to generate the final request URL.

