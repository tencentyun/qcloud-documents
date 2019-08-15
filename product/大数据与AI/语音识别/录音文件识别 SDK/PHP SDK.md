## 接入准备

### SDK 获取

录音文件识别 PHP SDK 以及 Demo 的下载地址：[PHP SDK ](https://sdk-1256085166.cos.ap-shanghai.myqcloud.com/php_record_asr_sdk.tar.gz)。


### 接入须知

开发者在调用前请先查看录音文件识别的[ 接口说明 ](https://cloud.tencent.com/document/product/1093/37139) ，了解接口的**使用要求**和**使用步骤**。

### 开发环境

+ **环境依赖**

此版本 SDK 适用于 PHP 5.4.16 及以上版本。

+ **安装 SDK**

根据下载地址下载源码，将源码中的 * .php 复制到项目中即可使用。

##  快速接入
1. 进入[ API 密钥管理页面 ](https://console.cloud.tencent.com/cam/capi)获取 AppID、SecretId、SecretKey，并将```php_record_asr_sdk/Config.py```中的配置项按需改成自己的值。
2. 参考```php_record_asr_sdk/OfflineClient.php``` 接入 

```
<?php
require ('OfflineSdk.php');

# 1. 先修改好Config.php文件中的配置值。也可以直接在下面修改，比如：
Config :: $ENGINE_MODEL_TYPE = "8k_0";
Config :: $VOICE_FORMAT = 1;

# 2. 然后开始调用：
// 方法1： 指定音频的url（识别服务器会主动去下载），发送请求，推荐使用此方法。
$audio_url = "https://xuhai2-1255824371.cos.ap-chengdu.myqcloud.com/test.wav";
$result = sendUrlRequest("http://yyy.yy.yyy", $audio_url);
echo "\n<br>8K UrlRequest result is: " . $result;

// 方法2：直接上传音频文件，文件大小不能超过5兆。
$filepath = "test_wav/8k/8k.wav";
$result = sendFileRequest("http://xxx.xx.xxx", $filepath);
echo "\n<br>8K FileRequest result is: " . $result;

# ---------------------------------------------------------------------
# 3. 若需中途调整参数值，可直接修改，然后继续发请求即可。例如：
Config :: $ENGINE_MODEL_TYPE = "16k_0";

$filepath = "test_wav/16k/16k.wav";
$result = sendFileRequest("http://xxx.xx.xxx", $filepath);
echo "\n<br>16K FileRequest result is: " . $result;

?>
```
