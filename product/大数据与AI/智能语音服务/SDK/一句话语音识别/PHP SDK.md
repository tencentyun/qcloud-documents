## 开发准备
### 相关环境
[一句话语音识别 PHP SDK下载地址 >>](https://main.qcloudimg.com/raw/7136827917db8f858af47f097dff76c7/SASRsdk.php)

### 环境依赖
此版本 SDK 适用于 PHP5.4.16 及以上版本。
### 安装 SDK
源码安装。
根据下载地址下载源码。将源码中的 SASRsdk.php 复制到项目中即可使用。
### 卸载 SDK
卸载方式即删除 RASRsdk.php 即可。
## 快速入门
```
//引用sdk文件
require('SASRsdk.php');
//用户需要修改为自己腾讯云官网账号中的appid，secretid与secret_key
$secretKey = 'kKm26uXCgLtGRWVJvKtGU0LYdWCgOvGP';
$SecretId = 'AKID31NbfXbpBLJ4kGJrytc9UfgVAlGltJJ8';
// 识别引擎 8k or 16k
$EngSerViceType = '16k';
// 语音数据来源 0:语音url，1:语音数据bodydata
$SourceType = 1;
// 语音数据地址
$URI = 'D:\\0601_ori\\180601_1011.mp3-enc.wav';
//$URI='http://liqiansunvoice-1255628450.cosgz.myqcloud.com/30s.wav';
// 音频格式 mp3 or wav
$VoiceFormat = 'wav';
//调用SASRsdk中的sendvoice函数获得识别结果
sendvoice($secretKey, $SecretId, $EngSerViceType, $SourceType, $URI, $VoiceFormat);
```
