## 简介

本文档提供关于如何使用非默认域名请求对象存储（Cloud Object Storage，COS）服务。

## 相关参数说明

通过初始化参数，来控制请求域名，相关的参数说明如下：

| 参数名                 | 参数描述                                                     | 类型     | 是否必填 |
| ---------------------- | ------------------------------------------------------------ | -------- | ---- |
| Domain                 | 调用操作存储桶和对象的 API 时自定义请求域名。可以使用模板，如`"{$Bucket}.cos.{$Region}.myqcloud.com" `，即在调用 API 时会使用参数中传入的 Bucket 和 Region 进行替换。 | String   | 否   |
| Protocol               | 发请求时用的协议，可选项`https:`、`http:`，默认判断当前页面是`http:` 时使用`http:`，否则使用`https:` | String   | 否   |

## 默认 CDN 加速域名

关于如何开启默认加速域名请参考 [开启默认 CDN 加速域名](https://cloud.tencent.com/document/product/436/36636)。

以下代码展示了如何使用默认加速域名访问 COS 服务。

```php
$bucket = "examplebucket-1250000000";

$cosClient = new Qcloud\Cos\Client(
    array(
        'domain' => $bucket . '.file.myqcloud.com', //默认加速域名
        'schema' => 'https', //协议头部，默认为http
        'credentials'=> array(
            'secretId'  => $secretId,
            'secretKey' => $secretKey
        )
    )
);
```

## 自定义 CDN 加速域名

关于如何开启 CDN 自定义加速域名请参考 [开启自定义 CDN 加速域名](https://cloud.tencent.com/document/product/436/36637)。

以下代码展示了如何使用自定义加速域名访问 COS 服务。

```php
$cosClient = new Qcloud\Cos\Client(
    array(
        'domain' => 'example-cdn-domain.com', //默认加速域名
        'schema' => 'https', //协议头部，默认为http
        'credentials'=> array(
            'secretId'  => $secretId,
            'secretKey' => $secretKey
        )
    )
);
```

## 自定义源站域名

关于如何设置自定义源站域名请参考 [自定义源站域名](https://cloud.tencent.com/document/product/436/36638)。

以下代码展示了如何使用自定义源站域名访问 COS 服务。

```php
$cosClient = new Qcloud\Cos\Client(
    array(
        'domain' => 'example-cos-domain.com', //默认加速域名
        'schema' => 'https', //协议头部，默认为http
        'credentials'=> array(
            'secretId'  => $secretId,
            'secretKey' => $secretKey
        )
    )
);
```

## 全球加速域名

关于全球加速功能请参考 [全球加速功能概述](https://cloud.tencent.com/document/product/436/38866)。

以下代码展示了如何使用全球加速域名访问 COS 服务。

```php
//{$bucket}.cos.{$region}.myqcloud.com/key 转换为
//{$bucket}.cos.accelerate.myqcloud.com/key
$cosClient = new Qcloud\Cos\Client(
    array(
        'schema' => 'https', //协议头部，默认为http
        'credentials'=> array(
            'secretId'  => $secretId,
            'secretKey' => $secretKey
        ),
        'allow_accelerate' => true // 指定 true，使用全球加速域名请求
    )
);
```
