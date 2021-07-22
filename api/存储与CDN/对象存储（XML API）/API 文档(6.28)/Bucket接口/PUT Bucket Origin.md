## 功能描述

PUT Bucket Origin 接口用于设置存储桶的回源。

## 请求

#### 请求示例

```shell
PUT /?origin HTTP 1.1
Host:<BucketName-APPID>.cos.<Region>.myqcloud.com
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

请求的请求体为回源规则。

```shell
<?xml version="1.0" encoding="UTF-8"?>
<OriginConfiguration>
	<OriginRule>
		<RulePriority>Integer</RulePriority>
		<OriginType>Mirror|Proxy</OriginType>
		<OriginCondition>
			<HTTPStatusCode>404</HTTPStatusCode>
			<Prefix>FilePrefix</Prefix>
		</OriginCondition>
		<OriginParameter>
            <Protocol>HTTP|HTTPS|FOLLOW</Protocol>
            <FollowQueryString>true|false</FollowQueryString>
            <HttpHeader>
                <FollowAllHeaders>true|false</FollowAllHeaders>
                <NewHttpHeaders>
                    <Header>
                        <Key>exampleKey</Key>
                        <Value>exampleValue</Value>
                    </Header>
                </NewHttpHeaders>
                <FollowHttpHeaders>
                    <Header>
                        <Key>x-cos|oss|amz-ContentType|CacheControl|ContentDisposition|ContentEncoding|HttpExpiresDate|UserMetaData</Key>
                    </Header>
                </FollowHttpHeaders>
            </HttpHeader>
            <FollowRedirection>true|false</FollowRedirection>
            <HttpRedirectCode>301|302</HttpRedirectCode>
        </OriginParameter>
        <OriginInfo>
            <HostInfo>
                <HostName><BucketName-APPID>.cos.<region>.myqcloud.com</HostName>
            </HostInfo>
            <FileInfo>
                <FixedFileConfiguration>
                    <FixedFilePath>String</FixedFilePath>
                </FixedFileConfiguration>
                <PrefixConfiguration>
                    <Prefix>String</Prefix>
                </PrefixConfiguration>
                <SuffixConfiguration>
                    <Suffix>String</Suffix>
                </SuffixConfiguration>
        	</FileInfo>
        </OriginInfo>
	</OriginRule>
