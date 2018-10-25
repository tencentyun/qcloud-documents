## REST API简介 
REST API是腾讯云暴露给APP后台的HTTP管理接口，其主要目的在于为APP后台提供一个后台管理入口。 
目前云通信支持的REST API参见REST API接口列表。 
除了REST API，APP控制台亦可实现简单的数据管理、单发/群发消息；相比之下，REST API接口较为原始，但管理能力却更为强大。
## 调用示例 
如下为通过REST API来获取APP中所有群组的示例。 
HTTPS请求： 
```
POST /v4/group_open_http_svc/get_appid_group_list?accesstoken=xxx&identifier=group_root&sdkappid=88888888&contenttype=json HTTP/1.1Host: console.tim.qq.comContent-Length: 22 {    "Limit" : 2}
```
HTTPS应答：
```
HTTP/1.1 200 OKServer: nginx/1.7.10Date: Fri, 09 Oct 2015 02:59:55 GMTContent-Length: 156Connection: keep-aliveAccess-Control-Allow-Origin: *Access-Control-Allow-Headers: X-Requested-WithAccess-Control-Allow-Methods: POST {    "ActionStatus": "OK",    "ErrorCode": 0,    "GroupIdList": [        {            "GroupId": "@TGS#1YTTZEAEG"        },        {            "GroupId": "@TGS#1KVTZEAEZ"        }    ],    "TotalCount": 58530}
```
## 调用方法 
### 请求URL 
REST API的URL格式如下： 
https://console.tim.qq.com/$ver/$servicename/$command?sdkappid=$sdkappid&identifier=$identifier&usersig=$usersig&contenttype=json
其中各个参数的含义以及取值如下（参数名称及其取值均区分大小写）： 

| 参数  | 含义  | 取值  |
|---------|---------|---------|
| ver  | 协议版本号 。|固定为v4。|
| servicename  | 内部服务名，不同的servicename对应不同的服务类型。 |参见API详细描述。|
| command  | 命令字，与servicename组合用来标识具体的业务功能。 |参见API详细描述。|
| sdkappid  | APP在即时通信云中的Appid。 |在申请接入时获得。 |
| identifier  | 用户名，调用REST API时一般为APP管理员帐号。 |用户名（必须为APP管理员帐号）。 |
| usersig  | 用户名对应的签名。 |对于使用独立帐号体系的APP，参见[这里](http://avc.qcloud.com/wiki2.0/im/帐号登录集成/TLS后台API使用手册/TLS后台API使用手册.html#articleContent/h3%3acontains%7blinux%E4%B8%8B%E7%94%9F%E6%88%90sig%E5%92%8C%E6%A0%A1%E9%AA%8Csig%7d)，生成sig。对于使用托管帐号体系的APP，参见[这里](http://avc.qcloud.com/wiki2.0/im/HIDE/如何/如何：生成用户凭证/如何：生成用户凭证.html)，生成sig。|

注意： 
1.APP服务端在调用REST API时，identifier必须为APP管理员帐号；
2.APP可以在每次调用REST API时都生成usersig，亦可生成一个固定的usersig重复使用，但请特别注意usersig的有效期。 
### HTTP请求包体格式
REST API仅支持POST方法，其请求包体为JSON格式，具体的包体格式参见每个API的详细描述。 
需要特别注意的是，POST包体不能为空，即使某条协议包体中不需要携带任何信息，也需要携带一个空的JSON对象，即{}。
### HTTP返回码 
除非发生网络错误（例如502错误），REST API的调用结果均为200，真正的API调用错误码与错误信息是在HTTP应答包体中返回的。详见HTTP应答格式一节。 
### HTTP应答包体格式 
REST API的应答包体也是JSON格式，其格式符合如下特征：
```
{    "ActionStatus": "OK",    "ErrorInfo": "",    "ErrorCode": 0,    // REST API其他应答内容}
```
应答包体中必然包含ActionStatus、ErrorInfo、ErrorCode这三个属性，其含义如下：

| 字段 | 类型| 说明 |
|---------|---------|---------|
|ActionStatus | String | 请求处理的结果，OK表示处理成功，FAIL表示失败，如果为FAIL，ErrorInfo带上失败原因。 |
|ErrorInfo  | String | 失败原因 |
|ErrorCode  | Integer | 错误码，0为成功，其他为失败。|
## REST API公共错误码 
| 错误码 |含义说明| 
|---------|---------|
| 80001 | 消息文本安全打击 | 
| 60002 | HTTP解析错误 | 
| 60003 | JSON解析错误 | 
| 60004 | 请求URI或JSON包体中帐号错误 | 
| 60005 | 请求URI或JSON包体中帐号错误 | 
| 60006 | sdkappid被限制 | 
| 60007 | sdkappid请求的REST接口频率超限 | 
| 60008 | 服务超时 | 
| 60009 | 请求资源错误 | 
## REST API调试工具 
您可以通过如下几种工具来REST API的调试： 
### REST API调试工具 
https://avc.qcloud.com/im/APITester/APITester.html
使用案例参见[这里](http://avc.qcloud.com/wiki2.0/im/新手指引/服务端集成指引/服务端集成指引.html#articleContent/h2%3acontains%7b%E5%AF%BC%E5%85%A5%E8%B4%A6%E5%8F%B7%E5%88%B0%E4%BA%91%E9%80%9A%E4%BF%A1%EF%BC%88%E4%BD%BF%E7%94%A8%E4%BA%91%E9%80%9A%E8%AE%AFREST%20API%E8%B0%83%E8%AF%95%E5%B7%A5%E5%85%B7%EF%BC%89%7d)。 
### Postman 
Postman是一款功能强大的网页调试与发送网页HTTP请求的Chrome插件。其使用案例参见[这里](http://avc.qcloud.com/wiki2.0/im/新手指引/服务端集成指引/服务端集成指引.html#articleContent/h2%3acontains%7b%E4%B8%BA%E5%AF%BC%E5%85%A5%E7%9A%84%E8%AE%BE%E7%BD%AE%E8%B4%A6%E5%8F%B7%E7%9A%84%E5%9F%BA%E6%9C%AC%E8%B5%84%E6%96%99%EF%BC%88%E4%BD%BF%E7%94%A8Postman%EF%BC%89%7d)。
### PHP Server SDK中的调试工具 
PHP Server SDK中包含了一个REST API调试工具：TimRestApiGear.php。您可以通过该工具在服务器上发起简单REST API调用。使用案例参见[这里](http://avc.qcloud.com/wiki2.0/im/新手指引/服务端集成指引/服务端集成指引.html#articleContent/h2%3acontains%7b%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E7%BE%A4%E7%BB%84%EF%BC%8C%E5%8C%85%E5%90%AB%E5%88%9D%E5%A7%8B%E7%BE%A4%E6%88%90%E5%91%98%EF%BC%88%E4%BD%BF%E7%94%A8PHP%20Server%20SDK%E4%B8%AD%E7%9A%84%E5%B7%A5%E5%85%B7%EF%BC%89%7d)。
## Server SDK集成 
### PHP Server SDK 
PHP Server SDK将一些常用的REST API封装成了函数，并以接口类的方式暴露给开发者。 
集成方法参见PHP Server SDK。 
