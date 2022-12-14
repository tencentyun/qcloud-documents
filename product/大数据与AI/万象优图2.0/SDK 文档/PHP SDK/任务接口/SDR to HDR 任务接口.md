## 简介

本文档提供关于SDR to HDR 任务接口的 API 概览和 SDK 示例代码。

| API                                                          | 操作描述             |
| ------------------------------------------------------------ | -------------------- |
| [提交 SDR to HDR 任务](https://cloud.tencent.com/document/product/436/60754) | 提交 SDR to HDR 任务 |


## 提交 SDR to HDR 任务

#### 功能说明

提交 SDR to HDR 任务。

#### 方法原型

```php
public Guzzle\Service\Resource\Model createMediaSDRtoHDRJobs(array $args = array());
```

#### 请求示例

```php
<?php

require dirname(__FILE__) . '/../vendor/autoload.php';

$secretId = "SECRETID"; //替换为用户的 secretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
$secretKey = "SECRETKEY"; //替换为用户的 secretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
$region = "ap-beijing"; //替换为用户的 region，已创建桶归属的 region 可以在控制台查看，https://console.cloud.tencent.com/cos5/bucket
$cosClient = new Qcloud\Cos\Client(
    array(
        'region' => $region,
        'schema' => 'https', //协议头部，默认为 http
        'credentials'=> array(
            'secretId'  => $secretId ,
            'secretKey' => $secretKey)));
try {
    // 提交 SDR to HDR 任务 https://cloud.tencent.com/document/product/436/60754
    $result = $cosClient->createMediaSDRtoHDRJobs(array(
        'Bucket' => 'examplebucket-1250000000', //存储桶名称，由 BucketName-Appid 组成，可以在 COS 控制台查看 https://console.cloud.tencent.com/cos5/bucket
        'Tag' => 'SDRtoHDR',
        'QueueId' => 'p81e648af2aee496885a8d09a8s09d8a0sd6',
        'Input' => array(
            'Object' => 'video01.mp4'
        ),
        'Operation' => array(
            'TranscodeTemplateId' => '',
            'WatermarkTemplateId' => '',
            'SDRtoHDR' => array(
                'HdrMode' => 'HLG',
            ),
            'Output' => array(
                'Region' => $region,
                'Bucket' => 'examplebucket-1250000000', //存储桶名称，由 BucketName-Appid 组成，可以在 COS 控制台查看 https://console.cloud.tencent.com/cos5/bucket
                'Object' => 'SDRtoHDR.flv',
            ),
//            'UserData' => 'xxx', // 透传用户信息
//            'JobLevel' => '0', // 任务优先级，级别限制：0 、1 、2。级别越大任务优先级越高，默认为0
        ),
        'CallBack' => '',
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

| 节点名称（关键字） | 父节点  | 描述                                                         | 类型      | 是否必选 |
| :----------------- | :------ | :----------------------------------------------------------- | :-------- | :------- |
| Tag                | Request | 创建任务的 Tag：SDRtoHDR                                     | String    | 是       |
| Input              | Request | 待操作的媒体信息                                             | Container | 是       |
| Operation          | Request | 操作规则                                                     | Container | 是       |
| QueueId            | Request | 任务所在的队列 ID                                            | String    | 是       |
| CallBackFormat     | Request | 任务回调格式，JSON 或 XML，默认 XML，优先级高于队列的回调格式 | String    | 否       |
| CallBackType       | Request | 任务回调类型，Url 或 TDMQ，默认 Url，优先级高于队列的回调类型 | String    | 否       |
| CallBack           | Request | 任务回调地址，优先级高于队列的回调地址。设置为 no 时，表示队列的回调地址不产生回调 | String    | 否       |
| CallBackMqConfig   | Request | 任务回调 TDMQ 配置，当 CallBackType 为 TDMQ 时必填。详情见 [CallBackMqConfig](https://cloud.tencent.com/document/product/460/78927#CallBackMqConfig) | Container | 否       |

Container 类型 Input 的具体数据描述如下：

| 节点名称（关键字） | 父节点        | 描述       | 类型   | 是否必选 |
| :----------------- | :------------ | :--------- | :----- | :------- |
| Object             | Request.Input | 媒体文件名 | String | 是       |


Container 类型 Operation 的具体数据描述如下：

| 节点名称（关键字）  | 父节点            | 描述                                                         | 类型           | 是否必选 |
| :------------------ | :---------------- | :----------------------------------------------------------- | :------------- | :------- |
| SDRtoHDR            | Request.Operation | 指定 SDRtoHDR 参数                                           | Container      | 是       |
| Transcode           | Request.Operation | 指定转码模板参数，不能与 TranscodeTemplateId 同时为空        | Container      | 否       |
| TranscodeTemplateId | Request.Operation | 指定的转码模板 ID，优先使用模板 ID，不能与 Transcode 同时为空 | String         | 否       |
| Watermark           | Request.Operation | 指定水印模板参数，同创建水印模板 [CreateMediaTemplate](https://cloud.tencent.com/document/product/460/77099#Watermark) 接口中的 Request.Watermark, 最多传3个 | Container 数组 | 否       |
| WatermarkTemplateId | Request.Operation | 指定的水印模板 ID，可以传多个水印模板 ID，最多传3个，优先使用模板 ID | String 数组    | 否       |
| Output              | Request.Operation | 结果输出地址                                                 | Container      | 是       |
| UserData            | Request.Operation | 透传用户信息, 可打印的 ASCII 码, 长度不超过1024              | String         | 否       |
| JobLevel            | Request.Operation | 任务优先级，级别限制：0 、1 、2。级别越大任务优先级越高，默认为0 | String         | 否       |

>?
>
> 提交 SDRtoHDR 任务必须传入转码参数。对于转码参数，优先使用 TranscodeTemplateId，无 TranscodeTemplateId 时使用 Transcode；对于水印参数，可以使用 WatermarkTemplateId 或Watermark 设置，WatermarkTemplateId 优先级更高。

Container 类型 SDRtoHDR 的具体数据描述如下：

| 节点名称（关键字） | 父节点                     | 描述     | 类型   | 是否必选 | 限制            |
| :----------------- | :------------------------- | :------- | :----- | :------- | :-------------- |
| HdrMode            | Request.Operation.SDRtoHDR | HDR 标准 | String | 是       | 1. HLG 2. HDR10 |

Container 类型 Transcode 的具体数据描述如下：

| 节点名称（关键字） | 父节点                      | 描述                                                         | 类型           | 必选 |
| :----------------- | :-------------------------- | :----------------------------------------------------------- | :------------- | :--- |
| TimeInterval       | Request.Operation.Transcode | 同创建转码模板 [CreateMediaTemplate](https://cloud.tencent.com/document/product/460/77093#TimeInterval) 接口中的 Request.TimeInterval | Container      | 否   |
| Container          | Request.Operation.Transcode | 同创建转码模板 [CreateMediaTemplate](https://cloud.tencent.com/document/product/460/77093#Container) 接口中的 Request.Container | Container      | 否   |
| Video              | Request.Operation.Transcode | 同创建转码模板 [CreateMediaTemplate](https://cloud.tencent.com/document/product/460/77093#Video) 接口中的 Request.Video | Container      | 否   |
| Audio              | Request.Operation.Transcode | 同创建转码模板 [CreateMediaTemplate](https://cloud.tencent.com/document/product/460/77093#Audio) 接口中的 Request.Audio | Container      | 否   |
| TransConfig        | Request.Operation.Transcode | 同创建转码模板 [CreateMediaTemplate](https://cloud.tencent.com/document/product/460/77093#TransConfig) 接口中的 Request.TransConfig | Container      | 否   |
| AudioMix           | Request.Operation.Transcode | 混音参数, 详情见[AudioMix](https://cloud.tencent.com/document/product/460/78927#AudioMix) | Container 数组 | 否   |

Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点                   | 描述             | 类型   | 是否必选 |
| :----------------- | :----------------------- | :--------------- | :----- | :------- |
| Region             | Request.Operation.Output | 存储桶的地域     | String | 是       |
| Bucket             | Request.Operation.Output | 存储结果的存储桶 | String | 是       |
| Object             | Request.Operation.Output | 输出结果的文件名 | String | 是       |

#### 返回结果示例

```php
GuzzleHttp\Command\Result Object
(
    [Body] => GuzzleHttp\Psr7\Stream Object
        (
            [stream:GuzzleHttp\Psr7\Stream:private] => Resource id #88
            [size:GuzzleHttp\Psr7\Stream:private] => 
            [seekable:GuzzleHttp\Psr7\Stream:private] => 1
            [readable:GuzzleHttp\Psr7\Stream:private] => 1
            [writable:GuzzleHttp\Psr7\Stream:private] => 1
            [uri:GuzzleHttp\Psr7\Stream:private] => php://temp
            [customMetadata:GuzzleHttp\Psr7\Stream:private] => Array
                (
                )

        )

    [RequestId] => NjI2N2I1NWFfZmNjYTNHDOASJDOIA1Yw==
    [ContentType] => application/xml
    [ContentLength] => 902
    [Bucket] => examplebucket-1250000000
    [Location] => examplebucket-1250000000.ci.ap-guangzhou.myqcloud.com/jobs
    [Response] => Array
        (
            [JobsDetail] => Array
                (
                    [Code] => Success
                    [CreationTime] => 2022-04-26T17:03:22+0800
                    [EndTime] => -
                    [Input] => Array
                        (
                            [BucketId] => examplebucket-1250000000
                            [Object] => video01.mp4
                            [Region] => ap-guangzhou
                        )

                    [JobId] => jb9289626c53f11ec8a9c4f3d8d099dcb
                    [Message] => 
                    [Operation] => Array
                        (
                            [Output] => Array
                                (
                                    [Bucket] => examplebucket-1250000000
                                    [Object] => SDRtoHDR.flv
                                    [Region] => ap-guangzhou
                                )

                            [SDRtoHDR] => Array
                                (
                                    [HdrMode] => HLG
                                )

                            [TranscodeTemplateId] => t0b612860a293f410785ba7s8d09a8d09a38
                            [WatermarkTemplateId] => t185e2e24551b242d09a80d8a0d80428a19c
                            [UserData] => xxx
                            [JobLevel] => 0
                        )

                    [QueueId] => t185e2e24551b242d09a80d8a0d80428a19c
                    [StartTime] => -
                    [State] => Submitted
                    [Tag] => SDRtoHDR
                )

        )

)
```



