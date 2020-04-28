## 功能描述

PUT Bucket Domain 请求用于设置存储桶的域名访问。

> !
> - 目前最多支持用户添加20条自定义域名，如需添加更多自定义域名，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们的技术服务团队。
> - 自定义域名支持默认源站、静态网站源站、全球加速源站三种源站类型，如果需要使用静态网站源站，需要 [开启静态网站](https://cloud.tencent.com/document/product/436/14984)；如果需要使用全球加速源站，需要 [开启全球加速](https://cloud.tencent.com/document/product/436/38864)。
> - 主账号默认拥有添加存储桶域名的权限，子账号添加存储桶自定义域名，需要主账号在 [访问管理控制台](https://console.cloud.tencent.com/cam/overview) 授予`PUT Bucket Domain`接口的权限。

## 请求

#### 请求示例

```plaintext
PUT /?domain HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-MD5: MD5
Authorization: Auth String

<Request body>
```

> ?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求参数

此接口无请求参数。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

```XML
<DomainConfiguration>
  <DomainRule>
    <Status>ENABLED</Status>
    <Name>DomainName</Name>
    <Type>REST|WEBSITE|ACCELERATE</Type>
    <ForcedReplacement>CNAME</ForcedReplacement>
  </DomainRule>
  ...
</DomainConfiguration>
```

具体内容描述如下：

| 名称                | 描述                                                         | 类型      | 是否必选 |
| ------------------- | ------------------------------------------------------------ | --------- | -------- |
| DomainConfiguration | 域名管理配置                                                 | Container | 是       |
| CustomDomainRule    | 单条自定义域名配置<Br/>父节点：DomainConfiguration           | Container | 否       |
| Status              | 是否生效，枚举值：`Enabled`，`Disabled`<Br/>父节点：CustomDomainRule | String    | 否       |
| Type                | 源站类型，枚举值：`REST`，`WEBSITE`，`ACCELERATE`<Br/>父节点：CustomDomainRule | String    |          |
| Domain              | 自定义域名<Br/>父节点：CustomDomainRule                      | String    | 否       |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

该请求的响应体返回为空。

#### 错误码

该请求可能会发生的一些常见的特殊错误如下，常见的错误码请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

| 错误码               | 描述                                         | 状态码               |
| :------------------- | :------------------------------------------- | :------------------- |
| InvalidArgument      | 不合法的参数值                               | HTTP 400 Bad Request |
| TooManyCustomDomains | 自定义域名已经达到20条的上限                 | HTTP 400 Bad Request |
| AccessDenied         | 未授权的访问。您可能不具备访问该存储桶的权限 | HTTP 403 Forbidden   |

## 实际案例

#### 请求

该请求表示在南京地域存储桶`examplebucket-1250000000`中添加一个名为`www.tencent.com`的自定义域名，选择的源站类型为默认源站。

```plaintext
PUT /?domain HTTP 1.1
Host: examplebucket-1250000000.cos.ap-nanjing.myqcloud.com
Date: GMT Date
Content-MD5: MD5 String
Authorization: Auth String

<DomainConfiguration>
  <DomainRule>
    <Status>ENABLED</Status>
    <Name>www.tencent.com</Name>
    <Type>REST</Type>
    <ForcedReplacement>CNAME</ForcedReplacement>
  </DomainRule>
</DomainConfiguration>
```

#### 响应

上述请求后，COS 返回如下响应，表明自定义域名已完成设置。

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Fri, 24 Apr 2020 02:53:38 GMT
Server: tencent-cos
x-cos-request-id: NTlhMzg1ZWVfMjQ4OGY3MGFfMWE1NF8****
```
