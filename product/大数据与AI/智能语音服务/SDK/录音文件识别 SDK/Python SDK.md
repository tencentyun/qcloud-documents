
录音文件识别 Python SDK [下载地址](https://main.qcloudimg.com/raw/e0d0d05c182b3aad00c801980e946d2a/python_record_asr_sdk_v1.0.tar.gz)。

## 功能简介
- 离线语音识别适用于多种标准语音格式的长段语音文件，通常应用于对识别结果返回时延要求不高的场景。目前支持的采样率为 8K 和 16K，仅支持中文。可以应用于客服语音记录质检、UGC 音频审核、会议语音记录转写和医生就诊录音转写等场景。 
- 语言和方言：语音识别服务目前主语言仅支持中文普通话，可以识别有一定方言口音的普通话，支持在普通话中掺杂少量英文字母和单词。   
- 音频格式支持：支持16bit、8k或者16k采样率的单声道或双声道的中文音频识别；支持音频格式为 wav、pcm、mp3、silk、speex、amr。 
- 音频数据长度支持：若采用直接上传音频数据方式，则音频数据不能大于5M，若采用上传 url 方式，则音频时长不能大于1小时。
  
>!如超出当天免费策略上限，您可以提交工单 [联系我们](https://cloud.tencent.com/about/connect) 处理。
　　

## 开发环境
**基本编译环境**
Python 2.7版本
**requests**
```
安装方法：pip install requests  
或者先下载，然后进入目录执行：python setup.py install
下载链接：https://2.python-requests.org//zh_CN/latest/user/install.html#install
```

## <span id="result">获取用户信息</span>
**获取用户鉴权信息及申请使用**
- 使用本接口之前需要先 [注册](https://cloud.tencent.com/register) 腾讯云账号，获得 AppID，SecretID 及 SecretKey。 并在 [语音识别](https://cloud.tencent.com/product/asr) 页面单击【立即使用】。
- 进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi)，获取 AppID、SecretId 与 SecretKey。
- 具体路径为：单击 [腾讯云控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F) 右上角您的账号，选择【访问管理】>【访问密钥】>【API 密钥管理】界面查看 AppID 和 key。

**配置用户信息**
**将 AppID、SecretId、SecretKey配置到 SDK 中**.

```
#需要配置成用户账号信息 python_record_asr_sdk/Config.py
SECRET_KEY = 'kFpw*****************************'
SECRETID = 'AKID*******************************'
APPID = '1259********'
```


## 开发相关
**参数说明**
**请求参数**

| 参数名称 | 必选 | 类型 | 描述 |  
| --- | --- | --- | --- |
| appid |  是 | Int | 用户在腾讯云注册账号的 AppId，具体可以参考 [获取用户信息](#result)。 |
| secretid | 是 | String | 用户在腾讯云注册账号AppId对应的SecretId，获取方法同上。 |
| sub\_service\_type | 否 | Int | 子服务类型。0：离线语音识别。|
| engine\_model\_type | 否 | String | 引擎类型。8k_0：电话 8k 通用模型；16k_0：16k 通用模型；8k_6：电话场景下单声道话者分离模型。 |
| res\_text\_format | 否 | Int | 识别结果文本编码方式。0：UTF-8；1：GB2312；2：GBK；3：BIG5。|
| res_type | 否 | Int | 结果返回方式。0：同步返回；1：异步返回。目前只支持异步返回。|
| callback_url | 是 | String | 回调 URL，用户接受结果，长度大于0，小于2048 。|
| channel_num | 否 | Int | 语音声道数，仅在电话8k通用模型下，支持1和2，其他模型仅支持1。 |
| source_type | 是 | Int | 语音数据来源。0：语音 URL；1：语音数据（post body） |
| url | 否 | String | 语音 URL，公网可下载。当 source_type 值为 0 时须填写该字段，为 1 时不填；URL 的长度大于0，小于2048。 |
| timestamp | 是 | Int | 当前 UNIX 时间戳，可记录发起 API 请求的时间。如果与当前时间相差过大，会引起签名过期错误。SDK会自动赋值当前时间戳。|
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

**请求 demo**
```
	Python OfflineClient.py
```
## Python 快速入门示例
参考 python_record_asr_sdk/OfflineClient.py

```
# 若需中途调整参数值，可直接修改，然后继续发请求即可。比如：
Config.config.CALLBACK_URL = ""
Config.config.ENGINE_MODEL_TYPE = "16k_0"
# ......
audio_url = "https://xuhai2-1255824371.cos.ap-chengdu.myqcloud.com/test.wav"
result = offlineSdk.task_process(audio_url)
print (result)
```





