## 功能描述

Complete Multipart Upload 接口请求用来实现完成整个分块上传。当使用 Upload Part 上传所有分块完成后，必须调用该 API 来完成整个文件的分块上传。在使用该 API 时，您必须在请求体中给出每一个块的 PartNumber 和 ETag，用来校验块的准确性。

由于分块上传完成后需要合并，而合并需要数分钟时间，因而当合并分块开始时，COS 会立即返回200的状态码并指定 Transfer-Encoding: chunked 响应头部，在合并的过程中，COS 会周期性的使用 chunked 方式返回空格信息来保持连接活跃，直到合并完成，COS 会在最后一个 chunk 中返回合并完成后整个对象的信息。

- 当上传的分块小于1MB的时候，在调用该 API 时，会返回400 EntityTooSmall。
- 当上传块编号不连续的时候，在调用该 API 时，会返回400 InvalidPart。
- 当请求 Body 中的块信息没有按序号从小到大排列的时候，在调用该 API 时，会返回400 InvalidPartOrder。
- 当 UploadId 不存在的时候，在调用该 API 时，会返回404 NoSuchUpload。

>! 建议您及时完成分块上传或者舍弃分块上传，因为已上传但是未终止的块会占用存储空间进而产生存储费用。
>

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=CompleteMultipartUpload&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>


#### 版本控制

- 如果对存储桶启用版本控制，对象存储将自动为要添加的对象生成唯一的版本 ID。对象存储使用 x-cos-version-id 响应头部在响应中返回此标识。
- 如果暂停存储桶的版本控制，则对象存储始终将 null 用作存储在存储桶中的对象的版本 ID，并返回 x-cos-version-id: null 响应头部。

## 请求

#### 请求示例

```plaintext
POST /<ObjectKey>?uploadId=UploadId HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Type: application/xml
Content-Length: Content Length
Content-MD5: MD5
Authorization: Auth String

[Request Body]
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求参数

| 名称     | 描述                                                         | 类型   | 是否必选 |
| -------- | ------------------------------------------------------------ | ------ | -------- |
| uploadId | 标识本次分块上传的 ID，使用 Initiate Multipart Upload 接口初始化分块上传时得到的 UploadId。 | string | 是       |

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

提交 **application/xml** 请求数据，包含所有分块信息。

```xml
<CompleteMultipartUpload>
	<Part>
		<PartNumber>integer</PartNumber>
		<ETag>string</ETag>
	</Part>
	<Part>
		<PartNumber>integer</PartNumber>
		<ETag>string</ETag>
	</Part>
</CompleteMultipartUpload>
```

具体的节点描述如下：

| 节点名称（关键字）      | 父节点 | 描述                                              | 类型      | 是否必选 |
| ----------------------- | ------ | ------------------------------------------------- | --------- | -------- |
| CompleteMultipartUpload | 无     | 包含 Complete Multipart Upload 操作的所有请求信息 | Container | 否       |

**Container 节点 CompleteMultipartUpload 的内容：**

| 节点名称（关键字） | 父节点                  | 描述                               | 类型      | 是否必选 |
| ------------------ | ----------------------- | ---------------------------------- | --------- | -------- |
| Part               | CompleteMultipartUpload | 用来说明本次分块上传中每个块的信息 | Container | 是       |

**Container 节点 Part 的内容：**

| 节点名称（关键字） | 父节点                       | 描述                                                        | 类型    | 是否必选 |
| ------------------ | ---------------------------- | ----------------------------------------------------------- | ------- | -------- |
| PartNumber         | CompleteMultipartUpload.Part | 块编号                                                      | integer | 是       |
| ETag               | CompleteMultipartUpload.Part | 使用 Upload Part 请求上传分块成功后返回的 ETag 响应头部的值 | string  | 是       |

## 响应

#### 响应头

此接口除返回公共响应头部外，还返回以下响应头部，了解公共响应头部详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

**版本控制相关头部**

在启用版本控制的存储桶中上传对象，将返回下列响应头部：

| 名称             | 描述          | 类型   |
| ---------------- | ------------- | ------ |
| x-cos-version-id | 对象的版本 ID | string |

**服务端加密（SSE）相关头部**

如果在上传对象时使用了服务端加密，则此接口将返回服务端加密专用头部，请参见 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7729#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8)。

#### 响应体

请求成功，返回 **application/xml** 数据，包含合并完成后的整个对象信息。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<CompleteMultipartUploadResult xmlns="http://www.qcloud.com/document/product/436/7751">
	<Location>string</Location>
	<Bucket>string</Bucket>
	<Key>string</Key>
	<ETag>string</ETag>
</CompleteMultipartUploadResult>
```

