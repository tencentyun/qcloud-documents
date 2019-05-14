## Signature Description

When using the Object Storage Service (COS), HTTP requests can be classified into **anonymous requests** and **signature requests**. The signature request will compute a string of ciphertexts based on the keys provided by Tencent Cloud and specific requests, and pass such by HTTP request.

- Anonymous request: The request does not include any identity and authentication information. HTTP operations such as PUT/GET/POST/DELET are conducted directly by using the COS address.
- Signature request: The COS server will determine whether the signature request is granted by passing the encrypted signature information in the Authorization field of the HTTP Headers or through the URL parameters.

Generally, when deploying a public access service, you can set the storage to allow all anonymous access. But writing requests are usually protected by signatures. COS can decide whether the request should be granted, and how to control the content and the validity period of the request based on the user-specified ACL policy and the passing signature.

Request restriction and signature access can be applied in the following scenarios:

> Verify the identity of the user: The process of calculating the signature is based on the keys provided by Tencent Cloud, including the SecretID and SecretKey and other elements.
>
> Verify the transmitted data: The verification information of the data is included in the ciphertext of the signature. If the check value of the passing data does not match the check value in the ciphertext, a failure will be returned for such request. Generally, this can guarantee that, when the request content is hijacked, the error data will not recorded.
>
> Protect the signature from being used twice: By encrypting the request's validity period in the signature, it is possible to ensure that the client cannot initiate the request after the signature expires, which is also used to prevent any third party from intervening in the use of the signature to protect data security when network is listened in.

## Signature Method

COS signature request is included in the HTTP request in the following two ways:

- HTTP Authorization Header: Passed through the Authorization field of the HTTP request headers.
- URL parameters: Pass the signature by adding the parameters after the URL.

## Signature Algorithm - HTTP Headers

### Overview

In addition to the POST operation, other signatures can be passed through the Authorization field of the HTTP request headers, which is also the most common request authentication method in the HTTP standard definition. Common requests are as follows:

```http
PUT ?versioning HTTP/1.1
Host: testbucket-125000000.cn-north.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=QmFzZTY0IGlzIGEgZ2VuZXJp&q-sign-time=1480932292;1481012292&q-key-time=1480932292;1481012292&q-header-list=host&q-url-param-list=versioning&q-signature=43803ef4a4207299d87bb75d1c739c06cc9406bb
```

The following table lists the information to be passed in the Authorization field:

| Name               | Description                                       |
| ---------------- | ---------------------------------------- |
| q-sign-algorithm | Describe the encryption method of the signature. Currently, Tencent Cloud uses HMAC-SHA1 for signature encryption. <br />Please keep the default value (sha1) for this field |
| q-ak             | Identify the user's identity in SecretID field; check in the Tencent Cloud API Key page.  |
|q-sign-time      | The valid start and end time of the signature, which is represented by a 10-digit Unix timestamp, with the validity accurate to seconds. <br />The start and end time are separated before and after by semicolon.  |
| q-key-time       | Users can define he valid start and end time of SignningKey, which is represented by a 10-digit Unix timestamp, with the validity accurate to seconds. <br />The start and end time are separated before and after by semicolon. <br />Generally, the time range of the q-key-time is greater than or equal to that of q-sign-time.  |
| q-header-list    | Provide the Headers list to be verified in ciphertexts in lowercase and sort them in lexicographical order.  |
| q-header-list    | Provide the Parameters list to be verified in ciphertexts in lowercase.       |
| q-signature      | Request verification information encrypted via the HMAC-SHA1 algorithm.                 |

### Calculating Signatures

Before configuring the signature, you must first obtain the API key pair for the Tencent Cloud account, including SecretID and SecretKey. For details, see "Key Management" on the left of the COS Console page or "Monitoring and Management - Cloud API Key" in the Tencent Cloud Console.

#### Signature Composition

- SignKey: A key string that carries the validity period and is encrypted with HMAC-SHA1 via SecretKey.
- FormatString: A string formatted according to certain standards from the request.
- StringToSign: A string containing the verification algorithm, validity period of the request, and FormatString verified by Hash.
- Signature: Encrypted signature, use the string encrypted with HMAC-SHA1 in SignKey and StringToSign to fill in q-signature.

#### Computing SignKey

In order to protect the security of SecretKey, the request needs to encrypt the SecretKey before transmission. The signature allows users to carry Unix timestamps to limit the effective time of SecretKey.

To enable users to send the key information needed for signature calculation to the untrusted client, SecretKey supports the generation of an irreversible key string encrypted along with the user-specified validity period, and sends it to theuntrusted client. The SignKey shall be computed in the following format:

$SignKey =

```
HMAC-SHA1($SecretKey,"<q-key-time>")
```

- SecretKey: The SecretKey from the API key pair provided by Tencent Cloud, for example `AKIDZfbOA78asKUYBcXFrJD0a1ICvR98JM`.
- q-key-time: The valid start and end time of the SignKey. The two timestamps are separated before and after by semicolon with 10-digit Unix timestamp, accurate to seconds. For example `1480932292; 1481012292`.

