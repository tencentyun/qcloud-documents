## 操作场景
本文档将向您介绍如何在 Notebook 中访问 COS，进行文件的上传和下载操作。

## 操作详情

```
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from ti.utils import get_temporary_secret_and_token

#### 获取用户临时密钥
secret_id, secret_key, token = get_temporary_secret_and_token()

scheme = 'https'
region='ap-guangzhou'

#### 指定notebook里需要上传的文件本地路径
local_path = "/notebooks/user_path/"
#### 用户的存储桶
bucket="user_bucket"

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
client = CosS3Client(config)

#### 上传本地文件到Cos
client.upload_file(Bucket=bucket, LocalFilePath=local_path+"/heart.csv", Key="user_key")

#### 列出Cos存储桶下所有文件
response = client.list_objects(bucket)

####  获取文件到本地
response = client.get_object(
    Bucket=bucket,
    Key='user_key',
)
response['Body'].get_stream_to_file('heart.csv')
```
