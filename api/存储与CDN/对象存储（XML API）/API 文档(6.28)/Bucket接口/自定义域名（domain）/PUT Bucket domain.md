## 功能描述

PUT Bucket domain 请求用于设置存储桶的自定义域名。

> !
> - 目前最多支持用户添加20条自定义域名，如需添加更多自定义域名，请联系 [在线客服](https://cloud.tencent.com/act/event/Online_service)。
> - 自定义域名支持默认源站、静态网站源站、全球加速源站三种源站类型，如果需要使用静态网站源站，需要 [开启静态网站](https://cloud.tencent.com/document/product/436/14984)；如果需要使用全球加速源站，需要 [开启全球加速](https://cloud.tencent.com/document/product/436/38864)。
> - 主账号默认拥有添加存储桶域名的权限，子账号如需添加存储桶自定义域名，需要主账号在 [访问管理控制台](https://console.cloud.tencent.com/cam/overview) 授予`PutBucketDomain`接口的权限。

## 请求

#### 请求示例

```plaintext
PUT /?domain HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Type: application/xml
Content-Length: Content Length
Content-MD5: MD5
Authorization: Auth String

[Request Body]
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

提交 **application/xml** 请求数据，包含完整的存储桶自定义域名信息。

```xml
<DomainConfiguration>
	<DomainRule>
		<Status>Enum</Status>
		<Name>string</Name>
		<Type>Enum</Type>
	</DomainRule>
	<DomainRule>
		<Status>Enum</Status>
		<Name>string</Name>
		<Type>Enum</Type>
	</DomainRule>
</DomainConfiguration>
```

具体的节点描述如下：

| 节点名称（关键字）  | 父节点 | 描述                                      | 类型      | 是否必选 |
| ------------------- | ------ | ----------------------------------------- | --------- | -------- |
| DomainConfiguration | 无     | 包含 PUT Bucket domain 操作的所有请求信息 | Container | 否       |

**Container 节点 DomainConfiguration 的内容：**

| 节点名称（关键字） | 父节点              | 描述     | 类型      | 是否必选 |
| ------------------ | ------------------- | -------- | --------- | -------- |
| DomainRule         | DomainConfiguration | 域名条目 | Container | 是       |

**Container 节点 DomainRule 的内容：**

| 节点名称（关键字） | 父节点                         | 描述                                                         | 类型   | 是否必选 |
| ------------------ | ------------------------------ | ------------------------------------------------------------ | ------ | -------- |
| Status             | DomainConfiguration.DomainRule | 是否启用。枚举值：<br><li>ENABLED：启用<li>DISABLED：禁用    | Enum   | 是       |
| Name               | DomainConfiguration.DomainRule | 完整域名                                                     | string | 是       |
| Type               | DomainConfiguration.DomainRule | 源站类型。枚举值：<br><li>REST：默认源站<li>WEBSITE：静态源站源站<li>ACCELERATE：全球加速源站 | Enum   | 是       |
| ForcedReplacement  | DomainConfiguration.DomainRule | 如果指定域名已经作为其他存储桶的自定义域名，那么可以指定该元素强制将该域名作为当前存储桶的自定义域名。当前只支持 CNAME，代表您需要先将该域名的 CNAME 指向当前存储桶的源站域名（根据 Type 元素的不同对应为默认源站、静态网站源站或全球加速源站）后才能通过该接口设置自定义域名。 | Enum   | 否       |

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
PUT /?domain HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 29 Apr 2020 09:16:14 GMT
Content-Type: application/xml
Content-Length: 288
Content-MD5: WHjVNjOz7lW82VThLKf4Lg==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1588151774;1588158974&q-key-time=1588151774;1588158974&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=domain&q-signature=5cd58e4c68125ee6c78d626089d12c41376a****
Connection: close

<DomainConfiguration>
	<DomainRule>
		<Status>ENABLED</Status>
		<Name>cos.cloud.tencent.com</Name>
		<Type>REST</Type>
	</DomainRule>
	<DomainRule>
		<Status>ENABLED</Status>
		<Name>www.cos.cloud.tencent.com</Name>
		<Type>WEBSITE</Type>
	</DomainRule>
</DomainConfiguration>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Length: 0
Connection: close
Date: Wed, 29 Apr 2020 09:16:15 GMT
Server: tencent-cos
x-cos-request-id: NWVhOTQ1ZGVfZTViOTJhMDlfMzA0MjJfMTEwMmJi****
```
