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
        <RulePriority>Integer</RulePriority>
        <OriginType>Redirect|Proxy|Mirror</OriginType>
        <OriginCondition>
            <!--回源设置的 HTTP 状态码设置根据回源类型决定，如果是 Proxy、Mirror 是404，如果是 Redirect 是4XX 或5XX 的任意状态码-->
            <HTTPStatusCode>404</HTTPStatusCode>
            <Prefix></Prefix>
        </OriginCondition>
        <OriginParameter>
            <Protocol>HTTP|HTTPS|FOLLOW</Protocol>
            <!--回源是否保留源站的错误码-->
            <TransparentErrorCode>true|false</TransparentErrorCode>
            <!--回源是否保留原始查询参数，支持保留、不保留两种-->
            <FollowQueryString>true|false</FollowQueryString>
            <!--回源的请求头部参数-->
            <HttpHeader>
                <!--回源是否传输全部的请求头部，支持传递、不传递两种-->
                <FollowAllHeaders>true|false</FollowAllHeaders>
                <!--回源新增指定头部，最多10个，自定义头部中一对键值算一个-->
                <!--如果有值则新增头部，如果为空则不新增-->
                <NewHttpHeaders>
                    <Header>
                        <Key>x-cos|oss|amz-ContentType|CacheControl|ContentDisposition|ContentEncoding|HttpExpiresDate|UserMetaData</Key>
                        <Value>string</Value>
                    </Header>
                </NewHttpHeaders>
                <!--回源透传原始请求的指定头部-->
                <FollowHttpHeaders>
                    <Header>
                        <Key>x-cos|oss|amz-ContentType|CacheControl|ContentDisposition|ContentEncoding|HttpExpiresDate|UserMetaData</Key>
                    </Header>
                </FollowHttpHeaders>
                <!--回源不透传原始请求的指定头部-->
                <ForbidFollowHeaders>
                    <Header>
                        <Key>String</Key>
                    </Header>
                </ForbidFollowHeaders>
            </HttpHeader>
            <!--follow3xx 参数-->
            <FollowRedirection>true|false</FollowRedirection>
            <!--重定向返回码参数只有在回源类型为 Redirect、Proxy 时可选，否则报参数错误-->
            <HttpRedirectCode>301|302|307</HttpRedirectCode>
        </OriginParameter>
	<!--切备错误码，默认5XX 切换备站，添加此选项后支持4XX 切换备站  -->
        <HTTPStandbyCode>                        
            <StatusCode>404</StatusCode>
            <StatusCode>403</StatusCode>
        </HTTPStandbyCode>
        <OriginInfo>
            <!--Mirror 模式支持设置多个源站，按比例回源，分担单个源站的回源流量，最多支持填入10条回源地址，比例按权重分配；Proxy 和 Redirect 仅支持一个源站-->
            <HostInfo>
                <HostName>bucketname-appid.cos.region.myqcloud.com</HostName>
                <!--源站权重，按比例回源-->
		<Weight>4</Weight> 
                <!--备份回源地址，最多支持填入10条备份回源地址，节点命名依次按照1-10编号-->
                <StandbyHostName_1>bucketname2-appid.cos.region.myqcloud.com</StandbyHostName_1>
                <StandbyHostName_2>bucketname3-appid.cos.region.myqcloud.com</StandbyHostName_2>
            </HostInfo>
            <HostInfo>
                <HostName>bucketname4-appid.cos.region.myqcloud.com</HostName>
                <!--源站权重，按比例回源-->
                <Weight>2</Weight> 
                <!--备份回源地址，最多支持填入10条备份回源地址，节点命名依次按照1-10编号-->
                <StandbyHostName_1>bucketname5-appid.cos.region.myqcloud.com</StandbyHostName_1>
                <StandbyHostName_2>bucketname6-appid.cos.region.myqcloud.com</StandbyHostName_2>
            </HostInfo>
            <FileInfo>
                <!--回源为指定的文件-->
                <FixedFileConfiguration>
                    <FixedFilePath>String</FixedFilePath>
                </FixedFileConfiguration>
                <!--回源文件的新增文件前缀-->
				<PrefixConfiguration>
					<Prefix></Prefix>
				</PrefixConfiguration>
                <!--回源文件的新增文件后缀-->
				<SuffixConfiguration>
					<Suffix></Suffix>
				</SuffixConfiguration>
            </FileInfo>
        </OriginInfo>
    </OriginRule>
