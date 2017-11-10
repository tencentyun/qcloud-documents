## 简介

基于 COS 的 PHP SDK 和云 API 的 SDK，VOD 提供了一个 PHP语言的 SDK，通过该 SDK，用户可以将服务端的视频和封面文件直接上传到腾讯云点播系统。

## 下载地址

* [从 Github 访问 >>](https://github.com/tencentyun/vod-php-sdk-v5)
* [点击下载 PHP SDK >>](https://github.com/tencentyun/vod-php-sdk-v5/archive/master.zip)

## 使用方式

### With Composer
* 引入依赖

```json
{
    "require": {
        "qcloud/vod-sdk-v5": "v1.2.1"
    }
}
```
* 调用示例

```php
<?php
require 'vendor/autoload.php';

use Vod\VodApi;

VodApi::initConf("your secretId", "your secretKey");

$result = VodApi::upload(
    array (
        'videoPath' => './test/Wildlife.wmv',
    ),
    array (
        'videoName' => 'WildAnimals',
//        'procedure' => 'myProcedure',
//        'sourceContext' => 'test',
    )
);
echo "upload to vod result: " . json_encode($result) . "\n";
```
上传成功后将获取文件的播放地址和 fileid

### Without Composer

* 复制src文件下的源码和test/non-composer文件的cos-sdk-v5、qcloudapi-sdk-php到同级目录
* 调用示例

```php
<?php
require './cos-sdk-v5/cos-autoloader.php';
require './qcloudapi-sdk-php/src/QcloudApi/QcloudApi.php';
require './src/Vod/VodApi.php';
require './src/Vod/Conf.php';

use Vod\VodApi;

VodApi::initConf("your secretId", "your secretKey");

$result = VodApi::upload(
    array (
        'videoPath' => '../Wildlife.wmv',
    ),
    array (
        'videoName' => 'WildAnimals',
//        'procedure' => 'myProcedure',
//        'sourceContext' => 'test',
    )
);
echo "upload to vod result: " . json_encode($result) . "\n";
```
上传成功后将获取文件的播放地址和 fileid