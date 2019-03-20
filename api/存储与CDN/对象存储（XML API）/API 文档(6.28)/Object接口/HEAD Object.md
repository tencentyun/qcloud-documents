## 功能描述
HEAD Object 接口请求可以获取对应 Object 的 meta 信息数据，HEAD 的权限与 GET 的权限一致。

### 版本

默认情况下，HEAD 操作从当前版本的对象中检索元数据。如要从不同版本检索元数据，请使用 versionId 子资源。

## 请求
### 请求示例

```shell
HEAD /<ObjectKey> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String（详情请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求头
#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部

名称|类型|必选|描述
---|---|---|---
If-Modified-Since|string|否|当 Object 在指定时间后被修改，则返回对应 Object 的 meta 信息，否则返回304

### 请求体
该请求请求体为空。

## 响应
### 响应头

#### 公共响应头

该响应使用公共响应头，了解公共响应头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

该请求操作的响应头具体数据为：

|名称|描述|类型|
|---|---|---|
|x-cos-meta- *|用户自定义的 meta|string|
|x-cos-object-type|用来表示 Object 是否可以被追加上传，枚举值：normal|string|
|x-cos-storage-class|Object 的存储级别，枚举值：STANDARD，STANDARD_IA，ARCHIVE|string|
|x-cos-version-id|返回的对象的版本 ID|string|
|x-cos-restore|如果对象是归档类型，且归档对象在恢复期间中（请参阅 [POST Object restore](https://cloud.tencent.com/document/product/436/12633)）或已经还原归档副本，则响应将包含此响应头部。<br>如果已恢复归档副本，则标头值指示删除该临时副本的时间。例如，x-cos-restore: ongoing-request="false", expiry-date="Fri, 15 Dec 2018 00:00:00 GMT"。如果正在进行对象恢复，则标头返回该值 ongoing-request="true"。|string|
|x-cos-server-side-encryption|如果通过 COS 管理的服务端加密来存储对象，响应将包含此头部和所使用的加密算法的值，AES256|string|


### 响应体
该请求响应体为空。

## 实际案例

### 请求

```shell
HEAD /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Thu, 12 Jan 2017 17:26:53 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213210;32557109210&q-key-time=1484213210;32557109210&q-header-list=host&q-url-param-list=&q-signature=ac61b8eb61964e7e6b935e89de163a479a25c210
```

### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 16087
Connection: keep-alive
Date: Thu, 12 Jan 2017 17:26:53 GMT
ETag: \"9a4802d5c99dafe1c04da0a8e7e166bf\"
Last-Modified: Wed, 11 Jan 2017 07:30:07 GMT
Server: tencent-cos
x-cos-object-type: normal
x-cos-request-id: NTg3NzRiZGRfYmRjMzVfM2Y2OF81N2YzNA==
x-cos-storage-class: STANDARD
```
