COS XML API Python SDK 操作成功会返回一个 dict 或者 None，失败会抛出异常（CosClientError 和 CosServiceError）。异常类会提供相关的错误信息，详见文末的异常类型介绍。
>?关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)。

## Bucket API 描述
### 创建 Bucket

#### 功能说明

创建一个存储桶（Put Bucket）。

#### 方法原型

```
create_bucket(Bucket, **kwargs)
```
#### 请求示例

```python
response = client.create_bucket(
    Bucket='examplebucket-1250000000',
    ACL='private'|'public-read'|'public-read-write',
    GrantFullControl='string',
    GrantRead='string',
    GrantWrite='string'	
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket |待创建的 Bucket 名称，由 BucketName-APPID 构成|String| 是|
| ACL |设置 Bucket 的 ACL，如 'private'，'public-read'，'public-read-write' |String| 否|
| GrantFullControl |赋予指定账户对 Bucket 的所有权限。格式为`id="[OwnerUin]"`|String|否|
|GrantRead |赋予指定账户对 Bucket 的读权限。格式为`id="[OwnerUin]"`|String|否|
| GrantWrite|赋予指定账户对 Bucket 的写权限。格式为`id="[OwnerUin]"`|String|否|

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
    Bucket='examplebucket-1250000000'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket|待删除的 Bucket 名称，由 BucketName-APPID 构成|String|是|

#### 返回结果说明
该方法返回值为 None。

### 查询 Bucket 是否存在

#### 功能说明

查询一个 bucket 是否存在或者拥有访问权限。

#### 方法原型

```
head_bucket(Bucket)
```
#### 请求示例

```python
response = client.head_bucket(
    Bucket='examplebucket-1250000000'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket|待查询的 Bucket 名称，由 BucketName-APPID 构成|String|是|

#### 返回结果说明
该方法返回值为 None。

### 获取 Bucket 地域信息

#### 功能说明

查询一个 bucket 所在 region 的信息。

#### 方法原型

```
get_bucket_location(Bucket)
```
#### 请求示例

```python
response = client.get_bucket_location(
    Bucket='examplebucket-1250000000'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket|待查询的 Bucket 名称，由 BucketName-APPID 构成|String|是|

#### 返回结果说明

Bucket 地域信息，类型为 dict。
```python
{
    'LocationConstraint': 'ap-beijing-1'|'ap-beijing'|'ap-shanghai'|'ap-guangzhou'|'ap-chengdu'|'ap-chongqing'|'ap-singapore'|'ap-hongkong'|'na-toronto'|'eu-frankfurt'|'ap-mumbai'|'ap-seoul'|'na-siliconvalley'|'na-ashburn'
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- | 
| LocationConstraint |存储桶所在地域的信息|String|

### 列出 Bucket 下所有文件 

#### 功能说明

获取指定 Bucket 下的所有 Objects。

#### 方法原型

```
list_objects(Bucket, Delimiter="", Marker="", MaxKeys=1000, Prefix="", EncodingType="", **kwargs)
```
#### 请求示例

```python
response = client.list_objects(
    Bucket='examplebucket-1250000000',
    Prefix='string',
    Delimiter='/',
    Marker='string',
    MaxKeys=100,
    EncodingType='url'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   | 存储桶名称，由 BucketName-APPID 构成  | String  | 是| 
| Prefix   |  默认为空，对对象的对象键进行筛选，匹配 prefix 为前缀的对象  | String  |  否| 
| Delimiter   |   默认为空，设置分隔符，比如设置/来模拟文件夹  | String|  否|
| Marker   |  默认以 UTF-8 二进制顺序列出条目，标记返回对象的 list 的起点位置  | String  |  否| 
| MaxKeys   | 最多返回的对象数量，默认为最大的1000  | Int  |  否| 
| EncodingType   |   默认不编码，规定返回值的编码方式，可选值：url  | String  | 否|

#### 返回结果说明

获取对象的元信息，类型为 dict：

```python
{
    'MaxKeys': '1000', 
    'Prefix': 'string',
    'Delimiter': 'string',
    'Marker': 'string',
    'NextMarker': 'string',
    'Name': 'examplebucket-1250000000',  
    'IsTruncated': 'false'|'true',
    'EncodingType': 'url',
    'Contents':[
        {
            'ETag': '"a5b2e1cfb08d10f6523f7e6fbf3643d5"', 
            'StorageClass': 'STANDARD', 
            'Key': 'exampleobject'
            'Owner': {
                'DisplayName': '1250000000',
                'ID': '1250000000'
            }, 
            'LastModified': '2017-08-08T09:43:35.000Z', 
            'Size': '23'
        },
    ],
    'CommonPrefixes':[
        {
            'Prefix': 'string'
        },
    ],
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- |
| MaxKeys   | 最多返回的对象数量，默认为最大的1000  | String |
| Prefix   |  默认为空，对，匹配 prefix 为前缀的对象 | String|
| Delimiter   |   默认为空，设置分隔符，比如设置/来模拟文件夹  | String|
| Marker   |  默认以 UTF-8 二进制顺序列出条目，标记返回对象的 list 的起点位置  | String  |
| NextMarker|  当 IsTruncated 为 true 时，标记下一次返回对象的 list 的起点位置  | String  |
| Name   | 存储桶名称，由 BucketName-APPID 构成  | String  | 
| IsTruncated   |  表示返回的对象否被截断  | String|
| EncodingType   | 默认不编码，规定返回值的编码方式，可选值：url  | String  | 否|
|Contents |包含所有对象元信息的 list，包括 'ETag'，'StorageClass'，'Key'，'Owner'，'LastModified'，'Size' 等信息|List|
|CommonPrefixes |所有以 Prefix 开头,以 Delimiter 结尾的对象被归到同一类|List| 

### 列出 Bucket 下所有分块上传

#### 功能说明

获取指定 Bucket 下的所有正在进行中的分块上传。

#### 方法原型

```
list_multipart_uploads(Bucket, Prefix="", Delimiter="", KeyMarker="", UploadIdMarker="", MaxUploads=1000, EncodingType="", **kwargs)
```
#### 请求示例

```python
response = client.list_multipart_uploads(
    Bucket='examplebucket-1250000000',
    Prefix='string',
    Delimiter='string',
    KeyMarker='string',
    UploadIdMarker='string'
    MaxUploads=100,
    EncodingType='url'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket   | 存储桶名称，由 BucketName-APPID 构成  | String  | 是|
| Prefix   |  默认为空，对分块上传的 key 进行筛选，匹配 prefix 为前缀的分块上传  | String  |  否| 
| Delimiter   |   默认为空，设置分隔符| String|  否|
| KeyMarker   |  和 UploadIdMarker 一起使用，指明列出分块上传的起始位置  | String  |  否|
| UploadIdMarker   |  和 KeyMarker 一起使用，指明列出分块上传的起始位置。如果没有指定 KeyMarker，UploadIdMarker 会被忽略| String  |  否|
| MaxUploads   | 最多返回的分块上传的数量，默认为最大的1000  | Int  |  否| 
| EncodingType   |   默认不编码，规定返回值的编码方式，可选值：url  | String  | 否|

#### 返回结果说明

获取分块上传的信息，类型为 dict：

```python
{
    'Bucket': 'examplebucket-1250000000',
    'Prefix': 'string',
    'Delimiter': 'string',
    'KeyMarker': 'string',
    'UploadIdMarker': 'string',
    'NextKeyMarker': 'string',
    'NextUploadIdMarker': 'string',
    'MaxUploads': '1000',
    'IsTruncated': 'true'|'false',,
    'EncodingType': 'url',
    'Upload':[
        {
            'UploadId': 'string',
            'Key': 'string',
            'Initiated': 'string',
            'StorageClass': 'STANDARD',
            'Owner': {
                'DisplayName': 'string',
                'ID': 'string'
            },
            'Initiator': {
                'ID': 'string',
                'DisplayName': 'string'
            }
        },
    ],
    'CommonPrefixes':[
        {
            'Prefix': 'string'
        },
    ],
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- |
| Bucket   | 存储桶名称，由 BucketName-APPID 构成  | String  | 
| Prefix   |  默认为空，对分块上传的 key 进行筛选，匹配 prefix 为前缀的分块上传  | String  |
| Delimiter   |   默认为空，设置分隔符| String|
| KeyMarker   |  和 UploadIdMarker 一起使用，指明列出分块上传的 key 起始位置  | String  |
| UploadIdMarker   |  和 KeyMarker 一起使用，指明列出分块上传的 uploadid 起始位置。如果没有指定 KeyMarker，UploadIdMarker 会被忽略| String  |
| NextKeyMarker   |  当 IsTruncated 为 true 时，指明下一次列出分块上传的 key 的起始位置  | String  |
| NextUploadIdMarker   |  当 IsTruncated 为 true 时，指明下一次列出分块上传的 uploadid 的起始位置| String  |
| MaxUploads   | 最多返回的分块上传的数量，默认为最大的1000  | Int  |
| IsTruncated   |  表示返回的分块上传否被截断  | String|
| EncodingType   |   默认不编码，规定返回值的编码方式，可选值：url  | String  |
|Upload |包含所有分块上传的 list，包括 'UploadId'，'StorageClass'，'Key'，'Owner'，'Initiator'，'Initiated' 等信息|List|
|CommonPrefixes |所有以 Prefix 开头,以 Delimiter 结尾的 Key 被归到同一类|List|

### 设置 Bucket ACL 信息

#### 功能说明

设置 Bucket 的 ACL 信息， 通过 ACL，GrantFullControl，GrantRead，GrantWrite 传入 header 的方式来设置 ACL，或者通过 AccessControlPolicy 传入 body 来设置 ACL，两种方式只能选择一种，否则会返回冲突。

#### 方法原型

```
put_bucket_acl(Bucket, AccessControlPolicy={}, **kwargs)
```
#### 请求示例

```python
response = client.put_bucket_acl(
    Bucket='examplebucket-1250000000',
    ACL='private'|'public-read'|'public-read-write',
    GrantFullControl='string',
    GrantRead='string',
    GrantWrite='string',
    AccessControlPolicy={
        'Grant': [
            {
                'Grantee': {
                    'DisplayName': 'string',
                    'Type': 'CanonicalUser'|'Group',
                    'ID': 'string',
                    'URI': 'string'
                },
                'Permission': 'FULL_CONTROL'|'WRITE'|'READ'
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
| Bucket | Bucket 名称，由 BucketName-APPID 构成|String|是|
| ACL |设置 Bucket 的 ACL，如 'private'，'public-read'，'public-read-write' |String| 否|
| GrantFullControl |赋予指定账户对 Bucket 的所有权限。格式为`id="[OwnerUin]"`|String|否|
|GrantRead |赋予指定账户对 Bucket 的读权限。格式为`id="[OwnerUin]"`|String|否|
| GrantWrite|赋予指定账户对 Bucket 的写权限。格式为`id="[OwnerUin]"`|String|否|
| AccessControlPolicy| 赋予指定账户对 Bucket 的访问权限，具体格式见 get bucket acl 返回结果说明|Dict|否 |

#### 返回结果说明
该方法返回值为 None。

### 获取 Bucket ACL 信息

#### 功能说明

获取指定 Bucket 的 ACL 信息。

#### 方法原型

```
get_bucket_acl(Bucket, **kwargs)
```
#### 请求示例

```python
response = client.get_bucket_acl(
    Bucket='examplebucket-1250000000',
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket|存储桶名称，由 BucketName-APPID 构成|String|是|


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
                'Type': 'CanonicalUser'|'Group',
                'ID': 'string',
                'URI': 'string'
            },
            'Permission': 'FULL_CONTROL'|'WRITE'|'READ'
        },
    ]
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- | 
| Owner |存储桶拥有者的信息，包括 DisplayName 和 ID|Dict|
| Grant |存储桶权限授予者的信息，包括 Grantee和 Permission|List|
| Grantee |权限授予者的信息，包括 DisplayName，Type，ID 和 URI|Dict|
| DisplayName |权限授予者的名字|String|
| Type |权限授予者的类型，类型为 CanonicalUser 或者 Group|String|
| ID |Type 为 CanonicalUser 时，对应权限授予者的 ID|String|
| URI |Type 为 Group 时，对应权限授予者的 URI|String|
| Permission |授予者所拥有的 Bucket 的权限，可选值有 FULL_CONTROL，WRITE，READ，分别对应所有权限、写权限、读权限|String|

### 设置 Bucket 跨域配置

#### 功能说明
设置指定 Bucket 的跨域资源配置。

#### 方法原型

```
put_bucket_cors(Bucket, CORSConfiguration={}, **kwargs)
```
#### 请求示例

```python
response = client.put_bucket_cors(
    Bucket='examplebucket-1250000000',
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
| Bucket |存储桶名称，由 BucketName-APPID 构成|String| 是|
| CORSRule |设置对应的跨域规则，包括 ID，MaxAgeSeconds，AllowedOrigin，AllowedMethod，AllowedHeader，ExposeHeader|List| 是|
| ID |设置规则的 ID|String|否|
| MaxAgeSeconds |设置 OPTIONS 请求得到结果的有效期|Int|否|
| AllowedOrigin |设置允许的访问来源，如 `"http://cloud.tencent.com"`，支持通配符 * |Dict|是|
| AllowedMethod |设置允许的方法，如 GET，PUT，HEAD，POST，DELETE|Dict|是|
| AllowedHeader |设置请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 * |Dict|否|
| ExposeHeader |设置浏览器可以接收到的来自服务器端的自定义头部信息|Dict|否|

#### 返回结果说明
该方法返回值为 None。

### 获取 Bucket 跨域配置

#### 功能说明
获取指定 Bucket 的跨域配置。

#### 方法原型

```
get_bucket_cors(Bucket, **kwargs)
```
#### 请求示例

```python
response = client.get_bucket_cors(
    Bucket='examplebucket-1250000000',
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket|存储桶名称，由 BucketName-APPID 构成|String| 是|

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
 | AllowedOrigin  | 允许的访问来源，如 `"http://cloud.tencent.com"`，支持通配符 *  | Dict | 
 | AllowedMethod  |  允许的方法，如 GET，PUT，HEAD，POST，DELETE | Dict |
 | AllowedHeader  |请求可以使用哪些自定义的 HTTP 请求头部，支持通配符 * |  Dict | 
 | ExposeHeader  | 浏览器可以接收到的来自服务器端的自定义头部信息 | Dict | 

### 删除 Bucket  跨域配置

#### 功能说明
删除指定 Bucket 的跨域配置。

#### 方法原型

```
delete_bucket_cors(Bucket, **kwargs)
```
#### 请求示例

```python
response = client.delete_bucket_cors(
    Bucket='examplebucket-1250000000',
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket|存储桶名称，由 BucketName-APPID 构成|String| 是

#### 返回结果说明

该方法返回值为 None。

### 设置 Bucket 生命周期配置

#### 功能说明
设置指定 Bucket 的生命周期配置。

#### 方法原型

```
put_bucket_lifecycle(Bucket, LifecycleConfiguration={}, **kwargs)
```
#### 请求示例

```python
from qcloud_cos import get_date
response = client.put_bucket_lifecycle(
    Bucket='examplebucket-1250000000',
    LifecycleConfiguration={
        'Rule': [
            {
                'ID': 'string',
                'Filter': {
                    'Prefix': 'string',
                    'Tag': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        }
                    ]
                },
                'Status': 'Enabled'|'Disabled',
                'Expiration': {
                    'Days': 100,
                    'Date': get_date(2018, 4, 20)
                },
                'Transition': [
                    {
                        'Days': 100,
                        'Date': get_date(2018, 4, 20),
                        'StorageClass': 'Standard_IA'|'Archive'
                    },
                ],
                'NoncurrentVersionExpiration': {
                    'NoncurrentDays': 100
                },
                'NoncurrentVersionTransition': [
                    {
                        'NoncurrentDays': 100,
                        'StorageClass': 'Standard_IA'
                    },
                ],
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
 |  Bucket  | Bucket 名称，由 BucketName-APPID 构成 | String |   是 | 
 |  Rule  |  设置对应的规则，包括 ID，Filter，Status，Expiration，Transition，NoncurrentVersionExpiration，NoncurrentVersionTransition，AbortIncompleteMultipartUpload | List |   是 |
 |  ID  |  设置规则的 ID | String |  否 |
 |  Filter  | 用于描述规则影响的 Object 集合,如需设置 bucket 中的所有 objects，请设置 Prefix 为空''| Dict |  是 | 
 |  Status  | 设置 Rule 是否启用，可选值为 Enabled 或者 Disabled | Dict |  是 | 
 |  Expiration  |  设置 Object 过期规则，可以指定天数 Days 或者指定日期 Date，Date 的格式必须是 GMT ISO 8601，建议使用 get_date 方法来指定具体的日期| Dict |  否 |
 |  Transition  | 设置 Object 转换存储类型规则，可以指定天数 Days 或者指定日期 Date，Date 的格式必须是 GMT ISO 8601，建议使用 get_date 方法来指定具体的日期。StorageClass 可选 Standard_IA，Archive，可以同时设置多条此类规则| List |  否 | 
 |  NoncurrentVersionExpiration  | 设置非当前版本 Object 过期规则，可以指定天数 NoncurrentDays |  Dict |  否 |
 |  NoncurrentVersionTransition  | 设置非当前版本 Object 转换存储类型规则，可以指定天数 NoncurrentDays，StorageClass 可选 Standard_IA, 可以同时设置多条此类规则| List |  否 | 
 |  AbortIncompleteMultipartUpload  |指明分块上传开始后多少天内必须完成上传 |  Dict |  否 | 


#### 返回结果说明

该方法返回值为 None。

### 获取 Bucket 生命周期配置

#### 功能说明
获取指定 Bucket 的生命周期配置。

#### 方法原型

```
get_bucket_lifecycle(Bucket, **kwargs)
```
#### 请求示例

```python
response = client.get_bucket_lifecycle(
    Bucket='examplebucket-1250000000',
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket |存储桶名称，由 BucketName-APPID 构成|String|是 |

#### 返回结果说明

Bucket 生命周期配置，类型为 dict。
```python
{
    'Rule': [
        {
            'ID': 'string',
            'Filter': {
                'Prefix': 'string',
                'Tag': [
                        {
                            'Key': 'string',
                            'Value': 'string'
                        }
                ]
            },
            'Status': 'string',
            'Expiration': {
                'Days': 100,
                'Date': 'string'
            },
            'Transition': [
                {
                    'Days': 100,
                    'Date': 'string',
                    'StorageClass': 'STANDARD_IA'|'Archive'
                },
            ],
            'NoncurrentVersionExpiration': {
                'NoncurrentDays': 100
            },
            'NoncurrentVersionTransition': [
                {
                    'NoncurrentDays': 100,
                    'StorageClass': 'STANDARD_IA'
                },
            ],
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
|  Transition  | Object 转换存储类型规则，可以指定天数 Days 或者指定日期 Date，StorageClass 可选 STANDARD_IA，Archive| List | 
|  NoncurrentVersionExpiration  | 非当前版本 Object 过期规则，可以指定天数 NoncurrentDays |  Dict |
|  NoncurrentVersionTransition  | 非当前版本 Object 转换存储类型规则，可以指定天数 NoncurrentDays，StorageClass 可选 STANDARD_IA| List | 
|  AbortIncompleteMultipartUpload  |  分块上传开始后多少天内必须完成上传 | Dict |

### 删除 Bucket 生命周期配置

#### 功能说明

删除指定 Bucket 的生命周期配置。

#### 方法原型

```
delete_bucket_lifecycle(Bucket, **kwargs)
```
#### 请求示例

```python
response = client.delete_bucket_lifecycle(
    Bucket='examplebucket-1250000000',
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket |存储桶名称，由 BucketName-APPID 构成|String|是 |

#### 返回结果说明

该方法返回值为 None。


### 设置 Bucket 版本控制配置

#### 功能说明
设置指定 Bucket 的版本控制相关配置。

#### 方法原型

```
put_bucket_versioning(Bucket, Status, **kwargs)
```
#### 请求示例

```python
response = client.put_bucket_versioning(
    Bucket='examplebucket-1250000000',
    Status='Enabled'|'Suspended'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|  Bucket  | Bucket 名称，由 BucketName-APPID 构成 | String |   是 | 
|  Status  | 设置Bucket版本控制的状态，可选值为'Enabled'， 'Suspended' | String |   是 |

#### 返回结果说明

该方法返回值为 None。

### 获取 Bucket 版本控制配置

#### 功能说明
获取指定 Bucket 的版本控制配置。

#### 方法原型

```
get_bucket_versioning(Bucket, **kwargs)
```
#### 请求示例

```python
response = client.get_bucket_versioning(
    Bucket='examplebucket-1250000000',
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket |存储桶名称，由 BucketName-APPID 构成|String|是 |

#### 返回结果说明

Bucket 版本控制配置，类型为 dict。
```python
{
    'Status': 'Enabled'|'Suspended'
}
```

| 参数名称   | 参数描述   |类型 |
| -------------- | -------------- |---------- | 
|  Status  |  Bucket版本控制的状态，可选值为'Enabled'，Suspended' | String | 


### 设置 Bucket 跨区域复制配置

#### 功能说明
设置指定 Bucket 的跨区域复制配置。

#### 方法原型

```
put_bucket_replication(Bucket, ReplicationConfiguration={}, **kwargs)
```
#### 请求示例

```python
response = client.put_bucket_replication(
    Bucket='examplebucket-1250000000',
    ReplicationConfiguration={
        'Role': 'qcs::cam::uin/735901238:uin/735901238',
        'Rule': [
            {
                'ID': 'string',
                'Status': 'Enabled'|'Disabled',
                'Prefix': 'string',
                'Destination': {
                    'Bucket': 'qcs::cos:ap-shanghai::replicationsouth-1252448703',
                    'StorageClass': 'STANDARD'|'STANDARD_IA'
                }
            }
        ]   
    }
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|  Bucket  | 源Bucket 名称，由 BucketName-APPID 构成 | String |   是 | 
|  Role  |  发起者身份标示, 格式为qcs::cam::uin/<OwnerUin>:uin/<SubUin> | String |  否 |
|  Rule  |  设置对应的规则，包括 ID，Status，Prefix，Destination | List |   是 |
|  ID  |  设置规则的 ID | String |  否 |
|  Status  | 设置 Rule 是否启用，可选值为 Enabled 或者 Disabled | String |  是 |
|  Prefix  | 设置 Rule的前缀匹配规则，为空时表示作用存储桶中的所有objects | String |  是 |
|  Destination  | 描述目的资源, 包括Bucket和StorageClass| Dict |  是 | 
|  Bucket  | 设置跨区域复制的目的bucket，格式为qcs::cos:[region]::[BucketName-APPID] | String |  是 |
|  StorageClass  | 设置目的文件的存储类型，可选值为'STANDARD'，'STANDARD_IA' | String |  否 |

#### 返回结果说明

该方法返回值为 None。

### 获取 Bucket 跨区域复制配置

#### 功能说明
获取指定 Bucket 的跨区域复制配置。

#### 方法原型

```
get_bucket_replication(Bucket, **kwargs)
```
#### 请求示例

```python
response = client.get_bucket_replication(
    Bucket='examplebucket-1250000000'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|  Bucket  | Bucket 名称，由 BucketName-APPID 构成 | String |   是 | 

#### 返回结果说明

Bucket 跨区域复制配置，类型为 dict。
```python
{
    'Role': 'qcs::cam::uin/735901238:uin/735901238',
    'Rule': [
        {
            'ID': 'string',
            'Status': 'Enabled'|'Disabled',
            'Prefix': 'string',
            'Destination': {
                'Bucket': 'qcs::cos:ap-shanghai::replicationsouth-1252448703',
                'StorageClass': 'STANDARD'|'STANDARD_IA'
            }
        }
    ]   
}
```

| 参数名称   | 参数描述   |类型 |
| -------------- | -------------- |---------- | 
|  Role  |  发起者身份标示, 格式为qcs::cam::uin/<OwnerUin>:uin/<SubUin> | String |  否 |
|  Rule  |  跨区域复制对应的规则，包括 ID，Status，Prefix，Destination | List |   是 |
|  ID  |  跨区域复制规则的 ID | String |  否 |
|  Status  | 跨区域复制 Rule 是否启用，可选值为 Enabled 或者 Disabled | String |  是 |
|  Prefix  | 跨区域复制 Rule的前缀匹配规则，为空时表示作用存储桶中的所有objects | String |  是 |
|  Destination  | 描述目的资源, 包括Bucket和StorageClass| Dict |  是 | 
|  Bucket  | 跨区域复制的目的bucket，格式为qcs::cos:[region]::[BucketName-APPID] | String |  是 |
|  StorageClass  | 目的文件的存储类型，可选值为'STANDARD'，'STANDARD_IA' | String |  否 |

### 删除 Bucket 跨区域复制配置

#### 功能说明

删除指定 Bucket 的跨区域复制配置。

#### 方法原型

```
delete_bucket_replication(Bucket, **kwargs)
```
#### 请求示例

```python
response = client.delete_bucket_replication(
    Bucket='examplebucket-1250000000',
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket |存储桶名称，由 BucketName-APPID 构成|String|是 |

#### 返回结果说明

该方法返回值为 None。

## Object API 描述

### 简单文件上传

#### 功能说明

支持上传本地文件或输入流到指定的 Bucket 中。推荐上传不大于20MB 的小文件，单次上传大小限制为5GB，大文件上传请使用分块上传。
>!当前访问策略条目限制为1000条，如果您不需要进行对象 ACL 控制，请在上传时不要设置，默认继承 Bucket 权限。

#### 方法原型

```
put_object(Bucket, Body, Key, **kwargs)
```
#### 请求示例

```python
response = client.put_object(
    Bucket='examplebucket-1250000000',
    Body=b'bytes'|file,
    Key='exampleobject',
    EnableMD5=False
)
```
#### 全部参数请求示例
```python
response = client.put_object(
    Bucket='examplebucket-1250000000',
    Body=b'bytes'|file,
    Key='exampleobject',
    EnableMD5=False|True,
    ACL='private'|'public-read',  # 请慎用此参数,否则会达到1000条ACL上限
    GrantFullControl='string',
    GrantRead='string',
    StorageClass='STANDARD'|'STANDARD_IA'|'ARCHIVE',
    Expires='string',
    CacheControl='string',
    ContentType='string',
    ContentDisposition='string',
    ContentEncoding='string',
    ContentLanguage='string',
    ContentLength='123',
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
 |  Bucket  | 存储桶名称，由 BucketName-APPID 构成 | String |   是 |
 |  Body  | 上传文件的内容，可以为文件流或字节流 |  file/bytes |  是 |
 |  Key  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | String |  是 | 
| EnableMD5 | 是否需要SDK计算Content-MD5，默认关闭，打开后会增加上传耗时|Bool | 否| 
| ACL |设置文件的ACL，如 'private'，'public-read' |String| 否|
| GrantFullControl |赋予被授权者所有的权限。格式：id="[OwnerUin]"|String|否|
|GrantRead |赋予被授权者读的权限。格式：id="[OwnerUin]"  |String|否|
 |  StorageClass  |  设置文件的存储类型，STANDARD，STANDARD_IA，ARCHIVE。默认值：STANDARD | String |   否 |
 |  Expires  | 设置 Content-Expires | String|  否 | 
 |  CacheControl  |  缓存策略，设置 Cache-Control | String |   否 |
 |  ContentType  | 内容类型，设置 Content-Type |String |   否 |  
 |  ContentDisposition  |  文件名称，设置 Content-Disposition | String |   否 |
 |  ContentEncoding  |  编码格式，设置 Content-Encoding | String |   否 |
 |  ContentLanguage  |  语言类型，设置 Content-Language | String |   否 |
 |  ContentLength  | 设置传输长度 | String |   否 | 
 |  ContentMD5  | 设置上传文件的 MD5 值用于校验 | String |   否 | 
 |  Metadata | 用户自定义的文件元信息， 必须以 x-cos-meta 开头，否则会被忽略 | Dict |  否 |

#### 返回结果说明
上传文件的属性，类型为 dict：

```python
{
    'ETag': 'string'
}
```


| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- |
|  ETag   |  上传文件的 MD5 值  | String  |
	
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
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
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
 |  Bucket  | 存储桶名称，由 BucketName-APPID 构成 | String  |  是 | 
 |  Key  |  对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | String  | 是 | 
 |  Range  |  设置下载文件的范围，格式为 bytes=first-last  | String  |  否 | 
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
    'x-cos-request-id': 'NTg3NzQ3ZmVfYmRjMzVfMzE5N182NzczMQ=='
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- | 
 | Body  |  下载文件的内容，get_raw_stream 方法可以得到一个文件流，`get_stream_to_file` 方法可以将文件内容下载到指定本地文件中 | StreamBody |
 | 文件元信息  |  下载文件的元信息，包括 Etag 和 x-cos-request-id 等信息，也会返回设置的文件元信息 | String |


### 获取预签名下载链接

#### 功能说明
获取预签名下载链接用于直接下载。

#### 方法原型

```
get_presigned_download_url(Bucket, Key, Expired=300, Params={}, Headers={})
```
#### 请求示例

```python
response = client.get_presigned_download_url(
    Bucket='examplebucket-1250000000',
    Key='exampleobject'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  |存储桶名称，由 BucketName-APPID 构成 |  String |  是 | 
 | Key  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | String | 是 | 
 |Expired| 签名过期时间，单位为秒| Int| 否|
 |Params| 签名中要签入的请求参数| Dict| 否|
 |Headers| 签名中要签入的请求头部| Dict| 否|

#### 返回结果说明
该方法返回值为预签名的下载 URL。

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
    Bucket='examplebucket-1250000000',
    Key='exampleobject'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  |存储桶名称，由 BucketName-APPID 构成 |  String |  是 | 
 | Key  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | String | 是 | 

#### 返回结果说明
该方法返回值为 None。

### 文件批量删除

#### 功能说明
将指定 Bucket 中的文件批量删除。

#### 方法原型

```
delete_objects(Bucket, Delete={}, **kwargs)
```
#### 请求示例

```python
response = client.delete_objects(
    Bucket='examplebucket-1250000000',
    Delete={
        'Object': [
            {
                'Key': 'exampleobject1',
            },
            {
                'Key': 'exampleobject2',
            },
        ],
        'Quiet': 'true'|'false'
    }
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  | Bucket 名称，由 BucketName-APPID 构成 |  String |  是 | 
 | Delete  | 说明本次删除的返回结果方式和目标 Object | Dict | 是 | 
 | Object  | 说明每个将要删除的目标 Object 信息 | List | 是 | 
 | Key     | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg| String|否|
 | Quiet   |指明删除的返回结果方式，可选值为'true','false'，默认为'false'。设置为'true'只返回失败的错误信息，设置为'false'时返回成功和失败的所有信息。|String|否|

#### 返回结果说明
批量删除文件的结果，类型为 dict：
```python
{
    'Deleted': [
        {
            'Key': 'string',
        },
        {
            'Key': 'string',
        },
    ],
    'Error': [
        {
            'Key': 'string',
            'Code': 'string',
            'Message': 'string'
        },
    ]
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- |
 | Deleted  |  删除成功的 Object 信息|  List |
 | Key     | 删除成功的 Object 的路径| String|
 | Error  |  删除失败的 Object 信息| List |
 | Key     | 删除失败的 Object 的路径| String|
 | Code     | 删除失败的 Object 对应的错误码| String|
 | Message   |删除失败的 Object 对应的错误信息| String|


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
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    IfModifiedSince='string'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
  | Bucket   | Bucket 名称，由 BucketName-APPID 构成  | String  |  是 | 
  | Key   |  对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg  |String  | 是 |
  | IfModifiedSince   | 在指定时间后被修改才返回  | String  | 否 | 

#### 返回结果说明

获取文件的元信息，类型为 dict：

```python
{
    'Content-Type': 'application/octet-stream',
    'Content-Length': '16807',
    'ETag': '"9a4802d5c99dafe1c04da0a8e7e166bf"',
    'Last-Modified': 'Wed, 28 Oct 2014 20:30:00 GMT',
    'x-cos-request-id': 'NTg3NzQ3ZmVfYmRjMzVfMzE5N182NzczMQ=='
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- | 
| 文件元信息 |获取文件的元信息，包括 Etag 和 x-cos-request-id 等信息，也会包含设置的文件元信息| String|

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
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    StorageClass='STANDARD'|'STANDARD_IA'|'ARCHIVE',
    Expires='string'
    CacheControl='string',
    ContentType='string',
    ContentDisposition='string',
    ContentEncoding='string',
    ContentLanguage='string',
    Metadata={
        'x-cos-meta-key1': 'value1',
        'x-cos-meta-key2': 'value2'
    },
    ACL='private'|'public-read',
    GrantFullControl='string',
    GrantRead='string'
)
# 获取UploadId供后续接口使用
uploadid = response['UploadId']
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  | Bucket 名称，由 BucketName-APPID 构成 |  String |  是 |
 | Key  |  对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | String | 是 |
 | StorageClass  | 设置文件的存储类型，STANDARD，STANDARD_IA，ARCHIVE。默认值：STANDARD | String |  否 | 
 | Expires  |  设置 Content-Expires | String| 否 |
 | CacheControl  | 缓存策略，设置 Cache-Control | String |  否 | 
 | ContentType  | 内容类型，设置 Content-Type | String |  否 | 
 | ContentDisposition  | 文件名称，设置 Content-Disposition | String |  否 | 
 | ContentEncoding  | 编码格式，设置 Content-Encoding | String |  否 | 
 | ContentLanguage  | 语言类型，设置 Content-Language |  String |  否 |
 | Metadata |用户自定义的文件元信息 | Dict |  否 |
 | ACL |设置文件的 ACL，如 'private'，'public-read' |String| 否|
| GrantFullControl |赋予被授权者所有的权限。格式：id="[OwnerUin]"|String|否|
|GrantRead |赋予被授权者读的权限。格式：id="[OwnerUin]" |String|否|

#### 返回结果说明

获取分块上传的初始化信息，类型为 dict：

```python
{
    'UploadId': '150219101333cecfd6718d0caea1e2738401f93aa531a4be7a2afee0f8828416f3278e5570',
    'Bucket': 'examplebucket-1250000000', 
    'Key': 'exampleobject' 
}

```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- |
|UploadId | 标识分块上传的 ID|String|
|Bucket|存储桶名称，由 bucket-appid 组成|String|
|Key | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg|String|

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
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    UploadId=uploadid
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket|存储桶名称，由 BucketName-APPID 构成|String| 是|
|Key |对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg|String| 是|
|UploadId |标识分块上传的 ID|String| 是|

#### 返回结果说明
该方法返回值为 None。

### 上传分块
#### 功能说明
上传一个分块到指定的 UploadId 中，单个大小不得超过5GB。

#### 方法原型

```
upload_part(Bucket, Key, Body, PartNumber, UploadId, **kwargs)
```
#### 请求示例

```python
# 注意，上传分块的块数最多10000块
response = client.upload_part(
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Body=b'bytes'|file,
    PartNumber=1,
    UploadId='string',
    EnableMD5=False|True,
    ContentLength='123',
    ContentMD5='string'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  | Bucket 名称，由 BucketName-APPID 构成 | String |  是|
 | Key  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | String |  是|
 | Body  | 上传分块的内容，可以为本地文件流或输入流 | file/bytes |  是|
 | PartNumber  |标识上传分块的序号 |  Int |  是|
 | UploadId  | 标识分块上传的 ID | String |  是|
 | EnableMD5 | 是否需要 SDK 计算 Content-MD5，默认关闭，打开后会增加上传耗时|Bool | 否| 
 | ContentLength  |设置传输长度 |  String |  否|
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
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    UploadId=uploadid,
    MaxParts=1000,
    PartNumberMarker=100,
    EncodingType='url'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket|存储桶名称，由 BucketName-APPID 构成|String| 是|
|Key |对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg|String| 是|
|UploadId |标识分块上传的 ID|String| 是|
|MaxParts |最多返回的分块的数量，默认为最大的1000|Int| 否|
|PartNumberMarker |默认为0，从第一块列出分块，从 PartNumberMarker 下一个分块开始列出|Int| 否|
|EncodingType |默认不编码，规定返回值的编码方式，可选值：url |String|否|

#### 返回结果说明

所有上传分块的信息，类型为 dict：

```python
{
    'Bucket': 'examplebucket-1250000000', 
    'Key': 'exampleobject', 
    'UploadId': '1502192444bdb382add546a35b2eeab81e06ed84086ca0bb75ea45ca7fa073fa9cf74ec4f2', 
    'EncodingType': None, 
    'MaxParts': '1000',
    'IsTruncated': 'true',
    'PartNumberMarker': '0', 
    'NextPartNumberMarker': '1000', 
    'StorageClass': 'Standard',
    'Part': [
        {
            'LastModified': '2017-08-08T11:40:48.000Z',
            'PartNumber': '1',
            'ETag': '"8b8378787c0925f42ccb829f6cc2fb97"',
            'Size': '10485760'
        },
    ], 
    'Initiator': {
        'DisplayName': '3333333333', 
        'ID': 'qcs::cam::uin/3333333333:uin/3333333333'
    }, 
    'Owner': {
        'DisplayName': '124564654654',
        'ID': '124564654654'
    }
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- | 
| Bucket   | 存储桶名称，由 BucketName-APPID 构成  | String  |
|  Key  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | String | 
|  UploadId  |  标识分块上传的 ID | String | 
| EncodingType   |   默认不编码，规定返回值的编码方式，可选值：url  | String  |
| MaxParts   | 最多返回的分块的数量，默认为最大的1000  | String  |
| IsTruncated   |  表示返回的分块是否被截断  | String|
| PartNumberMarker   | 默认为0，从第一块列出分块，从 PartNumberMarker 下一个分块开始列出  | String  |
| NextPartNumberMarker   |  指明下一次列出分块的起始位置  | String  |
 |  StorageClass  |  文件的存储类型，STANDARD，STANDARD_IA，ARCHIVE。默认值：STANDARD | String |
|  Part |上传分块的相关信息，包括 ETag，PartNumber，Size，LastModified | String |
 |  Initiator  | 分块上传的创建者，包括 DisplayName 和 ID | Dict | 
 |  Owner  | 文件拥有者的信息，包括 DisplayName 和 ID | Dict | 


### 完成分块上传

#### 功能说明

组装指定 UploadId 中所有的分块为一个完整的文件，文件最终大小必须大于1MB，否则会返回错误。

#### 方法原型

```
complete_multipart_upload(Bucket, Key, UploadId, MultipartUpload={}, **kwargs)
```
#### 请求示例

```python
response = client.complete_multipart_upload(
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
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
|  Bucket  | Bucket 名称，由 BucketName-APPID 构成 | String |   是| 
|  Key  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | String  |   是| 
|  UploadId  | 标识分块上传的 ID | String  |   是| 
|  MultipartUpload  |所有分块的 ETag 和 PartNumber 信息 |  Dict |   是| 

#### 返回结果说明

组装后的文件的相关信息，类型为 dict：

```python
{
    'ETag': '"3f866d0050f044750423e0a4104fa8cf-2"', 
    'Bucket': 'examplebucket-1250000000', 
    'Location': 'examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/exampleobject', 
    'Key': 'exampleobject'
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- | 
 |  ETag  |	合并后对象的唯一标签值，该值不是对象内容的 MD5 校验值，仅能用于检查对象唯一性。如需校验文件内容，可以在上传过程中校验单个分块的ETag值。|  String | 
 |  Bucket  |存储桶名称，由 BucketName-APPID 构成 |  String | 
 |  Location  | URL 地址 |  String | 
 |  Key  |  对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | String |

### 设置 Object ACL 信息

#### 功能说明

设置文件的 ACL 信息，通过 ACL，GrantFullControl，GrantRead，GrantWrite 传入 header 的方式来设置 ACL，或者通过 AccessControlPolicy 传入 body 来设置 ACL，两种方式只能选择一种，否则会返回冲突。
>!当前访问策略条目限制为1000条，如果您不需要进行对象 ACL 控制，请不要设置，默认继承 Bucket 权限。

#### 方法原型

```
put_object_acl(Bucket, Key, AccessControlPolicy={}, **kwargs)
```
#### 请求示例

```python
response = client.put_object_acl(
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    ACL='private'|'public-read',
    GrantFullControl='string',
    GrantRead='string',
    AccessControlPolicy={
        'Grant': [
            {
                'Grantee': {
                    'DisplayName': 'string',
                    'Type': 'CanonicalUser'|'Group',
                    'ID': 'string',
                    'URI': 'string'
                },
                'Permission': 'FULL_CONTROL'|'WRITE'|'READ'
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
| Bucket   | 存储桶名称，由 BucketName-APPID 构成 | String  |  是  |
| Key   | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | String  |  是  | 
| ACL |设置文件的 ACL，如 'private'，'public-read' |String| 否| 
| GrantFullControl |赋予指定账户对文件的所有权限。格式为`id="[OwnerUin]"`|String|否|
|GrantRead |赋予指定账户对文件的读权限。格式为`id="[OwnerUin]"`|String|否|
| AccessControlPolicy   | 赋予指定账户对文件的访问权限，具体格式见get object acl返回结果说明| Dict  | 否  | 


#### 返回结果说明

该方法返回值为 None。

### 获取 Object ACL 信息

#### 功能说明
获取指定文件的 ACL 信息。

#### 方法原型

```
get_object_acl(Bucket, Key, **kwargs)
```
#### 请求示例

```python
response = client.get_object_acl(
    Bucket='examplebucket-1250000000',
    Key='exampleobject'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket|存储桶名称，由 BucketName-APPID 构成|String| 是|
|Key |对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg|String|是|


#### 返回结果说明

Bucket ACL 信息，类型为 Dict：
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
                'Type': 'CanonicalUser'|'Group',
                'ID': 'string',
                'URI': 'string'
            },
            'Permission': 'FULL_CONTROL'|'WRITE'|'READ'
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
 |  Permission  |  授予者所拥有的文件的权限，可选值有 FULL_CONTROL，WRITE，READ，分别对应所有权限、写权限、读权限 | String |

### 文件拷贝

#### 功能说明
将一个文件从源路径复制到目标路径，在拷贝的过程中，文件元属性和 ACL 可以被修改。当需要执行拷贝操作时，如果对象大于5GB 且源和目标对象不在同一个地域时，必须使用 create_multipart_upload() 接口创建一个分块上传，再使用 upload_part_copy() 接口进行分块拷贝，并使用 complete_multipart_upload() 完成分块上传。如需要拷贝的对象小于等于5GB 或仅在同地域内拷贝，直接调用 copy_object() 即可。

#### 方法原型

```
copy_object(Bucket, Key, CopySource, CopyStatus='Copy', **kwargs)
```
#### 请求示例

```python
response = client.copy_object(
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    CopySource={
        'Appid': '1250000000',
        'Bucket': 'examplebucket', 
        'Key': 'exampleobject', 
        'Region': 'ap-guangzhou'
    },
    CopyStatus='Copy'|'Replaced',
    ACL='private'|'public-read',
    GrantFullControl='string',
    GrantRead='string',
    StorageClass='STANDARD'|'STANDARD_IA'|'ARCHIVE',
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
 |  Bucket  | 存储桶名称，由 BucketName-APPID 构成 | String|  是 |
 |  Key  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | String| 是 | 
 |  CopySource  | 描述拷贝源文件的路径，包含 Appid、Bucket、Key、Region |  Dict | 是 |
 |  CopyStatus  |  可选值为 'Copy','Replaced'，设置为 'Copy' 时，忽略设置的用户元数据信息直接复制，设置为 'Replaced' 时，按设置的元信息修改元数据，当目标路径和源路径一样时，必须设置为'Replaced' | String| 是 |
| ACL |设置文件的ACL，如 'private'，'public-read' |String| 否|
| GrantFullControl |赋予指定账户对文件的所有权限。格式为`id="[OwnerUin]"`|String|否|
|GrantRead |赋予指定账户对文件的读权限。格式为`id="[OwnerUin]"`|String|否|
 |  StorageClass  |  设置文件的存储类型，STANDARD,STANDARD_IA，默认值：STANDARD | String|  否 |
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

### 分块拷贝

#### 功能说明
将一个文件的分块内容从源路径复制到目标路径。

#### 方法原型

```
upload_part_copy(Bucket, Key, PartNumber, UploadId, CopySource, CopySourceRange='', **kwargs)
```
#### 请求示例

```python
response = client.upload_part_copy(
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    PartNumber=100,
    UploadId='string',
    CopySource={
        'Appid': '1250000000',
        'Bucket': 'examplebucket', 
        'Key': 'exampleobject', 
        'Region': 'ap-guangzhou'
    },
    CopySourceRange='string',
    CopySourceIfMatch='string',
    CopySourceIfModifiedSince='string',
    CopySourceIfNoneMatch='string',
    CopySourceIfUnmodifiedSince='string'
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|  Bucket  | 存储桶名称，由 BucketName-APPID 构成 | String|  是 |
|  Key  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | String| 是 |
| PartNumber  |标识上传分块的序号 |  Int |  是|
| UploadId  | 标识分块上传的 ID | String |  是|
|  CopySource  | 描述拷贝源文件的路径，包含 Appid、Bucket、Key、Region |  Dict | 是 |
|CopySourceRange| 描述拷贝源文件的范围，格式为 bytes=first-last。不指定时，默认拷贝整个源文件|String|否|
|CopySourceIfMatch| 源文件的 Etag 与给定的值相同时才拷贝|String|否|
|CopySourceIfModifiedSince| 源文件在给定的时间后被修改相才拷贝|String|否|
|CopySourceIfNoneMatch| 源文件的 Etag 与给定的值不相同时才拷贝|String|否|
|CopySourceIfUnmodifiedSince| 源文件在给定的时间后没有修改相才拷贝|String|否|

#### 返回结果说明

拷贝分块的属性，类型为 dict：

```python
{
    'ETag': 'string',
    'LastModified': 'string',
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- | 
| ETag |拷贝分块的 MD5 值|String|
| LastModified |拷贝分块的最后一次修改时间|String|

### 恢复归档文件

#### 功能说明
对一个通过 COS 归档为 archive 类型的对象进行恢复。

#### 方法原型

```
restore_object(Bucket, Key, RestoreRequest={}, **kwargs)
```
#### 请求示例

```python
response = client.restore_object(
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    RestoreRequest={
        'Days': 100,
        'CASJobParameters': {
            'Tier': 'Expedited'|'Standard'|'Bulk'
        }

    }
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|Bucket|存储桶名称，由 BucketName-APPID 构成|String| 是|
|Key |对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg|String|是|
|RestoreRequest| 描述取回的临时文件的规则| Dict|是|
|Days| 描述临时文件的过期时间| Int|是|
|CASJobParameters| 描述恢复类型的配置信息| Dict|否|
|Tier| 描述取回临时文件的模式，可选值为'Expedited'，Standard'，'Bulk'，分别对应快速、标准以及慢这三种模式| String|否|

#### 返回结果说明
该方法返回值为None。

## 高级接口（推荐）

### 文件上传（断点续传）

#### 功能说明
文件上传接口根据用户文件的长度自动选择简单上传以及分块上传，对于小于等于20M 的文件调用简单上传，对于大于20MB 的文件调用分块上传，对于分块上传的未完成的文件会自动进行断点续传。

#### 方法原型

```
upload_file(Bucket, Key, LocalFilePath, PartSize=1, MAXThread=5, **kwargs)
```
#### 请求示例

```python
response = client.upload_file(
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    LocalFilePath='local.txt',
    EnableMD5=False
)
```

#### 全部参数请求示例
```python
response = client.upload_file(
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    LocalFilePath='local.txt',
    PartSize=1,
    MAXThread=5,
    EnableMD5=False|True,
    ACL='private'|'public-read', # 请慎用此参数,否则会达到1000条ACL上限
    GrantFullControl='string',
    GrantRead='string',
    StorageClass='STANDARD'|'STANDARD_IA'|'ARCHIVE',
    Expires='string',
    CacheControl='string',
    ContentType='string',
    ContentDisposition='string',
    ContentEncoding='string',
    ContentLanguage='string',
    ContentLength='123',
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
 |  Bucket  | 存储桶名称，由 BucketName-APPID 构成 | String |   是 |
 |  Key  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | String |  是 | 
|  LocalFilePath  | 本地文件的路径名 |  String |  是 |
|  PartSize  | 分块上传的分块大小，默认为1MB |  Int |  否 |
|  MAXThread  | 分块上传的并发数量，默认为5个线程上传分块 |  Int |  否 |
| EnableMD5 | 是否需要 SDK 计算 Content-MD5，默认关闭，打开后会增加上传耗时|Bool | 否| 
| ACL |设置文件的 ACL，如 'private'，'public-read'|String| 否|
| GrantFullControl |赋予被授权者所有的权限。格式：id="[OwnerUin]"|String|否|
|GrantRead |赋予被授权者读的权限。格式：id="[OwnerUin]"  |String|否|
 |  StorageClass  |  设置文件的存储类型，STANDARD，STANDARD_IA，ARCHIVE。默认值：STANDARD | String |   否 |
 |  Expires  | 设置 Content-Expires | String|  否 | 
 |  CacheControl  |  缓存策略，设置 Cache-Control | String |   否 |
 |  ContentType  | 内容类型，设置 Content-Type |String |   否 |  
 |  ContentDisposition  |  文件名称，设置 Content-Disposition | String |   否 |
 |  ContentEncoding  |  编码格式，设置 Content-Encoding | String |   否 |
 |  ContentLanguage  |  语言类型，设置 Content-Language | String |   否 |
 |  ContentLength  | 设置传输长度 | String |   否 | 
 |  ContentMD5  | 设置上传文件的 MD5 值用于校验 | String |   否 | 
 |  Metadata | 用户自定义的文件元信息 | Dict |   否 |

#### 返回结果说明
上传文件的属性，类型为 dict：

```python
{
    'ETag': 'string'
}
```

| 参数名称   | 参数描述   |类型 | 
| -------------- | -------------- |---------- |
|  ETag   |  上传文件的 MD5 值  | String  |

## 签名获取 API 描述

### 签名获取

#### 功能说明
获取指定操作的签名，常用于移动端的签名分发。

#### 方法原型

```
get_auth(Method, Bucket, Key, Expired=300, Headers={}, Params={})
```
#### 请求示例

```python
response = client.get_auth(
    Method='PUT'|'POST'|'GET'|'DELETE'|'HEAD',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Expired=300,
    Headers={
        'Content-Length': 'string',
        'Content-MD5': 'string'
    },
    Params={
        'param1': 'string',
        'param2': 'string'
    }
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 | Method  |对应操作的method, 可选值为'PUT','POST','GET','DELETE','HEAD'|  String |  是 | 
 | Bucket  |存储桶名称，由 BucketName-APPID 构成 |  String |  是 | 
 | Key  | bucket 操作填入根路径/，object 操作填入文件的路径| String | 是| 
 |Expired| 签名过期时间，单位为秒| Int| 否|
 |Headers| 需要签入签名的请求头部| Dict| 否|
 |Params | 需要签入签名的请求参数| Dict| 否|

#### 返回结果说明
该方法返回值为对应操作的签名值。

### 获取预签名链接

#### 功能说明
获取预签名链接用于分发。

#### 方法原型

```
get_presigned_url(Bucket, Key, Method, Expired=300, Params={}, Headers={})
```
#### 请求示例

```python
response = client.get_presigned_url(
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Method='PUT'|'POST'|'GET'|'DELETE'|'HEAD'
)
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
 | Bucket  |存储桶名称，由 BucketName-APPID 构成 |  String |  是 | 
 | Key  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg | String | 是 | 
 | Method  |对应操作的method, 可选值为'PUT'，'POST'，'GET'，'DELETE'，'HEAD'|  String |  是 | 
 |Expired| 签名过期时间，单位为秒| Int| 否|
 |Params| 签名中要签入的请求参数| Dict| 否|
 |Headers| 签名中要签入的请求头部| Dict| 否|
 
 
#### 返回结果说明
该方法返回值为预签名的 URL。

## 异常类型 描述
包括 CosClientError 和 CosServiceError，分别对应 SDK 客户端错误和 COS 服务端错误。

### CosClientError
CosClientError 一般指如 timeout 引起的客户端错误，用户捕获后可以选择重试或其它操作。

### CosServiceError
CosServiceError 提供服务端返回的具体信息，获取错误码的更多信息请参考：[COS 错误码](https://cloud.tencent.com/document/product/436/7730)。

```python
#except CosServiceError as e
e.get_origin_msg()  # 获取原始错误信息，格式为XML
e.get_digest_msg()  # 获取处理过的错误信息，格式为dict
e.get_status_code() # 获取http错误码（如4XX，5XX)
e.get_error_code()  # 获取Cos定义的错误码
e.get_error_msg()   # 获取Cos错误码的具体描述
e.get_trace_id()    # 获取请求的 trace_id
e.get_request_id()  # 获取请求的 request_id
e.get_resource_location() # 获取URL地址
```
