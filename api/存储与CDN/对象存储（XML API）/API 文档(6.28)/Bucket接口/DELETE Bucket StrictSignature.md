## 功能描述

DELETE Bucket StrictSignature 接口用于删除存储桶的严格签名模式配置，严格签名模式用于对特定请求限定必须签入的请求头部和请求参数。

> !
>
> - 调用该请求时，请确保您有足够的权限对存储桶的严格签名模式进行操作。存储桶所有者默认拥有该权限，若您无该项权限，请先向存储桶所有者申请该项操作的权限。授权流程请参见 [COS 授权及身份认证流程](https://cloud.tencent.com/document/product/436/68279)。


## 请求

#### 请求示例

```shell
DELETE /?strict-signature HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
Content-MD5: MD5
```

>? 
>
>- Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参见 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参见 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
>- Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

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

该响应体返回为空。
      

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

下述请求示例展示了删除存储桶 examplebucket-1250000000 的严格签名模式配置。


```shell
DELETE /?strict-signature HTTP/1.1
Date: Date
Authorization: Auth String
Content-MD5: Content-MD5
Host: examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
Content-Length: 1024
```

#### 响应

上述请求后，COS 返回 204 No Content 的响应表明已成功删除了该存储桶的严格签名模式配置。

```shell
HTTP/1.1 204 No Content 
Server: tencent-cos
Date: Date
x-cos-id-2:0dfafa/DAPDIFdafdsfDdfSFFfdfKKJdafasiuKJK2
x-cos-request-id: NTlhM2I3M2JfMjQ4OGY3MGFfMWE1NF84****
```
