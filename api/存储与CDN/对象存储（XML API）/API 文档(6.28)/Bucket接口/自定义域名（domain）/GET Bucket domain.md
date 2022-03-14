## 功能描述

GET Bucket domain 请求用于查询存储桶的自定义域名配置。

> !主账号默认拥有查询存储桶自定义域名的权限，子账号如需查询存储桶自定义域名，需要通过主账号在 [访问管理控制台](https://console.cloud.tencent.com/cam/overview) 授予`GetBucketDomain`接口的权限。

## 请求

#### 请求示例

```plaintext
GET /?domain HTTP/1.1
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

查询成功，返回 **application/xml** 数据，包含完整的存储桶自定义域名信息。

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

| 节点名称（关键字）  | 父节点 | 描述                                  | 类型      |
| ------------------- | ------ | ------------------------------------- | --------- |
| DomainConfiguration | 无     | 保存 GET Bucket domain 结果的所有信息 | Container |

**Container 节点 DomainConfiguration 的内容：**

| 节点名称（关键字） | 父节点              | 描述     | 类型      |
| ------------------ | ------------------- | -------- | --------- |
| DomainRule         | DomainConfiguration | 域名条目 | Container |

**Container 节点 DomainRule 的内容：**

| 节点名称（关键字） | 父节点                         | 描述                                                         | 类型   |
| ------------------ | ------------------------------ | ------------------------------------------------------------ | ------ |
| Status             | DomainConfiguration.DomainRule | 是否启用。枚举值：<br><li>ENABLED：启用<li>DISABLED：禁用    | Enum   |
| Name               | DomainConfiguration.DomainRule | 完整域名                                                     | string |
| Type               | DomainConfiguration.DomainRule | 源站类型。枚举值：<br><li>REST：默认源站<li>WEBSITE：静态源站源站<li>ACCELERATE：全球加速源站 | Enum   |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```plaintext
GET /?domain HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 29 Apr 2020 09:16:26 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1588151786;1588158986&q-key-time=1588151786;1588158986&q-header-list=date;host&q-url-param-list=domain&q-signature=b5f4a4b7bd7bca2ade21503b8f64d512ef69****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 277
Connection: close
Date: Wed, 29 Apr 2020 09:16:26 GMT
Server: tencent-cos
x-cos-domain-txt-verification: tencent-cloud-cos-verification=673029e5ff8e4d2b5723d58f73aab232
x-cos-request-id: NWVhOTQ1ZWFfN2ViMTJhMDlfMjU5Zl8xMzQ1****

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
