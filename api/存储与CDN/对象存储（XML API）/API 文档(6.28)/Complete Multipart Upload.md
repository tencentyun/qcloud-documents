## 功能描述
Complete Multipart Upload 接口请求用来实现完成整个分块上传。当使用 Upload Parts 上传完所有块以后，必须调用该 API 来完成整个文件的分块上传。在使用该 API 时，您必须在请求 Body 中给出每一个块的 PartNumber 和 ETag，用来校验块的准确性。
由于分块上传完后需要合并，而合并需要数分钟时间，因而当合并分块开始的时候，COS 就立即返回 200 的状态码，在合并的过程中，COS 会周期性的返回空格信息来保持连接活跃，直到合并完成，COS会在 Body 中返回合并后块的内容。
当上传块小于 1 MB 的时候，在调用该 API 时，会返回 400 EntityTooSmall；
当上传块编号不连续的时候，在调用该 API 时，会返回 400 InvalidPart；
当请求 Body 中的块信息没有按序号从小到大排列的时候，在调用该 API 时，会返回 400 InvalidPartOrder；
当 UploadId 不存在的时候，在调用该 API 时，会返回 404 NoSuchUpload。
>**注：建议您及时完成分块上传或者舍弃分块上传，因为已上传但是未终止的块会占用存储空间进而产生存储费用。**

## 请求

语法示例：
```
POST /ObjectName?uploadId=UploadId HTTP/1.1
Host: <BucketName>-<AppID>.<Region>.myqcloud.com
Date: GMT Date
Content-length: Size
Authorization: Auth
```

> Authorization: Auth (详细参见 [请求签名](https://www.qcloud.com/document/product/436/7778) 章节)

### 请求行
```
POST /ObjectName?uploadId=UploadId HTTP/1.1
```
该 API 接口接受 POST 请求。

### 请求头

#### 公共头部
该请求操作的实现使用公共请求头,了解公共请求头详细请参见 [公共请求头部](https://www.qcloud.com/document/product/436/7728) 章节。

#### 非公共头部
该请求操作的实现没有使用特殊的请求头部。

### 请求体
该请求的请求体具体节点内容为：
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

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:--|
| CompleteMultipartUpload |无| 用来说明本次分块上传的所有信息 | Container |是|

Container 节点 ListPartsResult 的内容：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:--|
| Part |CompleteMultipartUpload| 用来说明本次分块上传中每个块的信息 | Container |是|

Container 节点 ListPartsResult 的内容：

|节点名称（关键字）|父节点|描述|类型|必选|
|:---|:-- |:--|:--|:--|
| PartNumber| CompleteMultipartUpload.Part | 块编号 | String |是|
| ETag | CompleteMultipartUpload.Part | 每个块文件的 MD5 算法校验值 | String |是|
## 响应

#### 响应头
**公共响应头** 
该响应使用公共响应头,了解公共响应头详细请参见 [公共响应头部](https://www.qcloud.com/document/product/436/7729) 章节。
**特有响应头**
该响应无特殊的响应头。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：
```
<CompleteMultipartUpload>
  <Location></Location>
  <Bucket></Bucket>
  <Key></Key>
  <ETag></ETag>
</CompleteMultipartUpload>
```
具体的数据内容如下：

具体的数据内容如下：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| CompleteMultipartUpload |无| 说明所有返回信息 | Container |

Container 节点 CompleteMultipartUpload 的内容：

|节点名称（关键字）|父节点|描述|类型|
|:---|:-- |:--|:--|
| Location |CompleteMultipartUpload| 创建的Object的外网访问域名 | URI |
| Bucket |CompleteMultipartUpload| 分块上传的目标Bucket | String |
| Key |CompleteMultipartUpload| Object的名称 | String |
| ETag |CompleteMultipartUpload| 合并后文件的 MD5 算法校验值| String |

## 实际案例

### 请求
```
POST /ObjectName?uploadId=1484728886e63106e87d8207536ae8521c89c42a436fe23bb58854a7bb5e87b7d77d4ddc48 HTTP/1.1
Host: arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com
Date: Wed，18 Jan 2017 16:17:03 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUjfGFO&q-sign-time=1484729794;32557625794&q-key-time=1484729794;32557625794&q-header-list=host&q-url-param-list=uploadId&q-signature=23627c8fddb3823cce4257b33c663fd83f9f820d
Content-Length: 155
Content-Type: application/x-www-form-urlencoded
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

<CompleteMultipartUpload>
    <Location>arlenhuangtestsgnoversion-1251668577.sg.myqcloud.com/ObjectName</Location>
    <Bucket>arlenhuangtestsgnoversion</Bucket>
    <Key>ObjectName</Key>
    <ETag>"3a0f1fd698c235af9cf098cb74aa25bc"</ETag>
</CompleteMultipartUpload>

```
