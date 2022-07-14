## 功能描述

DELETE Bucket domain 请求用于删除存储桶的自定义域名配置。

> ! 
>
> - 主账号默认拥有删除存储桶域名的权限，子账号删除存储桶自定义域名，需要通过主账号在 [访问管理控制台](https://console.cloud.tencent.com/cam/overview) 授予`DeleteBucketDomain`接口的权限。
> - 该接口将删除指定存储桶下所有绑定的自定义域名，请谨慎操作；如果需要删除部分自定义域名，可以通过`GET Bucket Domain`接口拉取存储桶下绑定的所有自定义域名，然后通过`PUT Bucket Domain`接口将不需要删除的自定义域名重新写入即可。

## 请求

#### 请求示例

```plaintext
DELETE /?domain HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
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

此接口无请求体。

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
DELETE /?domain HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 29 Apr 2020 09:10:59 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1588151459;1588158659&q-key-time=1588151459;1588158659&q-header-list=date;host&q-url-param-list=domain&q-signature=813ddfaa3de3882f4b5ed2e0683e8a5f09e4****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 204 No Content
Connection: close
Date: Wed, 29 Apr 2020 09:11:00 GMT
Server: tencent-cos
x-cos-request-id: NWVhOTQ0YTNfYWZjOTJhMDlfMWNhYTBfOTEw****
x-cos-trace-id: OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODczNTBmNjMwZmQ0MTZkMjg0NjlkNTYyNmY4ZTRkZTk0NzJmZTI0ZmJhYTZmZjYyNmU5ZGNlZDI5YjkyODkwYjNhZjFjMTVmYjUyNmEyY2VjMjAzMGI5NWM5ZmZlOWQyZGY=
Content-Length: 0
```
