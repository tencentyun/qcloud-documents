## 请求结构


### RESTful API请求结构

离线语音识别的 RESTful API 请求结构如下：

| 参数名称    | 必选    | 类型   | 描述    | 
| ------------- | ---------- | ------------- | ---------- |
| Version | 是         | String          | HTTPS 协议版本         | 
| URL  | 是         | String          | HTTPS 请求地址       | 
| Https Headers    | 是         | 数据集合          | HTTPS 请求头部         | 
| Https Method   |是         | String     | HTTPS 请求方法，离线语音识别请求方法为 POST
| Https Body   | 是         | String     | HTTPS 请求正文，即语音数据（当 source_type 字段为1时填充），大小不超过 5M   | 

其中，URL 的结构为 ：
```
https://aai.qcloud.com/asr/v1/appid?
projectid=xxx&
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
| sub_service_type  | 是   | uint   | 子服务类型。0：离线语音识别。1：实时流式识别。  | 
| engine_model_type | 是  | String  | 引擎类型。8k_0：电话8k通用模型；16k_0：16k 通用模型| 
| callback_url | 是  | String  | 回调 URL，用户接受结果，长度大于0，小于2048 |
| channel_num | 否  | unit  | 语音声道数，仅在电话8k通用模型下，支持1和2，其他模型仅支持1 |
| res_text_format | 是 | uint  | 识别结果文本编码方式。0：UTF-8；1：GB2312； 2：GBK； 3：BIG5 |
| res_type | 否 | uint  | 结果返回方式。0：同步返回；1：异步返回。目前只支持异步返回 |
| source_type | 是 | uint  |  语音数据来源。0：语音 URL；1：语音数据（post body）|
| url | 否   | String  | 语音URL，公网可下载。当 source_type 值为0时须填写该字段，为1时不填；URL 的长度大于0，小于2048 |
| secretid  | 是 | String | 官网 SecretId |
| timestamp | 是 | uint | 当前时间戳，是一个符合 UNIX Epoch 时间戳规范的数值，单位为秒 | 
| expired |  是 | uint | 签名的有效期，是一个符合 UNIX Epoch 时间戳规范的数值，单位为秒；expired 必须大于 timestamp 且 expired - timestamp 小于90天 |
| nonce | 是 | uint | 随机正整数。用户需自行生成，最长10位 |

HTTPS  Headers 的结构如下：

| 参数名称 | 必选  | 类型 | 描述  | 
| -------- | ------ | ------- | ------ |
| Host   | 是  | String | 语音识别服务域名，固定为 ``aai.qcloud.com ``| 
| Authorization  | 是   | String  | 用户的有效签名，用于鉴权。对应签名鉴权中得到的签名字符串 | 
| Content-Type   | 是 | String | application/octet-stream   | 
| Content-Length  | 是  | Int  | 请求长度，此处对应语音数据字节数，单位：字节  | 

### 请求示例

下列示例中，<箭头括号>表示必须替换为有效值的变量。当语音数据来源 source_type=0时，采用公网可访问URL语音数据，请求 Host 与路径：
```
http://aai.qcloud.com/asr/v1/<appid>
```
请求参数： 
```
{
"projectid":0,
"sub_service_type":0,
"engine_model_type":1,
"url":"http://test.qq.com/rec_callback",
"res_text_format":0,
"res_type":1,
"callback_url":"http://test.qq.com/rec_callback",
"source_type":0,
"secretid":"AKIDUfLUEUigQiXqm7CVSspKJnuaiIKtxqAv",
"timestamp":1473752207,
"expired":1473752807,
"nonce":"44925",
}
```
这里以< appid > = 200001, < SecretKey >=bLcPnl88WU30VY57ipRhSePfPdOfSruK 为例拼接签名原文，则拼接的签名原文为：
```
POSTaai.qcloud.com/asr/v1/2000001?callback_url=http://test.qq.com/rec_callback&engine_model_type=1&expired=1473752807&nonce=44925&projectid=0&res_text_format=0&res_type=1&secretid=AKIDUfLUEUigQiXqm7CVSspKJnuaiIKtxqAv&source_type=0&sub_service_type=0&timestamp=1473752207&url=http://test.qq.com/voice_url
```
对原文进行加密处理：
```
Base64Encode(HmacSha1(签名原文, SecretKey))
```
最终得到签名串为：
```
UyKZ+Q4xMbdu3gxOmPD7tgnAm1A=
```
请求 headers 为：
```
{
"Content-Type":"application/octet-stream",
"Authorization":"UyKZ+Q4xMbdu3gxOmPD7tgnAm1A="
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
&timestamp=1473752207
&url=<url>
```

## 返回结构

### RESTful API 返回结果
离线语音识别的 RESTful API 请求返回结果如下表所示：

| 参数名称           | 类型         | 说明          | 
| ------------- | ---------- | ------------- | 
|  code |int | 服务器错误码，0为成功|
| message  | String | 服务器返回的信息  |
| requestId  | int  | 如果成功，返回任务 id |

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

请求返回码如下所示：

| 数值 | 返回码 | 说明 |
|---------|---------|---------|
|0|SUCCESS|成功|
|1000|ERROR_BAD_REQ|请求的参数不符合要求|
|1001|ERROR_PARSE_DATA_FAILED|解析请求参数时失败|
|1002|ERROR_HAS_NO_VALID_PROJECTID|没有提供 projectid，或者值不合法|
|1003|ERROR_HAS_NO_VALID_RES_TEXT_FORMAT|没有提供 res_text_format，或者值不合法|
|1004|ERROR_HAS_NO_VALID_SUB_SERVICE_TYPE|没有提供 sub_service_type，或者值不合法|
|1005|ERROR_HAS_NO_VALID_ENGINE_MODEL_TYPE|没有提供 engine_model_type，或者值不合法|
|1006|ERROR_HAS_NO_VALID_CALLBACK_URL|没有提供 callback_url，或者值不合法|
|1007|ERROR_HAS_NO_VALID_RES_TYPE|没有提供 res_type，或者值不合法|
|1008|ERROR_HAS_NO_VALID_SOURCE_TYPE|没有提供 source_type，或者值不合法|
|1009|ERROR_HAS_NO_VALID_URL|没有提供下载语音的 url，或者值不合法|
|1010|ERROR_HAS_NO_VALID_SECRET_ID|没有提供 secretid，或者值不合法|
|1011|ERROR_HAS_NO_VALID_TIMESTAMP|没有提供 timestamp，或者值不合法|
|1012|ERROR_HAS_NO_VALID_EXPIRED|没有提供 expired，或者值不合法|
|1013|ERROR_HAS_NO_VALID_NONCE|没有提供 nonce，或者值不合法|
|1016|ERROR_URL_TOO_LONG|提供的 url 长度大于2048|
|1018|ERROR_APPID_NOT_REG|提供的 appid 未注册|
|1014|ERROR_HAS_NO_VALID_TEMPLATENAME|提供的 template_name 不合法|
|1016|ERROR_URL_TOO_LONG|提供的 url 长度大于2048|
|1018|ERROR_APPID_NOT_REGI|提供的 appid 未注册|
|1019|ERROR_APPID_PROJECTID_TEMPLATENAME_MISMATCH|提供的 appid，projectid 与 template_name 不匹配|
|1020|ERROR_PROCESS_FAILED|服务端处理出现内部错误|
|1021|ERROR_PROXY_BAD_AUTH | 签名不符合规则|
|1023|ERROR_PROXY_AUTH_TOO_LONG_EXPIRED |签名的有效期设置太长 |
|1024|ERROR_PROXY_AUTH_EXPIRED|签名过期|
|1026|ERROR_PROXY_AUTH_SECRETID_NOEXIST|签名中的 secretid 错误|
|1028|ERROR_PROXY_AUTH_REPLAY_ATTACK|重放攻击|
|1029|ERROR_PROXY_AUTH_FAILED|签名验证不通过|
|1031|ERROR_AUDIO_TOO_LARGE|发送的语音数据过大（大于 5M）|
|1033|ERROR_UNKNOWN|其他未知错误|

## PHP代码示例

```php
<?php
$appid = YOUR_APPID ;
// https://console.cloud.tencent.com/capi
// 从该页面获取APPID的SecretId和SecretKey
$secretid ='YOUR_SECRET_ID';
$secretkey = 'YOUR_SECRET_KEY';

$req_url = 'aai.qcloud.com/asr/v1/'.$appid;

$args = array(
    'channel_num' => 1,
    'secretid' => $secretid,
    'engine_model_type' => 1,
    'timestamp' => time(),
    'expired' => time() + 3600,
    'nonce' => rand(100000, 200000),
    'projectid' => 0,
    'callback_url' => "http://aai.qcloud.com/cb",
    'res_text_format' => 0,
    'res_type' => 1,
    'source_type' => 0,
    'sub_service_type' => 0,
    'url' => "http://aai.qcloud.com/test.mp3",
);

// 参数按照Key的字母序排序
ksort($args);

$arg_str = "";
foreach($args as $k => $v) {
    $arg_str = $arg_str . "$k=$v&";
}
$arg_str = trim($arg_str, "&");

// 拼接签名串
$sig_str = "POST$req_url?$arg_str";
echo "sig_str: $sig_str\n";

// 计算签名
$signature = base64_encode(hash_hmac("sha1", $sig_str, $secretkey, TRUE));
echo "signature: $signature\n";

$req_url = "https://$req_url?$arg_str";
echo "curl -sv -H 'Authorization:$signature' '$req_url' -d ''\n";

```

