## REST API 简介
REST API 是腾讯云提供给 App 后台的 HTTP 管理接口，其主要目的在于为 App 后台提供一个后台管理入口。目前云通信支持的 REST API 参见 [REST API 接口列表](/doc/product/269/REST%20API接口列表)。

除了 REST API，App [控制台](http://cloud.tencent.com/doc/product/269/%E5%8A%9F%E8%83%BD%E4%BB%8B%E7%BB%8D#.E6.8E.A7.E5.88.B6.E5.8F.B0) 也可实现简单的数据管理、单发/群发消息，开发者可以在控制台上进行简单的数据管理、查看及测试。相比之下，REST API 接口较为原始，但管理能力却更为强大。
为了安全性，REST API 仅提供 HTTPS 接口。
## 调用示例
以下为通过 REST API 来获取 App 中所有群组的示例。

HTTPS 请求：
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

## 调用方法
### 请求 URL

REST API 的 URL 格式如下：
```
https://console.tim.qq.com/$ver/$servicename/$command?sdkappid=$sdkappid&identifier=$identifier&usersig=$usersig&random=99999999&contenttype=json
```
其中各个参数的含义以及取值如下（参数名称及其取值均区分大小写）：

| 参数  | 含义  | 取值  |
|---------|---------|---------|
| ver  | 协议版本号 。|固定为 v4。|
| servicename  | 内部服务名，不同的 servicename 对应不同的服务类型。 |参见 API 详细描述。|
| command  | 命令字，与 servicename 组合用来标识具体的业务功能。 |参见 API 详细描述。|
| sdkappid  | App 在云通信控制台上获取的 Appid。 |在申请接入时获得。 |
| identifier  | 用户名，调用 REST API 时一般为 App 管理员帐号。 |用户名（必须为 [App 管理员帐号](/doc/product/269/帐号登录集成说明#3.4-app.E7.AE.A1.E7.90.86.E5.91.98)）。 |
| usersig  | 用户名对应的签名。 |对于使用独立帐号体系的 App，参见 [Linux 平台下生成 usersig](/doc/product/269/TLS后台API使用手册#2-linux.E5.B9.B3.E5.8F.B0)和[Windows平台下生成usersig](/doc/product/269/TLS后台API使用手册#3-windows.E5.B9.B3.E5.8F.B0)。对于使用托管帐号体系的 App，参见 [下载 UserSig](/doc/product/269/下载UserSig)。|
| random  | 标识当前请求的整数随机数参数。 |32 位无符号整数随机数。 |

>**注意：**
1. App 服务端在调用 REST API 时，identifier 必须为 [App 管理员帐号](/doc/product/269/帐号登录集成说明#3.4-app.E7.AE.A1.E7.90.86.E5.91.98)；
2. App 可以在每次调用 REST API 时都生成管理员帐号的 usersig，亦可生成一个固定的 usersig 重复使用，但请特别注意 usersig 的有效期。

### HTTP 请求包体格式
REST API 仅支持 POST 方法，其请求包体为 JSON 格式，具体的包体格式参见每个 API 的详细描述。
需要特别注意的是，POST 包体不能为空，即使某条协议包体中不需要携带任何信息，也需要携带一个空的 JSON 对象，即`{}`。

### HTTP 返回码
除非发生网络错误（例如 502 错误），REST API 的调用结果均为 200，真正的 API 调用错误码与错误信息是在 HTTP 应答包体中返回的。

### HTTP 应答包体格式
REST API 的应答包体也是 JSON 格式，其格式符合如下特征：
```
{
    "ActionStatus": "OK",
    "ErrorInfo": "",
    "ErrorCode": 0,
    // REST API 其他应答内容
}
```
应答包体中必然包含 ActionStatus、ErrorInfo、ErrorCode 这三个属性，其含义如下：

| 字段 | 类型| 说明 |
|---------|---------|---------|
|ActionStatus | String | 请求处理的结果，OK 表示处理成功，FAIL 表示失败，如果为 FAIL，ErrorInfo 带上失败原因。 |
|ErrorInfo  | String | 失败原因 。|
|ErrorCode  | Integer | 错误码，0 为成功，其他为失败，可查询 [错误码表](/doc/product/269/错误码) 得到具体的原因。|

## REST API 公共错误码

| 错误码 |含义说明|
|---------|---------|
| 80001 | 消息文本安全打击。 |
| 60002 | HTTP 解析错误 ，请检查 HTTP 请求 URL 格式。|
| 60003 | HTTP 请求 JSON 解析错误，请检查 JSON 格式 。|
| 60004 | 请求 URL 或 JSON 包体中帐号或签名错误 。|
| 60005 | 请求 URL 或 JSON 包体中帐号或签名错误 。|
| 60006 | appid 失效，请核对 appid 有效性 。|
| 60007 | rest 接口调用频率超过限制，请降低请求频率 。|
| 60008 | 服务请求超时或 HTTP 请求格式错误，请检查并重试 。|
| 60009 | 请求资源错误，请检查请求 URL。 |
| 60010 | 请求需要 [App 管理员](/doc/product/269/帐号登录集成说明#3.4-app.E7.AE.A1.E7.90.86.E5.91.98)权限，请检查接口调用权限。 |
| 60011 | appid 请求频率超限，请降低请求频率。 |
| 60012 | REST 接口需要带 sdkappid，请检查请求 URL 中的 sdkappid。 |
| 60013 | HTTP 响应包 JSON 解析错误。 |
| 60014 | 置换 ID 超时。 |
| 60015 | 请求包体帐号类型错误，请确认帐号为字符串格式。 |

## REST API 调试工具
您可以通过如下几种工具来 REST API 的调试。

### REST API 调试工具
通过 [REST API在线调试工具](https://avc.cloud.tencent.com/im/APITester/APITester.html)调试本接口
使用案例参见 [这里](/doc/product/269/%E6%9C%8D%E5%8A%A1%E7%AB%AF%E9%9B%86%E6%88%90%E6%8C%87%E5%BC%95#5.2-.E5.AF.BC.E5.85.A5.E8.B4.A6.E5.8F.B7.E5.88.B0.E4.BA.91.E9.80.9A.E4.BF.A1.EF.BC.88.E4.BD.BF.E7.94.A8.E4.BA.91.E9.80.9A.E8.AE.AFrest-api.E8.B0.83.E8.AF.95.E5.B7.A5.E5.85.B7.EF.BC.89)。

### Postman
Postman 是一款功能强大的网页调试与发送网页 HTTP 请求的 Chrome 插件。其使用案例参见 [这里](https://cloud.tencent.com/document/product/269/1510)。

### PHP Server SDK 中的调试工具

[PHP Server SDK](/doc/product/269/PHP%20Server%20SDK)中包含了一个 REST API 调试工具：TimRestApiGear.php。您可以通过该工具在服务器上发起简单 REST API 调用。使用案例参见 [这里](/doc/product/269/服务端集成指引#.E5.88.9B.E5.BB.BA.E4.B8.80.E4.B8.AA.E7.BE.A4.E7.BB.84.EF.BC.8C.E5.8C.85.E5.90.AB.E5.88.9D.E5.A7.8B.E7.BE.A4.E6.88.90.E5.91.98.EF.BC.88.E4.BD.BF.E7.94.A8php-server-sdk.E4.B8.AD.E7.9A.84.E5.B7.A5.E5.85.B7.EF.BC.89)。

## Server SDK 集成
### PHP Server SDK
[PHP Server SDK](/doc/product/269/PHP%20Server%20SDK)将一些常用的 REST API 封装成了函数，并以接口类的方式暴露给开发者。

## FAQ
### REST 请求有概率超时，收不到任何响应

（1）IM 后台 REST 接口设置的超时时间是 3s，调用方设置的超时时间应该长于 3s。
（2）telnet yun.tim.qq.com 443 确认能否连接服务端口。
（3）使用 curl -G https://yun.tim.qq.com 简单测试确认能够收到响应。
（4）确认机器的 dns server 配置是内网 dns server，还是公共 dns server。如果是内网 dns server，请确保 dns server 网络出口和本机器网络出口 IP 所在地域运营商一致。
（5）建议业务调用方使用“长连接+连接池”模式。
