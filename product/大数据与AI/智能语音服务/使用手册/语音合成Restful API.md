##  功能简介

语音合成服务提供文本转语音服务，支持多种音色选择、语速选择。

目前提供Restful API方式，用户可以通过API上传需要合成的中文文本，系统会立即进行合成，云端合成成功后，返回合成结果语音。

语音合成实现了机器向人的语音交互，适用场景包括：广播播报，有声小说，智能车载等等，让应用开口说话，便捷人机交互。

## Restful API
语音合成的 RESTful API 请求结构如下：

| 参数名称    | 必选   | 类型   | 描述    | 
| ------------- | ---------- | ------------- | ---------- |
| Version | 是         | String          | HTTPS 协议版本         | 
| URL  | 是         | String          | HTTPS 请求地址       | 
| Https Headers    | 是         | 数据集合          | HTTPS 请求头部         | 
| Https Method   |是         | String     | HTTPS 请求方法，请求方法为 POST
| Https Body   | 是         | String          | HTTPS 请求正文    | 

其中，URL 的结构为 ：
```
https://aai.qcloud.com/tts/v1/<appid>?
projectid=xxx&
sub_service_type=xxx&
speech_format=xxx&
volume=xxx&
person=xxx&
speed=xxx&
secretid=<secretid>&
timestamp=xxx&
expired=xxx&
nonce=xxx
```

URL 中各字段含义如下（各字段的值需要进行 URL 编码）：

| 字段           | 必选         | 类型          | 描述         | 
| ------------- | ---------- | ------------- | ---------- |
| appid  | 是 | uint  | 腾讯云应用 ID 值   | 
| projectid  | 否   | uint | 腾讯云项目 ID，不填为默认项目，即0，总长度不超过1024字节 | 
| sub_service_type  | 是   | uint   | 子服务类型。0：短文本实时合成。目前只支持短文本实时合成  | 
| speech_format  | 是  | String  | 合成语音格式，目前支持MP3格式  | 
| volume | 是  | uint  | 音量，默认为5，取值范围为0-10 |
| person | 是 | uint  | 发音人，目前仅支持0，女声 |
| speed | 是 | uint  | 语速，默认值为0，取值范围为-40到40，1表示加速到原来的1.1倍，-1为相对于正常语速放慢1.1倍 |
| secretid  | 是 | String | 官网云API密钥中获得的SecretId |
| timestamp | 是 | uint | 当前时间戳，是一个符合 UNIX Epoch 时间戳规范的数值，单位为秒 | 
| expired |  是 | uint | 签名的有效期，是一个符合 UNIX Epoch 时间戳规范的数值，单位为秒；expired 必须大于 timestamp 且 expired - timestamp 小于90天 |
| nonce | 是 | uint | 随机正整数。用户需自行生成，最长10位 |

HTTPS  Headers 的结构如下：

| 参数名称 | 必选  | 类型 | 描述  | 
| -------- | ------ | ------- | ------ |
| Host   | 是  | String | 语音识别服务域名，固定为 ``aai.qcloud.com ``| 
| Authorization  | 是   | String  | 用户的有效签名，用于鉴权。对应签名鉴权中得到的签名字符串 | 
| Content-Type   | 是 | String | multipart/form-data  | 
| Content-Length  | 是  | Int  | 请求长度，此处为https body总的字节数。文本数据，utf-8编码，长度限制为1024字节以内  | 

### 请求示例

下列示例中，<箭头括号>表示必须替换为有效值的变量。请求 Host 与路径：
```
https://aai.qcloud.com/tts/v1/<appid>?
```
请求参数： 
```
{
"projectid":"0",
"sub_service_type":"0",
"speech_format":"mp3",
"volume":"3",
"person":"0",
"speed":"0",
"secretid":"AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5",
"timestamp":"1484109983",
"expired":"1484113583",
"nonce":"1675199141"
}
```
这里以< appid > = 20170111, < SecretKey >=oaYWFO70LGDmcpfwo8uF1IInayysGtgZ 为例拼接签名原文，则拼接的签名原文为：
```
POSTaai.qcloud.com/tts/v1/20170111?expired=1484113583&nonce=1675199141&person=0&projectid=0&secretid=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5&speech_format=mp3&speed=0&sub_service_type=0&timestamp=1484109983&volume=3
```
对原文进行加密处理：
```
Base64Encode(HmacSha1(签名原文, SecretKey))
```
最终得到签名串为：
```
HRCKlbwPhWtVvfGn914qE5O1rwc=
```
请求 headers 为：
```
{
"Content-Type":"multipart/form-data",
"Authorization":"HRCKlbwPhWtVvfGn914qE5O1rwc="
}
```

## 返回结构

### RESTful API 返回结果

语音全文转写识别的 RESTful API 请求返回结果如下表所示：

| 参数名称           | 类型         | 说明          | 
| ------------- | ---------- | ------------- | 
|  code |int | 服务器错误码，0为成功|
| message  | String | 服务器返回的信息  |
| speech  | String | 经过Base64编码的合成语音数据  |

### 返回示例
 返回消息示例如下：
```
 {
 "code":0, 
 "message":"success",
 "speech": "xxxxxxx"
 }
```

## 返回码

请求返回码如下所示：

