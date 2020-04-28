## 功能描述

DELETE Bucket Domain 请求用于删除存储桶的自定义域名配置。

> ! 
> - 主账号默认拥有删除存储桶域名的权限，子账号删除存储桶自定义域名，需要通过主账号在 [访问管理控制台](https://console.cloud.tencent.com/cam/overview) 授予`DELETE Bucket Domain`接口的权限。
> - 该接口将删除指定存储桶下所有绑定的自定义域名，请谨慎操作；如果需要删除部分自定义域名，可以通过`GET Bucket Domain`接口拉取存储桶下绑定的所有自定义域名，然后通过`PUT Bucket Domain`接口将不需要删除的自定义域名重新写入即可。

## 请求

#### 请求示例

```plaintext
DELETE /?domain HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-MD5: MD5
Authorization: Auth String
```

> ?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

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

此接口无响应体。

#### 错误码

该请求无特殊错误码，常见的错误码请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例



#### 请求

该请求表示删除南京地域存储桶`examplebucket-1250000000`中所有存储桶的自定义域名。

```plaintext
DELETE /?domain HTTP 1.1
Host: examplebucket-1250000000.cos.ap-nanjing.myqcloud.com
Date: GMT Date
Content-MD5: MD5 String
Authorization: Auth String
```

#### 响应

上述请求后，COS 返回如下响应，表明自定义域名已完成删除。

```plaintext
HTTP/1.1 204 No Content 
Content-Type: application/xml
Content-Length: 0
Date: Fri, 24 Apr 2020 02:53:48 GMT
Server: tencent-cos
x-cos-request-id: NTlhMzg1ZWVfMjQ4OGY3MGFfMWE1NF8****
```
