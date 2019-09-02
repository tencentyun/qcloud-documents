## 基本API描述

COS XML API Python SDK 操作成功会返回一个 dict 或者 None，失败会抛出异常（CosClientError 和 CosServiceError）。异常类会提供相关的错误信息，详见文末的异常类型介绍。
> 关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)

### 创建 Bucket

#### 功能说明

在指定账号下创建一个新的 Bucket，当 Bucket 已存在时会返回错误。

#### 方法原型

```
create_bucket(Bucket, **kwargs)
```
#### 请求示例

```python
response = client.create_bucket(
    Bucket='test01',
    ACL='private',
    GrantFullControl='string',
    GrantRead='string',
    GrantWrite='string'	
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket |待创建的 Bucket 名称，由数字和小写字母以及中划线 "-" 构成|String| 是|
| ACL |设置 Bucket 的 ACL，如 'private，public-read'，'public-read-write' |String| 否|
| GrantFullControl |赋予指定账户对 Bucket 的读写权限|String|否|
|GrantRead |赋予指定账户对 Bucket 的读权限|String|否|
| GrantWrite|赋予指定账户对 Bucket 的写权限|String|否|

#### 返回结果说明
该方法返回值为 None。

### 删除 Bucket

#### 功能说明

在指定账号下删除一个已经存在的 Bucket，删除时 Bucket 必须为空。

#### 方法原型

```
delete_bucket(Bucket)
```
#### 请求示例

```python
response = client.delete_bucket(
    Bucket='test01'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket |待删除的 Bucket 名称，由数字和小写字母以及中划线 "-" 构成|String|是|

#### 返回结果说明
该方法返回值为 None。

### 设置 Bucket ACL 信息

#### 功能说明

设置 Bucket 的 ACL 信息， 通过 ACL，GrantFullControl，GrantRead，GrantWriteheader 传入 header 的方式来设置 ACL，或者通过 AccessControlPolicy 传入 body 来设置 ACL，两种方式只能选择一种，否则会返回冲突。

#### 方法原型

```
put_bucket_acl(self, Bucket, AccessControlPolicy={}, **kwargs)
```
#### 请求示例

```python
response = client.put_bucket_acl(
    Bucket='test01',
    ACL='private',
    GrantFullControl='string',
    GrantRead='string',
    GrantWrite='string',
    AccessControlPolicy={
        'Grant': [
            {
                'Grantee': {
                    'DisplayName': 'string',
                    'Type': 'string',
                    'ID': 'string',
                    'URI': 'string'
                },
                'Permission': 'string'
            },
        ],
        'Owner': {
            'DisplayName': 'string',
            'ID': 'string'
        }
    }
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket | Bucket 名称，由数字和小写字母以及中划线 "-" 构成|String|是|
| ACL | 设置 Bucket 的 ACL，如 'private，public-read'，'public-read-write' |String|否 |
| GrantFullControl |赋予指定账户对 Bucket 的读写权限|String|否 |
| GrantRead |赋予指定账户对 Bucket 的读权限|String|否 |
| GrantWrite |赋予指定账户对 Bucket 的写权限|String|否 |
| AccessControlPolicy| 赋予指定账户对 Bucket 的访问权限|Dict|否 |

#### 返回结果说明
该方法返回值为 None。

### 获取 Bucket ACL 信息

#### 功能说明

获取指定 Bucket 的 ACL 信息。

#### 方法原型

```
get_bucket_acl(self, Bucket, **kwargs)
```
#### 请求示例

```python
response = client.get_bucket_acl(
    Bucket='test01',
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket |Bucket 名称，由数字和小写字母以及中划线 "-" 构成|String|是|


#### 返回结果说明

Bucket ACL 信息，类型为 dict。
```python
{
    'Owner': {
        'DisplayName': 'string',
        'ID': 'string'
    },
    'Grant': [
        {
            'Grantee': {
                'DisplayName': 'string',
                'Type': 'string',
                'ID': 'string',
                'URI': 'string'
            },
            'Permission': 'string'
        },
    ]
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- | 
| Owner |Bucket 拥有者的信息，包括 DisplayName 和 ID|Dict|
| Grant |Bucket 权限授予者的信息，包括 Grantee和 Permission|List|
| Grantee |权限授予者的信息，包括 DisplayName，Type，ID 和 URI|Dict|
| DisplayName |权限授予者的名字|String|
| Type |权限授予者的类型，类型为 CanonicalUser 或者 Group|String|
| ID |Type 为 CanonicalUser时，对应权限授予者的 ID|String|
| URI |Type 为 Group时，对应权限授予者的 URI|String|
| Permission |授予者所拥有的Bucket的权限，可选值有FULL_CONTROL，WRITE，READ，分别对应读写权限、写权限、读权限|String|

### 设置 Bucket 跨域配置

#### 功能说明
设置指定 Bucket 的跨域资源配置。

#### 方法原型

```
put_bucket_cors(self, Bucket, CORSConfiguration={}, **kwargs)
```
#### 请求示例

```python
response = client.put_bucket_cors(
    Bucket='string',
    CORSConfiguration={
        'CORSRule': [
            {
                'ID': 'string',
                'MaxAgeSeconds': 100,
                'AllowedOrigin': [
                    'string',
                ],
                'AllowedMethod': [
                    'string',
                ],
                'AllowedHeader': [
                    'string',
                ],
                'ExposeHeader': [
                    'string',
                ]
            }
        ]
    },
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket |Bucket 名称，由数字和小写字母以及中划线 "-" 构成|String| 是|
| CORSRule |设置对应的跨域规则，包括 ID，MaxAgeSeconds，AllowedOrigin，AllowedMethod，AllowedHeader，ExposeHeader|List| 是|
| ID |设置规则的 ID|String|否|
| MaxAgeSeconds |设置 OPTIONS 请求得到结果的有效期|Int|否|
| AllowedOrigin |设置允许的访问来源，如 `"http://www.qcloud.com"`，支持通配符 * |Dict|是|
| AllowedMethod |设置允许的方法，如 GET，PUT，HEAD，POST，DELETE|Dict|是|
| AllowedHeader |设置请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 * |Dict|否|
| ExposeHeader |设置浏览器可以接收到的来自服务器端的自定义头部信息|Dict|否|

#### 返回结果说明
该方法返回值为 None。

### 获取 Bucket 跨域配置

#### 功能说明
获取指定 Bucket 的跨域资源配置。

#### 方法原型

```
get_bucket_cors(self, Bucket, **kwargs)
```
#### 请求示例

```python
response = client.get_bucket_cors(
    Bucket='string',
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket|Bucket 名称，由数字和小写字母以及中划线 "-" 构成|String| 是|

#### 返回结果说明

Bucket 跨域配置，类型为 dict。
```python
{
    'CORSRule': [
        {
            'ID': 'string',
            'MaxAgeSeconds': 100,
            'AllowedOrigin': [
                'string',
            ],
            'AllowedMethod': [
                'string',
            ],
            'AllowedHeader': [
                'string',
            ],
            'ExposeHeader': [
                'string',
            ],
        }
    ]
}
```

| 参数名称   | 参数描述   |类型 |
| -------------- | -------------- |---------- |
 | CORSRule  | 跨域规则，包括 ID，MaxAgeSeconds，AllowedOrigin，AllowedMethod，AllowedHeader，ExposeHeader |  List | 
 | ID  | 规则的 ID | String | 
 | MaxAgeSeconds  |  OPTIONS 请求得到结果的有效期 | String |
 | AllowedOrigin  | 允许的访问来源，如 `"http://www.qcloud.com"`，支持通配符 *  | Dict | 
 | AllowedMethod  |  允许的方法，如 GET，PUT，HEAD，POST，DELETE | Dict |
 | AllowedHeader  |请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 * |  Dict | 
 | ExposeHeader  | 浏览器可以接收到的来自服务器端的自定义头部信息 | Dict | 

### 删除 Bucket  跨域配置

#### 功能说明
删除指定 Bucket 的跨域资源配置。

#### 方法原型

```
delete_bucket_cors(self, Bucket, **kwargs)
```
#### 请求示例

```python
response = client.delete_bucket_cors(
    Bucket='string',
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket |Bucket 名称，由数字和小写字母以及中划线 "-" 构成|String| 是

#### 返回结果说明

该方法返回值为 None。

### 设置 Bucket 生命周期配置

#### 功能说明
设置指定 Bucket 的生命周期配置。

#### 方法原型

```
put_bucket_lifecycle(self, Bucket, LifecycleConfiguration={}, **kwargs)
```
#### 请求示例

```python
response = client.put_bucket_lifecycle(
    Bucket='string',
    LifecycleConfiguration={
        'Rule': [
            {
                'ID': 'string',
                'Filter': {
                    'Prefix': 'string',
                },
                'Status': 'string',
                'Expiration': {
                    'Days': 100,
                    'Date': 'string'
                },
                'Transition': {
                    'Days': 100,
                    'Date': 'string',
                    'StorageClass': 'string'
                },
                'NoncurrentVersionExpiration': {
                    'NoncurrentDays': 100
                },
                'NoncurrentVersionTransition': {
                    'NoncurrentDays': 100,
                    'StorageClass': 'string'
                },
                'AbortIncompleteMultipartUpload': {
                    'DaysAfterInitiation': 100
                }
            }
        ]   
    }
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 |  Bucket  | Bucket 名称，由数字和小写字母以及中划线 "-" 构成 | String |   是 | 
 |  Rule  |  设置对应的规则，包括 ID，Filter，Status，Expiration，Transition，NoncurrentVersionExpiration，NoncurrentVersionTransition，AbortIncompleteMultipartUpload | List |   是 |
 |  ID  |  设置规则的 ID | String |  否 |
 |  Filter  | 用于描述规则影响的 Object 集合 | Dict |  是 | 
 |  Status  | 设置 Rule 是否启用，可选值为 Enabled 或者 Disabled | Dict |  是 | 
 |  Expiration  |  设置 Object 过期规则，可以指定天数 Days 或者指定日期 Date | Dict |  否 |
 |  Transition  | 设置 Object 转换存储类型规则，可以指定天数 Days 或者指定日期 Date，StorageClass 可选 Standard_IA， Nearline | Dict |  否 | 
 |  NoncurrentVersionExpiration  | 设置非当前版本 Object 过期规则，可以指定天数 NoncurrentDays |  Dict |  否 |
 |  NoncurrentVersionTransition  | 设置非当前版本 Object 转换存储类型规则，可以指定天数 NoncurrentDays，StorageClass 可选 Standard_IA， Nearline | Dict |  否 | 
 |  AbortIncompleteMultipartUpload  |指明分块上传开始后多少天内必须完成上传 |  Dict |  否 | 


#### 返回结果说明

该方法返回值为 None。

### 获取 Bucket 生命周期配置

#### 功能说明
获取指定 Bucket 的生命周期配置。

#### 方法原型

```
get_bucket_lifecycle(self, Bucket, **kwargs)
```
#### 请求示例

```python
response = client.get_bucket_lifecycle(
    Bucket='string',
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket |Bucket 名称，由数字和小写字母以及中划线 "-" 构成|String|是 |

#### 返回结果说明

Bucket 跨域配置，类型为 dict。
```python
{
    'Rule': [
        {
            'ID': 'string',
            'Filter': {
                'Prefix': 'string',
            },
            'Status': 'string',
            'Expiration': {
                'Days': 100,
                'Date': 'string'
            },
            'Transition': {
                'Days': 100,
                'Date': 'string',
                'StorageClass': 'string'
            },
            'NoncurrentVersionExpiration': {
                'NoncurrentDays': 100
            },
            'NoncurrentVersionTransition': {
                'NoncurrentDays': 100,
                'StorageClass': 'string'
            },
            'AbortIncompleteMultipartUpload': {
                'DaysAfterInitiation': 100
            }
        }
    ]   
}
```

| 参数名称   | 参数描述   |类型 |
| -------------- | -------------- |---------- | 
 |  Rule  |  对应的规则，包括 ID，Filter，Status，Expiration，Transition，NoncurrentVersionExpiration，NoncurrentVersionTransition，AbortIncompleteMultipartUpload | List | 
 |  ID  | 规则的 ID | String | 
 |  Filter  |  必用于描述规则影响的 Object 集合 | Dict |
 |  Status  |  Rule 是否启用，可选值为 Enabled 或者 Disabled | Dict |
 |  Expiration  |Object 过期规则，可以指定天数 Days 或者指定日期 Date |  Dict | 
 |  Transition  | Object 转换存储类型规则，可以指定天数 Days 或者指定日期 Date，StorageClass 可选 Standard_IA， Nearline | Dict | 
 |  NoncurrentVersionExpiration  | 非当前版本 Object 过期规则，可以指定天数 NoncurrentDays |  Dict |
 |  NoncurrentVersionTransition  | 非当前版本 Object 转换存储类型规则，可以指定天数 NoncurrentDays，StorageClass 可选 Standard_IA， Nearline | Dict | 
 |  AbortIncompleteMultipartUpload  |  分块上传开始后多少天内必须完成上传 | Dict |

### 删除 Bucket 生命周期配置。

#### 功能说明

删除指定 Bucket 的生命周期配置。

#### 方法原型

```
delete_bucket_lifecycle(self, Bucket, **kwargs)
```
#### 请求示例

```python
response = client.delete_bucket_lifecycle(
    Bucket='string',
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket |Bucket 名称，由数字和小写字母以及中划线 "-" 构成|String|是 |

#### 返回结果说明

该方法返回值为 None。

### 简单文件上传

#### 功能说明

支持上传本地文件或输入流到指定的 Bucket 中。推荐上传不大于 20 MB 的小文件，单次上传大小限制为 5 GB，大文件上传请使用分块上传。

#### 方法原型

```
put_object(Bucket, Body, Key, **kwargs)
```
#### 请求示例

```python
response = client.put_object(
    Bucket='test01',
    Body='abc',
    Key='test.txt',
    ACL='private',
    GrantFullControl='string',
    GrantRead='string',
    GrantWrite='string',
    StorageClass='STANDARD',
    Expires='string'
    CacheControl='string',
    ContentType='string',
    ContentDisposition='string',
    ContentEncoding='string',
    ContentLanguage='string',
    ContentLength=123,
    ContentMD5='string',
    Metadata={
        'x-cos-meta-key1': 'value1',
        'x-cos-meta-key2': 'value2'
    }
)
```
#### 参数说明


| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 |  Bucket  |  Bucket 名称，由数字和小写字母以及中划线 "-" 构成 | String |   是 |
 |  Body  | 上传文件的内容，可以为文件流或字节流 |  file/String |  是 |
 |  Key  | 上传文件的路径名，默认从 Bucket 开始 | String |  是 | 
 |  ACL  | 设置文件的 ACL，如 'private，public-read'，'public-read-write' | String |   否 | 
 |  GrantFullControl  |赋予指定账户对文件的读写权限 |  String |  否 | 
 |  GrantRead  |  赋予指定账户对文件读权限 | String |  否 |
 |  GrantWrite  |  赋予指定账户对文件的写权限 | String |  否 |
 |  StorageClass  |  设置文件的存储类型，STANDARD,STANDARD_IA，NEARLINE，默认值：STANDARD | String |   否 |
 |  Expires  | 设置 Content-Expires | String|  否 | 
 |  CacheControl  |  缓存策略，设置 Cache-Control | String |   否 |
 |  ContentType  | 内容类型，设置 Content-Type |String |   否 |  
 |  ContentDisposition  |  文件名称，设置 Content-Disposition | String |   否 |
 |  ContentEncoding  |  编码格式，设置 Content-Encoding | String |   否 |
 |  ContentLanguage  |  语言类型，设置 Content-Language | String |   否 |
 |  ContentLength  | 设置传输长度 | Int |   否 | 
 |  ContentMD5  | 设置上传文件的 MD5 值用于校验 | String |   否 | 
 |  Metadata | 用户自定义的文件元信息 | Dict |   否 |

#### 返回结果说明
上传文件的属性，类型为 dict：

```python
{
    'ETag': 'string',
    'x-cos-expiration': 'string',
    'x-cos-version-id': 'string'
}
```


| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- |
|  ETag   |  上传文件的 MD5 值  | String  |
|  x-cos-expiration   | 设置生命周期后，返回文件过期规则  | String  | 
|  x-cos-version-id   |  设置版本管理后，返回文件版本  | String  |
	
### 文件下载

#### 功能说明
将指定 Bucket 中的文件下载到本地。

#### 方法原型

```
 get_object(Bucket, Key, **kwargs)
```
#### 请求示例

```python
response = client.get_object(
    Bucket='test01',
    Key='test.txt',
    Range='string',
    IfMatch='string',
    IfModifiedSince='string',
    IfNoneMatch='string',
    IfUnmodifiedSince='string',
    ResponseCacheControl='string',
    ResponseContentDisposition='string',
    ResponseContentEncoding='string',
    ResponseContentLanguage='string',
    ResponseContentType='string',
    ResponseExpires='string',
    VersionId='string'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 |  Bucket  |  Bucket 名称，由数字和小写字母以及中划线 "-" 构成 | String  |  是 | 
 |  Key  |  下载文件的路径名，默认从 Bucket 开始 | String  | 是 | 
 |  Range  |  设置下载文件的范围，格式为 `bytes 0-16086/16087`  | String  |  否 | 
 |  IfMatch  |  ETag 与指定的内容一致时才返回 |String  | 否 |  
 |  IfModifiedSince  |   在指定时间后被修改才返回 | String  | 否 |
 |  IfNoneMatch  |  ETag 与指定的内容不一致才返回 | String  | 否 | 
 |  IfUnmodifiedSince  |  文件修改时间早于或等于指定时间才返回 | String  | 否|
 |  ResponseCacheControl  |  设置响应头部 Cache-Control | String  | 否 | 
 |  ResponseContentDisposition  |  设置响应头部 Content-Disposition | String  | 否 | 
 |  ResponseContentEncoding  |   设置响应头部 Content-Encoding | String  | 否 |
 |  ResponseContentLanguage  |  设置响应头部 Content-Language | String  | 否 | 
 |  ResponseContentType  |   设置响应头部 Content-Type | String  | 否 |
 |  ResponseExpires  |设置响应头部 Content-Expires |   String  | 否 | 
 |  VersionId  | 指定下载文件的版本 |  String  | 否 | 

#### 返回结果说明

下载文件的 Body 和元信息，类型为 dict：

```python
{
    'Body': StreamBody(),
    'Accept-Ranges': 'bytes',
    'Content-Type': 'application/octet-stream',
    'Content-Length': '16807',
    'Content-Disposition': 'attachment; filename="filename.jpg"',
    'Content-Range': 'bytes 0-16086/16087',
    'ETag': '"9a4802d5c99dafe1c04da0a8e7e166bf"',
    'Last-Modified': 'Wed, 28 Oct 2014 20:30:00 GMT',
    'x-cos-version-id':'MTg0NDY3NDI1NjU0MDAwODY0NzI',
    'x-cos-object-type': 'normal',
    'x-cos-request-id': 'NTg3NzQ3ZmVfYmRjMzVfMzE5N182NzczMQ==',
    'x-cos-storage-class': 'STANDARD',
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- | 
 | Body  |  下载文件的内容，get_raw_stream 方法可以得到一个文件流，`get_stream_to_file` 方法可以将文件内容下载到指定本地文件中 | StreamBody |
 | 文件元信息  |  下载文件的元信息，包括 Etag 和 x-cos-request-id 等信息，也会返回设置的文件元信息 | String |

### 文件删除

#### 功能说明
将指定 Bucket 中的对应文件删除。

#### 方法原型

```
delete_object(Bucket, Key, **kwargs)
```
#### 请求示例

```python
response = client.delete_object(
    Bucket='test01',
    Key='test.txt'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  |Bucket 名称，由数字和小写字母以及中划线 "-" 构成 |  String |  是 | 
 | Key  | 删除文件的路径名，默认从 Bucket 开始 | String | 是 | 

#### 返回结果说明
该方法返回值为None。

### 获取文件属性
#### 功能说明
获取指定文件的元信息。

#### 方法原型

```
head_object(Bucket, Key, **kwargs)
```
#### 请求示例

```python
response = client.head_object(
    Bucket='test01',
    Key='test.txt',
    IfModifiedSince='string'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
  | Bucket   | Bucket 名称，由数字和小写字母以及中划线 "-" 构成  | String  |  是 | 
  | Key   |  文件的路径名，默认从 Bucket 开始  |String  | 是 |
  | IfModifiedSince   | 在指定时间后被修改才返回  | String  | 否 | 

#### 返回结果说明

获取文件的元信息，类型为 dict：

```python
{
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/octet-stream',
    'Content-Length': '16807',
    'ETag': '"9a4802d5c99dafe1c04da0a8e7e166bf"',
    'Last-Modified': 'Wed, 28 Oct 2014 20:30:00 GMT',
    'x-cos-version-id':'MTg0NDY3NDI1NjU0MDAwODY0NzI',
    'x-cos-object-type': 'normal',
    'x-cos-request-id': 'NTg3NzQ3ZmVfYmRjMzVfMzE5N182NzczMQ==',
    'x-cos-storage-class': 'STANDARD'
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- | 
| 文件元信息 |获取文件的元信息，包括 Etag 和 x-cos-request-id 等信息，也会包含设置的文件元信息| String|

### 获取文件列表
#### 功能说明
获取指定 Bucket 下的所有 Objects。

#### 方法原型

```
list_objects(Bucket, Delimiter="", Marker="", MaxKeys=1000, Prefix="", EncodingType="", **kwargs)
```
#### 请求示例

```python
response = client.list_objects(
    Bucket='test01',
    Delimiter='string',
    Marker='string',
    MaxKeys=100,
    Prefix='string',
    EncodingType='url'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket 名称，由数字和小写字母以及中划线 "-" 构成  | String  | 是| 
| Delimiter   |   默认为空，设置分隔符  | String|  否|
| Marker   |  默认以 UTF-8 二进制顺序列出条目，标记返回 objects 的 list 的起点位置  | String  |  否| 
| MaxKeys   | 最多返回的 objects 数量，默认为最大的 1000  | Int  |  否| 
| Prefix   |  默认为空，对 object 的 key 进行筛选，匹配 prefix 为前缀的 objects  | String  |  否| 
| EncodingType   |   默认不编码，规定返回值的编码方式，可选值：url  | String  | 否|

#### 返回结果说明

获取 objects 的元信息，类型为 dict：

```python
{
    'MaxKeys': '1000', 
    'Prefix': None, 
    'Name': 'test04-1252448703', 
    'Marker': None, 
    'IsTruncated': 'false',
    'EncodingType': 'url',
    'Contents':[
        {
            'ETag': '"a5b2e1cfb08d10f6523f7e6fbf3643d5"', 
            'StorageClass': 'STANDARD', 
            'Key': 'zh.cn.txt'
            'Owner': {ID': '1252448703'}, 
            'LastModified': '2017-08-08T09:43:35.000Z', 
            'Size': '23'
        }
    ],
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- | 
|Contents |包含所有 objects 元信息的 list，包括 'ETag'，'StorageClass'，'Key'，'Owner'，'LastModified'，'Size' 等信息|List| 

### 创建分块上传

#### 功能说明

创建一个新的分块上传任务，返回 UploadId。

#### 方法原型

```
create_multipart_upload(Bucket, Key, **kwargs):
```
#### 请求示例

```python
response = client.create_multipart_upload(
    Bucket='test01',
    Key='multipart.txt',
    StorageClass='STANDARD',
    Expires='string'
    CacheControl='string',
    ContentType='string',
    ContentDisposition='string',
    ContentEncoding='string',
    ContentLanguage='string',
    Metadata={
        'x-cos-meta-key1': 'value1',
        'x-cos-meta-key2': 'value2'
    }
)
# 获取UploadId供后续接口使用
uploadid = response['UploadId']
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  | Bucket 名称，由数字和小写字母以及中划线 "-" 构成 |  String |  是 |
 | Key  |  上传文件的路径名，默认从 Bucket 开始 | String | 是 |
 | StorageClass  | 设置文件的存储类型，STANDARD，STANDARD_IA，NEARLINE，默认值：STANDARD | String |  否 | 
 | Expires  |  设置 Content-Expires | String| 否 |
 | CacheControl  | 缓存策略，设置 Cache-Control | String |  否 | 
 | ContentType  | 内容类型，设置 Content-Type | String |  否 | 
 | ContentDisposition  | 文件名称，设置 Content-Disposition | String |  否 | 
 | ContentEncoding  | 编码格式，设置 Content-Encoding | String |  否 | 
 | ContentLanguage  | 语言类型，设置 Content-Language |  String |  否 |
 | Metadata |用户自定义的文件元信息 | Dict |  否 | 

#### 返回结果说明

获取分块上传的初始化信息，类型为 dict：

```python
{
    'UploadId': '150219101333cecfd6718d0caea1e2738401f93aa531a4be7a2afee0f8828416f3278e5570',
    'Bucket': 'test01-123456789', 
    'Key': 'multipartfile.txt' 
}

```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- |
|UploadId | 标识分块上传的 ID|String|
|Bucket |Bucket 名称，由 bucket-appid 组成|String|
|Key | 上传文件的路径名|String|

### 放弃分块上传

#### 功能说明
放弃一个分块上传任务，删除所有已上传的分块。

#### 方法原型

```
abort_multipart_upload(Bucket, Key, UploadId, **kwargs)
```
#### 请求示例

```python
response = client.abort_multipart_upload(
    Bucket='test01',
    Key='multipart.txt',
    UploadId=uploadid
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket |Bucket 名称，由数字和小写字母以及中划线 "-" 构成|String| 是|
|Key |上传文件的路径名，默认从 Bucket 开始|String| 是|
|UploadId |标识分块上传的 ID|String| 是|

#### 返回结果说明
该方法返回值为 None。

### 上传分块
#### 功能说明
上传一个分块到指定的 UploadId 中，单个大小不得超过 5 GB。

#### 方法原型

```
upload_part(Bucket, Key, Body, PartNumber, UploadId, **kwargs)
```
#### 请求示例

```python
# 注意，上传分块的块数最多 10000 块
response = client.upload_part(
    Bucket='test01',
    Key='multipart.txt',
    Body='A'*1024*1024*10,
    PartNumber=1,
    UploadId=uploadid,
    ContentLength=123,
    ContentMD5='string'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  | Bucket 名称，由数字和小写字母以及中划线 "-" 构成 | String |  是|
 | Key  | 上传分块的路径名，默认从 Bucket 开始 | String |  是|
 | Body  | 上传分块的内容，可以为本地文件流或输入流 | String |  是|
 | PartNumber  |标识上传分块的序号 |  String |  是|
 | UploadId  | 标识分块上传的 ID | String |  是|
 | ContentLength  |设置传输长度 |  Int |  否|
 | ContentMD5  | 设置上传文件的 MD5 值用于校验 | String |  否|
 
#### 返回结果说明

上传分块的属性，类型为 dict：

```python
{
    'ETag': 'string'
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- | 
| ETag |上传分块的 MD5 值。|String|

### 列出上传分块
#### 功能说明
列出指定 UploadId 中已经上传的分块的信息。

#### 方法原型

```
list_parts(Bucket, Key, UploadId, MaxParts=1000, PartNumberMarker=0, EncodingType='', **kwargs)
```
#### 请求示例

```python
response = client.list_parts(
    Bucket='test01',
    Key='multipart.txt',
    UploadId=uploadid,
    MaxParts=1000,
    PartNumberMarker=100,
    EncodingType='url'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket |Bucket 名称，由数字和小写字母以及中划线 "-" 构成|String| 是|
|Key |上传分块的路径名，默认从 Bucket 开始|String| 是|
|UploadId |标识分块上传的 ID|String| 是|
|MaxParts |最多返回的分块的数量，默认为最大的 1000|Int| 否|
|PartNumberMarker |默认为 0，从第一块列出分块，从 PartNumberMarker 下一个分块开始列出|Int| 否|
|EncodingType |默认不编码，规定返回值的编码方式，可选值：url |String|否|

#### 返回结果说明

所有上传分块的信息，类型为 dict：

```python
{
    'Initiator': {
        'DisplayName': '3333333333', 
        'ID': 'qcs::cam::uin/3333333333:uin/3333333333'
    }, 
    'Bucket': 'test01-123456789', 
    'Part': [
        {
            'LastModified': '2017-08-08T11:40:48.000Z',
            'PartNumber': '1',
            'ETag': '"8b8378787c0925f42ccb829f6cc2fb97"',
            'Size': '10485760'
        },
    ], 
    'UploadId': '1502192444bdb382add546a35b2eeab81e06ed84086ca0bb75ea45ca7fa073fa9cf74ec4f2', 
    'Encoding-type': None, 
    'Key': 'multipartfile.txt', 
    'Owner': {
        'DisplayName': '124564654654',
        'ID': '124564654654'
    }, 
    'MaxParts': '1000',
    'IsTruncated': 'false',
    'PartNumberMarker': '0', 
    'StorageClass': 'Standard'
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- | 
 |  Bucket  |   Bucket 名称 | String |
 |  Part |上传分块的相关信息，包括 ETag，PartNumber，Size，LastModified | String | 
 |  UploadId  |  标识分块上传的 ID | String | 
 |  Key  | 上传分块的路径名 | String |  

### 完成分块上传

#### 功能说明

组装指定 UploadId 中所有的分块为一个完整的文件，文件最终大小必须大于 1 MB，否则会返回错误。

#### 方法原型

```
complete_multipart_upload(Bucket, Key, UploadId, MultipartUpload={}, **kwargs)
```
#### 请求示例

```python
response = client.complete_multipart_upload(
    Bucket='test01',
    Key='multipart.txt',
    UploadId=uploadid,
    MultipartUpload={
        'Part': [
            {
                'ETag': 'string',
                'PartNumber': 1
            },
            {
                'ETag': 'string',
                'PartNumber': 2
            },
        ]
    },
)

```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|  Bucket  | Bucket 名称，由数字和小写字母以及中划线 "-" 构成 | String |   是| 
|  Key  | 上传分块的路径名，默认从 Bucket 开始 | String  |   是| 
|  UploadId  | 标识分块上传的 ID | String  |   是| 
|  MultipartUpload  |所有分块的 ETag 和 PartNumber 信息 |  Dict |   是| 

#### 返回结果说明

组装后的文件的相关信息，类型为 dict：

```python
{
    'ETag': '"3f866d0050f044750423e0a4104fa8cf-2"', 
    'Bucket': 'test01', 
    'Location': 'test01-123456789.cn-north.myqcloud.com/multipartfile.txt', 
    'Key': 'multipartfile.txt'
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- | 
 |  ETag  |组装后的文件的 MD5 值 |  String | 
 |  Bucket  |Bucket 名称，由数字和小写字母以及中划线 "-" 构成 |  String | 
 |  Location  | URL 地址 |  String | 
 |  Key  |  上传分块的路径名 | String |

### 设置 Object ACL 信息

#### 功能说明

设置文件的 ACL 信息，通过 ACL，GrantFullControl，GrantRead，GrantWriteheader 传入 header 的方式来设置 ACL，或者通过 AccessControlPolicy 传入 body 来设置 ACL，两种方式只能选择一种，否则会返回冲突。

#### 方法原型

```
put_object_acl(self, Bucket, Key, AccessControlPolicy={}, **kwargs)
```
#### 请求示例

```python
response = client.put_object_acl(
    Bucket='test01',
    Key='test.txt',
    ACL='private',
    GrantFullControl='string',
    GrantRead='string',
    GrantWrite='string',
    AccessControlPolicy={
        'Grant': [
            {
                'Grantee': {
                    'DisplayName': 'string',
                    'Type': 'string',
                    'ID': 'string',
                    'URI': 'string'
                },
                'Permission': 'string'
            },
        ],
        'Owner': {
            'DisplayName': 'string',
            'ID': 'string'
        }
    }
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   |  Bucket 名称，由数字和小写字母以及中划线 "-" 构成 | String  |  是  |
| Key   | 待设置 ACL 信息的文件路径 | String  |  是  | 
| ACL   | 设置文件的 ACL，如 'private，public-read'，'public-read-write' | String  |  否  | 
| GrantFullControl   |  赋予指定账户对文件的读写权限 | String  | 否  |
| GrantRead   |赋予指定账户对文件读权限 |  String  | 否  | 
| GrantWrite   | 赋予指定账户对文件的写权限 | String  | 否  | 
| AccessControlPolicy   | 赋予指定账户对文件的访问权限 | Dict  | 否  | 


#### 返回结果说明

该方法返回值为 None。

### 获取 Object ACL 信息

#### 功能说明
获取指定文件的 ACL 信息。

#### 方法原型

```
get_object_acl(self, Bucket, Key, **kwargs)
```
#### 请求示例

```python
response = client.get_object_acl(
    Bucket='test01',
    Key='test.txt'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket|Bucket 名称，由数字和小写字母以及中划线 "-" 构成|String| 是|
|Key |待获取 ACL 信息的文件路径|String|是|


#### 返回结果说明

Bucket ACL 信息，类型为 Dict。
```python
{
    'Owner': {
        'DisplayName': 'string',
        'ID': 'string'
    },
    'Grant': [
        {
            'Grantee': {
                'DisplayName': 'string',
                'Type': 'string',
                'ID': 'string',
                'URI': 'string'
            },
            'Permission': 'string'
        },
    ]
}
```

| 参数名称   | 参数描述   |类型 |
| -------------- | -------------- |---------- | 
 |  Owner  | 文件拥有者的信息，包括 DisplayName 和 ID | Dict | 
 |  Grant  | 文件权限授予者的信息，包括 Grantee 和 Permission | List | 
 |  Grantee  |文件权限授予者的信息，包括 DisplayName，Type，ID 和 URI |  Dict | 
 |  DisplayName  |  权限授予者的名字 | String |
 |  Type  |  权限授予者的类型，类型为 CanonicalUser 或者 Group | String |
 |  ID  | Type 为 CanonicalUser 时，对应权限授予者的 ID | String | 
 |  URI  |Type 为 Group 时，对应权限授予者的 URI |  String | 
 |  Permission  |  授予者所拥有的文件的权限，可选值有 FULL_CONTROL，WRITE，READ，分别对应读写权限、写权限、读权限 | String |

### 文件拷贝

#### 功能说明
将一个文件从源路径复制到目标路径，在拷贝的过程中，文件元属性和 ACL 可以被修改。

#### 方法原型

```
copy_object(self, Bucket, Key, CopySource, CopyStatus='Copy', **kwargs)
```
#### 请求示例

```python
response = client.copy_object(
    Bucket='test01',
    Key='test.txt',
    CopySource={
        'Appid': '1252408340',
        'Bucket': 'test02', 
        'Key': 'test.txt', 
        'Region': 'ap-guangzhou'
    }
    CopyStatus='Copy',
    ACL='private',
    GrantFullControl='string',
    GrantRead='string',
    GrantWrite='string',
    StorageClass='STANDARD',
    Expires='string'
    CacheControl='string',
    ContentType='string',
    ContentDisposition='string',
    ContentEncoding='string',
    ContentLanguage='string',
    Metadata={
        'x-cos-meta-key1': 'value1',
        'x-cos-meta-key2': 'value2'
    }
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 |  Bucket  |  Bucket 名称，由数字和小写字母以及中划线 "-" 构成 | String|  是 |
 |  Key  | 上传文件的路径名，默认从 Bucket 开始 | String| 是 | 
 |  CopySource  | 描述拷贝源文件的路径，包含 Appid、Bucket、Key、Region |  Dict | 是 |
 |  CopyStatus  |  可选值为 'COPY','REPLACE'，设置为 'COPY' 时，忽略设置的用户元数据信息直接复制，设置为 'Replaced' 时，按设置的元信息修改元数据，当目标路径和源路径一样时，必须设置为'REPLACE' | String| 是 |
 |  ACL  | 设置文件的 ACL，如 'private，public-read'，'public-read-write' | String|  否 | 
 |  GrantFullControl  |  赋予指定账户对文件的读写权限 | String| 否 |
 |  GrantRead  |  赋予指定账户对文件读权限 | String| 否 |
 |  GrantWrite  | 赋予指定账户对文件的写权限 | String| 否 | 
 |  StorageClass  |  设置文件的存储类型，STANDARD,STANDARD_IA，NEARLINE，默认值：STANDARD | String|  否 |
 |  Expires  | 设置 Content-Expires | String| 否 | 
 |  CacheControl  | 缓存策略，设置 Cache-Control | String|  否 | 
 |  ContentType  | 内容类型，设置 Content-Type | String|  否 | 
 |  ContentDisposition  |  文件名称，设置 Content-Disposition | String|  否 |
 |  ContentEncoding  | 编码格式，设置 Content-Encoding | String|  否 | 
 |  ContentLanguage  |  语言类型，设置 Content-Language | String|  否 |
 |  Metadata |用户自定义的文件元信息 | Dict |  否 | 
#### 返回结果说明

上传文件的属性，类型为 dict：

```python
{
    'ETag': 'string',
    'LastModified': 'string',
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- | 
| ETag |拷贝文件的 MD5 值|String|
| LastModified |拷贝文件的最后一次修改时间|String|

## 异常类型
包括 CosClientError 和 CosServiceError，分别对应 SDK 客户端错误和 COS 服务端错误。

### CosClientError
CosClientError 一般指如 timeout 引起的客户端错误，用户捕获后可以选择重试或其它操作。

### CosServiceError
CosServiceError 提供服务端返回的具体信息。

```python
#except CosServiceError as e
e.get_origin_msg()  # 获取原始错误信息，格式为XML
e.get_digest_msg()  # 获取处理过的错误信息，格式为dict
e.get_status_code() # 获取http错误码（如4XX,5XX)
e.get_error_code()  # 获取Cos定义的错误码
e.get_error_msg()   # 获取Cos错误码的具体描述
e.get_trace_id()    # 获取请求的trace_id
e.get_request_id()  # 获取请求的request_id
e.get_resource_location() # 获取URL地址
```