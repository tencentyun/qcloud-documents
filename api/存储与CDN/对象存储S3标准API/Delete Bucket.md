## 功能描述

Delete Bucket请求可以在指定账号下删除Bucket。必须在删除Bucket下所有Object才能执行Delete Bucket，否则，返回403无权限。
## 请求

### 请求语法

```Http
DELETE / HTTP/1.1
Host: [BucketName]-[UID].[Region].myqcloud.com
Date: date
Authorization: authorization string
```

### 请求参数

无特殊请求参数

### 请求头部

无特殊请求头部，其他内容请参见公共请求头部

### 请求内容

无

## 返回值

### 返回头部

无特殊请求头部，其他内容请参见公共返回头部

### 返回内容

无
