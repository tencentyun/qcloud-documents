## 功能概述

NTP 服务主要是解决资源受限的设备，系统不包含 NTP 服务，没有精确时间戳的问题。实现此类功能需利用以下两个 Topic：
- 请求 Topic（用于发布）：`$sys/operation/${ProductId}/${DeviceName}`。
- 响应 Topic（用于订阅）：`$sys/operation/result/${ProductId}/${DeviceName}`。

## 实现原理

物联网通信平台借鉴 NTP 协议原理，将平台作为 NTP 服务器。设备端向平台请求时，平台返回的 NTP 时间。设备端收到返回后，再结合请求时间和接收时间，一起计算出当前精确时间。

### 操作步骤
1. 设备端通过 MQTT 协议发布一条消息到 `$sys/operation/${ProductId}/${DeviceName}`，请求平台下发 NTP 时间，同时设备端记录请求时间 deviceSendtime，请求消息为 json 格式，内容如下：
```json
{
		 "type": "get",
		 "resource": [
		  "time"
		 ]
}
```
2. 平台通过 `$sys/operation/result/${ProductId}/${DeviceName}` 返回 NTP 时间，同时设备端记录接收时间 deviceRecvtime，返回消息为 json 格式，内容如下：
```
{
		 "type": "get",
		 "time": 1621562342,
		 "ntptime1": 1621562342773,
		 "ntptime2": 1621562342773
}
```
3. 通过设备端收到的 NTP 时间（${ntptime1} + ${ntptime2}）、接收时间（${deviceRecvtime}）和请求时间（${deviceSendtime}），一起计算精确时间，方法如下：
**精确时间 =(${ntptime1} + ${ntptime2} + ${deviceRecvtime} - ${deviceSendtime}) / 2**