| 数值  | 说明 |
|---------|---------|
|0|成功|
|100|获取文本失败 |
|101|文本字节数超过限制|
|102|参数不合法|
|103|appid不合法|
|104|模板不存在|
|105|鉴权失败|
|106|获取后台ip地址错误|
|107|后台服务器超时|
|108|后台服务器故障|
|109|合成结果为空|
|110|合成结果包格式错误|
|111|文本为空|
|112|文本转码失败|
|1000|后台接收包格式错误|
|1001|字符集不支持|
|1002|语音合成失败|
|1003|语音转码失败|

## Python代码示例
```python
#!/usr/bin/python
# coding: UTF-8

import requests
import time
import random
import hmac, hashlib, base64
import json

appid = 0
secret_id = 'your_secret_id'
secret_key = 'your_secret_key'

args = {
        'secretid': secret_id,
        'projectid': 0,
        'sub_service_type': 0,
        'speech_format': 'mp3',
        'volume': 2,
        'person': 0,
        'speed': 0,
        'timestamp': int(time.time()),
        'expired': int(time.time()) + 60 * 60,
        'nonce': random.randint(1048576, 104857600),
}

query_str = "&".join(["%s=%s"%(k,args[k]) for k in sorted(args.keys())])
calc_str = "POSTaai.qcloud.com/tts/v1/%(appid)s?%(query_str)s"%vars()
hashed = hmac.new(secret_key, calc_str, hashlib.sha1)
headers = {"Authorization": base64.b64encode(hashed.digest())}

url = "http://aai.qcloud.com/tts/v1/%(appid)s?%(query_str)s"%vars()
upload_file = "hello.txt"
files = {"file": open(upload_file, "rb")}
resp = requests.post(url=url, files=files, headers=headers)
resp = json.loads(resp.text)
data = base64.b64decode(resp["speech"])

f = open("hello.mp3", "w")
f.write(data)
f.close()
```

## PHP代码示例
```php
<?php
ini_set("display_errors", "1");
error_reporting(E_ALL);
$serverIp = "aai.qcloud.com";
$serverPort = 80;

$appid = YOUR_APPID;
// 获取secretId 和 secretKey -> https://console.cloud.tencent.com/capi
$secret_id = 'YOUR_SECRET_ID';
$secret_key = 'YOUR_SECRET_KEY';

$query_arr = array(
    'secretid' => $secret_id,
    'projectid' => 0,
    'sub_service_type' => 0,
    'speech_format' => 'mp3',
    'volume' => 2,
    'person' => 0,
    'speed' => 0,
    'timestamp' => time(),
    'expired' => time() + 60 * 60,
    'nonce' => rand(),
);

ksort($query_arr);
$query_str = "";
foreach($query_arr as $key => $val) {
    $query_str .= "$key=$val&";
}
$query_str = trim($query_str, "&");

// 计算签名
$sign_str = "POSTaai.qcloud.com/tts/v1/$appid?$query_str";
$signature = base64_encode(hash_hmac('SHA1', $sign_str, $secret_key, TRUE));

// 请求消息体，multipart/form-data格式
$form_boundary = "----WebKitFormBoundarybS1Fvrpes3yfBSvu";
$body_str = "--$form_boundary\r\n";
$body_str .= "Content-Disposition: form-data; name=".'"'."test1".'"'."; filename=".'"'."test_upload.txt".'"'."\r\n";
$body_str .= "Content-Type: application/octet-stream\r\n";
$body_str .= "\r\n";
$body_str .= "你好啊吃饭了没\r\n";
$body_str .= "--$form_boundary\r\n";
$body_str .= "Content-Disposition: form-data; name=".'"'."test2".'"'."; filename=".'"'."debug.log".'"'."\r\n";
$body_str .= "Content-Type: application/octet-stream\r\n";
$body_str .= "\r\n";
$body_str .= "最近雾霾很严重最好留在室内\r\n";
$body_str .= "--$form_boundary\r\n";
$body_str .= 'Content-Disposition: form-data; name="submit"'."\r\n";
$body_str .= "\r\n";
$body_str .= "Submit\r\n";
$body_str .= "--$form_boundary--\r\n";

$req = "POST /tts/v1/$appid?$query_str HTTP/1.1 \r\n";
$req .= "Host: aai.qcloud.com\r\n";
$req .= "Authorization: $signature\r\n";
$req .= "Content-Type: multipart/form-data; boundary=$form_boundary\r\n";
$req .= "Content-Length: ";
$req .= strlen($body_str);
$req .= "\r\n\r\n";
$req .= $body_str;
echo "=================== req start ===================\n";
echo "$req\n";
echo "=================== req end ===================\n";
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if($socket < 0){
    echo "socket_create failed : ".socket_strerror($socket)."\n";
    return ;
}
$res = socket_connect($socket, $serverIp,$serverPort);
if($res < 0){
    echo "socket_connect failed : ".socket_strerror($res)."\n";
    return ;
}
$res = socket_write($socket,$req,strlen($req));
if(!$res){
    echo "socket_write failed : ".socket_strerror($socket)."\n";
    return ;
}
$rsp = "";
while($tmprsp = socket_read($socket,8192)){
    $rsp .= $tmprsp;
}
echo "=================== resp ===================\n";
echo "rsp :\n".$rsp."\n";
socket_close($socket);
```