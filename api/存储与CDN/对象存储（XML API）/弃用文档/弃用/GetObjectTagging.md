## 功能描述
Get Object Tagging 用来查询 Object 的标签集合。

## 请求
#### 请求语法示例

**shell:** 

```shell
# You can also use curl
curl -X GET http://{bucket}.cos.{region}.myqcloud.com/{ObjectName}?tagging \
  -H 'Accept: application/xml'

```

**http:** 

```http
GET http://{bucket}.cos.{region}.myqcloud.com/{ObjectName}?tagging HTTP/1.1
Host: 

Accept: application/xml

```

### 请求行

```
GET /{ObjectName}?tagging HTTP/1.1
```

该 API 接口接受 `GET` 请求。


### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728 "公共请求头部") 章节。

#### 非公共头部


该请求操作无特殊的请求头部信息。

### 请求体
该请求请求体为空。
## 响应
### 响应头

#### 公共响应头

该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729 "公共响应头部") 章节。

#### 特有响应头


该请求操作无特殊的响应头部信息。

### 响应体
获取 Tag 成功。
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


### 错误码

错误码|描述|http状态码
---|---|---
SignatureDoesNotMatch|提供的签名不符合规则，返回该错误码|403 [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)
NoSuchBucket|当访问的 Bucket 不存在，返回该错误码|404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)
NoSuchKey|文件路径不存在|404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)


## 实际案例

### 请求

```
GET /dog.jpg?tagging HTTP/1.1
User-Agent: curl/7.29.0
Accept: */*
Host: chengwus3sdktj-1251668577.cos.ap-beijing-1.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDrbAYjEBqqdEconpFi8NPFsOjrnX4LYUE&q-sign-time=1516362907;1517362957&q-key-time=1516362907;1517362957&q-url-param-list=tagging&q-header-list=host&q-signature=af98c8e4b249aed72e89854a7879bc0e0e5127f4
```

### 响应

```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 202
Connection: keep-alive
Date: Fri, 19 Jan 2018 11:56:07 GMT
Server: tencent-cos
x-cos-request-id: NWE2MWRjZDdfMmJiMjM1MGFfNThmZV8xOTk4Mg==

<?xml version='1.0' encoding='utf-8' ?>
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


