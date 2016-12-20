## 功能描述
Upload Part请求实现在初始化以后的分块上传，支持的块的数量为1到10000，块的大小为1 MB 到5 GB。在每次请求Upload Part时候，需要携带partNumber和uploadID，partNumber为块的编号，支持乱序上传。

当传入uploadID和partNumber都相同的时候，后传入的块将覆盖之前传入的块。当uploadID不存在时会返回404错误，NoSuchUpload.

## 请求

### 请求语法

```http
PUT /ObjectName?partNumber=PartNumber&uploadId=UploadId HTTP 1.1
Host: <BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Content-Length: Size
Authorization: Auth
```

### 请求参数

无特殊请求参数

### 请求头部

#### 必选头部

| 名称             | 描述                             | 类型     | 必选   |
| -------------- | ------------------------------ | ------ | ---- |
| Content-Length | RFC 2616 中定义的 HTTP 请求内容长度（字节）。 | String | 是    |

#### 推荐使用头部

| 名称                 | 描述                                       | 类型     | 必选   |
| ------------------ | ---------------------------------------- | ------ | ---- |
| Expect             | 当使用 Expect: 100-continue 时，在收到服务端确认后，才会发送请求内容。 | String | 否    |
| x-cos-content-sha1 | RFC 3174 中定义的 160-bit 内容 SHA-1 算法校验值。    | String | 否    |

### 请求内容

文件内容

## 返回值

### 返回头部

无特殊返回头部，其他头部请参见公共返回头部

### 返回内容

无返回内容
