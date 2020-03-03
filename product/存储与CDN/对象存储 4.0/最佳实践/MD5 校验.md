## 简介

数据在客户端和服务器间传输时可能会出现错误，COS 可以通过 MD5 校验的方式保证上传数据的完整性，只有当 COS 服务器接收到的数据 MD5 校验值与用户设置的 MD5 校验值一致时，数据才可上传成功。

COS 里每个对象对应一个 ETag，ETag 是对象被创建时对象内容的信息标识，但 ETag 不一定等同于对象内容的 MD5 校验值，因此不能通过 ETag 来校验下载对象与原对象是否一致，但用户可使用自定义对象元数据（x-cos-meta-\*）来实现下载对象与原对象的一致性校验。

## 数据校验方式

- 校验上传对象
如果用户需要校验上传到 COS 的对象与本地对象是否一致，可以在上传时将 HTTP 请求的 [Content-MD5](https://cloud.tencent.com/document/product/436/7728) 字段设置为经过 Base64 编码的对象内容 MD5 校验值，此时 COS 服务器将校验用户上传的对象，只有当 COS 服务器接收到的对象 MD5 校验值与用户设置的 Content-MD5 一致时，对象才可上传成功。
- 校验下载对象
如果用户需要校验下载对象与原对象是否一致，可在对象上传时使用校验算法计算对象的校验值，通过自定义元数据设置对象的校验值，在下载对象后，用户重新计算对象的校验值，并与该自定义元数据进行比较验证。在这种方式下，用户可自主选择校验算法，但对于同一个对象而言，其上传和下载时所使用的校验算法应保持一致。   



## API 接口示例

#### 简单上传请求

下面为用户上传对象的请求示例。上传对象时，设置 Content-MD5 为经过 Base64 编码的对象内容 MD5 校验值，此时只有当 COS 服务器接收到的对象 MD5 校验值与用户设置的 Content-MD5 一致时，对象才可上传成功，并且将自定义元数据 x-cos-meta-md5 设置为对象的校验值。
>?示例演示是通过 MD5 校验算法得到对象的校验值，用户可自主选择其他的校验算法。  

```url
PUT /exampleobject HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 21 Jun 2019 09:24:28 GMT
Content-Type: image/jpeg
Content-Length: 13
Content-MD5: ti4QvKtVqIJAvZxDbP/c+Q==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1561109068;1561116268&q-key-time=1561109068;1561116268&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=&q-signature=998bfc8836fc205d09e455c14e3d7e623bd2****
x-cos-meta-md5: b62e10bcab55a88240bd9c436cffdcf9
Connection: close

[Object Content]
```

#### 分块上传请求

下面为初始化分块上传的请求示例。在上传对象分块时，用户可通过初始化分块上传来设置对象的自定义元数据，这里将自定义元数据 x-cos-meta-md5 设置为对象的校验值。   

```url
POST /exampleobject?uploads HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 21 Jun 2019 09:45:12 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1561109068;1561116268&q-key-time=1561109068;1561116268&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=&q-signature=998bfc8836fc205d09e455c14e3d7e623bd2****
x-cos-meta-md5: b62e10bcab55a88240bd9c436cffdcf9
```

#### 对象下载响应

下面为用户发出下载对象请求后得到的响应示例。从响应中用户可以得到对象的自定义元数据 x-cos-meta-md5，用户可通过重新计算对象的校验值，与该自定义元数据进行比较，从而验证下载对象和原对象是否一致。   

```url
HTTP/1.1 200 OK
Content-Type: application/octet-stream
Content-Length: 13
Connection: close
Accept-Ranges: bytes
Cache-Control: max-age=86400
Content-Disposition: attachment; filename=example.jpg
Date: Thu, 04 Jul 2019 11:33:00 GMT
ETag: "b62e10bcab55a88240bd9c436cffdcf9"
Last-Modified: Thu, 04 Jul 2019 11:32:55 GMT
Server: tencent-cos
x-cos-request-id: NWQxZGUzZWNfNjI4NWQ2NF9lMWYyXzk1NjFj****
x-cos-meta-md5: b62e10bcab55a88240bd9c436cffdcf9

[Object Content]
```

## SDK 示例

下面以 Python SDK 为例演示如何校验对象，完整的示例代码如下。

>?代码基于 Python 2.7，其中 Python SDK 详细使用方式，请参见 Python SDK  [对象操作](https://cloud.tencent.com/document/product/436/35151) 文档。

#### 1. 初始化配置

设置用户属性，包括 SecretId、SecretKey 和 Region，并创建客户端对象。

```python
# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos import CosServiceError
from qcloud_cos import CosClientError
import sys
import logging
import hashlib

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 设置用户属性, 包括 SecretId, SecretKey, Region
# APPID 已在配置中移除，请在参数 Bucket 中带上 APPID。Bucket 由 BucketName-APPID 组成。
secret_id = COS_SECRETID           # 替换为您的 SecretId 信息
secret_key = COS_SECRETKEY         # 替换为您的 SecretKey 信息
region = 'ap-beijing'      # 替换为您的 Region, 这里以北京为例
token = None               # 使用临时密钥需要传入 Token，默认为空，可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token)  # 获取配置对象
client = CosS3Client(config)
```

#### 2. 校验简单上传对象

#### （1）计算对象的校验值

通过 MD5 校验算法得到对象的校验值，用户可自主选择其他的校验算法。

```python
object_body = 'hello cos'
#得到对象的 md5 校验值
md5 = hashlib.md5()
md5.update(object_body)
md5_str = md5.hexdigest()
```

#### （2）简单上传对象

代码中 EnableMD5=True 表示开启对象上传的 MD5 校验，Python SDK 会计算 Content-MD5，打开后将增加上传耗时，当 COS 服务器接收到的对象 MD5 校验值与 Content-MD5 一致时，对象才可上传成功。
x-cos-meta-md5 为用户自定义的参数（自定义参数名称格式为 x-cos-meta-\*），这里参数表示了对象的 MD5 校验值。

```python
#简单上传对象，并打开 MD5 校验
response = client.put_object(
    Bucket='examplebucket-1250000000',      #替换为您的 Bucket 名称，examplebucket 是一个举例的存储桶，1250000000 为举例的 APPID。
    Body='hello cos',                 #上传的对象内容
    Key='example-object-1',           #替换为您上传的对象 Key 值 
    EnableMD5=True,                   #开启上传的 MD5 校验
    Metadata={                        #设置自定义参数，将对象的 MD5 校验值作为参数值存入 COS 服务器
        'x-cos-meta-md5' : md5_str
    }
)
print 'ETag: ' + response['ETag']     # Object 的 Etag 值
```

#### （3）下载对象

下载对象并得到用户自定义参数。

```python
#下载对象
response = client.get_object(
    Bucket='examplebucket-1250000000',      #替换为您的 Bucket 名称，examplebucket 是一个举例的存储桶，1250000000 为举例的 APPID。
    Key='example-object-1'                  #下载对象的 Key 值
)
fp = response['Body'].get_raw_stream()
download_object = fp.read()                 #得到对象内容
print "get object body: " + download_object
print 'ETag: ' + response['ETag']               
print 'x-cos-meta-md5: ' + response['x-cos-meta-md5']   #得到用户自定义参数 x-cos-meta-md5
```

#### （4） 校验对象

成功下载对象后，用户重新计算对象的校验值（校验算法应与上传对象时保持一致），并与用户自定义参数 x-cos-meta-md5 进行比较，验证下载的对象与上传对象内容是否一致。

```python
#计算下载对象的 MD5 校验值
md5 = hashlib.md5()                 
md5.update(download_object)
md5_str = md5.hexdigest()
print 'download object md5: ' + md5_str

#通过下载对象的 MD5 校验值与上传对象的 MD5 校验值比较，从而验证对象的一致性
if md5_str == response['x-cos-meta-md5']:
    print 'MD5 check OK'
else:
    print 'MD5 check FAIL'
```

#### 3. 校验分块上传对象

#### （1）计算对象的校验值

模拟对象分块，并计算整个对象的校验值，下面通过 MD5 校验算法得到对象的校验值，用户可自主选择其他的校验算法。

```python
OBJECT_PART_SIZE = 1024 * 1024      #模拟每个分块的大小
OBJECT_TOTAL_SIZE = OBJECT_PART_SIZE * 1 + 123      #对象的总大小
object_body = '1' * OBJECT_TOTAL_SIZE       #对象内容

#计算整个对象内容的 MD5 校验值
md5 = hashlib.md5()
md5.update(object_body)
md5_str = md5.hexdigest()
```

#### （2）初始化分块上传

在初始化分块上传时，设置自定义参数 x-cos-meta-md5，将整个对象的 MD5 校验值作为参数内容。

```python
#初始化分块上传
response = client.create_multipart_upload(
    Bucket='examplebucket-1250000000',  #替换为您的 Bucket 名称，examplebucket 是一个举例的存储桶，1250000000 为举例的 APPID。
    Key='exampleobject-2',              #替换为您上传的对象 Key 值 
    StorageClass='STANDARD',            #对象的存储级别
    Metadata={
        'x-cos-meta-md5' : md5_str      #设置自定义参数，设置为 MD5 校验值
    }
)
#获取分块上传的 UploadId
upload_id = response['UploadId']
```

#### （3）分块上传对象

分块上传对象，通过将对象切分成多个块进行上传，最多支持10000分块，每个分块大小为1MB - 5GB，最后一个分块可以小于1MB。上传分块时，需要设置每个分块的 PartNumber（编号）。EnableMD5=True 为打开分块校验，打开后将增加上传耗时，此时 Python SDK 会计算每个分块的  Content-MD5，只有当 COS 服务器接收到的对象 MD5 校验值与 Content-MD5 一致时，分块才可上传成功。上传成功后，返回每个分块的 ETag。     

```python
#分块上传对象，每个分块大小为 OBJECT_PART_SIZE，最后一个分块可能不足 OBJECT_PART_SIZE
part_list = list()
position = 0
left_size = OBJECT_TOTAL_SIZE
part_number = 0
while left_size > 0:
    part_number += 1
    if left_size >= OBJECT_PART_SIZE:
        body = object_body[position:position+OBJECT_PART_SIZE]
    else:
        body = object_body[position:]
    position += OBJECT_PART_SIZE
    left_size -= OBJECT_PART_SIZE

    #上传分块
    response = client.upload_part(
        Bucket='examplebucket-1250000000',  #替换为您的 Bucket 名称，examplebucket 是一个举例的存储桶，1250000000 为举例的 APPID。
        Key='exampleobject-2',              #对象的 Key 值 
        Body=body,
        PartNumber=part_number,
        UploadId=upload_id,
        EnableMD5=True       #打开分块校验，COS 服务器会对每个分块进行 MD5 校验。
    )
    etag = response['ETag']     #ETag 表示每个分块的 MD5 值
    part_list.append({'ETag' : etag, 'PartNumber' : part_number})
    print etag + ', ' + str(part_number)
```

#### （4）完成分块上传

在所有分块上传完成后，需要进行完成分块上传操作。每个分块的 ETag 和 PartNumber 需要一一对应，COS 服务器用于校验块的准确性。完成分块上传后，返回的 ETag 表示合并后对象的唯一标签值，而不是整个对象内容的 MD5 校验值，因此下载对象时，可通过自定义参数来进行校验。

```python
#完成分块上传
response = client.complete_multipart_upload(
    Bucket='examplebucket-1250000000',  #替换为您的 Bucket 名称，examplebucket 是一个举例的存储桶，1250000000 为举例的APPID。
    Key='exampleobject-2',              #对象的 Key 值 
    UploadId=upload_id,
    MultipartUpload={       #要求每个分块的 ETag 和 PartNumber 一一对应
        'Part' : part_list    
    },
)

#ETag 表示合并后对象的唯一标签值，该值不是对象内容的 MD5 校验值，仅用于检查对象唯一性。
print "ETag: " + response['ETag']   
print "Location: " + response['Location']   #URL地址
print "Key: " + response['Key'] 
```

#### （5）下载对象

下载对象并得到用户自定义参数。

```python
# 下载对象
response = client.get_object(
    Bucket='examplebucket-1250000000',  #替换为您的 Bucket 名称，examplebucket 是一个举例的存储桶，1250000000 为举例的 APPID。
    Key='exampleobject-2'               #对象的 Key 值 
)
print 'ETag: ' + response['ETag']                        #对象的 ETag 不是对象内容的 MD5 校验值
print 'x-cos-meta-md5: ' + response['x-cos-meta-md5']    #得到用户自定义参数 x-cos-meta-md5
```

#### （6）校验对象

成功下载对象后，用户重新计算对象的 MD5 校验值，并与用户自定义参数 x-cos-meta-md5 进行比较，验证下载的对象与上传对象内容是否一致。

```python
#计算下载对象的 MD5 校验值
fp = response['Body'].get_raw_stream()
DEFAULT_CHUNK_SIZE = 1024*1024
md5 = hashlib.md5()
chunk = fp.read(DEFAULT_CHUNK_SIZE)     
while chunk:
    md5.update(chunk)
    chunk = fp.read(DEFAULT_CHUNK_SIZE)
md5_str = md5.hexdigest()
print 'download object md5: ' + md5_str

#通过下载对象的 MD5 校验值与上传对象的 MD5 校验值比较，从而验证对象的一致性
if md5_str == response['x-cos-meta-md5']:
    print 'MD5 check OK'
else:
    print 'MD5 check FAIL'
```
