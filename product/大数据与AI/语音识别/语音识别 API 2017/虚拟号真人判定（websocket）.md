> !此接口为 API 2.0 版本，在参数风格、错误码等方面有区别于 API 3.0 版本，请知悉。


## 接口描述

本接口服务采用 websocket 协议，对实时音频流进行识别，能够过滤虚拟号平台转接语音，并在毫秒级快速识别真人用户接听状态并返回结果，帮助客户判断对话机器人的启动时机。

在使用该接口前，需要 [开通语音识别业务](https://cloud.tencent.com/document/product/1093/54362)，并进入 [API 密钥获取](https://console.cloud.tencent.com/cam/capi) 新建密钥，生成 AppID、SecretID 和 SecretKey，用于 API 调用时生成签名，签名将用来进行接口鉴权。

该接口属于ASR+系列产品，为独立接口，请前往 [计费概述](https://cloud.tencent.com/document/product/1093/35686) 了解此接口计费规则。

## 接口要求

集成虚拟号真人判定 API 时，需按照以下要求。

<table>
<tr>
<th rowspan="1" colSpan="1" >内容</td>
<th rowspan="1" colSpan="1" >说明</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >适用地区</td>
<td rowspan="1" colSpan="1" >仅支持中国大陆地区</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >支持行业</td>
<td rowspan="1" colSpan="1" >智能外呼等电话通信行业</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >音频属性</td>
<td rowspan="1" colSpan="1" >采样率：8000Hz<br>采样精度：16bits<br>声道：单声道（mono）</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >音频格式</td>
<td rowspan="1" colSpan="1" >pcm、wav、opus、speex、silk、mp3、m4a、aac</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >请求协议</td>
<td rowspan="1" colSpan="1" >wss 协议</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >请求地址</td>
<td rowspan="1" colSpan="1" >wss://asr.cloud.tencent.com/asr/virtual_number/v1/<appid>?{请求参数}</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >接口鉴权</td>
<td rowspan="1" colSpan="1" >签名鉴权机制，详见 <a href="#signature">签名生成 </a></td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >响应格式</td>
<td rowspan="1" colSpan="1" >统一采用 JSON 格式</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >数据发送</td>
<td rowspan="1" colSpan="1" >建议每40ms 发送40ms 时长（即1:1实时率）的数据包，对应 pcm 大小为：8k 采样率640字节<br>音频发送速率过快超过1:1实时率或者音频数据包之间发送间隔超过6秒，可能导致引擎出错，后台将返回错误并主动断开连接</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >并发限制</td>
<td rowspan="1" colSpan="1" >默认单账号限制并发数为200路</td>
</tr>
</table>


## 接口调用流程

接口调用流程分为两个阶段：握手阶段和识别阶段。两阶段后台均返回 text message，内容为 json 序列化字符串，以下是格式说明：

<table>
<tr>
<th rowspan="1" colSpan="1" >字段名</td>
<th rowspan="1" colSpan="1" >类型</td>
<th rowspan="1" colSpan="1" >描述</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >code</td>
<td rowspan="1" colSpan="1" >Integer</td>
<td rowspan="1" colSpan="1" >状态码，0代表正常，非0值表示发生错误</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >message</td>
<td rowspan="1" colSpan="1" >String</td>
<td rowspan="1" colSpan="1" >错误说明，发生错误时显示这个错误发生的具体原因，随着业务发展或体验优化，此文本可能会经常保持变更或更新</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >voice_id</td>
<td rowspan="1" colSpan="1" >String</td>
<td rowspan="1" colSpan="1" >音频流唯一 id，由客户端在握手阶段生成并赋值在调用参数中</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >message_id</td>
<td rowspan="1" colSpan="1" >String</td>
<td rowspan="1" colSpan="1" >本 message 唯一 id</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >result</td>
<td rowspan="1" colSpan="1" >Integer</td>
<td rowspan="1" colSpan="1" >接听识别结果。  0:真人用户尚未接听 1:真人用户已接听</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >final</td>
<td rowspan="1" colSpan="1" >Integer</td>
<td rowspan="1" colSpan="1" >该字段返回1时表示音频流全部识别结束</td>
</tr>
</table>


## 握手阶段

### 请求格式

握手阶段，客户端主动发起 websocket 连接请求，请求 URL 格式为：
```plaintext
wss://asr.cloud.tencent.com/asr/virtual_number/v1/<appid>?{请求参数}
```
其中`<appid>`需替换为腾讯云注册账号的 AppID，可通过 [API 密钥管理平台](https://console.cloud.tencent.com/cam/capi) 获取，{请求参数}格式为
```plaintext
key1=value2&key2=value2...(key 和 value 都需要进行 urlencode)
```

### 参数说明

<table>
<tr>
<th rowspan="1" colSpan="1" >参数名称</td>
<th rowspan="1" colSpan="1" >必填</td>
<th rowspan="1" colSpan="1" >类型</td>
<th rowspan="1" colSpan="1" >描述</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >secretid</td>
<td rowspan="1" colSpan="1" >是</td>
<td rowspan="1" colSpan="1" >String</td>
<td rowspan="1" colSpan="1" >腾讯云注册账号的密钥 SecretId，可通过 <a href="https://console.cloud.tencent.com/cam/capi">API 密钥管理平台</a> 获取</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >timestamp</td>
<td rowspan="1" colSpan="1" >是</td>
<td rowspan="1" colSpan="1" >Integer</td>
<td rowspan="1" colSpan="1" >当前 UNIX 时间戳，单位为秒。如果与当前时间相差过大，会引起签名过期错误</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >expired</td>
<td rowspan="1" colSpan="1" >是</td>
<td rowspan="1" colSpan="1" >Integer</td>
<td rowspan="1" colSpan="1" >签名的有效期截止时间 UNIX 时间戳，单位为秒。expired 必须大于 timestamp 且 expired - timestamp 小于90天</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >nonce</td>
<td rowspan="1" colSpan="1" >是</td>
<td rowspan="1" colSpan="1" >Integer</td>
<td rowspan="1" colSpan="1" >随机正整数。用户需自行生成，最长10位</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >voice_id</td>
<td rowspan="1" colSpan="1" >是</td>
<td rowspan="1" colSpan="1" >String</td>
<td rowspan="1" colSpan="1" >音频流识别全局唯一标识，一个 websocket 连接对应一个，用户自己生成（推荐使用 uuid），最长128位。</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >voice_format</td>
<td rowspan="1" colSpan="1" >否</td>
<td rowspan="1" colSpan="1" >Integer<br></td>
<td rowspan="1" colSpan="1" >语音编码方式，可选，默认值为4。1：pcm；4：speex(sp)；6：silk；8：mp3；10：opus；12：wav；14：m4a（每个分片须是一个完整的 m4a 音频）；16：aac</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >signature</td>
<td rowspan="1" colSpan="1" >是</td>
<td rowspan="1" colSpan="1" >String</td>
<td rowspan="1" colSpan="1" >接口签名参数</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >wait_time</td>
<td rowspan="1" colSpan="1" >否</td>
<td rowspan="1" colSpan="1" >Integer</td>
<td rowspan="1" colSpan="1" >接通等待时长，默认为30秒，最长60秒，识别超过等待时长返回未接通。</td>
</tr>
</table>



[](id:signature)
### signature 签名生成

1. 对除 signature 之外的所有参数按字典序进行排序，拼接请求 URL 作为签名原文，这里以 Appid=125922***，SecretId=*****Qq1zhZMN8dv0****** 为例拼接签名原文，则拼接的签名原文为：
``` plaintext
asr.cloud.tencent.com/asr/virtual_number/v1/125922***?expired=1673494772&needvad=1&nonce=1673408372&secretid=*****Qq1zhZMN8dv0******&timestamp=1673408372&voice_format=1&voice_id=c64385ee-3e5c-4fc5-bbfd-7c71addb35b0
```
2. 对签名原文使用 SecretKey 进行 HmacSha1 加密，之后再进行 base64 编码。例如对上一步的签名原文， SecretKey=*****SkqpeHgqmSz*****，使用 HmacSha1 算法进行加密并做 base64 编码处理：
``` plaintext
Base64Encode(HmacSha1("asr.cloud.tencent.com/asr/virtual_number/v1/125922***?expired=1673494772&needvad=1&nonce=1673408372&secretid=*****Qq1zhZMN8dv0******&timestamp=1673408372&voice_format=1&voice_id=c64385ee-3e5c-4fc5-bbfd-7c71addb35b0", "*****SkqpeHgqmSz*****"))
```
   得到 signature 签名值为：
``` plaintext
G8jDQBRg1JfeBi/YnTjyjekxfDA=
```
3. 将 signature 值进行 urlencode（必须进行 URL 编码，否则将导致鉴权失败偶现 ）后拼接得到最终请求 URL 为：
``` plaintext
wss://asr.cloud.tencent.com/asr/virtual_number/v1/1259228442?expired=1592380492&filter_dirty=1&filter_modal=1&filter_punc=1&needvad=1&nonce=1592294092123&secretid=AKIDoQq1zhZMN8dv0psmvud6OUKuGPO7pu0r&timestamp=1592294092&voice_format=1&voice_id=RnKu9FODFHK5FPpsrN&signature=HepdTRX6u155qIPKNKC%2B3U0j1N0%3D
```

### Opus 音频流封装说明

压缩 FrameSize 固定640，即一次压缩640 short，否则解压会失败。传到服务端可以是多帧的拼接组合，每一帧需满足下面格式。

每一帧压缩数据封装如下：

<table>
<tr>
<th rowspan="1" colSpan="1" >OpusHead（4字节）</td>
<th rowspan="1" colSpan="1" >帧数据长度（2字节）</td>
<th rowspan="1" colSpan="1" >Opus 一帧压缩数据</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >opus</td>
<td rowspan="1" colSpan="1" >长度 len</td>
<td rowspan="1" colSpan="1" >对应 len 长的 opus decode data</td>
</tr>
</table>


### 请求响应

客户端发起连接请求后，后台建立连接进并进行签名校验，校验成功则返回 code 值为0的确认消息表示握手成功；如果校验失败，后台返回 code 为非0值的消息并断开连接。

``` plaintext
{"code":0,"message":"success","voice_id":"RnKu9FODFHK5FPpsrN"}
```

## 识别阶段

握手成功之后，进入识别阶段，客户端上传语音数据并接收识别结果消息。

### 上传数据

在识别过程中，客户端持续上传 binary message 到后台，内容为音频流二进制数据。建议每40ms 发送40ms 时长（即1:1实时率）的数据包，对应 pcm 大小为：8k 采样率640字节。音频发送速率过快超过1:1实时率或者音频数据包之间发送间隔超过6秒，可能导致引擎出错，后台将返回错误并主动断开连接。

音频流上传完成之后，客户端需发送以下内容的 text message，通知后台结束识别。

``` plaintext
{"type": "end"}
```

### 接收消息

客户端上传数据的过程中，需要同步接收后台返回的实时识别结果，如果返回识别结果，则表示已经识别完成，客户端无需再继续给后台发送消息，结果示例：
``` plaintext
{"code":0,"message":"success","voice_id":"CzhjnqBkv8lk5pRUxhpX","message_id":"CzhjnqBkv8lk5pRUxhpX_241","final": "1", "result": 1}
```
识别过程中如果出现错误，后台返回 code 为非0值的消息并断开连接。
``` plaintext
{"code":4008,"message":"后台识别服务器音频分片等待超时","voice_id":"CzhjnqBkv8lk5pRUxhpX","message_id":"CzhjnqBkv8lk5pRUxhpX_241"}
```

## 错误码

<table>
<tr>
<th rowspan="1" colSpan="1" >数值</td>
<th rowspan="1" colSpan="1" >说明</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >4001</td>
<td rowspan="1" colSpan="1" >参数不合法，具体详情参考 message</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >4002</td>
<td rowspan="1" colSpan="1" >鉴权失败</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >4003</td>
<td rowspan="1" colSpan="1" >AppID 服务未开通，请在控制台开通服务</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >4004</td>
<td rowspan="1" colSpan="1" >无可使用的免费额度</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >4005</td>
<td rowspan="1" colSpan="1" >账户欠费停止服务，请及时充值</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >4006</td>
<td rowspan="1" colSpan="1" >账号当前调用并发超限</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >4007</td>
<td rowspan="1" colSpan="1" >音频解码失败，请检查上传音频数据格式与调用参数一致</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >4008</td>
<td rowspan="1" colSpan="1" >客户端数据上传超时</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >4009</td>
<td rowspan="1" colSpan="1" >客户端连接断开</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >4010</td>
<td rowspan="1" colSpan="1" >客户端上传未知文本消息</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >5000</td>
<td rowspan="1" colSpan="1" >后台错误，请重试</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >5001</td>
<td rowspan="1" colSpan="1" >后台识别服务器识别失败，请重试</td>
</tr>
<tr>
<td rowspan="1" colSpan="1" >5002</td>
<td rowspan="1" colSpan="1" >后台识别服务器识别失败，请重试</td>
</tr>
</table>


## 开发者资源

### SDK

- [GitHub - TencentCloud/tencentcloud-speech-sdk-go](https://github.com/TencentCloud/tencentcloud-speech-sdk-go)
- [GitHub - TencentCloud/tencentcloud-speech-sdk-java](https://github.com/TencentCloud/tencentcloud-speech-sdk-java)



