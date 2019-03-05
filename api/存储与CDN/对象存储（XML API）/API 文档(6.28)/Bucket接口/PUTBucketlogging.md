## 功能描述
PUT Bucket Logging 接口为源存储桶开启日志记录，将源存储桶的访问日志保存到指定的目标存储桶中。

## 请求

### 请求示例
```
PUT /?logging HTTP 1.1
Host: <Bucketname-APPID>.cos.<Region>.myqcloud.com
Date:date
Content-Length: length
Content-Type: application/xml
Content-MD5: MD5
Authorization: Auth String
[XML File]
```

> Authorization: Auth String (详细参见 [访问控制](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求行
~~~
PUT /?logging HTTP 1.1
~~~ 
该 API 接口接受 PUT 请求。
### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

#### 非公共头部
该请求操作的实现需要用帯 Content-MD5 的请求头来验证消息的完整性，具体内容如下：

|名称|描述|类型|必选 |
|:---|:-- |:--|:--|
| Content-MD5 | RFC 1864 中定义的 128 位内容 MD5 算法校验值，用以验证请求体在传输过程中是否有损坏。 | String| 是 |

### 请求体
该请求操作的实现需要有请求体。帯所有节点的请求体内容示例如下：
```
<BucketLoggingStatus>
  <LoggingEnabled>
    <TargetBucket></TargetBucket>
    <TargetPrefix></TargetPrefix>
  </LoggingEnabled>
</BucketLoggingStatus>
```

具体的数据描述如下：<style  rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

|节点名称（关键字）|父节点|描述|类型|必选 |
|:---|:-- |:--|:--|:--|
| BucketLoggingStatus |无| 说明日志记录配置的状态，如果无子节点信息则意为关闭日志记录 | Container | 是 |

Container 节点 BucketLoggingStatus 的内容：

|节点名称（关键字）|父节点|描述|类型|必选 |
|:---|:-- |:--|:--|:--|
| LoggingEnabled | BucketLoggingStatus | 存储桶 logging 设置的具体信息，主要是目标存储桶 | Container | 否 |

Container 节点 LoggingEnabled 的内容：

|节点名称（关键字）|父节点|描述|类型|必选 |
|:---|:-- |:--|:--|:--|
| TargetBucket | LoggingEnabled | 存放日志的目标存储桶 | String | 否 |
| TargetPrefix | LoggingEnabled | 日志存放在目标存储桶的指定路径中 | String | 否 |

## 响应

### 响应头
#### 公共响应头
该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特殊响应头
该响应无特殊的响应头。
### 响应体
该响应体返回为空。

## 实际案例

### 请求
```
PUT /?logging HTTP 1.1
Host: mybucket-1258888888.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Mar 2017 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfABC&q-sign-time=1484814927;32557710927&q-key-time=1484814927;32557710927&q-header-list=host&q-url-param-list=accelerate&q-signature=8b9f05dabce2578f3a79d732386e7cbade9033e3
Content-Type: application/xml
Content-Length: 147

<BucketLoggingStatus>
  <LoggingEnabled>
    <TargetBucket>logbucket</TargetBucket>
    <TargetPrefix>mylogs</TargetPrefix>
  </LoggingEnabled>
</BucketLoggingStatus>
```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 10 Mar 2017 09:45:46 GMT
Server: tencent-cos
x-cos-request-id: NTg4MDdiZWRfOWExZjRlXzQ2OWVfZG==

```

