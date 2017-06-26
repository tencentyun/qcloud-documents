## 功能描述
Get Service 接口是用来获取请求者名下的所有存储空间列表（Bucket list）。该 API 接口不支持匿名请求，您需要使用帯 Authorization 签名认证的请求才能获取 Bucket 列表，且只能获取签名中 AccessID 所属账户的 Bucket 列表。

## 请求

语法示例：
```
GET / HTTP 1.1
Host:service.cos.myqcloud.com
Date:date
Authorization: Auth
```

> Authorization:  Auth (详细参见 [访问控制](http://gggggggg) 章节)

### 请求行
~~~
GET / HTTP 1.1
~~~
该 API 接口接受 GET 请求。

### 请求头

**公共头部**
该请求操作的实现使用公共请求头,了解公共请求头详细请参见[公共请求头部]()章节。
**非公共头部**
该请求操作无特殊的请求头部信息。
### 请求体
该请求的请求体为空。

## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见[公共响应头部]()章节。
**特有响应头**
该响应无特殊有响应头。
#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```
<ListAllMyBucketsResult>
  <Owner>
   <ID></ID>
   <DisplayName></DisplayName>
  </Owner>
  <Buckets>
    <Bucket>
      <Name></Name>
      <Location></Location>
      <CreateDate></CreateDate>
    </Bucket>
   ...
  </Buckets>
</ListAllMyBucketsResult>
```

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| ListAllMyBucketsResult |无| 说明本次响应的所有信息 | Container |

Container 节点  ListAllMyBucketsResult  的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Owner | ListAllMyBucketsResult | 说明 Bucket 持有者的信息 | Container |
| Buckets | ListAllMyBucketsResult | 说明本次响应的所有 Bucket 列表信息 | Container |


Container 节点 Owner 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| ID  | ListAllMyBucketsResult.Owner | Bucket 所有者的 ID     | String    |
| DisplayName  | ListAllMyBucketsResult.Owner | Bucket 所有者的名字信息     | String    |

Container 节点 Buckets 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| Bucket  | ListAllMyBucketsResult.Buckets | 单个 Bucket 的信息  | Container    |

Container 节点 Bucket 的内容：

| 节点名称（关键字）          |父节点 | 描述                                    | 类型        |
| ------------ | ------------------------------------- | --------- |:--|
| Name      | ListAllMyBucketsResult.Buckets.Bucket | Bucket 的名称                               | String    |
| Location        | ListAllMyBucketsResult.Buckets.Bucket  | Bucket 所在区域。枚举值：china-east，china-south，china-north，china-southwest                             | String    |
| CreateDate          | ListAllMyBucketsResult.Buckets.Bucket | Bucket 创建时间。I SO8601 格式，例如 2016-11-09T08:46:32.000Z  | Date   |



## 实际案例

### 请求
```
GET / HTTP 1.1
Host:service.cos.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1489110340;32468694340&q-key-time=1489110340;32562006340&q-header-list=host&q-url-param-list=&q-signature=cb46d5ce6daed2d3dc0db7130a57193497605620
```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 19935
Connection: keep-alive
Date: Fri Mar 10 09:45:46 2017
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
            <Location>china-south</Location>
            <CreateDate>2016-09-13 15:20:15</CreateDate>
        </Bucket>
        <Bucket>
            <Name>0111</Name>
            <Location>china-south</Location>
            <CreateDate>2017-01-11 17:23:51</CreateDate>
        </Bucket>
        <Bucket>
            <Name>1201new</Name>
            <Location>china-south</Location>
            <CreateDate>2016-12-01 09:45:02</CreateDate>
        </Bucket>
   </Buckets>
</ListAllMyBucketsResult>
```

