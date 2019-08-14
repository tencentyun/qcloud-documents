## 1. 接入准备
### 1.1 SDK 获取
实时语音识别 PHP SDK 以及 Demo 的下载地址：[PHP SDK](https://sdk-1256085166.cos.ap-shanghai.myqcloud.com/php_realtime_asr_sdk.tar.gz)。

### 1.2 接入须知
开发者在调用前请先查看实时语音识别的[ 接口说明 ](https://cloud.tencent.com/document/product/1093/37138) ，了解接口的**使用要求**和**使用步骤**。


### 1.3 开发环境
+ **环境依赖**
该 SDK 适用于 PHP 5.4.16 及以上版本。
+ **安装 SDK**
根据下载地址下载源码，将源码中的 * .php 复制到项目中即可使用。

## 2. 快速接入
1. 进入[ API 密钥管理页面 ](https://console.cloud.tencent.com/cam/capi)获取 AppID、SecretId、SecretKey 并将```php_realtime_asr_sdk/Config.py```中的配置项按需改成自己的值。
2. 参考```php_realtime_asr_sdk/RasrClient.php``` 接入 ：

```
<?php
require ('RASRsdk.php');
# 1. 先修改好 Config.php 文件中的配置
# 2. 然后开始调用：
//调用 RASRsdk 中的 sendvoice 函数获得识别结果
$filepath = "test_wav/8k/8k.wav";
$result = sendvoice($filepath, false);
echo "<br>8K Result is: ".$result;


# ---------------------------------------------------------------------
# 3. 若需中途调整参数值，可直接修改，然后继续发请求即可。例如：
Config::$ENGINE_MODEL_TYPE = "16k_0";

$filepath = "test_wav/16k/16k.wav";
$result = sendvoice($filepath, false);
echo "<br>16K Result is: ".$result;

?>
```
