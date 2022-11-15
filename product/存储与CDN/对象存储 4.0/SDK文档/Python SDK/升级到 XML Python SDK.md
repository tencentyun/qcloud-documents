如果您细心对比过 JSON Python SDK 和 XML Python SDK 的文档，您会发现并不是一个简单的增量更新。XML Python SDK 在架构、可用性和安全性上有了非常大的提升，而且在易用性、健壮性和传输性能上也做了非常大的改进。如果您想要升级到 XML Python SDK，请参考下面的指引，完成 Python SDK 的升级工作。

## 功能对比

下表列出了 JSON Python SDK 和 XML Python SDK 的主要功能对比：

| 功能       | XML Python SDK         | JSON Python SDK                         |
| -------- | :------------: | :------------------:    |
| 文件上传 | 支持本地文件、字节流、输入流上传<br>默认覆盖上传<br>智能判断上传模式，支持断点续传<br>简单上传最大支持5GB<br>分块上传最大支持48.82TB（50,000GB）| 只支持本地文件上传<br>可选择是否覆盖<br>需要手动选择是简单还是分片上传<br>简单上传最大支持20MB<br>分片上传最大支持64GB|
| 存储桶基本操作 | 创建存储桶<br>获取存储桶<br>删除存储桶   | 不支持 |
| 存储桶ACL操作 | 设置存储桶ACL<br>获取设置存储桶ACL<br>删除设置存储桶ACL   | 不支持 |
| 存储桶生命周期 | 创建存储桶生命周期<br>获取存储桶生命周期<br>删除存储桶生命周期 | 不支持 |
| 目录操作 | 不单独提供接口   | 创建目录<br>查询目录<br>删除目录 |


## 升级步骤
请按照下面4个步骤升级 Python SDK。
**1. 更新 Python SDK**

通过 pip 命令您可以方便获取到最新的 XML Python SDK：
```
pip uninstall qcloud_cos_v4

pip install -U cos-python-sdk-v5
```

