## 功能描述
POST Object restore 接口可以对一个通过 COS 归档为 archive 类型的对象进行恢复，恢复出的可读取对象是临时的，您可以设置需要保持可读，以及随后删除该临时副本的时间。您可以用 Days 参数来指定临时对象的过期时间，若超出该时间且期间您没有发起任何复制、延长等操作，该临时对象将被系统自动删除。临时对象仅为 archive 类型对象的副本，被归档的源对象在此期间将始终存在。

## 请求
### 请求示例

```shell
POST /<ObjectKey>?restore HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```
 
> Authorization: Auth String （详情请查阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。
#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该请求操作的实现需要有如下请求体。

```shell
<RestoreRequest>
   <Days>2</Days>
   <CASJobParameters>
       <Tier>Bulk</Tier>
   </CASJobParameters>
</RestoreRequest>
```

具体的数据描述如下：
<table>
   <tr>
      <th nowrap="nowrap">节点名称（关键字）</th>
      <th>父节点</th>
      <th>描述</th>
      <th>类型</th>
      <th>必选</th>
   </tr>
   <tr>
      <td>RestoreRequest</td>
      <td>无</td>
      <td>用于恢复数据的容器</td>
      <td>Container</td>
      <td>是</td>
   </tr>
   <tr>
      <td>Days</td>
      <td>无</td>
      <td>设置临时副本的过期时间</td>
      <td>integer</td>
      <td>是</td>
   </tr>
   <tr>
      <td>CASJobParameters</td>
      <td>无</td>
      <td>归档存储工作参数的容器</td>
      <td>Container</td>
      <td>是</td>
   </tr>
   <tr>
      <td>Tier</td>
      <td>无</td>
      <td>恢复数据时，Tier 可以指定为 CAS 支持的三种恢复模式，分别为 Standard（标准模式，恢复任务在3 - 5小时内完成）、Expedited（极速模式，恢复任务在15分钟内可完成）以及 Bulk（批量模式，恢复任务在5 - 12小时内完成）</td>
      <td>Enum</td>
      <td>是</td>
   </tr>
</table>



## 响应
### 响应头

#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
该响应体为空。

### 错误码
该请求操作可能会出现如下错误信息，常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

错误码|描述|HTTP 状态码
---|---|---
None|恢复成功|202 [Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)
RestoreAlreadyInProgress|对象已经在恢复中|409 [Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)


## 实际案例

### 请求

```shell
POST /exampleobject?restore HTTP/1.1
Accept: */*
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
Content-Length: 105
Content-Type: application/x-www-form-urlencoded

<RestoreRequest>
   <Days>2</Days>
   <CASJobParameters>
       <Tier>Bulk</Tier>
   </CASJobParameters>
</RestoreRequest>
```

### 响应

```shell
HTTP/1.1 202 Accepted
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-cos
x-cos-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=
```


