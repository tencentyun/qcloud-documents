## 功能描述
Delete Bucket Tagging 接口用来实现删除指定 Bucket 的标签。

## 请求

语法示例：
```
DELETE /?tagging HTTP/1.1
Host: <Bucketname>-<AppID>.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth

```

> Authorization: Auth (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
~~~
DELETE /?tagging HTTP/1.1
~~~
该 API 接口接受 DELETE 请求。
#### 请求参数
**命令参数**
该 API 接口使用到的命令参数为 tagging。


### 请求头
**公共头部**
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。
**非公共头部**
该请求操作无特殊的请求头部信息。
### 请求体
该请求的请求体为空。

## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
**特有响应头**
该响应无特殊的响应头。
#### 响应体
该响应体返回为空。

## 实际案例

### 请求
```
DELETE /?tagging HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Date: Fri, 15 Jan 2014 15:31:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484817338;32557713338&q-key-time=1484817338;32557713338&q-header-list=host&q-url-param-list=tagging&q-signature=fa13dedef474fe2034d2bb5b93b3afeffb225e5a
```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 15 Jan 2014 15:31:00 GMT
Server: tencent-cos
x-cos-request-id: NTg4MDgzYzJfOWIxZjRlXzZmM2JfZWUw

```

