<font color="#0000cc">**Note:** </font>
> 1. This document applies only to the COS V5 version, which can be viewed on the COS console after login.
> 2. This document does not apply to the HTTP requests of POST object.

With the Object Storage Service (COS), an anonymous HTTP request or HTTP signature request can be made to the COS through the RESTful API. For a signature request, the COS server will authenticate its initiator.
* Anonymous request: The HTTP request does not include any identity and authentication information, and the HTTP request is performed through the RESTful API.
* Signature request: A signature is added in the HTTP request, and authentication is performed after the COS server receives the message. The request is accepted and executed after a successful authentication, otherwise it is discarded with an error message.

Tencent Cloud COS object storage is authenticated based on the custom HTTP solution for key HMAC (Hash Message Authentication Code).

## Signature Usage Scenarios
In scenarios where the COS object storage service is used, the object can usually be set to public read and private write for the data that requires an external publishing class. That is, the object can be viewed by everyone and written through the specified account or IP of ACL policies. In this case, you can associate the ACL policy with an API request signature to authenticate the access, and control the permissions and expiration of the operation.

<font color="#0000cc">**Note:** </font>
> The API request signature described herein is already included if you are using SDK for development. ** You only need to follow the steps described herein if you want to make a secondary development through the original APIs.

In the above scenario, a variety of safety protections can be included for the API request:
1. **Requester Authentication**. Confirm the requester identity with the unique ID and key of a visitor.
2. **Prevent Tampering of Transmission Data**. Encrypt and verify the data to ensure the integrity of transmission content.
3. **Prevent Theft of Signature**. Set the timeliness of signature, and encrypt data, so as to avoid the signature theft and re-use.

