Tencent Cloud VOD provides PHP SDK for the scenario of uploading videos from server. For more information about upload process, please see [Upload Videos from Server](/document/product/266/9759).

## Integration Method

### Using Composer
```json
{
    "require": {
        "qcloud/vod-sdk-v5": "v1.2.1"
    }
}
```

### Importing Using Source File
If the composer tool is not used for dependency management in the project, you can directly download the source code and import it into the project:

* [Access from Github >>](https://github.com/tencentyun/vod-php-sdk-v5)
* [Click to download PHP SDK >>](https://github.com/tencentyun/vod-php-sdk-v5/archive/master.zip)

Copy the source code in the src file as well as cos-sdk-v5 and qcloudapi-sdk-php in the file test/non-composer to the project directory of the same level

## Simple Upload of Video
### Initializing Upload Object
Initialize VodApi using the Cloud API key
**When you import the video using composer**
```
<?php
require 'vendor/autoload.php';

use Vod\VodApi;

VodApi::initConf("your secretId", "your secretKey");
```

**When you import the video using source code**
```php
<?php
require './cos-sdk-v5/cos-autoloader.php';
require './qcloudapi-sdk-php/src/QcloudApi/QcloudApi.php';
require './src/Vod/VodApi.php';
require './src/Vod/Conf.php';

use Vod\VodApi;

VodApi::initConf("your secretId", "your secretKey");
```

### Calling Upload
Pass video address to start uploading
```
$result = VodApi::upload(
    array (
        'videoPath' => '/data/videos/Wildlife.wmv',
    )
);
echo "upload to vod result: " . json_encode($result) . "\n";
```

## Advanced Features
### Uploading Cover
Pass both video address and cover address
```
$result = VodApi::upload(
    array (
        'videoPath' => '/data/videos/Wildlife.wmv',
        'coverPath' => '/data/videos/Wildlife.jpg',
    )
);
echo "upload to vod result: " . json_encode($result) . "\n";
```

### Specifying Task Flow
Pass the task flow parameter. For more information, please see [Overview of Task Flow](/document/product/266/11700). The task flow will be processed automatically after the video is uploaded.
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

### Specifying Upload Region
Pass a specified region ID to upload a video to the specified region. For more information, please see [Upload Videos from Server](/document/product/266/9759).
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

## API Description
Initialize upload object `VodApi::initConf(secretId, secretKey)`

| Parameter Name | Description | Type | Required |
| --------- | ---------------------- | ------- | ---- |
| secretId | Cloud API Key ID | String | Yes |
| secretKey | Cloud API Key | String | Yes |

Upload method `VodApi.upload(src, parameter)`

**src**

| Parameter Name | Description | Type | Required |
| ------------ | ------------ |  ------------ | ------------  |
| videoPath | Video path | String | Yes |
| coverPath | Cover path | String | No |

**parameter**

| Parameter Name | Description | Type | Required |
| ------------ | ------------ |  ------------ |   ------------  |
| videoName | Video name | String | No |
| sourceContext | User-defined context | String | No |
| storageRegion | Specified storage region | String | No |
| procedure | Task flow | String | No |

Upload Result 

| Member Variable Name | Description | Type |
| -------- | --------- | ------ |
| code | Result code | Int | 
| message | Message | String | 
| data | Returned data | Object |
| data.fileId | VOD file ID | String |
| data.video.url | Address where the video is stored | String |
| data.cover.url | Address where the cover is stored | String |

## Error Codes
After calling SDK to upload a video, you can check the video upload status with the code in the result.

| Status Code | Description |
| ----------- | ----------------- |
| 0 | Uploaded successfully |
| 31001 | Invalid session_key in user request |
| 31002 | The VOD signature in user request already exists |
| 31003 | The file to be uploaded does not exist |
| 32001 | Service error |

