## 功能描述

Initiate Multipart Upload 接口请求实现初始化分块上传，成功执行此请求后将返回 UploadId，用于后续的 Upload Part 请求。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=InitiateMultipartUpload&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
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
POST /<ObjectKey>?uploads HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Type: Content Type
Content-Length: 0
Authorization: Auth String
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求参数

此接口无请求参数。

#### 请求头

此接口除使用公共请求头部外，还支持以下请求头部，了解公共请求头部详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

| 名称                | 描述                                                         | 类型   | 是否必选 |
| ------------------- | ------------------------------------------------------------ | ------ | -------- |
| Cache-Control       | RFC 2616 中定义的缓存指令，将作为对象元数据保存              | string | 否       |
| Content-Disposition | RFC 2616 中定义的文件名称，将作为对象元数据保存              | string | 否       |
| Content-Encoding    | RFC 2616 中定义的编码格式，将作为对象元数据保存              | string | 否       |
| Content-Type        | RFC 2616 中定义的 HTTP 请求内容类型（MIME），此头部用于描述待上传对象的内容类型，将作为对象元数据保存。<br>例如`text/html`或 `image/jpeg` | string | 是       |
| Expires             | RFC 2616 中定义的缓存失效时间，将作为对象元数据保存          | string | 否       |
| x-cos-meta-\*       | 包括用户自定义元数据头部后缀和用户自定义元数据信息，将作为对象元数据保存，大小限制为2KB<br>**注意：**用户自定义元数据信息支持下划线（_），但用户自定义元数据头部后缀不支持下划线，仅支持减号（-） | string | 否       |
| x-cos-storage-class | 对象存储类型。枚举值请参见 [存储类型](https://cloud.tencent.com/document/product/436/33417) 文档，例如 MAZ_STANDARD，MAZ_STANDARD_IA，INTELLIGENT_TIERING，MAZ_INTELLIGENT_TIERING，STANDARD_IA，ARCHIVE，DEEP_ARCHIVE。默认值：STANDARD | Enum   | 否       |
|  x-cos-tagging   |对象的标签集合，最多可设置10个标签（例如，Key1=Value1&Key2=Value2）。 标签集合中的 Key 和 Value 必须先进行 URL 编码。| string| 否  |


**访问控制列表（ACL）相关头部**

在上传对象时可以通过指定下列请求头部来设置对象的访问权限：

| 名称                     | 描述                                                         | 类型   | 是否必选 |
| ------------------------ | ------------------------------------------------------------ | ------ | -------- |
| x-cos-acl                | 定义对象的访问控制列表（ACL）属性。枚举值请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752#.E9.A2.84.E8.AE.BE.E7.9A.84-acl) 文档中对象的预设 ACL 部分，例如 default，private，public-read 等，默认为 default。<br>**注意：**如果您不需要进行对象 ACL 控制，请设置为 default 或者此项不进行设置，默认继承存储桶权限 | Enum   | 否       |
| x-cos-grant-read         | 赋予被授权者读取对象的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如`id="100000000001",id="100000000002"` | string | 否       |
| x-cos-grant-read-acp     | 赋予被授权者读取对象的访问控制列表（ACL）的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如`id="100000000001",id="100000000002"` | string | 否       |
| x-cos-grant-write-acp    | 赋予被授权者写入对象的访问控制列表（ACL）的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如`id="100000000001",id="100000000002"` | string | 否       |
| x-cos-grant-full-control | 赋予被授权者操作对象的所有权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如`id="100000000001",id="100000000002"` | string | 否       |

**服务端加密（SSE）相关头部**

在上传对象时可以使用服务端加密，请参见 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7728#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8)。

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口除返回公共响应头部外，还返回以下响应头部，了解公共响应头部详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

**服务端加密（SSE）相关头部**

如果在上传对象时使用了服务端加密，则此接口将返回服务端加密专用头部，请参见 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7729#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8)。

#### 响应体

请求成功，返回 **application/xml** 数据，包含分块上传初始化信息。


```
<InitiateMultipartUploadResult>
       <Bucket>string</Bucket>
       <Key>string</Key>
       <UploadId>string</UploadId>
</InitiateMultipartUploadResult>
```

具体的节点描述如下：

| 节点名称（关键字）            | 父节点 | 描述                                          | 类型      |
| ----------------------------- | ------ | --------------------------------------------- | --------- |
| InitiateMultipartUploadResult | 无     | 保存 Initiate Multipart Upload 结果的所有信息 | Container |

**Container 节点 InitiateMultipartUploadResult 的内容：**

| 节点名称（关键字） | 父节点                        | 描述                                 | 类型   |
| ------------------ | ----------------------------- | ------------------------------------ | ------ |
| Bucket             | InitiateMultipartUploadResult | 目标存储桶                           | string |
| Key                | InitiateMultipartUploadResult | 目标对象键                           | string |
| UploadId           | InitiateMultipartUploadResult | 在后续 Upload Part 中使用的 UploadId | string |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：简单案例

#### 请求

```plaintext
POST /exampleobject?uploads HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 25 Mar 2020 10:07:01 GMT
Content-Type: video/mp4
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1585130821;1585138021&q-key-time=1585130821;1585138021&q-header-list=content-length;content-type;date;host&q-url-param-list=uploads&q-signature=38c5a4b181067206cdbdf65f6a4d662b2291****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: close
Date: Wed, 25 Mar 2020 10:07:01 GMT
Server: tencent-cos
x-cos-request-id: NWU3YjJkNDVfNDliNTJhMDlfYzZhMl8yOTVj****



<InitiateMultipartUploadResult>
			<Bucket>examplebucket-1250000000</Bucket>
			<Key>exampleobject</Key>
			<UploadId>1585130821cbb7df1d11846c073ad648e8f33b087cec2381df437acdc833cf654b9ecc6361</UploadId>
</InitiateMultipartUploadResult>
```

#### 案例二：使用请求头部指定元数据和 ACL

#### 请求

```plaintext
POST /exampleobject?uploads HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 28 May 2020 08:35:34 GMT
Content-Type: video/mp4
Cache-Control: max-age=86400
Content-Disposition: attachment; filename=example.jpg
x-cos-meta-example-field: example-value
x-cos-acl: public-read
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1590654934;1590662134&q-key-time=1590654934;1590662134&q-header-list=cache-control;content-disposition;content-length;content-type;date;host;x-cos-acl;x-cos-meta-example-field&q-url-param-list=uploads&q-signature=5465e9e05cd638e549f66457235d488bfb02****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: close
Date: Thu, 28 May 2020 08:35:34 GMT
Server: tencent-cos
x-cos-request-id: NWVjZjc3ZDZfOThjMjJhMDlfMjg5N18zNWYy****



<InitiateMultipartUploadResult>
			<Bucket>examplebucket-1250000000</Bucket>
			<Key>exampleobject</Key>
			<UploadId>1590654934dfb1343b4323b711afc22569c18af51596d4f2e40faf392fe1bb469c5b77115f</UploadId>
</InitiateMultipartUploadResult>
```

#### 案例三：使用服务端加密 SSE-COS

#### 请求

```plaintext
POST /exampleobject?uploads HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 28 May 2020 08:43:58 GMT
Content-Type: video/mp4
x-cos-server-side-encryption: AES256
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1590655438;1590662638&q-key-time=1590655438;1590662638&q-header-list=content-length;content-type;date;host;x-cos-server-side-encryption&q-url-param-list=uploads&q-signature=24fccaa68a5eb5e0a9e959dfd9493e3a0671****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: close
Date: Thu, 28 May 2020 08:43:58 GMT
Server: tencent-cos
x-cos-request-id: NWVjZjc5Y2VfZjhjODBiMDlfMjIyOGFfMzYxYWVm****
x-cos-server-side-encryption: AES256



<InitiateMultipartUploadResult>
			<Bucket>examplebucket-1250000000</Bucket>
			<Key>exampleobject</Key>
			<UploadId>15906554384f160dd0a272ebb6fbcdb0ffbb61adb2b46fa6b9f2ffabcfb2940b8f72277952</UploadId>
</InitiateMultipartUploadResult>
```

#### 案例四：使用服务端加密 SSE-KMS

#### 请求

```plaintext
POST /exampleobject?uploads HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 28 May 2020 08:44:19 GMT
Content-Type: video/mp4
x-cos-server-side-encryption: cos/kms
x-cos-server-side-encryption-cos-kms-key-id: 48ba38aa-26c5-11ea-855c-52540085****
x-cos-server-side-encryption-context: eyJhdXRob3IiOiJmeXNudGlhbiIsImNvbXBhbnkiOiJUZW5jZW50In0=
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1590655459;1590662659&q-key-time=1590655459;1590662659&q-header-list=content-length;content-type;date;host;x-cos-server-side-encryption;x-cos-server-side-encryption-context;x-cos-server-side-encryption-cos-kms-key-id&q-url-param-list=uploads&q-signature=11ab592d5aba2e740be67f69dfa254631293****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: close
Date: Thu, 28 May 2020 08:44:20 GMT
Server: tencent-cos
x-cos-request-id: NWVjZjc5ZTNfMmZiOTJhMDlfMzJlNDJfMjkzNGJi****
x-cos-server-side-encryption: cos/kms
x-cos-server-side-encryption-cos-kms-key-id: 48ba38aa-26c5-11ea-855c-52540085****



<InitiateMultipartUploadResult>
			<Bucket>examplebucket-1250000000</Bucket>
			<Key>exampleobject</Key>
			<UploadId>15906554607990121702e8e4b706eb0f12b8568a3f3b0b76b884e4df676ed50291f0b17131</UploadId>
</InitiateMultipartUploadResult>
```


#### 案例五：使用服务端加密 SSE-C

#### 请求

```plaintext
POST /exampleobject?uploads HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 28 May 2020 08:44:41 GMT
Content-Type: video/mp4
x-cos-server-side-encryption-customer-algorithm: AES256
x-cos-server-side-encryption-customer-key: MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=
x-cos-server-side-encryption-customer-key-MD5: U5L61r7jcwdNvT7frmUG8g==
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1590655481;1590662681&q-key-time=1590655481;1590662681&q-header-list=content-length;content-type;date;host;x-cos-server-side-encryption-customer-algorithm;x-cos-server-side-encryption-customer-key;x-cos-server-side-encryption-customer-key-md5&q-url-param-list=uploads&q-signature=abd12e9b8c4334a803b5ed8cc03c697904f8****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 230
Connection: close
Date: Thu, 28 May 2020 08:44:41 GMT
Server: tencent-cos
x-cos-request-id: NWVjZjc5ZjlfOGJjOTJhMDlfNzJmYV8xOTcy****
x-cos-server-side-encryption-customer-algorithm: AES256
x-cos-server-side-encryption-customer-key-MD5: U5L61r7jcwdNvT7frmUG8g==



<InitiateMultipartUploadResult>
			<Bucket>examplebucket-1250000000</Bucket>
			<Key>exampleobject</Key>
			<UploadId>15906554815fb0c8bda2edae20d895ad7452e949bf51541b31ca14a029fb6f1617f10ca186</UploadId>
</InitiateMultipartUploadResult>
```