具体的节点描述如下：

| 节点名称（关键字）            | 父节点 | 描述                                          | 类型      |
| ----------------------------- | ------ | --------------------------------------------- | --------- |
| CompleteMultipartUploadResult | 无     | 保存 Complete Multipart Upload 结果的所有信息 | Container |

**Container 节点 CompleteMultipartUploadResult 的内容：**

| 节点名称（关键字） | 父节点                        | 描述                                                         | 类型   |
| ------------------ | ----------------------------- | ------------------------------------------------------------ | ------ |
| Location           | CompleteMultipartUploadResult | 分块上传完成的对象位置，格式为`http://<BucketName-APPID>.cos.<Region>.myqcloud.com/<ObjectKey>`，例如`http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject` | string |
| Bucket             | CompleteMultipartUploadResult | 分块上传的目标存储桶，格式为`<BucketName-APPID>`，例如`examplebucket-1250000000` | string |
| Key                | CompleteMultipartUploadResult | 对象键                                                       | string |
| ETag               | CompleteMultipartUploadResult | 分块合并后的对象 ETag 值                                     | string |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。


## 实际案例

此接口响应默认为 Transfer-Encoding: chunked 编码方式，为了方便阅读，本文档实际案例均采用无 Transfer-Encoding 的方式展示，在使用过程中，不同语言和库可以自动处理这种编码形式，请开发者注意识别和处理，更多信息请查阅语言和库的相关文档。

#### 案例一：简单案例（未启用版本控制）

#### 请求

```plaintext
POST /exampleobject?uploadId=1585130821cbb7df1d11846c073ad648e8f33b087cec2381df437acdc833cf654b9ecc6361 HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 25 Mar 2020 10:07:26 GMT
Content-Type: application/xml
Content-Length: 353
Content-MD5: Me/0Gvtc2x4VPIOhoIRllw==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1585130846;1585138046&q-key-time=1585130846;1585138046&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=uploadid&q-signature=45dae7b1a54930587f8123954664b1b5148b****
Connection: close

<CompleteMultipartUpload>
	<Part>
		<PartNumber>1</PartNumber>
		<ETag>"39270a968a357d24207e9911162507eb"</ETag>
	</Part>
	<Part>
		<PartNumber>2</PartNumber>
		<ETag>"d899fbd1e06109ea2e4550f5751c88d6"</ETag>
	</Part>
	<Part>
		<PartNumber>3</PartNumber>
		<ETag>"762890d6c9a871b7bd136037cb2260cd"</ETag>
	</Part>
</CompleteMultipartUpload>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 378
Connection: close
Date: Wed, 25 Mar 2020 10:07:26 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 2290339086971918696
x-cos-request-id: NWU3YjJkNWVfZDFjODJhMDlfMTk2ODJfMmEyNTA0****

<?xml version="1.0" encoding="UTF-8"?>
<CompleteMultipartUploadResult xmlns="http://www.qcloud.com/document/product/436/7751">
	<Location>http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject</Location>
	<Bucket>examplebucket-1250000000</Bucket>
	<Key>exampleobject</Key>
	<ETag>&quot;aa259a62513358f69e98e72e59856d88-3&quot;</ETag>
</CompleteMultipartUploadResult>
```

#### 案例二：使用服务端加密 SSE-COS

#### 请求

