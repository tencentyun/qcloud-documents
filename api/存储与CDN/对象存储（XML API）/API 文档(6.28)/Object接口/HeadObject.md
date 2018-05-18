## 功能描述
Head Object 接口请求可以获取对应 Object 的 meta 信息数据，Head 的权限与 Get 的权限一致。

## 请求
#### 请求语法示例

**shell:** 

```shell
# You can also use curl
curl -X HEAD http://{bucket}.cos.{region}.myqcloud.com/{ObjectName} \
  -H 'If-Modified-Since: string'

```

**http:** 

```http
HEAD http://{bucket}.cos.{region}.myqcloud.com/{ObjectName} HTTP/1.1
Host: 


If-Modified-Since: string


```

### 请求行

```
HEAD /{ObjectName} HTTP/1.1
```

该 API 接口接受 `HEAD` 请求。


### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728 "公共请求头部") 章节。

#### 非公共头部


名称|类型|必选|描述
---|---|---|---
If-Modified-Since|string|否|当 Object 在指定时间后被修改，则返回对应 Object 的 meta 信息，否则返回 304


### 请求体
该请求请求体为空。
## 响应
### 响应头

#### 公共响应头

该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729 "公共响应头部") 章节。

#### 特有响应头

该请求操作的响应头具体数据为：

|名称|类型|描述|
|---|---|---|
|x-cos-meta- *|string|用户自定义的 meta|
|x-cos-object-type|string|用来表示 Object 是否可以被追加上传，枚举值：normal 或者 appendable|
|x-cos-storage-class|string|Object 的存储级别，枚举值：STANDARD,STANDARD_IA, NEARLINE|

### 响应体
该请求响应体为空。

## 实际案例

### 请求

```
HEAD /123 HTTP/1.1
Host: zuhaotestnorth-1251668577.cos.ap-beijing.myqcloud.com
Date: Thu, 12 Jan 2017 17:26:53 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213210;32557109210&q-key-time=1484213210;32557109210&q-header-list=host&q-url-param-list=&q-signature=ac61b8eb61964e7e6b935e89de163a479a25c210
```

### 响应

```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 16087
Connection: keep-alive
Date: Thu, 12 Jan 2017 17:26:53 GMT
ETag: \"9a4802d5c99dafe1c04da0a8e7e166bf\"
Last-Modified: Wed, 11 Jan 2017 07:30:07 GMT
Server: tencent-cos
x-cos-object-type: normal
x-cos-request-id: NTg3NzRiZGRfYmRjMzVfM2Y2OF81N2YzNA==
x-cos-storage-class: STANDARD
```