</OriginConfiguration>
```

具体的数据内容如下：

| 节点名称（关键字）  | 父节点 | 描述            | 类型      | 是否必选 |
| :------------------ | :----- | :-------------- | :-------- | :--- |
| OriginConfiguration | 无     | Origin 回源配置 | Container | 是   |

Container 节点 OriginConfiguration 的内容：

| 节点名称（关键字） | 父节点              | 描述                        | 类型      | 是否必选 |
| :----------------- | :------------------ | :-------------------------- | :-------- | :--- |
| OriginRule         | OriginConfiguration | 支持多条 OriginRule，通过优先级区分规则执行先后| Container | 是 |

Container 节点 OriginRule 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
|  RulePriority   |  OriginConfiguration.OriginRule   |  通过优先级区分规则执行先后  | Integer   |   是  |
| OriginType         | OriginConfiguration.OriginRule | 回源类型，支持同步回源（Mirror）和异步回源（Proxy）两种模式。 枚举值：Mirror、Proxy        | Enum |   是   |
| OriginCondition             | OriginConfiguration.OriginRule | 回源配置，配置用户使用的 HTTP 传输协议等信息。 | Container    | 是   |
| OriginParameter | OriginConfiguration.OriginRule | 回源地址相关信息                                 | Container | 是   |
| OriginInfo   | OriginConfiguration.OriginRule | 源站信息。例如源站域名或者源站 IP 等信息。              | Container    | 是   |

Container 节点 OriginCondition 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| HTTPStatusCode         | OriginConfiguration.OriginRule.<br/>OriginCondition | 触发回源的 HTTP 状态码，默认为404。                        | String | 是   |
| Prefix         | OriginConfiguration.OriginRule.<br/>OriginCondition | 触发回源的文件前缀，默认为空，任意文件均可触发。                        | String | 否   |

Container 节点 OriginParameter 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| Protocol         | OriginConfiguration.OriginRule.<br/>OriginParameter | 回源使用的协议，枚举值为 HTTP（使用 HTTP 协议），HTTPS（使用 HTTPS 协议）、FOLLOW（跟随用户使用的协议），默认值为 FOLLOW。                        | String | 是   |
| FollowQueryString         | OriginConfiguration.OriginRule.<br/>OriginParameter | Proxy 模式下是否需要透传 HTTP 请求串，枚举值：true、false，默认为 true。                      | Boolean | 否   |
| HttpHeader         | OriginConfiguration.OriginRule.<br/>OriginParameter |  Proxy 模式下是否需要 Http 头部传输配置。         | Container | 否   |
| FollowRedirection         | OriginConfiguration.OriginRule.<br/>OriginParameter | Proxy 模式下源站 3XX 响应策略，枚举值：true、false，选择 true 时跟随源站 3xx 重定向请求获取到资源，并将资源保存到 COS 上；选择 false 时透传 3XX 响应，不获取资源），默认为 true。                        | Boolean | 否  |
| HttpRedirectCode         | OriginConfiguration.OriginRule.<br/>OriginParameter | Proxy 模式下的返回码参数，枚举值：301、302，默认为 302。                      | String | 否  |

Container 节点 HttpHeader 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| FollowHttpHeader         | OriginConfiguration.OriginRule.<br/>OriginParameter.HttpHeader |  Proxy 模式下是否传输请求头部，枚举值：true、false，默认为 false。                        | Boolean | 否  |
| NewHttpHeader         | OriginConfiguration.OriginRule.<br/>OriginParameter.HttpHeader | 设置 Proxy 模式传输的请求头部。                        | Container | 否  |

Container 节点 NewHttpHeader 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| Header         | OriginConfiguration.OriginRule.<br/>OriginParameter.HttpHeader.NewHttpHeader | 回源到源站时添加新的自定义头部，默认为空。                        | Container | 否  |

Container 节点 Header 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| Key         | OriginConfiguration.OriginRule.<br/>OriginParameter.HttpHeader.NewHttpHeader.Header | 用户设置的头部名称，默认为空。形式如 x-cos、oss、amz-ContentType、CacheControl、ContentDisposition、ContentEncoding、HttpExpiresDate、UserMetaData       | String | 否  |
| Value         | OriginConfiguration.OriginRule.<br/>OriginParameter.HttpHeader.NewHttpHeader.Header | 用户设置的头部值，默认为空。          | String | 否  |

Container 节点 OriginInfo 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| HostInfo         | OriginConfiguration.OriginRule.OriginInfo | 源站信息。                        | Container | 是   |
| FileInfo         | OriginConfiguration.OriginRule.OriginInfo | 回源文件信息。                        | Container | 是   |

Container 节点 HostInfo 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| HostName         | OriginConfiguration.OriginRule.<br/>OriginInfo.HostInfo | 源站域名或者源站 IP。                        | String | 是   |

Container 节点 FileInfo 的内容：

| 节点名称（关键字） | 父节点                         | 描述                                             | 类型      | 是否必选 |
| :----------------- | :----------------------------- | :----------------------------------------------- | :-------- | :--- |
| PrefixConfiguration         | OriginConfiguration.OriginRule.<br/>OriginInfo.FileInfo | 回源文件前缀配置信息。                        |  Container | 否  |
| Prefix         | OriginConfiguration.OriginRule.OriginInfo.<br/>FileInfo.PrefixConfiguration | 回源文件的文件前缀，默认为空。                        |  String | 否  |
| SuffixConfiguration         | OriginConfiguration.OriginRule.<br/>OriginInfo.FileInfo | 回源文件后缀配置信息。                        |  Container | 否  |
| Suffix         | OriginConfiguration.OriginRule.<br/>OriginInfo.FileInfo.SuffixConfiguration | 回源文件的文件后缀，默认为空。                        |  String | 否  |
| FixedFileConfiguration         | OriginConfiguration.OriginRule.<br/>OriginInfo.FileInfo.FixedFileRedirection | 是否在回源时将文件重定向为其他后缀的文件，枚举值：TRUE、FALSE，默认为 FALSE。  |  Boolean | 否  |
| FixedFilePath         | OriginConfiguration.OriginRule.<br/>OriginInfo.FileInfo.FixedFileConfiguration | 回源的固定文件，默认为空。                        |  String | 否  |

## 响应

**响应头**

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

**响应体**

此接口响应体为空。

**错误码**

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。


## 实际案例

**请求（Mirror 模式）**

```shell
PUT /?origin= HTTP/1.1
Host: examplebucket-1250000000.cos.ap-shanghai.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUj****&q-sign-time=1484639384;32557535384&q-key-time=1484639384;32557535384&q-header-list=host&q-url-param-list=&q-signature=5c07b7c67d56497d9aacb1adc19963135b7d****
Content-Length: 347
Date: Sun, 28 Apr 2019 12:02:24 GMT

<?xml version="1.0" encoding="UTF-8"?>
<OriginConfiguration>
  <OriginRule>
    <RulePriority>1</RulePriority>
    <OriginType>Mirror</OriginType>
    <OriginCondition>
      <HTTPStatusCode>404</HTTPStatusCode>
      <Prefix></Prefix>
    </OriginCondition>
    <OriginParameter>
      <Protocol>HTTP</Protocol>
      <FollowQueryString>true</FollowQueryString>
      <HttpHeader>
        <FollowAllHeaders>false</FollowAllHeaders>
        <NewHttpHeaders>
          <Header>
            <Key>x-cos</Key>
            <Value>exampleHeader</Value>
          </Header>
        </NewHttpHeaders>
        <FollowHttpHeaders>
          <Header>
            <Key>exampleHeaderKey</Key>
          </Header>
        </FollowHttpHeaders>
      </HttpHeader>
      <FollowRedirection>true</FollowRedirection>
      <HttpRedirectCode>302</HttpRedirectCode>
    </OriginParameter>
    <OriginInfo>
      <HostInfo>
        <HostName>examplebucket-1250000000.cos.ap-shanghai.myqcloud.com</HostName>
      </HostInfo>
    </OriginInfo>
  </OriginRule>
</OriginConfiguration>
```

**响应**

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Sun, 28 Apr 2019 12:02:45 GMT
Server: tencent-cos
x-cos-request-id: NWNjNTk2NTFfMmM4OGY3MGFfNadfadsfY2****
```
