## 功能描述
Get Bucket Location接口获取Bucket所在地域信息，只有Bucket所有者有权限读取信息。

## 请求

### 请求语法

```HTTP
GET /?location HTTP 1.1
Host:<Bucketname>-<AppID>.<Region>.myqcloud.com
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

| 名称                 | 描述                                       | 类型     |
| ------------------ | ---------------------------------------- | ------ |
| LocationConstraint | Bucket所在区域，枚举值：china-east，china-south，china-north，china-west，singapore | String |


## 示例
### 请求
```xml
GET /?location HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484817522;32557713522&q-key-time=1484817522;32557713522&q-header-list=host&q-url-param-list=location&q-signature=ceb96fc929663dd4d2e6dc0aeb304cdde6761ed0

```
### 返回
```xml
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 92
Connection: keep-alive
Date: Thu Jan 19 17:18:49 2017
Server: tencent-cos
x-cos-request-id: NTg4MDg0NzlfNDYyMDRlXzM0OWFfZjFk

<LocationConstraint>singapore</LocationConstraint>
```

