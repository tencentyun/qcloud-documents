## 简介

本文档提供关于通用文字识别的 API 概览和 SDK 示例代码。

| API           | 操作描述                 |
| ------------- |  ---------------------- |
| [通用文字识别](https://cloud.tencent.com/document/product/436/64324) | 通用文字识别功能将图片上的文字内容，智能识别为可编辑的文本。 |

## 通用文字识别

#### 功能说明

通用文字识别功能（Optical Character Recognition，OCR）基于行业前沿的深度学习技术，将图片上的文字内容，智能识别为可编辑的文本，可应用于随手拍扫描、纸质文档电子化、电商广告审核等多种场景，大幅提升信息处理效率。

#### 方法原型

```php
public Guzzle\Service\Resource\Model opticalOcrRecognition(array $args = array());
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
    // https://cloud.tencent.com/document/product/436/64324 通用文字识别
    $result = $cosClient->opticalOcrRecognition(array(
        'Bucket' => 'examplebucket-1250000000', //存储桶名称，由 BucketName-Appid 组成，可以在 COS 控制台查看 https://console.cloud.tencent.com/cos5/bucket
        'Key' => 'test01.pdf',
        'CiProcess' => 'OCR',
        'Type' => 'general',
        'LanguageType' => 'zh',
        'IsPDF' => 'true',
        'PdfPageNumber' => 2,
        'IsWord' => 'true',
        'EnableWordPolygon' => 'false',
    ));
    // 请求成功
    print_r($result);
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 参数名称          | 描述                                                         | 类型    | 是否必选 |
| :---------------- | :----------------------------------------------------------- | :------ | :------- |
| Key               | 对象文件名，例如：folder/document.jpg。                      | String  | 是       |
| CiProcess         | 数据万象处理能力，图片文字识别固定为 OCR。                   | String  | 是       |
| Type              | OCR 的识别类型，有效值为 general，accurate，efficient，fast，handwriting。general 表示通用印刷体识别；accurate 表示印刷体高精度版；efficient 表示印刷体精简版；fast 表示印刷体高速版；handwriting 表示手写体识别。默认值为 general。 | String  | 否       |
| LanguageType      | type 值为 general 时有效，表示识别语言类型。支持自动识别语言类型，同时支持自选语言种类，默认中英文混合(zh)，各种语言均支持与英文混合的文字识别。可选值请参见 [可识别的语言类型](https://cloud.tencent.com/document/product/436/64324#language-type)。 | String  | 否       |
| IsPDF             | type 值为 general、fast 时有效，表示是否开启 PDF 识别，有效值为 true 和 false，默认值为 false，开启后可同时支持图片和 PDF 的识别。 | Boolean | 否       |
| PdfPageNumber     | type 值为 general、fast 时有效，表示需要识别的 PDF 页面的对应页码，仅支持 PDF 单页识别，当上传文件为 PDF 且 ispdf 参数值为 true 时有效，默认值为1。 | Integer | 否       |
| IsWord            | type 值为 general、accurate 时有效，表示识别后是否需要返回单字信息，有效值为 true 和 false，默认为 false。 | Boolean | 否       |
| EnableWordPolygon | type 值为 handwriting 时有效，表示是否开启单字的四点定位坐标输出，有效值为 true 和 false，默认值为 false。 | Boolean | 否       |

#### 返回结果示例

```php
GuzzleHttp\Command\Result Object
(
    [Body] => GuzzleHttp\Psr7\Stream Object
        (
            [stream:GuzzleHttp\Psr7\Stream:private] => Resource id #89
            [size:GuzzleHttp\Psr7\Stream:private] => 
            [seekable:GuzzleHttp\Psr7\Stream:private] => 1
            [readable:GuzzleHttp\Psr7\Stream:private] => 1
            [writable:GuzzleHttp\Psr7\Stream:private] => 1
            [uri:GuzzleHttp\Psr7\Stream:private] => php://temp
            [customMetadata:GuzzleHttp\Psr7\Stream:private] => Array
                (
                )

        )

    [RequestId] => NjJhOThmYjZfAOIUDOIUSDOITkwYTU1Zg==
    [ContentType] => application/xml
    [ContentLength] => 3144
    [Key] => test01.pdf
    [Bucket] => examplebucket-1250000000
    [Location] => examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/test01.pdf
    [Response] => Array
        (
            [Angel] => 359.99
            [Language] => zh
            [PdfPageSize] => 5
            [RequestId] => NjJhOThmYjZfAOIUDOIUSDOITkwYTU1Zg=
            [TextDetections] => Array
                (
                    [0] => Array
                        (
                            [Confidence] => 99
                            [DetectedText] => 第二页
                            [ItemPolygon] => Array
                                (
                                    [Height] => 118
                                    [Width] => 351
                                    [X] => 782
                                    [Y] => 403
                                )

                            [Polygon] => Array
                                (
                                    [0] => Array
                                        (
                                            [X] => 782
                                            [Y] => 403
                                        )

                                    [1] => Array
                                        (
                                            [X] => 1133
                                            [Y] => 403
                                        )

                                    [2] => Array
                                        (
                                            [X] => 1133
                                            [Y] => 521
                                        )

                                    [3] => Array
                                        (
                                            [X] => 782
                                            [Y] => 521
                                        )

                                )

                            [Words] => Array
                                (
                                    [0] => Array
                                        (
                                            [Character] => 第
                                            [Confidence] => 100
                                            [WordCoordPoint] => Array
                                                (
                                                    [WordCoordinate] => Array
                                                        (
                                                            [0] => Array
                                                                (
                                                                    [X] => 796
                                                                    [Y] => 403
                                                                )

                                                            [1] => Array
                                                                (
                                                                    [X] => 885
                                                                    [Y] => 403
                                                                )

                                                            [2] => Array
                                                                (
                                                                    [X] => 885
                                                                    [Y] => 521
                                                                )

                                                            [3] => Array
                                                                (
                                                                    [X] => 796
                                                                    [Y] => 521
                                                                )

                                                        )

                                                )

                                        )

                                    [1] => Array
                                        (
                                            [Character] => 二
                                            [Confidence] => 99
                                            [WordCoordPoint] => Array
                                                (
                                                    [WordCoordinate] => Array
                                                        (
                                                            [0] => Array
                                                                (
                                                                    [X] => 885
                                                                    [Y] => 403
                                                                )

                                                            [1] => Array
                                                                (
                                                                    [X] => 1034
                                                                    [Y] => 403
                                                                )

                                                            [2] => Array
                                                                (
                                                                    [X] => 1034
                                                                    [Y] => 521
                                                                )

                                                            [3] => Array
                                                                (
                                                                    [X] => 885
                                                                    [Y] => 521
                                                                )

                                                        )

                                                )

                                        )

                                    [2] => Array
                                        (
                                            [Character] => 页
                                            [Confidence] => 99
                                            [WordCoordPoint] => Array
                                                (
                                                    [WordCoordinate] => Array
                                                        (
                                                            [0] => Array
                                                                (
                                                                    [X] => 1033
                                                                    [Y] => 403
                                                                )

                                                            [1] => Array
                                                                (
                                                                    [X] => 1133
                                                                    [Y] => 403
                                                                )

                                                            [2] => Array
                                                                (
                                                                    [X] => 1133
                                                                    [Y] => 521
                                                                )

                                                            [3] => Array
                                                                (
                                                                    [X] => 1033
                                                                    [Y] => 521
                                                                )

                                                        )

                                                )

                                        )

                                )

                        )

                    [1] => Array
                        (
                            [Confidence] => 99
                            [DetectedText] => 内容
                            [ItemPolygon] => Array
                                (
                                    [Height] => 50
                                    [Width] => 93
                                    [X] => 914
                                    [Y] => 569
                                )

                            [Polygon] => Array
                                (
                                    [0] => Array
                                        (
                                            [X] => 914
                                            [Y] => 569
                                        )

                                    [1] => Array
                                        (
                                            [X] => 1007
                                            [Y] => 572
                                        )

                                    [2] => Array
                                        (
                                            [X] => 1005
                                            [Y] => 622
                                        )

                                    [3] => Array
                                        (
                                            [X] => 912
                                            [Y] => 619
                                        )

                                )

                            [Words] => Array
                                (
                                    [0] => Array
                                        (
                                            [Character] => 内
                                            [Confidence] => 99
                                            [WordCoordPoint] => Array
                                                (
                                                    [WordCoordinate] => Array
                                                        (
                                                            [0] => Array
                                                                (
                                                                    [X] => 919
                                                                    [Y] => 569
                                                                )

                                                            [1] => Array
                                                                (
                                                                    [X] => 958
                                                                    [Y] => 570
                                                                )

                                                            [2] => Array
                                                                (
                                                                    [X] => 956
                                                                    [Y] => 620
                                                                )

                                                            [3] => Array
                                                                (
                                                                    [X] => 917
                                                                    [Y] => 619
                                                                )

                                                        )

                                                )

                                        )

                                    [1] => Array
                                        (
                                            [Character] => 容
                                            [Confidence] => 99
                                            [WordCoordPoint] => Array
                                                (
                                                    [WordCoordinate] => Array
                                                        (
                                                            [0] => Array
                                                                (
                                                                    [X] => 958
                                                                    [Y] => 570
                                                                )

                                                            [1] => Array
                                                                (
                                                                    [X] => 1007
                                                                    [Y] => 572
                                                                )

                                                            [2] => Array
                                                                (
                                                                    [X] => 1005
                                                                    [Y] => 622
                                                                )

                                                            [3] => Array
                                                                (
                                                                    [X] => 956
                                                                    [Y] => 620
                                                                )

                                                        )

                                                )

                                        )

                                )

                        )

                )

        )

)
```

