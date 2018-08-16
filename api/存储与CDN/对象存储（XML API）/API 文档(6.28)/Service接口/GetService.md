## 功能描述
GET Service 接口是用来获取请求者名下的所有存储空间列表（Bucket list）。

## 请求
### 请求示例

```
GET / HTTP/1.1
Host: service.cos.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (详情参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该请求的请求体为空。

## 响应
### 响应头

#### 公共响应头
该响应使用公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729 "公共响应头部") 章节。

#### 特有响应头
该请求操作无特殊的响应头部信息。

### 响应体
查询成功，返回 application/xml 数据，包含 Bucket 中的对象信息。
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<ListAllMyBucketsResult>
  <Owner>
    <ID>string</ID>
    <DisplayName>string</DisplayName>
  </Owner>
  <Buckets>
    <Bucket>
      <Name>string</Name>
      <Location>string</Location>
      <CreateDate>string</CreateDate>
    </Bucket>
    <DisplayName>string</DisplayName>
  </Buckets>
</ListAllMyBucketsResult>
```

具体的数据描述如下：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
ListAllMyBucketsResult|无|说明本次响应的所有信息|Container|是

Container 节点 ListAllMyBucketsResult 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
Owner|ListAllMyBucketsResult|说明 Bucket 持有者的信息|Container|是
Buckets|ListAllMyBucketsResult|说明本次响应的所有 Bucket 列表信息|Container|是
Container 节点 Owner 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
ID|ListAllMyBucketsResult.Owner|Bucket 所有者的 ID|string|是
DisplayName|ListAllMyBucketsResult.Owner|Bucket 所有者的名字信息|string|是
Container 节点 Buckets 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
Bucket|ListAllMyBucketsResult.Buckets|单个 Bucket 的信息|Container|是
DisplayName|ListAllMyBucketsResult.Buckets|Bucket 所有者的名字信息|string|是
Container 节点 Bucket 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
Name|ListAllMyBucketsResult.Buckets.Bucket|Bucket 的名称|string|是
Location|ListAllMyBucketsResult.Buckets.Bucket|Bucket 所在地域。枚举值参见 [可用地域](https://cloud.tencent.com/document/product/436/6224) 文档，如：ap-beijing, ap-hongkong, eu-frankfurt 等|string|是
CreateDate|ListAllMyBucketsResult.Buckets.Bucket|Bucket 创建时间。ISO8601 格式，例如 2016-11-09T08:46:32.000Z|string|是


### 错误码

错误码|描述|HTTP 状态码
---|---|---
InvalidBucketName|Bucket 名称不合法|400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)
SignatureDoesNotMatch|提供的签名不符合规则，返回该错误码|403 [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)
NoSuchBucket|Bucket 不存在，返回该错误码|404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)


## 实际案例

### 请求

```
GET / HTTP/1.1
Host: service.cos.myqcloud.com
Date: Thu, 12 Jan 2016 19:12:22 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1489110340;32468694340&q-key-time=1489110340;32562006340&q-header-list=host&q-url-param-list=&q-signature=cb46d5ce6daed2d3dc0db7130a5719349760562
```

### 响应

```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 19935
Connection: keep-alive
Date: Thu, 12 Jan 2016 19:12:22 GMT
Server: tencent-cos
x-cos-request-id: NThjMjA1NGFfNTViMjM1XzI0NWRfMjA4OGIx

<ListAllMyBucketsResult>
    <Owner>
     <ID>qcs::cam::uin/1147518609:uin/1147518609</ID>
     <DisplayName>1147518609</DisplayName>
    </Owner>
    <Buckets>
        <Bucket>
            <Name>01</Name>
            <Location>ap-beijing</Location>
            <CreateDate>2016-09-13 15:20:15</CreateDate>
        </Bucket>
        <Bucket>
            <Name>0111</Name>
            <Location>ap-hongkong</Location>
            <CreateDate>2017-01-11 17:23:51</CreateDate>
        </Bucket>
        <Bucket>
            <Name>1201new</Name>
            <Location>eu-frankfurt</Location>
            <CreateDate>2016-12-01 09:45:02</CreateDate>
        </Bucket>
    </Buckets>
</ListAllMyBucketsResult
```


