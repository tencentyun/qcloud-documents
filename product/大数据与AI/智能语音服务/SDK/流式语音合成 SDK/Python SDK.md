
流式语音合成 Python SDK [下载地址](https://main.qcloudimg.com/raw/e173ae2ae9381046430cf2b5105a33d6/python_stream_tts_sdk_v1.0.tar.gz )。


接口请求域名：aai.cloud.tencent.com/tts  

腾讯云语音合成技术（TTS）可以将任意文本转化为语音，实现让机器和应用张口说话。 腾讯 TTS 技术可以应用到很多场景，例如，移动 App 语音播报新闻；智能设备语音提醒；支持车载导航语音合成的个性化语音播报。本接口内测期间免费使用。  

## 开发环境
**基本编译环境**
python 2.7版本
**requests**
安装方法：`pip install requests`  或先下载，然后进入目录执行：`python setup.py install`
下载 [requests 链接](https://2.python-requests.org//zh_CN/latest/user/install.html#install)。

##  <span id="result">获取用户信息</span>
**获取 AppID，SecretId 与 SecretKey**
- 进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi)，获取 AppID、SecretId 与 SecretKey。
-  具体路径为：单击 [腾讯云控制台](https://cloud.tencent.com/login?s_url=https%3A%2F%2Fconsole.cloud.tencent.com%2F) 右上角您的账号，选择【访问管理】>【访问密钥】>【API 密钥管理】界面查看 AppID 和 key。

**更改用户信息配置文件**
将查询到的用户信息更改到 conf/tcloud_auth.ini 配置文件中。

```
#需要配置成用户账号信息
[authorization]
AppId=1259***************
SecretId=AKID****************************
SecretKey=kFpwo**************************
```

## 开发相关
**请求参数** 

| 参数名称 | 必选 | 类型 | 描述 |  
| --- | --- | --- | --- |
| Action |  是 | String | 本接口取值：TextToStreamAudio，不可更改。 |
| AppId  |  是 | Int | 用户在腾讯云注册账号的 AppId，具体可以参考 [获取用户信息](#result)。 |
| SecretId | 是 | String | 用户在腾讯云注册账号 AppId 对应的 SecretId，获取方法同上。 |
| Text | 是 | String | 合成语音的源文本，最大支持800字符。|
| SessionId | 是 | String | 一次请求对应一个 SessionId，会原样返回，建议传入类似于 uuid 的字符串防止重复。|
| ModelType | 否 | Int | 模型类型，1：默认模型，此字段只需设置为1即可。|
| Volume | 否 | Float | 音量大小，范围：[0，10]，分别对应11个等级的音量，默认值为0，代表正常音量。没有静音选项。<br>输入除以上整数之外的其他参数不生效，按默认值处理。|
| Speed | 否 | Int | 语速，范围：[-2，2]分别对应不同语速：<br>-2代表0.6倍 <br>-1代表0.8倍<br>0代表1.0倍（默认）<br>1代表1.2倍<br>2代表1.5倍<br>输入除以上整数之外的其他参数不生效，按默认值处理。|
| VoiceType | 否 | Int | 音色选择：<br>0：亲和女声（默认）<br>1：亲和男声<br>2：成熟男声<br>3：活力男声<br>4：温暖女声<br>5：情感女声<br>6：情感男声|
| PrimaryLanguage | 否 | Int | 主语言类型：<br>1：中文（默认）<br>2：英文 |
| SampleRate | 否 | Int | 音频采样率：<br>16000:16k（默认）<br>8000:8k |
| Codec | 否 | String | 返回音频格式：<br>opus：返回多段含 opus 压缩分片音频，数据量小，建议使用（默认）。<br>pcm：返回二进制 pcm 音频，使用简单，但数据量大。|
| ProjectId | 否 | Int | 项目ID，可以根据控制台-账号中心-项目管理中的配置填写，如无配置请填写默认项目ID:0 。|
| Timestamp | 是 | Int | 当前 UNIX 时间戳，可记录发起 API 请求的时间。如果与当前时间相差过大，会引起签名过期错误。SDK 会自动赋值当前时间戳。|
| Expired | 是 | Int | 签名的有效期，是一个符合 UNIX Epoch 时间戳规范的数值，单位为秒；Expired 必须大于 Timestamp 且 Expired-Timestamp 小于90天。SDK默认设置1小时。|

**具体参数配置可以参考：conf/request_parameter.ini 的默认配置**

**请求demo**
```
python tcloud_tts.py
```
## Python 快速入门例子
参考 python_tts_sdk/tcloud_tts.py

```
def task_process():
    req = request()
    req.init()
    auth = authorization()
    auth.init()

    #request_data = collections.OrderedDict()
    request_data = dict()
    request_data['Action'] = req.Action
    request_data['AppId'] = auth.AppId
    request_data['Codec'] = req.Codec
    request_data['Expired'] = int(time.time()) + auth.Expired
    request_data['ModelType'] = req.ModelType
    request_data['PrimaryLanguage'] = req.PrimaryLanguage
    request_data['ProjectId'] = req.ProjectId
    request_data['SampleRate'] = req.SampleRate
    request_data['SecretId'] = auth.SecretId
    request_data['SessionId'] = req.SessionId
    request_data['Speed'] = req.Speed
    request_data['Text'] = req.Text
    request_data['Timestamp'] = int(time.time())
    request_data['VoiceType'] = req.VoiceType
    request_data['Volume'] = req.Volume

    signature = auth.generate_sign(request_data = request_data)
    header = {
        "Content-Type": "application/json",
        "Authorization": str(signature)
    }
    url = "https://aai.cloud.tencent.com/tts"

    r = requests.post(url, headers=header, data=json.dumps(request_data), stream = True)
    '''
    if str(r.content).find("Error") != -1 :
        print(r.content)
        return
    '''
    i = 1
    wavfile = wave.open('test.wav', 'wb')
    wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
    for chunk in r.iter_content(1000):
        if (i == 1) & (str(chunk).find("Error") != -1) :
            print(chunk)
            return 
        i = i + 1
        wavfile.writeframes(chunk)
        
    wavfile.close()
```




