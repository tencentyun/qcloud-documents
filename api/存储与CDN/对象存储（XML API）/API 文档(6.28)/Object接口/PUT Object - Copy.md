## 功能描述
PUT Object - Copy 请求创建一个已存在 COS 的对象的副本，即将一个对象从源路径（对象键）复制到目标路径（对象键）。建议对象大小1M到5G，超过5G的对象请使用分块上传 [Upload Part - Copy](https://cloud.tencent.com/document/product/436/8287)。在复制的过程中，对象元数据和访问控制列表（ACL）可以被修改。

用户可以通过此接口实现对象移动、重命名、修改对象元数据和创建副本。

>! 
>- 在跨账号复制的时候，需要先设置被复制文件的权限为公有读，或者对目标账号赋权，同账号则不需要。
>- 当 COS 收到复制请求或 COS 正在复制对象时可能会返回错误。如果在复制操作开始之前发生错误，则会收到标准的错误返回。如果在复制操作执行期间发生错误，则依然会返回 HTTP 200 OK，并将错误作为响应体返回。这意味着 HTTP 200 OK 响应既可以包含成功也可以包含错误，在使用此接口时应当进一步根据响应体的内容来判断复制请求的成功与失败并正确的处理结果。

#### 版本

默认情况下，在目标存储桶上启用版本控制，对象存储会为正在复制的对象生成唯一的版本 ID。此版本 ID 与源对象的版本 ID 不同。对象存储会在 x-cos-version-id 响应中的响应标头中返回复制对象的版本 ID。
如果您在目标存储桶没有启用版本控制或暂停版本控制，则对象存储生成的版本 ID 始终为 null。

## 请求
#### 请求示例

```shell
PUT /<ObjectKey> HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
x-cos-copy-source: <BucketName-APPID>.cos.<Region>.myqcloud.com/filepath
```

>?Authorization: Auth String （详细请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


#### 请求头

#### 公共头部

该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 非公共头部

<table>
   <tr>
      <th>名称</th>
      <th>描述</th>
      <th>类型</th>
      <th>必选</th>
   </tr>
   <tr>
      <td nowrap="nowrap">x-cos-copy-source</td>
      <td>源文件 URL 路径，可以通过 versionid 子资源指定历史版本</td>
      <td>string</td>
      <td>是</td>
   </tr>
   <tr>
      <td nowrap="nowrap">x-cos-metadata-directive</td>
      <td>是否拷贝源文件的元数据，枚举值：Copy, Replaced，默认值 Copy。假如标记为 Copy，则拷贝源文件的元数据；假如标记为 Replaced，则按本次请求的 Header 信息修改元数据。当目标路径和源路径一致，即用户试图修改元数据时，则标记必须为 Replaced</td>
      <td>string</td>
      <td>否</td>
   </tr>
   <tr>
      <td nowrap="nowrap">x-cos-copy-source-If-Modified-Since</td>
      <td>当 Object 在指定时间后被修改，则执行操作，否则返回412。可与 x-cos-copy-source-If-None-Match 一起使用，与其他条件联合使用返回冲突</td>
      <td>string</td>
      <td>否</td>
   </tr>
   <tr>
      <td nowrap="nowrap">x-cos-copy-source-If-Unmodified-Since</td>
      <td>当 Object 在指定时间后未被修改，则执行操作，否则返回412。可与 x-cos-copy-source-If-Match 一起使用，与其他条件联合使用返回冲突</td>
      <td>string</td>
      <td>否</td>
   </tr>
   <tr>
      <td>x-cos-copy-source-If-Match</td>
      <td>当 Object 的 Etag 和给定一致时，则执行操作，否则返回412。可与 x-cos-copy-source-If-Unmodified-Since 一起使用，与其他条件联合使用返回冲突</td>
      <td>string</td>
      <td>否</td>
   </tr>
   <tr>
      <td>x-cos-copy-source-If-None-Match</td>
      <td>当 Object 的 Etag 和给定不一致时，则执行操作，否则返回412。可与 x-cos-copy-source-If-Modified-Since 一起使用，与其他条件联合使用返回冲突</td>
      <td>string</td>
      <td>否</td>
   </tr>
   <tr>
      <td>x-cos-storage-class</td>
      <td>设置 Object 的存储级别，枚举值：STANDARD，STANDARD_IA。默认值：STANDARD</td>
      <td>string</td>
      <td>否</td>
   </tr>
   <tr>
      <td>x-cos-acl</td>
      <td>定义 Object 的 ACL 属性。有效值：private，public-read；默认值：private</td>
      <td>string</td>
      <td>否</td>
   </tr>
   <tr>
      <td>x-cos-grant-read</td>
      <td>赋予被授权者读的权限。格式：x-cos-grant-read: id="[OwnerUin]"</td>
      <td>string</td>
      <td>否</td>
   </tr>
   <tr>
      <td>x-cos-grant-write</td>
      <td>赋予被授权者写的权限。格式：x-cos-grant-write: id="[OwnerUin]"</td>
      <td>string</td>
      <td>否</td>
   </tr>
   <tr>
      <td>x-cos-grant-full-control</td>
      <td>赋予被授权者所有的权限。格式：x-cos-grant-full-control: id="[OwnerUin]"</td>
      <td>string</td>
      <td>否</td>
   </tr>
   <tr>
      <td>x-cos-meta-*</td>
      <td>包括用户自定义头部后缀和用户自定义头部信息，将作为 Object 元数据返回，大小限制为2KB。<b><br>注意：用户自定义头部信息支持下划线，但用户自定义头部后缀不支持下划线</br></b></td>
      <td>string</td>
      <td>否</td>
   </tr>
</table>

**服务端加密相关头部**

该请求操作指定腾讯云 COS 在数据存储时，应用数据加密的保护策略。腾讯云 COS 会帮助您在数据写入数据中心时自动加密，并在您取用该数据时自动解密。目前支持使用腾讯云 COS 主密钥对数据进行 AES-256 加密。如果您需要对数据启用服务端加密，则需传入以下头部：

| 名称         | 描述          | 类型     | 必选     |
| --------- | ---------- | ------ | ------ |
| x-cos-server-side-encryption | 指定将对象启用服务端加密的方式。<br/>使用 COS 主密钥加密填写：AES256 | String | 如需加密，是 |

#### 请求体
该请求的请求体为空。

## 响应
#### 响应头

#### 公共响应头

该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

<table>
   <tr>
      <th>名称</th>
      <th>描述</th>
      <th>类型</th>
   </tr>
   <tr>
      <td>x-cos-version-id</td>
      <td>目标存储桶中复制对象的版本，只有开启或开启后暂停的存储桶，才会响应此参数</td>
      <td>String</td>
   </tr>
   <tr>
      <td nowrap="nowrap">x-cos-server-side-encryption</td>
      <td>如果通过 COS 管理的服务端加密来存储对象，响应将包含此头部和所使用的加密算法的值，AES256</td>
      <td>String</td>
   </tr>
</table>


#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<CopyObjectResult>
    <ETag>"ba82b57cfdfda8bd17ad4e5879ebb4fe"</ETag>
    <LastModified>2017-08-04T02:41:45</LastModified>
</CopyObjectResult>
```

具体的数据内容如下：

| 名称               | 描述                                       | 类型     |
| ---------------- | ---------------------------------------- | ------ |
| CopyObjectResult | 返回复制结果信息                                 | String |
| ETag             | 返回文件的 MD5 算法校验值。ETag 的值可以用于检查 Object 的内容是否发生变化 | String |
| LastModified     | 返回文件最后修改时间，GMT 格式                        | String |


## 实际案例

#### 请求

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

#### 响应

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


