## 简介

本文档提供关于 Guetzli 压缩的相关的 API 概览以及 SDK 示例代码。

| API           |  操作描述               |
| :--------------- | :------------------ | 
| [开通 Guetzli 压缩](https://cloud.tencent.com/document/product/460/30112) | 对 Bucket 开通 Guetzli 压缩功能   |
| [查询 Guetzli 状态](https://cloud.tencent.com/document/product/460/30111) |用于查询 Guetzli 压缩功能是否开启 |
|[关闭 Guetzli 压缩](https://cloud.tencent.com/document/product/460/30113)  |   用于关闭 Guetzli 压缩功能   |

## 开通 Guetzli 压缩

#### 功能说明

对 Bucket 开通 Guetzli 压缩功能。

#### 示例代码

```php
<?php

require dirname(__FILE__) . '/../vendor/autoload.php';

$secretId = "SECRETID"; //替换为用户的 secretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
$secretKey = "SECRETKEY"; //替换为用户的 secretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
$region = "ap-beijing"; //替换为用户的 region，已创建桶归属的region可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为http
        'credentials'=> array(
            'secretId'  => $secretId ,
            'secretKey' => $secretKey)));

try {
        $result = $cosClient->PutBucketGuetzli(array(
        'Bucket' => 'examplebucket-1250000000', //存储桶名称，由BucketName-Appid 组成，可以在COS控制台查看 https://console.cloud.tencent.com/cos5/bucket
    ));
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称             | 类型        | 描述                                                         | 是否必填 |
| -------------------- | ----------- | ------------------------------------------------------------ | -------- |
| Bucket          | String      | 存储桶名称，格式：BucketName-APPID                        | 是       |

#### 返回结果示例

```php
Guzzle\Service\Resource\Model Object
(
    [structure:protected] => 
    [data:protected] => Array
        (
            [RequestId] => NWQwOGRkNDdfMjJiMjU4NjRfNzVjXzEwNmVjY2M=
            [Bucket] => examplebucket-1250000000
            [Location] => examplebucket-1250000000.pic.ap-beijing.myqcloud.com/
        )
)

```

#### 返回结果说明

| 参数名称             | 类型        | 描述                                          | 父节点  |
| -------------------- | ----------- | ------------------------------------------------- | ------ |
| RequestId             | String      | 请求 ID 标识                                | 无     |
| Bucket               | String      | 存储桶名称，格式：BucketName-APPID              | 无     |
| Location             | String      | 请求资源地址                                 | 无     |

## 查询 Guetzli 状态

#### 功能说明

用于查询 Guetzli 压缩功能是否开启。

#### 示例代码

```php
<?php

require dirname(__FILE__) . '/../vendor/autoload.php';

$secretId = "SECRETID"; //替换为用户的 secretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
$secretKey = "SECRETKEY"; //替换为用户的 secretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
$region = "ap-beijing"; //替换为用户的 region，已创建桶归属的region可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为http
        'credentials'=> array(
            'secretId'  => $secretId ,
            'secretKey' => $secretKey)));

try {
        $result = $cosClient->GetBucketGuetzli(array(
        'Bucket' => 'examplebucket-1250000000', //存储桶名称，由BucketName-Appid 组成，可以在COS控制台查看 https://console.cloud.tencent.com/cos5/bucket
    ));
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称             | 类型        | 描述                                                         | 是否必填 |
| -------------------- | ----------- | ------------------------------------------------------------ | -------- |
| Bucket          | String      | 存储桶名称，格式：BucketName-APPID                        | 是       |

#### 返回结果示例

```php
Guzzle\Service\Resource\Model Object
(
    [structure:protected] => 
    [data:protected] => Array
        (
            [RequestId] => NWQwOGRkNDdfMjJiMjU4NjRfNzVjXzEwNmVjY2M=
            [Bucket] => examplebucket-1250000000
            [Location] => examplebucket-1250000000.pic.ap-beijing.myqcloud.com/
            [GuetzliStatus] => on
        )
)

```

#### 返回结果说明

| 参数名称             | 类型        | 描述                                          | 父节点  |
| -------------------- | ----------- | ------------------------------------------------- | ------ |
| RequestId             | String      | 请求 ID 标识                                | 无     |
| Bucket               | String      | 存储桶名称，格式：BucketName-APPID              | 无     |
| Location             | String      | 请求资源地址                                 | 无     |
| GuetzliStatus         | String      | Guetzli 状态，on：开启，off：关闭                | 无     |

## 关闭 Guetzli 压缩

用于关闭 Guetzli 压缩功能。

#### 示例代码

```php
<?php

require dirname(__FILE__) . '/../vendor/autoload.php';

$secretId = "SECRETID"; //替换为用户的 secretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
$secretKey = "SECRETKEY"; //替换为用户的 secretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
$region = "ap-beijing"; //替换为用户的 region，已创建桶归属的region可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为http
        'credentials'=> array(
            'secretId'  => $secretId ,
            'secretKey' => $secretKey)));
            
try {
        $result = $cosClient->DeleteBucketGuetzli(array(
        'Bucket' => 'examplebucket-1250000000', //存储桶名称，由BucketName-Appid 组成，可以在COS控制台查看 https://console.cloud.tencent.com/cos5/bucket
    ));
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称             | 类型        | 描述                                                         | 是否必填 |
| -------------------- | ----------- | ------------------------------------------------------------ | -------- |
| Bucket          | String      | 存储桶名称，格式：BucketName-APPID                        | 是       |

#### 返回结果示例

```php
Guzzle\Service\Resource\Model Object
(
    [structure:protected] => 
    [data:protected] => Array
        (
            [RequestId] => NWQwOGRkNDdfMjJiMjU4NjRfNzVjXzEwNmVjY2M=
            [Bucket] => examplebucket-1250000000
            [Location] => examplebucket-1250000000.pic.ap-beijing.myqcloud.com/
        )
)

```

##### 返回结果说明

| 参数名称             | 类型        | 描述                                          | 父节点  |
| -------------------- | ----------- | ------------------------------------------------- | ------ |
| RequestId             | String      | 请求 ID 标识                                | 无     |
| Bucket               | String      | 存储桶名称，格式：BucketName-APPID              | 无     |
| Location             | String      | 请求资源地址                                 | 无     |
