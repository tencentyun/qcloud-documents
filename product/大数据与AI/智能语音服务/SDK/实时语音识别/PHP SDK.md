## 开发准备
### 相关环境
[实时识别 PHP SDK下载地址 >>](https://main.qcloudimg.com/raw/ef9e3dca0fdbe3f4eefd070e98a5bd5c/RASRsdk.php)

### 环境依赖
此版本 SDK 适用于 PHP5.4.16 及以上版本。
### 安装 SDK
源码安装。
根据下载地址下载源码，将源码中的 RASRsdk.php 复制到项目中即可使用。
### 卸载 SDK
卸载方式即删除 RASRsdk.php 即可。

## 快速入门
```
//引用 SDK 文件
require('RASRsdk.php');
//用户需要修改为自己腾讯云官网账号中的 APPID，SecretId 与 SecretKey
$secret_key = 'kKm26uXCgLtGRWVJvKtGU0LYdWCgOvGP';
$secretid = 'AKID31NbfXbpBLJ4kGJrytc9UfgVAlGltJJ8';
$appid = '1255628450';
//识别引擎 8k_0 or 16k_0
$engine_model_type = '8k_0';
//结果返回方式 0：同步返回 or 1：尾包返回
$res_type = 0;
// 识别结果文本编码方式 0:UTF-8,1:GB2312,2:GBK,3:BIG5
$result_text_format = 0;
// 语音编码方式 1:wav 4:sp 6:silk
$voice_format = 1;
$filepath="D:\\test20180903.wav";
// 语音切片长度 cutlength<200000
$cutlength = 6400;
//调用 RASRsdk 中的 sendvoice 函数获得识别结果
sendvoice($secret_key, $secretid, $appid, $engine_model_type, $res_type, $result_text_format, $voice_format, $filepath, $cutlength);
```
