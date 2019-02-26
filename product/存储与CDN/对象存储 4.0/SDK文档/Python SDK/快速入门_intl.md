## Preparations for Development

### Related resources
Download XML Python SDK resources of COS service from: [XML Python SDK ](https://github.com/tencentyun/cos-python-sdk-v5).
Download Demo from: [XML Python Demo](https://github.com/tencentyun/cos-python-sdk-v5/blob/master/qcloud_cos/demo.py).

### Environment dependencies

The XML Python SDK for COS service supports Python 2.6, Python 2.7 and Python 3.x.
> For more information on the definitions of SecretId, SecretKey, Bucket and other terms and how to obtain them, please see [COS Glossary](https://cloud.tencent.com/document/product/436/7751).

### Install SDK

There are three ways to install the SDK: installation using pip, manual installation, and offline installation.

#### Installation using pip (recommended)
```
 pip install -U cos-python-sdk-v5
```

#### Manual installation
Download the source code from [XML Python SDK](https://github.com/tencentyun/cos-python-sdk-v5) and install it manually via setup:
```
 python setup.py install
```
#### Offline installation
```
# Run the following command on a server with public network
mkdir cos-python-sdk-packages
pip download cos-python-sdk-v5 -d cos-python-sdk-packages
tar -czvf cos-python-sdk-packages.tar.gz cos-python-sdk-packages

# Copy the installer package to a server without public network and run the following command
tar -xzvf cos-python-sdk-packages.tar.gz
pip install cos-python-sdk-v5 --no-index -f cos-python-sdk-packages
```
 
## Getting Started
```python
# appid has been removed from the configuration. Please include the appid in the parameter Bucket. Bucket is in the format of bucketname-appid.
# 1. Set user configuration, including secretId, secretKey and Region
# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import sys
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

secret_id = 'xxxxxxxx'      # Replaced with user's secretId
secret_key = 'xxxxxxx'      # Replaced with user's secretKey
region = 'ap-beijing-1'     # Replaced with user's Region
token = None                # Token is required to use a temporary key. It is optional. Default is empty.
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
# 2. Obtain client object
client = CosS3Client(config)
# Refer to the description below or the Demo. For more information, please see https://github.com/tencentyun/cos-python-sdk-v5/blob/master/qcloud_cos/demo.py.
```

## Uploading File
### Simple upload of file stream
```python
file_name = 'test.txt'
with open('test.txt', 'rb') as fp:
    response = client.put_object(
        Bucket='test04-123456789',
        Body=fp,
        Key=file_name,
        StorageClass='STANDARD',
        ContentType='text/html; charset=utf-8'
    )
print(response['ETag'])
```
#### Parameters
| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
| Bucket| Bucket name, in the format of bucketname-appid |String |Yes | 
|  Body | The content of the uploaded file, which can be a file stream or a byte stream |file/bytes|Yes | 
|  Key | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name `bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg`, the object key is doc1/pic1.jpg. |String|Yes | 
|  StorageClass | Storage type of file: STANDARD and STANDARD_IA. Default: STANDARD | String |No | 
| ContentType | Content Type. Set Content-Type |String | No | 

For more optional parameters, please see [Python SDK Documentation](https://cloud.tencent.com/document/product/436/12270).

### Simple upload of byte stream
```python
response = client.put_object(
    Bucket='test04-123456789',
    Body=b'abcdefg',
    Key=file_name,
)
print(response['ETag'])
```

### Simple upload from local path
```python
response = client.put_object_from_local_file(
    Bucket='test04-123456789',
    LocalFilePath='local.txt',
    Key=file_name,
)
print(response['ETag'])
```

### Simple upload by setting HTTP header
```python
response = client.put_object(
    Bucket='test04-123456789',
    Body=b'test',
    Key=file_name,
    ContentType='text/html; charset=utf-8'
)
print(response['ETag'])
```

### Simple upload by setting custom header
```python
response = client.put_object(
    Bucket='test04-123456789',
    Body=b'test',
    Key=file_name,
    Metadata={
        'x-cos-meta-key1': 'value1',
        'x-cos-meta-key2': 'value2'
    }
)
print(response['ETag'])
```

### Advanced API for upload (recommended)
Simple upload or multipart upload is selected automatically based on the file size. Multipart upload supports resuming download from breakpoint.
```python
response = client.upload_file(
    Bucket='test04-123456789',
    LocalFilePath='local.txt',
    Key=file_name,
    PartSize=10,
    MAXThread=10
)
print(response['ETag'])
```

## Downloading File
### Download the file locally
```python
response = client.get_object(
    Bucket='test04-123456789',
    Key=file_name,
)
response['Body'].get_stream_to_file('output.txt')
```
#### Parameters
| Parameter Name | Description | Type | Required | 
| -------------- | -------------- |---------- | ----------- |
|  Bucket | Bucket name, in the format of bucketname-appid |String|Yes |
| Key | Object key is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg. |string|Yes |

For more optional parameters, please see [Python SDK Documentation](https://cloud.tencent.com/document/product/436/12270).

### Get file stream
```python
response = client.get_object(
    Bucket='test04-123456789',
    Key=file_name,
)
fp = response['Body'].get_raw_stream()
print(fp.read(2))
```

### Set Response HTTP header
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

### Specify the range of file download
```python
response = client.get_object(
    Bucket='test04-123456789',
    Key=file_name,
    Range='bytes=0-10'
)
fp = response['Body'].get_raw_stream()
print(fp.read())
```
## Exception Types
Exceptions include CosClientError (SDK client error) and CosServiceError (COS server error).

### CosClientError
CosClientError generally refers to a client error caused by the reasons such as timeout. When capturing such an error, you can choose to retry or perform other operations.

### CosServiceError
CosServiceError provides the message returned by the server.
```python
#except CosServiceError as e
e.get_origin_msg()  # Get original error message in XML format
e.get_digest_msg() # Get the processed error message in dict format
e.get_status_code() # Get http error code (e.g. 4XX, 5XX)
e.get_error_code() # Get COS-defined error code
e.get_error_msg() # Get a detailed description of the COS error code
e.get_trace_id() # Get the trace_id of the request
e.get_request_id() # Get the request_id of the request
e.get_resource_location() # Get the URL address
```

