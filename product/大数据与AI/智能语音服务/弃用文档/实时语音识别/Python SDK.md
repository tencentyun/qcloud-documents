
实时语音识别 Python SDK [下载地址](https://main.qcloudimg.com/raw/bfbb586ae3cb8e9ff9b13570d9409df3/python_realtime_asr_sdk_v1.0.tar.gz )。

## 功能简介
语音识别（ASR）可以把音频数据转换为文本，需要持续对音频进行识别的场景，推荐使用实时语音识别，例如视频录制时候的实时字幕，语音对话机器人等。   

- 语言和方言：语音识别服务目前主语言仅支持中文普通话，可以识别有一定方言口音的普通话，支持在普通话中掺杂少量英文字母和单词。  
- 采样率和位深度：支持16bit、8k或者16k采样率的单声道或双声道的中文音频识别。
- 我们建议每300或者500毫秒发送一次音频，对此，客户端需要做一些必要的缓存逻辑。
- VAD（Voice Activity Detection）指对语音进行分段的技术，是算法通过对语音之间的停顿进行检测，判断用户说话间的分句。
- voice_id 用于识别单次对话请求。如果用户持续说话一段时间，包含了很多句话，可以采用一个 voice_id 发送一系列的语音数据，seq 字段表示序号，从0开始。voice_id 不能重复，重复会导致识别错误。

例如，用户说：“今天天气好。”，大概2到3秒的时间。假设1秒发3个请求，则共计会发送8个左右的请求。服务器会返回相应个回包。类似于：
```
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":0,"text":"今"}
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":1,"text":"今天"}
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":2,"text":"今天"}
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":3,"text":"今天天气"}
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":4,"text":"今天天气好"}
{"code":0,"message":"成功","voice_id":"3b53e9b909b55929","seq":5,"text":"今天天气好。"}
```

## 开发环境
**基本编译环境**
安装 Python 2.7版本
**requests**
安装方法：pip install requests  。
或先下载，然后进入目录执行：```Python setup.py install```。
下载 [requests 文件](https://2.python-requests.org//zh_CN/latest/user/install.html#install)。


## <span id="result">获取用户信息</span>
**获取用户鉴权信息及申请使用**
- 使用本接口之前需要先 [注册](https://cloud.tencent.com/register) 腾讯云账号，获得 AppID，SecretID 及 SecretKey。 并在 [语音识别](https://cloud.tencent.com/product/asr) 页面单击【立即使用】。
- 进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi)，获取 AppID、SecretId 与 SecretKey。 
- 具体路径为：单击 [腾讯云控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F) 右上角您的账号，选择【访问管理】>【访问密钥】>【API 密钥管理】界面查看 AppID 和 key。

**配置用户信息**
**将 AppID、SecretId、SecretKey 配置到 SDK 中。**

```
#需要配置成用户账号信息 Python_realtime_asr_sdk/Config.py
SECRET_KEY = 'kFpw*****************************'
SECRETID = 'AKID*******************************'
APPID = '1259********'
```


## 开发相关
**请求参数**

| 参数名称 | 必选 | 类型 | 描述 |  
| --- | --- | --- | --- |
| appid |  是 | Int | 用户在腾讯云注册账号的 AppId，具体可以参考 [获取用户信息](#result)。 |
| secretid | 是 | String | 用户在腾讯云注册账号 AppId 对应的 SecretId，获取方法同上。 |
| sub\_service\_type | 否 | Int | 子服务类型。1：实时流式识别。|
| engine\_model\_type | 否 | String | 引擎类型引擎模型类型。8k_0:8k 通用，16k_0:16k 通用，16k_en：16k英文。|
| result\_text\_format | 否 | Int | 识别结果文本编码方式。0：UTF-8；1：GB2312；2：GBK；3：BIG5|
| res_type | 否 | Int | 结果返回方式。1：同步返回；0：尾包返回。|
| voice_format | 否 | Int | 语音编码方式，可选，默认值为 4。1：wav（pcm）；4：speex（sp）；6：silk；8：mp3（仅16k_0模型支持）。|
| needvad | 否 | Int | 0为后台不做 vad 分段，1为后台做自动 vad 分段。 |
| seq | 是 | Int | 	语音分片的序号从0开始。|
| end | 是 | Int | 是否为最后一片，最后一片语音片为1，其余为0。 |
| source | 是 | Int | 设置为0。 |
| voice_id | 是 | String | 16 位 String 串作为每个音频的唯一标识，用户自己生成。|
| timestamp | 是 | Int | 当前 UNIX 时间戳，可记录发起 API 请求的时间。如果与当前时间相差过大，会引起签名过期错误。SDK会自动赋值当前时间戳。|
| expired | 是 | Int | 签名的有效期，是一个符合 UNIX Epoch 时间戳规范的数值，单位为秒；Expired 必须大于 Timestamp 且 Expired-Timestamp 小于90天。SDK 默认设置1小时。|
| timeout | 是 | Int | 设置超时时间单位为毫秒。|
| nonce | 是 | Int | 随机正整数。用户需自行生成，最长10位。|

**返回参数**

| 参数名称 |  描述 |  
| --- | --- |
| code |  0：正常，其他，发生错误。 |
| message | 如果是0就是 success，不是0就是错误的原因信息。 |
| voice_id | 表示这通音频的标记，同一个音频流这个标记一样。 |
| seq | 语音分片的信号。<br> 如果请求参数 needvad 为0的话，表示不需要后台做 vad，这里的 seq 就是发送过来的 seq 的序号。<br>如果请求参数 needvad 为1，则表示需要后台做 vad，因后台做 vad ，vad 会重新分片，送入识别的 seq 会和发送过来的 seq 不一样，这里返回的 seq 就为0 。|
| text |  如果请求参数 needvad 为0的，表示不需要后台做 vad，text 的值是分片的识别结果。<br>如果请求参数 needvad 为1的话，表示需要后台做 vad，因为后台做 vad 的话，vad 会重新分片，送入识别的 seq 会和发送过来的 seq 不一样，text 为"" 。|
| result_number | 请求参数needvad=1， 此字段有效<br>result_number 表示后面的 result_list 里面有几段结果，如果是0表示没有结果，可能是遇到中间是静音了。<br>如果是1表示 result\_list 有一个结果， 在发给服务器分片很大的情况下可能会出现多个结果，正常情况下都是1个结果。 |
| result_list | 请求参数needvad=1， 此字段有效 <br>slice\_type: 返回分片类型标记， 0表示一小段话开始，1表示在小段话的进行中，2表示小段话的结束<br>index 表示第几段话<br>start\_time  当前分片所在小段的开始时间（相对整个音频流）。<br>end\_time 当前分片在整个音频流中的结束时间。<br>voice\_text_str 识别结果。 |
| final | 0 表示还在整个音频流的中间部分。<br>1 表示是整个音频流的最后一个包。<br>例如在电信电话场景中，是否是客户端发送的最后一个包的识别结果。 |

**请求 url 参数示例**

```
http://asr.cloud.tencent.com/asr/v1/125000001?
end=0&
engine_model_type=16k_0&
expired=1558016577&
nonce=434303218&
res_type=0&
result_text_format=0&
secretid=XXXXXXXXXXXXXXXXXXXXXXX&
needvad=1&
seq=0&
source=0&
sub_service_type=1&
timeout=5000&
timestamp=1558010577&
voice_format=1&
voice_id=82510017d7deb33e
```
其中v1表示 API 的版本，v1.0，后面125000001是 AppID，各个参数的说明参考上表。
**请求 demo**
```
Python RasrClient.py
```

## Python 快速入门示例
参考 Python\_realtime\_asr\_sdk/RasrClient.py

```
# -*- coding:utf-8 -*-
# 引用 SDK
import RASRsdk
import OS
import Config

# ----------------------------- 调用方法1 -----------------------------
# 音频文件路径
filepath = "../../test_wavs/8k.wav"
# 调用语音识别函数获得识别结果, 参数2标识是否打印中间结果到控制台
result = RASRsdk.sendVoice(filepath, True)
print("Final result: " + result)

# ---------------------------------------------------------------------
```






