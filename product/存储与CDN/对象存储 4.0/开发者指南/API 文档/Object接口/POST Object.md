## 功能描述
POST Object 接口请求允许使用者用表单的形式将文件（Object）上传至指定 Bucket 中。该操作需要请求者对 Bucket 有 WRITE 权限。所有由 HTTP 头部携带的 API 参数，都使用表单字段请求。

### 版本

如果对存储桶启用版本控制，POST 操作将自动为要添加的对象生成唯一的版本 ID。对象存储使用 x-cos-version-id 响应头部在响应中返回此标识。
如果需要暂停存储桶的版本控制，则对象存储始终将其 null 用作存储在存储桶中的对象的版本 ID。

### 细节分析
1. 需要有 Bucket 的写权限；
2. 如果试图添加的 Object 的同名文件已经存在，那么新上传的文件，将覆盖原来的文件，成功时返回 200 OK。

## 请求

请求示例：
```
POST / HTTP/1.1
Headers
Form
```

> Signature（详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节）


### 请求头
#### 必选头部
该请求操作需要用到如下必选请求头：

|名称|描述|类型| 必选|
|:---|:-- |:---|:-- |
| Content-Length | RFC 2616 中定义的 HTTP 请求内容长度（字节）|String| 是|

### 表单字段
|名称|描述|类型| 必选|
|:---|:-- |:---|:-- |
| acl |文件的权限，不填默认继承，详见 [PUT Object acl](https://cloud.tencent.com/document/product/436/7748) |String| 否|
| Cache-Control, Content-Type, Content-Disposition, Content-Encoding, Expires |RFC 2616 中定义的头部，详见 [PUT Object](https://cloud.tencent.com/document/product/436/7749) |String| 否|
| file|文件内容，作为表单的最后一个字段 |String| 是|
| key |上传后的文件名，使用 **${filename}** 则会进行替换。例如a/b/${filename}，上传文件 a1.txt，那么最终的上传路径就是 a/b/a1.txt |String| 是|
| success_action_redirect | 若设置优先生效，返回 303 并提供 Location 头部，在 URL 尾部加上 bucket={bucket}&key={key}&etag={%22etag%22} 参数 |String| 否|
| success_action_status |可选 200，201，204 默认返回 204。若填写 success_action_redirect 则会略此设置。 |String| 否|
| x-cos-meta- * | 自定义的信息，将作为 Object 元数据返回。大小限制 2K |String| 否|
| x-cos-storage-class  | 设置 Object 的存储级别，枚举值：STANDARD，STANDARD_IA，默认值：STANDARD |String| 否|
| policy | Base64 编码。用于做请求检查，如果请求的内容和  Policy 指定的条件不符，返回 403 AccessDenied |String| 否|

#### Policy
##### 基本格式
```json
{ "expiration": "2007-12-01T12:00:00.000Z",
  "conditions": [
    {"acl": "public-read" },
    {"bucket": "johnsmith" },
    ["starts-with", "$key", "user/eric/"],
  ]
}
```

##### Expiration
设置该 POST Policy 的超时时间，使用 ISO8601 GMT 时间，例如 2017-12-01T12:00:00.000Z。

##### Conditions 规则
| 类型   | 描述                                       |
| ---- | ---------------------------------------- |
| 完全匹配 | 使用`{"key": "value"}`或`["eq", "$key", "value"]`方式表达 |
| 前缀匹配 | 使用 `["starts-with", "$key", "value"]`方式表达，value 可留空 |
| 范围匹配 | 仅用于`["content-length-range", int1, int2]`则文件字节数必须在 int1 和 int2 范围内|

##### Conditions 参数
所有参数均为非必选，不填可以不校验。

| 名称                      | 描述                                       | 匹配方式  |
| ----------------------- | ---------------------------------------- | ----- |
| acl                     | 文件 ACL 属性的许可范围，可不填                       | 完全、前缀 |
| bucket                  | 指定上传的 Bucket                             | 完全    |
| content-length-range    | 指定文件的上传大小范围                              | 范围    |
| 五标准头部                   | Cache-Control Content-Type Content-Disposition Content-Encoding Expires | 完全、前缀 |
| key                     | 对象的存储路径                                  | 完全、前缀 |
| success_action_redirect | 上传成功后返回的 URL                             | 完全、前缀 |
| success_action_status   | 上传成功后返回的状态                               | 完全    |
| x-cos-credential        | 格式   *<your-access-key-id>*/*<date>*/*<aws-region>*/*<aws-service>*/aws4_request | 完全    |
| x-cos-date              | ISO8601的 UTC 时间      | 完全    |
| x-cos-meta-*            | 用户自定义的头部                                 | 完全、前缀 |
| x-cos-*                 | 其他需要签署的 aws 头部                           | 完全    |

## 响应
### 响应头
#### 公共响应头
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
该请求操作的响应头具体数据为：

|名称|描述|类型|
|:---|:-- |:-- |
| ETag| 返回文件的 MD5 算法校验值。ETag 的值可以用于检查 Object 在上传过程中是否有损坏 |String|
| Location| 若指定了上传 success_action_redirect 则返回对应的值，若无指定则返回对象完整的路径|String|
|x-cos-version-id|目标存储桶中复制对象的版本。|String|

### 响应体
|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:--|
| PostResponse |无| 保存 POST Object 结果的容器 | Container |是|

Container 节点 PostResponse 的内容：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:--|
| Location | PostResponse | 对象的完整路径。 |  String |是|
| Bucket | PostResponse | 对象所在的存储桶。 |  String |是|
| Key | PostResponse | 对象 key 名 |  String |是|
| ETag | PostResponse | Etag 内容。 |  String |是|
### 错误分析
以下描述此请求可能会发生的一些特殊的且常见的错误情况：

| 错误码                  |   HTTP 状态码                                      |    描述       |
| ------------------- | --------------------------------------- | ------------------ |
| InvalidDigest        |400 Bad Request     | 如果用户上传文件时携带 Content-MD5 头部，COS 会校验 body 的 Md5 和用户携带的 MD5 是否一致，如果不一致将返回 InvalidDigest | 
| KeyTooLong           |400 Bad Request     | 上传文件时携带的以x-cos-meta开头的自定义头部，每个自定义头部的key和value加起来不能超过4k，否则返回 KeyTooLong 错误 | 
| MissingContentLength | 411 Length Required |如果上传文件时，没有添加 Content-Length 头部，会返回该错误码     | 
| NoSuchBucket         | 404 Not Found       |如果试图添加的 Object 所在的 Bucket 不存在，返回 404 Not Found 错误，错误码：NoSuchBucket | 
| EntityTooLarge       | 400 Bad Request     |如果添加的文件长度超过5G，会返回 EntityTooLarge，并返回错误信息`“Your proposed upload exceeds the maximum allowed object size”` | 
| InvalidURI           | 400 Bad Request     | 对象 key 长度限制为 850，如果超过 850 会返回 InvalidURI       |

获取更多关于 COS 的错误码的信息，或者产品所有的错误列表，请查看 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例
### 请求
```
POST / HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.12.4
Host: xxxx-123456.cos.ap-guangzhou.myqcloud.com
Content-Length: 1352
Content-Type: multipart/form-data; boundary=e07f2a7876ae4755ae18d300807ad879

--e07f2a7876ae4755ae18d300807ad879
Content-Disposition: form-data; name="key"

a/${filename}
--e07f2a7876ae4755ae18d300807ad879
Content-Disposition: form-data; name="success_action_status"

201
--e07f2a7876ae4755ae18d300807ad879
Content-Disposition: form-data; name="Acl"

public-read
--e07f2a7876ae4755ae18d300807ad879
Content-Disposition: form-data; name="x-cos-storage-class"

STANDARD
--e07f2a7876ae4755ae18d300807ad879
Content-Disposition: form-data; name="Signature"

q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR98JM&q-sign-time=1512983814;1512984814&q-key-time=1512983814;1512984814&q-url-param-list=&q-header-list=host&q-signature=2ffd2ae714e7445a8da000ec5d51771ff5056500
--e07f2a7876ae4755ae18d300807ad879
Content-Disposition: form-data; name="policy"

eyJjb25kaXRpb25zIjogW3siYnVja2V0IjogImtpdG1hbnMzdGVzdDEifSwgWyJjb250ZW50LWxlbmd0aC1yYW5nZSIsIDAsIDEwMDAwMDAwXSwgWyJzdGFydHMtd2l0aCIsICJ4LWNvcy1tZXRhLWJiIiwgIjEyIl1dLCAiZXhwaXJhdGlvbiI6ICIyMDQ3LTEyLTAxVDEyOjAwOjAwLjAwMFoifQ==
--e07f2a7876ae4755ae18d300807ad879
Content-Disposition: form-data; name="x-Cos-meta-bb"

124
--e07f2a7876ae4755ae18d300807ad879
Content-Disposition: form-data; name="key1"

1
--e07f2a7876ae4755ae18d300807ad879
Content-Disposition: form-data; name="file"; filename="empty:a"


--e07f2a7876ae4755ae18d300807ad879--
```

### 响应
```
HTTP/1.1 201
Content-Type: application/xml
Content-Length: 232
Connection: keep-alive
Date: Mon, 11 Dec 2017 09:16:56 GMT
ETag: "d41d8cd98f00b204e9800998ecf8427e"
Location: http://xxxx-123456.cos.ap-guangzhou.myqcloud.com/a/empty:a
Server: tencent-cos
x-cos-request-id: NWEyZTRkMDZfMjQ4OGY3MGFfNTE4Yl81

<PostResponse>
        <Location>http://xxxx-123456.cos.ap-guangzhou.myqcloud.com/a/empty:a</Location>
        <Bucket>xxxx-123456</Bucket>
        <Key>a/empty:a</Key>
        <ETag>d41d8cd98f00b204e9800998ecf8427e</ETag>
</PostResponse>

```
