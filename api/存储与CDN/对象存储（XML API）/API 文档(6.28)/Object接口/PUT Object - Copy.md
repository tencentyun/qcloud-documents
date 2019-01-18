## 功能描述
PUT Object - Copy  请求实现将一个文件从源路径复制到目标路径。建议文件大小1M 到 5G，超过5G 的文件请使用分块上传 Upload - Copy。在拷贝的过程中，文件元属性和 acl 可以被修改。
用户可以通过该接口实现文件移动，文件重命名，修改文件属性和创建副本。

### 版本

默认情况下，在目标存储桶上启用版本控制，对象存储会为正在复制的对象生成唯一的版本 ID。此版本 ID 与源对象的版本 ID 不同。对象存储会在 x-cos-version-id 响应中的响应标头中返回复制对象的版本 ID。
如果您在目标存储桶没有启用版本控制或暂停版本控制，则对象存储生成的版本 ID 始终为 null。

>!在跨帐号复制的时候，需要先设置被复制文件的权限为公有读，或者对目标帐号赋权，同帐号则不需要。

## 请求
### 请求示例

```shell
PUT /<ObjectKey> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
x-cos-copy-source: <BucketName-APPID>.cos.<Region>.myqcloud.com/filepath
```

> Authorization: Auth String （详细请参阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节）。


### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情请参阅 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

#### 非公共头部

名称|描述|类型|必选
---|---|---|---
x-cos-copy-source|源文件 URL 路径，可以通过 versionid 子资源指定历史版本|string|是
x-cos-metadata-directive|是否拷贝源文件的元数据，枚举值：Copy, Replaced，默认值 Copy。假如标记为 Copy，则拷贝源文件的元数据；假如标记为 Replaced，则按本次请求的 Header 信息修改元数据。当目标路径和源路径一致，即用户试图修改元数据时，则标记必须为 Replaced|string|否
x-cos-copy-source-If-Modified-Since|当 Object 在指定时间后被修改，则执行操作，否则返回412。可与 x-cos-copy-source-If-None-Match 一起使用，与其他条件联合使用返回冲突|string|否
x-cos-copy-source-If-Unmodified-Since|当 Object 在指定时间后未被修改，则执行操作，否则返回412。可与 x-cos-copy-source-If-Match 一起使用，与其他条件联合使用返回冲突|string|否
x-cos-copy-source-If-Match|当 Object 的 Etag 和给定一致时，则执行操作，否则返回412。可与 x-cos-copy-source-If-Unmodified-Since 一起使用，与其他条件联合使用返回冲突|string|否
x-cos-copy-source-If-None-Match|当 Object 的 Etag 和给定不一致时，则执行操作，否则返回412。可与 x-cos-copy-source-If-Modified-Since 一起使用，与其他条件联合使用返回冲突|string|否
x-cos-storage-class|设置 Object 的存储级别，枚举值：STANDARD，STANDARD_IA。默认值：STANDARD|string|否
x-cos-acl|定义 Object 的 ACL 属性。有效值：private，public-read；默认值：private|string|否
x-cos-grant-read|赋予被授权者读的权限。格式：x-cos-grant-read: id="[OwnerUin]"|string|否
x-cos-grant-write|赋予被授权者写的权限。格式：x-cos-grant-write: id="[OwnerUin]"|string|否
x-cos-grant-full-control|赋予被授权者所有的权限。格式：x-cos-grant-full-control: id="[OwnerUin]"|string|否
x-cos-meta-\*|包括用户自定义头部后缀和用户自定义头部信息，将作为 Object 元数据返回，大小限制为2KB。<br>**注意：**用户自定义头部信息支持下划线，但用户自定义头部后缀不支持下划线|string|否

**服务端加密相关头部**

该请求操作指定腾讯云 COS 在数据存储时，应用数据加密的保护策略。腾讯云 COS 会帮助您在数据写入数据中心时自动加密，并在您取用该数据时自动解密。目前支持使用腾讯云 COS 主密钥对数据进行 AES-256 加密。如果您需要对数据启用服务端加密，则需传入以下头部：

| 名称         | 描述          | 类型     | 必选     |
| --------- | ---------- | ------ | ------ |
| x-cos-server-side-encryption | 指定将对象启用服务端加密的方式。<br/>使用 COS 主密钥加密填写：AES256 | String | 如需加密，是 |

### 请求体
该请求的请求体为空。

## 响应
### 响应头

#### 公共响应头

该响应包含公共响应头，了解公共响应头详情请参阅 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

| 名称         | 描述          | 类型     |
| --------- | ---------- | ------ |
|x-cos-version-id|目标存储桶中复制对象的版本。只有开启或开启后暂停的存储桶，才会响应此参数|String|
| x-cos-server-side-encryption | 如果通过 COS 管理的服务端加密来存储对象，响应将包含此头部和所使用的加密算法的值，AES256。 | String |

### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<CopyObjectResult>
  <ETag>String</ETag>
  <LastModified>String</LastModified>
</CopyObjectResult>
```

具体的数据内容如下：

| 名称               | 描述                                       | 类型     |
| ---------------- | ---------------------------------------- | ------ |
| CopyObjectResult | 返回复制结果信息                                 | String |
| ETag             | 返回文件的 MD5 算法校验值。ETag 的值可以用于检查 Object 的内容是否发生变化。 | String |
| LastModified     | 返回文件最后修改时间，GMT 格式                        | String |


## 实际案例

### 请求

```shell
PUT /exampleobject HTTP/1.1
Host: destinationbucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 04 Aug 2017 02:41:45 GMT
Connection: keep-alive Accept-Encoding: gzip, deflate Accept: */*
User-Agent: python-requests/2.12.4
Authorization: q-sign-algorithm=sha1&q-ak=AKID15IsskiBQKTZbAo6WhgcBqVls9SmuG00&q-sign-time=1480932292;1981012292&q-key-time=1480932292;1981012292&q-url-param-list=&q-header-list=host&q-signature=eacefe8e2a0dc8a18741d9a29707b1dfa5aa47cc
x-cos-copy-source: sourcebucket-1250000001.cos.ap-beijing.myqcloud.com/picture.jpg
Content-Length: 0
```

### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 133
Connection: keep-alive
Date: Fri, 04 Aug 2017 02:41:45 GMT
Server: tencent-cos
x-cos-request-id: NTk4M2RlZTlfZDRiMDM1MGFfYTA1ZV8xMzNlYw==

<CopyObjectResult>
    <ETag>"ba82b57cfdfda8bd17ad4e5879ebb4fe"</ETag>
    <LastModified>2017-08-04T02:41:45</LastModified>
</CopyObjectResult>
```


