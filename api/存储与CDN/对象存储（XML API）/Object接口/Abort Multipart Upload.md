## 功能描述
Abort Multipart Upload用来实现舍弃一个分块上传并删除已上传的块。当您调用Abort Multipart Upload时，如果有正在使用这个Upload Parts上传块的请求，则Upload Parts会返回失败。当该UploadID不存在时，会返回404 NoSuchUpload。

建议您及时完成分块上传或者舍弃分块上传，因为已上传但是未终止的块会占用存储空间进而产生存储费用。

## 请求

### 请求语法

```http
DELETE /ObjectName?uploadId=UploadId HTTP 1.1
Host: <BucketName>-<UID>.<Region>.myqcloud.com
Date: date
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

```HTTP
DELETE /ObjectName?uploadId=1484727270323ddb949d528c629235314a9ead80f0ba5d993a3d76b460e6a9cceb9633b08e HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484728626;32557624626&q-key-time=1484728626;32557624626&q-header-list=host&q-url-param-list=uploadId&q-signature=2d3036b57cade4a257b48a3a5dc922779a562b18
```

### 返回

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Wed Jan 18 16:37:13 2017
Server: tencent-cos
x-cos-request-id: NTg3ZjI5MzlfOTgxZjRlXzZhYjNfMjBh
```

