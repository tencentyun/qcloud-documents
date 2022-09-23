## 功能描述

PUT Object - Copy 接口请求创建一个已存在 COS 的对象的副本，即将一个对象从源路径（对象键）复制到目标路径（对象键）。建议对象大小为1M到5G，超过5G的对象请使用分块上传 [Upload Part - Copy](https://cloud.tencent.com/document/product/436/8287)。

在复制过程中，可以指定元数据的处理方式。默认情况下元数据将被复制到目标对象中，用户也可以选择不复制源对象的元数据信息，而在此接口请求中指定新的元数据信息。但是，除非在此接口请求中显式指定存储类型、访问控制列表（ACL）和服务端加密（SSE），否则无论何种处理方式，目标对象均保持为标准存储，继承（default）目标存储桶的 ACL 且不会使用 SSE。

用户可以通过此接口实现对象移动、重命名、修改对象元数据和创建副本。

该 API 的请求者需要对被复制对象有读取权限，或者被复制对象向所有人开放了读取权限（公有读），且需要对目标存储桶有写入权限。

> ! 
> - 当 COS 收到复制请求或 COS 正在复制对象时可能会返回错误。如果在复制操作开始之前发生错误，则会收到标准的错误返回。如果在复制操作执行期间发生错误，则依然会返回 HTTP 200 OK，并将错误作为响应体返回。这意味着 HTTP 200 OK 响应既可以包含成功也可以包含错误，在使用此接口时应当进一步根据响应体的内容来判断复制请求的成功与失败并正确的处理结果。
> - 标准存储（多 AZ）类型目前仅支持复制为标准存储（多 AZ）类型，不支持复制为标准存储、低频和归档存储类型。
> - 低频存储（多 AZ）类型目前仅支持复制为低频存储（多 AZ）类型，不支持复制为标准存储、低频和归档存储类型。
> 

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=PutObjectCopy&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>


#### 版本控制

- 如果源对象所在存储桶启用了版本控制，则默认复制源对象的最新版本，可以在请求头部 x-cos-copy-source 中指定 versionId 参数来复制指定版本。
- 如果对目标存储桶启用版本控制，对象存储将自动为目标对象生成唯一的版本 ID。

## 请求

#### 请求示例

```plaintext
PUT /<ObjectKey> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
x-cos-copy-source: <SourceBucketName-SourceAPPID>.cos.<SourceRegion>.myqcloud.com/<SourceObjectKey>
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

| 名称                                  | 描述                                                         | 类型   | 是否必选 |
| ------------------------------------- | ------------------------------------------------------------ | ------ | -------- |
| x-cos-copy-source                     | 源对象的 URL，其中对象键需经过 URLEncode，可以通过 versionId 参数指定源对象的版本，例如：<br>`sourcebucket-1250000001.cos.ap-shanghai.myqcloud.com/example-%E8%85%BE%E8%AE%AF%E4%BA%91.jpg`<br>或`sourcebucket-1250000001.cos.ap-shanghai.myqcloud.com/example-%E8%85%BE%E8%AE%AF%E4%BA%91.jpg?versionId=MTg0NDUxNzYzMDc0NDMzNDExOTc` | string | 是       |
| x-cos-metadata-directive              | 是否复制源对象的元数据信息，枚举值：Copy，Replaced，默认为 Copy。<br><li>如果标记为 Copy，则复制源对象的元数据信息<li>如果标记为 Replaced，则按本次请求的请求头中的元数据信息作为目标对象的元数据信息<br>当目标对象和源对象为同一对象时，即用户试图修改元数据时，则标记必须为 Replaced | Enum   | 否       |
| x-cos-copy-source-If-Modified-Since   | 当对象在指定时间后被修改，则执行复制操作，否则返回 HTTP 状态码为412（Precondition Failed） | string | 否       |
| x-cos-copy-source-If-Unmodified-Since | 当对象在指定时间后未被修改，则执行复制操作，否则返回 HTTP 状态码为412（Precondition Failed） | string | 否       |
| x-cos-copy-source-If-Match            | 当对象的 ETag 与指定的值一致，则执行复制操作，否则返回 HTTP 状态码为412（Precondition Failed） | string | 否       |
| x-cos-copy-source-If-None-Match       | 当对象的 ETag 与指定的值不一致，则执行复制操作，否则返回 HTTP 状态码为412（Precondition Failed） | string | 否       |
| x-cos-storage-class                   | 目标对象的存储类型。枚举值请参见 [存储类型](https://cloud.tencent.com/document/product/436/33417) 文档，例如 INTELLIGENT_TIERING，MAZ_INTELLIGENT_TIERING，STANDARD_IA，ARCHIVE，DEEP_ARCHIVE。默认值：STANDARD | Enum   | 否       |
| x-cos-tagging                         | 对象的标签集合，最多可设置10个标签（例如，Key1=Value1&Key2=Value2）。 标签集合中的 Key 和 Value 必须先进行 URL 编码 | string | 否       |
|  x-cos-tagging-directive  |  是否复制源对象的标签信息，枚举值：Copy，Replaced，默认为 Copy。<br><li>如果标记为 Copy，则复制源对象的标签信息。<br><li>如果标记为 Replaced，则按本次请求的请求头中的标签信息作为目标对象的标签信息<br>当目标对象和源对象为同一对象时，即用户试图修改对象标签时，则标记必须为 Replaced  |  Enum   | 否     |

**目标对象元数据相关头部**

在复制对象时可以通过指定下列请求头部来设置目标对象的元数据信息，此时请求头部 x-cos-metadata-directive 需指定为 Replaced，否则目标对象将使用源对象的元数据信息且不能指定下列任何头部。

| 名称                | 描述                                                         | 类型   | 是否必选 |
| ------------------- | ------------------------------------------------------------ | ------ | -------- |
| Cache-Control       | RFC 2616 中定义的缓存指令，将作为目标对象元数据保存          | string | 否       |
| Content-Disposition | RFC 2616 中定义的文件名称，将作为目标对象元数据保存          | string | 否       |
| Content-Encoding    | RFC 2616 中定义的编码格式，将作为目标对象元数据保存          | string | 否       |
| Content-Type        | RFC 2616 中定义的 HTTP 请求内容类型（MIME），此头部用于描述目标对象的内容类型，将作为目标对象元数据保存。<br>例如 `text/html` 或 `image/jpeg`。 | string | 是       |
| Expires             | RFC 2616 中定义的缓存失效时间，将作为目标对象元数据保存      | string | 否       |
| x-cos-meta-\*       | 包括用户自定义元数据头部后缀和用户自定义元数据信息，将作为目标对象元数据保存，大小限制为2KB<br>**注意：**用户自定义元数据信息支持下划线（_），但用户自定义元数据头部后缀不支持下划线，仅支持减号（-） | string | 否       |

**目标对象访问控制列表（ACL）相关头部**

在复制对象时可以通过指定下列请求头部来设置目标对象的访问权限：

| 名称                     | 描述                                                         | 类型   | 是否必选 |
| ------------------------ | ------------------------------------------------------------ | ------ | -------- |
| x-cos-acl                | 定义目标对象的访问控制列表（ACL）属性。枚举值请参见 [ACL 概述](https://cloud.tencent.com/document/product/436/30752#.E9.A2.84.E8.AE.BE.E7.9A.84-acl) 文档中对象的预设 ACL 部分，例如 default，private，public-read 等，默认为 default<br>**注意：**如果您不需要进行对象 ACL 控制，请设置为 default 或者此项不进行设置，默认继承存储桶权限 | Enum   | 否       |
| x-cos-grant-read         | 赋予被授权者读取目标对象的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如`id="100000000001",id="100000000002"` | string | 否       |
| x-cos-grant-read-acp     | 赋予被授权者读取目标对象的访问控制列表（ACL）的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如`id="100000000001",id="100000000002"` | string | 否       |
| x-cos-grant-write-acp    | 赋予被授权者写入目标对象的访问控制列表（ACL）的权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如`id="100000000001",id="100000000002"` | string | 否       |
| x-cos-grant-full-control | 赋予被授权者操作目标对象的所有权限，格式为 id="[OwnerUin]"，例如 id="100000000001"，可使用半角逗号（,）分隔多组被授权者，例如`id="100000000001",id="100000000002"` | string | 否       |

**源对象服务端加密（SSE）相关头部**

如果源对象使用了服务端加密且加密方式为 SSE-C 时，则需要指定下列请求头部来解密源对象：

| 名称                                                        | 描述                                                         | 类型   | 是否必选&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| ----------------------------------------------------------- | ------------------------------------------------------------ | ------ | ------------------------------------------------------------ |
| x-cos-copy-source-server-side-encryption-customer-algorithm | 服务端加密算法，目前仅支持 AES256                            | string | 源对象使用 SSE-C 时，此头部是必选项                          |
| x-cos-copy-source-server-side-encryption-customer-key       | 服务端加密密钥的 Base64 编码，例如<code>MDEyMzQ1Njc4OUFCQ<br>0RFRjAxMjM0NTY3ODlBQkNERUY=</code> | string | 源对象使用 SSE-C 时，此头部是必选项                          |
| x-cos-copy-source-server-side-encryption-customer-key-MD5   | 服务端加密密钥的 MD5 哈希值，使用 Base64 编码，<br>例如`U5L61r7jcwdNvT7frmUG8g==` | string | 源对象使用 SSE-C 时，此头部是必选项                          |

**目标对象服务端加密（SSE）相关头部**

在复制对象时可以使用服务端加密，请参见 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7728#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8)。

#### 请求体

此接口无请求体。

## 响应

#### 响应头

此接口除返回公共响应头部外，还返回以下响应头部，了解公共响应头部详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

**版本控制相关头部**

当指定了源对象的版本 ID 时，将返回下列响应头部：

| 名称                         | 描述            | 类型   |
| ---------------------------- | --------------- | ------ |
| x-cos-copy-source-version-id | 源对象的版本 ID | string |

**服务端加密（SSE）相关头部**

如果在复制对象时使用了服务端加密，则此接口将返回服务端加密专用头部，请参见 [服务端加密专用头部](https://cloud.tencent.com/document/product/436/7729#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.8A.A0.E5.AF.86.E4.B8.93.E7.94.A8.E5.A4.B4.E9.83.A8)。

#### 响应体

查询成功，返回 **application/xml** 数据，包含对象复制结果信息。

```plaintext
<?xml version="1.0" encoding="UTF-8"?>
<CopyObjectResult>
			<ETag>string</ETag>
			<CRC64>number</CRC64>
			<LastModified>date</LastModified>
			<VersionId>string</VersionId>
</CopyObjectResult>
```

具体的节点描述如下：

| 节点名称（关键字） | 父节点 | 描述                                  | 类型      |
| ------------------ | ------ | ------------------------------------- | --------- |
| CopyObjectResult   | 无     | 保存 PUT Object - Copy 结果的所有信息 | Container |

**Container 节点 CopyObjectResult 的内容：**

| 节点名称（关键字） | 父节点           | 描述                                                         | 类型   |
| ------------------ | ---------------- | ------------------------------------------------------------ | ------ |
| ETag               | CopyObjectResult | 对象的实体标签（Entity Tag），是对象被创建时标识对象内容的信息标签，可用于检查对象的内容是否发生变化。<br>例如`8e0b617ca298a564c3331da28dcb50df`，此头部并不一定返回对象的 MD5 值，而是根据对象上传和加密方式而有所不同 | string |
| CRC64              | CopyObjectResult | 对象的 CRC64 值，详情请参见 [CRC64 校验](https://cloud.tencent.com/document/product/436/40334) 文档 | number |
| LastModified       | CopyObjectResult | 对象最后修改时间，为 ISO8601 格式，例如`2019-05-24T10:56:40Z` | date   |
| VersionId          | CopyObjectResult | 对象的版本 ID，仅当目标存储桶启用了版本控制时才返回该元素    | string |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

此接口响应默认为 Transfer-Encoding: chunked 编码方式，为了方便阅读，本文档实际案例均采用无 Transfer-Encoding 的方式展示，在使用过程中，不同语言和库可以自动处理这种编码形式，请开发者注意识别和处理，更多信息请查阅语言和库的相关文档。

#### 案例一：简单案例

#### 请求

```plaintext
PUT /exampleobject HTTP/1.1
Host: destinationbucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 18:20:30 GMT
x-cos-copy-source: sourcebucket-1250000001.cos.ap-shanghai.myqcloud.com/example-%E8%85%BE%E8%AE%AF%E4%BA%91.jpg
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586542830;1586550030&q-key-time=1586542830;1586550030&q-header-list=content-length;date;host;x-cos-copy-source&q-url-param-list=&q-signature=f91b02809317616d993e14625996e416e08e****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 219
Connection: close
Date: Fri, 10 Apr 2020 18:20:30 GMT
Server: tencent-cos
x-cos-request-id: NWU5MGI4ZWVfNzljMDBiMDlfMWM3MjlfMWQ1****



<?xml version="1.0" encoding="UTF-8"?>
<CopyObjectResult>
			<ETag>"ee8de918d05640145b18f70f4c3aa602"</ETag>
			<CRC64>16749565679157681890</CRC64>
			<LastModified>2020-04-10T18:20:30Z</LastModified>
</CopyObjectResult>
```

#### 案例二：复制时替换元数据

#### 请求

```plaintext
PUT /exampleobject HTTP/1.1
Host: destinationbucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 18:20:41 GMT
x-cos-metadata-directive: Replaced
Content-Type: application/octet-stream
Content-Disposition: attachment; filename=example.jpg
x-cos-copy-source: sourcebucket-1250000001.cos.ap-shanghai.myqcloud.com/example-%E8%85%BE%E8%AE%AF%E4%BA%91.jpg
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586542841;1586550041&q-key-time=1586542841;1586550041&q-header-list=content-disposition;content-length;content-type;date;host;x-cos-copy-source;x-cos-metadata-directive&q-url-param-list=&q-signature=aa2522c12b0ac82e29a812fca4334705cc96****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 219
Connection: close
Date: Fri, 10 Apr 2020 18:20:41 GMT
Server: tencent-cos
x-cos-request-id: NWU5MGI4ZjlfYTZjMDBiMDlfN2Y1YV8xYjI4****



<?xml version="1.0" encoding="UTF-8"?>
<CopyObjectResult>
			<ETag>"ee8de918d05640145b18f70f4c3aa602"</ETag>
			<CRC64>16749565679157681890</CRC64>
			<LastModified>2020-04-10T18:20:41Z</LastModified>
</CopyObjectResult>
```

#### 案例三：修改对象元数据

#### 请求

```plaintext
PUT /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 18:20:52 GMT
x-cos-metadata-directive: Replaced
Cache-Control: max-age=86400
Content-Type: image/jpeg
x-cos-copy-source: examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586542852;1586550052&q-key-time=1586542852;1586550052&q-header-list=cache-control;content-length;content-type;date;host;x-cos-copy-source;x-cos-metadata-directive&q-url-param-list=&q-signature=1bcab704e474e46359d97c8c1fbb93642069****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 219
Connection: close
Date: Fri, 10 Apr 2020 18:20:52 GMT
Server: tencent-cos
x-cos-request-id: NWU5MGI5MDRfNmRjMDJhMDlfZGNmYl8yMDVh****



<?xml version="1.0" encoding="UTF-8"?>
<CopyObjectResult>
			<ETag>"ee8de918d05640145b18f70f4c3aa602"</ETag>
			<CRC64>16749565679157681890</CRC64>
			<LastModified>2020-04-10T18:20:52Z</LastModified>
</CopyObjectResult>
```

#### 案例四：修改对象存储类型

本案例演示将对象从标准存储转换为归档存储，该使用方法也适合标准存储与低频存储之间的互相转换，如果希望将归档存储或深度归档存储的对象转换为其他存储类型，需要首先使用 [POST Object restore](https://cloud.tencent.com/document/product/436/12633) 将归档存储或深度归档存储的对象回热，才能使用该接口请求转换存储类型。

#### 请求

```plaintext
PUT /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 18:21:02 GMT
x-cos-metadata-directive: Replaced
x-cos-storage-class: ARCHIVE
x-cos-copy-source: examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586542862;1586550062&q-key-time=1586542862;1586550062&q-header-list=content-length;date;host;x-cos-copy-source;x-cos-metadata-directive;x-cos-storage-class&q-url-param-list=&q-signature=8726a359b342cb1cace6945812ee8379c3ad****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 219
Connection: close
Date: Fri, 10 Apr 2020 18:21:02 GMT
Server: tencent-cos
x-cos-request-id: NWU5MGI5MGVfN2RiNDBiMDlfMTk1MjhfMWZm****



<?xml version="1.0" encoding="UTF-8"?>
<CopyObjectResult>
			<ETag>"ee8de918d05640145b18f70f4c3aa602"</ETag>
			<CRC64>16749565679157681890</CRC64>
			<LastModified>2020-04-10T18:21:55Z</LastModified>
</CopyObjectResult>
```

#### 案例五：将未加密的对象复制为使用 SSE-COS 加密的目标对象

#### 请求

```plaintext
PUT /exampleobject HTTP/1.1
Host: destinationbucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 18:21:12 GMT
x-cos-server-side-encryption: AES256
x-cos-copy-source: sourcebucket-1250000001.cos.ap-shanghai.myqcloud.com/example-%E8%85%BE%E8%AE%AF%E4%BA%91.jpg
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586542872;1586550072&q-key-time=1586542872;1586550072&q-header-list=content-length;date;host;x-cos-copy-source;x-cos-server-side-encryption&q-url-param-list=&q-signature=ee94ef60dfb512882b368be12c6d47526433****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 219
Connection: close
Date: Fri, 10 Apr 2020 18:21:13 GMT
Server: tencent-cos
x-cos-request-id: NWU5MGI5MTlfYmIwMmEwOV9hMmUxXzFkMDQ2****
x-cos-server-side-encryption: AES256



<?xml version="1.0" encoding="UTF-8"?>
<CopyObjectResult>
			<ETag>"ee8de918d05640145b18f70f4c3aa602"</ETag>
			<CRC64>16749565679157681890</CRC64>
			<LastModified>2020-04-10T18:21:13Z</LastModified>
</CopyObjectResult>
```

#### 案例六：将未加密的对象复制为使用 SSE-KMS 加密的目标对象

#### 请求

```plaintext
PUT /exampleobject HTTP/1.1
Host: destinationbucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 18:21:23 GMT
x-cos-server-side-encryption: cos/kms
x-cos-server-side-encryption-cos-kms-key-id: 48ba38aa-26c5-11ea-855c-52540085****
x-cos-server-side-encryption-context: eyJhdXRob3IiOiJmeXNudGlhbiIsImNvbXBhbnkiOiJUZW5jZW50In0=
x-cos-copy-source: sourcebucket-1250000001.cos.ap-shanghai.myqcloud.com/example-%E8%85%BE%E8%AE%AF%E4%BA%91.jpg
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586542883;1586550083&q-key-time=1586542883;1586550083&q-header-list=content-length;date;host;x-cos-copy-source;x-cos-server-side-encryption;x-cos-server-side-encryption-context;x-cos-server-side-encryption-cos-kms-key-id&q-url-param-list=&q-signature=28055a7cf07d7dde858fd924d6c0963b0c68****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 219
Connection: close
Date: Fri, 10 Apr 2020 18:21:23 GMT
Server: tencent-cos
x-cos-request-id: NWU5MGI5MjNfMTliOTJhMDlfMjRiYThfMTdk****
x-cos-server-side-encryption: cos/kms
x-cos-server-side-encryption-cos-kms-key-id: 48ba38aa-26c5-11ea-855c-52540085****



<?xml version="1.0" encoding="UTF-8"?>
<CopyObjectResult>
			<ETag>"f69901ec9755a5defc29057e9ec69126"</ETag>
			<CRC64>16749565679157681890</CRC64>
			<LastModified>2020-04-10T18:22:16Z</LastModified>
</CopyObjectResult>
```

#### 案例七：复制 SSE-C 加密的对象并更换密钥

#### 请求

```plaintext
PUT /exampleobject HTTP/1.1
Host: destinationbucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 18:21:44 GMT
x-cos-copy-source-server-side-encryption-customer-algorithm: AES256
x-cos-copy-source-server-side-encryption-customer-key: MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=
x-cos-copy-source-server-side-encryption-customer-key-MD5: U5L61r7jcwdNvT7frmUG8g==
x-cos-server-side-encryption-customer-algorithm: AES256
x-cos-server-side-encryption-customer-key: MDEyMzQ1Njc4OWFiY2RlZjAxMjM0NTY3ODlhYmNkZWY=
x-cos-server-side-encryption-customer-key-MD5: hRasmdxgYDKV3nvbahU1MA==
x-cos-copy-source: sourcebucket-1250000001.cos.ap-shanghai.myqcloud.com/example-%E8%85%BE%E8%AE%AF%E4%BA%91.jpg
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586542904;1586550104&q-key-time=1586542904;1586550104&q-header-list=content-length;date;host;x-cos-copy-source;x-cos-copy-source-server-side-encryption-customer-algorithm;x-cos-copy-source-server-side-encryption-customer-key;x-cos-copy-source-server-side-encryption-customer-key-md5;x-cos-server-side-encryption-customer-algorithm;x-cos-server-side-encryption-customer-key;x-cos-server-side-encryption-customer-key-md5&q-url-param-list=&q-signature=dece274320f748bb0c736b13e5409cd1c35f****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 219
Connection: close
Date: Fri, 10 Apr 2020 18:21:44 GMT
Server: tencent-cos
x-cos-request-id: NWU5MGI5MzhfZmFjODJhMDlfMTdlYzZfYmU1****
x-cos-server-side-encryption-customer-algorithm: AES256
x-cos-server-side-encryption-customer-key-MD5: hRasmdxgYDKV3nvbahU1MA==



<?xml version="1.0" encoding="UTF-8"?>
<CopyObjectResult>
			<ETag>"bf314b89d34119395d5610982d6581b1"</ETag>
			<CRC64>16749565679157681890</CRC64>
			<LastModified>2020-04-10T18:22:31Z</LastModified>
</CopyObjectResult>
```

#### 案例八：将 SSE-C 加密的对象修改为不加密

#### 请求

```plaintext
PUT /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Apr 2020 18:22:05 GMT
x-cos-metadata-directive: Replaced
x-cos-copy-source-server-side-encryption-customer-algorithm: AES256
x-cos-copy-source-server-side-encryption-customer-key: MDEyMzQ1Njc4OUFCQ0RFRjAxMjM0NTY3ODlBQkNERUY=
x-cos-copy-source-server-side-encryption-customer-key-MD5: U5L61r7jcwdNvT7frmUG8g==
x-cos-copy-source: examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586542925;1586550125&q-key-time=1586542925;1586550125&q-header-list=content-length;date;host;x-cos-copy-source;x-cos-copy-source-server-side-encryption-customer-algorithm;x-cos-copy-source-server-side-encryption-customer-key;x-cos-copy-source-server-side-encryption-customer-key-md5;x-cos-metadata-directive&q-url-param-list=&q-signature=b57bc8f6d666e9d722d30ad7d3ab442d9c43****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 219
Connection: close
Date: Fri, 10 Apr 2020 18:22:05 GMT
Server: tencent-cos
x-cos-request-id: NWU5MGI5NGRfOWFjOTJhMDlfMjg2NDdfMTA0****



<?xml version="1.0" encoding="UTF-8"?>
<CopyObjectResult>
			<ETag>"ee8de918d05640145b18f70f4c3aa602"</ETag>
			<CRC64>16749565679157681890</CRC64>
			<LastModified>2020-04-10T18:22:58Z</LastModified>
</CopyObjectResult>
```

#### 案例九：指定源对象的版本

#### 请求

```plaintext
PUT /exampleobject HTTP/1.1
Host: destinationbucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Sat, 11 Apr 2020 17:51:35 GMT
x-cos-copy-source: sourcebucket-1250000001.cos.ap-shanghai.myqcloud.com/example.jpg?versionId=MTg0NDUxNTc0NDYyMjQ2MzUzMjQ
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586627495;1586634695&q-key-time=1586627495;1586634695&q-header-list=content-length;date;host;x-cos-copy-source&q-url-param-list=&q-signature=da80bd079b2c1fdb0dd961dea8568ee8d998****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 219
Connection: close
Date: Sat, 11 Apr 2020 17:51:35 GMT
Server: tencent-cos
x-cos-copy-source-version-id: MTg0NDUxNTc0NDYyMjQ2MzUzMjQ
x-cos-request-id: NWU5MjAzYTdfMWZjMDJhMDlfNTE4N18zNGU2****



<?xml version="1.0" encoding="UTF-8"?>
<CopyObjectResult>
			<ETag>"ee8de918d05640145b18f70f4c3aa602"</ETag>
			<CRC64>16749565679157681890</CRC64>
			<LastModified>2020-04-11T17:51:35Z</LastModified>
</CopyObjectResult>
```

#### 案例十：复制对象到启用版本控制的存储桶

#### 请求

```plaintext
PUT /exampleobject HTTP/1.1
Host: destinationbucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Sat, 11 Apr 2020 17:51:56 GMT
x-cos-copy-source: sourcebucket-1250000001.cos.ap-shanghai.myqcloud.com/example.jpg
Content-Length: 0
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1586627516;1586634716&q-key-time=1586627516;1586634716&q-header-list=content-length;date;host;x-cos-copy-source&q-url-param-list=&q-signature=2c79d63b6078ace6fc9430fb6533b9a9ade1****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 272
Connection: close
Date: Sat, 11 Apr 2020 17:51:56 GMT
Server: tencent-cos
x-cos-request-id: NWU5MjAzYmNfNjRiMDJhMDlfOTE3N18yYWI4****



<?xml version="1.0" encoding="UTF-8"?>
<CopyObjectResult>
			<ETag>"22e024392de860289f0baa7d6cf8a549"</ETag>
			<CRC64>11596229263574363878</CRC64>
			<LastModified>2020-04-11T17:51:56Z</LastModified>
			<VersionId>MTg0NDUxNTc0NDYxOTI4MzU0MDI</VersionId>
</CopyObjectResult>
```

