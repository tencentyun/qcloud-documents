## 功能描述
Put Object 接口请求可以在 COS 的 Bucket 中将一个文件（Object）下载至本地。该操作需要请求者对 Bucket 有 WRITE 权限。
## 请求

语法示例：
```
PUT /ObjectName HTTP/1.1
Host: <BucketName>-<AppID>.<Region>.myqcloud.com
Date: GMT Date
Authorization: authorization string
```

> Authorization: Auth (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
```
PUT /<ObjectName> HTTP/1.1
```
#### 请求参数
**命令参数**
该 API 接口使用到的命令参数为 `<ObjectName> `。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。

#### 非公共头部
**必选头部**

该请求操作需要用到如下必选请求头：

|参数名称|描述|类型| 必选|
|:---|:-- |:---|:-- |
| Content-Length | RFC 2616 中定义的 HTTP 请求内容长度（字节）。|String| 是|

**推荐头部**
该请求操作推荐使用如下推荐请求头：

|参数名称|描述|类型| 必选|
|:---|:-- |:---|:-- |
| Cache-Control |RFC 2616 中定义的缓存策略，将作为 Object 元数据保存。|String| 否|
| Content-Disposition |RFC 2616 中定义的文件名称，将作为 Object 元数据保存。|String| 否|
| Content-Encoding|RFC 2616 中定义的编码格式，将作为 Object 元数据保存。|String| 否|
| Content-Type |RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据保存。|String| 否|
| Expect | 当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容。|String| 否|
| Expires |RFC 2616 中定义的过期时间，将作为 Object 元数据保存。|String| 否|
| x-cos-meta-`*`  | 允许用户自定义的头部信息，将作为 Object 元数据返回。大小限制2K。|String| 否|
| x-cos-storage-class  | 设置 Object 的存储级别，枚举值：STANDARD,STANDARD_IA，NEARLINE，默认值：STANDARD（目前只支持华南园区）|String| 否|

**权限相关头部**
该请求操作的实现可以用 Put 请求中的 x-cos-acl 头来设置 Object 访问权限。有三种访问权限：public-read-write，public-read 和 private。如果不设置，默认为 private 权限。也可以单独明确赋予用户读、写或读写权限。内容如下：

|名称|描述|类型|必选|
|:---|:-- |:--|:--|
| x-cos-acl | 设置 Object 访问权限。有效值：private，public-read-write，public-read；默认值：private | String|  否 |
| x-cos-grant-read | 赋予被授权者读的权限。格式：x-cos-grant-read: uin=" ",uin=" "；</br> 当需要给子账户授权时，uin="RootAcountID/SubaccountID"，当需要给根账户授权时，uin="RootAcountID" | String |  否 |
| x-cos-grant-write| 赋予被授权者写的权限。格式：x-cos-grant-write: uin=" ",uin=" "；</br>当需要给子账户授权时，uin="RootAcountID/SubaccountID"，当需要给根账户授权时，uin="RootAcountID" |String |  否 |
| x-cos-grant-full-control | 赋予被授权者读写权限。格式：x-cos-grant-full-control: uin=" ",uin=" "；</br>当需要给子账户授权时，uin="RootAcountID/SubaccountID"，当需要给根账户授权时，uin="RootAcountID" | String|  否 |


### 请求体
该请求的请求体为 Object 文件内容。

## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
**特有响应头**

|参数名称|描述|类型|
|:---|:-- |:-- |
| ETag| 返回文件的 MD5 算法校验值。ETag 的值可以用于检查 Object 在上传过程中是否有损坏。|String|


#### 响应体
该请求的响应体为空



## 实际案例

### 请求
```
PUT /ObjectName HTTP/1.1
Host:zuhaotestsgnoversion-1251668577.sg.myqcloud.com
Date: Wed, 28 Oct 2015 20:32:00 GMT
Authorization:q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484639384;32557535384&q-key-time=1484639384;32557535384&q-header-list=host&q-url-param-list=&q-signature=5c07b7c67d56497d9aacb1adc19963135b7d00dc
Content-Length: 64

[Object]
```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Wed, 28 Oct 2015 20:32:00 GMT
Etag: 020df6d63448ae38a1de7924a68ba1e2
x-cos-request-id: NTg3ZGNjYTlfNDUyMDRlXzUyOTlfMjRj

```
