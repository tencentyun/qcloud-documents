## 功能描述
Put Bucket Tagging 接口实现给指定 Bucket 打标签，用来组织和管理相关Bucket。当该请求设置相同 Key 名称，不同 Value 时，会返回 400。请求成功，则返回 204。

## 请求

语法示例：
```
PUT /?tagging HTTP 1.1
Host: <Bucketname>-<AppID>.<Region>.myqcloud.com
Date: GMT Date
Content-Type: application/xml
Authorization: Auth

[XML]
```

> Authorization: Auth (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
~~~
PUT /?tagging HTTP/1.1
~~~
该 API 接口接受 PUT 请求。
#### 请求参数
**命令参数**
该 API 接口使用到的命令参数为 tagging。


### 请求头
**公共头部**
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。
**非公共头部**
该请求操作无特殊的请求头部信息。
### 请求体
该请求的请求体数据节点如下：
```
<Tagging>
  <TagSet>
    <Tag>
      <Key></Key>
      <Value></Value>
    </Tag>
    <Tag>
      ...
    </Tag>
  </TagSet>
</Tagging>
```

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:--|
| Tagging |无| 说明所有 TagSet 和 Tag 的信息| Contianer |是|

Container 节点 Tagging 的内容：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:--|
| TagSet | Tagging| 说明一系列的 Tag 信息 |  Contianer |是|

Container 节点 TagSet 的内容：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:--|
| Tag | Tagging.TagSet | 说明单个的 Tag 信息 |  Contianer |是|

Container 节点 Tag 的内容：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:--|
| Key | Tagging.TagSet.Tag | Tag 的类别名称 | String |是|
| Value | Tagging.TagSet.Tag | Tag 的值 |  String |是|
## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
**特有响应头**
该响应无特殊的响应头。
#### 响应体
该响应体返回为空。

## 实际案例

### 请求
```
PUT /?tagging HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Date: Mon, 10 Jan 2015 12:31:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484817032;32557713032&q-key-time=1484817032;32557713032&q-header-list=host&q-url-param-list=tagging&q-signature=0a99e59b753c26b807e4b372560b0d026d26af26
Content-Type: application/xml
Content-Length: 75

<Tagging>
  <TagSet>
    <Tag>
      <Key>1</Key>
      <Value>2</Value>
    </Tag>
  </TagSet>
</Tagging>

```

### 响应
```
HTTP/1.1 204
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Mon, 10 Jan 2015 12:31:00 GMT
Server: tencent-cos
x-cos-request-id: NTg4MDgyZmRfOTkxZjRlXzEwNjRfZWI2


```

