## Overview

VOD provides a PHP-based SDK which is based on COS PHP SDK and Cloud API SDK. Users can refer to this SDK to upload videos and cover image files stored in their servers directly into Tencent Cloud VOD system.

## Download Links

* [visit Github >>](https://github.com/tencentyun/vod-php-sdk-v5)
* [click to download PHP SDK >>](https://github.com/tencentyun/vod-php-sdk-v5/archive/master.zip)

## How to Use

### With Composer
* install dependency

```json
{
    "require": {
        "qcloud/vod-sdk-v5": "v1.2.1"
    }
}
```
* example

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
After the upload is successful, the file's play address and fileid will be obtained

### Without Composer

* copy the src file under the source code and test/non-composer file cos-sdk-v5, qcloudapi-sdk-php to the same level directory
* example

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
After the upload is successful, the file's play address and fileid will be obtained