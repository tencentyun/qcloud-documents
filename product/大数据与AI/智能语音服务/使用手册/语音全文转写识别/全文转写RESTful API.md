## 请求结构

### RESTful API请求结构

语音全文转写识别的 RESTful API 请求结构如下：

| 参数名称    | 必选   | 类型   | 描述    | 
| ------------- | ---------- | ------------- | ---------- |
| Version | 是         | String          | HTTPS 协议版本         | 
| URL  | 是         | String          | HTTPS 请求地址       | 
| Https Headers    | 是         | 数据集合          | HTTPS 请求头部         | 
| Https Method   |是         | String     | HTTPS 请求方法，语音全文转写识别请求方法为 POST
| Https Body   | 是         | String          | HTTPS 请求正文，即语音数据（当 source_type 字段为1时填充），大小不超过5M        | 

其中，URL 的结构为 ：
```
https://aai.qcloud.com/asr/v1/appid?
projectid=xxx&
template_name=xxx&
sub_service_type=x&
engine_model_type=x&
callback_url=xxx&
res_text_format=x&
res_type=x&
source_type=x&
url=xxx&
secretid=xxx&
timestamp=xxx&
expired=xxx&
nonce=xxx
```

URL 中各字段含义如下（各字段的值需要进行 URL 编码）：

| 字段           | 必选         | 类型          | 描述         | 
| ------------- | ---------- | ------------- | ---------- |
| appid | 是 | uint  | 腾讯云应用 ID 值   | 
| projectid  | 否   | uint | 腾讯云项目 ID，不填为默认项目，即0，总长度不超过1024字节 | 
| template_name   | 否 | String  | 模板名称，模板是服务类型参数的组合。template_name和（sub_service_type，engine_model_type，callback_url，res_text_format，res_type）两者必须填一个，建议选择模板；如果两者都提供，则以template_name为准   | 
| sub_service_type  | 否   | uint   | 子服务类型。0：全文转写。目前只支持全文转写  | 
| engine_model_type | 否  | uint  | 引擎类型。0：8k 婚恋模型；1：16k 通用模型；2：16k 通用短语音模型；3：8k 话者分离（source_type 字段为 1 时填充）| 
| callback_url | 否  | String  | 回调 URL，用户接受结果，长度大于0，小于2048 |
| res_text_format | 否 | uint  | 识别结果文本编码方式。0：UTF-8；1：GB2312； 2：GBK； 3：BIG5 |
| res_type | 否 | uint  | 结果返回方式。0：同步返回；1：异步返回。目前只支持异步返回 |
| source_type | 是 | uint  |  语音数据来源。0：语音 URL；1：语音数据（post body）|
| url | 否   | String  | 语音URL，公网可下载。当 source_type 值为0时填写该字段，为1时不填；URL 的长度大于0，小于2048 |
| secretid  | 是 | String | 官网 SecretId |
| timestamp | 是 | uint | 当前时间戳，是一个符合 UNIX Epoch 时间戳规范的数值，单位为秒 | 
| expired |  是 | uint | 签名的有效期，是一个符合 UNIX Epoch 时间戳规范的数值，单位为秒；expired 必须大于 timestamp 且 expired - timestamp 小于90天 |
| nonce | 是 | uint | 随机正整数。用户需自行生成，最长10位 |

HTTPS  Headers 的结构如下：

| 参数名称 | 必选  | 类型 | 描述  | 
| -------- | ------ | ------- | ------ |
| Host   | 是  | String | 语音识别服务域名，固定为 aai.qcloud.com | 
| Authorization  | 是   | String  | 用户的有效签名，用于鉴权。对应签名鉴权中得到的签名字符串 | 
| Content-Type   | 是 | String | application/octet-stream   | 
| Content-Length  | 是  | Int  | 请求长度，此处对应语音数据字节数，单位：字节  | 

### 请求示例

下列示例中，<箭头括号>表示必须替换为有效值的变量。当语音数据来源 source_type=1 时，采用直接 POST 语音数据，请求 Host 与路径：
```
http://aai.qcloud.com/asr/v1/<appid>
```
请求参数： 
```
{
"projectid":0,
"sub_service_type":0,
"engine_model_type":0,
"url":"<url>",
"res_text_format":0,
"res_type":1,
"source_type":0,
"secretid":"<secretid>",
"timestamp":1473752207,
"expired":1473752807,
"nonce":"44925",
"template_name":"test"
}
```

请求 headers 为：
```
{
"Content-Type":"application/octet-stream",
"Authorization":"<Authorization>"
}
```

综上，语音全文转写识别请求 API 为：
```
http://aai.qcloud.com/asr/v1/<appid>?engine_model_type=0
&expired=1473752807
&nonce=44925
&projectid=0
&res_text_format=0
&res_type=1
&secretid=<secretid>
&source_type=0
&sub_service_type=0
&template_name=test
&timestamp=1473752207
&url=<url>
```

## 返回结构

### RESTful API返回结果
语音全文转写识别的 RESTful API 请求返回结果如下表所示：

