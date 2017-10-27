## 开发准备

### 相关资源
对象存储服务的 XML Python SDK  资源下载地址： [XML Python SDK ](https://github.com/tencentyun/cos-python-sdk-v5)
演示示例 Demo 下载地址：[XML Python Demo](https://github.com/tencentyun/cos-python-sdk-v5/blob/master/qcloud_cos/demo.py)

### 环境依赖

对象存储服务的 XML Python SDK  目前可以支持 Python2.6 与 Python2.7。
> 关于文章中出现的 SecretId、SecretKey、Bucket 等名称的含义和获取方式请参考：[COS 术语信息](https://cloud.tencent.com/document/product/436/7751)

### 安装SDK

安装 SDK 的方式有两种：pip 安装和手动安装。

- **使用 pip 安装**
```
 pip install -U cos-python-sdk-v5
```
- **手动安装**
 从 [XML Python SDK](https://github.com/tencentyun/cos-python-sdk-v5) 下载源码，通过 setup 手动安装：
 ```
 python setup.py install
```
 
## 快速入门

```python
# 1. 设置用户配置, 包括 APPID, secretId，secretKey 以及 Region
appid = '100000'            # 替换为用户的 APPID
secret_id = 'xxxxxxxx'      # 替换为用户的 secretId
secret_key = 'xxxxxxx'      # 替换为用户的 secretKey
region = 'ap-beijing-1'     # 替换为用户的 Region
token = ''                  # 使用临时秘钥需要传入 Token，默认为空，可不填
config = CosConfig(Appid=appid, Access_id=secret_id, Access_key=secret_key, Region=region, Token=token)
# 2. 获取客户端对象
client = CosS3Client(config)
# 参照下文的描述。或者参照 Demo程序，详见 https://github.com/tencentyun/cos-python-sdk-v5/blob/master/qcloud_cos/demo.py
```

## 简单上传

### 功能说明

支持上传文件流或字节流到指定的 Bucket中。推荐上传不大于 20MB 的小文件，单次上传大小限制为 5GB，返回类型为 dict，包含上传成功的文件的 Etag 等信息。

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

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
| Bucket| Bucket名称，由数字和小写字母以及中划线"-"构成|String |是 | 
|  Body file| 上传文件的内容，可以为文件流或字节流|String|是 | 
|  Key |  上传文件的路径名。|String|是 | 
|  StorageClass | 设置文件的存储类型，STANDARD,STANDARD_IA，NEARLINE，默认值：STANDARD| String |否| 
|  CacheControl | 缓存策略，设置 Cache-Control|String|否| 
| ContentDisposition |文件名称，设置 Content-Disposition|String | 否| 
 更多可选参数详见 [Python SDK 文档](链接)。

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

将指定存储桶中的文件下载到本地或文件流，返回类型为 dict，包含文件的内容和元信息。
### 文件下载 获取文件到本地
```python
response = client.get_object(
    Bucket='test04',
    Key=file_name,
)
response['Body'].get_stream_to_file('output.txt')
```
#### 参数说明

| 参数名称   | 参数描述   |类型 | 必填 | 
| -------------- | -------------- |---------- | ----------- |
|  Bucket |  存储桶名称，由数字和小写字母以及中划线"-"构成|String|是 |
| Key | 下载文件的路径名|string| 是 |
 更多可选参数详见 [Python SDK 文档](链接)。

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