#### Generating FormatString

This string formats the key information in the HTTP request and will be used as the primary part for the encryption signature verification. This can protect the HTTP request during transmission from being tampered by any third party.

To enable the COS server to verify the request in a fixed format, the key data in the HTTP request needs to be included in the FormatString, displaying one key element per line. It is generated as follows:

$FormatString = 

```
<FormatMethod>\n
<FormatURI>\n
<FormatParameters>\n
<FormatHeaders>\n
```

- FormatMethod: Refers to the requested HTTP operations, such as PUT/GET/DELETE; must be converted to lowercase.
  - For example, when initiating `GET http://testbucket-125000000.cn-north.myqcloud.com`, its FormatMethod is`get`.


- FormatURI: Refers to the URI of the request, that is, the remaining part after removing the http: // and domain name (usually starting with /), and does not contain the parameter in URL (usually starting with ?). FormatURI must be processed through URL Encode.
  - For example, in the address of `http://testbucket-125000000.cn-north.myqcloud.com/testfile`, the FormatURI is `%2Ftestfile`.
- FormatParameters: Refers to the parameters of the request (starting with ?), which is indicated by `key=value`. The key and value of the parameter must be processed through URL Encode. If there are multiple parameter pairs, use & in between. ** It must be converted to lowercase and sorted in lexicographical order.**
  - For example, when accessing `http://testbucket-125000000.cn-north.myqcloud.com/testfile?versioning`, the FormatParameters is `versioning=`.
  - For example, when accessing ``http://testbucket-125000000.cn-north.myqcloud.com/?prefix=abc&max-keys=20`, the FormatParameters is `prefix=abc&max-keys=20`.
- FormatHeaders: Refers to the HTTP header of the request, which is indicated by `key=value`. The key of the header must be in lowercase, and the value must be processed through URL Encode. If there are multiple parameter pairs, use & in between.
  - For example, in the head `Host:  testbucket-125000000.cn-north.myqcloud.com`, the FormatHeaders is `host=testbucket-125000000.cn-north.myqcloud.com`.

#### Computing StringToSign

The string contains the algorithm name and the validity period of the signature, and the FormatString processed by the SHA-1 hash. Thus, it is necessary to generate a FormatString before calculating the StringToSign.

The validity period of the signature in StringToSign is different from the effective time of the SecretKey in SignKey. The validity period can only be used to verify if the request is initiated within the valid time.

- If the client initiating the request is trusted, the SecretKey can be saved directly on the client, and the same valid start and end time can be used in both SignKey and StringToSign to ensure the validity of the request.
- If the client initiating the request is untrusted by default, the SecretKey shall be protected from being saved directly on the client. At this point, the SignKey can be issued to the client to compute the signature by limiting and encrypting the valid start and end time for SecretKey. The validity period of StringToSign shall be generated by the client when the request is initiated.

The StringToSign is generated in the following format:

$StringToSign =

```
<q-sign-algorithm>\n
<q-sign-time>\n
SHA1Hash($FormatString)\n
```

- q-sign-algorithm: The encryption algorithm used for signatures. The default is `sha1`.
- q-sign-time: The valid start and end time of the request. The two timestamps are separated before and after by semicolon with 10-digit Unix timestamp, accurate to seconds. For example `1480932292; 1481012292`.
- SHA1Hash($FormatString): A string that will generate part of the FormatString by using the SHA-1 hash algorithm to get an irreversible string that identifies the key content of the request.

#### Computing Signature

The Signature generated here will be placed in the q-signature field to verify the validity of the request content. By using the HMAC-SHA1 algorithm, SignKey is used as the key to encrypt and compute the StringToSign. The Signature is generated in the following format:

$Signature =

```
HMAC-SHA1($SignKey,$StringToSign)
```

### Generating Authorization

The contents generated in the signature and those in the request to be explicitly identified shall be indicated by `key=value`. Use & between multiple parameter pairs.

The Authorization is generated in the following format (a long string without line breaks):

```
q-sign-algorithm=sha1&
q-ak=<SecretID>&
q-sign-time=<SignTime>&
q-key-time=<KeyTime>&
q-header-list=<SignedHeaderList>&
q-url-param-list=<SignedParameterList>&
q-signature=<Signature>
```

### Example

COS will provide some examples to demonstrate the process and final result of signature generation, and you can also use the cases in the example to verify if your signature code is correctly computed. The example uses the following key pair:

| SecretID                 | SecretKey                          |
| ------------------------ | ---------------------------------- |
| QmFzZTY0IGlzIGEgZ2VuZXJp | AKIDZfbOA78asKUYBcXFrJD0a1ICvR98JM |

The start and end time for the key and request to be generated are: 1480932292 and 1481012292.

The Bucket used in test is the testbucket in North China, created under the developer account (AppID: 125000000).

Thus, the Host in the example is `testbucket-125000000.cn-north.myqcloud.com`.

#### GET Object Example

