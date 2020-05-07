## 功能描述

DELETE Bucket website 请求用于删除存储桶中的静态网站配置。

## 请求

#### 请求示例

```HTTP
DELETE /?website HTTP/1.1
Host:<BucketName-APPID>.<Region>.myqcloud.com
Date:date
Authorization: Auth String
```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部

该请求操作无特殊的请求头部信息。

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

#### 公共响应头

该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

该响应无特殊的响应头。

#### 响应体

该响应体为空。

#### 错误码

该请求操作无特殊错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```sh
DELETE /?website HTTP/1.1
Host: examplebucket-1250000000.cos.ap-shanghai.myqcloud.com
Date:Thu, 21 Sep 2017 13:21:09 +0000
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484816036;32557712036&q-key-time=1484816036;32557712036&q-header-list=host&q-url-param-list=website&q-signature=e92eecbf0022fe7e5fd39b2c500b22da062be50a
```

#### 响应

```sh
HTTP/1.1 204 No Content
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu, 21 Sep 2017 13:21:18 GMT
Server: tencent-cos
x-cos-request-id: NTljM2JjY2RfMjQ4OGY3MGFfNzk4OV84Mw==
```
