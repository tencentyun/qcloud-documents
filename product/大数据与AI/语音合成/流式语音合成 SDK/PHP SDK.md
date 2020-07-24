接口请求域名：tts.cloud.tencent.com/stream  

腾讯云语音合成技术（TTS）可以将任意文本转化为语音，实现让机器和应用张口说话。 腾讯 TTS 技术可以应用到很多场景，例如，移动 App 语音播报新闻，智能设备语音提醒，支持车载导航语音合成的个性化语音播报。本接口内测期间免费使用。  

### 开发环境
具体路径为：单击 [腾讯云控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F) 右上角您的账号，选择【访问管理】>【访问密钥】>【API 密钥管理】界面查看 AppID 和 key。
此版本 SDK 适用于 PHP5.4.16 及以上版本。
**下载 SDK**
流式语音合成 PHP SDK [下载地址](https://sdk-1300466766.cos.ap-shanghai.myqcloud.com/tts/php_stream_tts_sdk.zip)。

**安装 SDK**
源码安装。
根据下载地址下载源码，将源码中的 * .php 复制到项目中即可使用。

**卸载 SDK**
卸载方式即删除 * .php 即可。

### <span id="result">获取用户信息</span>
**获取 AppID，SecretId 与 SecretKey**
- 进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi)，获取 AppID、SecretId 与 SecretKey。  
- 具体路径为：单击 [腾讯云控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F) 右上角您的账号，选择【访问管理】>【访问密钥】>【API 密钥管理】界面查看 AppID 和 key。

**更改用户信息配置文件**
将查询到的用户信息更改到 php\_tts\_sdk/Config.php中。

```
#需要配置成用户账号信息
static $SECRET_ID = "AKID********************************";
static $SECRET_KEY = "kKm2*******************************";
static $APPID = 1255*********;
```

### 开发相关
#### 请求参数

| 参数名称 | 必选 | 类型 | 描述 |  
| --- | --- | --- | --- |
| Action |  是 | String | 本接口取值：TextToStreamAudio，不可更改。 |
| AppId  |  是 | Int | 用户在腾讯云注册账号的 AppId，具体可以参考 [获取用户信息](#result)。 |
| SecretId | 是 | String | 用户在腾讯云注册账号 AppId 对应的 SecretId，获取方法同上。 |
| Text | 是 | String | 合成语音的源文本。中文最大支持600个汉字（全角标点符号算一个汉字），英文最大支持1800个字母（半角标点符号算一个字母）。包含空格等字符时需要 URL encode 再传输。|
| SessionId | 是 | String | 一次请求对应一个 SessionId，会原样返回，建议传入类似于 uuid 的字符串防止重复。|
| ModelType | 否 | Int | 模型类型，1：默认模型，此字段只需设置为1即可。|
| Volume | 否 | Float | 音量大小，范围：[0，10]，分别对应11个等级的音量，默认值为0，代表正常音量。没有静音选项。<br>输入除以上整数之外的其他参数不生效，按默认值处理。|
| Speed | 否 | Int | 语速，范围：[-2，2]分别对应不同语速：<br>-2代表0.6倍 <br>-1代表0.8倍<br>0代表1.0倍（默认）<br>1代表1.2倍<br>2代表1.5倍<br>输入除以上整数之外的其他参数不生效，按默认值处理。|
| VoiceType | 否 | Int | 详见：[语音合成 API 文档中的 VoiceType 参数](https://cloud.tencent.com/document/product/1073/37995)。|
| PrimaryLanguage | 否 | Int | 主语言类型：<br>1：中文（默认）<br>2：英文 |
| SampleRate | 否 | Int | 音频采样率：<br>16000:16k（默认）<br>8000:8k |
| Codec | 否 | String | 返回音频格式：pcm：返回二进制 pcm 音频，使用简单，但数据量大。|
| ProjectId | 否 | Int | 项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0。 |
| Timestamp | 是 | Int | 当前 UNIX 时间戳，可记录发起 API 请求的时间。如果与当前时间相差过大，会引起签名过期错误。SDK 会自动赋值当前时间戳。|
| Expired | 是 | Int | 签名的有效期，是一个符合 UNIX Epoch 时间戳规范的数值，单位为秒；Expired 必须大于 Timestamp 且 Expired-Timestamp 小于90天。SDK 默认设置1小时。|

### PHP 快速入门示例
参考 php\_tts\_sdk/TCloudTTS.php

```
<?php
require ('TTSUtil.php');

# 1. 先修改好 Config.php 文件中的配置值。
# 2. TEXT为每次请求的文本，SESSION_ID 建议每次请求修改成唯一 ID，例如 uuid。
Config :: $TEXT = "您好，五一节准备去哪里玩啊";
Config :: $SESSION_ID = guid();
//echo "Session id : " . Config :: $SESSION_ID . "\n";

# 2. 调用获取pcm格式音频
$result = getVoice();
$pcm_file = fopen('./test.pcm', "w");
fwrite($pcm_file, $result);
?>
```




