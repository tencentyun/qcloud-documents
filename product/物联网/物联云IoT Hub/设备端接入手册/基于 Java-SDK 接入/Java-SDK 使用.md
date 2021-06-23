
Java SDK 除提供设备的接入功能之外，还提供网关子设备，设备影子等功能。相关功能接口如下。

## MQTT 接口 

MQTT 的相关接口定义在 TXMqttConnection 类中，支持发布和订阅功能；如果需支持设备影子功能，则需使用 TXShadowConnection 类及其方法，TXMqttConnection 类接口，介绍如下：

| 方法名           | 说明                     |
| ---------------- | ------------------------ |
| connect          | MQTT 连接                 |
| reconnect        | MQTT 重连                 |
| disConnect       | 断开 MQTT 连接             |
| publish          | 发布 MQTT 消息             |
| subscribe        | 订阅 MQTT 主题             |
| unSubscribe      | 取消订阅 MQTT 主题         |
| getConnectStatus | 获取 MQTT 连接状态         |
| setBufferOpts    | 设置断连状态 buffer 缓冲区 |


## MQTT 网关接口 

- 对于无法直接接入以太网网络的设备，可先接入本地网关设备的网络，利用网关设备的通信功能，将代理设备接入 IoT Hub 平台。
- 对于局域网中加入或退出网络的子设备，需通过平台进行绑定或解绑操作。

>!当子设备发起过上线，后续只要网关链接成功，后台就会显示子设备在线，除非设备已发起下线操作。
>
MQTT 网关的相关接口定义在 TXGatewayConnection 类接口中，介绍如下：

| 方法名               | 说明                     |
| -------------------- | ------------------------ |
| connect              | 网关 MQTT 连接             |
| reconnect            | 网关 MQTT 重连             |
| disConnect           | 断开网关 MQTT 连接         |
| publish              | 发布 MQTT 消息             |
| subscribe            | 订阅 MQTT 主题             |
| unSubscribe          | 取消订阅 MQTT 主题         |
| getConnectStatus     | 获取 MQTT 连接状态         |
| setBufferOpts        | 设置断连状态 buffer 缓冲区 |
| gatewaySubdevOffline | 子设备下线               |
| gatewaySubdevOnline  | 子设备上线               |
| gatewayBindSubdev    | 子设备绑定               |
| gatewayUnbindSubdev  | 子设备解绑               |

## 设备影子接口

如果需要支持设备影子功能，需使用 TXShadowConnection 类中的接口，介绍如下：

| 方法名                | 说明                                 |
| --------------------- | ------------------------------------ |
| connect               | MQTT 连接                             |
| reconnect             | MQTT 重连                             |
| disConnect            | 断开 MQTT 连接                         |
| publish               | 发布 MQTT 消息                         |
| subscribe             | 订阅 MQTT 主题                         |
| unSubscribe           | 取消订阅 MQTT 主题                     |
| update                | 更新设备影子文档                     |
| get                   | 获取设备影子文档                     |
| reportNullDesiredInfo | 更新 delta 信息后，上报空的 desired 信息 |
| setBufferOpts         | 设置断连状态 buffer 缓冲区             |
| getMqttConnection     | 获取 TXMqttConnection 实例             |
| getConnectStatus      | 获取 MQTT 连接状态                     |
