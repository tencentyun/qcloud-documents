如果您细心对比过 Python SDK V4 和 V5 的文档，您会发现并不是一个简单的增量更新。COS V5 在架构、可用性和安全性上有了非常大的提升，我们的 SDK 在易用性、健壮性和传输性能上也做了非常大的改进。如果您想要升级到 Python SDK V5，请参考下面的指引，一步步完成 SDK 的升级工作。

## 功能对比

下表列出了 V4 和 V5 SDK 的主要功能对比：

| 功能       | V5         | V4                         |
| -------- | :------------: | :------------------:    |
| 文件上传 | 支持本地文件、字节流、输入流上传<br>默认覆盖上传<br>智能判断上传模式，支持断点续传<br>简单上传最大支持5GB<br>分块上传最大支持50TB| 只支持本地文件上传<br>可选择是否覆盖<br>需要手动选择是简单还是分片上传<br>简单上传最大支持20MB<br>分片上传最大支持64GB|
| 文件删除 | 支持批量删除 | 只支持单文件删除 |
| 存储桶基本操作 | 创建存储桶<br>获取存储桶<br>删除存储桶   | 不支持 |
| 存储桶ACL操作 | 设置存储桶ACL<br>获取设置存储桶ACL<br>删除设置存储桶ACL   | 不支持 |
| 存储桶生命周期 | 创建存储桶生命周期<br>获取存储桶生命周期<br>删除存储桶生命周期 | 不支持 |
| 目录操作 | 不支持   | 创建目录<br>查询目录<br>删除目录 |


### 总览

