## 功能描述
Put Object - Copy请求实现将一个文件从源路径复制到目标路径。建议文件大小1M到5G，超过5G的文件请使用分块上传Upload - Copy。在拷贝的过程中，文件元属性和ACL可以被修改。

用户可以通过该接口实现文件移动，文件重命名，修改文件属性和创建副本。

当请求未被执行，返回对应错误码；当请求进行中出错，返回200和对应错误信息。

（目前只支持华南园区）

## 请求

### 请求语法

```HTTP
PUT /destinationObject HTTP 1.1
Host:<Bucketname>-<UID>.<Region>.myqcloud.com
Date:date
Cache-Control:
Content-Disposition:
Content-Encoding:
Content-Length:
Content-Type:
Expect:
Expires:
Authorization: Auth
X-cos-copy-source:
x-cos-metadata-directive:
x-cos-copy-source-If-Modified-Since:
x-cos-copy-source-If-Unmodified-Since:
x-cos-copy-source-If-Match:
x-cos-copy-source-If-None-Match:
x-cos-storage-class:
```

### 请求参数

无特殊请求头部，其他头部请参见公共请求头部

### 请求头部

#### 必选头部
| 名称                | 描述                                | 类型     | 必选   |
| ----------------- | --------------------------------- | ------ | ---- |
| x-cos-copy-source | 源文件URL绝对路径，可以通过versionid子资源指定历史版本 | String | 是    |

#### 推荐使用头部

| 名称                                    | 描述                                       | 类型     | 必选   |
| ------------------------------------- | ---------------------------------------- | ------ | ---- |
| x-cos-metadata-directive              | 是否拷贝元数据，枚举值：Copy, Replaced，默认值Copy。假如标记为Copy，忽略Header中的用户元数据信息直接复制；假如标记为Replaced，按Header信息修改元数据。当目标路径和原路径一致，即用户试图修改元数据时，必须为Replaced | String | 否    |
| x-cos-copy-source-If-Modified-Since   | 当Object在指定时间后被修改，则执行操作，否则返回412。可与x-cos-copy-source-If-None-Match一起使用，与其他条件联合使用返回冲突。 | String | 否    |
| x-cos-copy-source-If-Unmodified-Since | 当Object在指定时间后未被修改，则执行操作，否则返回412。可与x-cos-copy-source-If-Match一起使用，与其他条件联合使用返回冲突。 | String | 否    |
| x-cos-copy-source-If-Match            | 当Object的Etag和给定一致时，则执行操作，否则返回412。可与x-cos-copy-source-If-Unmodified-Since一起使用，与其他条件联合使用返回冲突。 | String | 否    |
| x-cos-copy-source-If-None-Match       | 当Object的Etag和给定不一致时，则执行操作，否则返回412。可与x-cos-copy-source-If-Modified-Since一起使用，与其他条件联合使用返回冲突。 | String | 否    |
| x-cos-storage-class                   | 存储级别，枚举值：存储级别，枚举值：Standard, Standard_IA，Nearline；默认值：Standard | String | 否    |

#### 权限相关头部

| 名称                       | 描述                                       | 类型     | 必选   |
| ------------------------ | ---------------------------------------- | ------ | ---- |
| x-cos-acl                | 允许用户自定义文件权限。<br />有效值：private , public-read，默认私有。 | String | 否    |
| X-cos-grant-read         | 赋予被授权者读的权限<br />格式X-cos-grant-read: uin=" ",uin=" " | String | 否    |
| X-cos-grant-write        | 赋予被授权者写的权限<br />格式X-cos-grant-write: uin=" ",uin=" " | String | 否    |
| X-cos-grant-full-control | 赋予被授权者读写权限<br />格式X-cos-grant-full-control: uin=" ",uin=" " | String | 否    |
| x-cos-meta-*             | 其他自定义的文件头部                               | String | 否    |

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

| 名称               | 描述                                       | 类型     |
| ---------------- | ---------------------------------------- | ------ |
| CopyObjectResult | 返回复制结果信息                                 | String |
| ETag             | 返回文件的 SHA-1 算法校验值。ETag 的值可以用于检查 Object 的内容是否发生变化。 | String |
| LastModified     | 返回文件最后修改时间，GMT格式                         | String |
```XML
<CopyObjectResult>
  <ETag></ETag>
  <LastModified></LastModified>
</CopyObjectResult>
```
## 示例

### 请求
```http
PUT /coss3/destinationObject HTTP/1.1
Host:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
X-cos-copy-source:arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com/ObjectName
Authorization:q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn&q-sign-time=1487063832;32466647832&q-key-time=1487063832;32559959832&q-header-list=host&q-url-param-list=&q-signature=a1c35e63125977022c7d8a81a5c7918c9c403f68

```

### 返回
```http
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 198
Connection: keep-alive
Date: Tue Feb 14 17:22:01 2017
ETag: "72c1bc1feb83a71c229de411c947f110"
Server: tencent-cos
x-cos-request-id: NThhMmNjMzlfMmM4OGY3XzZjZGFfOGM1

```
