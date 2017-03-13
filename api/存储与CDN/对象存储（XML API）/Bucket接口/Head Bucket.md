## 功能描述

Head Bucket请求可以确认是否存在该Bucket，是否有权限访问，Head的权限与Read一致。当其存在时，返回 HTTP 状态码200；当无权限时，返回 HTTP 状态码403；当不存在时，返回 HTTP 状态码404。

## 请求

### 请求语法

```http
HEAD / Http/1.1
Host:<BucketName>-<AppID>.<Region>.myqcloud.com
Date: date
Authorization: auth
```

### 请求参数

无特殊请求参数

### 请求头部

无特殊请求头部，其他头部参见公共请求头部

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部参见公共返回头部

### 返回内容

无返回内容

## 示例

### 请求

```HTTP
HEAD / HTTP/1.1
Host:zuhaotestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484640517;32557536517&q-key-time=1484640517;32557536517&q-header-list=host&q-url-param-list=&q-signature=7bedc2f84a0a3d29df85fe727d0c1e388c410376
```

### 返回

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Tue Jan 17 16:09:39 2017
x-cos-request-id: NTg3ZGQxNDNfNDUyMDRlXzUyOWNfMjY5
```

