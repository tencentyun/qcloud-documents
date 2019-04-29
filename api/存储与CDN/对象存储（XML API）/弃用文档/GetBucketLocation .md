## 功能描述
GET Bucket location 接口用于获取 Bucket 所在的地域信息，该 GET 操作使用 location 子资源返回 Bucket 所在的区域，只有 Bucket 持有者才有该 API 接口的操作权限。
### 细节分析
1. 目前区域的有效值请参阅 [可用地域](https://cloud.tencent.com/document/product/436/6224) 文档。
2.  查看 Bucket 区域信息，需要有该 Bucket 的读权限。

## 请求

语法示例：
```
GET /?location HTTP/1.1
Host: <Bucketname-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求行
~~~
GET /?location HTTP/1.1
~~~
该 API 接口接受 GET 请求。

### 请求头
#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。
#### 非公共头部
该请求操作无特殊的请求头部信息。
### 请求体
该请求的请求体为空。

## 响应

### 响应头
#### 公共响应头 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该响应无特殊有响应头。
### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：
```
<LocationConstraint></LocationConstraint>
```
具体的数据内容如下：
<style rel="stylesheet"> table th:nth-of-type(1) { width: 200px;	} </style>

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| LocationConstraint |无| 说明 Bucket 所在地域，枚举值参见 [可用地域](https://cloud.tencent.com/document/product/436/6224) 文档，如：ap-beijing, ap-hongkong, eu-frankfurt 等 | String |

## 实际案例

### 请求
```
GET /?location HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed, 18 Oct 2014 22:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484817522;32557713522&q-key-time=1484817522;32557713522&q-header-list=host&q-url-param-list=location&q-signature=ceb96fc929663dd4d2e6dc0aeb304cdde6761ed0
```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 92
Connection: keep-alive
Date: Wed, 18 Oct 2014 22:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg4MDg0NzlfNDYyMDRlXzM0OWFfZjFk

<LocationConstraint>cos.ap-beijing</LocationConstraint>
```

