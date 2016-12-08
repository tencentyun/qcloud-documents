## 功能描述
Complete Multipart Upload用来实现完成一个分块上传。当您已经使用Upload Parts上传所有块以后，你可以用该API完成上传。在使用该API时，您必须在Body中给出每一个块的PartNumber和ETag，用来校验块的准确性。

由于分块上传的合并需要数分钟时间，因而当合并分块开始的时候，COS就立即返回200的状态码，在合并的过程中，COS会周期性的返回空格信息来保持连接活跃，直到合并完成，COS会在Body中返回合并后块的内容。

当上传块小于1 MB的时候，在调用该请求时，会返回400 EntityTooSmall；当上传块编号不连续的时候，在调用该请求时，会返回400 InvalidPart；当请求Body中的块信息没有按序号从小到大排列的时候，在调用该请求时，会返回400 InvalidPartOrder；当UploadId不存在的时候，在调用该请求时，会返回404 NoSuchUpload。

建议您及时完成分块上传或者舍弃分块上传，因为已上传但是未终止的块会占用存储空间进而产生存储费用。

## 请求

### 请求语法

```http
POST /ObjectName?uploadId=UploadId HTTP 1.1
Host: <BucketName>-<UID>.<Region>.myqcloud.com
Date: date
Content-length: Size
Authorization: Auth
```

### 请求参数

无特殊请求参数

### 请求头部
无特殊请求头部

### 请求内容

| 名称                      | 描述                 | 类型        | 必须   |
| ----------------------- | ------------------ | --------- | ---- |
| CompleteMultipartUpload | 用来说明本次分块上传的所有信息    | Container | 是    |
| Part                    | 用来说明本次分块上传中每个块的信息  | Container | 是    |
| PartNumber              | 块编号                | String    | 是    |
| ETag                    | 每个块文件的 SHA-1 算法校验值 | String    | 是    |

```xml
<CompleteMultipartUpload>
  <Part>
    <PartNumber></PartNumber>
    <ETag></ETag>
  </Part>
  ...
</CompleteMultipartUpload>
```

## 返回值

### 返回头部

无特殊返回头部

### 返回内容

| 名称                      | 描述                 | 类型        |
| ----------------------- | ------------------ | --------- |
| CompleteMultipartUpload | 说明所有返回信息           | Contianer |
| Location                | 创建的Object的外网访问域名   | URI       |
| Bucket                  | 分块上传的目标Bucket      | String    |
| Key                     | Object的名称          | String    |
| ETag                    | 合并后文件的 SHA-1 算法校验值 | String    |

```xml
<CompleteMultipartUpload>
  <Location></Location>
  <Bucket></Bucket>
  <Key></Key>
  <ETag></ETag>
</CompleteMultipartUpload>
```
