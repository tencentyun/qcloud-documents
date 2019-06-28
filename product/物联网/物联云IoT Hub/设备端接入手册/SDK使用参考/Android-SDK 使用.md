

对设备端 SDK 的使用分以下两种情况：   
- 若 App 与 IoT-SDK 在同一进程中运行，则 App 只需依赖 iot_core 模块即可。
- 若 App 与 IoT-SDK 需运行在不同进程，则 App 只需依赖 iot_service 模块即可。

>!
- iot_service 模块依赖 iot_core 模块。
- iot_core 依赖开源社区实现的 mqtt 协议 **eclipse.paho**。

## SDK API 说明

###  MQTT 接口  
#### TXMqttConnection

| 序号  | 方法名                        | 说明                                |
| ---- | ---------------------------- | -----------------------------------|
| 1    | connect                      |  MQTT 连接                          |
| 2    | reconnect                    |  MQTT 重连                          |
| 3    | disConnect                   |  断开 MQTT连接                       |
| 4    | publish                      |  发布 MQTT 消息                      |
| 5    | subscribe                    |  订阅 MQTT 主题                      |
| 6    | unSubscribe                  |  取消订阅 MQTT 主题                   |
| 7    | getConnectStatus             |  获取 MQTT 连接状态                   |
| 8    | setBufferOpts                |  设置断连状态 buffer 缓冲区              |
| 9    | initOTA                      |  初始化 OTA 功能                        |
| 10   | reportCurrentFirmwareVersion |  上报设备当前版本信息到后台服务器        |
| 11   | reportOTAState               |  上报设备升级状态到后台服务器            |


### MQTT 网关接口 
#### TXGatewayConnection

| 序号  | 方法名                        | 说明                                |
| ---- | ---------------------------- | -----------------------------------|
| 1    | connect                      |  网关 连接                          |
| 2    | reconnect                    |  网关 重连                          |
| 3    | disConnect                   |  断开 网关MQTT连接                       |
| 4    | publish                      |  发布 MQTT 消息                      |
| 5    | subscribe                    |  订阅 MQTT 主题                      |
| 6    | unSubscribe                  |  取消订阅 MQTT 主题                   |
| 7    | getConnectStatus             |  获取 MQTT 连接状态                   |
| 8    | setBufferOpts                |  设置断连状态 buffer 缓冲区              |
| 9    | initOTA                      |  初始化 OTA 功能                        |
| 10   | reportCurrentFirmwareVersion |  上报设备当前版本信息到后台服务器        |
| 11   | reportOTAState               |  上报设备升级状态到后台服务器            |
| 12   | addSubDev                    |  添加子设备                            |
| 13   | removeSubdev                 |  移除子设备                            |
| 14   | findSubdev                   |  查找子设备                            |
| 15   | gatewaySubdevOffline         |  子设备下线                           |
| 16   | gatewaySubdevOnline          |  子设备上线                           |


###  设备影子接口 
#### TXShadowConnection

| 序号  | 方法名                              | 说明                                 |
| ---- | -----------------------------------| ----------------------------------  |
| 1    | connect                            | Shadow 连接                          |
| 2    | disConnect                         | 关闭 Shadow 连接                      |
| 3    | getConnectStatus                   | 获取 mqtt 连接状态                     |
| 4    | update                             | 更新设备影子文档                        |
| 5    | get                                | 获取设备影子文档                        |
| 6    | registerProperty                   | 注册设备属性                           |
| 7    | unRegisterProperty                 | 取消注册设备属性                        |
| 8    | reportNullDesiredInfo              | 更新 delta 信息后，上报空的 desired 信息 |
| 9    | setBufferOpts                      | 设置断连状态 buffer 缓冲区              |
| 10   | getMqttConnection                  | 获取 TXMqttConnection 实例            |

### MQTT 远程服务客户端 
#### TXMqttClient

| 序号  | 方法名                              | 说明                             |
| ---- | -----------------------------------| -------------------------------- |
| 1    | setMqttActionCallBack              | 设置 MqttAction 回调接口             |
| 2    | setServiceConnection               | 设置远程服务连接回调接口             |
| 3    | init                               | 初始化远程服务客户端                |
| 4    | startRemoteService                 | 开启远程服务                       |
| 5    | stopRemoteService                  | 停止远程服务                       |
| 6    | connect                            | MQTT 连接                        |
| 7    | disConnect                         | 断开 MQTT 连接                    |
| 8    | subscribe                          | 订阅 MQTT 主题                    |
| 9    | unSubscribe                        | 取消订阅 MQTT 主题                 |
| 10    | publish                            | 发布 MQTT 消息                    |
| 11   | setBufferOpts                      | 设置断连状态 buffer 缓冲区          |
| 12   | clear                              | 释放资源                          |

### Shadow 远程服务客户端 
#### TXShadowClient

| 序号  | 方法名                              | 说明                                  |
| ---- | -----------------------------------| -----------------------------------   |
| 1    | setShadowActionCallBack            | 设置 ShadowAction 回调接口              |
| 2    | setServiceConnection               | 设置远程服务连接回调接口                  |
| 3    | init                               | 初始化远程服务客户端                     |
| 4    | startRemoteService                 | 开启远程服务                            |
| 5    | stopRemoteService                  | 停止远程服务                            |
| 6    | connect                            | Shadow 连接                           |
| 7    | disConnect                         | 断开 Shadow 连接                       |
| 8    | getMqttClient                      | 获取 MQTT 客户端实                      |
| 9    | get                                | 获取设备影子                            |
| 10   | update                             | 更新设备影子                            |
| 11   | registerProperty                   | 注册设备属性                            |
| 12   | unRegisterProperty                 | 取消注册设备属性                         |
| 13   | reportNullDesiredInfo              | 更新 delta 信息后，上报空的 desired 信息  |
| 14   | setBufferOpts                      | 设置断连状态 buffer 缓冲区               |
| 15   | clear                              | 释放资源                               |

### MQTT 通道固件升级 
#### TXMqttClient

| 序号  | 方法名                              | 说明                             |
| ---- | -----------------------------------| -------------------------------- |
| 1   | initOTA                            |  初始化 OTA 功能                     |
| 2   | reportCurrentFirmwareVersion       |  上报设备当前版本信息到后台服务器     |
| 3   | reportOTAState                     |  上报设备升级状态到后台服务器         |
