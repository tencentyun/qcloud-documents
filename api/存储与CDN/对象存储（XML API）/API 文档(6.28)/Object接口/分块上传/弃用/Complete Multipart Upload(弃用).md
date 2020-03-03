## 功能描述
Complete Multipart Upload 接口请求用来实现完成整个分块上传。当使用 Upload Parts 上传完所有块以后，必须调用该 API 来完成整个文件的分块上传。在使用该 API 时，您必须在请求体中给出每一个块的 PartNumber 和 ETag，用来校验块的准确性。
由于分块上传完后需要合并，而合并需要数分钟时间，因而当合并分块开始的时候，COS 就立即返回 200 的状态码，在合并的过程中，COS 会周期性的返回空格信息来保持连接活跃，直到合并完成，COS会在响应体中返回合并后块的内容。
- 当上传块小于 1 MB 的时候，在调用该 API 时，会返回 400 EntityTooSmall；
- 当上传块编号不连续的时候，在调用该 API 时，会返回 400 InvalidPart；
- 当请求 Body 中的块信息没有按序号从小到大排列的时候，在调用该 API 时，会返回 400 InvalidPartOrder；
- 当 UploadId 不存在的时候，在调用该 API 时，会返回 404 NoSuchUpload。

><font color="#0000cc">**注意：** </font>
>建议您及时完成分块上传或者舍弃分块上传，因为已上传但是未终止的块会占用存储空间进而产生存储费用。

### 版本
当启用多版本，该 GET 操作返回对象的当前版本。要返回不同的版本，请使用 versionId 参数。

## 请求

语法示例：
```
POST /ObjectName?uploadId=UploadId HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-length: Size
Authorization: Auth String
```

> Authorization: Auth String (详细参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 章节)

### 请求行
```
POST /ObjectName?uploadId=UploadId HTTP/1.1
```
该 API 接口接受 POST 请求。
#### 请求参数 <style  rel="stylesheet"> table th:nth-of-type(1) { width: 200px; }</style>

具体内容如下：

| 参数名称     | 描述                                       | 类型     | 必选   |
| :------- | :--------------------------------------- | :----- | :--- |
| uploadId | 标识本次分块上传的 ID 。<br>使用 Initiate Multipart Upload 接口初始化分片上传时会得到一个 uploadId，该 ID 不但唯一标识这一分块数据，也标识了这分块数据在整个文件内的相对位置 | String | 是    |

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 章节。

#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该 API 接口请求的请求体具体节点内容为：
```
<CompleteMultipartUpload>
  <Part>
    <PartNumber></PartNumber>
    <ETag></ETag>
  </Part>
  ...
</CompleteMultipartUpload>
```

具体的数据内容如下：

| 节点名称（关键字）               | 父节点  | 描述              | 类型        | 必选   |
| :---------------------- | :--- | :-------------- | :-------- | :--- |
| CompleteMultipartUpload | 无    | 用来说明本次分块上传的所有信息 | Container | 是    |

Container 节点 CompleteMultipartUpload 的内容：

| 节点名称（关键字） | 父节点                     | 描述                | 类型        | 必选   |
| :-------- | :---------------------- | :---------------- | :-------- | :--- |
| Part      | CompleteMultipartUpload | 用来说明本次分块上传中每个块的信息 | Container | 是    |

Container 节点 Part 的内容：

| 节点名称（关键字）  | 父节点                          | 描述               | 类型      | 必选   |
| :--------- | :--------------------------- | :--------------- | :------ | :--- |
| PartNumber | CompleteMultipartUpload.Part | 块编号              | Integer | 是    |
| ETag       | CompleteMultipartUpload.Part | 每个块文件的 MD5 算法校验值 | String  | 是    |
## 响应

### 响应头
#### 公共响应头 
该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 章节。
#### 特有响应头

| 名称                           | 描述                                       | 类型     |
| ---------------------------- | ---------------------------------------- | ------ |
| x-cos-server-side-encryption | 指定将对象启用服务器端加密的方式。<br/>使用 COS 主密钥加密：AES256 | String |
|x-cos-version-id|在存储桶已启用多版本的情况下，新创建的对象的版本ID。| String |


### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：
```
<CompleteMultipartUploadResult>
  <Location></Location>
  <Bucket></Bucket>
  <Key></Key>
  <ETag></ETag>
</CompleteMultipartUploadResult>
```
具体的数据内容如下：

| 节点名称（关键字）                     | 父节点  | 描述       | 类型        |
| :---------------------------- | :--- | :------- | :-------- |
| CompleteMultipartUploadResult | 无    | 说明所有返回信息 | Container |

Container 节点 CompleteMultipartUploadResult 的内容：

| 节点名称（关键字） | 父节点                           | 描述                                       | 类型     |
| :-------- | :---------------------------- | :--------------------------------------- | :----- |
| Location  | CompleteMultipartUploadResult | 创建的Object的外网访问域名                         | URL    |
| Bucket    | CompleteMultipartUploadResult | 分块上传的目标Bucket，由用户自定义字符串和系统生成appid数字串由中划线连接而成，如：mybucket-1250000000 | String |
| Key       | CompleteMultipartUploadResult | Object的名称                                | String |
| ETag      | CompleteMultipartUploadResult | 合并后对象的唯一标签值，该值不是对象内容的 MD5 校验值，仅能用于检查对象唯一性                        | String |

## 实际案例

### 请求
```
POST /ObjectName?uploadId=1484728886e63106e87d8207536ae8521c89c42a436fe23bb58854a7bb5e87b7d77d4ddc48 HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com
Date: Wed，18 Jan 2017 16:17:03 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484729794;32557625794&q-key-time=1484729794;32557625794&q-header-list=host&q-url-param-list=uploadId&q-signature=23627c8fddb3823cce4257b33c663fd83f9f820d
Content-Length: 138

<CompleteMultipartUpload><Part><PartNumber>1</PartNumber><ETag>"fc392a65890e447ff4e2d256489a9773"</ETag></Part></CompleteMultipartUpload>
```

### 响应
```
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 277
Connection: keep-alive
Date: Wed，18 Jan 2017 16:17:03 GMT
Server: tencent-cos
x-cos-request-id: NTg3ZjJlMjVfNDYyMDRlXzM0YzRfMjc1

<CompleteMultipartUploadResult>
    <Location>arlenhuangtestsgnoversion-1251668577.cos.ap-beijing.myqcloud.com/ObjectName</Location>
    <Bucket>arlenhuangtestsgnoversion-1251668577</Bucket>
    <Key>ObjectName</Key>
    <ETag>"3a0f1fd698c235af9cf098cb74aa25bc"</ETag>
</CompleteMultipartUploadResult>

```
