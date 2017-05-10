Tencent Cloud API will perform identity authentication on each access request, so each request is required to include signature information in the common request parameters for user authentication. The Signature is generated with the user's security credential, which consists of a SecretId and a SecretKey. Users with no security credential can apply for a credential from the Tencent Cloud official website. Otherwise they will not be able to call Cloud APIs.

## 1. Applying for Security Credential
Before using the Cloud API for the first time, a user needs to apply for a security credential in the Tencent Cloud CVM console. A security credential consists of a SecretId, which identifies the API caller, and a SecretKey, which is used to encrypt the signature string and verify the signature string on the server. Users must strictly keep their SecretKeys confidential to avoid disclosure.

To apply for a security credential, please proceed as follows:

1) Log in to the [Tencent Cloud Console](https://console.qcloud.com/).

2) Click "Cloud Products", and select "Cloud API Key" under "Monitor & Management" to access the Cloud API key management page.
![](//mccdn.qcloud.com/img568f5fb824757.png)

3) On the [Cloud API Key Management](https://console.qcloud.com/capi) page, click "New Key" to create a pair of SecretId/SecretKey. Each account can have two pairs of SecretId/SecretKey at most.

## 2. Generating Signature String
With the SecretId and SecretKey, a signature string can be generated. The following is the detailed process for generating a signature string.

If a user has the following SecretId and SecretKey:
>  SecretId: AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
>  SecretKey: Gu5t9xGARNpq86cd98joQYCN3Cozk1qA

**Note: This is just an example. Please proceed with your actual SecretId and SecretKey!**
Take the [Bind EIP to CPM]()(EipBmBindRs) request as an example. The possible request parameters are as follows when this API is called:

| Parameter name | Description| Parameter Value| 
|---------|---------|---------|
| Action | Method name | DescribeInstances | 
| SecretId | Key ID | AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA | 
| Timestamp | Current timestamp | 1465185768 | 
| Nonce | Random positive integer | 11886 | 
| Region | Indicate the region where the instance is located | gz | 
| eipId | EIP instance ID | cpm-09dx96dg |
| instanceId | CPM instance ID | eip-testcpm |

According to the above table, among the request parameters, there are only 5 common request parameters (Action, SecretId, Timestamp, Nonce and Region), instead of 6 ones as described in "Common Request Parameters". Actually, Signature (the sixth one) is generated from other parameters (including the instruction request parameters) using the following procedure:
### 2.1. Sorting Parameters
First, sort all the request parameters in an ascending lexicographical order by their names, just like sorting words in a dictionary in ascending alphabetical order or numerical order. That is to say, sort the parameters by their first letters, then by their second letters if their first letters are the same, and so on. You can complete the sorting process using relevant sorting functions in programming language, such as the ksort function in PHP. The sorting result of the above sample parameters is as follows:

```
{
    'Action' : 'DescribeInstances',
    'Nonce' : 11886,
    'Region' : 'gz',
    'SecretId' : 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA',
    'Timestamp' : 1465185768,
    'eipId' : 'eip-testcpm',
	'instanceId' : 'cpm-09dx96dg',
}
```
Any other programming language can be used to sort these parameters as long as the same result is produced.
### 2.2. Generating Request String
This step is used to generate a request string.
Format the above sorted request parameters as "parameter name"="parameter value". Take the parameter "Action" as an example. If the parameter value is "EipBmBindRs", the resulting format will be "Action=EipBmBindRs".
**Note: 1. "Parameter value" is the original value instead of url encoded value. 2. If an input parameter contains an underscore"_", you need to convert it to ".".**

Then, joint the formatted parameters together using "&" to generate the final request string:

```
Action=DescribeInstances&Nonce=11886&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1465185768&instanceId=cpm-09dx96dg&eipId=eip-testcpm
```

### 2.3. Generating Original Signature String
This step is used to generate an original signature string.
The original signature string is composed of the following parameters:

1) Request method: The POST and GET methods are supported. In this case, a GET request is used. Note that the methods must be all in uppercase.
2) Request CVM: The request domain for API [Bind EIP to CPM]()(EipBmBindRs) is eip.api.qcloud.com. The actual request domain varies depending on the module to which the API belongs. For more information, please see descriptions of APIs.
3) Request path: The request path of Cloud API is always /v2/index.php.
4) Request string: This is the request string generated in the previous step.

Combination rule of original signature string:
> Request Method + Request CVM + Request Path + ? + Request String

The combination result is as follows:

```
GETeip.api.qcloud.com/v2/index.php?Action=DescribeInstances&Nonce=11886&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1465185768&instanceId=cpm-09dx96dg&eipId=eip-testcpm
```

### 2.4. Generating Signature String
This step is used to generate a signature string.
Sign the **original signature string** obtained in the previous step using HMAC-SHA1 algorithm, and then encode the signature string using Base64 to obtain the final signature string.

For example, the codes are as follows if written in PHP:

```
$secretKey = 'Gu5t9xGARNpq86cd98joQYCN3Cozk1qA';
$srcStr = 'GETeip.api.qcloud.com/v2/index.php?Action=DescribeInstances&Nonce=11886&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1465185768&instanceId=cpm-09dx96dg&eipId=eip-testcpm';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $secretKey, true));
echo $signStr;
```

The final signature string is as follows:

```
NSI3UqqD99b/UJb4tbG/xZpRW64=
```

When another programming language is used, you can perform the signature verification using the original signature string in the above example. If the resulting signature string is identical to the one in the example, it is considered to pass the verification.

## 3. Encoding Signature String
The generated signature string cannot be directly used as a request parameter, and needs to be encoded with URL encoding.
**Note: If the GET method is used, all request parameters need to be encoded with URL encoding.**
For example, the signature string generated as described above is: NSI3UqqD99b/UJb4tbG/xZpRW64=. After encoded, it should be: NSI3UqqD99b%2FUJb4tbG%2FxZpRW64%3D. The resulting signature string request parameter (Signature) is NSI3UqqD99b%2FUJb4tbG%2FxZpRW64%3D, which will be used to generate the final request URL.

