## 1 REST API简介 

REST API是腾讯云提供给APP后台的HTTP管理接口，其主要目的在于为APP后台提供一个后台管理入口。目前云通信支持的REST API参见[REST API接口列表](/doc/product/269/REST%20API接口列表)。 

除了REST API，APP[控制台](http://cloud.tencent.com/doc/product/269/%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D#3.10-.E6.8E.A7.E5.88.B6.E5.8F.B0)亦可实现简单的数据管理、单发/群发消息，开发者可以在控制台上进行简单的数据管理、查看及测试。相比之下，REST API接口较为原始，但管理能力却更为强大。

为了安全性，REST API仅提供HTTPS接口。

## 2 调用示例 

如下为通过REST API来获取APP中所有群组的示例。 

HTTPS请求： 
```
POST /v4/group_open_http_svc/get_appid_group_list?accesstoken=xxx&identifier=group_root&sdkappid=88888888&random=99999999&contenttype=json HTTP/1.1
Host: console.tim.qq.com
Content-Length: 22 
{    
    "Limit" : 2
}
```
HTTPS应答：
```
HTTP/1.1 200 OK
Server: nginx/1.7.10
Date: Fri, 09 Oct 2015 02:59:55 GMT
Content-Length: 156
Connection: keep-alive
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: X-Requested-With
Access-Control-Allow-Methods: POST

{
    "ActionStatus": "OK",
    "ErrorCode": 0,
    "GroupIdList": [
        {
            "GroupId": "@TGS#1YTTZEAEG"
        },
        {
            "GroupId": "@TGS#1KVTZEAEZ"
        }
    ],
    "TotalCount": 58530
}
```

## 3 调用方法 

### 3.1 请求URL 

REST API的URL格式如下： 
```
https://console.tim.qq.com/$ver/$servicename/$command?sdkappid=$sdkappid&identifier=$identifier&usersig=$usersig&random=99999999&contenttype=json
```
其中各个参数的含义以及取值如下（参数名称及其取值均区分大小写）： 

| 参数  | 含义  | 取值  |
|---------|---------|---------|
| ver  | 协议版本号 。|固定为v4。|
| servicename  | 内部服务名，不同的servicename对应不同的服务类型。 |参见API详细描述。|
| command  | 命令字，与servicename组合用来标识具体的业务功能。 |参见API详细描述。|
| sdkappid  | APP在云通信控制台上获取的Appid。 |在申请接入时获得。 |
| identifier  | 用户名，调用REST API时一般为APP管理员帐号。 |用户名（必须为[APP管理员帐号](/doc/product/269/账号登录集成说明#3.4-app.E7.AE.A1.E7.90.86.E5.91.98)）。 |
| usersig  | 用户名对应的签名。 |对于使用独立帐号体系的APP，参见[Linux平台下生成usersig](/doc/product/269/TLS后台API使用手册#2-linux.E5.B9.B3.E5.8F.B0)和[Windows平台下生成usersig](/doc/product/269/TLS后台API使用手册#3-windows.E5.B9.B3.E5.8F.B0)。对于使用托管帐号体系的APP，参见[下载UserSig](/doc/product/269/下载UserSig)。|
| random  | 标识当前请求的整数随机数参数。 |32位无符号整数随机数。 |

>**注意：** 
1. APP服务端在调用REST API时，identifier必须为[APP管理员帐号](/doc/product/269/账号登录集成说明#3.4-app.E7.AE.A1.E7.90.86.E5.91.98)；
2. APP可以在每次调用REST API时都生成管理员账号的usersig，亦可生成一个固定的usersig重复使用，但请特别注意usersig的有效期。 

### 3.2 HTTP请求包体格式

REST API仅支持POST方法，其请求包体为JSON格式，具体的包体格式参见每个API的详细描述。 

需要特别注意的是，POST包体不能为空，即使某条协议包体中不需要携带任何信息，也需要携带一个空的JSON对象，即`{}`。

### 3.3 HTTP返回码 

除非发生网络错误（例如502错误），REST API的调用结果均为200，真正的API调用错误码与错误信息是在HTTP应答包体中返回的。

### 3.4 HTTP应答包体格式 

REST API的应答包体也是JSON格式，其格式符合如下特征：
```
{
    "ActionStatus": "OK",
    "ErrorInfo": "",
    "ErrorCode": 0,
    // REST API其他应答内容
}
```
应答包体中必然包含ActionStatus、ErrorInfo、ErrorCode这三个属性，其含义如下：

| 字段 | 类型| 说明 |
|---------|---------|---------|
|ActionStatus | String | 请求处理的结果，OK表示处理成功，FAIL表示失败，如果为FAIL，ErrorInfo带上失败原因。 |
|ErrorInfo  | String | 失败原因 。|
|ErrorCode  | Integer | 错误码，0为成功，其他为失败，可查询[错误码表](/doc/product/269/错误码)得到具体的原因。|

## 4 REST API公共错误码 

| 错误码 |含义说明| 
|---------|---------|
| 80001 | 消息文本安全打击。 | 
| 60002 | HTTP解析错误 ，请检查HTTP请求URL格式。| 
| 60003 | HTTP请求JSON解析错误，请检查JSON格式 。| 
| 60004 | 请求URL或JSON包体中帐号或签名错误 。| 
| 60005 | 请求URL或JSON包体中帐号或签名错误 。| 
| 60006 | appid失效，请核对appid有效性 。| 
| 60007 | rest接口调用频率超过限制，请降低请求频率 。| 
| 60008 | 服务请求超时或HTTP请求格式错误，请检查并重试 。| 
| 60009 | 请求资源错误，请检查请求URL。 | 
| 60010 | 请求需要[APP管理员](/doc/product/269/账号登录集成说明#3.4-app.E7.AE.A1.E7.90.86.E5.91.98)权限，请检查接口调用权限。 | 
| 60011 | appid请求频率超限，请降低请求频率。 | 
| 60012 | REST接口需要带sdkappid，请检查请求URL中的sdkappid。 |
| 60013 | HTTP响应包JSON解析错误。 | 
| 60014 | 置换id超时。 | 
| 60015 | 请求包体帐号类型错误，请确认帐号为字符串格式。 | 

## 5 REST API调试工具 

您可以通过如下几种工具来REST API的调试。

### 5.1 REST API调试工具 

通过[REST API在线调试工具](https://avc.cloud.tencent.com/im/APITester/APITester.html)调试本接口
使用案例参见[这里](/doc/product/269/%E6%9C%8D%E5%8A%A1%E7%AB%AF%E9%9B%86%E6%88%90%E6%8C%87%E5%BC%95#5.2-.E5.AF.BC.E5.85.A5.E8.B4.A6.E5.8F.B7.E5.88.B0.E4.BA.91.E9.80.9A.E4.BF.A1.EF.BC.88.E4.BD.BF.E7.94.A8.E4.BA.91.E9.80.9A.E8.AE.AFrest-api.E8.B0.83.E8.AF.95.E5.B7.A5.E5.85.B7.EF.BC.89)。 

### 5.2 Postman 

Postman是一款功能强大的网页调试与发送网页HTTP请求的Chrome插件。其使用案例参见[这里](https://cloud.tencent.com/document/product/269/1510)。

### 5.3 PHP Server SDK中的调试工具 

[PHP Server SDK](/doc/product/269/PHP%20Server%20SDK)中包含了一个REST API调试工具：TimRestApiGear.php。您可以通过该工具在服务器上发起简单REST API调用。使用案例参见[这里](/doc/product/269/服务端集成指引#5.4-.E5.88.9B.E5.BB.BA.E4.B8.80.E4.B8.AA.E7.BE.A4.E7.BB.84.EF.BC.8C.E5.8C.85.E5.90.AB.E5.88.9D.E5.A7.8B.E7.BE.A4.E6.88.90.E5.91.98.EF.BC.88.E4.BD.BF.E7.94.A8php-server-sdk.E4.B8.AD.E7.9A.84.E5.B7.A5.E5.85.B7.EF.BC.89)。

## 6 Server SDK集成 

### 6.1 PHP Server SDK 

[PHP Server SDK](/doc/product/269/PHP%20Server%20SDK)将一些常用的REST API封装成了函数，并以接口类的方式暴露给开发者。 

## 7 FAQ 

### 7.1 REST请求有概率超时，收不到任何响应 

（1）IM后台REST接口设置的超时时间是3s，调用方设置的超时时间应该长于3s。
（2）telnet yun.tim.qq.com 443 确认能否连接服务端口。
（3）使用curl -G https://yun.tim.qq.com 简单测试确认能够收到响应。
（4）确认机器的dns server配置是内网dns server，还是公共dns server。如果是内网dns server，请确保dns server网络出口和本机器网络出口ip所在地域运营商一致。
（5）建议业务调用方使用“长连接+连接池”模式。 
