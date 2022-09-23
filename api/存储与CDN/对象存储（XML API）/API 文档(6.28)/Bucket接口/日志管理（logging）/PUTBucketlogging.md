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

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。


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

|节点名称（关键字）|父节点|描述|类型|是否必选 |
|:---|:-- |:--|:--|:--|
| BucketLoggingStatus |无| 说明日志记录配置的状态，如果无子节点信息则意为关闭日志记录 | Container | 是 |

Container 节点 BucketLoggingStatus 的内容：

|节点名称（关键字）|父节点|描述|类型|是否必选 |
|:---|:-- |:--|:--|:--|
| LoggingEnabled | BucketLoggingStatus | 存储桶 logging 设置的具体信息，主要是目标存储桶 | Container | 否 |

Container 节点 LoggingEnabled 的内容：

|节点名称（关键字）|父节点|描述|类型|是否必选 |
|:---|:-- |:--|:--|:--|
| TargetBucket | LoggingEnabled | 存放日志的目标存储桶，可以是同一个存储桶（但不推荐），或同一账户下、同一地域的存储桶 | String | 否 |
| TargetPrefix | LoggingEnabled | 日志存放在目标存储桶的指定路径 | String | 否 |

>?用户指定存放日志的存储桶和路径后，生成的日志文件名格式为：`目标存储桶/路径前缀{YYYY}/{MM}/{DD}/{time}_{random}_{index}.gz`。

## 响应

#### 响应头
此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。


#### 响应体
该响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求
```shell
PUT /?logging HTTP 1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 10 Mar 2017 09:45:46 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUj****&q-sign-time=1484814927;32557710927&q-key-time=1484814927;32557710927&q-header-list=host&q-url-param-list=accelerate&q-signature=8b9f05dabce2578f3a79d732386e7cbade90****
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
x-cos-request-id: NTg4MDdiZWRfOWExZjRlXzQ2OWVf****
```
