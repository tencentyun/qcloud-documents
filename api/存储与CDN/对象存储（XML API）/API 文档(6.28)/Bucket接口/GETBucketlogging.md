## 功能描述
GET Bucket logging 用于获取源存储桶的日志配置信息。

>!只有源存储桶拥有者才可进行该请求操作。

## 请求

#### 请求示例
```shell
GET /?logging HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。

#### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。
#### 非公共头部
该请求操作无特殊的请求头部信息。
#### 请求体
该请求的请求体为空。

## 响应

#### 响应头
#### 公共响应头 

该响应使用公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头
该响应无特殊的响应头。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：
```shell
<BucketLoggingStatus>
  <LoggingEnabled>
    <TargetBucket>examplebucket-1250000000</TargetBucket>
    <TargetPrefix>prefix</TargetPrefix>
  </LoggingEnabled>
</BucketLoggingStatus>
```
具体的数据内容如下：<style  rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| BucketLoggingStatus |无| 存储桶日志状态信息 | Container |

Container 节点 BucketLoggingStatus 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| LoggingEnabled | BucketLoggingStatus | 存储桶日志记录配置详细信息 |  Container |

Container 节点 LoggingEnabled 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| TargetBucket | LoggingEnabled | 存放日志的目标存储桶，可以是同一个存储桶（但不推荐），或同一账户下、同一地域的存储桶  |  String |
| TargetPrefix | LoggingEnabled | 日志存放在目标存储桶的指定路径 |  String |

## 实际案例

#### 请求
```shell
GET /?logging HTTP 1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 28 Oct 2017 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9&q-sign-time=1484815944;32557711944&q-key-time=1484815944;32557711944&q-header-list=host&q-url-param-list=accelerate&q-signature=a2d28e1b9023d09f9277982775a4b3b705d0e23e
```

#### 响应
```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 142
Connection: keep-alive
Date: Wed, 28 Oct 2017 21:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg4MDdlNGZfNDYyMDRlXzM0YWFfZT==

<BucketLoggingStatus>
  <LoggingEnabled>
    <TargetBucket>examplebucket-1250000000</TargetBucket>
    <TargetPrefix>prefix</TargetPrefix>
  </LoggingEnabled>
</BucketLoggingStatus>
```
