## 简介
Python SDK 提供获取签名、预签名 URL 、下载预签名 URL 的接口，用于将请求分发使用。
使用永久密钥或临时密钥获取预签名 URL 的调用方法相同，使用临时密钥时需要在 header 或 query_string 中加上 x-cos-security-token。

>?
> - 在获取签名时强烈建议将敏感请求头和请求参数算入签名，这样可以避免相关请求头和请求参数被使用者篡改，杜绝权限越界的情况发生。同时 SDK 会默认将请求域名算入签名，如果分发后修改了访问域名会导致访问失败，此时可以在获取签名时传入参数忽略请求域名，详细方法参见下面的请求示例。 
> - 建议用户使用临时密钥生成预签名，通过临时授权的方式进一步提高预签名上传、下载等请求的安全性。申请临时密钥时，请遵循 [最小权限指引原则](https://cloud.tencent.com/document/product/436/38618)，防止泄漏目标存储桶或对象之外的资源。
> - 如果您一定要使用永久密钥来生成预签名，建议永久密钥的权限范围仅限于上传或下载操作，以规避风险。
> 

## 获取预签名 URL

#### 功能说明

获取预签名链接用于分发。

#### 方法原型

```
get_presigned_url(Bucket, Key, Method, Expired=300, Params={}, Headers={})
```

#### 请求示例1：生成上传预签名 URL

```python
# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
import requests

# 正常情况日志级别使用INFO，需要定位时可以修改为DEBUG，此时SDK会打印和服务端的通信信息
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 1. 设置用户属性, 包括 secret_id, secret_key, region等。Appid 已在CosConfig中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
secret_id = 'SecretId'     # 替换为用户的 SecretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
secret_key = 'SecretKey'   # 替换为用户的 SecretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
region = 'ap-beijing'      # 替换为用户的 region，已创建桶归属的region可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
                           # COS支持的所有region列表参见https://cloud.tencent.com/document/product/436/6224
token = None               # 如果使用永久密钥不需要填入token，如果使用临时密钥需要填入，临时密钥生成和使用指引参见https://cloud.tencent.com/document/product/436/14048
scheme = 'https'           # 指定使用 http/https 协议来访问 COS，默认为 https，可不填

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)

# 生成上传URL，未限制头域和请求参数
url = client.get_presigned_url(
    Method='PUT',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Expired=120  # 120秒后过期，过期时间请根据自身场景定义
)
print(url)

# 生成上传URL，同时限制存储类型和上传速度
url = client.get_presigned_url(
    Method='PUT',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Headers={'x-cos-storage-class':'STANDARD_IA', 'x-cos-traffic-limit':'819200'},
    Expired=300  # 300秒后过期，过期时间请根据自身场景定义
)
print(url)

# 生成上传URL，只能上传指定的文件内容
url = client.get_presigned_url(
    Method='PUT',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Headers={'Content-MD5':'string'}, 
    Expired=300  # 300秒后过期，过期时间请根据自身场景定义
)
print(url)

# 生成上传URL，只能用于上传ACL
url = client.get_presigned_url(
    Method='PUT',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Params={'acl':''},
    Expired=120  # 120秒后过期，过期时间请根据自身场景定义
)
print(url)

# 生成上传URL，请求域名不算入签名，签名后使用者需要修改请求域名时使用
url = client.get_presigned_url(
    Method='PUT',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    SignHost=False, # 请求域名不算入签名，允许使用者修改请求域名，有一定安全风险
    Expired=120  # 120秒后过期，过期时间请根据自身场景定义
)
print(url)

# 使用上传URL
response = requests.put(url)
print(response)
```

#### 请求示例2：生成下载预签名 URL

```python
# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
import requests

# 正常情况日志级别使用INFO，需要定位时可以修改为DEBUG，此时SDK会打印和服务端的通信信息
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 1. 设置用户属性, 包括 secret_id, secret_key, region等。Appid 已在CosConfig中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
secret_id = 'SecretId'     # 替换为用户的 SecretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
secret_key = 'SecretKey'   # 替换为用户的 SecretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
region = 'ap-beijing'      # 替换为用户的 region，已创建桶归属的region可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
                           # COS支持的所有region列表参见https://cloud.tencent.com/document/product/436/6224
token = None               # 如果使用永久密钥不需要填入token，如果使用临时密钥需要填入，临时密钥生成和使用指引参见https://cloud.tencent.com/document/product/436/14048
scheme = 'https'           # 指定使用 http/https 协议来访问 COS，默认为 https，可不填

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)

# 生成下载URL，未限制头域和请求参数
url = client.get_presigned_url(
    Method='GET',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Expired=120  # 120秒后过期，过期时间请根据自身场景定义
)
print(url)

# 生成下载URL，同时限制下载速度
url = client.get_presigned_url(
    Method='GET',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Headers={'x-cos-traffic-limit':'819200'},
    Expired=300  # 300秒后过期，过期时间请根据自身场景定义
)
print(url)

# 生成下载URL，只能用于下载ACL
url = client.get_presigned_url(
    Method='GET',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Params={'acl':''},
    Expired=120  # 120秒后过期，过期时间请根据自身场景定义
)
print(url)

# 生成下载URL，请求域名不算入签名，签名后使用者需要修改请求域名时使用
url = client.get_presigned_url(
    Method='GET',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    SignHost=False, # 请求域名不算入签名，允许使用者修改请求域名，有一定安全风险
    Expired=120  # 120秒后过期，过期时间请根据自身场景定义
)
print(url)

# 使用下载URL
response = requests.get(url)
print(response)
```

#### 请求示例3：使用临时密钥生成下载预签名 URL

```python
# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
import requests

# 正常情况日志级别使用INFO，需要定位时可以修改为DEBUG，此时SDK会打印和服务端的通信信息
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 1. 设置用户属性, 包括 secret_id, secret_key, region等。Appid 已在CosConfig中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
secret_id = 'SecretId'     # 替换为用户的 SecretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
secret_key = 'SecretKey'   # 替换为用户的 SecretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
region = 'ap-beijing'      # 替换为用户的 region，已创建桶归属的region可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
                           # COS支持的所有region列表参见https://cloud.tencent.com/document/product/436/6224
token = None               # 如果使用永久密钥不需要填入token，如果使用临时密钥需要填入，临时密钥生成和使用指引参见https://cloud.tencent.com/document/product/436/14048
scheme = 'https'           # 指定使用 http/https 协议来访问 COS，默认为 https，可不填

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)

# 生成下载URL
url = client.get_presigned_url(
    Method='GET',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Headers={'x-cos-traffic-limit':'819200'}, # 限制下载速度
    Params={
        'x-cos-security-token': 'string' # 使用临时密钥需要填入Token到请求参数
    },
    Expired=120,  # 120秒后过期，过期时间请根据自身场景定义
    SignHost=False # 请求域名不算入签名，签名后使用者需要修改请求域名时使用，有一定安全风险
)
print(url)

# 使用下载URL
response = requests.get(url)
print(response)
```

#### 全部参数请求示例

```python
response = client.get_presigned_url(
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Method='PUT'|'POST'|'GET'|'DELETE'|'HEAD',
    Expired=300,
    Headers={
        'header1': 'string',
        'header2': 'string',
    },
    Params={
        'param1': 'string',
        'param2': 'string'
    },
    SignHost=True|False
)
```

#### 参数说明

| 参数名称   | 参数描述   |类型 | 是否必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket  |存储桶名称，由 BucketName-APPID 构成 |  String |  是 | 
| Key  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg` 中，对象键为 doc/pic.jpg | String | 是 | 
| Method  |对应操作的 Method, 可选值为 'PUT'，'POST'，'GET'，'DELETE'，'HEAD'|  String |  是 | 
|Expired| 签名过期时间，单位为秒| Int| 否|
|Params| 签名中要签入的请求参数| Dict| 否|
|Headers| 签名中要签入的请求头部| Dict| 否|
|SignHost | 请求域名是否算入签名，默认值True，签名后使用者需要修改请求域名时设置为False| Bool| 否|

可以签入的Header、Params和具体的方法相关，例如上传对象可以签入的Headers参见 [PUT Object 中的请求头](https://cloud.tencent.com/document/product/436/7749#.E8.AF.B7.E6.B1.82)描述，下载对象可以签入的Headers和Params参见 [GET Object 中的请求参数和请求头](https://cloud.tencent.com/document/product/436/7753#.E8.AF.B7.E6.B1.82)描述。

#### 返回结果说明

该方法返回值为预签名的 URL。

## 获取预签名下载 URL

#### 功能说明
获取预签名下载链接用于直接下载。

#### 方法原型

```
get_presigned_download_url(Bucket, Key, Expired=300, Params={}, Headers={})
```

#### 请求示例

```python
# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging
import requests

# 正常情况日志级别使用INFO，需要定位时可以修改为DEBUG，此时SDK会打印和服务端的通信信息
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 1. 设置用户属性, 包括 secret_id, secret_key, region等。Appid 已在CosConfig中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
secret_id = 'SecretId'     # 替换为用户的 SecretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
secret_key = 'SecretKey'   # 替换为用户的 SecretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
region = 'ap-beijing'      # 替换为用户的 region，已创建桶归属的region可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
                           # COS支持的所有region列表参见https://cloud.tencent.com/document/product/436/6224
token = None               # 如果使用永久密钥不需要填入token，如果使用临时密钥需要填入，临时密钥生成和使用指引参见https://cloud.tencent.com/document/product/436/14048
scheme = 'https'           # 指定使用 http/https 协议来访问 COS，默认为 https，可不填

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)

