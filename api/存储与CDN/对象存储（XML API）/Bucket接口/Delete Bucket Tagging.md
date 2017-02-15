## 功能描述
Delete Bucket Tagging接口实现删除指定Bucket的标签。

## 请求

### 请求语法

```HTTP
DELETE /?tagging HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date:date
Authorization: Auth
```

### 请求参数

无特殊请求参数

### 请求头部

无特殊请求头部，其他头部请参见公共请求头部

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

无返回内容

## 示例
### 请求
```xml
DELETE /?tagging HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484817338;32557713338&q-key-time=1484817338;32557713338&q-header-list=host&q-url-param-list=tagging&q-signature=fa13dedef474fe2034d2bb5b93b3afeffb225e5a

```
### 返回
```xml
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu Jan 19 17:15:46 2017
Server: tencent-cos
x-cos-request-id: NTg4MDgzYzJfOWIxZjRlXzZmM2JfZWUw

```
