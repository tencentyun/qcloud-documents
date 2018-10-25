## Get Bucket Location

### 功能描述

Get Bucket Location接口可以获取一个Bucket所在的区域。


### 细节分析

> 目前区域的有效值包括ap-beijing，ap-beijing，ap-shanghai，ap-guangzhou，ap-chengdu，ap-singapore，ap-hongkong，na-toronto，eu-frankfurt分别对应北京一区，北京，上海，广州，成都，新加坡，相关，多伦多和法兰克福等地数据中心


1. 查看bucket区域信息，需要有该bucket的读权限。


### Response


#### Special Errors

> GetBucketLocation没有特殊的错误

## Delete Multiple Object

### 功能描述

Delete Multiple Object接口用于批量删除对象。

### 细节分析

> 1. 每一个批量删除请求，最多只能包含1000个需要删除的对象；
> 2. 批量删除支持二种模式的放回，verbose模式和quiet模式，默认为verbose模式。verbose模式返回每个key的删除情况，quiet模式只返回删除失败的key的情况；
> 3. 批量删除需要携带Content-MD5头部，用以校验请求body没有被修改；
> 4. 批量删除请求允许删除一个不存在的key，仍然认为成功；

### Response

#### Special Errors

在该请求下经常会发生的一些错误如下：

| 错误码            | 描述                                       | HTTP状态码         |
| :------------- | :--------------------------------------- | :-------------- |
| InvalidRequest | 没有携带必填字段Content-MD5，同时返回“Missing required header for this request: Content-MD5”错误信息 | 400 Bad Request |
| MalformedXML   | 如果请求的key的个数，超过了1000，会返回 MalformedXML错误，同时返回“delete key size is greater than 1000” | 400 Bad Request |
| InvalidDigest  | 携带的Content-MD5和服务端计算的请求body的不一致          | 400 Bad Request |

获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看[错误码](https://cloud.tencent.com/document/product/436/7730)



## Put Bucket Versioning

### 功能描述

Put Bucket Versioning接口用于开启bucket的版本管理功能

### 细节分析

> 1. 版本管理功能一经打开，只能暂停，不能关闭；
> 2. 可以设置版本管理状态为Enabled或者Suspended，表示开启版本管理和暂停版本管理；
> 3. 设置版本版本管理，你需要有bucket写权限；

### Response

#### Special Errors

在该请求下经常会发生的一些错误如下：

| 错误码             | 描述                                       | HTTP状态码         |
| :-------------- | :--------------------------------------- | :-------------- |
| InvalidArgument | 如果开启版本管理的xml body为空，会返回 InvalidArgument  | 400 Bad Request |
| InvalidDigest   | 1.携带的Content-MD5和服务端计算的请求body的不一致；<br>2.开启版本管理的状态只有Enabled和Suspended两个合法值，如果写了其他状态，会返回InvalidArgument | 400 Bad Request |

获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看[错误码](https://cloud.tencent.com/document/product/436/7730)



## Get Bucket Versioning

### 功能描述

Get Bucket Versioning接口用于获取bucket的版本管理功能的状态

### 细节分析

> 1. 获取bucket版本管理的状态，需要有该bucket的读权限；

### Response

#### Special Errors

GetBucketVersioning接口没有特殊的错误

## List Multipart Uploads

### 功能描述

List Multipart Uploads 接口用于列取正在上传还没有上传完成的分块

### 细节分析

> 1. 需要有bucket的读权限；

### Response

#### Special Errors

在该请求下经常会发生的一些错误如下：

| 错误码             | 描述                                       | HTTP状态码         |
| :-------------- | :--------------------------------------- | :-------------- |
| InvalidArgument | 1.max-uploads必须是整数，且值介于0~1000之间，否则返回InvalidArgument；2.encoding-type只能取值url，否则会返回InvalidArgument | 400 Bad Request |

获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看[错误码](https://cloud.tencent.com/document/product/436/7730)

## Put Object

### 功能描述

上传文件到指定bucket

### 细节分析

> 1. 需要有bucket的写权限；
> 2. 如果请求头的Content-Length值小于实际请求体（body）中传输的数据长度，COS仍将成功创建文件，但Object大小只等于Content-Length中定义的大小，其他数据将被丢弃；
> 3. 如果试图添加的Object的同名文件已经存在，那么新上传的文件，江覆盖原来的文件，成功时返回200 OK；

### Response

#### Special Errors

在该请求下经常会发生的一些错误如下：

| 错误码                  | 描述                                       | HTTP状态码             |
| :------------------- | :--------------------------------------- | :------------------ |
| InvalidDigest        | 如果用户上传文件时携带Content-MD5头部，COS会校验body的Md5和用户携带的MD5是否一致，如果不一致将返回InvalidDigest | 400 Bad Request     |
| KeyTooLong           | 上传文件时携带的以x-cos-meta开头的自定义头部，每个自定义头部的key和value加起来不能超过4k，否则返回KeyTooLong错误 | 400 Bad Request     |
| MissingContentLength | 如果上传文件时，没有添加Content-Length头部，会返回该错误码     | 411 Length Required |
| NoSuchBucket         | 如果试图添加的Object所在的Bucket不存在，返回404 Not Found错误，错误码：NoSuchBucket | 404 Not Found       |
| EntityTooLarge       | 如果添加的文件长度超过5G，会返回EntityTooLarge，并返回错误信息“Your proposed upload exceeds the maximum allowed object size” | 400 Bad Request     |
| InvalidURI           | 对象key长度限制为850，如果超过850会返回InvalidURI       | 400 Bad Request     |

获取更多关于COS的错误码的信息，或者产品所有的错误列表，请查看[错误码](https://cloud.tencent.com/document/product/436/7730)