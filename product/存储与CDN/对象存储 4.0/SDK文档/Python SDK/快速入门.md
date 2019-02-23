## 开发准备

### 相关资源
对象存储的 XML Python SDK  资源下载地址： [XML Python SDK ](https://github.com/tencentyun/cos-python-sdk-v5)。
演示示例 Demo 下载地址：[XML Python Demo](https://github.com/tencentyun/cos-python-sdk-v5/blob/master/qcloud_cos/demo.py)。

### 环境依赖

对象存储的 XML Python SDK  目前可以支持 Python 2.6、Python 2.7 以及 Python 3.x。
>?关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)。

### 安装 SDK

安装 SDK 有三种安装方式：pip 安装、手动安装和离线安装。

#### 使用 pip 安装（推荐）
```sh
 pip install -U cos-python-sdk-v5
```

#### 手动安装
从 [XML Python SDK](https://github.com/tencentyun/cos-python-sdk-v5) 下载源码，通过 setup 手动安装，执行以下命令。
```python
 python setup.py install
```
#### 离线安装
```python
# 在有外网的机器下运行如下命令
mkdir cos-python-sdk-packages
pip download cos-python-sdk-v5 -d cos-python-sdk-packages
tar -czvf cos-python-sdk-packages.tar.gz cos-python-sdk-packages

# 将安装包拷贝到没有外网的机器后运行如下命令
# 请确保两台机器的 python 版本保持一致，否则会出现安装失败的情况
tar -xzvf cos-python-sdk-packages.tar.gz
pip install cos-python-sdk-v5 --no-index -f cos-python-sdk-packages
```
 
## 快速入门
请参考以下示例代码：
```python
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
region = 'ap-beijing-1'     # 替换为用户的 Region
token = None                # 使用临时密钥需要传入 Token，默认为空，可不填
scheme = 'https'            # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
# 2. 获取客户端对象
client = CosS3Client(config)
# 参照下文的描述。或者参照 Demo 程序，详见 https://github.com/tencentyun/cos-python-sdk-v5/blob/master/qcloud_cos/demo.py
```

关于临时密钥如何生成和使用，请参考 [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048)。

## 文件上传
### 文件流简单上传
```python
file_name = 'test.txt'
# 强烈建议您以二进制模式(binary mode)打开文件,否则可能会导致错误
with open('test.txt', 'rb') as fp:
    response = client.put_object(
        Bucket='test04-123456789',
        Body=fp,
        Key=file_name,
        StorageClass='STANDARD',
        EnableMD5=False
    )
print(response['ETag'])
```
#### 参数说明
| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket| Bucket 名称，由 bucketname-appid 构成|String |是 | 
|  Body | 上传文件的内容，可以为文件流或字节流|file/bytes|是 | 
|  Key |  对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 ` bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg ` 中，对象键为 doc1/pic1.jpg |String|是 | 
|  StorageClass | 设置文件的存储类型，STANDARD，STANDARD_IA，默认值：STANDARD| String |否| 
| EnableMD5 | 是否需要 SDK 计算 Content-MD5，默认关闭，打开后会增加上传耗时|Bool | 否| 

更多可选参数详见 [Python SDK 接口文档](https://cloud.tencent.com/document/product/436/12270)。

### 字节流简单上传
```python
response = client.put_object(
    Bucket='test04-123456789',
    Body=b'abcdefg',
    Key=file_name,
    EnableMD5=False
)
print(response['ETag'])

```
### chunk 简单上传
```python
import requests
stream = requests.get('https://cloud.tencent.com/document/product/436/7778')

# 网络流将以 Transfer-Encoding:chunked 的方式传输到 COS
response = client.put_object(
    Bucket='test04-123456789',
    Body=stream,
    Key=file_name
)
print(response['ETag'])
```

### 本地路径简单上传
```python
response = client.put_object_from_local_file(
    Bucket='test04-123456789',
    LocalFilePath='local.txt',
    Key=file_name,
    EnableMD5=False
)
print(response['ETag'])
```

### 设置 HTTP 头部简单上传
```python
response = client.put_object(
    Bucket='test04-123456789',
    Body=b'test',
    Key=file_name,
    ContentType='text/html; charset=utf-8',
    EnableMD5=False
)
print(response['ETag'])
```

### 设置自定义头部简单上传
```python
response = client.put_object(
    Bucket='test04-123456789',
    Body=b'test',
    Key=file_name,
    Metadata={
        'x-cos-meta-key1': 'value1',
        'x-cos-meta-key2': 'value2'
    },
    EnableMD5=False
)
print(response['ETag'])
```

### 高级上传接口（推荐）
根据文件大小自动选择简单上传或分块上传，分块上传具备断点续传功能。
```python
response = client.upload_file(
    Bucket='test04-123456789',
    LocalFilePath='local.txt',
    Key=file_name,
    PartSize=10,
    MAXThread=10,
    EnableMD5=False
)
print(response['ETag'])
```

## 文件下载
### 获取文件到本地
```python
response = client.get_object(
    Bucket='test04-123456789',
    Key=file_name,
)
response['Body'].get_stream_to_file('output.txt')
```
#### 参数说明
| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|  Bucket |  存储桶名称，由 bucketname-appid 构成|String|是 |
| Key | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg 中，对象键为 doc1/pic1.jpg |string| 是 |

更多可选参数详见 [Python SDK 接口文档](https://cloud.tencent.com/document/product/436/12270)。

### 获取文件流
```python
response = client.get_object(
    Bucket='test04-123456789',
    Key=file_name,
)
fp = response['Body'].get_raw_stream()
print(fp.read(2))
```

### 设置 Response HTTP 头部
```python
response = client.get_object(
    Bucket='test04-123456789',
    Key=file_name,
    ResponseContentType='text/html; charset=utf-8'
)
print response['Content-Type']
fp = response['Body'].get_raw_stream()
print(fp.read(2))
```

### 指定下载范围
```python
response = client.get_object(
    Bucket='test04-123456789',
    Key=file_name,
    Range='bytes=0-10'
)
fp = response['Body'].get_raw_stream()
print(fp.read())
```
## 异常类型
包括 CosClientError 和 CosServiceError，分别对应 SDK 客户端错误和 COS 服务端错误。

### CosClientError
CosClientError 一般指如 timeout 引起的客户端错误，用户捕获后可以选择重试或其它操作。

### CosServiceError
CosServiceError 提供服务端返回的具体信息。
```python
#except CosServiceError as e
e.get_origin_msg()  # 获取原始错误信息，格式为 XML
e.get_digest_msg()  # 获取处理过的错误信息，格式为 dict
e.get_status_code() # 获取 http 错误码（如4XX,5XX)
e.get_error_code()  # 获取 COS 定义的错误码
e.get_error_msg()   # 获取 COS 错误码的具体描述
e.get_trace_id()    # 获取请求的 trace_id
e.get_request_id()  # 获取请求的 request_id
e.get_resource_location() # 获取 URL 地址
```
