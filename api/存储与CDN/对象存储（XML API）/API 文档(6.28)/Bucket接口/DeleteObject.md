## 功能描述
Delete Object 接口请求可以在 COS 的 Bucket 中将一个文件（Object）删除。该操作需要请求者对 Bucket 有 WRITE 权限。

## 请求
#### 请求语法示例

**shell:** 

```shell
# You can also use curl
curl -X DELETE http://{bucket}.cos.{region}.myqcloud.com/{ObjectName} \
  -H 'Accept: application/xml'

```

**http:** 

```http
DELETE http://{bucket}.cos.{region}.myqcloud.com/{ObjectName} HTTP/1.1
Host: 

Accept: application/xml

```

### 请求行

```
DELETE /{ObjectName} HTTP/1.1
```

该 API 接口接受 `DELETE` 请求。


### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728 "公共请求头部") 章节。

#### 非公共头部


该请求操作无特殊的请求头部信息。

### 请求体
该请求请求体为空。
## 响应
### 响应头

#### 公共响应头

该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729 "公共响应头部") 章节。

#### 特有响应头


该请求操作无特殊的响应头部信息。

### 响应体
该请求响应体为空。

### 错误码

错误码|描述|http状态码
---|---|---
SignatureDoesNotMatch|提供的签名不符合规则，返回该错误码|403 [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)
NoSuchBucket|Bucket 不存在，返回该错误码|404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)


## 实际案例

### 请求

```
DELETE /123 HTTP/1.1
Host: zuhaotestnorth-1251668577.cos.ap-beijing.myqcloud.com
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