</OriginConfiguration>
```

具体的数据内容如下：

| 节点名称（关键字）  | 父节点 | 描述            | 类型      | 
| :------------------ | :----- | :-------------- | :-------- | 
| OriginConfiguration | 无     | Origin 回源配置 | Container |

Container 节点 OriginConfiguration 的内容：

| 节点名称（关键字） | 父节点              | 描述                        | 类型      | 
| :----------------- | :------------------ | :-------------------------- | :-------- | 
| OriginRule         | OriginConfiguration | 支持多条 OriginRule，通过优先级区分规则执行先后| Container |

Container 节点 OriginRule 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- |
|  RulePriority   |  OriginConfiguration.OriginRule   |  通过优先级区分规则执行先后  | Integer   | 
| OriginType         | OriginConfiguration.OriginRule | 回源类型，支持异步回源（Proxy）、同步回源（Mirror）和重定向回源（Redirect）三种模式。 枚举值：`Proxy`、`Mirror`、`Redirect`                       |String |
| OriginCondition             | OriginConfiguration.OriginRule | 回源配置，配置用户使用的 HTTP 传输协议等信息 | Container    |
| OriginParameter | OriginConfiguration.OriginRule | 回源地址相关信息                                 | Container | 
| OriginInfo   | OriginConfiguration.OriginRule | 源站信息。例如源站域名或者源站 IP 等信息              | Container    |

Container 节点 OriginCondition 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- |
| HTTPStatusCode         | OriginConfiguration.OriginRule.<br/>OriginCondition  | 触发回源的 HTTP 状态码，Proxy 和 Mirror 模式支持填写404，Redirect 模式支持填写4XX 和5XX                        | String |
| Prefix         | OriginConfiguration.OriginRule.<br/>OriginCondition | 触发回源的文件前缀，默认为空，任意文件均可触发                        | String |

Container 节点 OriginParameter 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- |
| Protocol         | OriginConfiguration.OriginRule.<br/>OriginParameter | 回源使用的协议，枚举值为 HTTP（使用 HTTP 协议），HTTPS（使用 HTTPS 协议）、FOLLOW（跟随用户使用的协议），默认值为 FOLLOW。                        | String | 
| FollowQueryString         | OriginConfiguration.OriginRule.OriginParameter | 回源是否需要透传 HTTP 请求串，枚举值：`true` 或 `false`，默认为 `true`                      | Boolean |
| HttpHeader         | OriginConfiguration.OriginRule.OriginParameter | 是否需要设置 Http 头部传输配置。                    | Container |
| FollowRedirection         | OriginConfiguration.OriginRule.OriginParameter | 源站 `3XX` 响应策略，枚举值 `true` 或 `false`，选择 true 时跟随源站 `3xx` 重定向请求获取到资源，并将资源保存到 COS 上;选择 `false` 时透传 `3XX` 响应，不获取资源），默认为 `true`。                        | Boolean | 
| HttpRedirectCode         | OriginConfiguration.OriginRule.OriginParameter | 仅支持 `Redirect` 和 `Proxy` 模式，设置重定向返回码参数，枚举值 `301` 或 `302` 或 `307`，默认为 `302` 。                      | String | 

Container 节点 HttpHeader 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- |
| FollowAllHeaders         | OriginConfiguration.OriginRule.OriginParameter.HttpHeader | 是否传输全部的请求头部，枚举值：`true` 或 `false`，默认为 `false`。                        | Boolean |
| NewHttpHeaders         | OriginConfiguration.OriginRule.OriginParameter.HttpHeader | 设置回源新增指定头部，最多10个。                        | Container |
| FollowHttpHeaders         | OriginConfiguration.OriginRule.OriginParameter.HttpHeader | 设置回源透传原始请求的指定头部。                       | Container |
| ForbidFollowHeaders         | OriginConfiguration.OriginRule.OriginParameter.HttpHeader | 设置回源不透传的原始请求的指定头部。                       | Container |

Container 节点 NewHttpHeaders、FollowHttpHeaders、ForbidFollowHeaders 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- |
| Header         | OriginConfiguration.OriginRule.OriginParameter.<br/>HttpHeader.NewHttpHeaders | 回源到源站时添加或者指定传递的自定义头部，默认为空。                        | Container | 

Container 节点 Header 的内容：


| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | 
| Key         | OriginConfiguration.OriginRule.OriginParameter.<br/>HttpHeader.NewHttpHeader.UserMetaData | 用户设置的头部名称，默认为空。形式如 `x-A-B`，A 支持填入 `cos` 或 `oss` 或 `amz`，B 支持填入 `ContentType` 或 `CacheControl` 或 `ContentDisposition` 或 `ContentEncoding` 或 `HttpExpiresDate` 或 `UserMetaData`                        | String | 
| Value         | OriginConfiguration.OriginRule.OriginParameter.<br/>HttpHeader.NewHttpHeader.UserMetaData | 用户设置的头部值，默认为空。                        | String |

Container 节点 OriginInfo 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- |
| HostInfo         | OriginConfiguration.OriginRule.OriginInfo | 源站信息。Mirror 模式支持设置多个源站，按比例回源，分担单个源站的回源流量，最多支持填入10条回源地址，比例按权重分配；Proxy 和 Redirect 模式仅支持一个源站。                        | Container |
| FileInfo         | OriginConfiguration.OriginRule.OriginInfo | 回源文件信息。                        | Container |

Container 节点 HostInfo 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | 
| HostName         | OriginConfiguration.OriginRule.<br/>OriginInfo.HostInfo | 源站域名或者源站 IP。                        | String | 
|Weight         | OriginConfiguration.OriginRule.OriginInfo.HostInfo | 源站权重，Mirror 模式下配置了多个源站时，会根据权重按比例回源。                       |Integer | 
| StandbyHostName_N         | OriginConfiguration.OriginRule.OriginInfo.HostInfo | 备份回源地址，最多支持填入10条备份回源地址，节点命名依次按照1-10编号，例如 `StandbyHostName_1`、`StandbyHostName_2`......`StandbyHostName_10`                        | String |

Container 节点 FileInfo 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | 
| PrefixConfiguration         | OriginConfiguration.OriginRule.OriginInfo.FileInfo | 回源文件的前缀设置。                        | Container |
| SuffixConfiguration         | OriginConfiguration.OriginRule.OriginInfo.FileInfo | 回源文件的后缀设置。                        | Container |
| FixedFileConfiguration         | OriginConfiguration.OriginRule.OriginInfo.FileInfo | 回源到固定的文件。                        | Container | 

Container 节点 FixedFileConfiguration 的内容：


| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | 
| FixedFilePath         | OriginConfiguration.OriginRule.OriginInfo.<br/>FileInfo.FixedFileConfiguration | 回源的固定文件路径。                        |  String | 


Container 节点 PrefixConfiguration 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | 
| Prefix       | OriginConfiguration.OriginRule.OriginInfo.<br/>FileInfo. PrefixConfiguration | 回源文件的新增文件前缀，默认为空。                        |  String |

Container 节点 SuffixConfiguration 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- |
| Suffix         | OriginConfiguration.OriginRule.OriginInfo.<br/>FileInfo. SuffixConfiguration | 回源文件的新增文件后缀，默认为空。                        |  String | 

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
                </NewHttpHeaders>
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

