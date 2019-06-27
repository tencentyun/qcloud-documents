
## 功能简介
- 离线语音识别适用于多种标准语音格式的长段语音文件，通常应用于对识别结果返回时延要求不高的场景。目前支持的采样率为 8K 和 16K，仅支持中文。可以应用于客服语音记录质检、UGC 音频审核、会议语音记录转写和医生就诊录音转写等场景。 
- 语言和方言：语音识别服务目前主语言仅支持中文普通话，可以识别有一定方言口音的普通话，支持在普通话中掺杂少量英文字母和单词。   
- 音频格式支持：支持16bit、8k或者16k采样率的单声道或双声道的中文音频识别；支持音频格式为 wav、pcm、mp3、silk、speex、amr。 
- 音频数据长度支持：若采用直接上传音频数据方式，则音频数据不能大于5M，若采用上传 url 方式，则音频时长不能大于1小时。
  
>! 如超出当天免费策略上限，您可以提交工单 [联系我们](https://cloud.tencent.com/about/connect) 处理。
　　

## 开发环境
**环境依赖**
此版本 SDK 适用于 PHP5.4.16 及以上版本。
**下载 SDK**
录音文件识别 PHP SDK [下载地址 ](https://main.qcloudimg.com/raw/f6f94691d81e947b3bb4fbe3cd317d54/php_record_asr_sdk_v1.0.tar.gz )。
**安装 SDK**
源码安装。
根据下载地址下载源码，将源码中的 * .php 复制到项目中即可使用。
**卸载 SDK**
卸载方式即删除 * .php 即可。

## <span id="result">获取用户信息</span>
**获取用户鉴权信息及申请使用**
- 使用本接口之前需要先 [注册](https://cloud.tencent.com/register) 腾讯云账号，获得 AppID，SecretID 及 SecretKey。 并在 [语音识别](https://cloud.tencent.com/product/asr) 页面单击【立即使用】。
- 进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi)，获取 AppID、SecretId 与 SecretKey。  
- 具体路径为：单击 [腾讯云控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F) 右上角您的账号，选择【访问管理】>【访问密钥】>【API 密钥管理】界面查看 AppID 和 key。

**配置用户信息**
**将 AppID、SecretId、SecretKey 配置到 SDK 中**。

将查询到的用户信息更改到 ```php\_record\_asr\_sdk/Config.php```中。

```
#需要配置成用户账号信息
static $SECRET_ID = "AKID********************************";
static $SECRET_KEY = "kKm2*******************************";
static $APPID = 1255*********;
```

## 开发相关
**参数说明 **
**请求参数**

| 参数名称 | 必选 | 类型 | 描述 |  
| --- | --- | --- | --- |
| appid |  是 | Int | 用户在腾讯云注册账号的 AppId，具体可以参考 [获取用户信息](#result)。 |
| secretid | 是 | String | 用户在腾讯云注册账号 AppId 对应的 SecretId，获取方法同上。 |
| sub\_service\_type | 否 | Int | 子服务类型。0：离线语音识别。|
| engine\_model\_type | 否 | String | 引擎类型。8k_0：电话 8k 通用模型；16k_0：16k 通用模型；8k_6: 电话场景下单声道话者分离模型。 |
| res\_text\_format | 否 | Int | 识别结果文本编码方式。0：UTF-8；1：GB2312；2：GBK；3：BIG5。|
| res_type | 否 | Int | 结果返回方式。0：同步返回；1：异步返回。目前只支持异步返回。|
| callback_url | 是 | String | 回调 URL，用户接受结果，长度大于0，小于2048。 |
| channel_num | 否 | Int | 语音声道数，仅在电话 8k 通用模型下，支持1和2，其他模型仅支持1。 |
| source_type | 是 | Int | 语音数据来源。0：语音 URL；1：语音数据（post body）。 |
| url | 否 | String | 语音 URL，公网可下载。当 source_type 值为0时须填写该字段，为1时不填；URL 的长度大于0，小于 2048 。|
| timestamp | 是 | Int | 当前 UNIX 时间戳，可记录发起 API 请求的时间。如果与当前时间相差过大，会引起签名过期错误。SDK 会自动赋值当前时间戳。|
| expired | 是 | Int | 签名的有效期，是一个符合 UNIX Epoch 时间戳规范的数值，单位为秒；Expired 必须大于 Timestamp 且 Expired-Timestamp 小于90天。SDK默认设置1小时。|
| nonce | 是 | Int | 随机正整数。用户需自行生成，最长10位。|

**请求 url 参数示例**
```
https://aai.qcloud.com/asr/v1/125000001?engine_model_type=0
&expired=1473752807
&nonce=44925
&projectid=0
&res_text_format=0
&res_type=1
&secretid=<secretid>
&source_type=0
&sub_service_type=0
&timestamp=1473752207
&url=<url>
&callback_url=<callback_url>
```
```
headers:
{
"Content-Type":"application/octet-stream",
"Authorization":"UyKZ+Q4xMbdu3gxOmPD7tgnAm1A="
}
```
其中v1表示 API 的版本，v1.0，后面125000001是 AppID，各个参数的说明参考上表。
**返回参数**
离线语音识别的 RESTful API 请求返回结果如下表所示：

| 参数名称 | 类型 | 描述 |  
| --- | --- | --- |
| code |  Int | 服务器错误码，0为成功 |
| message |  String | 服务器返回的信息 |
| requestId |  Int | 如果成功，返回任务 ID |

## PHP 快速入门示例
参考 PHP\_record\_asr\_sdk/OfflineClient.php

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
# 3. 若需中途调整参数值，可直接修改，然后继续发请求即可。比如：
Config :: $ENGINE_MODEL_TYPE = "16k_0";

$filepath = "test_wav/16k/16k.wav";
$result = sendFileRequest("http://xxx.xx.xxx", $filepath);
echo "\n<br>16K FileRequest result is: " . $result;

?>
```





