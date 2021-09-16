## 功能描述

APPEND Object 接口请求可以将一个对象以分块追加的方式上传至指定存储桶中。对象首次使用 APPEND Object 接口上传时，该对象的属性自动为 appendable ，使用其他接口上传时则属性自动为 normal （如果该对象已存在则属性会被覆盖为 normal），可以使用 [GET Object](https://cloud.tencent.com/document/product/436/7753) 或 [HEAD Object](https://cloud.tencent.com/document/product/436/7745) 接口获取 x-cos-object-type 响应头来判断对象属性。对象属性为 appendable 时才能使用本接口追加上传。

追加上传的对象，每个分块大小默认最大为5GB，无最小限制，同时通过追加方式产生的对象大小不得超过5GB。如果 Position 的值和当前对象的长度不致，COS 将返回409错误。如果追加一个 normal 属性的文件，COS 将返回409 ObjectNotAppendable。

>! 
>- Appendable 的对象不可以被复制，不参与版本管理，不参与生命周期管理，不可跨地域复制。
>- 使用 APPEND 接口进行追加上传时，COS 不会校验请求携带的存储类型，仅会以当前对象的存储类型为准。
>- APPEND 接口不支持智能分层存储类型。

## 请求

#### 请求示例

```sh
POST /ObjectName?append&position=*position* HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Content-Length: size
Content-Type: ContentType
Date: GMT Date
Authorization: Auth String
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部

**必选头部**
该请求操作的实现使用如下必选头部：

| 名称           | 描述                                        | 类型   | 是否必选 |
| -------------- | ------------------------------------------- | ------ | ---- |
| Content-Length | RFC 2616 中定义的 HTTP 请求内容长度（字节） | String | 是   |

**推荐头部**
该请求操作的实现使用如下推荐请求头部信息：

| 节点名称（关键字）  | 描述                                                         | 类型   | 是否必选 |
| ------------------- | ------------------------------------------------------------ | ------ | ---- |
| Cache-Control       | RFC 2616 中定义的缓存策略，将作为 Object 元数据返回          | String | 否   |
| Content-Disposition | RFC 2616 中定义的文件名称，将作为 Object 元数据返回          | String | 否   |
| Content-Encoding    | RFC 2616 中定义的编码格式，将作为 Object 元数据返回          | String | 否   |
| Content-MD5         | RFC 1864中定义的请求体内容的16字节二进制 MD5 哈希值的 Base64 编码形式，用于完整性检查，验证请求体在传输过程中是否发生变化，最终的取值长度应为24个字符，请注意在编写代码时使用正确的方法和参数，例如`ZzD3iDJdrMAAb00lgLLeig==` | String | 否   |
| Content-Type        | RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据返回  | String | 否   |
| Expect              | 当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容 | String | 否   |
| Expires             | RFC 2616 中定义的过期时间，将作为 Object 元数据返回          | String | 否   |
| x-cos-meta- *       | 允许用户自定义的头部信息，将作为 Object 元数据返回，大小限制2K | String | 否   |

**权限相关头部**
该请求操作的实现可以用 POST 请求中的 x-cos-acl 头来设置文件访问权限。目前 Object 访问权限有三种：public-read-write，public-read 和 private。如果不设置，默认为 private 权限。也可以单独明确赋予用户读、写或读写权限。内容如下：

>?了解更多 ACL 请求可详细请参见 [PUT Bucket acl](https://cloud.tencent.com/document/product/436/7737) 文档。

| 名称                     | 描述                                                         | 类型   | 是否必选 |
| ------------------------ | ------------------------------------------------------------ | ------ | ---- |
| x-cos-acl                | 定义 Object 的 ACL 属性，有效值为 private，public-read-write，public-read<br>默认值为 private | String | 否   |
| x-cos-grant-read         | 赋予被授权者读的权限，格式：`x-cos-grant-read: id=" ",id=" "`<br><li>当需要给子账号授权时，`id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"`<br><li>当需要给主账号授权时，`id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"` | String | 否   |
| x-cos-grant-write        | 赋予被授权者写的权限，格式：`x-cos-grant-write: id=" ",id=" "` <br><li>当需要给子账号授权时，`id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"`<br><li>当需要给主账号授权时，`id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"` | String | 否   |
| x-cos-grant-full-control | 赋予被授权者读写权限，格式：`x-cos-grant-full-control: id=" ",id=" "`<br><li> 当需要给子账号授权时，`id="qcs::cam::uin/<OwnerUin>:uin/<SubUin>"`<br> <li>当需要给主账号授权时，`id="qcs::cam::uin/<OwnerUin>:uin/<OwnerUin>"` | String | 否   |

#### 请求参数

具体内容如下：

| 参数名称 | 描述                                                         | 类型    | 是否必选 |
| -------- | ------------------------------------------------------------ | ------- | ---- |
| position | 追加操作的起始点，单位为字节。首次追加则设置 Position=0，后续追加则设置 Position 为当前 Object 的 content-length | Int | 是   |

#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

#### 公共响应头

该响应使用公共响应头，了解公共请求头详情请参见  [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

该请求操作的响应头具体数据为：

| 节点名称（关键字）         | 描述                               | 类型   |
| -------------------------- | ---------------------------------- | ------ |
| x-cos-next-append-position | 下一次追加操作的起始点，单位：字节 | String |
| ETag                       | 文件的唯一标识                     | String |


#### 响应体

该响应体返回为空。

#### 错误分析

1. 如果对一个非 appendable 的文件进行 APPEND 操作，那么会返回409 Confilct，错误信息：
The operation is not valid for the current state of the object。
2. 如果请求中未携带 position 参数，会返回400 Bad Request，错误信息：InvalidArgument。
3. 如果请求中缺失 Content-Length 头部，会返回 411 Length Required，错误信息：
You must provide the Content-Length HTTP header。

获取更多关于 COS 的错误码的信息，或者产品所有的错误列表，请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```sh
POST /coss3/app?append&position=0 HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Tue, 16 Jan 2016 21:32:00 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3M****&q-sign-time=1484208848;32557104848&q-key-time=1484208848;32557104848&q-header-list=host&q-url-param-list=append;position&q-signature=855fe6b833fadf20570f7f650e2120e17ce8****
Content-Length: 4096

[Object]
```

#### 响应

```sh
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Tue, 16 Jan 2016 21:32:00 GMT
ETag: 1ce5b469b7d6600ecc2fd112e570917b
Server: tencent-cos
x-cos-content-sha1: 1ceaf73df40e531df3bfb26b4fb7cd95fb7bff1d
x-cos-next-append-position: 4096
x-cos-request-id: NTg3NzNhZGZfMmM4OGY3X2I2Zl8x****
```
