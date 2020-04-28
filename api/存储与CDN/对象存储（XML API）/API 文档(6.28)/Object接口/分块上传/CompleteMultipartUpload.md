## 功能描述
Complete Multipart Upload 接口请求用来实现完成整个分块上传。当使用 Upload Parts 上传所有分块完成后，必须调用该 API 来完成整个文件的分块上传。在使用该 API 时，您必须在请求 Body 中给出每一个块的 PartNumber 和 ETag，用来校验块的准确性。
由于分块上传完成后需要合并，而合并需要数分钟时间，因而当合并分块开始时，COS 会立即返回200的状态码，在合并的过程中，COS 会周期性的返回空格信息来保持连接活跃，直到合并完成，COS 会在 Body 中返回合并完成后，整个块的内容。
- 当上传的分块小于1MB的时候，在调用该 API 时，会返回400 EntityTooSmall。
- 当上传块编号不连续的时候，在调用该 API 时，会返回400 InvalidPart。
- 当请求 Body 中的块信息没有按序号从小到大排列的时候，在调用该 API 时，会返回400 InvalidPartOrder。
- 当 UploadId 不存在的时候，在调用该 API 时，会返回404 NoSuchUpload。

>!建议您及时完成分块上传或者舍弃分块上传，因为已上传但是未终止的块会占用存储空间进而产生存储费用。

## 请求

#### 请求示例

```shell
POST /<ObjectKey>?uploadId=UploadId HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-length: Size
Authorization: Auth String
```

>? Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


#### 请求头
此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。


#### 请求体

该 API 接口请求的请求体具体节点内容为：
```shell
<CompleteMultipartUpload>
  <Part>
    <PartNumber>1</PartNumber>
    <ETag>"fc392a65890e447ff4e2d256489a9773"</ETag>
  </Part>
  <Part>
    <PartNumber>2</PartNumber>
    <ETag>"fc392a65890e447ff4e2d256489a9773"</ETag>
  </Part>
    ...
</CompleteMultipartUpload>
```

具体的数据内容如下：

| 节点名称（关键字）               | 父节点  | 描述              | 类型        | 是否必选   |
| :---------------------- | :--- | :-------------- | :-------- | :--- |
| CompleteMultipartUpload | 无    | 用来说明本次分块上传的所有信息 | Container | 是    |

Container 节点 CompleteMultipartUpload 的内容：

| 节点名称（关键字） | 父节点                     | 描述                | 类型        | 是否必选   |
| :-------- | :---------------------- | :---------------- | :-------- | :--- |
| Part      | CompleteMultipartUpload | 用来说明本次分块上传中每个块的信息 | Container | 是    |

Container 节点 Part 的内容：

| 节点名称（关键字）  | 父节点                          | 描述               | 类型      | 是否必选   |
| :--------- | :--------------------------- | :--------------- | :------ | :--- |
| PartNumber | CompleteMultipartUpload.Part | 块编号              | Integer | 是    |
| ETag       | CompleteMultipartUpload.Part | 每个块文件的 MD5 算法校验值 | String  | 是    |

## 响应

#### 响应头
#### 公共响应头 
该响应使用公共响应头，了解公共响应头详细请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 特有响应头

**服务端加密相关响应**

如果在上传时指定使用了服务端加密，响应头部将会包含如下信息：

| 名称                           | 描述                                       | 类型     |
| ---------------------------- | ---------------------------------------- | ------ |
| x-cos-server-side-encryption | 指定将对象启用服务端加密的方式。<br/>使用 COS 主密钥加密：AES256 | String |

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：
```shell
<CompleteMultipartUploadResult>
    <Location>examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject</Location>
    <Bucket>examplebucket-1250000000</Bucket>
    <Key>exampleobject</Key>
    <ETag>"3a0f1fd698c235af9cf098cb74aa25bc"</ETag>
</CompleteMultipartUploadResult>
```

具体的数据内容如下：

| 节点名称（关键字）                     | 父节点  | 描述       | 类型        |
| :---------------------------- | :--- | :------- | :-------- |
| CompleteMultipartUploadResult | 无    | 说明所有返回信息 | Container |

Container 节点 CompleteMultipartUploadResult 的内容：

| 节点名称（关键字） | 父节点                           | 描述                                       | 类型     |
| :-------- | :---------------------------- | :--------------------------------------- | :----- |
| Location  | CompleteMultipartUploadResult | 新创建的对象的外网访问域名                         | URL    |
| Bucket    | CompleteMultipartUploadResult | 分块上传的目标存储桶，格式为 BucketName-APPID，例如：examplebucket-1250000000 | String |
| Key       | CompleteMultipartUploadResult | 对象名称                                | String |
| ETag      | CompleteMultipartUploadResult | 合并后对象的唯一标签值，该值不是对象内容的 MD5 校验值，仅能用于检查对象唯一性                        | String |

## 实际案例

#### 请求
```shell
POST /exampleobject?uploadId=1484728886e63106e87d8207536ae8521c89c42a436fe23bb58854a7bb5e87b7d77d4ddc48 HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed，18 Jan 2017 16:17:03 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDWtTCBYjM5OwLB9CAwA1Qb2ThTSUj****&q-sign-time=1484729794;32557625794&q-key-time=1484729794;32557625794&q-header-list=host&q-url-param-list=uploadId&q-signature=23627c8fddb3823cce4257b33c663fd83f9f****
Content-Length: 138

<CompleteMultipartUpload>
  <Part>
    <PartNumber>1</PartNumber>
    <ETag>"fc392a65890e447ff4e2d256489a9773"</ETag>
  </Part>
  <Part>
    <PartNumber>2</PartNumber>
    <ETag>"fc392a65890e447ff4e2d256489a9774"</ETag>
  </Part>
</CompleteMultipartUpload>
```

#### 响应
```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 277
Connection: keep-alive
Date: Wed，18 Jan 2017 16:17:03 GMT
Server: tencent-cos
x-cos-request-id: NTg3ZjJlMjVfNDYyMDRlXzM0YzRfMjc1

<CompleteMultipartUploadResult>
    <Location>examplebucket-1250000000.cos.ap-beijing.myqcloud.com/exampleobject</Location>
    <Bucket>examplebucket-1250000000</Bucket>
    <Key>exampleobject</Key>
    <ETag>"3a0f1fd698c235af9cf098cb74aa25bc"</ETag>
</CompleteMultipartUploadResult>
```
