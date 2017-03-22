## 功能描述

Get Object 请求可以将一个文件（Object）下载至本地。该操作需要对目标 Object 具有读权限或目标 Object 对所有人都开放了读权限（公有读）。

## 请求

### 请求语法

```http
GET /ObjectName Http/1.1
Host:<BucketName>-<AppID>.<Region>.myqcloud.com
Date: date
Authorization: authorization string(公有读无需此头部，若携带也无效)
Range: bytes=byte_range
```

### 请求参数

| 名称                           | 描述                               | 类型     | 必选   |
| ---------------------------- | -------------------------------- | ------ | ---- |
| response-content-type        | 设置返回头部中的 Content-Type 参数。        | String | 否    |
| response-content-language    | 设置返回头部中的 Content-Language 参数。    | String | 否    |
| response-expires             | 设置返回头部中的 Content-Expires 参数。     | String | 否    |
| response-cache-control       | 设置返回头部中的 Cache-Control 参数。       | String | 否    |
| response-content-disposition | 设置返回头部中的 Content-Disposition 参数。 | String | 否    |
| response-content-encoding    | 设置返回头部中的 Content-Encoding 参数。    | String | 否    |

### 请求头部

#### 推荐使用头部

| 名称                | 描述                                       | 类型     | 必选   |
| ----------------- | ---------------------------------------- | ------ | ---- |
| Range             | RFC 2616 中定义的指定文件下载范围，以字节（bytes）为单位。     | String | 否    |
| If-Modified-Since | 如果文件修改时间晚于指定时间，才返回文件内容。否则返回 304 (not modified)。 | String | 否    |

### 请求内容

无请求内容

## 返回值

### 返回头部

| 名称                  | 描述                                       | 类型     |
| ------------------- | ---------------------------------------- | ------ |
| x-cos-meta-*        | 用户自定义的元数据                                | String |
| x-cos-object-type   | 用来表示object是否可以被追加上传，枚举值：normal或者appendable | string |
| x-cos-storage-class | Object的存储级别，枚举值：Standard，Standard_IA，Nearline | String |


### 返回内容

文件内容

## 示例

### 请求

```HTTP
GET /123 HTTP/1.1
Host:zuhaotestnorth-1251668577.cn-north.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484212200;32557108200&q-key-time=1484212200;32557108200&q-header-list=host&q-url-param-list=&q-signature=11522aa3346819b7e5e841507d5b7f156f34e639
```

### 返回

```HTTP
HTTP/1.1 200 OK
Date: Thu, 12 Jan 2017 09:10:22 GMT
Content-Type: application/octet-stream
Content-Length: 16087
Connection: keep-alive
Accept-Ranges: bytes
Content-Disposition: attachment; filename*="UTF-8''123"
Content-Range: bytes 0-16086/16087
ETag: "9a4802d5c99dafe1c04da0a8e7e166bf"
Last-Modified: Wed, 11 Jan 2017 15:30:07 GMT
x-cos-object-type: normal
x-cos-request-id: NTg3NzQ3ZmVfYmRjMzVfMzE5N182NzczMQ==

[Object]
```

