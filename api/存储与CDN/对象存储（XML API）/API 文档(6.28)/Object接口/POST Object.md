## 功能描述
POST Object 接口请求允许使用者用表单的形式将文件（Object）上传至指定 Bucket 中。该操作需要请求者对 Bucket 有 WRITE 权限。所有由 HTTP 头部携带的 API 参数，都使用表单字段请求。

#### 版本

如果对存储桶启用版本控制，POST 操作将自动为要添加的对象生成唯一的版本 ID。对象存储使用 x-cos-version-id 响应头部在响应中返回此标识。
如果需要暂停存储桶的版本控制，则对象存储始终将其 null 用作存储在存储桶中的对象的版本 ID。

#### 细节分析
1. 需要有 Bucket 的写权限。
2. 如果试图添加的 Object 的同名文件已经存在，那么新上传的文件，将覆盖原来的文件，并按照上传成功正常返回。

## 请求
#### 请求示例

```shell
POST / HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Content-Length: length
Headers
Form
```

#### 请求头

##### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情，请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

##### 非公共头部
该请求操作需要用到如下必选请求头：

|名称|描述|类型| 必选|
|:---|:-- |:---|:-- |
| Content-Length | RFC 2616中定义的 HTTP 请求内容长度（字节）|String| 是|

#### 表单字段

<table>
   <tr>
      <th>名称</td>
      <th>描述</td>
      <th>类型</td>
      <th>必选</td>
   </tr>
   <tr>
      <td>acl</td>
      <td>定义 Object 的 ACL 属性，有效值：private，public-read，default，默认值：default（继承 Bucket 权限）。注意：当前访问策略条目限制为1000条，如果您不需要进行 Object ACL 控制，请填 default 或者此项不进行设置，默认继承 Bucket 权限</td>
      <td>String</td>
      <td>否</td>
   </tr>
   <tr>
      <td>Cache-Control，Content-Type，Content-Disposition，Content-Encoding， Expires&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
      <td>RFC 2616 中定义的头部，请参见 <a href="https://cloud.tencent.com/document/product/436/7749">PUT Object</a> 文档</td>
      <td>String</td>
      <td>否</td>
   </tr>
   <tr>
      <td>file</td>
      <td>文件内容，作为表单的最后一个字段</td>
      <td>String</td>
      <td>是</td>
   </tr>
   <tr>
      <td>key</td>
      <td>上传后的文件名，使用<code>${filename}</code>则会进行替换，例如<code>a/b/${filename}</code>，上传文件 photo.jpg，那么最终的上传路径就是<code>a/b/photo.jpg</code></td>
      <td>String</td>
      <td>是</td>
   </tr>
   <tr>
      <td>success_action_redirect</td>
      <td>若设置优先生效，返回303，并提供 Location 头部，在 URL 尾部加上<code>bucket={bucket}&key={key}&etag={%22etag%22}</code>参数</td>
      <td>String</td>
      <td>否</td>
   </tr>
   <tr>
      <td>success_action_status</td>
      <td>可选200，201，204，默认返回204。若填写 success_action_redirect 则会略此设置</td>
      <td>String</td>
      <td>否</td>
   </tr>
   <tr>
      <td>x-cos-meta-*</td>
      <td>包括用户自定义头部后缀和用户自定义头部信息，将作为 Object 元数据返回，大小限制为2KB<br>注意：用户自定义头部信息支持下划线，但用户自定义头部后缀不支持下划线</td>
      <td>String</td>
      <td>否</td>
   </tr>
   <tr>
      <td>x-cos-storage-class</td>
      <td>设置 Object 的存储级别，枚举值：STANDARD、STANDARD_IA 和 ARCHIVE，默认值：STANDARD</td>
      <td>String</td>
      <td>否</td>
   </tr>
   <tr>
      <td>policy</td>
      <td>Base64 编码。用于做请求检查，如果请求的内容和 Policy 指定的条件不符，返回403 AccessDenied</td>
      <td>String</td>
      <td>否</td>
   </tr>
   <tr>
      <td>x-cos-server-side-encryption</td>
      <td>指定将对象启用服务端加密的方式。使用 COS 主密钥加密时，填写 AES256</td>
      <td>String</td>
      <td nowrap="nowrap">如需加密，是</td>
   </tr>
