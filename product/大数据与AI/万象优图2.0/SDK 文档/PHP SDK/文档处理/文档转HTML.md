## 简介

本文档提供关于文档预览的相关的 API 概览以及 SDK 示例代码。

| API           |    操作名  |   操作描述               |
| :--------------- | :------------------ | :--------------------- |
| [文档转 HTML](https://cloud.tencent.com/document/product/436/54059) |   文档转 HTML 同步请求   |获取文档转 HTML 的请求 URL |

## 文档转 HTML

#### 功能说明

文档转 HTML 同步请求，获取文档转 HTML 的请求 URL。

#### 示例代码

```php
<?php

require dirname(__FILE__, 2) . '/vendor/autoload.php';

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
    // 2. 文档转HTML https://cloud.tencent.com/document/product/460/52518
    $bucket = 'examplebucket-1250000000';
    $key = 'exampleobject';
    $url = $cosClient->getObjectUrl($bucket, $key, "+30 minutes");
    $params = array(
        'ci-process' => 'doc-preview',
//        'srcType' => '',
        'dstType' => 'html',
//        'sign' => '',
//        'copyable' => '',
//        'htmlParams' => '',
//        'htmlwaterword' => '',
//        'htmlfillstyle' => '',
//        'htmlfront' => '',
//        'htmlrotate' => '',
//        'htmlhorizontal' => '',
//        'htmlvertical' => '',
    );
    $query = http_build_query($params);
    echo $url . $query; // 生成的可访问链接
} catch (\Exception $e) {
    // 请求失败
    echo($e);
}
```

#### 参数说明

| 名称           | 描述                                                         | 类型   | 是否必选 |
| :------------- | :----------------------------------------------------------- | :----- | :------- |
| Key            | 对象文件名，例如 folder/document.pdf                         | String | 是       |
| ci-process     | 数据万象处理能力，文档 HTML 预览固定为 doc-preview           | String | 是       |
| dstType        | 转换输出目标文件类型，文档 HTML 预览固定为 html（需为小写字母） | String | 是       |
| srcType        | 指定目标文件类型，支持的文件类型请见下方                     | String | 否       |
| sign           | 对象下载签名，如果预览的对象为私有读时，需要传入签名，详情请参见 [请求签名](https://cloud.tencent.com/document/product/460/6968) 文档</br>注意：需要进行 urlencode | String | 否       |
| copyable       | 是否可复制。默认为可复制，填入值为1；不可复制，填入值为0     | String | 否       |
| htmlParams     | 自定义配置参数，JSON 结构，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/32832#.E4.BB.80.E4.B9.88.E6.98.AF-url-.E5.AE.89.E5.85.A8.E7.9A.84-base64-.E7.BC.96.E7.A0.81.EF.BC.9F) 的 Base64 编码，默认配置为：{ commonOptions: { isShowTopArea: true, isShowHeader: true } }，支持的配置参考 [自定义配置项说明](https://cloud.tencent.com/document/product/436/59408#.E8.87.AA.E5.AE.9A.E4.B9.89.E9.85.8D.E7.BD.AE.E9.80.89.E9.A1.B9) | String | 否       |
| htmlwaterword  | 水印文字，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/32832#.E4.BB.80.E4.B9.88.E6.98.AF-url-.E5.AE.89.E5.85.A8.E7.9A.84-base64-.E7.BC.96.E7.A0.81.EF.BC.9F) 的 Base64 编码，默认为空 | String | 否       |
| htmlfillstyle  | 水印 RGBA（颜色和透明度），需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/32832#.E4.BB.80.E4.B9.88.E6.98.AF-url-.E5.AE.89.E5.85.A8.E7.9A.84-base64-.E7.BC.96.E7.A0.81.EF.BC.9F) 的 Base64 编码，默认为：rgba(192,192,192,0.6) | String | 否       |
| htmlfront      | 水印文字样式，需要经过 [URL 安全](https://cloud.tencent.com/document/product/460/32832#.E4.BB.80.E4.B9.88.E6.98.AF-url-.E5.AE.89.E5.85.A8.E7.9A.84-base64-.E7.BC.96.E7.A0.81.EF.BC.9F) 的 Base64 编码，默认为：bold 20px Serif | String | 否       |
| htmlrotate     | 水印文字旋转角度，0 - 360，默认315度                         | String | 否       |
| htmlhorizontal | 水印文字水平间距，单位 px，默认为50                          | String | 否       |
| htmlvertical   | 水印文字垂直间距，单位 px，默认为100                         | String | 否       |

>!
> - 目前支持的输入文件类型包含如下格式：
>   - 演示文件：pptx、ppt、pot、potx、pps、ppsx、dps、dpt、pptm、potm、ppsm。
>   - 文字文件：doc、dot、wps、wpt、docx、dotx、docm、dotm。
>   - 表格文件：xls、xlt、et、ett、xlsx、xltx、csv、xlsb、xlsm、xltm、ets。
>   - 其他格式文件： pdf、 lrc、 c、 cpp、 h、 asm、 s、 java、 asp、 bat、 bas、 prg、 cmd、 rtf、 txt、 log、 xml、 htm、 html。
> - 输入文件大小限制在200MB之内。
> - 输入文件页数限制在5000页之内。
> 

#### 返回结果示例

```php
同步请求URL
https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/example.ppt?sign=q-sign-algorithmxxxxxxxxxxxxx&ci-process=doc-preview&dstType=html
```

