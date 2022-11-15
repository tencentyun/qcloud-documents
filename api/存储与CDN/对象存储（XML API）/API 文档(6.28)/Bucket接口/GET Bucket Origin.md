## 功能描述

GET Bucket Origin 接口用于查询存储桶的回源配置。

## 请求

#### 请求示例

```plaintext
GET /?origin HTTP 1.1
Host:<BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> - 该请求需结合请求体一起使用。



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

响应体为回源规则，结构如下。

```plaintext
<OriginConfiguration>
  <OriginRule>
    <OriginType>Redirect|Proxy</OriginType>
    <OriginCondition>
    	<HTTPStatusCode>404</HTTPStatusCode>
    	<Prefix></Prefix>
    </OriginCondition>
    
    <OriginParameter>
    	<Protocol>HTTP|HTTPS|FOLLOW</Protocol>
    	<!--查询参数选项只有在回源类型为 Proxy 时可选，否则报参数错误-->
    	<FollowQueryString>true|false</FollowQueryString>
    	<!--请求头部参数只有在回源类型为 Proxy 时可选，否则报参数错误-->
    	<HttpHeader>
    		<!--头部支持传递、不传递两种-->
    		<FollowAllHeaders>true|false</FollowAllHeaders>
    		<!--支持设置头部，最多10个，自定义头部中一对键值算一个-->
            <!--如果有值则新增头部，如果为空则不新增-->
    		<NewHttpHeaders>
                <Header>
                    <Key>x-cos|oss|amz-ContentType|CacheControl|ContentDisposition|ContentEncoding|HttpExpiresDate|UserMetaData</Key>
                    <Value>string</Value>
    			</Header>
    			...
    		</NewHttpHeaders>
			<FollowHttpHeaders>
                <Header>
                    <Key>x-cos|oss|amz-ContentType|CacheControl|ContentDisposition|ContentEncoding|HttpExpiresDate|UserMetaData</Key>
    			</Header>
    			...
    		</FollowHttpHeaders>
    	</HttpHeader>
    	<!--follow3xx参数只有在回源类型为 Proxy 时可选，否则报参数错误-->
    	<FollowRedirection>true|false</FollowRedirection>
    	<!--重定向返回码参数只有在回源类型为 Redirect 时可选，否则报参数错误-->
    	<HttpRedirectCode>301|302|307</HttpRedirectCode> 
    	
    </OriginParameter>
    
    <OriginInfo>
    	<HostInfo>
			<HostName>bucketname-appid.cos.region.myqcloud.com</HostName>
		</HostInfo>
    </OriginInfo>
  </OriginRule>
  ...