## Signature Process
The client signs the HTTP request, and then sends it to Tencent Cloud for signature verification. The specific process is shown in the figure below.
![Flow Chart](//mc.qcloudimg.com/static/img/4a1eb29033caa977c648cb84d9398fdd/image.png)


## Preparations
1. APPID, SecretId and SecretKey. 
   They are available on the [Cloud API Key](https://buy.cloud.tencent.com/capi) page of console.
2. Specify the development languages:
   Support but not limited to Java, PHP, C Sharp, C++, node.js, Python, and specify the corresponding HMAC-SHA1, SHA1 functions.

## Signature Content

The HTTP signature request initiated to COS through the RESTful API is passed by using the standard HTTP Authorization header, as shown in the following example:
```
PUT ?versioning HTTP/1.1
Host: bucket1-1254000000.cos.ap-beijing.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDQjz3ltompVjBni5LitkWHFlFpwkn9U5q&q-sign-time=1480932292;1481012298&q-key-time=1480932292;1481012298&q-header-list=host&q-url-param-list=versioning&q-signature=438023e4a4207299d87bb75d1c739c06cc9406bb

```
Where, the signature content is formed by a number of key=value pairs linked with "&". The format is as follows:
```
q-sign-algorithm=sha1&q-ak=[SecretID]&q-sign-time=[SignTime]&
q-key-time=[KeyTime]&q-header-list=[SignedHeaderList]&
q-url-param-list=[SignedParameterList]&q-signature=[Signature]
```

<span id="signaturesplit"></span>
### Key Value Description

Where, the key value (key=value) pairs which form the signature content are described as follows:
<style>
table th:first-of-type {
    width: 150px;
}
</style><style rel="stylesheet"> table th:nth-of-type(1) { width: 140px; }</style>

Key(key)|Value(value)	| Description
---|---|---
q-sign-algorithm | sha1 |Required. <br>It is sha1, as only sha1 is currently supported for the signature algorithm.
q-ak | parameter[*SecretID*] | Required. <br>Account ID, namely SecretID, which is available on the [Cloud API Key](https://console.cloud.tencent.com/capi) page of console.<br><br>**For example:** AKIDQjz3ltompVjBni5LitkWHFlFpwkn9U5q.
q-sign-time | parameter[*SignTime*] | Required. <br>The valid start/end time of this signature, which are described by the Unix timestamp<font color="#3300ff"><sup>Note 1</sup></font> in seconds, in the format of [*start-seconds*];[*end-seconds*].<br><br>**For example:** 1480932292;1481012298.
q-key-time | parameter[*KeyTime*] | Required. <br>Its value is the same as q-sign-time.
q-header-list | parameter[*SignedHeaderList*] | Required. <br>HTTP request header. Some or all keys need to be extracted from key:value pairs. The key need to be converted to lowercase, and multiple keys need to be sorted in lexicographical order and can be connected by ";".<br><br>**For example:** Suppose an HTTP request "Host: bucket1-1254000000.cos.ap-beijing.myqcloud.com Content-Type: image/jpeg". Its SignedHeaderList is content-type;host.
q-url-param-list | parameter[*SignedParameterList*] | Required. <br>HTTP request parameters. Some or all keys need to be extracted from key:value pairs. The key need to be converted to lowercase, and multiple keys need to be sorted in lexicographical order and can be connected by ";".<br><br>**For example:** Suppose an HTTP requrest "GET /?prefix=abc&max-keys=20". Its SignedParameterList is max-keys;prefix or prefix.
q-signature | parameter[Signature] | Required. <br>For HTTP content signature, please see [Signature Calculation](#signature).


<font color="#3300ff">Note 1: </font> **About q-sign-time and q-key-time** <br>
> 1. Unix timestamp is the total number of seconds from Greenwich time at 00:00:00 on January 01, 1970 (Beijing time at 08:00:00 on January 01, 1970) to the current time.
> 2. The end timestamp must be greater than the start timestamp, otherwise it will cause the signature to expire immediately.

<span id="signature"></span>
### Signature Calculation

Signature calculation is divided into four steps:
1. Encrypt the calculated value SignKey for the valid start/end time of the temporary key.
2. Generate HttpString according to the fixed format combination.
3. Encrypt HttpString, and generate StringToSign according to the fixed format combination.
4. Encrypt StringToSign to generate Signature.

#### Code Description
The pseudo codes are:
```
SignKey = HMAC-SHA1(SecretKey,"[q-key-time]")
HttpString = [HttpMethod]\n[HttpURI]\n[HttpParameters]\n[HttpHeaders]\n
StringToSign = [q-sign-algorithm]\n[q-sign-time]\nSHA1-HASH(HttpString)\n
Signature = HMAC-SHA1(SignKey,StringToSign)
```
Where the following parts should be adapted to language specifications under different development language environments:
1. The definition and assignment of variables. Please update according to the specification of the language used.
2. The pseudo function SHA1_FUNC. It is output in hexadecimal lowercase. Please replace it with the corresponding function in the development language used, as shown in the following table:

Pseudo function| PHP | Java
---|---|---|---
HMAC-SHA1 | hash_hmac | HmacUtils.hmacSha1Hex
SHA1-HASH | sha1 | DigestUtils.sha1Hex
#### Code Example (PHP)
For example, in the PHP development environment, the above codes are:

```
$SignKey = hash_hmac($SecretKey,"[q-key-time]")
$HttpString = [HttpMethod]\n[HttpURI]\n[HttpParameters]\n[HttpHeaders]\n
$StringToSign = [q-sign-algorithm]\n[q-sign-time]\nsha1($HttpString)\n
$Signature = hash_hmac($SignKey,$StringToSign)
```

##### Parameter Description
Parameter | Description
---|---
[q-key-time] | must be consistent with the q-key-time descripted in [Key Description](#signaturesplit).
[HttpMethod] | HTTP request method. Only lowercase is supported, such as get, post, put, delete, head, and options.<br><br>**For example:** Suppose an HTTP request "GET /testfile". Its HttpMethod is get.
[HttpURI] | The URI part of an HTTP request. Namely the part starting from the "/" virtual root path.<br><br>**For example:** Suppose an HTTP request "GET /testfile". Its HttpURI is /testfile.
[HttpParameters] | HTTP request parameter. This is the part after “?” and linked with "&" in URI. You need to select part or all of key=value pairs. Besides, the key needs to be converted to lowercase, and the URLEncode conversion is to perform on its value. Many pairs of key=value are linked with "&" and sorted in the lexicographical order.<br><br>**For example:** Suppose an HTTP request "GET /?prefix=abc&max-keys=20". Its HttpParameters is max-keys=20&prefix=abc or prefix=abc.<br><br><font color="#0000cc">**Note:** </font><br>The key in the key=value pair it contains must be consistent with the key in q-url-param-list descripted in [Key Description](#signaturesplit).
[HttpHeaders] | HTTP request header. You need to select part or all of the key:value pairs, and convert them into the key=value format. Besides, the key needs to be converted to lowercase, and the URLEncode conversion is to perform on its value. Multiple pairs of key=value are linked with "&" and sorted in the lexicographical order.<br><br>**For example:** Suppose an HTTP request "Host: bucket1-1254000000.cos.ap-beijing.myqcloud.com Content-Type: image/jpeg". Its HttpHeaders is content-type=image%2Fjpeg&host=bucket1-1254000000.cos.ap-beijing.myqcloud.com.<br><br><font color="#0000cc">**Note:** </font><br>The key in the key=value pair it contains must be consistent with the key in q-header-list descripted in [Key Description](#signaturesplit).
[q-sign-algorithm] | sha1. Only sha1 encryption algorithm is currently supported.
[q-sign-time] | Must be consistent with the q-sign-time descripted in [Key Description](#signaturesplit).


#### Parameter Instance
Parameter | Value
---|---
[q-key-time] | 1417773892;1417853898
[HttpMethod] | get
[HttpURI] | /testfile
[HttpParameters] | max-keys=20&prefix=abc
[HttpHeaders] | host=bucket1-1254000000.cos.ap-beijing.myqcloud.com
[q-sign-algorithm] | sha1
[q-sign-time] | 1417773892;1417853898


## Examples
A user wants to download and upload objects using the API calling method, and make a signature to the calling.

### Preparations
Obtain APPID, SecretId, and SecretKey by logging in to the [Cloud API Key](https://console.cloud.tencent.com/capi) page, and specify the development language as follows:

APPID | SecretId | SecretKey | Development Language
---|---|---|---
1254000000|AKIDQjz3ltompVjBni5LitkWHFlFpwkn9U5q | BQYIM75p8x0iWVFSIgqEKwFprpRSVHlz | PHP

### Upload Objects

Requirement: Upload objects to the Bucket bucket1

The original HTTP request is:

```
PUT /testfile2 HTTP/1.1
Host: bucket1-1254000000.cos.ap-beijing.myqcloud.com
x-cos-content-sha1: 7b502c3a1f48c8609ae212cdfb639dee39673f5e
x-cos-storage-class: nearline

Hello world
```

The signed HTTP request is:

```
PUT /testfile2 HTTP/1.1
Host: bucket1-1254000000.cos.ap-beijing.myqcloud.com
x-cos-content-sha1: 7b502c3a1f48c8609ae212cdfb639dee39673f5e
x-cos-storage-class: nearline
Authorization: q-sign-algorithm=sha1&q-ak=AKIDQjz3ltompVjBni5LitkWHFlFpwkn9U5q&q-sign-time=1417773892;1417853898&q-key-time=1417773892;1417853898&q-header-list=host;x-cos-content-sha1;x-cos-storage-class&q-url-param-list=&q-signature=84f5be2187452d2fe276dbdca932143ef8161145

Hello world
```

The value and description corresponding to each parameter are as follows:

Key(key) | Value(value)	| Note
---|---|---
q-sign-algorithm | sha1 | Only sha1 signature algorithm is currently supported.
q-ak | AKIDQjz3ltompVjBni5LitkWHFlFpwkn9U5q | SecretId field
q-sign-time | 1417773892;1417853898 | 2014/12/5 18:04:52 to 2014/12/6 16:18:18
q-key-time | 1417773892;1417853898 | 2014/12/5 18:04:52 to 2014/12/6 16:18:18 
q-header-list | host;x-cos-content-sha1;x-cos-storage-class | The list of HTTP header keys in lexicographical order.
q-url-param-list | | The HTTP parameter list is empty.
q-signature | 84f5be2187452d2fe276dbdca932143ef8161145 | Calculated by codes

Where, the calculation code of q-signature is:
```
$signTime = '1417773892;1417853898';
$signKey = hash_hmac('sha1', $signTime, 'BQYIM75p8x0iWVFSIgqEKwFprpRSVHlz');
$httpString = "put\n/testfile2\n\nhost=bucket1-1254000000.cos.ap-beijing.myqcloud.com&x-cos-content-sha1=7b502c3a1f48c8609ae212cdfb639dee39673f5e&x-cos-storage-class=nearline\n";
$sha1edHttpString = sha1($httpString);
$stringToSign = "sha1\n$signTime\n$sha1edHttpString\n";
$signature = hash_hmac('sha1', $stringToSign, $signKey);
```

### Download Objects

Requirement: Download the first 4 bytes of objects in the Bucket bucket1

The original HTTP request is:

```
GET /testfile HTTP/1.1
Host: bucket1-1254000000.cos.ap-beijing.myqcloud.com
Range: bytes=0-3
```

The signed HTTP request is:

```
GET /testfile HTTP/1.1
Host: bucket1-1254000000.cos.ap-beijing.myqcloud.com
Range: bytes=0-3
Authorization: q-sign-algorithm=sha1&q-ak=AKIDQjz3ltompVjBni5LitkWHFlFpwkn9U5q&q-sign-time=1417773892;1417853898&q-key-time=1417773892;1417853898&q-header-list=host;range&q-url-param-list=&q-signature=4b6cbab14ce01381c29032423481ebffd514e8be
```

The value and description corresponding to each parameter are as follows:

Key(key) | Value(value)	| Note
---|---|---
q-sign-algorithm | sha1 | Only sha1 signature algorithm is currently supported.
q-ak | AKIDQjz3ltompVjBni5LitkWHFlFpwkn9U5q | SecretId field
q-sign-time | 1417773892;1417853898 | 2014/12/5 18:04:52 to 2014/12/6 16:18:18
q-key-time | 1417773892;1417853898 | 2014/12/5 18:04:52 to 2014/12/6 16:18:18 
q-header-list | host;range | List of HTTP header keys
q-url-param-list | | The HTTP parameter list is empty.
q-signature | 4b6cbab14ce01381c29032423481ebffd514e8be | Calculated by codes

Where, the calculation code of q-signature is:
```
$signTime = '1417773892;1417853898';
$signKey = hash_hmac('sha1', $signTime, 'BQYIM75p8x0iWVFSIgqEKwFprpRSVHlz');
$httpString = "get\n/testfile\n\nhost=bucket1-1254000000.cos.ap-beijing.myqcloud.com&range=bytes%3D0-3\n";
$sha1edHttpString = sha1($httpString);
$stringToSign = "sha1\n$signTime\n$sha1edHttpString\n";
$signature = hash_hmac('sha1', $stringToSign, $signKey);
```


