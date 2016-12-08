## 功能描述
Initiate Multipart请求实现初始化分片上传，成功执行此请求以后会返回Upload ID用于后续的Upload Part请求。

## 请求

### 请求语法

```http
POST /Object?uploads HTTP 1.1
Host: <BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Authorization: Auth
```

### 请求参数

无特殊请求参数

### 请求头部

#### 推荐使用头部

| 名称   | 描述   | 类型   | 必选   |
| ---- | ---- | ---- | ---- |
| Cache-Control       | RFC 2616 中定义的缓存策略，将作为 Object 元数据保存。      | String | 否    |
| Content-Disposition | RFC 2616 中定义的文件名称，将作为 Object 元数据保存。      | String | 否    |
| Content-Encoding    | RFC 2616 中定义的编码格式，将作为 Object 元数据保存。      | String | 否    |
| Content-Type        | RFC 2616 中定义的内容类型（MIME），将作为 Object 元数据保存。 | String | 否    |
| Expires             | RFC 2616 中定义的过期时间，将作为 Object 元数据保存。      | String | 否    |
| x-cos-meta-              | 允许用户自定义的头部信息，将作为 Object 元数据返回。           | String | 否    |

#### 权限相关头部

| 名称   | 描述   | 类型   | 必选   |
| ---- | ---- | ---- | ---- |
| x-cos-acl                | 允许用户自定义文件权限。<br />有效值：private \| public-read | String | 否    |
| X-cos-grant-read         | 赋予被授权者读的权限<br />格式X-cos-grant-read: uin=" ",uin=" " | String | 否    |
| X-cos-grant-write        | 赋予被授权者写的权限<br />格式X-cos-grant-write: uin=" ",uin=" " | String | 否    |
| X-cos-grant-full-control | 赋予被授权者读写权限<br />格式X-cos-grant-full-control: uin=" ",uin=" " | String | 否    |

### 请求内容

无请求内容

## 返回值

### 返回头部

无特殊返回Header

### 返回内容

| 名称                            | 描述            | 类型        |
| ----------------------------- | ------------- | --------- |
| InitiateMultipartUploadResult | 说明所有返回信息      | Contianer |
| Bucket                        | 分片上传的目标Bucket | String    |
| Key                           | Object的名称     | String    |
| UploadID                      | 在后续上传中使用的ID   | String    |

```xml
<InitiateMultipartUploadResult>
  <Bucket></Bucket>
  <Key></Key>
  <Upload></Upload>
</InitiateMultipartUploadResult>
```