```plaintext
POST /exampleobject?uploadId=1590862540251355295a5c736513d70d42b92bbde4f0fafb5e0ecb314b55aa0018cc9fa76f HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Sat, 30 May 2020 18:16:08 GMT
Content-Type: application/xml
Content-Length: 153
Content-MD5: wmpyfdr9s/A+VCBwDdC1bA==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1590862568;1590869768&q-key-time=1590862568;1590869768&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=uploadid&q-signature=abe1fd2d2c057c8f3e4d331a0448b06ecf5b****
Connection: close

<CompleteMultipartUpload>
	<Part>
		<PartNumber>1</PartNumber>
		<ETag>"108f528eb63b65e734f27ae331f5ffaa"</ETag>
	</Part>
</CompleteMultipartUpload>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 378
Connection: close
Date: Sat, 30 May 2020 18:16:08 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 4510578591875220731
x-cos-request-id: NWVkMmEyZThfYTJjMjJhMDlfMmQzOV8zYTM5****
x-cos-server-side-encryption: AES256

<?xml version="1.0" encoding="UTF-8"?>
<CompleteMultipartUploadResult xmlns="http://www.qcloud.com/document/product/436/7751">
	<Location>http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject</Location>
	<Bucket>examplebucket-1250000000</Bucket>
	<Key>exampleobject</Key>
	<ETag>&quot;915fca1c3b2737c262458b3a1a43c683-1&quot;</ETag>
</CompleteMultipartUploadResult>
```

#### 案例三：使用服务端加密 SSE-KMS

#### 请求

```plaintext
POST /exampleobject?uploadId=15908625793957d71176fa878282d266a95b79dc2aec159b4a73d1d79c80d4f931cda6ad65 HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Sat, 30 May 2020 18:16:40 GMT
Content-Type: application/xml
Content-Length: 153
Content-MD5: jUFgTSZThmPT3qseea0mRQ==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1590862600;1590869800&q-key-time=1590862600;1590869800&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=uploadid&q-signature=68aaf036efac07ef8d6ef101f81a1589849a****
Connection: close

<CompleteMultipartUpload>
	<Part>
		<PartNumber>1</PartNumber>
		<ETag>"1d3e8ae9da423b440341b09f1616f074"</ETag>
	</Part>
</CompleteMultipartUpload>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 378
Connection: close
Date: Sat, 30 May 2020 18:16:40 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 4510578591875220731
x-cos-request-id: NWVkMmEzMDhfYzhjODJhMDlfMjNhYTBfMjdmNjNl****
x-cos-server-side-encryption: cos/kms
x-cos-server-side-encryption-cos-kms-key-id: 48ba38aa-26c5-11ea-855c-52540085****

<?xml version="1.0" encoding="UTF-8"?>
<CompleteMultipartUploadResult xmlns="http://www.qcloud.com/document/product/436/7751">
	<Location>http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject</Location>
	<Bucket>examplebucket-1250000000</Bucket>
	<Key>exampleobject</Key>
	<ETag>&quot;8093dc3e18f7070444e6ca21789eb8d4-1&quot;</ETag>
</CompleteMultipartUploadResult>

```

#### 案例四：使用服务端加密 SSE-C

#### 请求

