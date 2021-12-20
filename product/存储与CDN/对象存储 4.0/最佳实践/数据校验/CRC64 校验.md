## 简介

数据在客户端和服务器间传输时可能会出现错误，COS 除了可以通过 [MD5 和自定义属性](https://cloud.tencent.com/document/product/436/36427) 验证数据完整性外，还可以通过 CRC64 检验码来进行数据校验。

COS 会对新上传的对象进行 CRC64 计算，并将结果作为对象的属性进行存储，随后在返回的响应头部中携带 x-cos-hash-crc64ecma，该头部表示上传对象的 CRC64 值，根据 [ECMA-182标准]( https://www.ecma-international.org/publications/standards/Ecma-182.htm) 计算得到。对于 CRC64 特性上线前就已经存在于 COS 的对象，COS 不会对其计算 CRC64 值，所以获取此类对象时不会返回其 CRC64 值。

## 操作说明

目前支持 CRC64 的 API 如下：

- 简单上传接口
	- [PUT Object](https://cloud.tencent.com/document/product/436/7749) 和 [POST Object](https://cloud.tencent.com/document/product/436/14690)：用户可在返回的响应头中获得文件 CRC64 校验值。
- 分块上传接口
	- [Upload Part](https://cloud.tencent.com/document/product/436/7750)：用户可以根据 COS 返回的 CRC64 值与本地计算的数值进行比较验证。
	- [Complete Multipart Upload](https://cloud.tencent.com/document/product/436/7742)：如果每个分块都有 CRC64 属性，则会返回整个对象的 CRC64 值，如果某些分块不具备 CRC64 值，则不返回。
- 执行 [Upload Part - Copy](https://cloud.tencent.com/document/product/436/8287) 时，会返回对应的 CRC64 值。
- 执行 [PUT Object - Copy](https://cloud.tencent.com/document/product/436/10881) 时，如果源对象存在 CRC64 值，则返回 CRC64，否则不返回。
- 执行 [HEAD Object](https://cloud.tencent.com/document/product/436/7745) 和 [GET Object](https://cloud.tencent.com/document/product/436/7753) 时，如果对象存在 CRC64，则返回。用户可以根据 COS 返回的 CRC64 值和本地计算的 CRC64 进行比较验证。

## API 接口示例

#### 分块上传响应

下面为用户发出 Upload Part 请求后得到的响应示例。x-cos-hash-crc64ecma 头部表示分块的 CRC64 值，用户可以通过该值与本地计算的 CRC64 值进行比较，从而校验分块完整性。

```shell
HTTP/1.1 200 OK
content-length: 0
connection: close
date: Thu, 05 Dec 2019 01:58:03 GMT
etag: "358e8c8b1bfa35ee3bd44cb3d2cc416b"
server: tencent-cos
x-cos-hash-crc64ecma: 15060521397700495958
x-cos-request-id: NWRlODY0MmJfMjBiNDU4NjRfNjkyZl80ZjZi****
```

#### 完成分块上传响应

下面为用户发出 Complete Multipart Upload 请求后得到的响应示例。x-cos-hash-crc64ecma 头部表示整个对象的 CRC64 值，用户可以通过该值与本地计算的 CRC64 值进行比较，从而校验对象完整性。

```shell
HTTP/1.1 200 OK
content-type: application/xml
transfer-encoding: chunked
connection: close
date: Thu, 05 Dec 2019 02:01:17 GMT
server: tencent-cos
x-cos-hash-crc64ecma: 15060521397700495958
x-cos-request-id: NWRlODY0ZWRfMjNiMjU4NjRfOGQ4Ml81MDEw****

[Object Content]
```

## SDK 示例

### Python SDK

下面以 Python SDK 为例演示如何校验对象，完整的示例代码如下。

> ?代码基于 Python 2.7，其中 Python SDK 详细使用方式，请参见 Python SDK 的 [对象操作](https://cloud.tencent.com/document/product/436/35151) 文档。

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
import crcmod

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

# 设置用户属性, 包括 SecretId, SecretKey, Region
# APPID 已在配置中移除，请在参数 Bucket 中带上 APPID。Bucket 由 BucketName-APPID 组成
secret_id = COS_SECRETID           # 替换为您的 SecretId 信息
secret_key = COS_SECRETKEY         # 替换为您的 SecretKey 信息
region = 'ap-beijing'      # 替换为您的 Region, 这里以北京为例
token = None               # 使用临时密钥需要传入 Token，默认为空，可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token)  # 获取配置对象
client = CosS3Client(config)
```

#### 2. 计算对象的校验值

模拟对象分块，并计算整个对象的 CRC64 校验值。

```python
OBJECT_PART_SIZE = 1024 * 1024      #模拟每个分块的大小
OBJECT_TOTAL_SIZE = OBJECT_PART_SIZE * 1 + 123      #对象的总大小
object_body = '1' * OBJECT_TOTAL_SIZE       #对象内容

#计算整个对象 crc64 校验值
c64 = crcmod.mkCrcFun(0x142F0E1EBA9EA3693L, initCrc=0L, xorOut=0xffffffffffffffffL, rev=True)
local_crc64 =str(c64(object_body))
```

#### 3. 初始化分块上传

```python
#初始化分块上传
response = client.create_multipart_upload(
    Bucket='examplebucket-1250000000',  #替换为您的 Bucket 名称，examplebucket 是一个举例的存储桶，1250000000 为举例的 APPID
    Key='exampleobject',                #替换为您上传的对象 Key 值
    StorageClass='STANDARD',            #对象的存储类型
)
#获取分块上传的 UploadId
upload_id = response['UploadId']
```

#### 4. 分块上传对象

分块上传对象，通过将对象切分成多个块进行上传，最多支持10000分块，每个分块大小为1MB - 5GB，最后一个分块可以小于1MB。上传分块时，需要设置每个分块的 PartNumber（编号），并计算每个分块的 CRC64 值，在分块上传成功后，可以通过返回的 CRC64 值与本地计算的数值进行校验。

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
    local_part_crc64 = str(c64(body))	#本地计算 CRC64

    response = client.upload_part(
        Bucket='examplebucket-1250000000',
        Key='exampleobject',
        Body=body,
        PartNumber=part_number,
        UploadId=upload_id,
    )   
    part_crc_64 = response['x-cos-hash-crc64ecma']	# 服务器返回的 CRC64
    if local_part_crc64 != part_crc_64:		# 数据检验
    	print 'crc64 check FAIL'
    	exit(-1)
    etag = response['ETag']
    part_list.append({'ETag' : etag, 'PartNumber' : part_number})
```

#### 5. 完成分块上传

在所有分块上传完成后，需要进行完成分块上传操作。可以通过 COS 返回的 CRC64 和本地对象的 CRC64 进行比较验证。

```python
#完成分块上传
response = client.complete_multipart_upload(
    Bucket='examplebucket-1250000000',  #替换为您的 Bucket 名称，examplebucket 是一个举例的存储桶，1250000000 为举例的 APPID
    Key='exampleobject',             #对象的 Key 值
    UploadId=upload_id,
    MultipartUpload={       			#要求每个分块的 ETag 和 PartNumber 一一对应
        'Part' : part_list    
    },
)
crc64ecma = response['x-cos-hash-crc64ecma']
if crc64ecma != local_crc64:			# 数据检验
    print 'check crc64 Failed'
    exit(-1)
```

### Java SDK

上传对象，推荐使用 Java SDK 的高级接口，参见 Java SDK [对象操作](https://cloud.tencent.com/document/product/436/35215#.E4.B8.8A.E4.BC.A0.E5.AF.B9.E8.B1.A1.EF.BC.88.E8.8E.B7.E5.8F.96.E8.BF.9B.E5.BA.A6.EF.BC.89)。

#### 如何在本地计算文件的 crc64

```java
String calculateCrc64(File localFile) throws IOException {
    CRC64 crc64 = new CRC64();

    try (FileInputStream stream = new FileInputStream(localFile)) {
        byte[] b = new byte[1024 * 1024];
        while (true) {
            final int read = stream.read(b);
            if (read <= 0) {
                break;
            }
            crc64.update(b, read);
        }
    }

    return Long.toUnsignedString(crc64.getValue());
}
```

#### 如何获得 COS 上文件的 crc64 值, 并与本地文件做校验

```java
// COSClient 的创建参考：[快速入门](https://cloud.tencent.com/document/product/436/10199);
ObjectMetadata cosMeta = COSClient().getObjectMetadata(bucketName, cosFilePath); 
String cosCrc64 = cosMeta.getCrc64Ecma();
String localCrc64 = calculateCrc64(localFile);

if (cosCrc64.equals(localCrc64)) {
    System.out.println("ok");
} else {
    System.out.println("fail");
}
```