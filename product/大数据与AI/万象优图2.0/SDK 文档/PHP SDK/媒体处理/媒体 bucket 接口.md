## 简介

本文档提供关于查询媒体处理开通状态的 API 概览和 SDK 示例代码。

| API           | 操作描述                 |
| ------------- |  ---------------------- |
| [查询媒体处理开通状态](https://cloud.tencent.com/document/product/436/48988) | 查询媒体处理开通状态 |


## 查询媒体处理开通状态

#### 功能说明

查询已经开通媒体处理功能的存储桶。

#### 方法原型

```php
public Guzzle\Service\Resource\Model describeMediaBuckets(array $args = array());
```

#### 请求示例

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
    $result = $cosClient->describeMediaBuckets(array(
        'Regions' => '', // 可选 地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串
        'BucketNames' => '', // 可选 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索
        'BucketName' => '', // 可选 存储桶名称前缀，前缀搜索
        'PageNumber' => 1, // 可选 第几页
        'PageSize' => 20, // 可选 每页个数
    ));
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

Request 中的具体数据描述如下：

| 名称        | 描述                                                         | 类型   | 是否必选 |
| :---------- | :----------------------------------------------------------- | :----- | :------- |
| regions     | 地域信息，例如 ap-shanghai、ap-beijing，若查询多个地域以“,”分隔字符串，支持中国大陆地域，详情请参见 [地域与域名](https://cloud.tencent.com/document/product/460/31066) | string | 否       |
| bucketNames | 存储桶名称，以“,”分隔，支持多个存储桶，精确搜索              | string | 否       |
| bucketName  | 存储桶名称前缀，前缀搜索                                     | string | 否       |
| pageNumber  | 第几页                                                       | string | 否       |
| pageSize    | 每页个数                                                     | string | 否       |

#### 返回结果示例

```php
GuzzleHttp\Command\Result Object
(
    [RequestId] => NjI2MTE5OTlfNzgSxDxIHF0ZF8xZjk0MmQ=
    [ContentType] => application/xml
    [ContentLength] => 4744
    [TotalCount] => 51
    [PageNumber] => 1
    [PageSize] => 5
    [MediaBucketList] => Array
        (
            [0] => Array
                (
                    [BucketId] => examplebucket-1250000000
                    [Name] => examplebucket-1250000000
                    [Region] => ap-guangzhou
                    [CreateTime] => 2022-04-07T22:06:57+0800
                )

            [1] => Array
                (
                    [BucketId] => examplebucket-1250000000
                    [Name] => examplebucket-1250000000
                    [Region] => ap-guangzhou
                    [CreateTime] => 2022-04-07T22:06:57+0800
                )

            [2] => Array
                (
                    [BucketId] => examplebucket-1250000000
                    [Name] => examplebucket-1250000000
                    [Region] => ap-guangzhou
                    [CreateTime] => 2022-04-07T22:06:57+0800
                )

            [3] => Array
                (
                    [BucketId] => examplebucket-1250000000
                    [Name] => examplebucket-1250000000
                    [Region] => ap-guangzhou
                    [CreateTime] => 2022-04-07T22:06:57+0800
                )

            [4] => Array
                (
                    [BucketId] => examplebucket-1250000000
                    [Name] => examplebucket-1250000000
                    [Region] => ap-guangzhou
                    [CreateTime] => 2022-04-07T22:06:57+0800
                )

        )

    [Location] => ci.ap-guangzhou.myqcloud.com/mediabucket
)
```

