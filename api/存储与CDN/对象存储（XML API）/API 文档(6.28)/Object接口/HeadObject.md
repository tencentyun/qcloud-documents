## 功能描述
HEAD Object 接口请求可以获取对应 Object 的 meta 信息数据，HEAD 的权限与 GET 的权限一致

---
### 版本

默认情况下，HEAD 操作从当前版本的对象中检索元数据。如要从不同版本检索元数据，请使用 versionId 子资源。

---

### 细节分析

1. HEAD Object 请求是不返回消息体的。
2. 这里的 If-Modified-Since 统一采用 GMT(RFC822) 时间格式，例如：Tue, 22 Oct 2017 01:35:21 GMT。
3. 如果 head 的文件不存在，则会返回 404 NOT FOUND。

## 请求

语法示例：
```
HEAD /<ObjectName> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String

```

> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求行
```
HEAD /<ObjectName> HTTP/1.1
```
该 API 接口接受 HEAD 请求。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

#### 非公共头部
**推荐头部**
该请求操作推荐请求头使用推荐头部，具体内容如下：

| 名称                | 描述                                       | 类型     | 必选   |
| :---------------- | :--------------------------------------- | :----- | :--- |
| If-Modified-Since | 当 Object 在指定时间后被修改，则返回对应 Object 的 meta 信息，否则返回 304 | String | 否    |

### 请求体
该请求的请求体为空。

## 响应

### 响应头
#### 公共响应头 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该请求操作的响应头具体数据为：

| 名称                  | 描述                                       | 类型     |
| :------------------ | :--------------------------------------- | :----- |
| x-cos-meta- *       | 用户自定义的 meta                              | String |
| x-cos-object-type   | 用来表示 Object 是否可以被追加上传，枚举值：normal 或者 appendable | String |
| x-cos-storage-class | Object 的存储级别，枚举值：STANDARD,STANDARD_IA | String |

**服务端加密相关响应**

如果在上传时指定使用了服务端加密，响应头部将会包含如下信息：

| 名称                           | 描述                                       | 类型     |
| ---------------------------- | ---------------------------------------- | ------ |
| x-cos-server-side-encryption | 指定将对象启用服务端加密的方式。<br/>使用 COS 主密钥加密：AES256 | String |

*注意：如果对象使用了启用了服务端加密，获取数据时腾讯云 COS 将会自动执行解密并返回解密后的数据。发送 GET/HEAD Object 请求时，无需带入 `x-cos-server-side-encryption` 头部，否则请求将返回 `400 BadRequest` 错误。*

### 响应体

该请求的响应体为空。

### 错误分析
以下描述此请求可能会发生的一些特殊的且常见的错误情况：

| 错误码                 | HTTP状态码         | 描述                                       |
| ------------------- | --------------- | ---------------------------------------- |
| SSEHeaderNotAllowed | 400 Bad Request | 如果头部携带 x-cos-server-side-encryption 的标头，就会返回该错误 |
获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

### 请求
```
HEAD /123 HTTP/1.1
Host: zuhaotestnorth-1251668577.cos.ap-beijing.myqcloud.com
Date: Thu, 12 Jan 2017 17:26:53 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484213210;32557109210&q-key-time=1484213210;32557109210&q-header-list=host&q-url-param-list=&q-signature=ac61b8eb61964e7e6b935e89de163a479a25c210

```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 16087
Connection: keep-alive
Date: Thu, 12 Jan 2017 17:26:53 GMT
ETag: "9a4802d5c99dafe1c04da0a8e7e166bf"
Last-Modified: Wed, 11 Jan 2017 07:30:07 GMT
Server: tencent-cos
x-cos-object-type: normal
x-cos-request-id: NTg3NzRiZGRfYmRjMzVfM2Y2OF81N2YzNA==
x-cos-storage-class: STANDARD

```
