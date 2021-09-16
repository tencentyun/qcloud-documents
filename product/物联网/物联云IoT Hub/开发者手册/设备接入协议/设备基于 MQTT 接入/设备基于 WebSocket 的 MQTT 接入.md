

## MQTT-WebSocket 概述

物联网平台支持基于 WebSocket 的 MQTT 通信，设备可以在 WebSocket 协议的基础之上使用 MQTT 协议进行消息的传输。从而使基于浏览器的应用可以实现与平台及与平台连接的设备之间的数据通信。同时 WebSocket 采用443/80端口，消息传输时可以穿过大多数防火墙。

## MQTT-WebSocket 接入

由于 MQTT-WebSocket 协议与 MQTT-TCP 协议最终都是基于 MQTT 进行消息的传输，所以这两种协议在 MQTT 接入参数上是相同的，区别主要在于 MQTT 连接平台的协议及端口。密钥认证的设备采用 WS 的方式进行接入，证书认证的设备采用 WSS 的方式接入，即 WS+TLS。

#### 证书认证设备接入指引

1. 下载证书、设备私钥等文件。
2. 连接域名：广州域设备需连接，`${ProductId}.ap-guangzhou.iothub.tencentdevices.com:443`，其中 ${ProductId} 为变量参数产品 ID。
3. MQTT 连接参数设置：
连接参数设置与 MQTT-TCP 接入时一致，具体信息请参见 [设备基于 TCP 的 MQTT 接入](https://cloud.tencent.com/document/product/634/32546#mqtt-.E6.8E.A5.E5.85.A5) 文档中的 MQTT 接入章节。
```plaintext
UserName:${productid}${devicename};${sdkappid};${connid};${expiry}
PassWord:密码。(可设置任意值)
ClientId:${ProductId}${DeviceName}
KeepAlive:保持连接的时间，取值范围为0 - 900s
```


#### 密钥认证设备接入指引
1. 获取设备密钥。
2. 连接域名：广州域设备需连接，`${ProductId}.ap-guangzhou.iothub.tencentdevices.com:80`，其中 ${ProductId} 为变量参数产品 ID。
3. MQTT 连接参数设置：
连接参数设置与 MQTT-TCP 接入时一致，具体信息请参见 [设备基于 TCP 的 MQTT 接入](https://cloud.tencent.com/document/product/634/32546#.E5.AF.86.E9.92.A5.E8.AE.A4.E8.AF.81.E8.AE.BE.E5.A4.87.E6.8E.A5.E5.85.A5.E6.8C.87.E5.BC.95) 文档中的密钥设备接入指引章节。
```plaintext
UserName:${productid}${devicename};${sdkappid};${connid};${expiry}
PassWord:${token};hmac 签名方法
ClientId:${ProductId}${DeviceName}
KeepAlive:保持连接的时间，取值范围为0 - 900s
```



