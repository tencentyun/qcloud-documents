REST API 是即时通信 IM 提供给 App 后台的 HTTP 管理接口，其主要目的在于为 App 后台提供一个后台管理入口。目前即时通信 IM 支持的 REST API 请参见 [REST API 接口列表](https://cloud.tencent.com/document/product/269/1520)。
除了 REST API，App 控制台也可实现简单的数据管理、单发/群发消息，开发者可以在控制台进行简单的数据管理、查看及测试。相比之下，REST API 接口较为原始，但管理能力却更为强大。
为了安全性，REST API 仅提供 HTTPS 接口。
以下视频将帮助您快速了解即时通信 IM 的 REST API 接口：
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2543-43220?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 前提条件
要调用 REST API，您必须已完成：
1. 在即时通信 IM 控制台创建 App，具体方法参见 [应用接入指引](https://cloud.tencent.com/document/product/269/32577)。
2. 为您的 App 指定管理员帐号，具体方法参见 [基础配置](https://cloud.tencent.com/document/product/269/32578) 的帐号体系集成。

>!调用 REST API 时请务必使用 App 管理员帐号，否则会导致不必要的调用错误。

## 调用方法
### 请求 URL

REST API 的 URL 格式如下：
```
https://console.tim.qq.com/$ver/$servicename/$command?sdkappid=$SDKAppID&identifier=$identifier&usersig=$usersig&random=99999999&contenttype=json
```
其中各个参数的含义以及取值如下（参数名称及其取值均区分大小写）：

| 参数  | 含义  | 取值  |
|---------|---------|---------|
| https    |请求协议      | 请求协议为 HTTPS，请求方式为 POST       |
| console.tim.qq.com |请求域名  | 固定为`console.tim.qq.com`      |
| ver  | 协议版本号 | 固定为`v4`  |
| servicename  | 内部服务名，不同的 servicename 对应不同的服务类型 |示例：<br>`v4/im_open_login_svc/account_import`，其中`im_open_login_svc`为`servicename`<br/>更多详情请参见 [REST API 接口列表](https://cloud.tencent.com/document/product/269/1520) |
| command  | 命令字，与 servicename 组合用来标识具体的业务功能 |示例：<br>`v4/im_open_login_svc/account_import`，其中`account_import`为`command`<br/>更多详情请参见 [REST API 接口列表](https://cloud.tencent.com/document/product/269/1520) |
| sdkappid  | App 在即时通信 IM 控制台获取的应用标识 |在申请接入时获得 |
| identifier  | 用户名，调用 REST API 时必须为 App 管理员帐号 |参见 [App 管理员](https://cloud.tencent.com/document/product/269/31999#app-.E7.AE.A1.E7.90.86.E5.91.98)  |
| usersig  | 用户名对应的密码 |参见 [生成 UserSig](https://cloud.tencent.com/document/product/269/32688) |
| random  | 标识当前请求的随机数参数 |32位无符号整数随机数，取值范围0 - 4294967295 |
| contenttype   |请求格式     | 固定值为`json`                   |

>!
>- App 服务端在调用 REST API 时，identifier 必须为 App 管理员帐号。
>- App 可以在每次调用 REST API 时都生成管理员帐号的 UserSig，亦可生成一个固定的 UserSig 重复使用，但请特别注意 UserSig 的有效期。

### HTTP 请求包体格式
REST API 仅支持 POST 方法，其请求包体为 JSON 格式，具体的包体格式参见每个 API 的详细描述。
需要特别注意的是，POST 包体不能为空，即使某条协议包体中不需要携带任何信息，也需要携带一个空的 JSON 对象，即`{}`。

### HTTP 返回码
除非发生网络错误（例如502错误），否则 REST API 的调用结果均为200，真正的 API 调用错误码与错误信息在 HTTP 应答包体中返回。

### HTTP 应答包体格式
REST API 的应答包体也是 JSON 格式，其格式符合如下特征：
```
{
    "ActionStatus": "OK", 
    "ErrorInfo": "", 
    "ErrorCode": 0
    // REST API 其他应答内容
}
```
应答包体中必然包含 ActionStatus、ErrorInfo、ErrorCode 这三个属性，其含义如下：

| 字段 | 类型| 说明 |
|---------|---------|---------|
|ActionStatus | String | 请求处理的结果，OK 表示处理成功，FAIL 表示失败，如果为 FAIL，ErrorInfo 带上失败原因 |
|ErrorInfo  | String | 失败原因 |
|ErrorCode  | Integer | 错误码，0为成功，其他为失败，可查询 [错误码表](https://cloud.tencent.com/document/product/269/1671) 得到具体的原因 |

## 调用示例
以下为通过 REST API 来 [获取 App 中所有群组](https://cloud.tencent.com/document/product/269/1614) 示例。

HTTPS 请求：
```
POST /v4/group_open_http_svc/get_appid_group_list?usersig=xxx&identifier=admin&sdkappid=88888888&random=99999999&contenttype=json HTTP/1.1
Host: console.tim.qq.com
Content-Length: 22
{
    "Limit": 2
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

## REST API 公共错误码

| 错误码 |含义说明|
|---------|---------|
| 80001 | 消息文本安全打击 |
| 60002 | HTTP 解析错误 ，请检查 HTTP 请求 URL 格式 |
| 60003 | HTTP 请求 JSON 解析错误，请检查 JSON 格式 |
| 60004 | 请求 URL 或 JSON 包体中帐号或签名错误 |
| 60005 | 请求 URL 或 JSON 包体中帐号或签名错误 |
| 60006 | SDKAppID 失效，请核对 SDKAppID 有效性 |
| 60007 | REST 接口调用频率超过限制，请降低请求频率 |
| 60008 | 服务请求超时或 HTTP 请求格式错误，请检查并重试 |
| 60009 | 请求资源错误，请检查请求 URL |
| 60010 | 请求需要 App 管理员权限 |
| 60011 | SDKAppID 请求频率超限，请降低请求频率 |
| 60012 | REST 接口需要带 SDKAppID，请检查请求 URL 中的 SDKAppID |
| 60013 | HTTP 响应包 JSON 解析错误 |
| 60014 | 置换帐号超时 |
| 60015 | 请求包体帐号类型错误，请确认帐号为字符串格式 |
| 60016  | SDKAppID 被禁用。                  |
| 60017  | 请求被禁用。              |
| 60018  | 请求过于频繁，请稍后重试。                                   |
| 60019  | 请求过于频繁，请稍后重试。                                   |
| 60020  | 您的专业版套餐包已到期并停用，请登录 [即时通信 IM 购买页面](https://buy.cloud.tencent.com/avc) 重新购买套餐包。购买后，将在5分钟后生效。 |
|60021  |RestAPI 调用来源 IP 非法。|

## FAQ
### REST API 请求有概率超时，收不到任何响应

1. 即时通信 IM 后台 REST 接口设置的超时时间是 3s，调用方设置的超时时间应该长于 3s。
2. telnet console.tim.qq.com 443 确认能否连接服务端口。
3. 使用 curl -I https://console.tim.qq.com 简单测试看状态码是否为200。
4. 确认机器的 dns server 配置是内网 dns server，还是公共 dns server。如果是内网 dns server，请确保 dns server 网络出口和本机器网络出口 IP 所在地域运营商一致。
5. 建议业务调用方使用“长连接+连接池”模式。
>?由于 HTTPS 短连接建连耗时比较大，每次请求都有TCP + tls 握手开销，所以建议 REST API 长连接接入。
使用标准 HTTP 库的场景：HTTP1.0 需要指定请求头部 Connection: keep-alive，HTTP1.1 默认支持长连接；基于 TCP 封装 HTTPS 请求的场景，可以复用 TCP 连接来收发请求。

