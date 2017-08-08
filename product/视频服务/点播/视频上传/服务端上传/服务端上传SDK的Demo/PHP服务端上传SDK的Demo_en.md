## Overview

VOD provides a PHP-based Demo which is based on COS PHP SDK and Cloud API SDK. Users can refer to this demo to upload videos and cover image files stored in their servers directly into Tencent Cloud VOD system.

## Download Links

* [VOD PHP DEMO](https://github.com/tencentyun/vod-php-sdk-based-demo)
* [COS PHP SDK](https://www.qcloud.com/document/product/436/6274)
* [Cloud API PHP SDK](https://www.qcloud.com/document/developer-resource/494/7243)

## How to Use

1. Download and decompress VOD PHP DEMO. Switch your working directory to where upload_demo.php is located.
2. Decompress cos-php-sdk-v4-master.zip and place the files to the working directory.
3. Decompress qcloudapi-sdk-php-master.zip and place the files to the working directory.
4. Edit cos-php-sdk-v4-master/qcloudcos/conf.php, configure **APP_ID** as **"10022853"**, configure SECRET_ID and SECRET_KEY as the "secret id" and "secret key" in API secret key.
5. Edit cos-php-sdk-v4-master/qcloudcos/cosapi.php, modify the value of **EXPIRED_SECONDS** into **24 * 3600**. This helps avoid the problem where the upload process does not restart automatically if an error occurred while uploading large files.
6. Execute php upload_demo.php to initiate file upload process. You will acquire file playback address and fileid once the process is successfully completed.
