## 功能描述
DELETE Bucket policy 请求可以向存储桶删除权限策略。

>!只有存储桶所有者有权限发起该请求。如果权限策略不存在，将返回204 No Content。

## 请求

#### 请求示例

```shell
DELETE /?policy HTTP/1.1
Host:<BucketName-APPID>.cos.<Region>.myqcloud.com
Date: date
Authorization: Auth String
```
>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。


#### 请求体
该请求的请求体为空。

## 响应
#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。


#### 响应体
该响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```shell
DELETE /?policy HTTP/1.1
Host: examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUj****&q-sign-time=1484814613;32557710613&q-key-time=1484814613;32557710613&q-header-list=host&q-url-param-list=policy&q-signature=57c9a3f67b786ddabd2c208641944ec7f9b0****
```

#### 响应

```shell
HTTP/1.1 204 No Content
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu Jan 19 16:30:21 2017
Server: tencent-cos
x-cos-request-id: NTg4MDc5MWRfNDQyMDRlXzNiMDRf****
```
