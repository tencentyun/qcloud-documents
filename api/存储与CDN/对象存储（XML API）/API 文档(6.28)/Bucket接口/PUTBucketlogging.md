## 功能描述
PUT Bucket Logging 接口用于为源存储桶开启日志记录，将源存储桶的访问日志保存到指定的目标存储桶中。

>!
>- 只有源存储桶拥有者才可进行该请求操作。
>- 开启访问日志功能，需要授予日志服务（CLS）产品写入 COS 的权限，授权流程请参见 [启用日志管理](https://cloud.tencent.com/document/product/436/16920#.E5.90.AF.E7.94.A8.E6.97.A5.E5.BF.97.E7.AE.A1.E7.90.86)。

## 请求

#### 请求示例
```shell
PUT /?logging HTTP 1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date:date
Content-Length: length
Content-Type: application/xml
Content-MD5: MD5
Authorization: Auth String
```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


#### 请求头
#### 公共头部

该请求操作的实现需要用 Content-MD5 的请求头来验证消息的完整性，具体内容如下。其他公共请求头详情，请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

|名称|描述|类型|是否必选 |
|:---|:-- |:--|:--|
| Content-MD5 | RFC 1864 中定义的经过 Base64 编码的请求体内容 MD5 哈希值，用于完整性检查，验证请求体在传输过程中是否发生变化 | String| 是 |

#### 请求体
该请求操作的实现需要有请求体。带所有节点的请求体内容示例如下：
```shell
<BucketLoggingStatus>
  <LoggingEnabled>
    <TargetBucket>examplebucket-1250000000</TargetBucket>
    <TargetPrefix>prefix</TargetPrefix>
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
| TargetBucket | LoggingEnabled | 存放日志的目标存储桶，可以是同一个存储桶（但不推荐），或同一账户下、同一地域的存储桶 | String | 否 |
| TargetPrefix | LoggingEnabled | 日志存放在目标存储桶的指定路径 | String | 否 |

## 响应

#### 响应头
此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。


#### 响应体
该响应体返回为空。

## 实际案例

#### 请求
```shell
PUT /?logging HTTP 1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Mar 2017 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfABC&q-sign-time=1484814927;32557710927&q-key-time=1484814927;32557710927&q-header-list=host&q-url-param-list=accelerate&q-signature=8b9f05dabce2578f3a79d732386e7cbade9033e3
Content-Type: application/xml
Content-Length: 147

<BucketLoggingStatus>
  <LoggingEnabled>
    <TargetBucket>examplebucket-1250000000</TargetBucket>
    <TargetPrefix>prefix</TargetPrefix>
  </LoggingEnabled>
</BucketLoggingStatus>
```

#### 响应
```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 10 Mar 2017 09:45:46 GMT
Server: tencent-cos
x-cos-request-id: NTg4MDdiZWRfOWExZjRlXzQ2OWVfZG==
```
