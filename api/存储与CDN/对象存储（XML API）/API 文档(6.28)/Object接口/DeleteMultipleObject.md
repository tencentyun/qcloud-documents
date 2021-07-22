## 功能描述

DELETE Multiple Objects 接口请求可以批量删除指定存储桶中的多个对象（Object），单次请求支持最多删除1000个对象。对于响应结果，COS 提供 Quiet 模式和 Verbose 模式：

- Quiet 模式在响应中仅包含删除失败的对象信息和错误信息。
- Verbose 模式在响应中包含每个对象的删除结果信息。

该 API 的请求者需要对存储桶有写入权限。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=DeleteMultipleObjects&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>


#### 版本控制

当启用版本控制时，该请求操作可以为每一个要删除的对象指定版本 ID，此时将永久删除对象的指定版本或指定删除标记，否则将创建一个删除标记作为指定对象的最新版本。

当针对某个对象的删除操作创建或删除了删除标记，那么该对象的删除结果将同时返回 &lt;DeleteMarker>true&lt;/DeleteMarker&gt; 和 &lt;DeleteMarkerVersionId&gt; 元素，代表该请求操作创建或删除了指定对象的删除标记。

当针对某个对象的删除操作永久删除了特定的版本 ID（包括删除标记的版本 ID），那么该对象的删除结果将返回 &lt;VersionId&gt; 元素，代表该请求操作删除的版本 ID。

## 请求

#### 请求示例

```plaintext
POST /?delete HTTP/1.1
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

此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

提交 **application/xml** 请求数据，包含要删除的对象信息。

```xml
<Delete>
	<Quiet>boolean</Quiet>
	<Object>
		<Key>string</Key>
	</Object>
	<Object>
		<Key>string</Key>
		<VersionId>string</VersionId>
	</Object>
</Delete>
```

具体的节点描述如下：

| 节点名称（关键字） | 父节点 | 描述                                            | 类型      | 是否必选 |
| ------------------ | ------ | ----------------------------------------------- | --------- | -------- |
| Delete             | 无     | 包含 DELETE Multiple Objects 操作的所有请求信息 | Container | 是       |

**Container 节点 Delete 的内容：**

| 节点名称（关键字） | 父节点 | 描述                                                         | 类型      | 是否必选 |
| ------------------ | ------ | ------------------------------------------------------------ | --------- | -------- |
| Quiet              | Delete | 布尔值，默认为 false <br><li>true 为使用 Quiet 模式，在响应中仅包含删除失败的对象信息和错误信息<br><li>false 为使用 Verbose 模式，在响应中包含每个对象的删除结果 | boolean   | 是       |
| Object             | Delete | 单个要删除的目标对象的信息                                   | Container | 是       |

**Container 节点 Object 的内容：**

| 节点名称（关键字）                                           | 父节点        | 描述                                                         | 类型   | 是否必选 |
| ------------------------------------------------------------ | ------------- | ------------------------------------------------------------ | ------ | -------- |
| Key&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | Delete.Object | 要删除的目标对象的对象键                                     | string | 是       |
| VersionId                                                    | Delete.Object | 当启用版本控制并且要删除对象的指定版本时需指定该元素，值为要删除的版本 ID。若未开启版本控制或开启版本控制但需要插入删除标记，则无需指定该元素 | string | 是       |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

请求成功，返回 **application/xml** 数据，包含删除结果信息。

```xml
<DeleteResult>
	<Deleted>
		<Key>string</Key>
		<DeleteMarker>boolean</DeleteMarker>
		<DeleteMarkerVersionId>string</DeleteMarkerVersionId>
	</Deleted>
	<Deleted>
		<Key>string</Key>
		<VersionId>string</VersionId>
	</Deleted>
	<Deleted>
		<Key>string</Key>
		<DeleteMarker>boolean</DeleteMarker>
		<DeleteMarkerVersionId>string</DeleteMarkerVersionId>
		<VersionId>string</VersionId>
	</Deleted>
	<Error>
		<Key>string</Key>
		<VersionId>string</VersionId>
		<Code>string</Code>
		<Message>string</Message>
	</Error>