1. 更新您的 Python SDK
2. 根据指引修改 SDK 的初始化方式
3. 我们的 `存储桶名称` 和 `可用区域简称` 有了更新，请对应修改
4. 一些操作的 API 发生了变化，我们做了封装让 SDK 更加易用，具体请参考我们的示例和 [接口文档](https://cloud.tencent.com/document/product/436/12270)

**1. 更新 Python SDK**

通过 pip 您可以非常方便的获取到最新的 COS Python SDK V5，请执行以下命令获取：
```
 pip uninstall qcloud_cos_v4

 pip install -U cos-python-sdk-v5
```

当然，您也可以根据官网的 [快速入门](https://cloud.tencent.com/document/product/436/12269) 选择合适您的安装方式。


**2. 更改 SDK 初始化**

在 V5 中，我们的初始化接口发生了一些变化：

* V5新增了CosConfig对象来管理您访问COS的配置,你可以方便的设置访问的协议HTTP/HTTPS,设置临时秘钥等信息。

v4的初始化方式如下：

```
secret_id = u'xxxxxxxx'      # 替换为用户的 secretId
secret_key = u'xxxxxxx'      # 替换为用户的 secretKey
region = 'sh'                # 替换为用户的 Region
appid = 100000               # 替换为用户的appid
cos_client = CosClient(appid, secret_id, secret_key, region=region)
```

v5的初始化方式如下：

```
# appid 已在配置中移除,请在参数 Bucket 中带上 appid。Bucket 由 bucketname-appid 组成
# 1. 设置用户配置, 包括 secretId，secretKey 以及 Region
# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

secret_id = 'xxxxxxxx'      # 替换为用户的 secretId
secret_key = 'xxxxxxx'      # 替换为用户的 secretKey
region = 'ap-shanghai'      # 替换为用户的 Region
token = None                # 使用临时密钥需要传入 Token，默认为空，可不填
scheme = 'https'            # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
# 2. 获取客户端对象
client = CosS3Client(config)
```


**3. 更改存储桶名称和可用区域简称**

SDK V5 的存储桶名称和可用区域简称与 SDK V4 的不同，需要您进行相应的更改。

- 存储桶 Bucket
在 V5 中，存储桶名称由两部分组成：用户自定义字符串 和 APPID，两者以中划线“-”相连。例如 `mybucket1-1250000000`，其中 `mybucket1` 为用户自定义字符串，`1250000000` 为 APPID。
>?APPID 是腾讯云账户的账户标识之一，用于关联云资源。在用户成功申请腾讯云账户后，系统自动为用户分配一个 APPID。可通过 腾讯云控制台 【账号信息】查看 APPID。

	在设置 Bucket 时，请参考下面的示例代码：

	```
	bucket = "mybucket1-1250000000"
	file_name = "test.txt"
	local_path = 'local.txt'
	response = client.upload_file(
			Bucket=bucket,
			LocalFilePath=local_path,
			Key=file_name
	)
	```

**存储桶可用区域简称 Region**

V5 的存储桶可用区域简称发生了变化，下面列出了不同区域在 V4 和 V5 中的对应关系：

| 地域       | V5 地域简称         | V4 地域简称                         |
| -------- | ------------ | ---------------------------------------- |
| 北京一区（华北） | ap-beijing-1 | tj |
| 北京       | ap-beijing   | bj |
| 上海（华东）   | ap-shanghai  | sh |
| 广州（华南）   | ap-guangzhou | gz |
| 成都（西南）   | ap-chengdu   | cd |
| 重庆       | ap-chongqing | 无 |
| 新加坡      | ap-singapore | sgp |
| 香港       | ap-hongkong  | hk |
| 多伦多      | na-toronto   | ca |
| 法兰克福     | eu-frankfurt | ger |
| 孟买       | ap-mumbai    | 无 |
| 首尔       | ap-seoul     | 无 |
| 硅谷       | na-siliconvalley     | 无 |
| 弗吉尼亚       | na-ashburn     | 无 |
| 曼谷       | ap-bangkok     | 无 |
| 莫斯科       | eu-moscow     | 无 |

在初始化时，请将存储桶所在区域简称设置到 `CosConfig` 中。



**4. 更改 API**
升级到 SDK V5之后，一些操作的 API 发生了变化，请您根据实际需求进行相应的更改。我们做了封装让 SDK 更加易用，具体请参考我们的示例和 接口文档。
API 变化有以下三点：

- 不再支持目录操作
在 V5 中，我们不再支持目录操作。

	对象存储中本身是没有文件夹和目录的概念的，对象存储不会因为上传对象 project/a.txt 而创建一个 project 文件夹。为了满足用户使用习惯，对象存储在控制台、COS browser 等图形化工具中模拟了「 文件夹」或「 目录」的展示方式，具体实现是通过创建一个键值为 project/，内容为空的对象，展示方式上模拟了传统文件夹。

	例如：上传对象 project/doc/a.txt ，分隔符 / 会模拟「 文件夹」的展示方式，于是可以看到控制台上出现「 文件夹」project 和 doc，其中 doc 是 project 下一级「 文件夹」，并包含了 a.txt 。

	因此，如果您的应用场景只是上传文件，可以直接上传即可，不需要先创建文件夹。

	如果您的使用场景里面有文件夹的概念，需要提供创建文件夹的功能，您可以上传一个路径以 '/' 结尾的 0KB 文件。这样在您调用 `GetBucket` 接口时，就可以将这样的文件当做文件夹。


**2）高级上传接口（推荐）**

在 V5 SDK 中，我们封装了高级上传接口，支持根据文件大小智能选择简单上传还是分片上传，分块上传具备断点续传功能, 同时您还可以设置线程数量来控制您的上传速度。

使用断点续传高级上传接口的示例代码如下：

```
response = client.upload_file(
    Bucket='test04-123456789',
    LocalFilePath='local.txt',
    Key=file_name,
    PartSize=10,
    MAXThread=10
)
```

**3）新增API**

V5 增加了很多新的API，包括：

* 存储桶的操作，如 create_bucket, delete_bucket, list_objects 等
* 存储桶ACL的操作，如 put_bucket_acl, get_bucket_acl 等
* 存储桶生命周期的操作，如 put_bucket_lifecycle, get_bucket_lifecycle 等

具体请参考我们的 [Python SDK 接口文档](https://cloud.tencent.com/document/product/436/12270)。
