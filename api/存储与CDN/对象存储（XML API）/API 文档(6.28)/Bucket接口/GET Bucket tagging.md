## 功能描述

COS 支持为已存在的存储桶查询标签（Tag）。GET Bucket tagging 接口用于查询指定存储桶下已有的存储桶标签。

> ?若您使用子账号调用此项接口，请确保您已经在主账号处获取了 GET Bucket tagging 这个接口的权限。

## 请求

#### 请求示例

```http
GET /?tagging HTTP 1.1
Host:<BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。


#### 响应体
查询成功，返回 application/xml 数据，包含存储桶下已有的标签信息。
```shell
<Tagging>
    <TagSet>
        <Tag>
            <Key>string</Key>
            <Value>string</Value>
        </Tag>
        <Tag>
            <Key>string</Key>
            <Value>string</Value>
        </Tag>
    </TagSet>
</Tagging>
```

具体的节点描述如下：

| 节点名称（关键字） | 父节点             | 描述                                                         | 类型       |
| ------------------ | ------------------ | ------------------------------------------------------------ | ---------- |
| Tagging            | 无                 | 标签集合                                                     | Container  |
| TagSet             | Tagging            | 标签集合                                                     | Container  |
| Tag                | Tagging.TagSet     | 标签集合, 最多支持50个标签                                 | Containers |
| Key                | Tagging.TagSet.Tag | 标签键, 长度不超过128字节，支持英文字母、数字、空格、加号、减号、下划线、等号、点号、冒号、斜线 | String     |
| Value              | Tagging.TagSet.Tag | 标签值, 长度不超过256字节，支持英文字母、数字、空格、加号、减号、下划线、等号、点号、冒号、斜线 | String     |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

如下请求申请查询存储桶`examplebucket-1250000000`下的标签信息，COS 解析该请求后，并返回了该存储桶下已有的 {age:18} 和 {name:xiaoming} 两个标签。

```shell
GET /?tagging HTTP/1.1
User-Agent: curl/7.29.0
Accept: */*
Host: examplebucket-1250000000.cos.ap-chengdu.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDrbAYjEBqqdEconpFi8NPFsOjrnX4****&q-sign-time=1516361923;1517361973&q-key-time=1516361923;1517361973&q-url-param-list=tagging&q-header-list=content-md5;host&q-signature=71251feb4501494edcfbd01747fa87300375****
Content-Length: 127
Content-Type: application/xml
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Connection: close
Date: Fri, 19 Jan 2018 11:40:22 GMT
Server: tencent-cos
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
