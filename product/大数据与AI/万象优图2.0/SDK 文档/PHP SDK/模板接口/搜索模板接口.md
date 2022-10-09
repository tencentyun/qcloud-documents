## 简介

本文档提供关于搜索模板接口的 API 概览和 SDK 示例代码。

| API           | 操作描述                 |
| ------------- |  ---------------------- |
| [搜索动图模板](https://cloud.tencent.com/document/product/436/54027) | 用于搜索动图模板。 |
| [搜索截图模板](https://cloud.tencent.com/document/product/436/54031) | 用于搜索截图模板。 |
| [搜索水印模板](https://cloud.tencent.com/document/product/436/54035) | 用于搜索水印模板。 |
| [搜索转码模板](https://cloud.tencent.com/document/product/436/54039) | 用于搜索转码模板。 |
| [搜索拼接模板](https://cloud.tencent.com/document/product/436/54043) | 用于搜索拼接模板。 |
| [搜索极速高清转码模板](https://cloud.tencent.com/document/product/436/58309) | 用于搜索极速高清转码模板。 |
| [搜索精彩集锦模板](https://cloud.tencent.com/document/product/436/58312) | 用于搜索精彩集锦模板。 |
| [搜索人声分离模板](https://cloud.tencent.com/document/product/436/58317) | 用于搜索人声分离转码模板。 |
| [搜索视频增强模板](https://cloud.tencent.com/document/product/436/60747) | 用于搜索视频增强模板。 |
| [搜索图片处理模板](https://cloud.tencent.com/document/product/436/67227) | 用于搜索图片处理模板。 |
| [搜索超分辨率模板](https://cloud.tencent.com/document/product/436/67168) | 用于搜索超分辨率模板。 |

## 搜索模板

#### 功能说明

用于搜索模板，支持 [Animation](https://cloud.tencent.com/document/product/436/54027)、[Snapshot](https://cloud.tencent.com/document/product/436/54031)、[Watermark](https://cloud.tencent.com/document/product/436/54035)、[Transcode](https://cloud.tencent.com/document/product/436/54039)、[Concat](https://cloud.tencent.com/document/product/436/54043)、[HighSpeedHd](https://cloud.tencent.com/document/product/436/58309)、[VideoMontage](https://cloud.tencent.com/document/product/436/58312)、[VoiceSeparate](https://cloud.tencent.com/document/product/436/58317)、[VideoProcess](https://cloud.tencent.com/document/product/436/60747)、[PicProcess](https://cloud.tencent.com/document/product/436/67227)、[SuperResolution](https://cloud.tencent.com/document/product/436/67168) 多种模板类型。

#### 方法原型

```php
public Guzzle\Service\Resource\Model describeMediaTemplates(array $args = array());
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
    // 查询模板列表
    $result = $cosClient->describeMediaTemplates(array(
        'Bucket' => 'examplebucket-125000000', //存储桶名称，由BucketName-Appid 组成，可以在COS控制台查看 https://console.cloud.tencent.com/cos5/bucket
        'Tag' => '', // 模板 Tag：Animation、Snapshot、Watermark、Transcode、Concat、HighSpeedHd、VideoMontage、VoiceSeparate、VideoProcess、PicProcess
        'Category' => 'Custom',
        'Ids' => '',
        'Name' => '',
        'PageNumber' => '',
        'PageSize' => '',
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

| 节点名称（关键字） | 父节点 | 描述                             | 类型    | 必选 |
| :----------------- | :----- | :------------------------------- | :------ | :--- |
| Tag                | 无     | 模板 Tag                         | String  | 是   |
| Category           | 无     | Official，Custom，默认值：Custom | String  | 否   |
| Ids                | 无     | 模板 ID，以`,`符号分割字符串     | String  | 否   |
| Name               | 无     | 模板名称前缀                     | String  | 否   |
| PageNumber         | 无     | 第几页                           | Integer | 否   |
| PageSize           | 无     | 每页个数                         | Integer | 否   |

#### 返回结果示例

```php
GuzzleHttp\Command\Result Object
(
    [RequestId] => NjJhOTRlZDFfNzgwYzdkAOIUDOAIUDTA4ZWE=
    [ContentType] => application/xml
    [ContentLength] => 782
    [TotalCount] => 1
    [PageNumber] => 1
    [PageSize] => 10
    [TemplateList] => Array
        (
            [0] => Array
                (
                    [TemplateId] => t1456ea89fcbdf45basd7fa98sd97a5
                    [Name] => VoiceSeparate-Name
                    [State] => Normal
                    [Tag] => VoiceSeparate
                    [CreateTime] => 2021-12-27T22:19:15+0800
                    [UpdateTime] => 2021-12-27T22:19:15+0800
                    [BucketId] => examplebucket-125000000
                    [Category] => Custom
                    [VoiceSeparate] => Array
                        (
                            [AudioMode] => AudioAndBackground
                            [AudioConfig] => Array
                                (
                                    [Codec] => mp3
                                    [Samplerate] => 44100
                                    [Bitrate] => 128
                                    [Channels] => 2
                                )

                        )

                )

        )

    [Bucket] => examplebucket-125000000
    [Location] => examplebucket-125000000.ci.ap-guangzhou.myqcloud.com/template
)
```
