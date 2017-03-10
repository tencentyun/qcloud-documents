## 功能描述
Delete Object请求可以将一个文件（Object）删除。

## 请求

### 请求语法

```Http
DELETE /ObjectName HTTP/1.1
Host:<BucketName>-<AppID>.<Region>.myqcloud.com
Date: date
Content-Length:length
Authorization: auth
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

```HTTP
DELETE /123 HTTP/1.1
Host:zuhaotestnorth-1251668577.cn-north.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213409;32557109409&q-key-time=1484213409;32557109409&q-header-list=host&q-url-param-list=&q-signature=1c24fe260ffe79b8603f932c4e916a6cbb0af44a
```

### 返回

```HTTP
HTTP/1.1 204 No Content
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Thu Jan 12 17:30:12 2017
Server: tencent-cos
x-cos-request-id: NTg3NzRjYTRfYmRjMzVfMzFhOF82MmM3Yg==
```

