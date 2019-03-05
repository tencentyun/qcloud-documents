The Tencent Cloud API authenticates each access request. Each request is required to include the Signature in its common request parameters for user authentication. The Signature is generated with the user's security credentials that consists of a SecretId and a SecretKey. Users who have no security credentials can apply for one on Tencent Cloud official website. Otherwise, the Cloud API cannot be called.

## 1. Applying for security credentials

Before calling the Cloud API for the first time, user needs to apply for security credentials on the Tencent Cloud console. Security credentials consist of a SecretId, which is used to identify an API caller, and a SecretKey, which is used to encrypt the signature string and verify its key on the server. Users must keep their SecretKeys private to avoid disclosure.

The steps to apply for security credentials are as below:

1) Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/).

2) Click "Cloud Products", and choose "Cloud API Key" under "Monitor & Management" to access the Cloud API key management page.

![](https://mccdn.qcloud.com/static/img/d9ee6db6ea3736d5aa04b9f161242b27/image.jpg)

3) Click "New Key" to create a pair of SecretId/SecretKey. Each account can have two pairs of SecretId/SecretKey at most.
![](https://mccdn.qcloud.com/static/img/939bf79efcc5b8da20e529b0640884d7/image.jpg)

## 2. Generating signature string

With the SecretId and SecretKey, a signature string can be generated. The procedure to generate a signature is as below:

Suppose that your SecretId and SecretKey are respectively:

>SecretId: AKIDT8G5AsY1D3MChWooNq1rFSw1fyBVCX9D
>SecretKey: pxPgRWDbCy86ZYyqBTDk7WmeRZSmPco0

**Note: This is just an example. You need to proceed with your actual SecretId and SecretKey.**
Take [Query Domain Information](https://cloud.tencent.com/document/product/228/3937) request as an example. When you call the API, the request parameters are as follows:

| Parameter Name | Description| Parameter Value |
| --------------- | ------ | ------------------------------------ |
| Action | Method name | DescribeCdnHosts |
| SecretId | Key ID | AKIDT8G5AsY1D3MChWooNq1rFSw1fyBVCX9D |
| Timestamp | Current timestamp | 1463122059 |
| Nonce | Random positive integer | 13029 |
| SignatureMethod | Siganature method | Default string: HmacSHA256 |
| offset | Offset value | 0 |
| limit | Number of output values for query | 10 |

According to the above table, among the request parameters, there are only 5 common request parameters - Action, SecretId, Timestamp, Nonce and SignatureMethod (specific to SHA256) - instead of 6 ones as described in "Common Request Parameters". Actually, Region is not mandatory for CDN, and Signature (the sixth one) is generated from other parameters (including the instruction request parameters) using the following procedure:

### 2.1 Sorting parameters

First, sort all of the request parameters in ascending lexicographical order by their names, just like sorting words in a dictionary in ascending alphabetical order or numerical order. That is to say, sort the parameters by their first letters, and then sort the parameters with the same first letter by their second letters, and so on. You can complete the sorting with the relevant sorting functions in programming language, such as the ksort function in PHP. The sorting result of the above sample parameters is as follows:

```
{
    'Action' : 'DescribeCdnHosts',
    'Nonce' : 48059,
    'SecretId' : 'AKIDT8G5AsY1D3MChWooNq1rFSw1fyBVCX9D',
    'Timestamp' : 1502197934,
    'SignatureMethod':'HmacSHA256',
    'limit' : 10,
    'offset' : 0
}
```

Any other programming language can be used to sort these parameters as long as the same result is produced.

### 2.2 Generating request string

This step is used to generate request string.
Format the above sorted parameters as "parameter name=parameter value". Take the parameter "Action" as an example, the formatting result will be "Action=DescribeCdnHosts".

**Note: 1. The parameter value is the original value, instead of a URL encoded value. 2. Any underscore in the input parameters needs to be converted to ".".**

Then, join the formatted parameters together using "&" to generate the final request string:

```
Action=DescribeCdnHosts&Nonce=48059&SecretId=AKIDT8G5AsY1D3MChWooNq1rFSw1fyBVCX9D&SignatureMethod=HmacSHA256&Timestamp=1502197934&limit=10&offset=0
```

### 2.3. Generating original signature string

This step is used to generate the original signature string.
The original signature string is composed of the following parameters: 

1) Request method: The POST and GET methods are supported. In this case, a GET request is used. Note that the methods must be in upper-case.
2) Request server: The request domain name for "Viewing Domain Name" (DescribeCdnHosts) is cdn.api.qcloud.com. The actual request domain name varies with the module to which the API belongs. For more information, please see the relevant API description.
3) Request path: The request path for cloud APIs is always /v2/index.php.
4) Request string: The request string generated in the previous step.

Construction rule of original signature string:

> Request Method + Request Server + Request Path + ? + Request String

For a GET request, the resulting string in the example is:

```
GETcdn.api.qcloud.com/v2/index.php?Action=DescribeCdnHosts&Nonce=48059&SecretId=AKIDT8G5AsY1D3MChWooNq1rFSw1fyBVCX9D&SignatureMethod=HmacSHA256&Timestamp=1502197934&limit=10&offset=0
```

For a POST request, the resulting string in the example is:

```
POSTcdn.api.qcloud.com/v2/index.php?Action=DescribeCdnHosts&Nonce=48059&SecretId=AKIDT8G5AsY1D3MChWooNq1rFSw1fyBVCX9D&SignatureMethod=HmacSHA256&Timestamp=1502197934&limit=10&offset=0
```


### 2.4 Generating signature string

This step is used to generate a signature string.
Sign the**original signature string**obtained in the previous step using HMAC-SHA256 algorithm, and then encode the signature string using Base64 to obtain the final signature string.

For example, the codes are as follows if written in PHP:

```
$secretKey = 'pxPgRWDbCy86ZYyqBTDk7WmeRZSmPco0';
$srcStr = 'GETcdn.api.qcloud.com/v2/index.php?Action=DescribeCdnHosts&Nonce=48059&SecretId=AKIDT8G5AsY1D3MChWooNq1rFSw1fyBVCX9D&SignatureMethod=HmacSHA256&Timestamp=1502197934&limit=10&offset=0';
$signStr = base64_encode(hash_hmac('sha256', $srcStr, $secretKey, true));
echo $signStr
```

The final signature string is as follows:

```
b/HlnO7vWEtR/kf21BvF0fX4vGmIThwWxlaD5GQtlSM=
```

When another programming language is used, you can perform the signature verification using the original signature in the above example. If the resulting signature string is identical to the one in the example, it is considered to pass the verification.

## 3. Encoding signature string

The generated signature string cannot be directly used as a request parameter, and needs to be encoded with URL encoding.
Note: If the GET method is used, all request parameters need to be encoded with URL encoding.
For example, the signature string generated as described above is:

> b/HlnO7vWEtR/kf21BvF0fX4vGmIThwWxlaD5GQtlSM=

After encoded, it should be:
> b%2FHlnO7vWEtR%2Fkf21BvF0fX4vGmIThwWxlaD5GQtlSM%3D

The resulting signature string request parameter (Signature) is b%2FHlnO7vWEtR%2Fkf21BvF0fX4vGmIThwWxlaD5GQtlSM%3D, which will be used to generate the final request URL.

**Note: Some language libraries encode URLs automatically. Repeated encoding can cause the failure of signature verification.**



















