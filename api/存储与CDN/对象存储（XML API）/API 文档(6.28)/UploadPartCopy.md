## 功能描述
Upload Part - Copy  请求实现将一个文件的分块内容从源路径复制到目标路径。通过指定 x-cos-copy-source 来指定源文件，x-cos-copy-source-range 指定字节范围。允许分块的大小为 5 MB - 5 GB。

>**注意：**
>如果目标文件和源文件不属于同一个园区，且目标文件分块会超过 5 GB, 那么需要使用分块上传或者分块拷贝的接口来复制文件。
>使用上传分块文件，必须先初始化分块上传。在初始化分块上传的响应中，会返回一个唯一的描述符（upload ID），您需要在分块上传请求中携带此 ID。

## 请求

语法示例：
```
PUT /destinationObject?partNumber=PartNumber&uploadId=UploadId  HTTP/1.1
Host: <Bucketname-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
x-cos-copy-source: <Bucketname>-<APPID>.cos.<Region>.myqcloud.com/filepath
x-cos-copy-source-range: bytes=first-last
x-cos-copy-source-if-match: etag
x-cos-copy-source-if-none-match : etag
x-cos-copy-source-if-unmodified-since: time_stamp
x-cos-copy-source-if-modified-since: time_stamp
```

> Authorization： Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求行

```
PUT /destinationObject?partNumber=PartNumber&uploadId=UploadId  HTTP/1.1
```
该 API 接口接受 PUT 请求。<style  rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

#### 非公共头部

**必选头部**
该请求操作的实现使用如下必选头部：

| 名称                | 描述                                  | 类型     | 必选   |
| ----------------- | ----------------------------------- | ------ | ---- |
| x-cos-copy-source | 源文件 URL 路径，可以通过 versionid 子资源指定历史版本 | String | 是    |


**推荐头部**
该请求操作的实现使用如下推荐请求头部信息：

| 名称                                    | 描述                                       | 类型      | 必选   |
| ------------------------------------- | ---------------------------------------- | ------- | ---- |
| x-cos-copy-source-range               | 源文件的字节范围，范围值必须使用 bytes=first-last 格式，first 和 last 都是基于 0 开始的偏移量。<br>例如 bytes=0-9 表示你希望拷贝源文件的开头10个字节的数据 ， 如果不指定，则表示拷贝整个文件。 | Integer | 是    |
| x-cos-copy-source-If-Modified-Since   | 当 Object 在指定时间后被修改，则执行操作，否则返回 412。<br>可与 x-cos-copy-source-If-None-Match 一起使用，与其他条件联合使用返回冲突。 | String  | 否    |
| x-cos-copy-source-If-Unmodified-Since | 当 Object 在指定时间后未被修改，则执行操作，否则返回 412。<br>可与 x-cos-copy-source-If-Match 一起使用，与其他条件联合使用返回冲突。 | String  | 否    |
| x-cos-copy-source-If-Match            | 当 Object 的 Etag 和给定一致时，则执行操作，否则返回 412。<br>可与x-cos-copy-source-If-Unmodified-Since 一起使用，与其他条件联合使用返回冲突。 | String  | 否    |
| x-cos-copy-source-If-None-Match       | 当 Object 的 Etag 和给定不一致时，则执行操作，否则返回 412。<br>可与 x-cos-copy-source-If-Modified-Since 一起使用，与其他条件联合使用返回冲突。 | String  | 否    |

### 请求体
该请求的请求体为空。

## 响应

### 响应头
#### 公共响应头 
该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头
**服务端加密相关响应**

如果在上传时指定使用了服务端加密，响应头部将会包含如下信息：

| 名称                           | 描述                                       | 类型     |
| ---------------------------- | ---------------------------------------- | ------ |
| x-cos-server-side-encryption | 指定将对象启用服务端加密的方式。<br/>使用 COS 主密钥加密：AES256 | String |

### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：
```
<CopyPartResult>
  <ETag></ETag>
  <LastModified></LastModified>
</CopyPartResult>
```
具体的数据内容如下：

| 名称             | 描述                                       | 类型     |
| -------------- | ---------------------------------------- | ------ |
| CopyPartResult | 返回复制结果信息                                 | String |
| ETag           | 返回文件的MD5算法校验值。ETag 的值可以用于检查 Object 的内容是否发生变化。 | String |
| LastModified   | 返回文件最后修改时间，GMT 格式                        | String |


## 实际案例
### 请求
```
PUT /jimmy/test.file2?partNumber=1&uploadId=1505706248ca8373f8a5cd52cb129f4bcf85e11dc8833df34f4f5bcc456c99c42cd1ffa2f9 HTTP/1.1
> User-Agent: curl/7.19.7 (x86_64-redhat-linux-gnu) libcurl/7.19.7 NSS/3.13.1.0 zlib/1.2.3 libidn/1.18 libssh2/1.2.2
> Accept: */*
> x-cos-copy-source:jimmyyantest-1251668577.cos.ap-shanghai.myqcloud.com/test.file1
> x-cos-copy-source-range: bytes=10-100
> Host: jimmyyantest-1251668577.cos.ap-shanghai.myqcloud.com
> Authorization:q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3MqQCn&q-sign-time=1507530223;1508530223&q-key-time=1507530223;1508530223&q-header-list=&q-url-param-list=&q-signature=d02640c0821c49293e5c289fa07290e6b2f05cb2
```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 133 
Connection: keep-alive 
Date: Mon, 04 Sep 2017 04:45:45 GMT
Server: tencent-cos
x-cos-request-id: NTlkYjFjYWJfMjQ4OGY3MGFfNGIzZV9k

<CopyPartResult>
<ETag>"ba82b57cfdfda8bd17ad4e5879ebb4fe"</ETag>
<LastModified>2017-09-04T04:45:45</LastModified>
</CopyPartResult>
```
