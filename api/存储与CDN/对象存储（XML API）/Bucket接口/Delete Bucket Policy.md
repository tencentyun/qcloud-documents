## 功能描述
Delete Bucket Policy请求可以向Bucket删除权限策略。

只有Bucket所有者有权限发起该请求。
假如您没有拥有Delete Bucket Policy的权限，则返回403 Access Denied；
假如您拥有Delete Bucket Policy的权限但不是所有者时，将返回405 Method Not Allowed；
如果权限策略不存在，将返回204 No Content。

## 请求

### 请求语法

```http
DELETE /?policy Http/1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date: date
Authorization: Auth String
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
```json

DELETE /?policy HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484814613;32557710613&q-key-time=1484814613;32557710613&q-header-list=host&q-url-param-list=policy&q-signature=57c9a3f67b786ddabd2c208641944ec7f9b02f98


```
### 返回
```json
HTTP/1.1 204 No Content
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu Jan 19 16:30:21 2017
Server: tencent-cos
x-cos-request-id: NTg4MDc5MWRfNDQyMDRlXzNiMDRfZTEw


```

 
