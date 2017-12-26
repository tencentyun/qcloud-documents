## 功能描述

POST Object restore 接口可以对一个通过 COS 归档为 archive 类型的对象进行恢复，恢复出的可读取对象是临时的，您可以设置需要保持可读，以及随后删除该临时副本的时间。

您可以用 Days 参数来指定临时对象的过期时间，若超出该时间且期间您没有发起任何复制、延长等操作，该临时对象将被系统自动删除。临时对象仅为 archive 类型对象的副本，被归档的源对象在此期间将始终存在。

### 恢复模式

通过 COS 的生命周期功能归档为 archive 类型的对象，是不可以被直接读取的，您需要先将归档的对象通过该接口恢复（复制）成一个临时副本，期间 archive 类型的对象仍然存在。您可以选择以下几种恢复速度的模式：

- Expedited：当紧急需要恢复数据时，该模式提供了最快的恢复速度，费用较高 。对于小于  256 MB 的文件，在 1~5 分钟的时间内即可获得临时副本。
- Standard：**默认为该模式**，该模式提供了在 3~5 小时后恢复临时副本的能力，通常适用于不太紧急的恢复任务。
- Bulk：该模式的恢复成本最低，适用于在一天内提供副本的数据恢复。通常 Bulk 模式可以在 5~12 小时后提供临时副本。

### 恢复功能说明

#### 查看恢复状态

通过发起 HEAD Object 请求，您可以获得 archive 类型对象的当前恢复状态，状态于 x-cos-restore 头部中提供。

#### 延长临时副本的过期时间

再次发起 POST Object restore，您可以对已经恢复的临时对象进行延期，延期删除的时间将从再次发起请求的时间开始计算。

如果存储桶包含生命周期的配置，则需注意所配置的过期时间，系统将自动执行较短的过期时间配置。例如生命周期配置了所有对象 3 天过期，而恢复对象时指定了 10 天过期，则临时副本将在 3 天后被删除。

#### 恢复错误状态

您无法对于已经在恢复中的对象执行该操作，您将收到如下错误响应：

```http
HTTP/1.1 409 Conflict
```

您无法对于一个非 archive 类型的对象执行该操作，您将收到如下响应：

```http
HTTP/1.1 405 Method Not Allowed
```

## 请求

语法示例：

```http
POST /ObjectName?restore HTTP 1.1
Host:<BucketName-APPID>.<Region>.myqcloud.com
Content-Length: length
Date: GMT Date
Authorization: Auth String 
Content-MD5: MD5

Restore configuration in the request body
```

> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求行

```http
POST /ObjectName?restore HTTP 1.1
```

该 API 接口接受 POST 请求。

### 请求头

**公共头部**
该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

**非公共头部**
该请求操作的实现需要用帯 Content-MD5 的请求头来验证消息的完整性，具体内容如下：

| 名称          | 描述                                       | 类型     | 必选   |
| ----------- | ---------------------------------------- | ------ | ---- |
| Content-MD5 | RFC 1864 中定义的 128位 内容 MD5 算法校验值，用以验证请求体在传输过程中是否有损坏。 | String | 是    |

### 请求体

该请求操作的实现需要有请求体。帯所有节点的请求体内容示例如下：

```xml
<RestoreRequest>
   <Days>NumberOfDays</Days>
   <CASJobParameters>
       <Tier>RetrievalOption</Tier>
   </CASJobParameters>
</RestoreRequest> 
```

具体的数据描述如下：

| 名称               | 父节点              | 描述                                       | 类型        | 必选   |
| ---------------- | ---------------- | ---------------------------------------- | --------- | ---- |
| RestoreRequest   | 无                | 说明恢复数据的配置信息                              | Container | 是    |
| Days             | RestoreRequest   | 设置临时副本的过期时间                              | Integer   | 是    |
| CASJobParameters | RestoreRequest   | 复原的过程类型配置信息                              | Container | 否    |
| Tier             | CASJobParameters | 具体复原过程类型，枚举值： `Expedited` ，`Standard` ，`Bulk`；默认值：`Standard` | String    | 否    |

## 响应

响应示例：

```http
HTTP/1.1 202 Accepted
Content-Type: application/xml
Date: Sat, 05 Aug 2017 07:13:50 GMT
Content-Length: 0
Server: tencent-cos
x-cos-request-id: NTk4NTcwMDNfMjQ4OGY3MGFfNDI0Y181
```

### 响应头

#### 公共响应头

该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。

#### 特有响应头

该响应无特殊的响应头。

### 响应体

该响应体返回为空。

## 实际案例

### 请求

```http
POST /arvin/arvin6.txt?restore HTTP/1.1
Accept: */*
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host:arvin1-7319456.cn-north.myqcloud.com
Content-Length: 105
Content-Type: application/x-www-form-urlencoded
```

### 响应

```http
HTTP/1.1 202 Accepted
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-cos
x-cos-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=
```

### 错误：对象已经在恢复中

```http
HTTP/1.1 409 Conflict
Content-Type: application/xml
Content-Length: 476
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-cos
x-cos-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjg=
x-cos-trace-id: OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODczNTBmNjMwZmQ0MTZkMjg0NjlkNTYyNmY4ZTRkZTk0NzNiZDc3OTU1NzQ4ZmVhODc3MzdkMzBlNGEzMmQ2ZDEyMjgyNWIxZDljY2VmMzAwYTQyMjI4ZjU2NmFhMjJkYzg=

<?xml version='1.0' encoding='utf-8' ?>
<Error>
	<Code>RestoreAlreadyInProgress</Code>
	<Message>Object restore is already in progress.</Message>
	<Resource>arvin1-7319456.cn-north.myqcloud.com/arvin6.txt</Resource>
	<RequestId>NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjg=</RequestId>
	<TraceId>OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODczNTBmNjMwZmQ0MTZkMjg0NjlkNTYyNmY4ZTRkZTk0NzNiZDc3OTU1NzQ4ZmVhODc3MzdkMzBlNGEzMmQ2ZDEyMjgyNWIxZDljY2VmMzAwYTQyMjI4ZjU2NmFhMjJkYzg=</TraceId>
</Error>
```

