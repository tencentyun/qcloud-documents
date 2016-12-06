## 功能描述

Head Bucket请求可以确认是否存在该Bucket已经是否有权限访问，Head的权限与Read一致。当其存在时，返回 HTTP 状态码200；当无权限时，返回 HTTP 状态码403；当不存在时，返回 HTTP 状态码404。

## 请求

### 请求语法

```http
GET / Http/1.1
Host:<BucketName>-<UID>.<Region>.myqcloud.com
Date: *date*
Authorization: authorization string
```

### 请求参数

无特殊请求参数

#### 推荐使用头部

无特殊请求Header，继承公共请求Header：Authorizaton，Host，Date

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回Header，继承公共返回Header：x-cos-request-id，x-cos-troubleshoot-id，Date，Server

### 返回内容

无返回内容