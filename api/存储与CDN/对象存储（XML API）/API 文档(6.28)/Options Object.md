## 功能描述
Options Object 接口实现 Object 跨域访问配置的预请求。即在发送跨域请求之前会发送一个 OPTIONS 请求并带上特定的来源域，HTTP 方法和 HEADER 信息等给 COS，以决定是否可以发送真正的跨域请求。当 CORS 配置不存在时，请求返回403 Forbidden。
可以通过 Put Bucket CORS 接口来开启 Bucket 的 CORS 支持。

## 请求

语法示例：
```
OPTIONS /ObjectName HTTP/1.1
Host: <Bucketname>-<AppID>.<Region>.myqcloud.com
Date: GMT Date
Origin: Origin
Access-Control-Request-Method: HTTPMethod
Access-Control-Request-Headers: RequestHeader
Authorization: Auth String
```

> Authorization: Auth String (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
```
OPTIONS /ObjectName HTTP/1.1
```
该 API 接口接受 OPTIONS 请求。
#### 请求参数
**命令参数**
该 API 接口使用到的命令参数为 ObjectName。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。

#### 非公共头部
**必选头部**
该请求操作需要请求头帯必选头部参数，具体内容如下：

|名称|描述|类型|必选|
|:---|:---|:---|:---|
| Origin | 模拟跨域访问的请求来源域 | String | 是 |
| Access-Control-Request-Method | 模拟跨域访问的请求 HTTP 方法| String | 是 |


**推荐头部**
该请求操作推荐请求头使用推荐头部参数，具体内容如下：

|名称|描述|类型|必选|
|:---|:---|:---|:---|
| Access-Control-Request-Headers | 模拟跨域访问的请求头部 | String | 否 |

### 请求体
该请求的操作请求体为空。

## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
**特有响应头**
该请求操作的响应头具体数据为：

|名称|描述|类型|
|:---|:---|:---|
| Access-Control-Allow-Origin | 模拟跨域访问的请求来源域名，当来源不允许的时候，此 Header 不返回。 | String | 
| Access-Control-Allow-Methods | 模拟跨域访问的请求 HTTP 方法，当请求方法不允许的时候，此 Header 不返回。 | String | 
| Access-Control-Allow-Headers | 模拟跨域访问的请求头部，当模拟任何请求头部不允许的时候，此 Header 不返回该请求头部。| String | 
| Access-Control-Expose-Headers | 跨域支持返回头部，用逗号区分| String | 
| Access-Control-Max-Age | 设置 OPTIONS 请求得到结果的有效期 | String | 

#### 响应体
该请求的响应体为空。
## 实际案例

### 请求
```
OPTIONS /coss3/ObjectName HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Date: Thu, 12 Jan 2017 17:26:53 GMT
Origin: http://www.qq.com
Access-Control-Request-Method: PUT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn&q-sign-time=1487070734;32466654734&q-key-time=1487070734;32559966734&q-header-list=host&q-url-param-list=&q-signature=2ac3ada19910f44836ae0df72a0ec1003f34324b

```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Headers: x-cos-meta-test
Access-Control-Allow-Methods: PUT
Access-Control-Allow-Origin: http://www.qq.com
Access-Control-Expose-Headers: x-cos-meta-test1
Access-Control-Max-Age: 500
Date: Thu, 12 Jan 2017 17:26:53 GMT
Server: tencent-cos
x-cos-request-id: NThhMmU2NmZfMmM4OGY3XzZjZGFfMTkzNw==

```
