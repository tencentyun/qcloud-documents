## 功能描述

Head Object请求可以取回对应Object的元数据，Head的权限与Get的权限一致

## 请求

### 请求语法

```Http
HEAD /ObjectName HTTP/1.1
Host:<BucketName>-<AppID>.<Region>.myqcloud.com
Date: date
Authorization: auth
```

### 请求参数

无特殊请求参数

### 请求头部

#### 推荐使用头部

| 名称                | 描述                                      | 类型     | 必选   |
| ----------------- | --------------------------------------- | ------ | ---- |
| If-Modified-Since | 当Object在指定时间后被修改，则返回对应Object元信息，否则返回304 | String | 否    |

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

无返回内容

## 示例

### 请求

```HTTP
HEAD /123 HTTP/1.1
Host:zuhaotestnorth-1251668577.cn-north.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213210;32557109210&q-key-time=1484213210;32557109210&q-header-list=host&q-url-param-list=&q-signature=ac61b8eb61964e7e6b935e89de163a479a25c210
```

### 返回

```HTTP
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 16087
Connection: keep-alive
Date: Thu Jan 12 17:26:53 2017
ETag: "9a4802d5c99dafe1c04da0a8e7e166bf"
Last-Modified: Wed, 11 Jan 2017 07:30:07 GMT
Server: tencent-cos
x-cos-object-type: normal
x-cos-request-id: NTg3NzRiZGRfYmRjMzVfM2Y2OF81N2YzNA==
```

