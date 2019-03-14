## 功能描述
PUT Object 接口请求可以将本地的对象（Object）上传至指定存储桶中。该操作需要请求者对存储桶有写入权限。

### 版本

如果对存储桶启用版本控制，对象存储将自动为要添加的对象生成唯一的版本 ID。对象存储使用 x-cos-version-id 响应头部在响应中返回此标识。
如果需要暂停存储桶的版本控制，则对象存储始终将其 null 用作存储在存储桶中的对象的版本 ID。

### 细节分析
1. 需要有 Bucket 的写权限。
2. 如果请求头的 Content-Length 值小于实际请求体（body）中传输的数据长度，COS 仍将成功创建文件，但 Object 大小只等于 Content-Length 中定义的大小，其他数据将被丢弃。
3. 如果试图添加的 Object 的同名文件已经存在，那么新上传的文件，将覆盖原来的文件，成功时返回200 OK。

## 请求
### 请求示例

```shell
PUT /<ObjectKey> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```
> Authorization: Auth String （详请请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部
该操作的实现还可以使用以下请求头。

名称|描述|类型|必选
---|---|---|---
Content-Disposition|RFC 2616 中定义的文件名称，将作为 Object 元数据保存|string|否
Content-Encoding|RFC 2616 中定义的编码格式，将作为 Object 元数据保存|string|否
Expect|当使用 Expect：100-continue 时，在收到服务端确认后，才会发送请求内容|string|否
Expires|RFC 2616 中定义的缓存策略，将作为 Object 元数据保存|string|否
x-cos-meta-\*|包括用户自定义头部后缀和用户自定义头部信息，将作为 Object 元数据返回，大小限制为2KB<br>**注意**：用户自定义头部信息支持下划线，但用户自定义头部后缀不支持下划线|string|否
x-cos-storage-class|设置 Object 的存储级别，枚举值：STANDARD，STANDARD_IA，ARCHIVE。默认值：STANDARD|string|否
x-cos-acl|定义 Object 的 ACL 属性，有效值：private，public-read，default；默认值：default（继承 Bucket 权限）<br>**注意**：当前访问策略条目限制为1000条，如果您不需要进行 Object ACL 控制，请填 default 或者此项不进行设置，默认继承 Bucket 权限|string|否
x-cos-grant-read |赋予被授权者读的权限，格式：x-cos-grant-read: id="[OwnerUin]" | String |  否 
x-cos-grant-full-control | 赋予被授权者所有的权限，格式：x-cos-grant-full-control: id="[OwnerUin]" | String| 否 

#### 服务端加密相关头部

该请求操作指定腾讯云 COS 在数据存储时，应用数据加密的保护策略。腾讯云 COS 会帮助您在数据写入数据中心时自动加密，并在您取用该数据时自动解密。目前支持使用腾讯云 COS 主密钥对数据进行 AES-256 加密。如果您需要对数据启用服务端加密，则需传入以下头部：

| 名称        | 描述    | 类型     | 必选     |
| --------- | --------- | ------ | ------ |
| x-cos-server-side-encryption | 指定将对象启用服务端加密的方式。<br/>使用 COS 主密钥加密填写：AES256 | String | 如需加密，是 |

### 请求体
该请求的请求体为 Object 文件内容。

## 响应
### 响应头

#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

该请求操作的响应头具体数据为：

|名称|类型|描述|
|---|---|---|
|ETag|string|上传文件内容的 MD5 值|
|x-cos-version-id|string|返回对象的版本|
|x-cos-server-side-encryption|string|如果通过 COS 管理的服务端加密来存储对象，响应将包含此头部和所使用的加密算法的值，AES256|

### 响应体
该请求响应体为空。

### 错误码
该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

### 请求

```shell
PUT /picture.jpg HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 28 Oct 2015 20:32:00 GMT
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484639384;32557535384&q-key-time=1484639384;32557535384&q-header-list=host&q-url-param-list=&q-signature=5c07b7c67d56497d9aacb1adc19963135b7d00dc
Content-Length: 64

[Object]
```

### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Wed,16 Aug 2017 11: 59: 33 GMT
Server: tencent-cos
x-cos-request-id: NTk5NDMzYTRfMjQ4OGY3Xzc3NGRfMWY=
```


