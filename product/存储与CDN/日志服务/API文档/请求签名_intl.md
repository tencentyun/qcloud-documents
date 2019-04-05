## Preparations

1. Obtain SecretId and SecretKey.
    They are available on the [Cloud API Key](https://console.cloud.tencent.com/capi) page of the console.
2. Specify the development language:
     Supported languages include but not limisted to java, php, c sharp, c++, node.js, and python. You need to specify the HMAC-SHA1 function depending on development languages.

## Signature Content
The HTTP signature request initiated to CLS through the API is passed by using the standard HTTP Authorization header, as shown in the following example:
```
GET /logset?logset_id=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx HTTP/1.1
Host: ap-shanghai.cls.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDc9YlmrBcFk4C8sbmXQ8i65XXXXXXXXXX&q-sign-time=1510109254;1510109314&q-key-time=1510109254;1510109314&q-header-list=content-type;host&q-url-param-list=logset_name&q-signature=e8b23b818caf4e33f196f895218bdabdbd1f1423
```

The `Host` field in the request is ${region}.cls.myqcloud.com ("region" is replaced by the actual region of the CLS service), with the following ID:

```
ap-beijing - Beijing
ap-shanghai - Shanghai
ap-guangzhou - Guangzhou
ap-chengdu - Chengdu
```

The signature content in the request is comprised of a number of key-value pairs connected with "&". The format is as follows:

```
q-sign-algorithm=[Algorithm]&q-ak=[SecretId]&q-sign-time=[SignTime]&q-key-time=[KeyTime]&q-header-list=[SignedHeaderList]&q-url-param-list=[SignedParamList]&q-signature=[Signature]
```

### Key-Value Description

The key-value pairs (Key=Value) in the signature content are described as follows:



| Key | Value | Description |
| ---------------- | -------------------- | ---------------------------------------- |
| q-sign-algorithm | sha1 | Signature algorithm (required). Only sha1 is supported. |
| q-ak | Parameter [SecretId] | Account's SecretId (required). ID obtained from the console in the preparation above |
| q-sign-time | Parameter [SignTime] | Signature start and end time (required) which are unix timestamp in seconds and separated by ```;```. |
| q-key-time | Parameter [KeyTime] | It is required, and is the same as q-sign-time. |
| q-header-list | Parameter [SignedHeaderList] | The key (required) of the HTTP request header that needs adding a signature. The key must be converted to lowercase. Multiple keys must be sorted in lexicographic order and separated by ```;```. |
| q-url-param-list | Parameter [SignedParamList] | The parameter (required) of the Http request Uri that needs adding a signature. The keys must be converted to lowercase. Multiple keys must be sorted in lexicographic order and separated by ```;```. |
| q-signature | Parameter [Signature] | Calculated signature content (required) comprised of lowercase letters |

*Note: For q-sign-time and q-key-time, the end time must be later than the start time. Otherwise, the signature expires immediately.*

### Calculation Method

Signature calculation involves two steps:


1. Combine the related information of the Http request to the string HttpRequestInfo, according to a certain format.
2. Use the sha1 algorithm to calculate the hash value for HttpRequestInfo, and then combine the hash value with other specified parameters according to a certain format to generate the original string StringToSign.
3. Encrypt the q-key-time using the SecretKey to get the SignKey.
4. Encrypt the StringToSign using the SignKey to generate the Signature.


#### Combining HttpRequestInfo

HttpRequestInfo consists of Method, Uri, Headers, and Parameters in the HTTP request, as shown below:
```
HttpRequestInfo = Method + "\n"
                + Uri + "\n"
                + FormatedParameters + "\n"
                + FormatedHeaders + "\n"
```

```\n``` indicates a newline escape character, ```+``` indicates a string concatenation operation. The other parameters are defined as follows:



| Field Name | Description |
| ------------------ | ---------------------------------------- |
| Method | Method (in lowercase letters) used for HTTP requests, such as ```get, post``` |
| Uri | The name of resource of the HTTP request, excluding the query string, for example, ```/logset``` |
| FormatedParameters | The serialized string of parameters in the Http request's query string, namely the parameters specified in q-url-param-list. If no parameter is specified, an empty string is used. The key and the value are connected with ```=```. Different key-value pairs are connected with ```&```, and need to be sorted in lexicographical order. The key must be lowercase letters, and the value must be URL encoded. |
| FormatedHeaders | The header of Http request, namely the Http header specified in q-header-list. If no header is specified, an empty string is used. The key and the value are connected with ```=```. Different key-value pairs are connected with ```&```, and need to be sorted in lexicographical order, The key must be lowercase letters, and the value must be URL encoded. |

#### Combining StringToSign

StringToSign is composed of the sha1 hash values of q-sign-algorithm, q-sign-time, and HttpRequestInfo, as shown below:
```
StringToSign = q-sign-algorithm + "\n"
             + q-sign-time + "\n"
             + sha1(HttpRequestInfo) + "\n"
```

```\n``` indicates a newline escape character. ```+``` indicates a string concatenation operation. Other parameters have been described above. The sha1 hash of HttpRequestInfo is a lowercase hexadecimal string.

#### Generating SignKey
Now, the API only supports one digital signature algorithm, hmac-sha1 (default). Its pseudo code is as follows:
```
SignKey = Hexdigest(HMAC-SHA1(q-key-time, SecretKey))
```
```HMAC-SHA1``` is the encryption algorithm, and ```Hexdigest``` is the method used for hexadecimal string conversion. The output results of some languages using the encryption algorithm are hexadecimal strings, so conversion is not needed.

#### Generating Signature
Now, the API only supports one digital signature algorithm, hmac-sha1 (default). Its pseudo code is as follows:
```
Signature = Hexdigest(HMAC-SHA1(StringToSign, SignKey))
```
```HMAC-SHA1``` is the encryption algorithm, and ```Hexdigest``` is the method used for hexadecimal string conversion. The output results of some languages using the encryption algorithm are hexadecimal strings, so conversion is not needed.


## Examples

Take the following SecretId and SecretKey as examples:
```
SecretId = "AKIDc9YlmrBcFk4C8sbmXQ8i65XXXXXXXXXX"
SecretKey = "LUSE4nPK1d4tX5SHyXv6tZXXXXXXXXXX"

StartTime = 1510109254
EndTime = 1510109314
```

**Example 1**:
To get logset information, the HTTP request is as follows:
```
GET /logset?logset_name=testset HTTP/1.1
Host: ap-shanghai.cls.myqcloud.com

```

For the above request, if a signature is added in the request header Host, the generated string HttpRequestInfo is:
```
get\n/logset\nlogset_name=testset\nhost=ap-shanghai.cls.myqcloud.com\n
```

The original string StringToSign generated using HttpRequestInfo is:
```
sha1\n1510109254;1510109314\n74713a7e01250b81424dac21dced038ee5b8054d\n
```

Encrypt the q-key-time using the SecretKey to get the SignKey:
```
a4501294d3a835f8dab6caf5c19837dd19eef357
```

Encrypt the StringToSign using the SignKey to generate the Signature:
```
42a7a1d1b44f14ae39a5e7fc3172feec6a08b197
```

The combined signature Authorization is:
```
q-sign-algorithm=sha1&q-ak=AKIDc9YlmrBcFk4C8sbmXQ8i65XXXXXXXXXX&q-sign-time=1510109254;1510109314&q-key-time=1510109254;1510109314&q-header-list=host&q-url-param-list=logset_name&q-signature=42a7a1d1b44f14ae39a5e7fc3172feec6a08b197
```

The final request content is:
```
GET /logset?logset_name=testset HTTP/1.1
Host: ap-shanghai.cls.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDc9YlmrBcFk4C8sbmXQ8i65XXXXXXXXXX&q-sign-time=1510109254;1510109314&q-key-time=1510109254;1510109314&q-header-list=host&q-url-param-list=logset_name&q-signature=42a7a1d1b44f14ae39a5e7fc3172feec6a08b197

```

**Example 2**:
To modify logset information, the HTTP request is as follows:
```
PUT /logset HTTP/1.1
Host: ap-shanghai.cls.myqcloud.com
Content-Type: application/json
Content-Length: 50

{"logset_id":"xxxx-xx-xx-xx-xxxxxxxx","period":30}
```

The md5 value calculated for the body content is:
```
f9c7fc33c7eab68dfa8a52508d1f4659
```

For the above request, if a signature is added in the request header Host, the generated string HttpRequestInfo is:
```
put\n/logset\n\ncontent-md5=f9c7fc33c7eab68dfa8a52508d1f4659&content-type=application%2Fjson&host=ap-shanghai.cls.myqcloud.com\n
```

The original string StringToSign generated using HttpRequestInfo is:
```
sha1\n1510109254;1510109314\n0ca0242c3d50441fda6aa234d31bea7a7a12a1ea\n
```

Encrypt the q-key-time using the SecretKey to get the SignKey:
```
a4501294d3a835f8dab6caf5c19837dd19eef357
```

Encrypt the StringToSign using the SignKey to generate the Signature:
```
85a55e61de42483ba03bffd07a6c01b8d651af51
```

The combined signature Authorization is:
```
q-sign-algorithm=sha1&q-ak=AKIDc9YlmrBcFk4C8sbmXQ8i65XXXXXXXXXX&q-sign-time=1510109254;1510109314&q-key-time=1510109254;1510109314&q-header-list=content-md5;content-type;host&q-url-param-list=&q-signature=85a55e61de42483ba03bffd07a6c01b8d651af51
```

The final request content is:
```
PUT /logset HTTP/1.1
Host: ap-shanghai.cls.myqcloud.com
Content-Type: application/json
Content-MD5: f9c7fc33c7eab68dfa8a52508d1f4659
Content-Length: 50
Authorization: q-sign-algorithm=sha1&q-ak=AKIDc9YlmrBcFk4C8sbmXQ8i65XXXXXXXXXX&q-sign-time=1510109254;1510109314&q-key-time=1510109254;1510109314&q-header-list=content-md5;content-type;host&q-url-param-list=&q-signature=85a55e61de42483ba03bffd07a6c01b8d651af51

{"logset_id":"xxxx-xx-xx-xx-xxxxxxxx","period":30}
```

