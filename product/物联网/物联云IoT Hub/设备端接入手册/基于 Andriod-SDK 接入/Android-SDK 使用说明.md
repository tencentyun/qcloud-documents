
Andriod SDK 在提供设备的接入功能之外，还提供了网关子设备，设备影子，OTA 等功能。相关功能接口描述如下。

###  MQTT 接口  

#### TXMqttConnection

| 方法名                       | 说明                             |
| ---------------------------- | -------------------------------- |
| connect                      | MQTT 连接                        |
| reconnect                    | MQTT 重连                        |
| disConnect                   | 断开 MQTT 连接                    |
| publish                      | 发布 MQTT 消息                   |
| subscribe                    | 订阅 MQTT 主题                   |
| unSubscribe                  | 取消订阅 MQTT 主题               |
| getConnectStatus             | 获取 MQTT 连接状态               |
| setBufferOpts                | 设置断连状态 buffer 缓冲区       |
| initOTA                      | 初始化 OTA 功能                  |
| reportCurrentFirmwareVersion | 上报设备当前版本信息到后台服务器 |
| reportOTAState               | 上报设备升级状态到后台服务器     |


### MQTT 网关接口 

#### TXGatewayConnection

| 方法名                       | 说明                             |
| ---------------------------- | -------------------------------- |
| connect                      | 网关连接                        |
| reconnect                    | 网关重连                        |
| disConnect                   | 断开网关 MQTT 连接              |
| publish                      | 发布 MQTT 消息                   |
| subscribe                    | 订阅 MQTT 主题                   |
| unSubscribe                  | 取消订阅 MQTT 主题               |
| getConnectStatus             | 获取 MQTT 连接状态               |
| setBufferOpts                | 设置断连状态 buffer 缓冲区       |
| initOTA                      | 初始化 OTA 功能                  |
| reportCurrentFirmwareVersion | 上报设备当前版本信息到后台服务器 |
| reportOTAState               | 上报设备升级状态到后台服务器     |
| addSubDev                    | 添加子设备                       |
| removeSubdev                 | 移除子设备                       |
| findSubdev                   | 查找子设备                       |
| gatewaySubdevOffline         | 子设备下线                       |
| gatewaySubdevOnline          | 子设备上线                       |


###  设备影子接口 

#### TXShadowConnection

| 方法名                | 说明                                     |
| --------------------- | ---------------------------------------- |
| connect               | Shadow 连接                              |
| disConnect            | 关闭 Shadow 连接                         |
| getConnectStatus      | 获取 MQTT 连接状态                       |
| update                | 更新设备影子文档                         |
| get                   | 获取设备影子文档                         |
| registerProperty      | 注册设备属性                             |
| unRegisterProperty    | 取消注册设备属性                         |
| reportNullDesiredInfo | 更新 delta 信息后，上报空的 desired 信息 |
| setBufferOpts         | 设置断连状态 buffer 缓冲区               |
| getMqttConnection     | 获取 TXMqttConnection 实例               |

### MQTT 远程服务客户端 

#### TXMqttClient

| 方法名                | 说明                       |
| --------------------- | -------------------------- |
| setMqttActionCallBack | 设置 MqttAction 回调接口   |
| setServiceConnection  | 设置远程服务连接回调接口   |
| init                  | 初始化远程服务客户端       |
| startRemoteService    | 开启远程服务               |
| stopRemoteService     | 停止远程服务               |
| connect               | MQTT 连接                  |
| disConnect            | 断开 MQTT 连接             |
| subscribe             | 订阅 MQTT 主题             |
| unSubscribe           | 取消订阅 MQTT 主题         |
| publish               | 发布 MQTT 消息             |
| setBufferOpts         | 设置断连状态 buffer 缓冲区 |
| clear                 | 释放资源                   |

### Shadow 远程服务客户端 

#### TXShadowClient

| 方法名                  | 说明                                     |
| ----------------------- | ---------------------------------------- |
| setShadowActionCallBack | 设置 ShadowAction 回调接口               |
| setServiceConnection    | 设置远程服务连接回调接口                 |
| init                    | 初始化远程服务客户端                     |
| startRemoteService      | 开启远程服务                             |
| stopRemoteService       | 停止远程服务                             |
| connect                 | Shadow 连接                              |
| disConnect              | 断开 Shadow 连接                         |
| getMqttClient           | 获取 MQTT 客户端实                       |
| get                     | 获取设备影子                             |
| update                  | 更新设备影子                             |
| registerProperty        | 注册设备属性                             |
| unRegisterProperty      | 取消注册设备属性                         |
| reportNullDesiredInfo   | 更新 delta 信息后，上报空的 desired 信息 |
| setBufferOpts           | 设置断连状态 buffer 缓冲区               |
| clear                   | 释放资源                                 |

### MQTT 通道固件升级 

#### TXMqttClient

| 方法名                       | 说明                             |
| ---------------------------- | -------------------------------- |
| initOTA                      | 初始化 OTA 功能                  |
| reportCurrentFirmwareVersion | 上报设备当前版本信息到后台服务器 |
| reportOTAState               | 上报设备升级状态到后台服务器     |
