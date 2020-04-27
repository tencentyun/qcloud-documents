## 功能描述

GET Bucket Domain 请求用于查询存储桶的自定义域名配置。

> !主账号默认拥有查询存储桶自定义域名的权限，子账号查询存储桶自定义域名，需要通过主账号在 [访问管理控制台](https://console.cloud.tencent.com/cam/overview) 授予`GET Bucket Domain`接口的权限。

## 请求

#### 请求示例

```plaintext
GET /?domain HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-MD5: MD5
Authorization: Auth String
```

> ?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

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

```XML
<DomainConfiguration>
  <CustomDomainRule>
    <Status>ENABLED</Status>
    <Name>DomainName</Name>
    <Type>REST|WEBSITE|ACCELERATE</Type>
    <ForcedReplacement>CNAME</ForcedReplacement>
  </CustomDomainRule>
  ...
</DomainConfiguration>
```

| 名称                | 描述                                                         | 类型      |
| ------------------- | ------------------------------------------------------------ | --------- |
| DomainConfiguration | 域名管理配置                                                 | Container |
| CustomDomainRule    | 单条自定义域名配置<Br/>父节点：DomainConfiguration           | Container |
| Status              | 是否生效，枚举值：`Enabled`，`Disabled`<Br/>父节点：CustomDomainRule | String    |
| Type                | 源站类型，枚举值：`REST`，`WEBSITE`，`ACCELERATE`<Br/>父节点：CustomDomainRule | String    |
| Domain              | 自定义域名<Br/>父节点：CustomDomainRule                      | String    |

#### 错误码

该请求无特殊错误码，常见的错误码请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例



#### 请求

该请求表示查询南京地域存储桶`examplebucket-1250000000`中绑定的自定义域名。

```plaintext
GET /?domain HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-MD5: MD5
Authorization: Auth String
```

#### 响应

上述请求后，COS 返回如下响应，表明已查询到自定义域名配置。该存储桶绑定了一个名为`www.examplecustomdomain.com`的自定义域名，选择的源站类型为默认源站。

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Fri, 24 Apr 2020 02:53:38 GMT
Server: tencent-cos
x-cos-request-id: NTlhMzg1ZWVfMjQ4OGY3MGFfMWE1NF8****

<DomainConfiguration>
  <DomainRule>
    <Status>ENABLED</Status>
    <Name>www.examplecustomdomain.com</Name>
    <Type>REST</Type>
    <ForcedReplacement>CNAME</ForcedReplacement>
  </DomainRule>
</DomainConfiguration>
```
