## 功能描述
为 Object 设置标签(Tag)。

## 请求
#### 请求语法示例

**shell:** 

```shell
# You can also use curl
curl -X PUT http://{bucket}.cos.{region}.myqcloud.com/{ObjectName}?tagging \
  -H 'Content-MD5: string' \
  -H 'Content-Type: application/xml' \
  -H 'Accept: application/xml'

```

**http:** 

```http
PUT http://{bucket}.cos.{region}.myqcloud.com/{ObjectName}?tagging HTTP/1.1
Host: 
Content-Type: application/xml
Accept: application/xml
Content-MD5: string


```

### 请求行

```
PUT /{ObjectName}?tagging HTTP/1.1
```

该 API 接口接受 `PUT` 请求。


### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728 "公共请求头部") 章节。

#### 非公共头部


该请求操作无特殊的请求头部信息。

### 请求体
要设置的标签集合。
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<Tagging>
  <TagSet>
    <Tag>
      <Key>string</Key>
      <Value>string</Value>
    </Tag>
  </TagSet>
</Tagging>
```


具体的数据描述如下：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
Tagging|无|标签集合|Container|是

Container 节点 Tagging 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
TagSet|Tagging|标签集合|Container|是
Container 节点 TagSet 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
Tag|Tagging.TagSet|标签集合, 最多支持 10 个标签|Containers|是
Container 节点 Tag 的内容：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
Key|Tagging.TagSet.Tag|标签的 Key, 长度不超过 128 字节, 支持英文字母、数字、空格、加号、减号、下划线、等号、点号、冒号、斜线|string|是
Value|Tagging.TagSet.Tag|标签的 Value, 长度不超过 256 字节, 支持英文字母、数字、空格、加号、减号、下划线、等号、点号、冒号、斜线|string|是


## 响应
### 响应头

#### 公共响应头

该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729 "公共响应头部") 章节。

#### 特有响应头


该请求操作无特殊的响应头部信息。

### 响应体
该请求响应体为空。

### 错误码

错误码|描述|http状态码
---|---|---
None|设置成功，响应体返回为空|204 [No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)
SignatureDoesNotMatch|提供的签名不符合规则，返回该错误码|403 [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)
NoSuchBucket|Object 所在的 Bucket 不存在，返回该错误码|404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)
NoSuchKey|Object 不存在，返回该错误码|404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)
MalformedXML|XML 格式不合法，请跟 restful api 文档仔细比对|400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)
BadRequest|如超过了允许一个 Object 最大设置的 Tag 数量，目前最大支持 10|400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)
InvalidTag|Tag 的 key 和 value 中包含了保留字符串 cos:|400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)
InvalidTag|Tag 的 key 长度超过了 128 个字符或者 value 超过了 256 个字符|400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)
InvalidTag|Tag的 key 和 value 包含了非法字符, 目前只支持英文字母、数字、空格、加号、减号、下划线、等号、点号、冒号、斜线|400 [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)


## 实际案例

### 请求

```
PUT /dog.jpg?tagging HTTP/1.1
User-Agent: curl/7.29.0
Accept: */*
Host: chengwus3sdktj-1251668577.cos.ap-beijing-1.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDrbAYjEBqqdEconpFi8NPFsOjrnX4LYUE&q-sign-time=1516362723;1517362773&q-key-time=1516362723;1517362773&q-url-param-list=tagging&q-header-list=content-md5;host&q-signature=7428a0606f4b52516453a1ff1ccb84c19b72a206
Content-Md5: LIbd5t5HLPhuNWYkP6qHcQ==
Content-Length: 127
Content-Type: application/x-www-form-urlencoded

<Tagging><TagSet><Tag><Key>name</Key><Value>xiaoming</Value></Tag><Tag><Key>age</Key><Value>18</Value></Tag></TagSet></Tagging>
```

### 响应

```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 19 Jan 2018 11:54:15 GMT
Server: tencent-cos
x-cos-request-id: NWE2MWRjNjdfYWRhZDM1MGFfYWU0MV8xNTlkYg==
```


