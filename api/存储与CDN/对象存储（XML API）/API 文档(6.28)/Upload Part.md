## 功能描述
Upload Part 接口请求实现在初始化以后的分块上传，支持的块的数量为1到10000，块的大小为1 MB 到5 GB。
使用 Initiate Multipart Upload 接口初始化分片上传时会得到一个 uploadId，该 ID 不但唯一标识这一分块数据，也标识了这分块数据在整个文件内的相对位置。在每次请求 Upload Part 时候，需要携带 partNumber 和 uploadId，partNumber为块的编号，支持乱序上传。
当传入 uploadId 和 partNumber 都相同的时候，后传入的块将覆盖之前传入的块。当 uploadId 不存在时会返回 404 错误，NoSuchUpload.

## 请求

语法示例：
```
PUT /ObjectName?partNumber=PartNumber&uploadId=UploadId HTTP/1.1
Host: <BucketName>-<APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Length: Size
Authorization: Auth String
```

> Authorization: Auth String (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
```
PUT /ObjectName?partNumber=PartNumber&uploadId=UploadId HTTP/1.1
```
该 API 接口接受 PUT 请求。

#### 请求参数
包含所有请求参数的请求行示例：<style  rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>
```
PUT /ObjectName?partNumber=PartNumber&uploadId=UploadId HTTP/1.1
```
具体内容如下：

|参数名称|描述|类型|必选|
|:---|:---|:---|:---|
| partNumber | 标识本次分块上传的编号 | String | 是 |
| uploadId | 标识本次分块上传的 ID；<br>使用 Initiate Multipart Upload 接口初始化分片上传时会得到一个 uploadId，该 ID 不但唯一标识这一分块数据，也标识了这分块数据在整个文件内的相对位置| String | 是 |

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。

#### 非公共头部
**必选头部**
该请求操作需要请求头使用必选头部，具体内容如下：

|名称|描述|类型|必选|
|:---|:---|:---|:---|
| Content-Length | RFC 2616 中定义的 HTTP 请求内容长度（字节）| String | 是 |

**推荐头部**
该请求操作推荐请求头使用推荐头部，具体内容如下：

|名称|描述|类型|必选|
|:---|:---|:---|:---|
| Expect | RFC 2616 中定义的 HTTP 请求内容长度（字节）| String | 否 |
| Content-MD5 | RFC 1864 中定义的经过Base64编码的128-bit 内容 MD5 校验值。此头部用来校验文件内容是否发生变化| String | 否 |

### 请求体
该请求的操作请求体为空。

## 响应

### 响应头
#### 公共响应头 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
该响应的响应体为空。

## 实际案例

### 请求
```
PUT /ObjectName?partNumber=1&uploadId=1484727270323ddb949d528c629235314a9ead80f0ba5d993a3d76b460e6a9cceb9633b08e HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed，18 Jan 2017 16:17:03 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484727403;32557623403&q-key-time=1484727403;32557623403&q-header-list=host&q-url-param-list=partNumber;uploadId&q-signature=bfc54518ca8fc31b3ea287f1ed2a0dd8c8e88a1d
Content-Length: 10485760

[Object]
```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed，18 Jan 2017 16:17:03 GMT
Etag: "e1e5b4965bc7d30880ed6d226f78a5390f1c09fc"
Server: tencent-cos
x-cos-request-id: NTg3ZjI0NzlfOWIxZjRlXzZmNGJfMWYy

```
