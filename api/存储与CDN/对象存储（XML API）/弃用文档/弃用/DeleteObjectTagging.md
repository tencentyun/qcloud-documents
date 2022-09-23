## 功能描述
该接口用于删除 Object 的 Tag。

## 请求
#### 请求语法示例

**shell:** 

```shell
# You can also use curl
curl -X DELETE http://{bucket}.cos.{region}.myqcloud.com/{ObjectName}?tagging \
  -H 'Accept: application/xml'

```

**http:** 

```http
DELETE http://{bucket}.cos.{region}.myqcloud.com/{ObjectName}?tagging HTTP/1.1
Host: 

Accept: application/xml

```

### 请求行

```
DELETE /{ObjectName}?tagging HTTP/1.1
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
None|删除成功, 响应体返回为空|204 [No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)
NoSuchBucket|当访问的 Bucket 不存在，返回该错误码|404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)
NoSuchKey|文件路径不存在|404 [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)


## 实际案例

### 请求

```
DELETE /dog.jpg?tagging HTTP/1.1
User-Agent: curl/7.29.0
Accept: */*
Host: chengwus3sdktj-1251668577.cos.ap-beijing-1.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDrbAYjEBqqdEconpFi8NPFsOjrnX4LYUE&q-sign-time=1516362927;1517362977&q-key-time=1516362927;1517362977&q-url-param-list=tagging&q-header-list=host&q-signature=da82624189ea0982bcd2928d717a584af6d3789b
```

### 响应

```
HTTP/1.1 204 No Content
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 19 Jan 2018 11:56:23 GMT
Server: tencent-cos
x-cos-request-id: NWE2MWRjZTdfNTJhZTM1MGFfNGJkY18yYjYyOQ==
```


