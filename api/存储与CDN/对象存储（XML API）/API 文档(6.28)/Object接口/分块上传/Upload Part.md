## 功能描述

Upload Part 接口请求实现将对象按照分块的方式上传到 COS。最多支持10000分块，每个分块大小为1MB - 5GB，最后一个分块可以小于1MB。

> ? 
> 1. 分块上传首先需要进行初始化，使用 [Initiate Multipart Upload](https://cloud.tencent.com/document/product/436/7746) 接口实现，初始化后将得到一个 UploadId，唯一标识本次上传。
> 2. 在每次请求 Upload Part 时，需要携带 partNumber 和 uploadId，partNumber 为块的编号，支持乱序上传。
> 3. 当传入 uploadId 和 partNumber 都相同的时候，后发起上传请求的块将覆盖之前传入的块。当 uploadId 不存在时将返回404错误，NoSuchUpload。
> 

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=UploadPart&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>

## 请求

#### 请求示例

```plaintext
PUT /<ObjectKey>?partNumber=PartNumber&uploadId=UploadId HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Type: Content Type
Content-Length: Content Length
Content-MD5: MD5
Authorization: Auth String

[Object Part]
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求参数

| 名称       | 描述                                                         | 类型    | 是否必选 |
| ---------- | ------------------------------------------------------------ | ------- | -------- |
| partNumber | 标识本次分块上传的编号，范围在1 - 10000                | integer | 是       |
| uploadId   | 标识本次分块上传的 ID，使用 Initiate Multipart Upload 接口初始化分块上传时得到的 UploadId | string  | 是       |

#### 请求头

此接口除使用公共请求头部外，还支持以下请求头部，了解公共请求头部详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

**服务端加密（SSE）相关头部**

如果当前分块上传在初始化时使用了 SSE-C，那么在上传分块时需指定与初始化分块上传时所指定的加密算法和密钥信息，否则不能指定下列头部。

| 名称                                            | 描述                                                         | 类型   | 是否必选 |
| ----------------------------------------------- | ------------------------------------------------------------ | ------ | -------- |
| x-cos-server-side-encryption-customer-algorithm | 服务端加密算法，目前仅支持 AES256                            | string | 是       |
| x-cos-server-side-encryption-customer-key       | 服务端加密密钥的 Base64 编码<br>例如`MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=` | string | 是       |
| x-cos-server-side-encryption-customer-key-MD5   | 服务端加密密钥的 MD5 哈希值，使用 Base64 编码<br>例如`U5L61r7jcwdNvT7frmUG8g==` | string | 是       |
| x-cos-traffic-limit | 针对本分块上传进行流量控制的限速值，必须为数字，单位默认为 bit/s。限速值设置范围为819200 - 838860800，即100KB/s - 100MB/s，如果超出该范围将返回400错误 | integer | 否       |

#### 请求体

此接口请求的请求体为对象（文件）分块内容。

## 响应

#### 响应头

此接口除返回公共响应头部外，还返回以下响应头部，了解公共响应头部详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

**服务端加密（SSE）相关头部**

如果当前分块上传在初始化时使用了服务端加密，则此接口将返回服务端加密专用头部，请参见 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7729#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8)。

#### 响应体

此接口响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：简单案例

#### 请求

```plaintext
PUT /exampleobject?partNumber=1&uploadId=1585130821cbb7df1d11846c073ad648e8f33b087cec2381df437acdc833cf654b9ecc6361 HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 25 Mar 2020 10:07:14 GMT
Content-Type: application/octet-stream
Content-Length: 1048576
Content-MD5: OScKloo1fSQgfpkRFiUH6w==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1585130834;1585138034&q-key-time=1585130834;1585138034&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=partnumber;uploadid&q-signature=a815da18232cfec87e8218f32f31b1e2c5eb****
Connection: close

[Object Part]
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Length: 0
Connection: close
Date: Wed, 25 Mar 2020 10:07:14 GMT
ETag: "39270a968a357d24207e9911162507eb"
Server: tencent-cos
x-cos-hash-crc64ecma: 9973912126177188060
x-cos-request-id: NWU3YjJkNTJfZDBjODJhMDlfMjU4NTZfMjc5MzBh****
```

#### 案例二：使用服务端加密 SSE-COS

#### 请求

```plaintext
PUT /exampleobject?partNumber=1&uploadId=1590862540251355295a5c736513d70d42b92bbde4f0fafb5e0ecb314b55aa0018cc9fa76f HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Sat, 30 May 2020 18:15:50 GMT
Content-Type: application/octet-stream
Content-Length: 13
Content-MD5: EI9SjrY7Zec08nrjMfX/qg==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1590862550;1590869750&q-key-time=1590862550;1590869750&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=partnumber;uploadid&q-signature=2a0085596de5861410bcc43f3d107dc9dda5****
Connection: close

[Object Part]
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Length: 0
Connection: close
Date: Sat, 30 May 2020 18:15:51 GMT
ETag: "108f528eb63b65e734f27ae331f5ffaa"
Server: tencent-cos
x-cos-hash-crc64ecma: 4510578591875220731
x-cos-request-id: NWVkMmEyZDZfYjNjMjJhMDlfMmJlM18zOWI2****
x-cos-server-side-encryption: AES256
```

#### 案例三：使用服务端加密 SSE-KMS

#### 请求

```plaintext
PUT /exampleobject?partNumber=1&uploadId=15908625793957d71176fa878282d266a95b79dc2aec159b4a73d1d79c80d4f931cda6ad65 HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Sat, 30 May 2020 18:16:29 GMT
Content-Type: application/octet-stream
Content-Length: 13
Content-MD5: EI9SjrY7Zec08nrjMfX/qg==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1590862589;1590869789&q-key-time=1590862589;1590869789&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=partnumber;uploadid&q-signature=2d1231c77c72727bd1c2454726813e095a7e****
Connection: close

[Object Part]
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Length: 0
Connection: close
Date: Sat, 30 May 2020 18:16:30 GMT
ETag: "1d3e8ae9da423b440341b09f1616f074"
Server: tencent-cos
x-cos-hash-crc64ecma: 4510578591875220731
x-cos-request-id: NWVkMmEyZmRfYTRiOTJhMDlfMTE0ZGRfMmE3OTk4****
x-cos-server-side-encryption: cos/kms
x-cos-server-side-encryption-cos-kms-key-id: 48ba38aa-26c5-11ea-855c-52540085****
```

#### 案例四：使用服务端加密 SSE-C

#### 请求

```plaintext
PUT /exampleobject?partNumber=1&uploadId=1590862610acd643927bad05cd3947bf98b56b04b0b0b2a45a49969f87cc95b7fd5fcc065a HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Sat, 30 May 2020 18:17:01 GMT
x-cos-server-side-encryption-customer-algorithm: AES256
x-cos-server-side-encryption-customer-key: MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=
x-cos-server-side-encryption-customer-key-MD5: U5L61r7jcwdNvT7frmUG8g==
Content-Type: application/octet-stream
Content-Length: 13
Content-MD5: EI9SjrY7Zec08nrjMfX/qg==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1590862621;1590869821&q-key-time=1590862621;1590869821&q-header-list=content-length;content-md5;content-type;date;host;x-cos-server-side-encryption-customer-algorithm;x-cos-server-side-encryption-customer-key;x-cos-server-side-encryption-customer-key-md5&q-url-param-list=partnumber;uploadid&q-signature=6d0914f1db0e03569b6b5d340dc8d71616bf****
Connection: close

[Object Part]
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Length: 0
Connection: close
Date: Sat, 30 May 2020 18:17:01 GMT
ETag: "ff14981a35a58eb97bca838b055c573b"
Server: tencent-cos
x-cos-hash-crc64ecma: 4510578591875220731
x-cos-request-id: NWVkMmEzMWRfYjRjOTJhMDlfYWRhXzFhZmYw****
x-cos-server-side-encryption-customer-algorithm: AES256
x-cos-server-side-encryption-customer-key-MD5: U5L61r7jcwdNvT7frmUG8g==
```
