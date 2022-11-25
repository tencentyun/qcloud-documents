
## 功能描述

Get Bucket StrictSignature 接口用于查询存储桶的严格签名模式配置，严格签名模式用于为针对特定的请求规定必须签入的请求头部和请求参数。

> !
>
> - COS 支持在每个存储桶中创建最多10条严格签名模式的规则。
> - 调用该请求时，请确保您有足够的权限对存储桶的严格签名模式进行操作。存储桶所有者默认拥有该权限，若您无该项权限，请先向存储桶所有者申请该项操作的权限。授权流程请参见 [COS 授权及身份认证流程](https://cloud.tencent.com/document/product/436/68279)。


## 请求

#### 请求示例

```shell
GET /?strict-signature HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
Content-MD5: MD5
```

>? 
>
>- Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
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

用户在请求体中使用 XML 语言设置严格模式的具体配置信息，配置信息包括规则名称、适用的操作范围、必须签入的请求头部、必须签入的请求参数。


```shell
<StrictSignatureConfiguration>
    <Rule>
        <ID></ID>
        <actionlist>
            <action></action>
            <action></action>
        </actionlist>
        <headerlist>
            <header></header>
            <header></header>
        </headerlist>
        <paramlist>
            <param></param>
            <param></param>
        </paramlist>
    </Rule>
</StrictSignatureConfiguration>
```

具体的节点描述如下：

| 节点名称（关键字）           | 父节点                                       | 描述                                                         | 类型      | 是否必选 |
| ---------------------------- | -------------------------------------------- | ------------------------------------------------------------ | --------- | -------- |
| StrictSignatureConfiguration | 无                                           | 严格签名模式配置                                             | Container | 是       |
| Rule                         | StrictSignatureConfiguration                 | 规则描述，最多支持10条规则                                   | Container | 是       |
| ID                           | StrictSignatureConfiguration.Rule            | 用于唯一地标识规则，长度不能超过255个字符，合法字符：`a-z，A-Z，0-9，-，_，.` | String    | 是       |
| actionlist                   | StrictSignatureConfiguration.Rule            | action 列表，最多包括200个 action                            | Container | 否       |
| action                       | StrictSignatureConfiguration.Rule.actionlist | 规则指定的 action，命名方式参考接入 CAM 的授权动作；支持通配符，如 `Put*` | String    | 否       |
| headerlist                   | StrictSignatureConfiguration.Rule            | 规则规定必须签入的 header 列表，列表内 header 的数量不得超过20个 | Container | 否       |
| headerlist                   | StrictSignatureConfiguration.Rule.headerlist | 必须签入的请求头部，支持填入的具体请求头部可参考 [支持的请求头部](跳转到开发者指南>严格签名模式概述文档中的“支持的请求头部”一节) | String    | 否       |
| paramlist                    | StrictSignatureConfiguration.Rule            | 规则规定必须签入的请求参数列表，列表内 param 的数量不得超过20个 | Container | 否       |
| param                        | StrictSignatureConfiguration.Rule.paramlist  | 必须签入的请求参数，支持填入的具体请求参数可参考 [支持的请求参数](跳转到开发者指南>严格签名模式概述文档中的“请求参数"一节) | String    | 否       |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```shell
PUT /?strict-signature HTTP/1.1
Date: Date
Authorization: Auth String
Content-MD5: Content-MD5
Host: examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
Content-Length: 1024
```


#### 响应

上述请求后，COS 返回以下响应，表明该存储桶配置了两条严格签名模式规则。

- 名称为 limit_acl 的规则针对 `PutObjectACL` 和 `PutBucketACL` 请求生效，规定签名中必须签入请求头部 `Host` 和请求参数 `acl`
- 名称为 test 的规则针对所有 Put 请求（即 `Put*`）生效，规定签名中必须签入请求头部 `Host` 和所有请求参数（即 `all`）。

```shell
<StrictSignatureConfiguration>
    <Rule>
        <ID>limit_acl</ID>
        <actionlist>
            <action>PutObjectACL</action>
            <action>PutBucketACL</action>
        </actionlist>
        <headerlist>
            <header>Host</header>
        </headerlist>
        <paramlist>
            <param>acl</param>
        </paramlist>
    </Rule>
    <Rule>
        <ID>test</ID>
        <actionlist>
            <action>Put*</action>
        </actionlist>
        <headerlist>
            <header>Host</header>
        </headerlist>
        <paramlist>
            <param>all</param>
        </paramlist>
    </Rule>
</StrictSignatureConfiguration>
```



