>?此接口为 API 2.0 版本，在参数风格、错误码等方面有区别于 API 3.0 版本，请知悉。

## 接口描述
本接口服务采用 websocket 协议，对实时音频流进行识别，同步返回识别结果，达到“边说边出文字”的效果。
在使用该接口前，需要在语音识别控制台开通服务，并进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi) 新建密钥，生成 AppID、SecretID 和 SecretKey，用于 API 调用时生成签名，签名将用来进行接口鉴权。

## 接口要求
集成实时语音识别 API 时，需按照以下要求。

| 内容 | 说明 |
|---------|---------|
| 语言种类 | 中文普通话、英文、粤语、韩语、日语、泰语、上海话方言。可通过接口参数 engine_model_type 设置对应引擎类型。若有四川话、南京话、南昌话需求，可填写 [表单](https://cloud.tencent.com/apply/p/75h8nunsh9) 申请|
| 支持行业 | 通用、金融、游戏、教育、医疗 |
| 音频属性 | 采样率：16000Hz或8000Hz<br>采样精度：16bits<br>声道：单声道（mono） |
| 音频格式 | pcm、wav、opus、speex、silk、mp3、m4a、aac |
| 请求协议 | wss 协议 |
| 请求地址 | wss://asr.cloud.tencent.com/asr/v2/&lt;appid&gt;?{请求参数} |
| 接口鉴权 | 签名鉴权机制，详见 [签名生成](#sign) |
| 响应格式 | 统一采用 JSON 格式 |
| 数据发送 | 建议每40ms发送40ms时长（即1:1实时率）的数据包，对应8k采样率为640字节，16k采样率为1280字节。<br>音频发送速率过快超过1:1实时率或者音频数据包之间发送间隔超过6秒，可能导致引擎出错，后台将返回错误并主动断开连接。 |
| 并发限制 | 默认单账号限制并发连接数为20路，如您有提高并发限制的需求，[请提工单](https://console.cloud.tencent.com/workorder/category) 进行咨询。 |

## 接口调用流程
接口调用流程分为两个阶段：握手阶段和识别阶段。两阶段后台均返回 text message，内容为 json 序列化字符串，以下是格式说明：

| 字段名 | 类型 | 描述 |
|---------|---------|---------|
| code | Integer | 状态码，0代表正常，非0值表示发生错误。 |
| message | String | 错误说明，发生错误时显示这个错误发生的具体原因，随着业务发展或体验优化，此文本可能会经常保持变更或更新。 |
| voice_id | String | 音频流唯一 id，由客户端在握手阶段生成并赋值在调用参数中。 |
| message_id | String | 本 message 唯一 id。 |
| result | Result | 最新语音识别结果。 |
| final | Integer | 该字段返回1时表示音频流全部识别结束。 |

其中识别结果 Result 结构体格式为：

| 字段名 | 类型 | 描述 |
|---------|---------|---------|
| slice_type | Integer | 该识别结果类型，0表示一句话开始，1表示一句话进行中，2表示一句话结束。<br>根据一句话时间长度以及后台处理情况，一句话识别过程中后台可能返回的 message 序列为：<br>0-1-2：1表示一个或者多个结果类型为1的 message。<br>0-2:后台仅返回一句话开始与结束两个 message。<br>2:后台仅返回一句话完整结果的 message。 |
| index | Integer | 当前一句话结果在整个音频流中的序号，从0开始逐句递增。 |
| start_time | Integer | 当前一句话结果在整个音频流中的起始时间。 |
| end_time | Integer | 当前一句话结果在整个音频流中的结束时间。 |
| voice_text_str | String | 当前一句话文本结果，编码为 UTF8。 |
| word_size | Integer | 当前一句话的词结果个数。 |
| word_list | Word Array | 当前一句话的词列表，Word 结构体格式为：<br>word：String 类型，该词的内容；<br>start_time：Integer 类型，该词在整个音频流中的起始时间；<br>end_time：Integer 类型，该词在整个音频流中的结束时间；<br>stable_flag：Integer 类型，该词的稳态结果，0表示该词在后续识别中可能发生变化，1表示该词在后续识别过程中不会变化。 |

### 握手阶段
#### 请求格式
握手阶段，客户端主动发起 websocket 连接请求，请求 URL 格式为：
```
wss://asr.cloud.tencent.com/asr/v2/<appid>?{请求参数}
```
其中&lt;appid&gt;需替换为腾讯云注册账号的 AppID，可通过 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi) 获取，{请求参数}格式为
```
key1=value2&key2=value2...(key 和 value 都需要进行 urlencode)
```

参数说明：

| 参数名称 | 必填 | 类型 | 描述 |
|---------|---------|---------|---------|
| secretid | 是 | String | 腾讯云注册账号的密钥 SecretId，可通过 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi) 获取。 |
| timestamp | 是 | Integer | 当前 UNIX 时间戳，单位为秒。如果与当前时间相差过大，会引起签名过期错误。 |
| expired | 是 | Integer | 签名的有效期截止时间 UNIX 时间戳，单位为秒。expired 必须大于 timestamp 且 expired - timestamp 小于90天。 |
| nonce | 是 | Integer | 随机正整数。用户需自行生成，最长10位。 |
| engine_model_type | 是 | String | 引擎模型类型。<br>电话场景：<br>• 8k_en：电话 8k 英语；<br>• 8k_zh：电话 8k 中文普通话通用；<br>• 8k_zh_finance：电话 8k 金融领域模型；<br>非电话场景：<br>• 16k_zh：16k 中文普通话通用；<br>• 16k_en：16k 英语；<br>• 16k_ca：16k 粤语；<br>• 16k_ko：16k 韩语；<br>• 16k_zh-TW：16k 中文普通话繁体；<br>• 16k_ja：16k 日语；<br>• 16k_wuu-SH：16k 上海话方言；<br>• 16k_zh_medical 医疗；<br>• 16k_en_game 英文游戏；<br>• 16k_zh_court 法庭；<br>• 16k_en_edu 英文教育；<br>• 16k_zh_edu 中文教育；<br>• 16k_th 泰语。 |
| voice_id | 是 | String | 16位 String 串作为每个音频的唯一标识，用户自己生成。 |
| voice_format | 否 | Integer | 语音编码方式，可选，默认值为4。1：pcm；4：speex(sp)；6：silk；8：mp3；12：wav；14：m4a（每个分片须是一个完整的 m4a 音频）；16：aac。 |
| needvad | 否 | Integer | 0：关闭 vad，1：开启 vad。<br>如果语音分片长度超过60秒，用户需开启 vad。 |
| hotword_id | 否 | String | 热词 id。用于调用对应的热词表，如果在调用语音识别服务时，不进行单独的热词 id 设置，自动生效默认热词；如果进行了单独的热词 id 设置，那么将生效单独设置的热词 id。 |
| customization_id | 否 | String | 自学习模型 id。用于调用对应的自学习模型，如果在调用语音识别服务时，不进行单独的自学习模型 id 设置，自动生效默认自学习模型；如果进行了单独的自学习模型 id 设置，那么将生效单独设置的自学习模型 id。|
| filter_dirty | 否 | Integer | 是否过滤脏词（目前支持中文普通话引擎）。默认为0。0：不过滤脏词；1：过滤脏词；2：将脏词替换为 * 。 |
| filter_modal | 否 | Integer | 是否过语气词（目前支持中文普通话引擎）。默认为0。0：不过滤语气词；1：部分过滤；2：严格过滤 。 |
| filter_punc | 否 | Integer | 是否过滤句末的句号（目前支持中文普通话引擎）。默认为0。0：不过滤句末的句号；1：过滤句末的句号。 |
| convert_num_mode | 否 | Integer | 是否进行阿拉伯数字智能转换（目前支持中文普通话引擎）。0：不转换，直接输出中文数字，1：根据场景智能转换为阿拉伯数字，3: 打开数学相关数字转换。默认值为1。 |
| word_info | 否 | Int | 是否显示词级别时间戳。0：不显示；1：显示，不包含标点时间戳，2：显示，包含标点时间戳。支持引擎 8k_en、8k_zh、8k_zh_finance、16k_zh、16k_en、16k_ca、16k_zh-TW、16k_ja、16k_wuu-SH，默认为0。|
| vad_silence_time | 否 | Integer | 语音断句检测阈值，静音时长超过该阈值会被认为断句（多用在智能客服场景，需配合 needvad = 1 使用），取值范围：240-2000，单位 ms，此参数建议不要随意调整，可能会影响识别效果，目前仅支持 8k_zh、8k_zh_finance、16k_zh 引擎模型。 |
| signature | 是 | String | 接口签名参数。 |

[](id:sign)
**signature 签名生成**
1. 对除 signature 之外的所有参数按字典序进行排序，拼接请求 URL 作为签名原文，这里以 Appid=1259228442, SecretId=AKIDoQq1zhZMN8dv0psmvud6OUKuGPO7pu0r 为例拼接签名原文，则拼接的签名原文为：
```
asr.cloud.tencent.com/asr/v2/1259228442?engine_model_type=16k_zh&expired=1592380492&filter_dirty=1&filter_modal=1&filter_punc=1&needvad=1&nonce=1592294092123&secretid=AKIDoQq1zhZMN8dv0psmvud6OUKuGPO7pu0r&timestamp=1592294092&voice_format=1&voice_id=RnKu9FODFHK5FPpsrN
```
2. 对签名原文使用 SecretKey 进行 HmacSha1 加密，之后再进行 base64 编码。例如对上一步的签名原文， SecretKey=kFpwoX5RYQ2SkqpeHgqmSzHK7h3A2fni，使用 HmacSha1 算法进行加密并做 base64 编码处理：
```
Base64Encode(HmacSha1("asr.cloud.tencent.com/asr/v2/1259228442?engine_model_type=16k_zh&expired=1592380492&filter_dirty=1&filter_modal=1&filter_punc=1&needvad=1&nonce=1592294092123&secretid=AKIDoQq1zhZMN8dv0psmvud6OUKuGPO7pu0r&timestamp=1592294092&voice_format=1&voice_id=RnKu9FODFHK5FPpsrN", "kFpwoX5RYQ2SkqpeHgqmSzHK7h3A2fni"))
```
得到 signature 签名值为：
```
HepdTRX6u155qIPKNKC+3U0j1N0=
```
3. 将 signature 值进行 **urlencode（必须进行 URL 编码，否则将导致鉴权失败偶现** ）后拼接得到最终请求 URL 为：
```
wss://asr.cloud.tencent.com/asr/v2/1259228442?engine_model_type=16k_zh&expired=1592380492&filter_dirty=1&filter_modal=1&filter_punc=1&needvad=1&nonce=1592294092123&secretid=AKIDoQq1zhZMN8dv0psmvud6OUKuGPO7pu0r&timestamp=1592294092&voice_format=1&voice_id=RnKu9FODFHK5FPpsrN&signature=HepdTRX6u155qIPKNKC%2B3U0j1N0%3D
```

#### 请求响应
客户端发起连接请求后，后台建立连接进并进行签名校验，校验成功则返回 code 值为0的确认消息表示握手成功；如果校验失败，后台返回 code 为非0值的消息并断开连接。
```
 {"code": 0, "message": "sucess"}
```


### 识别阶段
握手成功之后，进入识别阶段，客户端上传语音数据并接收识别结果消息。

#### 上传数据
在识别过程中，客户端持续上传 binary message 到后台，内容为音频流二进制数据。建议每40ms发送40ms时长（即1:1实时率）的数据包，对应8k采样率为640字节，16k采样率为1280字节。音频发送速率过快超过1:1实时率或者音频数据包之间发送间隔超过6秒，可能导致引擎出错，后台将返回错误并主动断开连接。
音频流上传完成之后，客户端需发送以下内容的 text message，通知后台结束识别。
```
{"type": "end"}
```

#### 接收消息
客户端上传数据的过程中，需要同步接收后台返回的实时识别结果，结果示例：
```
 {"code":0,"message":"success","voice_id":"RnKu9FODFHK5FPpsrN","message_id":"RnKu9FODFHK5FPpsrN_11_0","result":{"slice_type":0,"index":0,"start_time":0,"end_time":1240,"voice_text_str":"实时","word_size":0,"word_list":[]}}
```

```
{"code":0,"message":"success","voice_id":"RnKu9FODFHK5FPpsrN","message_id":"RnKu9FODFHK5FPpsrN_33_0","result":{"slice_type":2,"index":0,"start_time":0,"end_time":2840,"voice_text_str":"实时语音识别","word_size":0,"word_list":[]}}
```
后台识别完所有上传的语音数据之后，最终返回 final 值为1的消息并断开连接。
```
{"code":0,"message":"success","voice_id":"CzhjnqBkv8lk5pRUxhpX","message_id":"CzhjnqBkv8lk5pRUxhpX_241","final":1}
```
识别过程中如果出现错误，后台返回 code 为非0值的消息并断开连接。
```
{"code":4008,"message":"后台识别服务器音频分片等待超时","voice_id":"CzhjnqBkv8lk5pRUxhpX","message_id":"CzhjnqBkv8lk5pRUxhpX_241"}
```

## 开发者资源
### SDK
- [Tencent Cloud Speech SDK for Go](https://github.com/TencentCloud/tencentcloud-speech-sdk-go)
- [Tencent Cloud Speech SDK for Java](https://github.com/TencentCloud/tencentcloud-speech-sdk-java)
- [Tencent Cloud Speech SDK for C++](https://github.com/TencentCloud/tencentcloud-speech-sdk-cpp)
- [Tencent Cloud Speech SDK for Python](https://github.com/TencentCloud/tencentcloud-speech-sdk-python)
- [Tencent Cloud Speech SDK for JS](https://github.com/TencentCloud/tencentcloud-speech-sdk-js)

### SDK 调用示例
- [Golang 示例](https://github.com/TencentCloud/tencentcloud-speech-sdk-go/blob/master/examples/asrexample/asrexample.go) 
- [Java 示例](https://github.com/TencentCloud/tencentcloud-speech-sdk-java-example/blob/main/src/main/java/com/tencentcloud/asr/SpeechRecognitionWebsocketExample.java) 
- [C++ 示例](https://github.com/TencentCloud/tencentcloud-speech-sdk-cpp/blob/master/examples/asr_example.cpp) 
- [Python 示例](https://github.com/TencentCloud/tencentcloud-speech-sdk-python/blob/master/examples/asr/asrexample.py) 
- [JS 示例](https://github.com/TencentCloud/tencentcloud-speech-sdk-js/tree/main/examples)

## 错误码

| 数值 | 说明 |
|---------|---------|
| 4001 | 参数不合法，具体详情参考 message |
| 4002 | 鉴权失败 |
| 4003 | AppID 服务未开通，请在控制台开通服务 |
| 4004 | 无可使用的免费额度 |
| 4005 | 账户欠费停止服务，请及时充值 |
| 4006 | 账号当前调用并发超限 |
| 4007 | 音频解码失败，请检查上传音频数据格式与调用参数一致 |
| 4008 | 客户端数据上传超时 |
| 4009 | 客户端连接断开 |
| 4010 | 客户端上传未知文本消息 |
| 5000 | 后台错误，请重试 |
| 5001 | 后台识别服务器识别失败，请重试 |
| 5002 | 后台识别服务器识别失败，请重试 |
