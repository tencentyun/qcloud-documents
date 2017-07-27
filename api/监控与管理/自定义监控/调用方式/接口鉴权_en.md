Tencent Cloud APIs use signature for authentication. Each request should contain signature information to authenticate user's identity.

Before calling the Cloud API for the first time, you need to apply for a security credential on the Tencent Cloud console. A security credential consists of a SecretId, which is used to identify an API caller, and a SecretKey, which is used to encrypt the signature string and verify the signature string on the server. SecretKey must be kept confidential to avoid leakage. Users who already have security credential can start from generating signature strings.

## 1. Apply for Security Credential
Before using Cloud APIs for the first time, you need to apply for security credential.

1) Log in to the [Tencent Cloud Console](https://console.qcloud.com/).

2) Click "Cloud Products", and then select "Cloud API Key" under "Monitor & Management" to access the Cloud API key management page.
![](//mccdn.qcloud.com/img568f5fb824757.png)

3) On the [Cloud API Key Management] (https://console.qcloud.com/capi) page, click "New" to create a SecretId. Each account can create two SecretIds at most.

## 2. Generate Signature String
Suppose the SecretId and SecretKey got from the last step are:
>  SecretId:  AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
>  SecretKey:  Gu5t9xGARNpq86cd98joQYCN3Cozk1qA

Take querying CVM instance list as an example, the request parameters are as follows:

| Parameter | Parameter Format | 
|---------|---------|
| Method name | Action=DescribeInstances | 
| SecretId | SecretId= AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA | 
| Current time stamp | Timestamp=1408704141 | 
| A random positive integer | Nonce=345122 | 
| Region | Region=gz | 
| Instance ID of the first machine to be queried | instanceIds.0=qcvm12345 | 
| Instance ID of the second machine to be queried | instanceIds.1=qcvm56789 | 


The steps for generating API signature are as follows:
### 2.1. Sort Parameters
Sort the request parameters in an ascending lexicographical order by their names (such as using the ksort function in PHP), and the result is as follows:

```
{
    'Action' : 'DescribeInstances',
    'Nonce' : 345122,
    'Region' : 'gz',
    'SecretId' : 'AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA',
    'Timestamp' : 1408704141
    'instanceIds.0' : 'qcvm12345',
    'instanceIds.1' : 'qcvm56789',
}
```

### 2.2. Construct Request String
Format the above sorted request parameters as k=v, and then joint them with "&". Please note that v is the original value, instead of URL encoded value. Result:

```
Action=DescribeInstances&Nonce=345122&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1408704141& instanceIds.0=qcvm12345&instanceIds.1=qcvm56789
```

### 2.3. Construct Original Signature String
The following parameters are needed for constructing original signature string:

1) Request method:  The POST and GET methods are supported. In this case, a GET request is used. Please note that the methods must be all in uppercase.
2) Request CVM:  cvm.api.qcloud.com. Domain names varies depending on the module to which the API belongs. For more information, please see the descriptions of each API
3) Request path:  /v2/index.php
4) Request string:  This is the request string generated in the previous 2 steps.

Construction rule of original signature:
> Request Method + Request CVM + Request Path + ? + Request String

The resulting string is:

```
GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances&Nonce= 345122&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1408704141
```

### 2.4. Generate Signature String
1) Sign the**original signature string**obtained in the previous step using HMAC-SHA1 algorithm.

2) Encode the signature string using Base64 to obtain the final signature string.

For example, the code is as follows if written in PHP:

```
$secretKey = 'Gu5t9xGARNpq86cd98joQYCN3Cozk1qA';
$srcStr = 'GETcvm.api.qcloud.com/v2/index.php?Action=DescribeInstances&Nonce=345122&Region=gz&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA&Timestamp=1408704141';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $secretKey, true));
echo $signStr;
```

The resulting signature string is as follows:

```
HgIYOPcx5lN6gz8JsCFBNAWp2oQ=
```

When another programming language is used, you can perform the signature verification using the original signature in the above example. If the resulting signature string is identical to the one in the example, it is considered to pass the verification.

### 2.5. Add Signature and Send Request
1) Add Signature parameter, which is the **signature string** generated in last step, to the request parameter and convert the signature to a URL-encoded one. The signature generated above is HgIYOPcx5lN6gz8JsCFBNAWp2oQ=. After being encoded, it is converted to HgIYOPcx5lN6gz8JsCFBNAWp2oQ%3D.

2) If GET method is used, all the request parameters need to be URL-encoded; if POST method is used, URL encoding is only needed for Signature parameter.
  
3) Send HTTPS protocol request to obtain the returned value of API in JSON string format.

The final request URL is as follows:

```
https://cvm.api.qcloud.com/v2/index.php?Action=DescribeInstances
&Nonce=345122
&Region=gz
&SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
&Signature=HgIYOPcx5lN6gz8JsCFBNAWp2oQ%3D
&Timestamp=1408704141
&instanceIds.0=qcvm12345
&instanceIds.1=qcvm56789 
```
