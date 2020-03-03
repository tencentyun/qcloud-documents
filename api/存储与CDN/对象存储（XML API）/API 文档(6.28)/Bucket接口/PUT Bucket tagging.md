## 功能描述

COS 支持为已存在的 Bucket 设置标签（Tag）。PUT Bucket tagging 接口用于为存储桶设置键值对作为存储桶标签，可以协助您管理已有的存储桶资源，并通过标签进行成本管理。

> !目前存储桶标签功能最多支持一个存储桶下设置50个不同的标签。

## 请求

#### 请求示例

```http
PUT /?tagging HTTP 1.1
Host:<BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
Content-MD5: MD5
Content-Length: Content Length
Content-Type: application/xml

[Request Body]
```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口除使用公共请求头部外，还支持以下请求头部，了解公共请求头部详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

|名称&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	|描述	|类型	|是否必选|
|---|---|---|---|
|Content-MD5	|RFC 1864 中定义的经过 Base64 编码的请求体内容 MD5 哈希值，用于完整性检查，验证请求体在传输过程中是否发生变化	|string	|是|

#### 请求体

该请求需要设置如下标签集合：

```http
<?xml version="1.0" encoding="UTF-8" ?>
<Tagging>
    <TagSet>
        <Tag>
            <Key>age</Key>
            <Value>18</Value>
        </Tag>
        <Tag>
            <Key>name</Key>
            <Value>xiaoming</Value>
        </Tag>
    </TagSet>
</Tagging>
```

具体的数据描述如下：

| 节点名称（关键字） | 父节点             | 描述                                                         | 类型       | 必选 |
| ------------------ | ------------------ | ------------------------------------------------------------ | ---------- | ---- |
| Tagging            | 无                 | 标签集合                                                     | Container  | 是   |
| TagSet             | Tagging            | 标签集合                                                     | Container  | 是   |
| Tag                | Tagging.TagSet     | 标签集合，最多支持10个标签                                 | Containers | 是   |
| Key                | Tagging.TagSet.Tag | 标签的 Key，长度不超过128字节, 支持英文字母、数字、空格、加号、减号、下划线、等号、点号、冒号、斜线 | String     | 是   |
| Value              | Tagging.TagSet.Tag | 标签的 Value，长度不超过256字节, 支持英文字母、数字、空格、加号、减号、下划线、等号、点号、冒号、斜线 | String     | 是   |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

该请求响应体为空。

#### 错误码

以下描述此请求可能会发生的一些特殊的且常见的错误情况：

| 错误码                | 描述                                                         | HTTP 状态码                                                  |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| SignatureDoesNotMatch | 提供的签名不符合规则，返回该错误码                           | 403 [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3) |
| NoSuchBucket          | 如果试图添加的规则所在的 Bucket 不存在，返回该错误码         | 404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4) |
| MalformedXML          | XML 格式不合法，请跟 restful api 文档仔细比对                | 400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1) |
| BadRequest            | 如超过了允许一个 Bucket 最大设置的 Tag 数量，目前最大支持10个 | 400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1) |
| InvalidTag            | Tag 的 key 和 value 中包含了保留字符串 cos: 或者 Project     | 400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1) |

## 实际案例

#### 请求

如下请求向存储桶`examplebucket-1250000000`中写入了{age:18}和{name:xiaoming}两个标签。COS 配置标签成功并返回204成功请求。

```shell
PUT /?tagging HTTP/1.1
User-Agent: curl/7.29.0
Accept: */*
Host: examplebucket-1250000000.cos.ap-chengdu.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDrbAYjEBqqdEconpFi8NPFsOjrnX4LYUE&q-sign-time=1516361923;1517361973&q-key-time=1516361923;1517361973&q-url-param-list=tagging&q-header-list=content-md5;host&q-signature=71251feb4501494edcfbd01747fa873003759404
Content-MD5: LIbd5t5HLPhuNWYkP6qHcQ==
Content-Length: 127
Content-Type: application/xml

<Tagging>
    <TagSet>
        <Tag>
            <Key>age</Key>
            <Value>18</Value>
        </Tag>
        <Tag>
            <Key>name</Key>
            <Value>xiaoming</Value>
        </Tag>
    </TagSet>
</Tagging>
```

#### 响应

```shell
HTTP/1.1 204 No Content
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 19 Jan 2018 11:40:22 GMT
Server: tencent-cos
x-cos-request-id: NWE2MWQ5MjZfMTBhYzM1MGFfMTA5ODVfMTVjNDM=
```
