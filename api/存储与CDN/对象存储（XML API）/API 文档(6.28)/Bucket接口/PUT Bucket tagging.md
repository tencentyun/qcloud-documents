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

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。


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

该响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

如下请求向存储桶`examplebucket-1250000000`中写入了{age:18}和{name:xiaoming}两个标签。COS 配置标签成功并返回204成功请求。

```shell
PUT /?tagging HTTP/1.1
User-Agent: curl/7.29.0
Accept: */*
Host: examplebucket-1250000000.cos.ap-chengdu.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDrbAYjEBqqdEconpFi8NPFsOjrnX4****&q-sign-time=1516361923;1517361973&q-key-time=1516361923;1517361973&q-url-param-list=tagging&q-header-list=content-md5;host&q-signature=71251feb4501494edcfbd01747fa87300375****
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
x-cos-request-id: NWE2MWQ5MjZfMTBhYzM1MGFfMTA5ODVfMTVj****
```