</OriginConfiguration>
```

具体的数据内容如下：

| 节点名称（关键字）  | 父节点 | 描述            | 类型      | 是否必选 |
| :------------------ | :----- | :-------------- | :-------- | :--- |
| OriginConfiguration | 无     | Origin 回源配置 | Container | 是   |

Container 节点 OriginConfiguration 的内容：

| 节点名称（关键字） | 父节点              | 描述                        | 类型      | 是否必选 |
| :----------------- | :------------------ | :-------------------------- | :-------- | :--- |
| OriginRule         | OriginConfiguration | 目前只需支持一条 OriginRule | Container | 是   |

Container 节点 OriginRule 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| OriginType         | OriginConfiguration.OriginRule | 回源类型，支持异步回源（Proxy）、同步回源（Mirror）和重定向回源（Redirect）三种模式。 枚举值：`Proxy|Mirror|Redirect`                       | Container |
| OriginCondition             | OriginConfiguration.OriginRule | 回源配置，配置用户使用的 HTTP 传输协议等信息。 | Container    | 是   |
| OriginParameter | OriginConfiguration.OriginRule | 回源地址相关信息                                 | Container | 是   |
| OriginInfo   | OriginConfiguration.OriginRule | 源站信息。例如源站域名或者源站 IP 等信息              | Container    | 是   |

Container 节点 OriginCondition 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| HTTPStatusCode         | OriginConfiguration.OriginRule.OriginCondition | 触发回源的 HTTP 状态码，默认为404。                        | String | 是   |
| Prefix         | OriginConfiguration.OriginRule.OriginCondition | 触发回源的文件前缀，默认为空，任意文件均可触发。                        | String | 否   |

Container 节点 OriginParameter 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| Protocol         | OriginConfiguration.OriginRule.OriginParameter | 回源使用的协议，枚举值为`HTTP`（使用HTTP协议），`HTTPS`（使用HTTPS协议）、`FOLLOW`（跟随用户使用的协议），默认值为`FOLLOW`。                        | String | 是   |
| FollowQueryString         | OriginConfiguration.OriginRule.OriginParameter | `Proxy`模式下是否需要透传HTTP请求串，枚举值：`true|false`，默认为`true`。                      | Boolean | 否   |
| HttpHeader         | OriginConfiguration.OriginRule.OriginParameter | `Proxy`模式下是否需要Http头部传输配置。                    | Container | 否   |
| FollowRedirection         | OriginConfiguration.OriginRule.OriginParameter | `Proxy`模式下源站`3XX`响应策略，枚举值`true|FALSE`，选择true时跟随源站`3xx`重定向请求获取到资源，并将资源保存到COS上;选择`FALSE`时透传`3XX`响应，不获取资源），默认为`true`。                        | Boolean | 否  |
| HttpRedirectCode         | OriginConfiguration.OriginRule.OriginParameter | `Redirect`模式下重定向返回码参数，枚举值`301|302|307`，默认为`302` 。                      | String | 否  |
| CopyOriginData         | OriginConfiguration.OriginRule.OriginParameter | `Redirect`模式下重定向到源站同时是否需要额外复制一份到源站，枚举值`true|FALSE`，默认为`FALSE` 。                      | Boolean | 否  |

Container 节点 HttpHeader 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| FollowAllHeaders         | OriginConfiguration.OriginRule.OriginParameter.HttpHeader | `Proxy`模式下是否传输全部的请求头部，枚举值：`true|FALSE`，默认为`FALSE`。                        | Boolean | 否  |
| NewHttpHeaders         | OriginConfiguration.OriginRule.OriginParameter.HttpHeader | 设置`Proxy`模式设置的指定头部                        | Container | 否  |
| FollowHttpHeaders         | OriginConfiguration.OriginRule.OriginParameter.HttpHeader | 设置`Proxy`模式传输的请求头部。                        | Container | 否  |

Container 节点 NewHttpHeaders、FollowHttpHeaders 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| Header         | OriginConfiguration.OriginRule.OriginParameter.HttpHeader.NewHttpHeader | 回源到源站时添加或者指定传递的自定义头部，默认为空。                        | Container | 否  |


Container 节点 Header 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| Key         | OriginConfiguration.OriginRule.OriginParameter.HttpHeader.NewHttpHeader.UserMetaData | 用户设置的头部名称，默认为空。形式如`x-cos|oss|amz-ContentType|CacheControl|ContentDisposition|ContentEncoding|HttpExpiresDate|UserMetaData`                        | String | 否  |
| Value         | OriginConfiguration.OriginRule.OriginParameter.HttpHeader.NewHttpHeader.UserMetaData | 用户设置的头部值，默认为空。                        | String | 否  |

Container 节点 OriginInfo 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| HostInfo         | OriginConfiguration.OriginRule.OriginInfo | 源站信息。                        | Container | 是   |
| FileInfo         | OriginConfiguration.OriginRule.OriginInfo | 回源文件信息。                        | Container | 是   |

Container 节点 HostInfo 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| HostName         | OriginConfiguration.OriginRule.OriginInfo.HostInfo | 源站域名或者源站 IP。                        | String | 是   |

Container 节点 FileInfo 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| PrefixDirective         | OriginConfiguration.OriginRule.OriginInfo.FileInfo | 是否在回源时将文件重定向为其他前缀的文件，枚举值：`true|FALSE`，默认为`FALSE`。                        |  Boolean | 否  |
| Prefix         | OriginConfiguration.OriginRule.OriginInfo.FileInfo | 回源文件的文件前缀，默认为空。                        |  String | 否  |
| Suffix         | OriginConfiguration.OriginRule.OriginInfo.FileInfo | 回源文件的文件后缀，默认为空。                        |  String | 否  |

## 实际案例

#### 请求

```plaintext
GET /?origin= HTTP/1.1
Host: examplebucket-1250000000.cos.ap-shanghai.myqcloud.com
Authorization: Auth String
Date: Sun, 28 Apr 2019 12:02:24 GMT
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Sun, 28 Apr 2019 12:02:25 GMT
Server: tencent-cos
x-cos-request-id: NWNjNTk2NTFfMmM4OGY3MGFfNTI1****

<?xml version="1.0" encoding="UTF-8"?>
<OriginConfiguration>
  <OriginRule>
    <OriginType>Proxy</OriginType>
    <OriginCondition>
    	<HTTPStatusCode>404</HTTPStatusCode>
    	<Prefix></Prefix>
    </OriginCondition>
    
    <OriginParameter>
    	<Protocol>FOLLOW</Protocol>
    	<FollowQueryString>true</FollowQueryString>
    	<HttpHeader>
    		<FollowAllHeaders>true</FollowAllHeaders>
    		<NewHttpHeaders>
                <Header>
                    <Key>x-cos-ContentType</Key>
                    <Value>csv</Value>
    			</Header>
    		</NewHttpHeader>
    		<FollowHttpHeaders>
                <Header>
                    <Key>Content-Type</Key>
    			</Header>
    		</FollowHttpHeaders>
    	</HttpHeader>
    	<FollowRedirection>true</FollowRedirection>
    </OriginParameter>
    
    <OriginInfo>
    	<HostInfo>
			<HostName>examplebucket-1250000000.cos.ap-shanghai.myqcloud.com</HostName>
		</HostInfo>
    </OriginInfo>
  </OriginRule>
</OriginConfiguration>
```