# 生成下载URL，未限制头域和请求参数
url = client.get_presigned_download_url(
    Method='GET',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Expired=120  # 120秒后过期，过期时间请根据自身场景定义
)
print(url)

# 生成下载URL，同时限制下载速度
url = client.get_presigned_download_url(
    Method='GET',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Headers={'x-cos-traffic-limit':'819200'},
    Expired=300  # 300秒后过期，过期时间请根据自身场景定义
)
print(url)

# 生成下载URL，只能用于下载ACL
url = client.get_presigned_download_url(
    Method='GET',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Params={'acl':''},
    Expired=120  # 120秒后过期，过期时间请根据自身场景定义
)
print(url)

# 生成下载URL，请求域名不算入签名，签名后使用者需要修改请求域名时使用
url = client.get_presigned_download_url(
    Method='GET',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    SignHost=False, # 请求域名不算入签名，允许使用者修改请求域名，有一定安全风险
    Expired=120  # 120秒后过期，过期时间请根据自身场景定义
)
print(url)

# 生成下载URL，使用临时密钥签名
url = client.get_presigned_download_url(
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Params={
        'x-cos-security-token': 'string'  # 使用永久密钥不需要填入token，如果使用临时密钥需要填入
    }
)
print(url)

# 使用下载URL
response = requests.get(url)
print(response)
```

#### 全部参数请求示例

```python
response = client.get_presigned_download_url(
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Expired=300,
    Headers={
        'header1': 'string'
    },
    Params={
        'param1': 'string',
        'param2': 'string'
    },
    SignHost=True|False
)
```

#### 参数说明

| 参数名称   | 参数描述   |类型 | 是否必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket  |存储桶名称，由 BucketName-APPID 构成 |  String |  是 | 
| Key  | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg` 中，对象键为 doc/pic.jpg | String | 是 | 
|Expired| 签名过期时间，单位为秒| Int| 否|
|Params| 签名中要签入的请求参数| Dict| 否|
|Headers| 签名中要签入的请求头部| Dict| 否|
|SignHost | 请求域名是否算入签名，默认值True，签名后使用者需要修改请求域名时设置为False| Bool| 否|

