Tencent Cloud API will authenticate each access request, so each request is required to include the signature information in the common request parameter for user authentication. The Signature is generated with the user's security credential, which consists of a SecretId and a SecretKey. Users who have no security credential can apply for a credential on the Tencent Cloud. Otherwise, the Cloud API cannot be called.

## 1. Applying for security credential

Before using the Cloud API for the first time, user needs to apply for a security credential on the Tencent Cloud CVM console. A security credential consists of a SecretId, which identifies the API caller, and a SecretKey, which is used to encrypt the signature string and verify the signature string on the server. Users must strictly keep their SecretKeys confidential to avoid disclosure.

To apply for a security credential, please proceed as follows:

1) Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/).

2) Click "Cloud Products", and choose "Cloud API Key" under "Monitor & Management" to access the Cloud API key management page.
![](//mccdn.qcloud.com/static/img/d9ee6db6ea3736d5aa04b9f161242b27/image.jpg)

3) Click "New Key" to create a pair of SecretId/SecretKey. Each account can have two pairs of SecretId/SecretKey at most.
![](//mccdn.qcloud.com/static/img/939bf79efcc5b8da20e529b0640884d7/image.jpg)

## 2. Generate a Signature String

With the Secret ID and Secret Key, signature string can be generated. The following is the detailed process for generating signature string.

Suppose that a user has the following SecretId and SecretKey:

>SecretId: AKIDT8G5AsY1D3MChWooNq1rFSw1fyBVCX9D
>SecretKey: pxPgRWDbCy86ZYyqBTDk7WmeRZSmPco0

**Note: This is just an example. Please proceed with your actual SecretId and SecretKey.**
Take [Query Domain Information](https://cloud.tencent.com/document/product/228/3937) request as an example. When the user calls the API, the request parameters are as follows:

| Parameter name | Description | Parameter Value |
| ------ | ---- | ---- |
| Action | Method name | DescribeCdnHosts |
| SecretId  | Key ID | AKIDT8G5AsY1D3MChWooNq1rFSw1fyBVCX9D  |
| Timestamp | Current timestamp | 1463122059 |
| Nonce | Random positive integer | 13029 |
| offset | Offset value | 0 |
| limit | Number of output values for query | 10 |

According to the above table, among the request parameters, there are only 4 common request parameters (Action, SecretId, Timestamp and Nonce), instead of 6 ones as described in "Common Request Parameters". Actually, Region is not mandatory for CDN, and Signature (the sixth one) is generated from other parameters (including the instruction request parameters) using the following procedure:

### 2.1. Sorting Parameters

First, sort all request parameters in ascending lexicographical order by their names, just like sorting words in a dictionary in ascending alphabetical order or numerical order. That is to say, sort the parameters by their first letters, and then sort the parameters with the same first letter by their second letters, and so on. You can complete the sorting with the relevant sorting functions in programming language, such as the ksort function in PHP. The sorting result of the above sample parameters is as follows:

```
{
    'Action' : 'DescribeCdnHosts',
    'Nonce' : 13029,
    'SecretId' : 'AKIDT8G5AsY1D3MChWooNq1rFSw1fyBVCX9D',
    'Timestamp' : 1463122059,
    'limit' : 10,
    'offset' : 0
}
```

Any other programming language can be used to sort these parameters as long as the same result is produced.

### 2.2. Joining request strings together

This step is used to generate a request string.
Format the above sorted parameters as "parameter name=parameter value". Take the parameter "Action" as an example, the resulting format will be "Action=DescribeCdnHosts".

** Note: 1. "Parameter value" is the original value instead of url encoded value. 2. If the input parameter contains an underscore"_", you need to convert it to ".". **

Then, joint the formatted parameters together using "&" generate the final request string:

```
Action=DescribeCdnHosts&Nonce=13029&SecretId=AKIDT8G5AsY1D3MChWooNq1rFSw1fyBVCX9D&Timestamp=1463122059&limit=10&offset=0
```

### 2.3. Generating original signature string

This step is used to generate the original signature string.
The original signature string is composed of the following parameters:

1) Request method: The POST and GET methods are supported. In this case, a GET request is used. Note that the methods must be in upper-case.
2) Request host: The request domain to view the domain information (DescribeCdnHosts) is: cdn.api.qcloud.com. The actual request domain varies depending on the module to which the API belongs. For more information, refer to descriptions of APIs.
3) Request path: The request path of Cloud API is always /v2/index.php.
4) Request string: Indicate the request string generated in the previous step.

Combination rule of original signature string:

> request method + request host +request path + ? + request string

For a GET request, the resulting string in the example is:

```
GETcdn.api.qcloud.com/v2/index.php?Action=DescribeCdnHosts&Nonce=13029&SecretId=AKIDT8G5AsY1D3MChWooNq1rFSw1fyBVCX9D&Timestamp=1463122059&limit=10&offset=0
```

For a POST request, the resulting string in the example is:

```
POSTcdn.api.qcloud.com/v2/index.php?Action=DescribeCdnHosts&Nonce=13029&SecretId=AKIDT8G5AsY1D3MChWooNq1rFSw1fyBVCX9D&Timestamp=1463122059&limit=10&offset=0
```


### 2.4. Generating Signature String

This step is used to generate a signature string.
Sign the original signature string obtained in the previous step using HMAC-SHA1 algorithm, and then encode the signature string using Base64 to obtain the final signature string.

For example, the codes are as follows if written in PHP:

```
$secretKey = 'pxPgRWDbCy86ZYyqBTDk7WmeRZSmPco0';
$srcStr = 'GETcdn.api.qcloud.com/v2/index.php?Action=DescribeCdnHosts&Nonce=13029&SecretId=AKIDT8G5AsY1D3MChWooNq1rFSw1fyBVCX9D&Timestamp=1463122059&limit=10&offset=0';
$signStr = base64_encode(hash_hmac('sha1', $srcStr, $secretKey, true));
echo $signStr
```

The final signature string is as follows:

```
bWMMAR1eFGjZ5KWbfxTlBiLiNLc=
```

For a POST request, the final signature result is:

```
i/KcLp6VaOtUmVtT0dqtLpKJOkg=
```

When other programming language are used, you can verify the final signature string using the above example, as long as the same signed string is produced.

## 3. Encode a Signature String

The generated signature string cannot be directly used as a request parameter, and needs to be URL encoded.
Note: If the GET method is used, all request parameters need to be encoded with URL encoding.
For example, the signature string generated as described above is:

> bWMMAR1eFGjZ5KWbfxTlBiLiNLc=

After encoded, it should be:
> bWMMAR1eFGjZ5KWbfxTlBiLiNLc%3D

The resulting signature string request parameter is bWMMAR1eFGjZ5KWbfxTlBiLiNLc%3D, which will be used to generate the final request URL.

**Note: Some language libraries will automatically encode URLs. Reduplicate encoding will cause signature authentication to fail.**



















