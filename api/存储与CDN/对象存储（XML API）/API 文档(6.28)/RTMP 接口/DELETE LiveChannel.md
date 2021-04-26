## 功能描述

 DELETE LiveChannel 接口用于删除指定通道（Live Channel）。

>!
> - 只有桶的拥有者才能进行该请求操作
> - 当有客户端正在向 LiveChannel 推流时，删除请求会失败。
> - 本接口只会删除 LiveChannel 本身，不会删除推流生成的文件。
> - 如果桶内还有通道存在，是不能删除桶的。

## 请求

#### 请求示例

```plaintext
DELETE /<ChannelName>?live HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT date
Content-Length: Content Size
Content-Md5: Content MD5
Authorization: Auth String

```



> ? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数
此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

此接口响应体为空。
#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```plaintext
DELETE /test-channel?live HTTP 1.1
Host: examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
Date: GMT date
Content-Length:Content Size
Content-Md5:Content MD5
Authorization: Auth String
```

#### 响应

```plaintext
HTTP/1.1 204 No Content
Content-Length: 0
Connection: close
Date: Wed, 14 Aug 2019 11:59:40 GMT
Server: tencent-cos
x-cos-request-id: NWQ1M2Y3YWNfMzdiMDJhMDlfODA1Yl8xZThj****
```
