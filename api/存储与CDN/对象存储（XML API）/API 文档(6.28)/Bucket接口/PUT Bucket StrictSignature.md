## 功能描述

PUT Bucket StrictSignature 用于为存储桶设置严格签名模式，严格签名模式用于对特定请求限定必须签入的请求头部和请求参数。

> !
>
> - COS 支持在每个存储桶中创建最多10条严格签名模式的规则。
> - 严格签名模式仅对签名请求生效，不适用于匿名请求。
> - 调用该请求时，请确保您有足够的权限对存储桶的严格签名模式进行操作。存储桶所有者默认拥有该权限，若您无该项权限，请先向存储桶所有者申请该项操作的权限。授权流程请参见 [COS 授权及身份认证流程](https://cloud.tencent.com/document/product/436/68279)。


## 请求

#### 请求示例

```shell
PUT /?strict-signature HTTP/1.1
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

用户在请求体中使用 XML 语言设置严格签名模式的具体配置信息，配置信息包括规则名称、适用的操作范围、必须签入的请求头部和请求参数。


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
| action                       | StrictSignatureConfiguration.Rule.actionlist | 规则指定的 action，命名方式参考接入 CAM 的授权动作；支持通配符，例如 `Put*` | String    | 否       |
| headerlist                   | StrictSignatureConfiguration.Rule            | 规则限定必须签入的 header 列表，列表内 header 的数量不得超过20个 | Container | 否       |
| headerlist                   | StrictSignatureConfiguration.Rule.headerlist | 必须签入的请求头部，支持填入的具体请求头部可参见 [支持的请求头部](https://cloud.tencent.com/document/product/436/83234#:~:text=%E4%BC%9A%E6%8A%A5%E9%94%99%E3%80%82-,%E6%94%AF%E6%8C%81%E7%9A%84%E8%AF%B7%E6%B1%82%E5%A4%B4%E9%83%A8,-%E4%B8%A5%E6%A0%BC%E7%AD%BE%E5%90%8D%E6%A8%A1%E5%BC%8F) | String    | 否       |
| paramlist                    | StrictSignatureConfiguration.Rule            | 规则限定必须签入的请求参数列表，列表内 param 的数量不得超过20个 | Container | 否       |
| param                        | StrictSignatureConfiguration.Rule.paramlist  | 必须签入的请求参数，支持填入的具体请求参数可参见 [支持的请求参数](https://cloud.tencent.com/document/product/436/83234#:~:text=20%E4%B8%AA%20Header%E3%80%82-,%E6%94%AF%E6%8C%81%E7%9A%84%E8%AF%B7%E6%B1%82%E5%8F%82%E6%95%B0,-%E4%B8%A5%E6%A0%BC%E7%AD%BE%E5%90%8D%E6%A8%A1%E5%BC%8F) | String    | 否       |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

该请求的响应体返回为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：为修改 ACL 相关的请求设置严格签名模式

#### 请求

该示例向存储桶 `examplebucket-1250000000` 中添加一条名为 limit_acl 的严格签名模式规则。

- 该规则针对 `PutObjectACL` 和 `PutBucketACL` 请求生效。
- 规定签名中必须签入请求头部 `Host` 和请求参数 `acl`，从而避免恶意用户盗用其他存储桶或请求的签名用于修改存储桶和对象 ACL。

```shell
PUT /?strict-signature HTTP/1.1
Date: Date
Authorization: Auth String
Content-MD5: Content-MD5
Host: examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
Content-Length: 1024

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
</StrictSignatureConfiguration>
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Date
Server: tencent-cos
x-cos-request-id: NTlhMzg1ZWVfMjQ4OGY3MGFfMWE1NF8****
```

#### 案例二：限制 Put 请求必须签入 Host 和请求参数

#### 请求

该示例向存储桶 `examplebucket-1250000000` 中添加一条名为 test 的严格签名模式规则。

- 该规则针对所有 Put 请求生效，即 `Put*`。
- 规定签名中必须签入请求头部 `Host` 和所有请求参数，从而避免恶意用户盗用其他存储桶或其他请求的签名。

```shell
PUT /?strict-signature HTTP/1.1
Date: Date
Authorization: Auth String
Content-MD5: Content-MD5
Host: examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
Content-Length: 1024

<StrictSignatureConfiguration>
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

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Date
Server: tencent-cos
x-cos-request-id: NTlhMzg1ZWVfMjQ4OGY3MGFfMWE1NF8****
```
