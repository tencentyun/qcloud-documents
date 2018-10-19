## 适用场景

利用生命周期设置，可以让符合规则的对象在指定的条件下自动执行一些操作。例如：

- 转换存储类型：将创建的对象在指定时间后转换为低频存储类型 STANDARD_IA 或者归档存储类型 ARCHIVE。
- 过期删除：设置对象的过期时间，使对象到期后被自动删除。

请参考生命周期功能的 [基本说明文档](/document/product/436/17028)，设置时需指定 [配置元素](/document/product/436/17029)。

## 使用方法
### 使用对象存储控制台
有关使用对象存储控制台设置生命周期，请查阅 [生命周期管理](https://cloud.tencent.com/document/product/436/14605) 控制台指南文档。

### 使用 REST API

您可以直接使用 REST API 配置和管理 Bucket 中 Object 的生命周期，可参考以下 API 文档部分：

- [PUT Bucket lifecycle](https://cloud.tencent.com/document/product/436/8280)
- [GET Buket lifecycle](https://cloud.tencent.com/document/product/436/8278)
- [DELETE Bucket lifecycle](https://cloud.tencent.com/document/product/436/8284)

### 使用 C++ SDK

对象存储 COS 的 C++ SDK 中提供了此方法，可参考 C++ SDK 接口文档 [ PUT Bucket lifecycle 部分](https://cloud.tencent.com/document/product/436/12302#put-bucket-lifecycle)。

步骤说明：

1. 初始化客户端 cosClient。
2. 执行 putBucketLifecycle 和 GetBucketLifecycle 分别设置存储桶生命周期和检索生命周期。

#### 设置生命周期

代码示例：

```
cloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-12345";

// PutBucketLifecycleReq 的构造函数需要传入 bucket_name
qcloud_cos::PutBucketLifecycleReq req(bucket_name);
qcloud_cos::PutBucketLifecycleResp resp;

// 设置规则
{
    qcloud_cos::LifecycleRule rule;
    rule.SetIsEnable(true);
    rule.SetId("lifecycle_rule00");
	
    // 设置 Filter， 对带标签键 datalevel 和值 backup 的标签的对象生效
    qcloud_cos::LifecycleFilter filter;
    Lifecycle tag;
    tag.key = "datalevel";
    tag.value = "backup";
    filter.AddTag(tag);
    rule.SetFilter(filter);

    // 对象创建 30 天后将其转换为 STANDARD_IA
    qcloud_cos::LifecycleTransition transition1;
    transition1.SetDays(30);
    transition1.SetStorageClass("STANDARD_IA");
    rule.AddTransition(transition1);
	
    // 对象创建 365 天后将其转换为 ARCHIVE 存储类别
    qcloud_cos::LifecycleTransition transition2;
    transition2.SetDays(365);
    transition2.SetStorageClass("ARCHIVE");
    rule.AddTransition(transition2);
	
    req.AddRule(rule);
}

qcloud_cos::CosResult result = cos.PutBucketLifecycle(req, &resp);
// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 设置生命周期失败，可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
}
```

#### 检索生命周期
代码示例：

```
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "cpp_sdk_v5-12345";

// GetBucketLifecycleReq 的构造函数需要传入 bucket_name
qcloud_cos::GetBucketLifecycleReq req(bucket_name);
qcloud_cos::GetBucketLifecycleResp resp;
qcloud_cos::CosResult result = cos.GetBucketLifecycle(req, &resp);

// 调用成功，调用 resp 的成员函数获取返回内容
if (result.IsSucc()) {
    // ...
} else {
    // 获取生命周期配置失败，可以调用 CosResult 的成员函数输出错误信息，比如 requestID 等
}
```

### 使用 Python SDK
对象存储 COS 的 Python SDK 中提供了此方法，可参考 Python SDK 接口文档 [设置 Bucket 生命周期配置部分](https://cloud.tencent.com/document/product/436/12270#.E8.AE.BE.E7.BD.AE-bucket-.E7.94.9F.E5.91.BD.E5.91.A8.E6.9C.9F.E9.85.8D.E7.BD.AE)。
#### 设置生命周期
步骤说明：

1. 通过 CosConfig 类来配置, 初始化客户端 CosS3Client。
2. 执行 put_bucket_lifecycle() 方法来设置存储桶下的生命周期配置。

设置生命周期的代码示例如下：

```python
# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = 'xxxxxxxx'      # 替换为用户的 secretId
secret_key = 'xxxxxxx'      # 替换为用户的 secretKey
region = 'ap-beijing-1'     # 替换为用户的 Region
token = ''                  # 使用临时密钥需要传入 Token，默认为空，可不填

config = CosConfig(Access_id=secret_id, Access_key=secret_key, Region=region, Token=token)
client = CosS3Client(config)

bucket = 'testbucket-123456789'
lifecycle_config = {
    'Rule': [
        {
            'Status': 'Enabled',
            'Filter': {
                # 作用于带标签键 datalevel 和值 backup 的标签的对象
                'Tag': [
                    {
                        'Key': 'datalevel',
                        'Value': 'backup'
                    }
                ]
            },
            'Transition': [
                {
                    # 30天后转换为Standard_IA
                    'Days': 30,
                    'StorageClass': 'Standard_IA'
                },
                {
                    # 365天后转换为Archive
                    'Days': 365,
                    'StorageClass': 'Archive'
                }
            ],
            'Expiration': {
                # 3650天后过期删除
                'Days': 3650
            }
        }
    ]
}

response = client.put_bucket_lifecycle(
    Bucket=bucket,
    LifecycleConfiguration=lifecycle_config
)
```

#### 获取生命周期
步骤说明:

1. 通过 CosConfig 类来配置, 初始化客户端 CosS3Client.
2. 执行 get_bucket_lifecycle() 方法来获取存储桶下的生命周期配置

获取生命周期配置代码如下：

```python
# -*- coding=utf-8
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

secret_id = 'xxxxxxxx'      # 替换为用户的 secretId
secret_key = 'xxxxxxx'      # 替换为用户的 secretKey
region = 'ap-beijing-1'     # 替换为用户的 Region
token = ''                  # 使用临时密钥需要传入 Token，默认为空，可不填

config = CosConfig(Access_id=secret_id, Access_key=secret_key, Region=region, Token=token)
client = CosS3Client(config)

bucket = 'testbucket-123456789'
response = client.get_bucket_lifecycle(
    Bucket=bucket    
)
```

### 使用 PHP SDK
对象存储 COS 的 PHP SDK 中提供了此方法，可参考 PHP SDK 接口文档 [PUT Bucket lifecycle](https://cloud.tencent.com/document/product/436/12267#putbucketlifecycle)。

#### 设置生命周期
步骤说明：

1. 初始化客户端 cosClient。
2. 执行 putBucketLifecycle 设置存储桶生命周期。

以下代码演示了设置存储桶生命周期的步骤：

```php
## putBucketLifecycle(设置bucket生命周期)
$cosClient = new Qcloud\Cos\Client(array('region' => getenv('COS_REGION'),
    'credentials'=> array(
        'secretId'    => getenv('COS_KEY'),
        'secretKey' => getenv('COS_SECRET'))));

//bucket的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
$bucket = 'lewzylu02-1252448703';

try {
    $result = $cosClient->putBucketLifecycle(array(
        'Bucket' => $bucket,
        'Rules' => array(
            array(
                'Status' => 'Enabled',
                'Filter' => array(
                    'Tag' => array(
                        'Key' => 'datalevel',
                        'Value' => 'backup'
                    )
                ),
                'Transitions' => array(
                   array(
                    # 30天后转换为Standard_IA
                    'Days' => 30,
                    'StorageClass' => 'Standard_IA'),
                array(
                    # 365天后转换为Archive
                    'Days' => 365,
                    'StorageClass' => 'Archive')
                ),
                'Expiration' => array(
                # 3650天后过期删除
                'Days' => 3650,
                )
            )
        )
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```

#### 获取生命周期
步骤说明：

1. 初始化客户端 cosClient。
2. 执行 getBucketLifecycle 获取存储桶生命周期信息。

以下代码演示了获取存储桶生命周期的步骤：

```php
## getBucketLifecycle(获取 bucket 生命周期)
$cosClient = new Qcloud\Cos\Client(array('region' => getenv('COS_REGION'),
    'credentials'=> array(
        'secretId'    => getenv('COS_KEY'),
        'secretKey' => getenv('COS_SECRET'))));

//bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
$bucket = 'lewzylu02-1252448703';

try {
    $result = $cosClient->getBucketLifecycle(array(
        'Bucket' =>$bucket,
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```

#### 删除生命周期
步骤说明：

1. 初始化客户端 cosClient。
2. 执行 deleteBucketLifecycle 删除存储桶生命周期。

以下代码演示了删除存储桶生命周期的步骤：

```php
## deleteBucketLifecycle(删除 bucket 生命周期)
$cosClient = new Qcloud\Cos\Client(array('region' => getenv('COS_REGION'),
    'credentials'=> array(
        'secretId'    => getenv('COS_KEY'),
        'secretKey' => getenv('COS_SECRET'))));

//bucket 的命名规则为{name}-{appid} ，此处填写的存储桶名称必须为此格式
$bucket = 'lewzylu02-1252448703';

try {
    $result = $cosClient->deleteBucketLifecycle(array(
        'Bucket' =>$bucket,
    ));
    print_r($result);
} catch (\Exception $e) {
    echo "$e\n";
}
```
