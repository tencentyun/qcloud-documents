## 开发准备

### 相关资源

COS Python SDK V5 相关资源地址: [github项目](https://github.com/tencentyun/cos-python-sdk-v5)

> COS Python SDK 相关资源地址: [github项目](https://github.com/tencentyun/cos-python-sdk-v5)
> by  vivianlei  // 无V5这一说。
### 环境依赖

V5 版本 COS Python SDK 目前可以支持 Python2.6 与 Python2.7

> 系统需先安装 Python 和 pip，支持python版本： 2.6 ， 2.7
> 1. python 下载和安装：请根据所使用操作系统，从[python官网]（https://www.python.org/downloads/）下载对应版本，并安装。
> 2. pip 下载和安装：请查看[pip官网](https://pip.pypa.io/en/stable/installing/) 
> by  vivianlei  // 1. 尽量简洁 2. 标题是环境依赖，描述是说明支持版本

### 安装SDK

安装 SDK 的方式有两种：pip安装和手动安装。

- 使用pip安装
  
        pip install -U cos-python-sdk-v5

- 手动安装

        从[github项目](https://github.com/tencentyun/cos-python-sdk-v5)下载源码,通过setup手动安装：

        python setup.py install

### 卸载SDK

使用 pip uninstall 删除package
 
## 快速入门

```python
# 1.设置用户配置, 包括appid, secret_id，secret_key以及region
appid = 100000              # 替换为用户的appid
secret_id = u'xxxxxxxx'     # 替换为用户的secret_id
secret_key = u'xxxxxxx'     # 替换为用户的secret_key
region = 'ap-beijing-1'     # 替换为用户的region
token = ''                  # 使用临时秘钥需要传入Token，默认为空，可不填
config = CosConfig(Appid=appid, Access_id=secret_id, Access_key=secret_key, Region=region, Token=token)
# 2.获取客户端对象
client = CosS3Client(config)
# 参照下文的API描述。或者参照Demo程序，详见https://github.com/tencentyun/cos-python-sdk-v5/blob/master/qcloud_cos/test.py
```


> <font size=4 color=red> 这里需要是使用的范例， 不是接口说明哈！！下面的章节可以删去，简化成上传下载等使用的范例。 </font>
> by stongdong
> 

## 基本API描述

COS XML API Python SDK 操作成功会返回一个dict或者None，失败会抛出异常(CosClientError 和 CosServiceError)。异常类会提供相关的错误信息，详见文末的异常类型介绍。

### 创建Bucket

#### 功能说明

在指定账号下创建一个新的Bucket，当Bucket已存在时会返回错误。

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

* Bucket —— (String) ： 必选参数，待创建的Bucket名称，由数字和小写字母以及中划线"-"构成。
* ACL —— (String) ： 可选参数，设置Bucket的ACL，如'private，public-read'，'public-read-write'。
* GrantFullControl —— (string) ：可选参数，赋予指定账户对Bucket的读写权限。
* GrantRead —— (string) ：可选参数，赋予指定账户对Bucket的读权限。
* GrantWrite —— (string) ：可选参数，赋予指定账户对Bucket的写权限。


#### 返回结果说明

该方法返回值为None。

### 删除Bucket

#### 功能说明

在指定账号下删除一个已经存在的Bucket，删除时Bucket必须为空。

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

* Bucket —— (String) ： 必选参数，待删除的Bucket名称，由数字和小写字母以及中划线"-"构成。
#### 返回结果说明

该方法返回值为None。

### 设置Bucket ACL信息

#### 功能说明

设置Bucket的ACL信息, 通过ACL，GrantFullControl，GrantRead，GrantWriteheader传入header的方式来设置ACL，或者通过AccessControlPolicy传入body来设置ACL，两种方式只能选择一种，否则会返回冲突。

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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* ACL —— (String) ： 可选参数，设置Bucket的ACL，如'private，public-read'，'public-read-write'。
* GrantFullControl —— (string) ：可选参数，赋予指定账户对Bucket的读写权限。
* GrantRead —— (string) ：可选参数，赋予指定账户对Bucket的读权限。
* GrantWrite —— (string) ：可选参数，赋予指定账户对Bucket的写权限。
* AccessControlPolicy —— (dict) ：可选参数，赋予指定账户对Bucket的访问权限。


#### 返回结果说明

该方法返回值为None。

### 获取Bucket ACL信息

#### 功能说明

获取指定bucket的ACL信息。

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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。


#### 返回结果说明

Bucket ACL信息，类型为dict。
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
* Owner —— (dict) ：Bucket拥有者的信息，包括DisplayName和ID。
* Grant —— (list) ：Bucket权限授予者的信息，包括Grantee和Permission。
* Grantee —— (dict) ：权限授予者的信息，包括DisplayName，Type，ID和URI。
* DisplayName —— (string) ：权限授予者的名字。
* Type —— (string) ：权限授予者的类型，类型为CanonicalUser或者Group。
* ID —— (string) ：Type为CanonicalUser时，对应权限授予者的ID。
* URI —— (string) ：Type为Group时，对应权限授予者的URI。
* Permission —— (string) ：授予者所拥有的Bucket的权限，可选值有FULL_CONTROL，WRITE，READ，分别对应读写权限、写权限、读权限。

### 设置Bucket跨域配置

#### 功能说明

设置指定Bucket的跨域资源配置。

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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* CORSRule —— (list) ： 必选参数，设置对应的跨域规则，包括ID，MaxAgeSeconds，AllowedOrigin，AllowedMethod，AllowedHeader，ExposeHeader。
* ID —— (String) ：可选参数，设置规则的ID。
* MaxAgeSeconds —— (int) ：可选参数，设置OPTIONS请求得到结果的有效期。
* AllowedOrigin —— (dict) ：必选参数，设置允许的访问来源，如"http://www.qcloud.com"，支持通配符*。
* AllowedMethod —— (dict) ：必选参数，设置允许的方法，如GET，PUT，HEAD，POST，DELETE。
* AllowedHeader —— (dict) ：可选参数，设置请求可以使用哪些自定义的HTTP请求头部，支持通配符*。
* ExposeHeader —— (dict) ：可选参数，设置浏览器可以接收到的来自服务器端的自定义头部信息。


#### 返回结果说明

该方法返回值为None。

### 获取Bucket跨域配置

#### 功能说明

获取指定Bucket的跨域资源配置。

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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。

#### 返回结果说明

Bucket跨域配置，类型为dict。
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
* CORSRule —— (list) ： 跨域规则，包括ID，MaxAgeSeconds，AllowedOrigin，AllowedMethod，AllowedHeader，ExposeHeader。
* ID —— (String) ：规则的ID。
* MaxAgeSeconds —— (string) ：OPTIONS请求得到结果的有效期。
* AllowedOrigin —— (dict) ：允许的访问来源，如"http://www.qcloud.com"，支持通配符*。
* AllowedMethod —— (dict) ：允许的方法，如GET，PUT，HEAD，POST，DELETE。
* AllowedHeader —— (dict) ：请求可以使用哪些自定义的HTTP请求头部，支持通配符*。
* ExposeHeader —— (dict) ：浏览器可以接收到的来自服务器端的自定义头部信息。

### 删除Bucket跨域配置

#### 功能说明

删除指定Bucket的跨域资源配置。

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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。

#### 返回结果说明

该方法返回值为None。

### 设置Bucket生命周期配置

#### 功能说明

设置指定Bucket的生命周期配置。

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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* Rule —— (list) ： 必选参数，设置对应的规则，包括ID，Filter，Status，Expiration，Transition，NoncurrentVersionExpiration，NoncurrentVersionTransition，AbortIncompleteMultipartUpload。
* ID —— (String) ：可选参数，设置规则的ID。
* Filter —— (dict) ：必选参数，用于描述规则影响的Object集合。
* Status —— (dict) ：必选参数，设置Rule是否启用，可选值为Enabled或者Disabled。
* Expiration —— (dict) ：可选参数，设置Object过期规则，可以指定天数Days或者指定日期Date。
* Transition —— (dict) ：可选参数，设置Object转换存储类型规则，可以指定天数Days或者指定日期Date，StorageClass可选Standard_IA, Nearline。
* NoncurrentVersionExpiration —— (dict) ：可选参数，设置非当前版本Object过期规则，可以指定天数NoncurrentDays。
* NoncurrentVersionTransition —— (dict) ：可选参数，设置非当前版本Object转换存储类型规则，可以指定天数NoncurrentDays，StorageClass可选Standard_IA, Nearline。
* AbortIncompleteMultipartUpload —— (dict) ：可选参数，指明分块上传开始后多少天内必须完成上传。


#### 返回结果说明

该方法返回值为None。

### 获取Bucket生命周期配置

#### 功能说明

获取指定Bucket的生命周期配置。

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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。

#### 返回结果说明

Bucket跨域配置，类型为dict。
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
* Rule —— (list) ： 对应的规则，包括ID，Filter，Status，Expiration，Transition，NoncurrentVersionExpiration，NoncurrentVersionTransition，AbortIncompleteMultipartUpload。
* ID —— (String) ：规则的ID。
* Filter —— (dict) ：必用于描述规则影响的Object集合。
* Status —— (dict) ：Rule是否启用，可选值为Enabled或者Disabled。
* Expiration —— (dict) ：Object过期规则，可以指定天数Days或者指定日期Date。
* Transition —— (dict) ：Object转换存储类型规则，可以指定天数Days或者指定日期Date，StorageClass可选Standard_IA, Nearline。
* NoncurrentVersionExpiration —— (dict) ：非当前版本Object过期规则，可以指定天数NoncurrentDays。
* NoncurrentVersionTransition —— (dict) ：非当前版本Object转换存储类型规则，可以指定天数NoncurrentDays，StorageClass可选Standard_IA, Nearline。
* AbortIncompleteMultipartUpload —— (dict) ：分块上传开始后多少天内必须完成上传。

### 删除Bucket生命周期配置。

#### 功能说明

删除指定Bucket的生命周期配置。

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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。

#### 返回结果说明

该方法返回值为None。

### 简单文件上传

#### 功能说明

支持上传本地文件或输入流到指定的Bucket中。推荐上传不大于20MB的小文件，单次上传大小限制为5GB，大文件上传请使用分块上传。


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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* Body —— (file|string) ：必选参数，上传文件的内容，可以为文件流或字节流。
* Key —— (string) ：必选参数，上传文件的路径名，默认从Bucket开始。
* ACL —— (String) ： 可选参数，设置文件的ACL，如'private，public-read'，'public-read-write'。
* GrantFullControl —— (string) ：可选参数，赋予指定账户对文件的读写权限。
* GrantRead —— (string) ：可选参数，赋予指定账户对文件读权限。
* GrantWrite —— (string) ：可选参数，赋予指定账户对文件的写权限。
* StorageClass —— (string) ： 可选参数，设置文件的存储类型，STANDARD,STANDARD_IA，NEARLINE，默认值：STANDARD。
* Expires —— (string): 可选参数，设置Content-Expires。
* CacheControl —— (string) ： 可选参数，缓存策略，设置Cache-Control。
* ContentType —— (string) ： 可选参数，内容类型，设置Content-Type。
* ContentDisposition —— (string) ： 可选参数，文件名称，设置Content-Disposition。
* ContentEncoding —— (string) ： 可选参数，编码格式，设置Content-Encoding。
* ContentLanguage —— (string) ： 可选参数，语言类型，设置Content-Language。
* ContentLength —— (int) ： 可选参数，设置传输长度。
* ContentMD5 —— (string) ： 可选参数，设置上传文件的MD5值用于校验。
* Metadata —— （dict) ： 可选参数，用户自定义的文件元信息。
#### 返回结果说明

上传文件的属性，类型为dict：

```python
{
    'ETag': 'string',
    'x-cos-expiration': 'string',
    'x-cos-version-id': 'string'
}
```

* ETag —— (string) ：上传文件的MD5值。
* x-cos-expiration —— (string) ：设置生命周期后，返回文件过期规则。
* x-cos-version-id —— (string) ：设置版本管理后，返回文件版本。

### 文件下载

#### 功能说明

将指定Bucket中的文件下载到本地。


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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* Key —— (string) ：必选参数，下载文件的路径名，默认从Bucket开始。
* Range —— (string) ： 可选参数，设置下载文件的范围，格式为'bytes 0-16086/16087'。
* IfMatch —— (string) ：可选参数，ETag 与指定的内容一致时才返回。
* IfModifiedSince —— (string) ：可选参数，在指定时间后被修改才返回。
* IfNoneMatch —— (string) ：可选参数，ETag 与指定的内容不一致才返回。
* IfUnmodifiedSince —— (string) ：文件修改时间早于或等于指定时间才返回。
* ResponseCacheControl —— (string) ：可选参数，设置响应头部Cache-Control。
* ResponseContentDisposition —— (string) ：可选参数，设置响应头部Content-Disposition。
* ResponseContentEncoding —— (string) ：可选参数，设置响应头部Content-Encoding。
* ResponseContentLanguage —— (string) ：可选参数，设置响应头部Content-Language。
* ResponseContentType —— (string) ：可选参数，设置响应头部Content-Type。
* ResponseExpires —— (string) ：可选参数，设置响应头部Content-Expires。
* VersionId —— (string) ：可选参数，指定下载文件的版本。
#### 返回结果说明

下载文件的Body和元信息，类型为dict：

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

* Body —— (StreamBody) ：下载文件的内容，get_raw_stream方法可以得到一个文件流，get_stream_to_file方法可以将文件内容下载到指定本地文件中。
* 文件元信息 —— (string) ：下载文件的元信息，包括Etag和x-cos-request-id等信息，也会返回设置的文件元信息。

### 文件删除

#### 功能说明
将指定Bucket中的对应文件删除。


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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* Key —— (string) ：必选参数，删除文件的路径名，默认从Bucket开始。
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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* Key —— (string) ：必选参数，文件的路径名，默认从Bucket开始。
* IfModifiedSince —— (string) ：可选参数，在指定时间后被修改才返回。
#### 返回结果说明

获取文件的元信息，类型为dict：

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
* 文件元信息 —— (string) ：获取文件的元信息，包括Etag和x-cos-request-id等信息，也会包含设置的文件元信息。

### 获取文件列表

#### 功能说明
获取指定Bucket下的所有Objects。


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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* Delimiter —— (string)  可选参数，默认为空，设置分隔符。
* Marker —— (string) ： 可选参数，默认以 UTF-8 二进制顺序列出条目，标记返回objects的list的起点位置。
* MaxKeys —— (int) ： 可选参数，最多返回的objects数量，默认为最大的1000。
* Prefix —— (string) ： 可选参数，默认为空，对object的key进行筛选，匹配prefix为前缀的objects。
* EncodingType —— (string) ：可选参数，默认不编码，规定返回值的编码方式，可选值：url。
#### 返回结果说明

获取objects的元信息，类型为dict：

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

* Contents —— (list) ： 包含所有objects元信息的list，包括'ETag'，'StorageClass'，'Key'，'Owner'，'LastModified'，'Size'等信息。

### 创建分块上传

#### 功能说明
创建一个新的分块上传任务，返回UploadId。


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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* Key —— (string) ：必选参数，上传文件的路径名，默认从Bucket开始。
* StorageClass —— (string) ： 可选参数，设置文件的存储类型，STANDARD,STANDARD_IA，NEARLINE，默认值：STANDARD。
* Expires —— (string): 可选参数，设置Content-Expires。
* CacheControl —— (string) ： 可选参数，缓存策略，设置Cache-Control。
* ContentType —— (string) ： 可选参数，内容类型，设置Content-Type。
* ContentDisposition —— (string) ： 可选参数，文件名称，设置Content-Disposition。
* ContentEncoding —— (string) ： 可选参数，编码格式，设置Content-Encoding。
* ContentLanguage —— (string) ： 可选参数，语言类型，设置Content-Language。
* Metadata —— （dict) ： 可选参数，用户自定义的文件元信息。
#### 返回结果说明

获取分块上传的初始化信息，类型为dict：

```python
{
    'UploadId': '150219101333cecfd6718d0caea1e2738401f93aa531a4be7a2afee0f8828416f3278e5570',
    'Bucket': 'test01-123456789', 
    'Key': 'multipartfile.txt' 
}

```

* UploadId —— (string) ： 标识分块上传的ID。
* Bucket —— (String) ： Bucket名称，由bucket-appid组成。
* Key —— (string) ： 上传文件的路径名。

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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* Key —— (string) ： 必选参数，上传文件的路径名，默认从Bucket开始。
* UploadId —— (string) ： 必选参数，标识分块上传的ID。
#### 返回结果说明

该方法返回值为None。

### 上传分块

#### 功能说明
上传一个分块到指定的UploadId中，单个大小不得超过5GB。


#### 方法原型

```
upload_part(Bucket, Key, Body, PartNumber, UploadId, **kwargs)
```
#### 请求示例

```python
# 注意，上传分块的块数最多10000块
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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* Key —— (string) ： 必选参数，上传分块的路径名，默认从Bucket开始。
* Body —— (string) ： 必选参数，上传分块的内容，可以为本地文件流或输入流。
* PartNumber —— (string) ： 必选参数，标识上传分块的序号。
* UploadId —— (string) ： 必选参数，标识分块上传的ID。
* ContentLength —— (int) ： 可选参数，设置传输长度。
* ContentMD5 —— (string) ： 可选参数，设置上传文件的MD5值用于校验。
#### 返回结果说明

上传分块的属性，类型为dict：

```python
{
    'ETag': 'string'
}
```

* ETag —— （string) ：上传分块的MD5值。

### 列出上传分块

#### 功能说明
列出指定UploadId中已经上传的分块的信息。


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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* Key —— (string) ： 必选参数，上传分块的路径名，默认从Bucket开始。
* UploadId —— (string) ： 必选参数，标识分块上传的ID。
* MaxParts —— (int) ： 可选参数，最多返回的分块的数量，默认为最大的1000。
* PartNumberMarker —— (int) ： 可选参数，默认为0,从第一块列出分块，从PartNumberMarker下一个分块开始列出。
* EncodingType —— (string) ：可选参数，默认不编码，规定返回值的编码方式，可选值：url。
#### 返回结果说明

所有上传分块的信息，类型为dict：

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

* Bucket —— (string) ： Bucket名称。
* Part —— （string) ：上传分块的相关信息，包括ETag，PartNumber，Size，LastModified。
* UploadId —— (string) ： 标识分块上传的ID。
* Key —— (string) ： 上传分块的路径名。

### 完成分块上传

#### 功能说明
组装指定UploadId中所有的分块为一个完整的文件，文件最终大小必须大于1MB，否则会返回错误。

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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* Key —— (string) ： 必选参数，上传分块的路径名，默认从Bucket开始。
* UploadId —— (string) ： 必选参数，标识分块上传的ID。
* MultipartUpload —— (dict) ： 必选参数，所有分块的ETag和PartNumber信息。
#### 返回结果说明

组装后的文件的相关信息，类型为dict：

```python
{
    'ETag': '"3f866d0050f044750423e0a4104fa8cf-2"', 
    'Bucket': 'test01', 
    'Location': 'test01-123456789.cn-north.myqcloud.com/multipartfile.txt', 
    'Key': 'multipartfile.txt'
}
```

* ETag —— （string) ：组装后的文件的MD5值。
* Bucket —— （string) ：Bucket名称，由数字和小写字母以及中划线"-"构成。
* Location —— （string) ：URL地址。
* Key —— （string) ：上传分块的路径名。

### 设置Object ACL信息

#### 功能说明

设置文件的ACL信息, 通过ACL，GrantFullControl，GrantRead，GrantWriteheader传入header的方式来设置ACL，或者通过AccessControlPolicy传入body来设置ACL，两种方式只能选择一种，否则会返回冲突。

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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* Key —— (string) ： 必选参数，待设置ACL信息的文件路径。
* ACL —— (String) ： 可选参数，设置文件的ACL，如'private，public-read'，'public-read-write'。
* GrantFullControl —— (string) ：可选参数，赋予指定账户对文件的读写权限。
* GrantRead —— (string) ：可选参数，赋予指定账户对文件读权限。
* GrantWrite —— (string) ：可选参数，赋予指定账户对文件的写权限。
* AccessControlPolicy —— (dict) ：可选参数，赋予指定账户对文件的访问权限。


#### 返回结果说明

该方法返回值为None。

### 获取Object ACL信息

#### 功能说明

获取指定文件的ACL信息。

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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* Key —— (string) ： 必选参数，待获取ACL信息的文件路径。


#### 返回结果说明

Bucket ACL信息，类型为dict。
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
* Owner —— (dict) ：文件拥有者的信息，包括DisplayName和ID。
* Grant —— (list) ：文件权限授予者的信息，包括Grantee和Permission。
* Grantee —— (dict) ：文件权限授予者的信息，包括DisplayName，Type，ID和URI。
* DisplayName —— (string) ：权限授予者的名字。
* Type —— (string) ：权限授予者的类型，类型为CanonicalUser或者Group。
* ID —— (string) ：Type为CanonicalUser时，对应权限授予者的ID。
* URI —— (string) ：Type为Group时，对应权限授予者的URI。
* Permission —— (string) ：授予者所拥有的文件的权限，可选值有FULL_CONTROL，WRITE，READ，分别对应读写权限、写权限、读权限。

### 文件拷贝

#### 功能说明

将一个文件从源路径复制到目标路径，在拷贝的过程中，文件元属性和ACL可以被修改。


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

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* Key —— (string) ：必选参数，上传文件的路径名，默认从Bucket开始。
* CopySource —— (dict) ：必选参数，描述拷贝源文件的路径，包含Appid、Bucket、Key、Region。
* CopyStatus —— (string) ：必选参数，可选值为'COPY','REPLACE'，设置为'COPY'时，忽略设置的用户元数据信息直接复制，设置为'Replaced'时，按设置的元信息修改元数据，当目标路径和源路径一样时，必须设置为'REPLACE'。
* ACL —— (String) ： 可选参数，设置文件的ACL，如'private，public-read'，'public-read-write'。
* GrantFullControl —— (string) ：可选参数，赋予指定账户对文件的读写权限。
* GrantRead —— (string) ：可选参数，赋予指定账户对文件读权限。
* GrantWrite —— (string) ：可选参数，赋予指定账户对文件的写权限。
* StorageClass —— (string) ： 可选参数，设置文件的存储类型，STANDARD,STANDARD_IA，NEARLINE，默认值：STANDARD。
* Expires —— (string): 可选参数，设置Content-Expires。
* CacheControl —— (string) ： 可选参数，缓存策略，设置Cache-Control。
* ContentType —— (string) ： 可选参数，内容类型，设置Content-Type。
* ContentDisposition —— (string) ： 可选参数，文件名称，设置Content-Disposition。
* ContentEncoding —— (string) ： 可选参数，编码格式，设置Content-Encoding。
* ContentLanguage —— (string) ： 可选参数，语言类型，设置Content-Language。
* Metadata —— （dict) ： 可选参数，用户自定义的文件元信息。
#### 返回结果说明

上传文件的属性，类型为dict：

```python
{
    'ETag': 'string',
    'LastModified': 'string',
}
```

* ETag —— (string) ：拷贝文件的MD5值。
* LastModified —— (string) ：拷贝文件的最后一次修改时间。

## 异常类型
包括CosClientError和CosServiceError，分别对应SDK客户端错误和COS服务端错误。

### CosClientError
CosClientError一般指如timeout引起的客户端错误，用户捕获后可以选择重试或其它操作。

### CosServiceError
CosServiceError提供服务端返回的具体信息。

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