| 参数名称           | 类型         | 说明          | 
| ------------- | ---------- | ------------- | 
|  code |int | 服务器错误码, 0为成功|
| message  | String | 服务器  |
| requestId  | int  | 如果成功，返回任务id |

### 返回示例
 返回消息示例如下：
```
 {
 "code":0, 
 "message":"success",
 "requestId":500
 }
```

## 返回码

请求返回码如下所示。

| 数值 | 返回码 | 说明 |
|---------|---------|---------|
|0|SUCCESS|成功|
|1000|ERROR_BAD_REQ|请求的参数不符合要求|
|1001|int32|请求图片的高度|
|1002|ERROR_PARSE_DATA_FAILED|没有提供projectid，或者值不合法|
|1003|ERROR_HAS_NO_VALID_RES_TEXT_FORMAT|没有提供res_text_format，或者值不合法|
|1004|ERROR_HAS_NO_VALID_SUB_SERVICE_TYPE|没有提供sub_service_type，或者值不合法|
|1005|ERROR_HAS_NO_VALID_ENGINE_MODEL_TYPE|没有提供engine_model_type，或者值不合法|
|1006|ERROR_HAS_NO_VALID_CALLBACK_URL|没有提供callback_url，或者值不合法|
|1007|ERROR_HAS_NO_VALID_RES_TYPE|没有提供res_type，或者值不合法|
|1008|ERROR_HAS_NO_VALID_SOURCE_TYPE|没有提供source_type，或者值不合法|
|1009|ERROR_HAS_NO_VALID_URL|没有提供下载语音的url，或者值不合法|
|1010|ERROR_HAS_NO_VALID_SECRET_ID|没有提供secretid，或者值不合法|
|1011|ERROR_HAS_NO_VALID_TIMESTAMP|没有提供timestamp，或者值不合法|
|1012|ERROR_HAS_NO_VALID_EXPIRED|没有提供expired，或者值不合法|
|1013|ERROR_HAS_NO_VALID_NONCE|没有提供nonce，或者值不合法|
|1014|ERROR_HAS_NO_VALID_TEMPLATENAME|提供的template_name不合法|
|1016|ERROR_URL_TOO_LONG|提供的url长度大于2048|
|1018|ERROR_APPID_NOT_REGI|提供的appid未注册|
|1019|ERROR_APPID_PROJECTID_TEMPLATENAME_MISMATCH|提供的appid，projectid与template_name不匹配|
|1020|ERROR_PROCESS_FAILED|服务端处理出现内部错误|
|1021|ERROR_PROXY_BAD_AUTH | 签名不符合规则|
|1023|ERROR_PROXY_AUTH_TOO_LONG_EXPIRED |签名的有效期设置太长 |
|1024|ERROR_PROXY_AUTH_EXPIRED|签名过期|
|1026|ERROR_PROXY_AUTH_SECRETID_NOEXIST|签名中的secretid错误|
|1028|ERROR_PROXY_AUTH_REPLAY_ATTACK|重放攻击|
|1029|ERROR_PROXY_AUTH_FAILED|签名验证不通过|
|1031|ERROR_AUDIO_TOO_LARGE|发送的语音数据过大（大于5M）|
|1032|ERROR_SHOULD_NOT_BIND_COS|使用的template_name配置为绑定COS，但restful API的应用场景应该为不绑定COS|
|1033|ERROR_UNKNOWN|其他未知错误|


## RESTful API 回调结果

### 回调结果
当语音识别系统完成识别后，会将结果通过HTTP POST请求的形式通知到用户，用户需要在回调服务器上实现以下接口。

| 字段         | 必选      | 类型          | 说明      | 
| ------------- | ---------- | ------------- | ---------- |
| code | 是 | Int32 | 任务状态：0，成功；其他，失败 | 
| message | 是 | String | 成功或者失败原因文字描述 | 
| requestId | 是 | Unit64 | 请求 ID，与后台任务 ID 一一对应 | 
| appid | 是 | Unit64 | 腾讯云应用 ID |
| projecteid | 是 | Unit64 | 腾讯云项目 ID |
| audioUrl | 是 | String | 语音下载url |
| text | 是 | String | 识别出的结果文本 |
| audioTime | 是 | double | 语音总时长 |

注意：为了防止某些字段中，出现诸如”&”等特殊字符，导致用户解包失败，所有字段的 value 值都将进行 url_encode 之后发给用户。用户获取 value 之后，需要先对 value 进行 url_decode 以获取原始 value 值。

### 用户返回值

用户返回值如下表：

| 参数名称           | 类型         | 说明          | 
| ------------- | ---------- | ------------- | 
|  code |int | 服务器错误码, 0为成功，其他值代表失败 |
| message  | String | 失败原因说明：比如用户来不及入库。 如果用户返回失败，会间隔一段时间重新通知  |

### 示例
接口样例如下所示：
```
POST http://xx.yy.com/ code=code
& message=message
& requestId = requestId 
& appid=appid
& projectid=projectid
& audioUrl = audioUrl 
& text=text
& audioTime = audioTime
```
语音识别系统发起请求，收到请求后，用户侧需要以json格式回以响应：
```
{
  "code" : 0,   
  "message" : "成功"
}
```




