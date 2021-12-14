事件回调服务支持将实时音视频业务下的事件，以 HTTP/HTTPS 请求的形式通知到您的服务器。事件回调服务已集成房间事件组（Room Event）和媒体事件组（Media Event）下的一些事件，您可以向腾讯云提供相关的配置信息来开通该服务。

[](id:deploy)
## 配置信息
实时音视频 TRTC 控制台支持自助配置回调信息，配置完成后即可接收事件回调通知。详细操作指引请参见 [回调配置](https://cloud.tencent.com/document/product/647/52428)。


>!您需要提前准备以下信息：
>- **必要项**：接收回调通知的 HTTP/HTTPS 服务器地址。
>- **可选项**：计算签名的密钥 key，由您自定义一个最大32个字符的 key，以大小写字母及数字组成。

## 超时重试
事件回调服务器在发送消息通知后，5秒内没有收到您的服务器的响应，即认为通知失败。首次通知失败后会立即重试，后续失败会以**10秒**的间隔继续重试，直到消息存续时间超过1分钟，不再重试。

[](id:format)
## 事件回调消息格式

事件回调消息以 HTTP/HTTPS POST 请求发送给您的服务器，其中：

- **字符编码格式**：UTF-8。
- **请求**：body 格式为 JSON。
- **应答**：HTTP STATUS CODE = 200，服务端忽略应答包具体内容，为了协议友好，建议客户应答内容携带 JSON： {"code":0}。
- **包体示例**：下述为“房间事件组-进入房间”事件的包体示例。
<dx-codeblock>
::: JSON JSON
{
    "EventGroupId": 1,                #房间事件组
    "EventType": 103,                 #进入房间事件
    "CallbackTs": 1615554923704,      #回调时间，单位毫秒
    "EventInfo": {
        "RoomId": 12345,                #数字房间号
        "EventTs": 1615554922,          #事件发生时间，单位秒
        "UserId": "test",               #用户ID
        "UniqueId": 1615554922656,      #唯一标识符
        "Role": 20,                     #用户角色，主播
        "TerminalType": 3,        #终端类型，IOS端
        "UserType": 3,        #用户类型，Native SDK
        "Reason": 1        #进房原因，正常进房
	}
}
:::
</dx-codeblock>



## 参数说明
[](id:message)
### 回调消息参数

- 事件回调消息的 header 中包含以下字段：
<table id="header">
<tr><th>字段名</th><th>值</th></tr></thead><tr>
<td>Content-Type</td><td>application/json</td>
</tr><tr>
<td>Sign</td><td>签名值</td>
</tr><tr>
<td>SdkAppId</td><td>sdk application id</td>
</tr></table>
- 事件回调消息的 body 中包含以下字段：
<table id="body">
<tr><th>字段名</th><th>类型</th><th>含义</th>
</tr><tr>
<td>EventGroupId</td><td>Number</td>
<td><a href="#eventId">事件组 ID</a></td>
</tr><tr>
<td>EventType</td>
<td>Number</td>
<td><a href="#event_type">回调通知的事件类型</a></td>
</tr><tr>
<td>CallbackTs</td>
<td>Number</td>
<td>事件回调服务器向您的服务器发出回调请求的 Unix 时间戳，单位为毫秒</td>
</tr><tr>
<td>EventInfo</td>
<td>JSON Object</td>
<td><a href="#event_infor">事件信息</a></td>
</tr>
</tbody></table>

[](id:eventId)
### 事件组 ID

| 字段名            | 值   | 含义       |
| ----------------- | ---- | ---------- |
| EVENT_GROUP_ROOM  | 1    | 房间事件组 |
| EVENT_GROUP_MEDIA | 2    | 媒体事件组 |

[](id:event_type)
### 事件类型

| 字段名                  | 值   | 含义             |
| ----------------------- | ---- | ---------------- |
| EVENT_TYPE_CREATE_ROOM  | 101  | 创建房间         |
| EVENT_TYPE_DISMISS_ROOM | 102  | 解散房间         |
| EVENT_TYPE_ENTER_ROOM   | 103  | 进入房间         |
| EVENT_TYPE_EXIT_ROOM    | 104  | 退出房间         |
|  EVENT_TYPE_CHANGE_ROLE   | 105  |    切换角色      |
| EVENT_TYPE_START_VIDEO  | 201  | 开始推送视频数据 |
| EVENT_TYPE_STOP_VIDEO   | 202  | 停止推送视频数据 |
| EVENT_TYPE_START_AUDIO  | 203  | 开始推送音频数据 |
| EVENT_TYPE_STOP_AUDIO   | 204  | 停止推送音频数据 |
| EVENT_TYPE_START_ASSIT  | 205  | 开始推送辅路数据 |
| EVENT_TYPE_STOP_ASSIT   | 206  | 停止推送辅路数据 |

[](id:event_infor)
### 事件信息



| 字段名  | 类型   | 含义                              |
| ------- | ------ | --------------------------------- |
|RoomId      |     String/Number       |     房间名（类型与客户端房间号类型一致）    |
|EventTs      |    Number     |      事件发生的 Unix 时间戳，单位为秒（兼容保留）|
|EventMsTs    |     Number     |     事件发生的 Unix 时间戳，单位为毫秒  |
| UserId  | String | 用户 ID                            |
| UniqueId  | Number | 唯一标识符（option：房间事件组携带） [](id:UniqueId)<br>当客户端发生了一些特殊行为，例如切换网络、进程异常退出及重进等，此时您的回调服务器可能会收到同一个用户多次进房和退房回调，UniqueId 可用于标识用户的同一次进退房                            |
| Role    | Number | [角色类型](#role_type)（option：进退房时携带）  |
|TerminalType  |  Number    |   [终端类型](#terminal)（option：进房时携带）|
|UserType  |  Number   |    [用户类型](#usertype)（option：进房时携带）|
| Reason  | Number | [具体原因](#reason) （option：进退房时携带） |


>! 我们已发布“过滤客户端特殊行为导致的重复回调”策略。如果您是2021年07月30日之后接入回调服务，默认走新策略，房间事件组不再携带 [UniqueId](#UniqueId)（唯一标识符）。


[](id:role_type)
### 角色类型

| 字段名             | 值   | 含义 |
| ------------------ | ---- | ---- |
| MEMBER_TRTC_ANCHOR | 20   | 主播 |
| MEMBER_TRTC_VIEWER | 21   | 观众 |


[](id:terminal)
### 终端类型
| 字段名             | 值   | 含义 |
| ------------------ | ---- | ---- |
| TERMINAL_TYPE_WINDOWS | 1 | Windows 端   |
| TERMINAL_TYPE_ANDROID | 2  | Android 端 |
| TERMINAL_TYPE_IOS | 3  | iOS 端 |
| TERMINAL_TYPE_LINUX | 4  | Linux 端 |
| TERMINAL_TYPE_OTHER | 100  | 其他 |

[](id:usertype)
### 用户类型
| 字段名             | 值   | 含义 |
| ------------------ | ---- | ---- |
| USER_TYPE_WEBRTC | 1 | webrtc   |
| USER_TYPE_APPLET | 2  | 小程序 |
| USER_TYPE_NATIVE_SDK | 3  | Native SDK |


[](id:reason)
### 具体原因

| 字段名    | 含义                              |
| -------  | --------------------------------- |
|进房   |<li/>1：正常进房<li/>2：切换网络<li/>3：超时重试<li/>4：跨房连麦进房 |
|退房 | <li/>1：正常退房<li/>2：超时离开<li/>3：房间用户被移出<li/>4：取消连麦退房<li/>5：强杀|




### 计算签名
签名由 HMAC SHA256 加密算法计算得出，您的事件回调接收服务器收到回调消息后，通过同样的方式计算出签名，相同则说明是腾讯云的实时音视频的事件回调，没有被伪造。签名的计算如下所示：
```
//签名 Sign 计算公式中 key 为计算签名 Sign 用的加密密钥。
Sign = base64（hmacsha256(key, body)）
```

>! body 为您收到回调请求的原始包体，不要做任何转化，示例如下：
>```
body="{\n\t\"EventGroupId\":\t1,\n\t\"EventType\":\t103,\n\t\"CallbackTs\":\t1615554923704,\n\t\"EventInfo\":\t{\n\t\t\"RoomId\":\t12345,\n\t\t\"EventTs\":\t1608441737,\n\t\t\"UserId\":\t\"test\",\n\t\t\"UniqueId\":\t1615554922656,\n\t\t\"Role\":\t20,\n\t\t\"Reason\":\t1\n\t}\n}"
```