```plaintext
POST /exampleobject?uploadId=1590862610acd643927bad05cd3947bf98b56b04b0b0b2a45a49969f87cc95b7fd5fcc065a HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Sat, 30 May 2020 18:17:11 GMT
Content-Type: application/xml
Content-Length: 153
Content-MD5: MnXmb3yvrbwMfBlUwUE1Hg==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1590862631;1590869831&q-key-time=1590862631;1590869831&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=uploadid&q-signature=5ce15a35c591eb797e8abaf210313e58ac03****
Connection: close

<CompleteMultipartUpload>
	<Part>
		<PartNumber>1</PartNumber>
		<ETag>"ff14981a35a58eb97bca838b055c573b"</ETag>
	</Part>
</CompleteMultipartUpload>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 378
Connection: close
Date: Sat, 30 May 2020 18:17:11 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 4510578591875220731
x-cos-request-id: NWVkMmEzMjdfODljOTJhMDlfMzQ2ZDNfMWMwZWYy****
x-cos-server-side-encryption-customer-algorithm: AES256
x-cos-server-side-encryption-customer-key-MD5: U5L61r7jcwdNvT7frmUG8g==

<?xml version="1.0" encoding="UTF-8"?>
<CompleteMultipartUploadResult xmlns="http://www.qcloud.com/document/product/436/7751">
	<Location>http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject</Location>
	<Bucket>examplebucket-1250000000</Bucket>
	<Key>exampleobject</Key>
	<ETag>&quot;55973f71e8e892273053617e6b83d1c7-1&quot;</ETag>
</CompleteMultipartUploadResult>
```

#### 案例五：启用版本控制

#### 请求

```plaintext
POST /exampleobject?uploadId=15908626631e1995018f81a5e563837d6d7f1b51d7c97dff09989296403e32366e52f2877b HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Sat, 30 May 2020 18:18:04 GMT
Content-Type: application/xml
Content-Length: 153
Content-MD5: wmpyfdr9s/A+VCBwDdC1bA==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1590862684;1590869884&q-key-time=1590862684;1590869884&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=uploadid&q-signature=5409509944602014d1b61cb4bbe1e39003b4****
Connection: close

<CompleteMultipartUpload>
	<Part>
		<PartNumber>1</PartNumber>
		<ETag>"108f528eb63b65e734f27ae331f5ffaa"</ETag>
	</Part>
</CompleteMultipartUpload>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 378
Connection: close
Date: Sat, 30 May 2020 18:18:04 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 4510578591875220731
x-cos-request-id: NWVkMmEzNWNfOGNjOTJhMDlfMWQ4NjJfMWM0NGUw****
x-cos-version-id: MTg0NDUxNTMyMTEwNDU1NDc3OTc

<?xml version="1.0" encoding="UTF-8"?>
<CompleteMultipartUploadResult xmlns="http://www.qcloud.com/document/product/436/7751">
	<Location>http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject</Location>
	<Bucket>examplebucket-1250000000</Bucket>
	<Key>exampleobject</Key>
	<ETag>&quot;42318fc0ec58952b0d9ab4d7a006f595-1&quot;</ETag>
</CompleteMultipartUploadResult>
```

#### 案例六：暂停版本控制

#### 请求

```plaintext
POST /exampleobject?uploadId=1590862705b4349d597c0db1281e1c666bc431eb468b3a64076be7093c91a963bc5ead2ea4 HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Sat, 30 May 2020 18:18:45 GMT
Content-Type: application/xml
Content-Length: 153
Content-MD5: wmpyfdr9s/A+VCBwDdC1bA==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1590862725;1590869925&q-key-time=1590862725;1590869925&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=uploadid&q-signature=b212e42daaeabcd2b8e9f6722b62fe8d618b****
Connection: close

<CompleteMultipartUpload>
	<Part>
		<PartNumber>1</PartNumber>
		<ETag>"108f528eb63b65e734f27ae331f5ffaa"</ETag>
	</Part>
</CompleteMultipartUpload>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 378
Connection: close
Date: Sat, 30 May 2020 18:18:45 GMT
Server: tencent-cos
x-cos-hash-crc64ecma: 4510578591875220731
x-cos-request-id: NWVkMmEzODVfZjZjMjBiMDlfNGYzZV8zODc4****
x-cos-version-id: null

<?xml version="1.0" encoding="UTF-8"?>
<CompleteMultipartUploadResult xmlns="http://www.qcloud.com/document/product/436/7751">
	<Location>http://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject</Location>
	<Bucket>examplebucket-1250000000</Bucket>
	<Key>exampleobject</Key>
	<ETag>&quot;491509b1fdf8e13d1f51d323c4a6d0e8-1&quot;</ETag>
</CompleteMultipartUploadResult>
```
