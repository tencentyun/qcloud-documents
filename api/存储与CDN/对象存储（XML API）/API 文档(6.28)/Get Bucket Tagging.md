## 功能描述
Get Bucket Tagging 接口请求获取指定 Bucket 的标签。该 API 请求使用 GET 的 tagging 子资源实现获取与 Bucket 相关联的标签集。默认情况下，Bucket 的持有者有此操作权限，持有者也可以将权限授予其他用户。

## 请求

语法示例：
```
GET /?tagging HTTP/1.1
Host: <Bucketname>-<AppID>.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth
```

> Authorization: Auth (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
~~~
GET /?tagging HTTP/1.1
~~~
该 API 接口接受 GET 请求。
#### 请求参数
**命令参数**
该 API 接口使用到的命令参数为 tagging。


### 请求头
**公共头部**
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。
**非公共头部**
该请求操作无特殊的请求头部信息。
### 请求体
该请求的请求体为空。

## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
**特有响应头**
该响应无特殊的响应头。
#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：
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

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Tagging |无| 说明所有 TagSet 和 Tag 的信息| Contianer |

Container 节点 Tagging 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| TagSet | Tagging| 说明一系列的 Tag 信息 |  Contianer |

Container 节点 TagSet 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Tag | Tagging.TagSet | 说明单个的 Tag 信息 |  Contianer |

Container 节点 Tag 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Key | Tagging.TagSet.Tag | Tag 的类别名称 | String |
| Value | Tagging.TagSet.Tag | Tag 的值 |  String |
## 实际案例

### 请求
```
GET /?tagging HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Date: Thu, 20 Jan 2015 16:31:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484817283;32557713283&q-key-time=1484817283;32557713283&q-header-list=host&q-url-param-list=tagging&q-signature=b1da7bf83c43fd06fc4c5664ecb832b98966b193
```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 96
Connection: keep-alive
Date: Thu, 20 Jan 2015 16:31:00 GMT
Server: tencent-cos
x-cos-request-id: NTg4MDgzOGJfOWExZjRlXzQ2YTBfZTY0

<Tagging>
    <TagSet>
        <Tag>
            <Key>1</Key>
            <Value>2</Value>
        </Tag>
    </TagSet>
</Tagging>
```