</table>

#### 签名保护

当发起一个表单上传 HTTP POST 请求需要签名保护时，表单需要包含以下的内容结构 form-data 的内容：

| 表单字段         | 描述                                                         |
| ---------------- | ----------------------------------------- |
| policy           | 经过 Base64 加密的策略内容，策略内容将用于对请求内容的检查。如果请求内容与策略指定条件不符，则请求将被拒绝 |
| q-sign-algorithm | 用于计算签名的算法，腾讯云 COS 目前支持 SHA1，此处填写小写 sha1 |
| q-ak             | 用户在腾讯云的账户密钥 ID，即 SecretId                     |
| q-key-time      | 用于请求签名的密钥有效起止时间，通过 Unix 时间戳描述起始和结束时间，以秒为单位<br>格式为 `[start-seconds];[end-seconds]`，例如`1480932292;1481012298` |
| q-signature      | 使用上述元素计算的请求签名，COS 将会使用表单元素与签名内容做校验，若签名与所签内容不一致，则请求将被拒绝 |

#### 签名计算

签名 q-signature 的计算分为三个步骤：

1. 使用密钥内容对 q-key-time 的时间加密计算值 SignKey。
2. 创建一个 POST 请求 policy 并将内容进行 sha1 加密，得到 StringToSign。
3. 使用 SignKey 对 StringToSign 进行加密，生成签名 Signature。

#### Policy
以下是一个完整的 policy 示例：

```shell
{ "expiration": "2007-12-01T12:00:00.000Z",
  "conditions": [
    {"acl": "public-read" },
    {"bucket": "examplebucket-1250000000" },
    ["starts-with", "$key", "user/eric/"],
    {"q-sign-algorithm": "sha1" },
    {"q-ak": "AKIDQjz3ltompVjBni5LitkWHFlFpwkn9U5q" },
    {"q-sign-time": "1480932292;1481012298" }
  ]
}
```

**Expiration**
设置该 POST Policy 的超时时间，使用 ISO8601 GMT 时间，例如 2017-12-01T12:00:00.000Z。

**Conditions 规则**

| 类型   | 描述                                       |
| ---- | ---------------------------------------- |
| 完全匹配 | 使用`{"key": "value"}`或`["eq", "$key", "value"]`方式表达 |
| 前缀匹配 | 使用`["starts-with", "$key", "value"]`方式表达，value 可留空 |
| 范围匹配 | 仅用于`["content-length-range", int1, int2]`则文件字节数必须在 int1 和 int2 范围内|

**Conditions 参数**
所有参数均为非必选，不填可以不校验。

| 名称             | 描述             | 匹配方式  |
| --------------- | ---------------------- | ----- |
| acl                     | 文件 ACL 属性的许可范围，可不填                       | 完全、前缀 |
| bucket                  | 指定上传的 Bucket                             | 完全    |
| content-length-range    | 指定文件的上传大小范围                              | 范围    |
| key                     | 对象的存储路径                                  | 完全、前缀 |
| success_action_redirect | 上传成功后返回的 URL                             | 完全、前缀 |
| success_action_status   | 上传成功后返回的状态                               | 完全    |
| x-cos-meta-\*            | 包括用户自定义头部后缀和用户自定义头部信息，将作为 Object 元数据返回，大小限制为 2KB<br>注意：用户自定义头部信息支持下划线，但用户自定义头部后缀不支持下划线  | 完全、前缀 |
| x-cos-\*      | 其他需要签署的 COS 头部            | 完全    |


## 响应
#### 响应头
#### 公共响应头
该响应使用公共响应头，了解公共响应头详情，请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头
该请求可能会返回如下响应头部：

