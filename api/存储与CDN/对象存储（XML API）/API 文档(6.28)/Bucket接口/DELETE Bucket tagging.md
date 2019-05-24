## 功能描述

COS 支持为已存在的 Bucket 设置标签（Tag）。DELETE Bucket tagging 接口用于删除指定存储桶下已有的存储桶标签。

> ?如您使用子账号调用此项接口，请确保您已经在主账号处获取了`DELETE Bucket tagging `这个接口的权限。

## 请求

### 请求示例

```http
DELETE /?tagging HTTP 1.1
Host:<BucketName-APPID>.cos.<Region>.myqcloud.com
Date:date
Authorization: Auth String
```

> Authorization: Auth String （详请请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情，请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728 "公共请求头部") 文档。

#### 非公共头部

该请求操作无特殊的请求头部信息。

### 请求体

该请求的请求体为空。

## 响应

### 响应头

#### 公共响应头

该响应使用公共响应头，了解公共响应头详情，请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729 "公共响应头部") 文档。

#### 特有响应头

该请求操作无特殊的响应头部信息。

### 响应体

该请求无特殊响应体信息。

### 错误码

以下描述此请求可能会发生的一些特殊的且常见的错误情况：

| 错误码                | 描述                                                 | HTTP 状态码                                                  |
| --------------------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| SignatureDoesNotMatch | 提供的签名不符合规则，返回该错误码                   | 403 [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3) |
| NoSuchBucket          | 如果试图添加的规则所在的 Bucket 不存在，返回该错误码 | 404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4) |
| NoSuchTagSetError     | 请求的存储桶中未设置存储桶标签                       | 404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4) |

## 实际案例

### 请求

如下请求申请删除存储桶`examplebucket-1250000000`下已有的标签信息。COS 解析该请求后删除该存储桶下所有标签。

```shell
DELETE /?tagging HTTP/1.1
User-Agent: curl/7.29.0
Accept: */*
Host: examplebucket-1250000000.cos.ap-chengdu.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDrbAYjEBqqdEconpFi8NPFsOjrnX4LYUE&q-sign-time=1516361923;1517361973&q-key-time=1516361923;1517361973&q-url-param-list=tagging&q-header-list=content-md5;host&q-signature=71251feb4501494edcfbd01747fa873003759404
Content-Md5: LIbd5t5HLPhuNWYkP6qHcQ==
Content-Length: 127
Content-Type: application/xml
```

### 响应

```shell
HTTP/1.1 204 No Content
Content-Type: application/xml
Connection: close
Date: Fri, 19 Jan 2018 11:40:22 GMT
```