</DeleteResult>
```

具体的节点描述如下：

| 节点名称（关键字） | 父节点 | 描述                                        | 类型      |
| ------------------ | ------ | ------------------------------------------- | --------- |
| DeleteResult       | 无     | 保存 DELETE Multiple Objects 结果的所有信息 | Container |

**Container 节点 DeleteResult 的内容：**

| 节点名称（关键字） | 父节点       | 描述                                                        | 类型      |
| ------------------ | ------------ | ----------------------------------------------------------- | --------- |
| Deleted            | DeleteResult | 单个删除成功的对象条目，仅当使用 Verbose 模式才会返回该元素 | Container |
| Error              | DeleteResult | 单个删除失败的对象条目                                      | Container |

**Container 节点 Deleted 的内容：**

| 节点名称（关键字）    | 父节点               | 描述                                                         | 类型    |
| --------------------- | -------------------- | ------------------------------------------------------------ | ------- |
| Key                   | DeleteResult.Deleted | 删除成功的对象的对象键                                       | string  |
| DeleteMarker          | DeleteResult.Deleted | 仅当对该对象的删除创建了一个删除标记，或删除的是该对象的一个删除标记时才返回该元素，布尔值，固定为 true | boolean |
| DeleteMarkerVersionId | DeleteResult.Deleted | 仅当对该对象的删除创建了一个删除标记，或删除的是该对象的一个删除标记时才返回该元素，值为创建或删除的删除标记的版本 ID | string  |
| VersionId             | DeleteResult.Deleted | 删除成功的版本 ID，仅当请求中指定了要删除对象的版本 ID 时才返回该元素 | string  |

**Container 节点 Error 的内容：**

| 节点名称（关键字） | 父节点             | 描述                                                         | 类型   |
| ------------------ | ------------------ | ------------------------------------------------------------ | ------ |
| Key                | DeleteResult.Error | 删除失败的对象的对象键                                       | string |
| VersionId          | DeleteResult.Error | 删除失败的版本 ID，仅当请求中指定了要删除对象的版本 ID 时才返回该元素 | string |
| Code               | DeleteResult.Error | 删除失败的错误码，用来定位唯一的错误条件和确定错误场景       | string |
| Message            | DeleteResult.Error | 删除失败的具体错误信息                                       | string |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：简单案例

#### 请求

```plaintext
POST /?delete HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Tue, 20 Aug 2019 11:59:35 GMT
Content-Type: application/xml
Content-Length: 158
Content-MD5: zUd/xgzNGDrqJMJUOWV2AQ==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1566302375;1566309575&q-key-time=1566302375;1566309575&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=delete&q-signature=82f77c745ca66fe8c5d93274b3fc44fb895c****
Connection: close

<Delete>
	<Quiet>false</Quiet>
	<Object>
		<Key>example-object-1.jpg</Key>
	</Object>
	<Object>
		<Key>example-object-2.jpg</Key>
	</Object>
</Delete>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 144
Connection: close
Date: Tue, 20 Aug 2019 11:59:35 GMT
Server: tencent-cos
x-cos-request-id: NWQ1YmUwYTdfM2FiMDJhMDlfYzczN18zMGM1****

<DeleteResult>
	<Deleted>
		<Key>example-object-1.jpg</Key>
	</Deleted>
	<Deleted>
		<Key>example-object-2.jpg</Key>
	</Deleted>
</DeleteResult>
```

#### 案例二：简单案例（Quiet 模式）

#### 请求

```plaintext
POST /?delete HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Tue, 20 Aug 2019 12:12:26 GMT
Content-Type: application/xml
Content-Length: 157
Content-MD5: +iI9kJvM2k/y5y3nHcn8BQ==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1566303146;1566310346&q-key-time=1566303146;1566310346&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=delete&q-signature=16581dcc0ae999ce343488de2449436ee182****
Connection: close

<Delete>
	<Quiet>true</Quiet>
	<Object>
		<Key>example-object-1.jpg</Key>
	</Object>
	<Object>
		<Key>example-object-2.jpg</Key>
	</Object>
</Delete>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 15
Connection: close
Date: Tue, 20 Aug 2019 12:12:27 GMT
Server: tencent-cos
x-cos-request-id: NWQ1YmUzYWFfMTljMDJhMDlfNTg3ZV8zNDI0****

<DeleteResult/>
```

#### 案例三：启用版本控制（创建删除标记）

#### 请求

```plaintext
POST /?delete HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 21 Aug 2019 12:04:03 GMT
Content-Type: application/xml
Content-Length: 100
Content-MD5: MowFtlG7iwK7Wmk79IVXFA==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1566389043;1566396243&q-key-time=1566389043;1566396243&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=delete&q-signature=b1aee84c567b16e5e6c8634c2760a0e5d348****
Connection: close

<Delete>
	<Quiet>false</Quiet>
	<Object>
		<Key>example-object-1.jpg</Key>
	</Object>
</Delete>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 200
Connection: close
Date: Wed, 21 Aug 2019 12:04:03 GMT
Server: tencent-cos
x-cos-request-id: NWQ1ZDMzMzNfNDhiNDBiMDlfMmIzNzZfMTBh****

<DeleteResult>
	<Deleted>
		<Key>example-object-1.jpg</Key>
		<DeleteMarker>true</DeleteMarker>
		<DeleteMarkerVersionId>MTg0NDUxNzc2ODQ2NjU3ODM4NTc</DeleteMarkerVersionId>
	</Deleted>