此外，您也可以参考 Python SDK [快速入门](https://cloud.tencent.com/document/product/436/12269) 文档选择合适您的安装方式。


**2. 更改 SDK 初始化**

XML Python SDK 新增 CosConfig 对象来管理您访问 COS 的配置，您可以方便的设置访问协议 HTTP/HTTPS、临时密钥等信息。请根据以下示例进行 SDK 初始化。

JSON Python SDK 的初始化方式如下：

```python
secret_id = u'COS_SECRETID'      # 替换为用户的 secretId
secret_key = u'COS_SECRETKEY'      # 替换为用户的 secretKey
region = 'sh'                # 替换为用户的 Region
appid = 100000               # 替换为用户的 appid
cos_client = CosClient(appid, secret_id, secret_key, region=region)
```

XML Python SDK 的初始化方式如下：

```python
# appid 已在配置中移除,请在参数 Bucket 中带上 appid。Bucket 由 bucketname-appid 组成
# 1. 设置用户配置, 包括 secretId，secretKey 以及 Region
# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 1. 设置用户属性, 包括 secret_id, secret_key, region等。Appid 已在CosConfig中移除，请在参数 Bucket 中带上 Appid。Bucket 由 BucketName-Appid 组成
secret_id = 'SecretId'     # 替换为用户的 SecretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
secret_key = 'SecretKey'   # 替换为用户的 SecretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
region = 'ap-beijing'      # 替换为用户的 region，已创建桶归属的region可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
                           # COS支持的所有region列表参见https://cloud.tencent.com/document/product/436/6224
token = None               # 如果使用永久密钥不需要填入token，如果使用临时密钥需要填入，临时密钥生成和使用指引参见https://cloud.tencent.com/document/product/436/14048
scheme = 'https'           # 指定使用 http/https 协议来访问 COS，默认为 https，可不填

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)

# 2. 获取客户端对象
client = CosS3Client(config)
```


**3. 更改存储桶名称和可用区域简称**

XML Python SDK 的存储桶名称和可用区域简称与 JSON Python SDK 的不同，需要您进行相应的更改。

**存储桶 Bucket**
XML Python SDK 存储桶名称由两部分组成：用户自定义字符串 和 APPID，两者以中划线“-”相连。
例如 `mybucket1-1250000000`，其中 `mybucket1` 为用户自定义字符串，`1250000000` 为 APPID。
>?APPID 是腾讯云账户的账户标识之一，用于关联云资源。在用户成功申请腾讯云账户后，系统自动为用户分配一个 APPID。可登录腾讯云控制台后，在 [账号信息](https://console.cloud.tencent.com/developer) 查看 APPID。

设置 Bucket ，请参考以下示例代码：
```python
bucket = "examplebucket-1250000000"
file_name = "test.txt"
local_path = 'local.txt'
response = client.upload_file(
    Bucket=bucket,
    LocalFilePath=local_path,
    Key=file_name
)
```


**存储桶可用区域简称 Region**

XML Python SDK 的存储桶可用区域简称发生了变化，在初始化时，请将存储桶所在区域简称设置到 CosConfig 中。不同区域在 JSON Python SDK 和 XML Python SDK 中的对应关系请查看下表：

| 地域       | XML Python SDK 地域简称         | JSON Python SDK 地域简称                         |
| -------- | ------------ | ---------------------------------------- |
| 北京一区（华北） | ap-beijing-1 | tj |
| 北京       | ap-beijing   | bj |
| 上海（华东）   | ap-shanghai  | sh |
| 广州（华南）   | ap-guangzhou | gz |
| 成都（西南）   | ap-chengdu   | cd |
| 重庆       | ap-chongqing | 无 |
| 香港       | ap-hongkong  | hk |
| 新加坡      | ap-singapore | sgp |
| 多伦多      | na-toronto   | ca |
| 法兰克福     | eu-frankfurt | ger |
| 孟买       | ap-mumbai    | 无 |
| 首尔       | ap-seoul     | 无 |
| 硅谷       | na-siliconvalley     | 无 |
| 弗吉尼亚       | na-ashburn     | 无 |
| 曼谷       | ap-bangkok     | 无 |
| 莫斯科       | eu-moscow     | 无 |


**4. 更改 API**
升级到 XML Python SDK 之后，一些操作的 API 发生了变化，请您根据实际需求进行相应的更改。同时我们做了封装让 SDK 更加易用，具体请参考我们的示例和 [快速入门](https://cloud.tencent.com/document/product/436/12269) 文档。
API 变化有以下四点：

**（1）没有单独的目录接口**

在 XML SDK 中，不再提供单独的目录接口。对象存储中本身是没有文件夹和目录的概念的，对象存储不会因为上传对象`project/a.txt` 而创建一个 project 文件夹。为了满足用户使用习惯，对象存储在控制台、COS browser 等图形化工具中模拟了「文件夹」或「目录」的展示方式，具体实现是通过创建一个键值为 `project/`，内容为空的对象，在展示方式上模拟了传统文件夹。

例如：上传对象`project/doc/a.txt`，分隔符`/`会模拟「文件夹」的展示方式，于是可以看到控制台上出现「文件夹」project 和 doc，其中 doc 是 project 下一级「文件夹」，并包含 a.txt 文件。

因此，如果您的应用场景只是上传文件，可以直接上传即可，不需要先创建文件夹。使用场景里面有文件夹的概念，则需要提供创建文件夹的功能，您可以上传一个路径以`/`结尾的0KB 文件。这样在您调用 GetBucket 接口时，就可以将该文件当做文件夹。



**（2）高级上传接口**

在 XML SDK 中，我们封装了高级上传接口，该接口支持根据文件大小智能选择简单上传还是分块上传，分块上传具备断点续传功能，同时您还可以设置线程数量来控制您的上传速度。

使用高级上传接口断点续传示例代码如下：

```python
response = client.upload_file(
    Bucket='examplebucket-1250000000',
    LocalFilePath='local.txt',
    Key=file_name,
    PartSize=10,
    MAXThread=10
)
```

**（3）签名算法不同**

通常您不需要手动计算签名，但如果您将 SDK 的签名返回给前端使用，请注意我们的签名算法发生了改变。签名不再区分单次和多次签名，而是通过设置签名的有效期来保证安全性。具体的算法请参考 [XML 请求签名](https://cloud.tencent.com/document/product/436/7778) 文档。

**（4）新增 API**

XML Python SDK 新增 API，您可根据需求进行调用。包括：

* 存储桶的操作，如 create_bucket、delete_bucket、list_objects 等。
* 存储桶 ACL 的操作，如 put_bucket_acl、get_bucket_acl 等。
* 存储桶生命周期的操作，如 put_bucket_lifecycle、get_bucket_lifecycle 等。

阅读更多请参考我们的 Python SDK [快速入门](https://cloud.tencent.com/document/product/436/12269) 文档。

