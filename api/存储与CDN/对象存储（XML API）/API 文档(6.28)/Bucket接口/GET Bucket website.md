## 功能描述

GET Bucket website 请求用于查询与存储桶关联的静态网站配置信息。

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=GetBucketWebsite&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>

## 请求

#### 请求示例

```plaintext
GET /?website HTTP/1.1
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

查询成功，返回 **application/xml** 数据，包含完整的存储桶静态网站配置信息。

```xml
<WebsiteConfiguration>
	<IndexDocument>
		<Suffix>string</Suffix>
	</IndexDocument>
	<RedirectAllRequestsTo>
		<Protocol>string</Protocol>
	</RedirectAllRequestsTo>
	<ErrorDocument>
		<Key>string</Key>
	</ErrorDocument>
	<RoutingRules>
		<RoutingRule>
			<Condition>
				<HttpErrorCodeReturnedEquals>integer</HttpErrorCodeReturnedEquals>
			</Condition>
			<Redirect>
				<Protocol>string</Protocol>
				<ReplaceKeyWith>string</ReplaceKeyWith>
			</Redirect>
		</RoutingRule>
		<RoutingRule>
			<Condition>
				<KeyPrefixEquals>string</KeyPrefixEquals>
			</Condition>
			<Redirect>
				<Protocol>string</Protocol>
				<ReplaceKeyPrefixWith>string</ReplaceKeyPrefixWith>
			</Redirect>
		</RoutingRule>
	</RoutingRules>
</WebsiteConfiguration>
```

具体的节点描述如下：

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| WebsiteConfiguration | 无 | 保存 GET Bucket website 结果的所有信息 | Container |

**Container 节点 WebsiteConfiguration 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| IndexDocument | WebsiteConfiguration | 索引文档配置 | Container |
| RedirectAllRequestsTo | WebsiteConfiguration | 重定向所有请求配置 | Container |
| ErrorDocument | WebsiteConfiguration | 错误文档配置 | Container |
| RoutingRules | WebsiteConfiguration | 重定向规则配置 | Container |

**Container 节点 IndexDocument 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Suffix | WebsiteConfiguration.IndexDocument | 指定索引文档的对象键后缀。例如指定为`index.html`，那么当访问到存储桶的根目录时，会自动返回 index.html 的内容，或者当访问到`article/`目录时，会自动返回`article/index.html`的内容 | string |

**Container 节点 RedirectAllRequestsTo 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Protocol | WebsiteConfiguration.RedirectAllRequestsTo | 指定重定向所有请求的目标协议 | string |

**Container 节点 ErrorDocument 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Key | WebsiteConfiguration.ErrorDocument | 指定通用错误文档的对象键 | string |

**Container 节点 RoutingRules 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| RoutingRule | WebsiteConfiguration.RoutingRules | 单条重定向规则配置 | Container |

**Container 节点 RoutingRules.RoutingRule 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Condition | WebsiteConfiguration.RoutingRules.RoutingRule | 重定向规则的条件配置 | Container |
| Redirect | WebsiteConfiguration.RoutingRules.RoutingRule | 重定向规则的具体重定向目标配置 | Container |

**Container 节点 RoutingRules.RoutingRule.Condition 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| HttpErrorCodeReturnedEquals | WebsiteConfiguration.RoutingRules.<br>RoutingRule.Condition | 指定重定向规则的错误码匹配条件 | integer |
| KeyPrefixEquals | WebsiteConfiguration.RoutingRules.<br>RoutingRule.Condition | 指定重定向规则的对象键前缀匹配条件 | string |

**Container 节点 RoutingRules.RoutingRule.Redirect 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 |
| --- | --- | --- | --- |
| Protocol | WebsiteConfiguration.RoutingRules.<br>RoutingRule.Redirect | 指定重定向规则的目标协议 | string |
| ReplaceKeyWith | WebsiteConfiguration.RoutingRules.<br>RoutingRule.Redirect | 指定重定向规则的具体重定向目标的对象键，替换方式为替换整个原始请求的对象键 | string |
| ReplaceKeyPrefixWith | WebsiteConfiguration.RoutingRules.<br>RoutingRule.Redirect | 指定重定向规则的具体重定向目标的对象键，替换方式为替换原始请求中所匹配到的前缀部分 | string |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```plaintext
GET /?website HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 20 May 2020 09:33:49 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1589967229;1589974429&q-key-time=1589967229;1589974429&q-header-list=date;host&q-url-param-list=website&q-signature=50a22a30b02b59e5da4a0820d15a36805ea7****
Connection: close
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 1163
Connection: close
Date: Wed, 20 May 2020 09:33:49 GMT
Server: tencent-cos
x-cos-request-id: NWVjNGY5N2RfYTdjMjJhMDlfNjZkY18yYWUx****

<WebsiteConfiguration>
	<IndexDocument>
		<Suffix>index.html</Suffix>
	</IndexDocument>
	<RedirectAllRequestsTo>
		<Protocol>https</Protocol>
	</RedirectAllRequestsTo>
	<ErrorDocument>
		<Key>pages/error.html</Key>
	</ErrorDocument>
	<RoutingRules>
		<RoutingRule>
			<Condition>
				<HttpErrorCodeReturnedEquals>403</HttpErrorCodeReturnedEquals>
			</Condition>
			<Redirect>
				<Protocol>https</Protocol>
				<ReplaceKeyWith>pages/403.html</ReplaceKeyWith>
			</Redirect>
		</RoutingRule>
		<RoutingRule>
			<Condition>
				<HttpErrorCodeReturnedEquals>404</HttpErrorCodeReturnedEquals>
			</Condition>
			<Redirect>
				<ReplaceKeyWith>pages/404.html</ReplaceKeyWith>
			</Redirect>
		</RoutingRule>
		<RoutingRule>
			<Condition>
				<KeyPrefixEquals>assets/</KeyPrefixEquals>
			</Condition>
			<Redirect>
				<ReplaceKeyWith>index.html</ReplaceKeyWith>
			</Redirect>
		</RoutingRule>
		<RoutingRule>
			<Condition>
				<KeyPrefixEquals>article/</KeyPrefixEquals>
			</Condition>
			<Redirect>
				<Protocol>https</Protocol>
				<ReplaceKeyPrefixWith>archived/</ReplaceKeyPrefixWith>
			</Redirect>
		</RoutingRule>
	</RoutingRules>
</WebsiteConfiguration>
```