|名称|描述|类型|
|:---|:-- |:-- |
|x-cos-version-id|目标存储桶中复制对象的版本。当开启或开启后暂停的存储桶，才会响应此头部|String|
|x-cos-server-side-encryption|如果通过 COS 管理的服务端加密来存储对象，响应将包含此头部和所使用的加密算法的值：AES256|string|


#### 响应参数
|名称|描述|类型|
|:---|:-- |:-- |
| ETag| 返回文件的 MD5 算法校验值，ETag 的值可以用于检查 Object 在上传过程中是否有损坏|String|
| Location| 若指定了上传 success_action_redirect 则返回对应的值，若无指定则返回对象完整的路径|String|


#### 响应体
该响应体返回为 application/xml 数据，包含完整节点数据的内容展示如下：

```shell
<PostResponse>
        <Location>http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/photo.jpg</Location>
        <Bucket>examplebucket-1250000000</Bucket>
        <Key>photo.jpg</Key>
        <ETag>d41d8cd98f00b204e9800998ecf8427e</ETag>
</PostResponse>
```

具体的数据描述如下：

| 节点名称（关键字） | 父节点 | 描述                        | 类型      |
| :----------------- | :----- | :-------------------------- | :-------- |
| PostResponse       | 无     | 保存 POST Object 结果的容器 | Container |


Container 节点 PostResponse 的内容：

| 节点名称（关键字） | 父节点       | 描述             | 类型   |
| :----------------- | :----------- | :--------------- | :----- |
| Location           | PostResponse | 对象的完整路径   | String |
| Bucket             | PostResponse | 对象所在的存储桶 | String |
| Key                | PostResponse | 对象 key 名      | String |
| ETag               | PostResponse | Etag 内容        | String |


#### 错误码
以下描述此请求可能会发生的一些特殊的且常见的错误情况。关于 COS 更多的错误码信息，请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

| 错误码                  |   HTTP 状态码                                      |    描述       |
| ------------------- | --------------------------------------- | ------------------ |
| InvalidDigest        |400 Bad Request     | 如果用户上传文件时携带 Content-MD5 头部，COS 会校验 body 的 MD5 和用户携带的 MD5 是否一致，如果不一致将返回 InvalidDigest |
| KeyTooLong           |400 Bad Request     | 上传文件时携带的以 x-cos-meta 开头的自定义头部，每个自定义头部的 key 和 value 加起来不能超过4k，否则返回 KeyTooLong 错误 |
| MissingContentLength | 411 Length Required |如果上传文件时，没有添加 Content-Length 头部，会返回该错误码     |
| NoSuchBucket         | 404 Not Found       |如果试图添加的 Object 所在的 Bucket 不存在，返回404 Not Found 错误，错误码：NoSuchBucket |
| EntityTooLarge       | 400 Bad Request     |如果添加的文件长度超过5G，会返回 EntityTooLarge，并返回错误信息`“Your proposed upload exceeds the maximum allowed object size”` |
| InvalidURI           | 400 Bad Request     | 对象 key 长度限制为850，如果超过850将返回 InvalidURI      |


## 实际案例
#### 请求

```
POST / HTTP/1.1
Connection: keep-alive
Accept-Encoding: gzip, deflate
Accept: */*
User-Agent: python-requests/2.12.4
Host: examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com
Content-Length: 1352
Content-Type: multipart/form-data; boundary=e07f2a7876ae4755ae18d300807ad879

--e07f2a7876ae4755ae18d300807ad879
Content-Disposition: form-data; name="key"

photo.jpg
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

#### 响应

```shell
HTTP/1.1 204
Content-Type: application/xml
Content-Length: 232
Connection: keep-alive
Date: Mon, 11 Dec 2017 09:16:56 GMT
ETag: "d41d8cd98f00b204e9800998ecf8427e"
Location: http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/photo.jpg
Server: tencent-cos
x-cos-request-id: NWEyZTRkMDZfMjQ4OGY3MGFfNTE4Yl81
```
