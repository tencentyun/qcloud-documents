## 功能描述
Get Object 接口请求可以在 COS 的 Bucket 中将一个文件（Object）下载至本地。该操作需要请求者对目标 Object 具有读权限或目标 Object 对所有人都开放了读权限（公有读）。

## 请求

语法示例：
```
GET /<ObjectName> HTTP/1.1
Host: <BucketName>-<AppID>.<Region>.myqcloud.com
Date: GMT Date
Authorization: auth
```

> Authorization: Auth (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
```
GET /<ObjectName> HTTP/1.1
```

#### 请求参数
**命令参数**
该 API 接口使用到的命令参数为 ObjectName。
在发送该 GET 请求时，可以自定义 COS 响应数据中的一些参数，但 发送 Get Object 请求时必须携带签名。这些参数包括：

|参数名称|描述|类型| 必选|
|:---|:-- |:---|:-- |
| response-content-type |设置响应头部中的 Content-Type 参数。|String| 否|
| response-content-language |设置响应头部中的 Content-Language 参数。|String| 否|
| response-expires |设置响应头部中的 Content-Expires 参数。 |String| 否|
| response-cache-control |设置响应头部中的 Cache-Control 参数。|String| 否|
| response-content-disposition |设置响应头部中的 Content-Disposition 参数。|String| 否|
| response-content-encoding |设置响应头部中的 Content-Encoding 参数。|String| 否|

### 请求头

**公共头部**
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。

**非公共头部**
该请求操作推荐使用如下推荐请求头：

|参数名称|描述|类型| 必选|
|:---|:-- |:---|:-- |
| Range |RFC 2616 中定义的指定文件下载范围，以字节（bytes）为单位。|String| 否|
| If-Modified-Since |如果文件修改时间晚于指定时间，才返回文件内容。否则返回 304 (not modified)。|String| 否|
### 请求体
该请求的请求体为空。

## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
**特有响应头**

|参数名称|描述|类型|
|:---|:-- |:-- |
| x-cos-meta-`*` | 用户自定义的元数据|String|
| x-cos-object-type | 用来表示 object 是否可以被追加上传，枚举值：normal 或者 appendable |String|
| x-cos-storage-class | Object 的存储级别，枚举值：STANDARD，STANDARD_IA，NEARLINE|String|

#### 响应体
Object 的文件内容。



## 实际案例

### 请求
```
GET /123 HTTP/1.1
Host:zuhaotestnorth-1251668577.cn-north.myqcloud.com
Date: Wed, 28 Oct 2014 22:32:00 GMT
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484212200;32557108200&q-key-time=1484212200;32557108200&q-header-list=host&q-url-param-list=&q-signature=11522aa3346819b7e5e841507d5b7f156f34e639
```

### 响应
```
HTTP/1.1 200 OK
Date: Wed, 28 Oct 2014 22:32:00 GMT
Content-Type: application/octet-stream
Content-Length: 16087
Connection: keep-alive
Accept-Ranges: bytes
Content-Disposition: attachment; filename*="UTF-8''123"
Content-Range: bytes 0-16086/16087
ETag: "9a4802d5c99dafe1c04da0a8e7e166bf"
Last-Modified: Wed, 28 Oct 2014 20:30:00 GMT
x-cos-object-type: normal
x-cos-request-id: NTg3NzQ3ZmVfYmRjMzVfMzE5N182NzczMQ==

[Object]
```
