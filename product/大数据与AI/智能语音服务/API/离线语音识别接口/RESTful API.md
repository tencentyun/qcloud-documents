
## 接口描述
本接口服务对一小时之内的录音文件进行识别，异步返回识别全部结果，支持语音 URL 和本地语音文件两种请求方式。接口是 HTTP RESTful 形式，在使用该接口前，需要在[ 语音识别控制台 ](https://console.cloud.tencent.com/asr)开通服务，并进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi) 新建密钥，生成 AppID、SecretID 和 SecretKey ，用于 API 调用时生成签名，签名将用来进行接口鉴权。

## 输入参数
集成实时语音识别 API 时，需按照以下要求。

| 内容 | 说明 | 
| --- | --- |
| 请求协议 | http |
| 请求地址 | https://aai.qcloud.com/asr/v1/? {请求参数} |
| 接口鉴权 | 签名机制，详见 [签名生成](#sign) |
| 响应格式 | 统一采用 JSON 格式 |
| 开发语言 | 任意，只要可以向腾讯云服务发起 HTTP 请求的均可 |
| 音频属性 | 采样率16k或8k（英文仅支持16k）、位长16bits、单声道 |
| 音频格式 | 支持wav、pcm、mp3、silk、speex、amr等主流音频格式 |
| 数据长度 | 若采用直接上传音频数据方式，建议音频数据不能大于1MB；若采用上传音频 url 方式，本地上传限制大小为5MB。 |
| 语言种类 | 中文普通话、英文和带有一定方言口音的普通话 |

**请求结构**
请求结构主要由**请求方法、请求 URL、请求头部、请求正文**组成。
**请求方法**
HTTPS 请求方法，录音文件识别的请求方法为 **POST**。
**请求 URL**
RESTful 形式的 URL 结构示例如下：

```
https://aai.qcloud.com/asr/v1/<appid>? projectid=xxx&
sub_service_type=xxx& 
engine_model_type=xxx& 
callback_url=xxx& 
channel_num=xxx& 
res_text_format=xxx&
res_type=xxx&  
source_type=xxx&
url=xxx&
secretid=xxx&
timestamp=xxx& 
expired=xxx& 
nonce=xxx
```
URL中各字段含义如下：  

| 参数名称 | 必选 | 类型 | 描述 |  
| --- | --- | --- | --- |
| appid |  是 | Int | 用户在腾讯云注册账号的 AppId，具体可以参考 [ API 密钥管理](https://console.cloud.tencent.com/cam/capi) |
| secretid | 是 | String | 用户在腾讯云注册账号 AppId 对应的 SecretId，获取方法同上 |
| sub\_service\_type | 否 | Int | 子服务类型。0：离线语音识别 |
| engine\_model\_type | 否 | String | 引擎类型。8k\_0：电话 8k 通用模型；16k\_0：16k 通用模型；8k\_6: 电话场景下单声道话者分离模型 |
| res\_text\_format | 否 | Int | 识别结果文本编码方式。0：UTF-8；1：GB2312；2：GBK；3：BIG5|
| res_type | 否 | Int | 结果返回方式。 1：同步返回；0：尾包返回|
| callback_url | 是 | String | 回调 URL，用户接受结果，长度大于 0，小于 2048, 接入方需自行实现回调服务 |
| channel_num | 否 | Int | 语音声道数，仅在电话 8k 通用模型下，支持1和2，其他模型仅支持1 |
| source_type | 是 | Int | 语音数据来源。0：语音 URL；1：语音数据（post body） |
| url | 否 | String | 语音 URL，公网可下载。当 source_type 值为0时须填写该字段，为1时不填；URL 的长度大于 0，小于 2048 |
| timestamp | 是 | Int | 当前 UNIX 时间戳，可记录发起 API 请求的时间。如果与当前时间相差过大，会引起签名过期错误。SDK会自动赋值当前时间戳|
| expired | 是 | Int | 签名的有效期，是一个符合 UNIX Epoch 时间戳规范的数值，单位为秒；Expired 必须大于 Timestamp 且 Expired-Timestamp 小于90天。SDK默认设置1小时|
| nonce | 是 | Int | 随机正整数。用户需自行生成，最长10位 |

**请求头部**
请求头部，包括 Host、Authorization、Content-Type、Content-Length 四个参数。  

| 参数名称 | 必选 | 类型 | 描述 |  
| --- | --- | --- | --- |
| Host |  是 | String | 语音识别服务域名，固定为 aai.qcloud.com |
| Authorization | 是 | String | 用户的有效签名，用于鉴权。对应签名鉴权中得到的签名字符串 |
| Content-Type | 是 | String | application/octet-stream|
| Content-Length | 是 | Int | 请求长度，此处对应语音数据字节数，单位：字节|

**请求正文**
请求正文主要包含音频数据，音频数据不能大于1MB。

## 输入参数
**返回结果**
离线语音识别的 RESTful API 请求返回结果如下表所示：

| 参数名称 | 类型 | 描述 |  
| --- | --- | --- |
| code |  Int | 服务器错误码，0 为成功 |
| message |  String | 服务器返回的信息 |
| requestId |  Int | 如果成功，返回任务 ID |

## 请求示例
请求示例如下，示例生成请参考下面 PHP 代码。

```
curl -sv -H 'Authorization:UyKZ+Q4xMbdu3gxOmPD7tgnAm1A=' 'https://aai.qcloud.com/asr/v1/YOUR_APPID?callback_url=http://aai.qcloud.com/cb&channel_num=1&engine_model_type=1&expired=1560842782&nonce=199546&projectid=0&res_text_format=0&res_type=1&secretid=YOUR_SECRET_ID&source_type=0&sub_service_type=0&timestamp=1560839182&url=http://aai.qcloud.com/test.mp3' -d ''
```
说明：其中YOUR\_APPID和YOUR\_SECRET\_ID对应的是AppID、SecretID。
<span id="sign"></span>
**签名生成**
这里以 Appid = 200001, SecretId = AKIDUfLUEUigQiXqm7CVSspKJnuaiIKtxqAv为例拼接签名原文，则拼接的签名原文为：

```
POSTaai.qcloud.com/asr/v1/2000001?callback_url=http://test.qq.com/rec_callback&engine_model_type=1&expired=1473752807&nonce=44925&projectid=0&res_text_format=0&res_type=1&secretid=AKIDUfLUEUigQiXqm7CVSspKJnuaiIKtxqAv&source_type=0&sub_service_type=0&timestamp=1473752207&url=http://test.qq.com/voice_url 
```
对签名原文和SecretKey= bLcPnl88WU30VY57ipRhSePfPdOfSruK,使用**HmacSha1**算法进行加密处理：

```
签名串=Base64Encode(HmacSha1(签名原文,SecretKey))
```
最终得到签名串为：

```
UyKZ+Q4xMbdu3gxOmPD7tgnAm1A=
```

**返回示例**
返回消息示例如下：

```
 { "code":0, "message":"success", "requestId":500 }
```
## 结果回调
当语音识别系统完成识别后，会将结果通过 HTTP POST 请求的形式通知到用户，用户需要在自身业务服务器上搭建服务接收回调。
**服务端返回结果**
语音识别系统通过回调接口形式将识别结果回调通知客户，接口 Body 各字段说明如下：

| 字段 | 类型 | 描述 |  
| --- | --- | --- |
| code |  Int | 服务器错误码，0 为成功，其他：失败 |
| message |  String | 成功或者失败原因文字描述 |
| requestId |  Int | 请求 ID，与后台任务 ID 一一对应 |
| appid |  Int | 腾讯云应用 ID |
| projectid |  Int | 腾讯云项目 ID |
| audioUrl |  String | 语音下载 ur。如果语音源非公网可下载 URL，则不包含该字段 |
| text |  String | 识别出的结果文本 |
| audioTime |  Double | 语音总时长 |

>!为了防止某些字段中，出现诸如 “&” 等特殊字符，导致解包失败，所有字段的 value 值都将进行 url\_encode 之后发送给用户业务服务器，在获取 value 之后，需要先对 value 进行 url\_decode 以获取原始 value 值。


**客户端确认返回**
用户业务服务器在接收到语音识别系统发起的 HTTP POST 回调请求后，需要按照如下约定，返回结果：

| 参数名称 | 类型 | 描述 |  
| --- | --- | --- |
| code |  Int | 错误码，0 为成功，其他值代表失败 |
| message |  String | 失败原因说明，比如业务服务器过载。 如果业务服务器返回失败，会间隔一段时间重新通知 |

**回调示例**
服务端返回 json 示例： 

``` 
{ "code":0, "message":"success", "requestId":500, "appid": 12000001, "projectid": 0, "audioUrl":"http://test.qq.com/voice_url", "text":"你好", audioTime:2.5 }
```
语音识别系统发起请求，收到请求后，用户侧需要以 json 格式回以响应：

```
{ "code" : 0, "message" : "成功" }
```

## 请求错误码

|数值	|返回码 |	说明|
| --- | --- | --- |
|1000	|ERROR\_BAD\_REQ	|请求的参数不符合要求|
|1001	|ERROR\_PARSE\_DATA\_FAILED	|解析请求参数时失败|
|1002	|ERROR\_HAS\_NO\_VALID\_PROJECTID	|没有提供 projectid，或者值不合法|
|1003	|ERROR\_HAS\_NO\_VALID\_RES\_TEXT\_FORMAT |没有提供 res\_text\_format，或者值不合法|
|1004	|ERROR\_HAS\_NO\_VALID\_SUB\_SERVICE\_TYPE |没有提供 sub\_service\_type，或者值不合法|
|1005	|ERROR\_HAS\_NO\_VALID\_ENGINE\_MODEL\_TYPE|没有提供 engine\_model\_type，或者值不合法|
|1006	|ERROR\_HAS\_NO\_VALID\_CALLBACK\_URL	|没有提供 callback\_url，或者值不合法|
|1007	|ERROR\_HAS\_NO\_VALID\_RES\_TYPE	|没有提供 res\_type，或者值不合法|
|1008	|ERROR\_HAS\_NO\_VALID\_SOURCE\_TYPE	|没有提供 source\_type，或者值不合法|
|1009	|ERROR\_HAS\_NO\_VALID\_URL	|没有提供下载语音的 url，或者值不合法|
|1010	|ERROR\_HAS\_NO\_VALID\_SECRET\_ID	|没有提供 SecretId，或者值不合法|
|1011	|ERROR\_HAS\_NO\_VALID\_TIMESTAMP	|没有提供 timestamp，或者值不合法|
|1012	|ERROR\_HAS\_NO\_VALID\_EXPIRED	|没有提供 expired，或者值不合法|
|1013	|ERROR\_HAS\_NO\_VALID\_NONCE	|没有提供 nonce，或者值不合法|
|1014	|ERROR\_HAS\_NO\_VALID\_TEMPLATENAME	|提供的 template\_name 不合法|
|1015	|ERROR\_HAS\_NO\_BUCKET	|没有提供 bucket，或者值不合法|
|1016	|ERROR\_HAS\_NO\_AMOUNT	|没有剩余的免费用量|
|1017	|ERROR\_URL\_TOO\_LONG	|提供的 url 长度大于 2048|
|1018	|ERROR\_FILEID\_TOO\_LONG	|提供的文件名长度大于 2048|
|1019	|ERROR\_APPID\_NOT\_REGISTER	|提供的 APPID 未注册|
|1020	|ERROR\_APPID\_PROJECTID\_TEMPLATENAME\_MISMATCH	|提供的 APPID，ProjectId 与 template\_name 不匹配|
|1021	|ERROR\_PROCESS\_FAILED	|服务端处理出现内部错误|
|1022	|ERROR\_PROXY\_BAD\_AUTH	|签名不符合规则|
|1024	|ERROR\_PROXY\_AUTH\_TOO\_LONG\_EXPIRED	|签名的有效期设置太长|
|1025	|ERROR\_PROXY\_AUTH\_EXPIRED	|签名过期|
|1026	|ERROR\_PROXY\_AUTH\_PROJECTID\_NOEXIST	|签名中的 ProjectId 错误|
|1027	|ERROR\_PROXY\_AUTH\_SECRETID\_NOEXIST	|签名中的 SecretId 错误|
|1028	|ERROR\_PROXY\_AUTH\_PROJECTID\_MISMATCH	|签名中的 ProjectId 不匹配|
|1029	|ERROR\_PROXY\_AUTH\_REPLAY\_ATTACK	|重放攻击|
|1030	|ERROR\_PROXY\_AUTH\_FAILED	|签名验证不通过|
|1032	|ERROR\_AUDIO\_TOO\_LARGE	|发送的语音数据过大（大于 5M）|
|1034	|ERROR\_UNKNOWN	|其他未知错误|

## 回调错误码
| 数值 |  说明 |  
| --- | --- |
| 10000 | 语音非标准格式，转码失败 |
| 10001 | 识别不成功 |
| 10002 | 语音时长过长 |
| 10003 | 语音时长过长 |
| 10004 | 无效的语音文件 |
| 10005 | 其他失败 |
| 10006 | 音轨个数不匹配 |




