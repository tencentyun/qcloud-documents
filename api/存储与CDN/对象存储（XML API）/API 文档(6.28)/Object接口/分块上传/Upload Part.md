## 功能描述
Upload Part 接口请求实现将对象按照分块的方式上传到 COS。最多支持10000分块，每个分块大小为1MB - 5GB，最后一个分块可以小于1MB。


#### 细节分析
1. 分块上传首先需要进行初始化，使用 Initiate Multipart Upload 接口实现，初始化后会得到一个 uploadId ，唯一标识本次上传。
2. 在每次请求 Upload Part 时，需要携带 partNumber 和 uploadId，partNumber 为块的编号，支持乱序上传。
3. 当传入 uploadId 和 partNumber 都相同的时候，后传入的块将覆盖之前传入的块。当 uploadId 不存在时会返回404错误，NoSuchUpload。

## 请求

#### 请求示例

```shell
PUT /<ObjectKey>?partNumber=PartNumber&uploadId=UploadId HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Length: Size
Authorization: Auth String

[Object]
```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


#### 请求头

#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详请请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部
**必选头部**
该请求操作需要请求头使用必选头部，具体内容如下：

| 名称             | 描述                            | 类型     | 是否必选   |
| :------------- | :---------------------------- | :----- | :--- |
| Content-Length | RFC 2616 中定义的 HTTP 请求内容长度（字节） | String | 是    |

**推荐头部**
该请求操作推荐请求头使用推荐头部，具体内容如下：

| 名称          | 描述                                       | 类型     | 是否必选   |
| :---------- | :--------------------------------------- | :----- | :--- |
| Expect      | RFC 2616 中定义的 HTTP 请求内容长度（字节）            | String | 否    |
| Content-MD5 | RFC 1864 中定义的经过 Base64 编码的请求体内容 MD5 哈希值，用于完整性检查，验证请求体在传输过程中是否发生变化 | String | 否    |

#### 请求参数
具体内容如下：

| 参数名称       | 描述                                       | 类型     | 是否必选   |
| :--------- | :--------------------------------------- | :----- | :--- |
| partNumber | 标识本次分块上传的编号，partNumber 需要大于等于1                              | String | 是    |
| uploadId   | 标识本次分块上传的 ID，使用 Initiate Multipart Upload 接口初始化分片上传时会得到一个 uploadId，该 ID 不但唯一标识这一分块数据，也标识了这分块数据在整个文件内的相对位置 | String | 是    |


#### 请求体
该请求的请求体为该分块的数据内容。

## 响应


#### 响应头
#### 公共响应头 
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。
#### 特有响应头
该响应将可能返回如下响应头部信息：

| 名称                           | 描述                                       | 类型     |
| ---------------------------- | ---------------------------------------- | ------ |
| x-cos-server-side-encryption | 如果在上传时指定使用了服务端加密，响应头部将会返回该响应头，枚举值： AES256 | String |
|x-cos-storage-class|返回对象的存储类型信息，COS 为除了 Standard 存储类型之外的所有对象返回此响应头部，枚举值：STANDARD_IA 和 ARCHIVE| String |


#### 响应体
该请求的响应体为空。


#### 错误码
该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求
```shell
PUT /exampleobject?partNumber=1&uploadId=1484727270323ddb949d528c629235314a9ead80f0ba5d993a3d76b460e6a9cceb9633b08e HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed，18 Jan 2017 16:17:03 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUj****&q-sign-time=1484727403;32557623403&q-key-time=1484727403;32557623403&q-header-list=host&q-url-param-list=partNumber;uploadId&q-signature=bfc54518ca8fc31b3ea287f1ed2a0dd8c8e8****
Content-Length: 10485760

[Object]
```

#### 响应
```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed，18 Jan 2017 16:17:03 GMT
Etag: "e1e5b4965bc7d30880ed6d226f78a5390f1c09fc"
Server: tencent-cos
x-cos-request-id: NTg3ZjI0NzlfOWIxZjRlXzZmNGJfMWYy
```
