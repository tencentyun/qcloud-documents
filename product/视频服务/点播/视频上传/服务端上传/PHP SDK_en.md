## Overview

The PHP SDK is used to upload videos and cover image files stored in the servers into Tencent Cloud VOD system.

## Integration Method

### Using Composer
```json
{
    "require": {
        "qcloud/vod-sdk-v5": "v1.2.1"
    }
}
```

### Using Source File
If the composer tool is not reruired for dependency management in the project, you can download the source code directly into the project:

* [Access from Github >>](https://github.com/tencentyun/vod-php-sdk-v5)
* [Click to download PHP SDK >>](https://github.com/tencentyun/vod-php-sdk-v5/archive/master.zip)

Copy the source codes in the src file and cos-sdk-v5, qcloudapi-sdk-php in the file test/non-composer to the project directory of the same level

## Steps for Upload
### Step 1: Initialize Configuration
Initialize configuration using the cloud API key

**For the integration using composer**

```
<?php
require 'vendor/autoload.php';

use Vod\VodApi;

VodApi::initConf("your secretId", "your secretKey");
```

**For the integration using source code**
```php
<?php
require './cos-sdk-v5/cos-autoloader.php';
require './qcloudapi-sdk-php/src/QcloudApi/QcloudApi.php';
require './src/Vod/VodApi.php';
require './src/Vod/Conf.php';

use Vod\VodApi;

VodApi::initConf("your secretId", "your secretKey");
```

### Step 2: Call the upload method to start uploading

Method Signature
```
public static function upload(array $src, $parameter = null)
```

Method Parameters
**The src parameter**

| Parameter Name | Description | Type | Required |
| ------------ | ------------ |  ------------ | ------------  |
| videoPath | Video path | String | Yes |
| coverPath | Cover path | String | No |

**The parameter parameter**

| Parameter Name | Description | Type |
| ------------ | ------------ |  ------------ | 
| videoName | Video name | String | 
| sourceContext | User-defined context | String | 
| storageRegion | Specified storage region | String | 
| procedure | Task flow | String | 

Returned values

| Name | Description | Type |
| ------------ | ------------ |  ------------ | 
| code | Status code, 0: Successful, others: Failed | Integer | 
| message | Message | String | 
| data | Returned data | Object |
| data.fileId | Video file ID | String |
| data.video.url | Video Url | String |
| data.cover.url | Cover Url | String |

#### Upload Video
```
$result = VodApi::upload(
    array (
        'videoPath' => '/data/videos/Wildlife.wmv',
    )
);
echo "upload to vod result: " . json_encode($result) . "\n";
```

#### Uploading Videos with Cover Images
```
$result = VodApi::upload(
    array (
        'videoPath' => '/data/videos/Wildlife.wmv',
        'coverPath' => '/data/videos/Wildlife.jpg',
    )
);
echo "upload to vod result: " . json_encode($result) . "\n";
```

#### Uploading Videos and Specifying the Task Flow
```
$result = VodApi::upload(
    array (
        'videoPath' => '/data/videos/Wildlife.wmv',
        'coverPath' => '/data/videos/Wildlife.jpg',
    ),
    array (
        'procedure' => 'QCVB_SimpleProcessFile(1, 1)'
    )
);
echo "upload to vod result: " . json_encode($result) . "\n";
```

#### Uploading Videos to Specified Region
```
$result = VodApi::upload(
    array (
        'videoPath' => '/data/videos/Wildlife.wmv',
        'coverPath' => '/data/videos/Wildlife.jpg',
    ),
    array (
        'storageRegion' => 'tj'
    )
);
echo "upload to vod result: " . json_encode($result) . "\n";
```
## Error Codes

| Error Code | Description |
| ----------- | ----------------- |
| 31001 | Invalid session_key in user request |
| 31002 | The VOD signature in user request already exists |
| 31003 | Uploaded file does not exist |
| 32001 | Service error |

