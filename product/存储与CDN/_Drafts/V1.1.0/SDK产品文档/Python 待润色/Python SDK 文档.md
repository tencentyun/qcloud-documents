## 开发准备

### 相关资源

COS Python SDK V5 相关资源地址: [github项目](https://github.com/tencentyun/cos-python-sdk-v5)

### 环境依赖

V5 版本 COS Python SDK 目前可以支持 Python2.6 与 Python2.7

### 安装SDK

安装 SDK 的方式有两种：pip安装和手动安装。

- 使用pip安装
  
        pip install -U cos-python-sdk-v5

- 手动安装

        从[github项目](https://github.com/tencentyun/cos-python-sdk-v5)下载源码,通过setup手动安装：

        python setup.py install
 
## 快速入门

```python
# 1.设置用户配置, 包括appid, secret_id，secret_key以及region
appid = '100000'            # 替换为用户的appid
secret_id = 'xxxxxxxx'      # 替换为用户的secret_id
secret_key = 'xxxxxxx'      # 替换为用户的secret_key
region = 'ap-beijing-1'     # 替换为用户的region
token = ''                  # 使用临时秘钥需要传入Token，默认为空，可不填
config = CosConfig(Appid=appid, Access_id=secret_id, Access_key=secret_key, Region=region, Token=token)
# 2.获取客户端对象
client = CosS3Client(config)
# 参照下文的描述。或者参照Demo程序，详见https://github.com/tencentyun/cos-python-sdk-v5/blob/master/qcloud_cos/demo.py
```

## 简单上传

### 功能说明

支持上传文件流或字节流到指定的Bucket中。推荐上传不大于20MB的小文件，单次上传大小限制为5GB,返回类型为dict，包含上传成功的文件的Etag等信息.

### 文件流 简单上传
```python
fp = open('test.txt', 'rb')
file_name = 'test.txt'
response = client.put_object(
    Bucket='test04',
    Body=fp,
    Key=file_name,
    StorageClass='STANDARD',
    CacheControl='no-cache',
    ContentDisposition='download.txt'
)
fp.close()
print response['ETag']
```
#### 参数说明

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* Body —— (file|string) ：必选参数，上传文件的内容，可以为文件流或字节流。
* Key —— (string) ：必选参数，上传文件的路径名。
* StorageClass —— (string) ： 可选参数，设置文件的存储类型，STANDARD,STANDARD_IA，NEARLINE，默认值：STANDARD。
* CacheControl —— (string) ： 可选参数，缓存策略，设置Cache-Control。
* ContentDisposition —— (string) ： 可选参数，文件名称，设置Content-Disposition。
* 更多可选参数详见 Python SDK 文档(链接).

### 字节流 简单上传
```python
response = client.put_object(
    Bucket='test04',
    Body='abcdefg',
    Key=file_name,
    CacheControl='no-cache',
    ContentDisposition='download.txt'
)
print response['ETag']
```

## 简单下载

### 功能说明

将指定Bucket中的文件下载到本地或文件流，返回类型为dict，包含文件的内容和元信息。
### 文件下载 获取文件到本地
```python
response = client.get_object(
    Bucket='test04',
    Key=file_name,
)
response['Body'].get_stream_to_file('output.txt')
```
#### 参数说明

* Bucket —— (String) ： 必选参数，Bucket名称，由数字和小写字母以及中划线"-"构成。
* Key —— (string) ：必选参数，下载文件的路径名。
* 更多可选参数详见 Python SDK 文档(链接).

### 文件下载 获取文件流
```python
response = client.get_object(
    Bucket='test04',
    Key=file_name,
)
fp = response['Body'].get_raw_stream()
print fp.read(2)
```

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
