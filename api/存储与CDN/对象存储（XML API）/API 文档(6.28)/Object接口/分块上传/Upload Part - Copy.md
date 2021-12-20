## 功能描述
Upload Part - Copy  请求用于实现将一个对象的分块内容从源路径复制到目标路径。通过指定 x-cos-copy-source 来指定源对象，x-cos-copy-source-range 指定字节范围（允许分块的大小为1MB - 5GB）。

>!
>- 使用 Upload Part - Copy 接口前，需先使用 [Initiate Multipart Upload](https://cloud.tencent.com/document/product/436/7746) 接口初始化分块上传任务并指定目标路径。
>- 如果目标对象和源对象不属于同一个地域，且目标对象分块会超过5GB，那么需要使用分块上传或者分块拷贝的接口来复制对象。
>- 使用上传分块对象，必须先初始化分块上传。在初始化分块上传的响应中，会返回一个唯一的描述符（upload ID），您需要在分块上传请求中携带此 ID。
>

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=UploadPartCopy&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>

#### 版本控制
当存储桶启用了版本控制，x-cos-copy-source 标识被复制的对象的当前版本。如果当前版本是删除标记，并且 x-cos-copy-source 不指定版本，则对象存储会认为该对象已删除并返回404错误。如果您在 x-cos-copy-source 中指定 versionId 且 versionId 是删除标记，则对象存储会返回 HTTP 400错误，因为删除标记不允许作为 x-cos-copy-source 的版本。

## 请求
#### 请求示例

```http
PUT /examplebucket?partNumber=PartNumber&uploadId=UploadId  HTTP/1.1
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

| 名称         | 描述           | 类型     | 是否必选   |
| ----------- | ----------- | ------------- | ---- |
| x-cos-copy-source     | 源对象 URL 路径，可以通过 versionid 子资源指定历史版本         | String | 是    |


**推荐头部**

该请求操作的实现使用如下推荐请求头部信息：

| 名称          | 描述      | 类型     | 是否必选   |
| ---------------- | ---------- | ------ | -------- |
| x-cos-copy-source-range                    | 源对象的字节范围，范围值必须使用 bytes=first-last 格式，first 和 last 都是基于 0 开始的偏移量。<br>例如 bytes=0-9 表示您希望拷贝源对象的开头10个字节的数据，如果不指定，则表示拷贝整个对象       | String  | 否   |
| x-cos-copy-source-If-Modified-Since   | 当 Object 在指定时间后被修改，则执行操作，否则返回412，<br>可与 x-cos-copy-source-If-None-Match 一起使用，与其他条件联合使用返回冲突 | String | 否    |
| x-cos-copy-source-If-Unmodified-Since | 当 Object 在指定时间后未被修改，则执行操作，否则返回412，<br>可与 x-cos-copy-source-If-Match 一起使用，与其他条件联合使用返回冲突 | String | 否    |
| x-cos-copy-source-If-Match            | 当 Object 的 Etag 和给定一致时，则执行操作，否则返回412，<br>可与 x-cos-copy-source-If-Unmodified-Since 一起使用，与其他条件联合使用返回冲突 | String | 否    |
| x-cos-copy-source-If-None-Match       | 当 Object 的 Etag 和给定不一致时，则执行操作，否则返回412，<br>可与 x-cos-copy-source-If-Modified-Since 一起使用，与其他条件联合使用返回冲突 | String | 否    |

#### 请求参数

 名称|描述|类型|是否必选
---|---|---|---
partNumber|分块拷贝的块号|String|是
uploadId|使用上传分块文件，必须先初始化分块上传。在初始化分块上传的响应中，会返回一个唯一的描述符（upload ID），您需要在分块上传请求中携带此 ID|String|是

#### 请求体
该请求的请求体为空。

## 响应

#### 响应头
#### 公共响应头 
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

|名称&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|描述|类型|
|---|---|---|
|x-cos-copy-source-version-id|如果已在源存储桶上启用版本控制，则复制源对象的版本|String|
|x-cos-server-side-encryption | 如果通过 COS 管理的服务端加密来存储对象，响应将包含此头部和所使用的加密算法的值，AES256 | String|

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<?xml version="1.0" encoding="UTF-8" ?>
<CopyPartResult>
   <ETag>"ba82b57cfdfda8bd17ad4e5879ebb4fe"</ETag>
   <LastModified>2017-09-04T04:45:45</LastModified>
</CopyPartResult>
```

具体的节点描述如下：

| 名称          | 描述             | 类型     |
| ---------- | ------------------- | ------ |
| CopyPartResult | 返回复制结果信息           | String |
| ETag             | 返回对象的 MD5 算法校验值，ETag 的值可以用于检查 Object 的内容是否发生变化 | String |
| LastModified     | 返回对象最后修改时间，GMT 格式        | String |

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例
#### 请求

```HTTP
PUT /exampleobject?partNumber=1&uploadId=1505706248ca8373f8a5cd52cb129f4bcf85e11dc8833df34f4f5bcc456c99c42cd1ffa2f9 HTTP/1.1
User-Agent: curl/7.19.7 (x86_64-redhat-linux-gnu) libcurl/7.19.7 NSS/3.13.1.0 zlib/1.2.3 libidn/1.18 libssh2/1.2.2
Accept: */*
x-cos-copy-source:examplebucket-1250000000.cos.ap-shanghai.myqcloud.com/exampleobject1
x-cos-copy-source-range: bytes=10-100
Host: examplebucket-1250000000.cos.ap-shanghai.myqcloud.com
Authorization:q-sign-algorithm=sha1&q-ak=AKIDDNMEycgLRPI2axw9xa2Hhx87wZ3M****&q-sign-time=1507530223;1508530223&q-key-time=1507530223;1508530223&q-header-list=&q-url-param-list=&q-signature=d02640c0821c49293e5c289fa07290e6b2f0****
```

#### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 133 
Connection: keep-alive 
Date: Mon, 04 Sep 2017 04:45:45 GMT
Server: tencent-cos
x-cos-request-id: NTlkYjFjYWJfMjQ4OGY3MGFfNGIz****

<CopyPartResult>
   <ETag>"ba82b57cfdfda8bd17ad4e5879ebb4fe"</ETag>
   <LastModified>2017-09-04T04:45:45</LastModified>
</CopyPartResult>
```
