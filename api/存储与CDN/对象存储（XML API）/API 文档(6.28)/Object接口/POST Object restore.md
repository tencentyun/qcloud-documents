## 功能描述
POST Object restore 接口可以对一个通过 COS 归档为 archive 类型的对象进行恢复，恢复出的可读取对象是临时的，您可以设置需要保持可读，以及随后删除该临时副本的时间。您可以用 Days 参数来指定临时对象的过期时间，若超出该时间且期间您没有发起任何复制、延长等操作，该临时对象将被系统自动删除。临时对象仅为 archive 类型对象的副本，被归档的源对象在此期间将始终存在。

## 请求
### 请求示例

```
POST /ObjectName?restore HTTP/1.1
Host: <Bucketname-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String

request body
 ```
> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)


### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。
#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该请求操作的实现需要有如下请求体。

```
<RestoreRequest>
   <Days>NumberOfDays</Days>
   <CASJobParameters>
       <Tier>RetrievalOption</Tier>
   </CASJobParameters>
</RestoreRequest>
```

具体的数据描述如下：

节点名称（关键字）|父节点|描述|类型|必选
---|---|---|---|---
RestoreRequest|无|用于恢复数据的容器|Container|是
Days|无|设置临时副本的过期时间|integer|是
CASJobParameters|无|归档存储工作参数的容器|Container|是
Tier|无|恢复数据时，Tier 可以指定为 CAS 支持的三种恢复类型，分别为 Expedited、Standard、Bulk |Enum|是

## 响应
### 响应头

#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
该响应体为空。

### 错误码
该请求操作可能会出现如下错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 章节。

错误码|描述|HTTP 状态码
---|---|---
None|恢复成功|202 [Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)
RestoreAlreadyInProgress|对象已经在恢复中|409 [Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)


## 实际案例

### 请求

```
POST /arvin/arvin6.txt?restore HTTP/1.1
Accept: */*
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:arvin1-7319456.cn-north.myqcloud.com
Content-Length: 105
Content-Type: application/x-www-form-urlencoded

<RestoreRequest>
   <Days>NumberOfDays</Days>
   <CASJobParameters>
       <Tier>RetrievalOption</Tier>
   </CASJobParameters>
</RestoreRequest>
```

### 响应

```
HTTP/1.1 202 Accepted
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-cos
x-cos-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=
```


