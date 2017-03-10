## 功能描述
Options Object请求实现跨域访问的预请求。即发出一个 OPTIONS 请求给服务器以确认是否可以进行跨域操作。

当CORS配置不存在时，请求返回403 Forbidden。

## 请求

### 请求语法

```HTTP
OPTIONS /ObjectName HTTP 1.1
Host:<Bucketname>-<AppID>.<Region>.myqcloud.com
Origin:Origin
Access-Control-Request-Method:HTTPMethod
Access-Control-Request-Headers:RequestHeader
```

### 请求参数

无特殊请求参数

### 请求头部

#### 必选头部

| 名称                            | 描述              | 类型     | 必选   |
| ----------------------------- | --------------- | ------ | ---- |
| Origin                        | 模拟跨域访问的请求来源域名   | String | 是    |
| Access-Control-Request-Method | 模拟跨域访问的请求HTTP方法 | String | 是    |

#### 推荐使用头部

| 名称                             | 描述          | 类型     | 必选   |
| ------------------------------ | ----------- | ------ | ---- |
| Access-Control-Request-Headers | 模拟跨域访问的请求头部 | String | 否    |


### 请求内容

无请求内容

## 返回值

### 返回头部

| 名称                            | 描述                                       | 类型     |
| ----------------------------- | ---------------------------------------- | ------ |
| Access-Control-Allow-Origin   | 模拟跨域访问的请求来源域名，当来源不允许的时候，此Header不返回。      | String |
| Access-Control-Allow-Methods  | 模拟跨域访问的请求HTTP方法，当请求方法不允许的时候，此Header不返回。  | String |
| Access-Control-Allow-Headers  | 模拟跨域访问的请求头部，当模拟任何请求头部不允许的时候，此Header不返回该请求头部。 | String |
| Access-Control-Expose-Headers | 跨域支持返回头部，用逗号区分                           | String |
| Access-Control-Max-Age        | 设置 OPTIONS 请求得到结果的有效期                    | String |

### 返回内容

无返回内容

## 示例

### 请求
```http
OPTIONS /coss3/ObjectName HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Origin:http://www.qq.com
Access-Control-Request-Method:PUT
Authorization:q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn&q-sign-time=1487070734;32466654734&q-key-time=1487070734;32559966734&q-header-list=host&q-url-param-list=&q-signature=2ac3ada19910f44836ae0df72a0ec1003f34324b

```
### 返回
```http
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Access-Control-Allow-Headers: x-cos-meta-test
Access-Control-Allow-Methods: PUT
Access-Control-Allow-Origin: http://www.qq.com
Access-Control-Expose-Headers: x-cos-meta-test1
Access-Control-Max-Age: 500
Date: Tue Feb 14 19:13:51 2017
Server: tencent-cos
x-cos-request-id: NThhMmU2NmZfMmM4OGY3XzZjZGFfMTkzNw==
```