可以签入的Header、Params和具体的方法相关，例如上传对象可以签入的Headers参见 [PUT Object 中的请求头](https://cloud.tencent.com/document/product/436/7749#.E8.AF.B7.E6.B1.82)描述，下载对象可以签入的Headers和Params参见 [GET Object 中的请求参数和请求头](https://cloud.tencent.com/document/product/436/7753#.E8.AF.B7.E6.B1.82)描述。

#### 返回结果说明

该方法返回值为预签名的下载 URL。

## 获取签名

#### 功能说明
获取指定操作的签名，常用于移动端的签名分发。

#### 方法原型

```
get_auth(Method, Bucket, Key, Expired=300, Headers={}, Params={})
```

#### 请求示例1：生成上传签名

```python
# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging

# 正常情况日志级别使用INFO，需要定位时可以修改为DEBUG，此时SDK会打印和服务端的通信信息
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 1. 设置用户属性, 包括 secret_id, secret_key, region等。Appid 已在CosConfig中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
secret_id = 'SecretId'     # 替换为用户的 SecretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
secret_key = 'SecretKey'   # 替换为用户的 SecretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
region = 'ap-beijing'      # 替换为用户的 region，已创建桶归属的region可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
                           # COS支持的所有region列表参见https://cloud.tencent.com/document/product/436/6224
token = None               # 如果使用永久密钥不需要填入token，如果使用临时密钥需要填入，临时密钥生成和使用指引参见https://cloud.tencent.com/document/product/436/14048
scheme = 'https'           # 指定使用 http/https 协议来访问 COS，默认为 https，可不填

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)

# 生成上传签名，未限制头域和请求参数
response = client.get_auth(
    Method='PUT',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Expired=120  # 120秒后过期，过期时间请根据自身场景定义
)
print(response)

# 生成上传签名，同时限制存储类型和上传速度
response = client.get_auth(
    Method='PUT',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Headers={'x-cos-storage-class':'STANDARD_IA', 'x-cos-traffic-limit':'819200'},
    Expired=300  # 300秒后过期，过期时间请根据自身场景定义
)
print(response)

# 生成上传URL，只能上传指定的文件内容
response = client.get_auth(
    Method='PUT',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Headers={'Content-MD5':'string'}, 
    Expired=300  # 300秒后过期，过期时间请根据自身场景定义
)
print(response)

# 生成上传签名，只能用于上传ACL
response = client.get_auth(
    Method='PUT',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Params={'acl':''},
    Expired=120  # 120秒后过期，过期时间请根据自身场景定义
)
print(response)

# 生成上传签名，请求域名不算入签名，签名后使用者需要修改请求域名时使用
response = client.get_auth(
    Method='PUT',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    SignHost=False, # 请求域名不算入签名，允许使用者修改请求域名，有一定安全风险
    Expired=120  # 120秒后过期，过期时间请根据自身场景定义
)
print(response)
```

#### 请求示例2：生成下载签名

```python
# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging

# 正常情况日志级别使用INFO，需要定位时可以修改为DEBUG，此时SDK会打印和服务端的通信信息
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 1. 设置用户属性, 包括 secret_id, secret_key, region等。Appid 已在CosConfig中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
secret_id = 'SecretId'     # 替换为用户的 SecretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
secret_key = 'SecretKey'   # 替换为用户的 SecretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
region = 'ap-beijing'      # 替换为用户的 region，已创建桶归属的region可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
                           # COS支持的所有region列表参见https://cloud.tencent.com/document/product/436/6224
token = None               # 如果使用永久密钥不需要填入token，如果使用临时密钥需要填入，临时密钥生成和使用指引参见https://cloud.tencent.com/document/product/436/14048
scheme = 'https'           # 指定使用 http/https 协议来访问 COS，默认为 https，可不填

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)


# 生成下载签名，未限制头域和请求参数
response = client.get_auth(
    Method='GET',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Expired=120  # 120秒后过期，过期时间请根据自身场景定义
)
print(response)

# 生成下载签名，同时限制下载速度
response = client.get_auth(
    Method='GET',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Headers={'x-cos-traffic-limit':'819200'},
    Expired=300  # 300秒后过期，过期时间请根据自身场景定义
)
print(response)

# 生成下载签名，只能用于下载ACL
response = client.get_auth(
    Method='GET',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Params={'acl':''},
    Expired=120  # 120秒后过期，过期时间请根据自身场景定义
)
print(response)

# 生成下载签名，请求域名不算入签名，签名后使用者需要修改请求域名时使用
response = client.get_auth(
    Method='GET',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    SignHost=False, # 请求域名不算入签名，允许使用者修改请求域名，有一定安全风险
    Expired=120  # 120秒后过期，过期时间请根据自身场景定义
)
print(response)

# 生成下载签名，使用临时密钥签名
response = client.get_auth(
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Params={
        'x-cos-security-token': 'string'  # 使用永久密钥不需要填入token，如果使用临时密钥需要填入
    }
)
print(response)
```

#### 全部参数请求示例

```python
response = client.get_auth(
    Method='PUT'|'POST'|'GET'|'DELETE'|'HEAD',
    Bucket='examplebucket-1250000000',
    Key='exampleobject',
    Expired=300,
    Headers={
        'header1': 'string',
        'header2': 'string'
    },
    Params={
        'param1': 'string',
        'param2': 'string'
    },
    SignHost=True|False
)
```

#### 参数说明

| 参数名称   | 参数描述   |类型 | 是否必填 | 
| -------------- | -------------- |---------- | ----------- |
| Method  |对应操作的 Method, 可选值为 'PUT'，'POST'，'GET'，'DELETE'，'HEAD'|  String |  是 | 
| Bucket  |存储桶名称，由 BucketName-APPID 构成 |  String |  是 | 
| Key  | Bucket 操作填入根路径`/`，object 操作填入文件的路径| String | 是| 
|Expired| 签名过期时间，单位为秒| Int| 否|
|Headers| 需要签入签名的请求头部| Dict| 否|
|Params | 需要签入签名的请求参数| Dict| 否|
|SignHost | 请求域名是否算入签名，默认值True，签名后使用者需要修改请求域名时设置为False| Bool| 否|

可以签入的Header、Params和具体的方法相关，例如上传对象可以签入的Headers参见 [PUT Object 中的请求头](https://cloud.tencent.com/document/product/436/7749#.E8.AF.B7.E6.B1.82)描述，下载对象可以签入的Headers和Params参见 [GET Object 中的请求参数和请求头](https://cloud.tencent.com/document/product/436/7753#.E8.AF.B7.E6.B1.82)描述。

#### 返回结果说明

该方法返回值为对应操作的签名值。
