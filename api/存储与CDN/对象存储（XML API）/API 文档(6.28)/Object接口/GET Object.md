## 功能描述
GET Object 接口请求可以在 COS 的存储桶中将一个文件（对象）下载至本地。该操作需要请求者对目标对象具有读权限或目标对象对所有人都开放了读权限（公有读）。

### 版本
当启用多版本，该 GET 操作返回对象的当前版本。要返回不同的版本，请使用 versionId 参数。

>**注意**
如果该对象的当前版本是删除标记，则 COS 的行为表现为该对象不存在，并返回响应 x-cos-delete-marker: true。

## 请求

请求示例：
```
GET /<ObjectName> HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求行

```
GET /{ObjectName} HTTP/1.1
```

该 API 接口接受 `GET` 请求。

#### 请求参数


| 名称                         | 类型   | 必选 | 描述                                      |
| ---------------------------- | ------ | ---- | ----------------------------------------- |
| response-content-type        | string | 否   | 设置响应头部中的 Content-Type 参数        |
| response-content-language    | string | 否   | 设置响应头部中的 Content-Language 参数    |
| response-expires             | string | 否   | 设置响应头部中的 Content-Expires 参数     |
| response-cache-control       | string | 否   | 设置响应头部中的 Cache-Control 参数       |
| response-content-disposition | string | 否   | 设置响应头部中的 Content-Disposition 参数 |
| response-content-encoding    | string | 否   | 设置响应头部中的 Content-Encoding 参数    |

### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728 "公共请求头部") 章节。

#### 非公共头部

| 名称                | 类型   | 必选 | 描述                                                         |
| ------------------- | ------ | ---- | ------------------------------------------------------------ |
| Range               | string | 否   | RFC 2616 中定义的指定文件下载范围，以字节（bytes）为单位     |
| If-Unmodified-Since | string | 否   | 如果文件修改时间早于或等于指定时间，才返回文件内容。否则返回 412 (precondition failed) |
| If-Modified-Since   | string | 否   | 当 Object 在指定时间后被修改，则返回对应 Object meta 信息，否则返回 304(not modified) |
| If-Match            | string | 否   | 当 ETag 与指定的内容一致，才返回文件。否则返回 412 (precondition failed) |
| If-None-Match       | string | 否   | 当 ETag 与指定的内容不一致，才返回文件。否则返回 304 (not modified) |

### 请求体

该请求请求体为空。

## 响应

### 响应头

#### 公共响应头

该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729 "公共响应头部") 章节。

#### 特有响应头

该请求操作的响应头具体数据为：

|名称|类型|描述|
|---|---|---|
|x-cos-meta- *|string|用户自定义的元数据|
|x-cos-object-type|string|用来表示 Object 是否可以被追加上传，枚举值：normal 或者 appendable|
|x-cos-storage-class|string|Object 的存储级别，枚举值：STANDARD，STANDARD_IA|
|x-cos-version-id|string|如果检索到的对象具有唯一的版本ID，则返回版本ID。|
|x-cos-server-side​-encryption|string|如果通过 COS 管理的服务端加密来存储对象，响应将包含此头部和所使用的加密算法的值，AES256。|


### 响应体

下载成功，文件内容在响应体中。

### 错误码

| 错误码                | 描述                               | HHTP 状态码                                                  |
| --------------------- | ---------------------------------- | ------------------------------------------------------------ |
| InvalidArgument       | 提供的参数错误                     | 400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1) |
| SignatureDoesNotMatch | 提供的签名不符合规则，返回该错误码 | 403 [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3) |
| NoSuchKey             | 如果下载的文件不存在，返回该错误码 | 404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4) |

## 实际案例

### 请求一

```
GET /123 HTTP/1.1
Host: zuhaotestnorth-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 28 Oct 2014 22:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484212200;32557108200&q-key-time=1484212200;32557108200&q-header-list=host&q-url-param-list=&q-signature=11522aa3346819b7e5e841507d5b7f156f34e639
```

### 响应一

```
HTTP/1.1 200 OK
Date: Wed, 28 Oct 2014 22:32:00 GMT
Content-Type: application/octet-stream
Content-Length: 16087
Connection: keep-alive
Accept-Ranges: bytes
Content-Disposition: attachment; filename=\"filename.jpg\"
Content-Range: bytes 0-16086/16087
ETag: \"9a4802d5c99dafe1c04da0a8e7e166bf\"
Last-Modified: Wed, 28 Oct 2014 20:30:00 GMT
x-cos-object-type: normal
x-cos-request-id: NTg3NzQ3ZmVfYmRjMzVfMzE5N182NzczMQ==
x-cos-storage-class: STANDARD

[Object]
```

### 请求二

**携带 response-xxx 参数**

```
GET /123?response-content-type=application%2fxml HTTP/1.1
Host: zuhaotestnorth-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 28 Oct 2014 22:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484212200;32557108200&q-key-time=1484212200;32557108200&q-header-list=host&q-url-param-list=&q-signature=11522aa3346819b7e5e841507d5b7f156f34e639

```

### 响应二

```
HTTP/1.1 200 OK
Date: Wed, 28 Oct 2014 22:32:00 GMT
Content-Type: application/xml
Content-Length: 16087
Connection: keep-alive
Accept-Ranges: bytes
Content-Disposition: attachment; filename=\"filename.jpg\"
Content-Range: bytes 0-16086/16087
ETag: \"9a4802d5c99dafe1c04da0a8e7e166bf\"
Last-Modified: Wed, 28 Oct 2014 20:30:00 GMT
x-cos-object-type: normal
x-cos-request-id: NTg3NzQ3ZmVfYmRjMzVfMzE5N182NzczMQ==
x-cos-storage-class: STANDARD

[Object]
```