The following shows a signature example for GET Object operation with the address of `http://testbucket-125000000.cn-north.myqcloud.com/testfile` and requests the first 4 bytes of the file through the Range parameter.

```http
GET /testfile HTTP/1.1
Host: testbucket-125000000.cn-north.myqcloud.com
Range: bytes=0-3
```

**Step 1: Computing SignKey**

```
HMAC-SHA1(AKIDZfbOA78asKUYBcXFrJD0a1ICvR98JM,"1480932292;1481012292")
```

$SignKey = 95d110a8ead64cac52083100db75b7e3f369e72f

**Step 2: Generating FormatString**

*Note that the end line still needs \n to wrap.*

```
get
/testfile

host=testbucket-125000000.cn-north.myqcloud.com&range=bytes%3d0-3

```

In order to facilitate the use of SHA1Hash($FormatString) in Step 3, first process the content via hash. The result:

```
c92f7246e3f922fe4abae5d6d5ebcd2397dc88cb
```

**Step 3: Computing StringToSign**

*Note that the end line still needs \n to wrap.*

```
sha1
1480932292;1481012292
c92f7246e3f922fe4abae5d6d5ebcd2397dc88cb

```

**Step 4: Computing Signature**

```
HMAC-SHA1(95d110a8ead64cac52083100db75b7e3f369e72f,$StringToSign)
```

The result:

```
29b2f454bb9d8a629e7cad61227bd5fd0dd11a2d
```

**Step 5: Generating Authorization**

```
q-sign-algorithm=sha1&q-ak=QmFzZTY0IGlzIGEgZ2VuZXJp&q-sign-time=1480932292;1481012292&q-key-time=1480932292;1481012292&q-header-list=host;range&q-url-param-list=&q-signature=29b2f454bb9d8a629e7cad61227bd5fd0dd11a2d
```

**Final request example**

```http
GET /testfile HTTP/1.1
Host: testbucket-125000000.cn-north.myqcloud.com
Range: bytes=0-3
Authorization: q-sign-algorithm=sha1&q-ak=QmFzZTY0IGlzIGEgZ2VuZXJp&q-sign-time=1480932292;1481012292&q-key-time=1480932292;1481012292&q-header-list=host;range&q-url-param-list=&q-signature=29b2f454bb9d8a629e7cad61227bd5fd0dd11a2d
```

#### PUT Object Example

The following shows a signature example for PUT Object operation with the address of `http://testbucket-125000000.cn-north.myqcloud.com/testfile2` and verifies the file "HelloWorld" (hash value: `Db8ac1c259eb89d4a131b253bacfca5f319d54f2`) via SHA-1 to specify that the file is stored on the nearline storage medium.

```http
PUT /testfile2 HTTP/1.1
Host: testbucket-125000000.cn-north.myqcloud.com
x-cos-content-sha1: db8ac1c259eb89d4a131b253bacfca5f319d54f2
x-cos-stroage-class: nearline

<Payload>
```

**Step 1: Computing SignKey**

```
HMAC-SHA1(AKIDZfbOA78asKUYBcXFrJD0a1ICvR98JM,"1480932292;1481012292")
```

$SignKey = 95d110a8ead64cac52083100db75b7e3f369e72f

**Step 2: Generating FormatString**

*Note that the end line still needs \n to wrap.*

```
put
/testfile2

host=testbucket-125000000.cn-north.myqcloud.com&x-cos-content-sha1=db8ac1c259eb89d4a131b253bacfca5f319d54f2&x-cos-stroage-class=nearline

```

In order to facilitate the use of SHA1Hash($FormatString) in Step 3, first process the content via hash. The result:

```
c3aa791042f601c81e8453dbb05472de8242576d
```

**Step 3: Computing StringToSign**

*Note that the end line still needs \n to wrap.*

```
sha1
1480932292;1481012292
c3aa791042f601c81e8453dbb05472de8242576d

```

**Step 4: Computing Signature**

```
HMAC-SHA1(95d110a8ead64cac52083100db75b7e3f369e72f,$StringToSign)
```

The result:

```
b237c36c5495b048519b82b17a200840594c0339
```

**Step 5: Generating Authorization**

```
q-sign-algorithm=sha1&q-ak=QmFzZTY0IGlzIGEgZ2VuZXJp&q-sign-time=1480932292;1481012292&q-key-time=1480932292;1481012292&q-header-list=host;x-cos-content-sha1;x-cos-storage-class&q-url-param-list=&q-signature=b237c36c5495b048519b82b17a200840594c0339
```

**Final request example**

```http
PUT /testfile2 HTTP/1.1
Host: testbucket-125000000.cn-north.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=QmFzZTY0IGlzIGEgZ2VuZXJp&q-sign-time=1480932292;1481012292&q-key-time=1480932292;1481012292&q-header-list=host;x-cos-content-sha1;x-cos-storage-class&q-url-param-list=&q-signature=b237c36c5495b048519b82b17a200840594c0339
x-cos-content-sha1: db8ac1c259eb89d4a131b253bacfca5f319d54f2
x-cos-stroage-class: nearline

HelloWorld
```

