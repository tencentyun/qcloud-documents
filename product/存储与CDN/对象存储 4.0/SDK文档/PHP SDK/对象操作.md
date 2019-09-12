## 简介

本文档提供关于对象的简单操作、分块操作等其他操作相关的 API 概览以及 SDK 示例代码。

**简单操作**

| API                                                          | 操作名         | 操作描述                                  |
| ------------------------------------------------------------ | -------------- | ----------------------------------------- |
| [GET Bucket（List Object）](https://cloud.tencent.com/document/product/436/7734) | 查询对象列表   | 查询存储桶下的部分或者全部对象                  |
| [GET Bucket Object Versions](https://cloud.tencent.com/document/product/436/35521) | 查询对象及其历史版本列表 |   查询存储桶下的部分或者全部对象及其历史版本信息|
| [PUT Object](https://cloud.tencent.com/document/product/436/7749) | 简单上传对象       | 上传一个 Object（文件/对象）至 Bucket     |
| [POST Object](https://cloud.tencent.com/document/product/436/14690) | 表单上传对象   | 使用表单请求上传对象                      |
| [HEAD Object](https://cloud.tencent.com/document/product/436/7745) | 查询对象元数据 | 查询 Object 的 Meta 信息                  |
| [GET Object](https://cloud.tencent.com/document/product/436/7753) | 下载对象       | 下载一个 Object（文件/对象）至本地        |
| [PUT Object - Copy](https://cloud.tencent.com/document/product/436/10881) | 设置对象复制   | 复制文件到目标路径                        |
| [DELETE Object](https://cloud.tencent.com/document/product/436/7743) | 删除单个对象   | 在 Bucket 中删除指定 Object （文件/对象） |
|[DELETE Multiple Object](https://cloud.tencent.com/document/product/436/8289) 	|  删除多个对象	|   在 Bucket 中批量删除 Object （文件/对象）|


**分块操作**

| API                                                          | 操作名         | 操作描述                             |
| ------------------------------------------------------------ | -------------- | ------------------------------------ |
| [List Multipart Uploads](https://cloud.tencent.com/document/product/436/7736) | 查询分块上传   | 查询正在进行中的分块上传信息         |
| [Initiate Multipart Upload](https://cloud.tencent.com/document/product/436/7746) | 初始化分块上传 | 初始化 Multipart Upload 上传操作     |
| [Upload Part](https://cloud.tencent.com/document/product/436/7750) | 上传分块       | 分块上传对象  |
| [Upload Part - Copy](https://cloud.tencent.com/document/product/436/8287) | 复制分块       | 将其他对象复制为一个分块             |
| [List Parts](https://cloud.tencent.com/document/product/436/7747) | 查询已上传块   | 查询特定分块上传操作中的已上传的块   |
| [Complete Multipart Upload](https://cloud.tencent.com/document/product/436/7742) | 完成分块上传   | 完成整个对象的分块上传               |
| [Abort Multipart Upload](https://cloud.tencent.com/document/product/436/7740) | 终止分块上传   | 终止一个分块上传操作并删除已上传的块 |

**其他操作**

| API                                                          | 操作名       | 操作描述                                      |
| ------------------------------------------------------------ | ------------ | --------------------------------------------- |
| [POST Object restore](https://cloud.tencent.com/document/product/436/12633) | 恢复归档对象 | 将归档类型的对象取回访问                      |
| [PUT Object acl](https://cloud.tencent.com/document/product/436/7748) | 设置对象 ACL | 设置 Bucket 中某个 Object （文件/对象）的 ACL |
| [GET Object acl](https://cloud.tencent.com/document/product/436/7744) | 查询对象 ACL | 查询 Object（文件/对象）的 ACL                |



## 简单操作

### 查询对象列表

#### 功能说明

查询指定存储桶中所有的对象（List Object）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model listObjects(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->listObjects(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Delimiter' => '/',
        'EncodingType' => 'url',
        'Marker' => 'doc/picture.jpg',
        'Prefix' => 'doc',
        'MaxKeys' => 1000,
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 必填          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 是 |
| Delimiter | String | 默认为空，设置分隔符，比如设置`/`来模拟文件夹    | 否 |
| EncodingType | String | 默认不编码，规定返回值的编码方式，可选值：url    | 否 |
| Marker | String |	默认以 UTF-8 二进制顺序列出条目，标记返回 objects 的 list 的起点位置                     | 否 |
| Prefix | String | 默认为空，对 object 的 key 进行筛选，匹配指定前缀（prefix）的 objects        | 否 |
| MaxKeys | Int | 最多返回的 objects 数量，默认为最大的1000 | 否|

#### 返回结果示例

```php
Guzzle\Service\Resource\Model Object
(
    [structure:protected] => 
    [data:protected] => Array
        (
            [Name] => examplebucket-1250000000
            [Prefix] => doc
            [Marker] => doc/picture.jpg
            [MaxKeys] => 10
            [IsTruncated] => 1
            [NextMarker] => doc/exampleobject
            [Contents] => Array
                (
                    [0] => Array
                        (
                            [Key] => doc/exampleobject
                            [LastModified] => 2019-02-14T12:20:40.000Z
                            [ETag] => "e37b429559d82e852af0b2f5b4d078ab72b90208"
                            [Size] => 6532594
                            [Owner] => Array
                                (
                                    [ID] => 100000000001
                                    [DisplayName] => 100000000001
                                )

                            [StorageClass] => STANDARD
                        )

                    [1] => Array
                        (
                            [Key] => doc/exampleobject2
                            [LastModified] => 2019-03-04T06:34:43.000Z
                            [ETag] => "988f9f28e68eba9b8c1f5f98ccce0a3c"
                            [Size] => 28
                            [Owner] => Array
                                (
                                    [ID] => 100000000001
                                    [DisplayName] => 100000000001
                                )

                            [StorageClass] => STANDARD
                        )
                )
            [RequestId] => NWNhMzM0MmZfOWUxYzBiMDlfOTk2YV83ZWE3ODE=
        )

)
```
#### 返回结果说明

| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Name | String | 存储桶名称，格式：BucketName-APPID                         | 无 |
| Delimiter | String | 设置分隔符，比如设置`/`来模拟文件夹    | 无 |
| EncodingType | String | 规定返回值的编码方式    | 无 |
| Marker | String |	默认以 UTF-8 二进制顺序列出条目，标记返回 objects 的 list 的起点位置                     | 无 |
| Prefix | String | 对 object 的 key 进行筛选，匹配指定前缀（prefix）的 objects        | 无  |
| MaxKeys | Int | 最多返回的 objects 数量，默认为最大的1000 | 无 |
| IsTruncated | Int | 表示返回的 objects 否被截断 | 无 |
| Contents | Array | 返回的对象列表 | 无 |
| Content | Array | 返回的对象属性，包含所有 objects 元信息的 list，包括 'ETag'，'StorageClass'，'Key'，'Owner'，'LastModified'，'Size' 等信息 | Contents |


### 查询对象及其历史版本列表 

#### 功能说明

查询存储桶下的部分或者全部对象及其历史版本信息。

#### 方法原型

```
public Guzzle\Service\Resource\Model listObjectVersions(array $args = array());
```
#### 请求示例

```php
try {
    $result = $cosClient->listObjectVersions(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Delimiter' => '/',
        'EncodingType' => 'url',
        'KeyMarker' => 'string',
        'VersionIdMarker' => 'string',
        'Prefix' => 'doc',
        'MaxKeys' => 1000,
    )); 
    print_r($result);
} catch (\Exception $e) {
    echo($e);
}
```

#### 参数说明

| 参数名称     | 类型      | 描述                            | 必填 |
| ------------- | -------------------------- | ------ | ---- |
| Bucket   | String |    存储桶名称，由 BucketName-APPID 构成     |                    是   |
| Prefix    | String  | 默认为空，对对象的对象键进行筛选，匹配 prefix 为前缀的对象 | 否   |
| Delimiter  | String   | 默认为空，设置分隔符，比如设置`/`来模拟文件夹          | 否   |
| KeyMarker | String      | 默认以 UTF-8 二进制顺序列出条目，标记返回对象的 list 的 Key 的起点位置  | 否   |
| VersionIdMarker | String  | 默认以 UTF-8 二进制顺序列出条目，标记返回对象的 list 的 VersionId 的起点位置| 否   |
| MaxKeys        | Int   | 最多返回的对象数量，默认为最大的1000          | 否   |
| EncodingType      | String    | 默认不编码，规定返回值的编码方式，可选值：url         | 否   |

#### 返回结果示例

```php
Guzzle\Service\Resource\Model Object
(
    [structure:protected] => 
    [data:protected] => Array
        (
            [Name] => examplebucket-1250000000
            [Prefix] => doc
            [KeyMarker] => string
            [VersionIdMarker] => string
            [MaxKeys] => 10
            [IsTruncated] => 1
            [NextKeyMarker] => string
            [NextVersionIdMarker] => string
            [Versions] => Array
                (
                    [0] => Array
                        (
                            [Key] => doc/exampleobject1
                            [VersionId] => null
                            [IsLatest] => 1
                            [LastModified] => 2019-06-13T09:24:52.000Z
                            [ETag] => "96e79218965eb72c92a549dd5a330112"
                            [Size] => 6
                            [StorageClass] => STANDARD
                            [Owner] => Array
                                (
                                    [UID] => 1251668577
                                )
                        )

                    [1] => Array
                        (
                            [Key] => doc/exampleobject2
                            [VersionId] => MTg0NDUxODMyMTE2ODY0OTExOTk
                            [IsLatest] => 1
                            [LastModified] => 2019-06-18T12:47:03.000Z
                            [ETag] => "698d51a19d8a121ce581499d7b701668"
                            [Size] => 3
                            [StorageClass] => STANDARD
                            [Owner] => Array
                                (
                                    [UID] => 1251668577
                                )
                        )
                    )
            [RequestId] => NWQwOGVkZGRfMjViMjU4NjRfODNjN18xMTE5YWI4
        )

)
```
#### 返回结果说明

| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Name | String | 存储桶名称，格式：BucketName-APPID                         | 无 |
| Delimiter | String | 设置分隔符，比如设置`/`来模拟文件夹    | 无 |
| EncodingType | String | 规定返回值的编码方式    | 无 |
| KeyMarker | String |默认以 UTF-8 二进制顺序列出条目，标记返回对象的 list 的 Key 的起点位置    | 无 |
| VersionIdMarker | String |	 默认以 UTF-8 二进制顺序列出条目，标记返回对象的 list 的 VersionId 的起点位置          | 无 |
| NextKeyMarker | String |	当 IsTruncated 为 true 时，标记下一次返回对象的 list 的 Key 的起点位置        | 无 |
| NextVersionIdMarker | String | 当 IsTruncated 为 true 时，标记下一次返回对象的 list 的 VersionId 的起点位置    | 无 |
| Prefix | String | 对 object 的 key 进行筛选，匹配指定前缀（prefix）的 objects        | 无  |
| MaxKeys | Int | 最多返回的 objects 数量，默认为最大的1000 | 无 |
| IsTruncated | Int | 表示返回的 objects 否被截断 | 无 |
| Versions | Array | 包含所有多个版本对象元数据的 list | 无 |
| Version | Array | 包含所有多个版本对象元数据的 list，包括 'ETag'，'StorageClass'，'Key'，'VersionId'，'IsLatest'，'Owner'，'LastModified'，'Size' 等信息 | Versions |
| CommonPrefixes | Array | 所有以 Prefix 开头，以 Delimiter 结尾的对象被归到同一类 | 无 |




### 简单上传对象

#### 功能说明

上传对象到指定的存储桶中（PUT Object），最大支持5G大小的文件，如果需要上传超过5G的文件，建议使用高级接口中的复合上传接口。

#### 方法原型

```php
public Guzzle\Service\Resource\Model putObject(array $args = array())
```

#### 请求示例

```php
try { 
    $result = $cosClient->putObject(array( 
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID 
        'Key' => 'exampleobject', 
        'Body' => fopen('/data/exampleobject', 'rb'), 
        /*
        'ACL' => 'string',
        'CacheControl' => 'string',
        'ContentDisposition' => 'string',
        'ContentEncoding' => 'string',
        'ContentLanguage' => 'string',
        'ContentLength' => integer,
        'ContentType' => 'string',
        'Expires' => 'string',
        'GrantFullControl' => 'string',
        'GrantRead' => 'string',
        'GrantWrite' => 'string',
        'Metadata' => array(
        'string' => 'string',
        ),
        'ContentMD5' => 'string',
        'ServerSideEncryption' => 'string',
        'StorageClass' => 'string'
        */
    )); 
    // 请求成功 
    print_r($result); 
} catch (\Exception $e) { 
    // 请求失败 
    echo($e); 
}

```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 必填          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 是 |
| Key | String | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg 中，对象键为 doc/pic.jpg    | 否 |
| ACL | String | 设置对象的 ACL，如 private、public-read| 否 |
| Body | File/String | 上传的内容 | 是 |
| CacheControl | String |	缓存策略，设置 Cache-Control | 否 |
| ContentDisposition | String | 文件名称，设置 Content-Disposition  | 否  |
| ContentEncoding | String | 编码格式，设置 Content-Encoding | 否 |
| ContentLanguage | String | 语言类型，设置 Content-Language | 否 |
| ContentLength | Int | 设置传输长度 | 否 |
| ContentType | String | 	内容类型，设置 Content-Type | 否 |
| Expires | String | 设置 Content-Expires | 否 |
| Metadata | Array | 用户自定义的文件元信息 | 否 |
| StorageClass | String | 文件的存储类型，STANDARD 、 STANDARD_IA 、 ARCHIVE，默认值：STANDARD | 否 |
| ContentMD5 | String | 设置上传文件的 MD5 值用于校验 | 否 |
| ServerSideEncryption | String | 服务端加密方法 | 否 |

#### 返回结果示例

```php
Guzzle\Service\Resource\Model Object
(
    [structure:protected] => 
    [data:protected] => Array
        (
            [ETag] => "698d51a19d8a121ce581499d7b701668"
            [VersionId] => MTg0NDUxODMyMTE2ODY0OTExOTk
            [RequestId] => NWQwOGRkNDdfMjJiMjU4NjRfNzVjXzEwNmVjY2M=
            [ObjectURL] => http://lewzylucd2-1251668577.cos.ap-chengdu.myqcloud.com/123
        )

)
```
#### 返回结果说明

| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| ETag | String |	上传文件的 MD5 值 | 无 |
| VersionId | String | 开启多版本后，文件的版本号  | 无  |


### 查询对象元数据

#### 功能说明

查询 Object 的 Meta 信息（HEAD Object）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model headObject(array $args = array());
```

#### 请求示例

```php
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为 http
        'credentials'=> array(
            'secretId'  => $secretId ,
            'secretKey' => $secretKey)));
try {
    $result = $cosClient->headObject(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Key' => 'exampleobject',
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 必填     |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 是 |
| Key | String | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名<br>examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg 中，对象键为 doc/pic.jpg    | 是 |
| VersionId | String | 开启多版本后，指定文件的具体版本                        | 否 |

#### 返回结果示例

```php
Guzzle\Service\Resource\Model Object
(
    [structure:protected] => 
    [data:protected] => Array
        (
            [DeleteMarker] => 
            [AcceptRanges] => 
            [Expiration] => 
            [Restore] => 
            [LastModified] => Tue, 02 Apr 2019 12:38:09 GMT
            [ContentLength] => 238186
            [ETag] => "af9f3b8eaf64473278909183abba1e31"
            [MissingMeta] => 
            [VersionId] => 
            [CacheControl] => 
            [ContentDisposition] => 
            [ContentEncoding] => 
            [ContentLanguage] => 
            [ContentType] => text/plain; charset=utf-8
            [Expires] => 
            [ServerSideEncryption] => 
            [Metadata] => Array
                (
                    [md5] => af9f3b8eaf64473278909183abba1e31
                )
            [SSECustomerAlgorithm] => 
            [SSECustomerKeyMD5] => 
            [SSEKMSKeyId] => 
            [StorageClass] => 
            [RequestCharged] => 
            [ReplicationStatus] => 
            [RequestId] => NWNhMzU3Y2ZfMzFhYzM1MGFfODdhMF8xOTExM2U=
        )

)
```
#### 返回结果说明

| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| CacheControl | String |	缓存策略，设置 Cache-Control | 无 |
| ContentDisposition | String | 文件名称，设置 Content-Disposition  | 无  |
| ContentEncoding | String | 编码格式，设置 Content-Encoding | 无 |
| ContentLanguage | String | 语言类型，设置 Content-Language | 无 |
| ContentLength | Int | 设置传输长度 | 无 |
| ContentType | String | 	内容类型，设置 Content-Type | 无 |
| Metadata | Array | 用户自定义的文件元信息 | 无 |
| StorageClass | String | 文件的存储类型，STANDARD 、 STANDARD_IA 、 ARCHIVE | 无 |
| ServerSideEncryption | String | 服务端加密方法 | 无 |
| ETag | String | 文件的MD5值 | 无 |
| Restore | String | 归档文件的回热信息 | 无 |


### 下载对象

#### 功能说明

下载对象到本地（GET Object）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model getObject(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->getObject(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Key' => 'exampleobject',
        'SaveAs' => '/data/exampleobject',
        /*
        'Range' => 'bytes=0-10',
        'VersionId' => 'string',
        'ResponseCacheControl' => 'string',
        'ResponseContentDisposition' => 'string',
        'ResponseContentEncoding' => 'string',
        'ResponseContentLanguage' => 'string',
        'ResponseContentType' => 'string',
        'ResponseExpires' => 'string',
        */
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 必填          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 是 |
| Key | String | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名<br>examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg 中，对象键为 doc/pic.jpg    | 是 |
| SaveAs | String | 保存到本地的本地文件路径 | 否 |
| VersionId   | String |  开启多版本后，指定文件的具体版本  | 否 |
| Range | String | 设置下载文件的范围，格式为 bytes=first-last   | 否|
| ResponseCacheControl | String | 	设置响应头部 Cache-Control | 否 |
| ResponseContentDisposition | String | 设置响应头部 Content-Disposition  | 否 |
| ResponseContentEncoding | String | 	设置响应头部 Content-Encoding | 否 |
| ResponseContentLanguage | String | 设置响应头部 Content-Language  | 否 |
| ResponseContentType | String | 	设置响应头部 Content-Type | 否 |
| ResponseExpires | String | 设置响应头部 Content-Expires  | 否 |


#### 返回结果示例

```php
Guzzle\Service\Resource\Model Object
(
    [structure:protected] => 
    [data:protected] => Array
        (
            [Body] => 
            [DeleteMarker] => 
            [AcceptRanges] => bytes
            [Expiration] => 
            [Restore] => 
            [LastModified] => Tue, 02 Apr 2019 20:38:09 GMT
            [ContentLength] => 238186
            [ETag] => "af9f3b8eaf64473278909183abba1e31"
            [MissingMeta] => 
            [VersionId] => 
            [CacheControl] => 
            [ContentDisposition] => 
            [ContentEncoding] => 
            [ContentLanguage] => 
            [ContentRange] => 
            [ContentType] => text/plain; charset=utf-8
            [Expires] => 
            [WebsiteRedirectLocation] => 
            [ServerSideEncryption] => 
            [Metadata] => Array
                (
                    [md5] => af9f3b8eaf64473278909183abba1e31
                )

            [SSECustomerAlgorithm] => 
            [SSECustomerKeyMD5] => 
            [SSEKMSKeyId] => 
            [StorageClass] => 
            [RequestCharged] => 
            [ReplicationStatus] => 
            [RequestId] => NWNhNDBmYzBfNmNhYjM1MGFfMmUzYzFfMWIzMDYz
        )

)
```
#### 返回结果说明

| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Body | File/String | 下载内容    | 无 |
| ETag | String | 文件的 MD5 值 | 无 |
| Expires | String | Content-Expires | 无 |
| Metadata | Array | 用户自定义的文件元信息 | 无 |
| StorageClass | String | 文件的存储类型，STANDARD 、 STANDARD_IA 、 ARCHIVE，默认值：STANDARD | 无 |
| ContentMD5 | String | 设置上传文件的 MD5 值用于校验 | 无 |
| ServerSideEncryption | String | 服务端加密方法 | 无 |
| CacheControl | String |	缓存策略，设置 Cache-Control | 无 |
| ContentDisposition | String | 文件名称，设置 Content-Disposition  | 无  |
| ContentEncoding | String | 编码格式，设置 Content-Encoding | 无 |
| ContentLanguage | String | 语言类型，设置 Content-Language | 无 |
| ContentLength | Int | 设置传输长度 | 无 |
| ContentType | String | 	内容类型，设置 Content-Type | 无 |
| Metadata | Array | 用户自定义的文件元信息 | 无 |
| Restore | String | 归档文件的回热信息 | 无 |

### 设置对象复制
将一个对象复制到目标路径（PUT Object - Copy）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model copyObject(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->copyObject(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Key' => 'exampleobject',
        'CopySource' => 'examplebucket2-1250000000.cos.ap-guangzhou.myqcloud.com/exampleobject',
        /*
        'MetadataDirective' => 'string',
        'ACL' => 'string',
        'CacheControl' => 'string',
        'ContentDisposition' => 'string',
        'ContentEncoding' => 'string',
        'ContentLanguage' => 'string',
        'ContentLength' => integer,
        'ContentType' => 'string',
        'Expires' => 'string',
        'GrantFullControl' => 'string',
        'GrantRead' => 'string',
        'GrantWrite' => 'string',
        'Metadata' => array(
        'string' => 'string',
        ),
        'ContentMD5' => 'string',
        'ServerSideEncryption' => 'string',
        'StorageClass' => 'string'
        */
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}

```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 必填          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 是 |
| Key | String | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名<br>examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg 中，对象键为 doc/pic.jpg    | 是 |
| CopySource | String | 描述拷贝源文件的路径，包含 Appid、Bucket、Key、Region，<br>例如 examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg | 是 |
| MetadataDirective | String | 可选值为 Copy、Replaced。设置为 Copy 时，忽略设置的用户元数据信息直接复制，设置为 Replaced 时，按设置的元信息修改元数据，当目标路径和源路径一样时，必须设置为 Replaced   | 否 |

### 删除单个对象

#### 功能说明

在存储桶中删除指定 Object （文件/对象）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model deleteObject(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->deleteObject(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Key' => 'exampleobject',
        'VersionId' => 'string'
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 必填          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 是|
| Key | String | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名<br>examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg 中，对象键为 doc/pic.jpg    | 是 |
| VersionId | String | 删除文件的版本号 |  否  |


### 删除多个对象

#### 功能说明

在存储桶中批量删除 Object （文件/对象）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model deleteObjects(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->deleteObjects(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Objects' => array(
            array(
                'Key' => 'exampleobject',
        		'VersionId' => 'string'
            ),  
            // ... repeated
        ),  
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}

```

#### 参数说明

| 参数名称 | 类型   | 描述                                                         | 必填 |
| -------- | ------ | ------------------------------------------------------------ | ------ |
| Bucket   | String | 存储桶名称，格式：BucketName-APPID                           | 是     |
| Objects   | Array | 删除对象列表     | 是     |
| Object   | Array | 删除的对象     | 是     |
| Key      | String | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名<br>examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg 中，对象键为 doc/pic.jpg |    是    |
| VersionId | String | 删除文件的版本号 |  否  |

#### 返回结果示例

```php
Guzzle\Service\Resource\Model Object
(
    [structure:protected] => 
    [data:protected] => Array
        (
            [Deleted] => Array
                (
                    [0] => Array
                        (
                            [Key] => exampleobject1
                        )
                )
            [Errors] => Array
                (
                    [0] => Array
                        (
                            [Key] => exampleobject2
                            [Code] => 
                            [Message] => 
                        )
                )
            [RequestId] => NWNhZWYzYWNfMTlhYTk0MGFfNGRjX2MzZTVhOQ==
        )
）
```
#### 返回结果说明

| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Deleted | Array | 成功删除的对象的列表   | 无 |
| Errors | Array | 失败删除的对象的列表 | 无 |
| Key | String | 对象键 | Deleted/Errors |
| Code | String | 失败错误码 | Errors|
| Message | String | 失败错误信息 | Errors |


## 分块操作

### 查询分片上传

#### 功能说明

查询指定存储桶中正在进行的分片上传（List Multipart Uploads）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model listMultipartUploads(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->listMultipartUploads(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Delimiter' => '/',
        'EncodingType' => 'url',
        'KeyMarker' => 'string',
        'UploadIdMarker' => 'string',
        'Prefix' => 'prfix',
        'MaxUploads' => 1000,
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 必填          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 是 |
| Delimiter | String | 默认为空，设置分隔符，比如设置`/`来模拟文件夹    | 否 |
| EncodingType | String | 默认不编码，规定返回值的编码方式，可选值：url    | 否 |
| KeyMarker | String |	标记返回 parts 的 list 的起点位置        | 否 |
| UploadIdMarker | String |	标记返回 parts 的 list 的起点位置     | 否 |
| Prefix | String | 默认为空，对 parts 的 key 进行筛选，匹配指定前缀（prefix）的 objects        | 否  |
| MaxUploads | Int | 最多返回的 parts 数量，默认为最大的1000 | 否 |

#### 返回结果示例

```php
Guzzle\Service\Resource\Model Object
(
    [structure:protected] => 
    [data:protected] => Array
        (
            [Bucket] => examplebucket-1250000000
            [EncodingType] => 
            [KeyMarker] => 
            [UploadIdMarker] => 
            [MaxUploads] => 1000
            [Prefix] => 
            [IsTruncated] => 
            [Uploads] => Array
                (
                    [0] => Array
                        (
                            [Key] => exampleobject
                            [UploadId] => 1551693693b1e6d0e00eec30c534059865ec89c9393028b60bfaf167e9420524b25eeb2940
                            [Initiator] => Array
                                (
                                    [ID] => qcs::cam::uin/100000000001:uin/100000000001
                                    [DisplayName] => 100000000001
                                )

                            [Owner] => Array
                                (
                                    [ID] => qcs::cam::uin/100000000001:uin/100000000001
                                    [DisplayName] => 100000000001
                                )

                            [StorageClass] => STANDARD
                            [Initiated] => 2019-03-04T10:01:33.000Z
                        )

                    [1] => Array
                        (
                            [Key] => exampleobject
                            [UploadId] => 155374001100563fe0e9d37964d53077e54e9d392bce78f630359cd3288e62acee2b719534
                            [Initiator] => Array
                                (
                                    [ID] => qcs::cam::uin/100000000001:uin/100000000001
                                    [DisplayName] => 100000000001
                                )

                            [Owner] => Array
                                (
                                    [ID] => qcs::cam::uin/100000000001:uin/100000000001
                                    [DisplayName] => 100000000001
                                )

                            [StorageClass] => STANDARD
                            [Initiated] => 2019-03-28T02:26:51.000Z
                        )

                )

            [RequestId] => NWNhNDJmNzBfZWFhZDM1MGFfMjYyM2FfMWIyNzhh
        )

)
```
#### 返回结果说明

| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 无 |
| IsTruncated | Int | 表示返回的 objects 否被截断 | 无 |
| Uploads | Array | 返回的分块列表 | 无 |
| Upload | Array | 返回的分块属性 | Uploads |
| Key | String | 对象健名 | Upload |
| UploadId | String | 对象的分块上传 ID | Upload |
| Initiator | String | 初始化该分片的操作者 | Upload |
| Owner | String | 分块拥有者 | Upload |
| StorageClass | String | 分块存储类型 | Upload |
| Initiated | String | 分块初始化时间 | Upload |


### 分片上传对象

分片上传对象可包括的操作：

- 分片上传对象： 初始化分片上传，  上传分片块， 完成分块上传。
- 分片续传：查询已上传块， 上传分片块，完成分块上传。
- 删除已上传分片块。

### <span id = "INIT_MULIT_UPLOAD"> 初始化分片上传 </span>

#### 功能说明

初始化 Multipart Upload 上传操作（Initiate Multipart Upload）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model createMultipartUpload(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->createMultipartUpload(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Key' => 'exampleobject',
        /*  
        'CacheControl' => 'string',
        'ContentDisposition' => 'string',
        'ContentEncoding' => 'string',
        'ContentLanguage' => 'string',
        'ContentLength' => integer,
        'ContentType' => 'string',
        'Expires' => 'string',
        'Metadata' => array(
            'string' => 'string',
        ),
        'StorageClass' => 'string'
        */
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 必填          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 是 |
| Key | String | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名<br>examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg 中，对象键为 doc/pic.jpg    | 是 |
| CacheControl | String |	缓存策略，设置 Cache-Control | 否 |
| ContentDisposition | String | 文件名称，设置 Content-Disposition  | 否  |
| ContentEncoding | String | 编码格式，设置 Content-Encoding | 否 |
| ContentLanguage | String | 语言类型，设置 Content-Language | 否 |
| ContentLength | Int | 设置传输长度 | 否 |
| ContentType | String | 	内容类型，设置 Content-Type | 否 |
| Expires | String | 设置 Content-Expires | 否 |
| Metadata | Array | 用户自定义的文件元信息 | 否 |
| StorageClass | String | 文件的存储类型，STANDARD 、 STANDARD_IA 、 ARCHIVE，默认值：STANDARD | 否 |
| ContentMD5 | String | 设置上传文件的 MD5 值用于校验 | 否 |
| ServerSideEncryption | String | 服务端加密方法 | 否 |

#### 返回结果示例

```php
Guzzle\Service\Resource\Model Object
(
    [structure:protected] => 
    [data:protected] => Array
        (
            [Bucket] => examplebucket-1250000000
            [Key] => exampleobject
            [UploadId] => 1554277569b3e83df05c730104c325eb7b56000449fb7d51300b0728aacde02a6ea7f6c033
            [RequestId] => NWNhNDY0YzFfMmZiNTM1MGFfNTM2YV8xYjliMTg=
        )

)
```
#### 返回结果说明

| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 无 |
| Key | String | 对象键 | 无 |
| UploadId | String | 对象分块上传的ID | 无 |

### <span id = "LIST_MULIT_UPLOAD"> 查询已上传块 </span>

#### 功能说明

查询特定分块上传操作中的已上传的块（List Parts）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model listParts(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->listParts(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Key' => 'exampleobject',
        'UploadId' => 'NWNhNDY0YzFfMmZiNTM1MGFfNTM2YV8xYjliMTg',
        'PartNumberMarker' => 1,
        'MaxParts' => 1000,
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 必填          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 是 |
| Key | String | 对象键 | 是 |
| UploadId | String | 对象分块上传的 ID | 是 |
| PartNumberMarker | Int | 标记返回 parts 的 list 的起点位置 | 否 |
| MaxParts | Int | 最多返回的 parts 数量，默认最大值为1000 | 否 |

#### 返回结果示例

```php
Guzzle\Service\Resource\Model Object
(
    [structure:protected] => 
    [data:protected] => Array
        (
            [Bucket] => examplebucket-1250000000
            [Key] => exampleobject
            [UploadId] => 1554279643cf19d71bb5fb0d29613e5541131f3a96387d9e168cd939c23a3d608c9eb94707
            [Owner] => Array
                (
                    [ID] => 1250000000
                    [DisplayName] => 1250000000
                )
            [PartNumberMarker] => 1
            [Initiator] => Array
                (
                    [ID] => qcs::cam::uin/100000000001:uin/100000000001
                    [DisplayName] => 100000000001
                )
            [StorageClass] => Standard
            [MaxParts] => 1000
            [IsTruncated] => 
            [Parts] => Array
                (
                    [0] => Array
                        (
                            [PartNumber] => 2
                            [LastModified] => 2019-04-03T08:21:28.000Z
                            [ETag] => "b948e77469189ac94b98e09755a6dba9"
                            [Size] => 1048576
                        )
                    [1] => Array
                        (
                            [PartNumber] => 3
                            [LastModified] => 2019-04-03T08:21:22.000Z
                            [ETag] => "9e5060e2994ec8463bfbebd442fdff16"
                            [Size] => 1048576
                        )                       
                )
            [RequestId] => NWNhNDZkNTJfOGNiMjM1MGFfMTRlYl8xYmJiOTU=
        )

)
```
#### 返回结果说明

| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 无 |
| Key | String | 对象键 | 无 |
| UploadId | String | 对象分块上传的 ID | 无 |
| IsTruncated | Int | 表示返回的 objects 否被截断 | 无 |
| PartNumberMarker | Int | 标记返回 parts 的 list 的起点位置 | 无 |
| MaxParts | Int | 最多返回的 parts 数量，默认最大值为1000 | 无 |
| Initiator | String | 初始化该分片的操作者 | 无  |
| Parts | Array | 返回的分块列表 | 无 |
| Part | Array | 返回的分块属性 | Parts |
| PartNumber | Int | 分块标号 | Part |
| LastModified | String | 分块的最后上传时间 | Part |
| ETag | String | 分块的 MD5 值 | Part |
| Size | String | 分块的大小 | Part |

### <span id = "MULIT_UPLOAD_PART"> 上传分块 </span>

分块上传文件（Upload Part）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model uploadPart(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->uploadPart(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Key' => 'exampleobject', 
        'Body' => 'string',
        'UploadId' => 'NWNhNDY0YzFfMmZiNTM1MGFfNTM2YV8xYjliMTg',
        'PartNumber' => integer,
        /*
        'ContentMD5' => 'string',
        'ContentLength' => integer,
        */
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}

```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 必填          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 是 |
| Key | String | 对象键 | 是 |
| UploadId | String | 对象分块上传的 ID | 是 |
| Body | File/String | 上传的内容 | 是 |
| PartNumber | Int | 上传分块的编号 | 是 |
| ContentLength | Int | 设置传输长度 | 否 |
| ContentMD5 | String | 设置上传文件的 MD5 值用于校验 | 否 |

#### 返回结果示例

```php
Guzzle\Service\Resource\Model Object
(
    [structure:protected] => 
    [data:protected] => Array
        (
            [ETag] => "96e79218965eb72c92a549dd5a330112"
            [RequestId] => NWNhNDdjYWFfNjNhYjM1MGFfMjk2NF8xY2ViMWM=
        )

)
```
#### 返回结果说明

| 参数名称            | 类型 | 描述                               | 父节点          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| ETag | String | 分块的 MD5 值 | 无 |

### <span id = "COMPLETE_MULIT_UPLOAD"> 完成分块上传 </span>

#### 功能说明

完成整个文件的分块上传（Complete Multipart Upload）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model completeMultipartUpload(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->completeMultipartUpload(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Key' => 'exampleobject', 
        'UploadId' => 'string',
        'Parts' => array(
            array(
                'ETag' => 'string',
                'PartNumber' => integer,
            ),  
            array(
                'ETag' => 'string',
                'PartNumber' => integer,
            )), 
            // ... repeated
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 必填          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 是 |
| Key | String | 对象键 | 是 |
| UploadId | String | 对象分块上传的 ID | 是 |
| Parts | Array | 分块信息列表 | 是 |
| Part | Array | 上传分块的内容信息 | 是 |
| ETag | String | 分块内容的 MD5 | 是 |
| PartNumber | Int | 分块编号 | 是 |


### <span id = "ABORT_MULIT_UPLOAD"> 终止分块上传 </span>

#### 功能说明

终止一个分块上传操作并删除已上传的块（Abort Multipart Upload）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model abortMultipartUpload(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->abortMultipartUpload(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Key' => 'exampleobject', 
        'UploadId' => 'string',
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 必填    |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID              | 是 |
| Key | String | 对象键 | 是 |
| UploadId | String | 对象分块上传的 ID | 是 |


## 其他操作

### 恢复归档对象 

#### 功能说明

将归档类型的对象取回访问（POST Object restore）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model restoreObject(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->putObject(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Key' => 'exampleobject',
        'Days' => integer,
        'CASJobParameters' => array(
            'Tier' =>'string'
        )    
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称            | 类型 | 描述                               | 必填          |
| ------------------- | -------- | ---------------------------------- | ------------- |
| Bucket | String | 存储桶名称，格式：BucketName-APPID                         | 是 |
| Key | String | 对象键 | 是 |
| Days | String | 设置临时副本的过期时间，单位(天) | 是 |
| CASJobParameters | Array | 恢复信息 | 是 |
| Tier | String | 恢复数据时，Tier 可以指定为 CAS 支持的三种恢复类型，分别为 Expedited、Standard、Bulk | 是 |

### 设置对象 ACL

#### 功能说明

设置指定对象访问权限控制列表（ACL）（PUT Object acl）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model putObjectAcl(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->putObjectAcl(array(
        'Bucket' => 'examplebucket-1250000000', //格式：BucketName-APPID
        'Key' => 'exampleobject',
        'ACL' => 'private',
        'Grants' => array(
            array(
                'Grantee' => array(
                    'DisplayName' => 'qcs::cam::uin/100000000001:uin/100000000001',
                    'ID' => 'qcs::cam::uin/100000000001:uin/100000000001',
                    'Type' => 'CanonicalUser',
                ),  
                'Permission' => 'FULL_CONTROL',
            ),  
            // ... repeated
        ),  
        'Owner' => array(
            'DisplayName' => 'qcs::cam::uin/100000000001:uin/100000000001',
            'ID' => 'qcs::cam::uin/100000000001:uin/100000000001',
        )));
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo "$e\n";
}
```

#### 参数说明

| 参数名称    | 类型   | 描述                                                         | 必填          |
| ----------- | ------ | ------------------------------------------------------------ | --------------- |
| Bucket      | String | 存储桶名称，格式：BucketName-APPID                           | 是              |
| Key | String | 对象键 | 是 |
| Grants      | Array  | ACL权限列表                                                  | 否              |
| Grant       | Array  | ACL权限信息                                                  | 否          |
| Grantee     | Array  | ACL权限信息                                                  | 否           |
| Type        | String | 所有者权限类型                                               | 否         |
| Permission  | String | 权限类型，可选值: FULL_CONTROL 、WRITE 、READ          | 否           |
| ACL         | String | 整体权限类型，可选值: private 、 public-read | 否              |
| Owner       | String | 存储桶所有者信息                                             | 否              |
| DisplayName | String | 权限所有者的名字信息                                         | 否 |
| ID          | String | 权限所有者 ID                                                 | 否 |


### 获取对象 ACL

#### 功能说明

获取指定对象的访问权限控制列表（ACL）（GET Object acl）。

#### 方法原型

```php
public Guzzle\Service\Resource\Model getObjectAcl(array $args = array());
```

#### 请求示例

```php
try {
    $result = $cosClient->getObjectAcl(array(
        'Bucket' => 'examplebucket-1250000000' //格式：BucketName-APPID
        'Key' => 'exampleobject',
    )); 
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 返回结果示例

```php
Array
(
    [data:protected] => Array
        (
            [Owner] => Array
                (
                    [ID] => qcs::cam::uin/100000000001:uin/100000000001
                    [DisplayName] => qcs::cam::uin/100000000001:uin/100000000001
                )

            [Grants] => Array
                (
                    [0] => Array
                        (
                            [Grantee] => Array
                                (
                                    [ID] => qcs::cam::uin/100000000001:uin/100000000001
                                    [DisplayName] => qcs::cam::uin/100000000001:uin/100000000001
                                )

                            [Permission] => FULL_CONTROL
                        )

                )

            [RequestId] => NWE3YzhjMTRfYzdhMzNiMGFfYjdiOF8yYzZmMzU=
        )
)
```

#### 返回结果说明

| 参数名称    | 类型   | 描述                                            | 父节点          |
| ----------- | ------ | ----------------------------------------------- | --------------- |
| Grants      | Array  | ACL权限列表                                     | 无              |
| Grant       | Array  | ACL权限信息                                     | Grants          |
| Grantee     | Array  | ACL权限信息                                     | Grant           |
| Permission  | String | 权限类型，可选值: FULL_CONTROL 、WRITE 、 READ | Grant           |
| Owner       | String | 存储桶所有者信息                                | 无              |
| DisplayName | String | 权限所有者的名字信息                            | Grantee / Owner |
| ID          | String | 权限所有者 ID                                    | Grantee / Owner |


## 高级接口（推荐）
该小节主要讲述由 COS 提供的封装了上传和复制操作的高级接口，用户只需要设置相应的参数，该接口内部会根据文件大小决定是进行简单上传（复制）还是分片上传（复制），使用接口前请确认已完成了 [快速入门](https://cloud.tencent.com/document/product/436/12266) 中指引的初始化步骤。


### 复合上传

#### 功能说明

该接口内部会根据文件大小，对小文件调用简单上传接口，对大文件调用分块上传接口。

#### 请求示例

```php
try {
    $result = $cosClient->Upload(
        $bucket = 'examplebucket-1250000000', //格式：BucketName-APPID
        $key = 'exampleobject',
        $body = fopen('/data/exampleobject', 'rb')
        /*
        $options = array(
            'ACL' => 'string',
            'CacheControl' => 'string',
            'ContentDisposition' => 'string',
            'ContentEncoding' => 'string',
            'ContentLanguage' => 'string',
            'ContentLength' => integer,
            'ContentType' => 'string',
            'Expires' => 'string',
            'GrantFullControl' => 'string',
            'GrantRead' => 'string',
            'GrantWrite' => 'string',
            'Metadata' => array(
                'string' => 'string',
            ),
            'ContentMD5' => 'string',
            'ServerSideEncryption' => 'string',
            'StorageClass' => 'string'
        )
        */
    );
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

### 复合复制

#### 功能说明

该接口内部会根据文件大小，对小文件调用设置对象复制接口，对大文件调用分块复制接口。

#### 请求示例

```php
try {
    $result = $cosClient->Copy(
        $bucket = 'examplebucket-1250000000', //格式：BucketName-APPID
        $key = 'exampleobject',
        $copysource = 'examplebucket2-1250000000.cos.ap-guangzhou.myqcloud.com/exampleobject'
        /*
        $options = array(
            'ACL' => 'string',
            'MetadataDirective' => 'string',
            'CacheControl' => 'string',
            'ContentDisposition' => 'string',
            'ContentEncoding' => 'string',
            'ContentLanguage' => 'string',
            'ContentLength' => integer,
            'ContentType' => 'string',
            'Expires' => 'string',
            'GrantFullControl' => 'string',
            'GrantRead' => 'string',
            'GrantWrite' => 'string',
            'Metadata' => array(
                'string' => 'string',
            ),
            'ContentMD5' => 'string',
            'ServerSideEncryption' => 'string',
            'StorageClass' => 'string'
        )
        */
    );
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```