</DeleteResult>
```

#### 案例四：删除指定版本

#### 请求

```plaintext
POST /?delete HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 21 Aug 2019 11:24:43 GMT
Content-Type: application/xml
Content-Length: 154
Content-MD5: EwFydeQSMzaHWi0qMTOGWw==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1566386683;1566393883&q-key-time=1566386683;1566393883&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=delete&q-signature=2b6261e526960a433124b752fd21a7a9a363****
Connection: close

<Delete>
	<Quiet>false</Quiet>
	<Object>
		<Key>example-object-2.jpg</Key>
		<VersionId>MTg0NDUxNzc2ODcwMjYyNjIwMTM</VersionId>
	</Object>
</Delete>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 140
Connection: close
Date: Wed, 21 Aug 2019 11:24:44 GMT
Server: tencent-cos
x-cos-request-id: NWQ1ZDI5ZmJfNDhiNDBiMDlfMmIzODNfMTA0****

<DeleteResult>
	<Deleted>
		<Key>example-object-2.jpg</Key>
		<VersionId>MTg0NDUxNzc2ODcwMjYyNjIwMTM</VersionId>
	</Deleted>
</DeleteResult>
```

#### 案例五：删除指定删除标记

#### 请求

```plaintext
POST /?delete HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 21 Aug 2019 12:04:04 GMT
Content-Type: application/xml
Content-Length: 154
Content-MD5: EKphCPpHcKiVqJtMqE+DmA==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1566389044;1566396244&q-key-time=1566389044;1566396244&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=delete&q-signature=f6b49a9b98386632b9545a4cc087449f789f****
Connection: close

<Delete>
	<Quiet>false</Quiet>
	<Object>
		<Key>example-object-1.jpg</Key>
		<VersionId>MTg0NDUxNzc2ODQ2NjU3ODM4NTc</VersionId>
	</Object>
</Delete>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 253
Connection: close
Date: Wed, 21 Aug 2019 12:04:04 GMT
Server: tencent-cos
x-cos-request-id: NWQ1ZDMzMzRfYmIwMmEwOV83YTQzXzEyM2Ri****

<DeleteResult>
	<Deleted>
		<Key>example-object-1.jpg</Key>
		<DeleteMarker>true</DeleteMarker>
		<DeleteMarkerVersionId>MTg0NDUxNzc2ODQ2NjU3ODM4NTc</DeleteMarkerVersionId>
		<VersionId>MTg0NDUxNzc2ODQ2NjU3ODM4NTc</VersionId>
	</Deleted>
</DeleteResult>
```

#### 案例六：部分删除失败

#### 请求

```plaintext
POST /?delete HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 21 Aug 2019 12:04:05 GMT
Content-Type: application/xml
Content-Length: 436
Content-MD5: ZAbgvje31aO+0j7pkEkYvQ==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1566389045;1566396245&q-key-time=1566389045;1566396245&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=delete&q-signature=543a9f9f65c45e533a415afe5d014cdc9c73****
Connection: close

<Delete>
	<Quiet>false</Quiet>
	<Object>
		<Key>example-object-1.jpg</Key>
	</Object>
	<Object>
		<Key>example-object-2.jpg</Key>
		<VersionId>MTg0NDUxNzc2ODQ2NjQ1MjM5MTk</VersionId>
	</Object>
	<Object>
		<Key>example-object-3.jpg</Key>
		<VersionId>MTg0NDUxNzc2ODQ2NjQwMTIwMDI</VersionId>
	</Object>
	<Object>
		<Key>example-object-4.jpg</Key>
		<VersionId>MTg0NDUxNzc2ODQ2NjQ0NjI0MDQ</VersionId>
	</Object>
</Delete>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 703
Connection: close
Date: Wed, 21 Aug 2019 12:04:06 GMT
Server: tencent-cos
x-cos-request-id: NWQ1ZDMzMzVfOTNjMjJhMDlfMzhiM18xMWY3****

<DeleteResult>
	<Deleted>
		<Key>example-object-1.jpg</Key>
		<DeleteMarker>true</DeleteMarker>
		<DeleteMarkerVersionId>MTg0NDUxNzc2ODQ2NjM1NTI2NDY</DeleteMarkerVersionId>
	</Deleted>
	<Deleted>
		<Key>example-object-2.jpg</Key>
		<VersionId>MTg0NDUxNzc2ODQ2NjQ1MjM5MTk</VersionId>
	</Deleted>
	<Deleted>
		<Key>example-object-3.jpg</Key>
		<DeleteMarker>true</DeleteMarker>
		<DeleteMarkerVersionId>MTg0NDUxNzc2ODQ2NjQwMTIwMDI</DeleteMarkerVersionId>
		<VersionId>MTg0NDUxNzc2ODQ2NjQwMTIwMDI</VersionId>
	</Deleted>
	<Error>
		<Key>example-object-4.jpg</Key>
		<VersionId>MTg0NDUxNzc2ODQ2NjQ0NjI0MDQ</VersionId>
		<Code>PathConflict</Code>
		<Message>Path conflict.</Message>
	</Error>
</DeleteResult>
```
