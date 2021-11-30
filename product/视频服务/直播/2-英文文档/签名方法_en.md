The Tencent Cloud API authenticates each access request. Each request is required to include the Signature in its common request parameters for user authentication. The Signature is generated with the user's security credential that consists of a SecretId and a SecretKey. Users who have no security credential can apply for one on Tencent Cloud official website. Otherwise, the Cloud API cannot be called.

## 1. Apply for Security Credential
Before calling the Cloud API for the first time, user needs to apply for a security credential on the Tencent Cloud console. A security credential consists of a SecretId, which is used to identify an API caller, and a SecretKey, which is used to encrypt the signature string and verify its key on the server. Users must keep their SecretKeys private to avoid disclosure.

Apply for a security credential by following the steps below:

1) Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/).

2) Click "Cloud Products", and select "Cloud API Key" under "Monitor and Management" to access the Cloud API key management page.
![](//mccdn.qcloud.com/img568f5fb824757.png)

3) On the [Cloud API Key Management](https://console.cloud.tencent.com/capi) page, click "New" to create a pair of SecretId/SecretKey. Each account can have two pairs of SecretId/SecretKey at most.

## 2. Generate Signature String
With the SecretId and SecretKey, a signature string can be generated. For details on how to generate a signature string, see below:

Suppose that you have the following SecretId and SecretKey:
>  SecretId: AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
>  SecretKey: Gu5t9xGARNpq86cd98joQYCN3Cozk1qA

**Note: This is just an example. You need to proceed with your actual SecretId and SecretKey.**
Take [View Instance List](/doc/api/229/查看实例列表) (DescribeInstances) as an example. The possible request parameters are as follows when this API is called:

| Parameter Name | Description| Parameter Value| 
|---------|---------|---------|
| Action | Method name | DescribeInstances | 
| SecretId | Key ID | AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA | 
| Timestamp | Current timestamp | 1465185768 | 
| Nonce | A random positive integer | 11886 | 
| Region | Region where the instance resides in | gz | 
| instanceIds.0 | ID of the instance to be queried | ins-09dx96dg | 
| offset | Offset value | 0 | 
| limit | Maximum output allowed | 20 | 

According to the above table, among the request parameters, there are only 5 common request parameters (Action, SecretId, Timestamp, Nonce and Region), instead of 6 ones as described in "Common Request Parameters". Actually, Signature (the sixth one) is generated from other parameters (including the instruction request parameters) using the following procedure:
### 2.1. Sort Parameters
First, sort all the request parameters in an ascending lexicographical order by their names, just like sorting words in a dictionary in ascending alphabetical order or numerical order. That is to say, sort the parameters by their first letters, then by their second letters if their first letters are the same, and so on. You can complete the sorting process using relevant sorting functions in programming language, such as the ksort function in PHP. The sorting result of the above sample parameters is as follows:

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
When another programming language is used, you can sort the parameters in the above example. If the resulting signature string is identical to the one in the example, it is considered to pass the verification.
### 2.2. Construct Request String
This step is used to generate request string.
Format the above sorted request parameters as "parameter name"="parameter value". Take the parameter "Action" as an example. If the parameter value is "DescribeInstances", the resulting format is "Action=DescribeInstances".
**Note: 1. "Parameter value" is the original value instead of URL encoded value. 2. If an input parameter contains an underscore"_", you need to convert it to ".".**

Then, join the formatted parameters together using "&" to generate the final request string:

```
Action=DescribeInstances&Nonce=11886&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1465185768&instanceIds.0=ins-09dx96dg&limit=20&offset=0
```

### 2.3. Construct Original Signature String
This step is used to generate the original signature string.
The original signature string is composed of the following parameters:

1) Request method: The POST and GET methods are supported. In this case, a GET request is used. Please note that the methods must be all in uppercase.
2) Request CVM: The request domain name in [Query Instance List](/doc/api/229/查看实例列表) (DescribeInstances) is cvm.api.qcloud.com. The actual request domain name varies with the module an API belongs to. For more information, please see the corresponding API description.
3) Request path: The request path of the Cloud API is always /v2/index.php.
4) Request string: Indicates the request string generated in the previous step.

Construction rule of original signature string:
> Request Method + Request CVM + Request Path + ? + Request String

The resulting string is:

```
GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances&Nonce=11886&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1465185768&instanceIds.0=ins-09dx96dg&limit=20&offset=0
```

### 2.4. Generate Signature String
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

## 3. Encode Signature String
The generated signature string cannot be directly used as a request parameter, and needs to be encoded with URL encoding.
**Note: If the GET method is used, all the request parameters need to be URL encoded.**
For example, the signature string generated as described above is: NSI3UqqD99b/UJb4tbG/xZpRW64=. After being encoded, it should be: NSI3UqqD99b%2FUJb4tbG%2FxZpRW64%3D after encoded. The resulting signature string request parameter (Signature) is NSI3UqqD99b%2FUJb4tbG%2FxZpRW64%3D, which is used to generate the final request URL.

