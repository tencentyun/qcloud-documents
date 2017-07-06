## 功能描述
Delete Object 接口请求可以在 COS 的 Bucket 中将一个文件（Object）删除。该操作需要请求者对 Bucket 有 WRITE 权限。
## 请求

语法示例：
```
DELETE /ObjectName HTTP/1.1
Host:<BucketName>-<AppID>.<Region>.myqcloud.com
Date: GMT Date
Content-Length: length
Authorization: Auth String
```

> Authorization: Auth String (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
```
DELETE /ObjectName HTTP/1.1
```
#### 请求参数
**命令参数**
该 API 接口使用到的命令参数为 &lt;ObjectName&gt;。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。

#### 非公共头部
该请求操作无特殊的请求头部信息。


### 请求体
该请求的请求体空。

## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
**特有响应头**
该请求操作无特殊的响应头。


#### 响应体
该请求的响应体为空



## 实际案例

### 请求
```
DELETE /123 HTTP/1.1
Host: zuhaotestnorth-1251668577.cn-north.myqcloud.com
Date: Wed, 23 Oct 2016 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213409;32557109409&q-key-time=1484213409;32557109409&q-header-list=host&q-url-param-list=&q-signature=1c24fe260ffe79b8603f932c4e916a6cbb0af44a

```

### 响应
```
HTTP/1.1 204 No Content
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed, 23 Oct 2016 21:32:00 GMT
Server: tencent-cos
x-cos-request-id: NTg3NzRjYTRfYmRjMzVfMzFhOF82MmM3Yg==

```
